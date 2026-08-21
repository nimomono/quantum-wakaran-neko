"""Stochastic integration of the explicit M45 local degrees of freedom."""

from __future__ import annotations

from dataclasses import asdict, dataclass

import numpy as np

from .model import (
    ModelParameters,
    active_force,
    potential_and_force,
    well_index,
)


@dataclass(frozen=True)
class SimulationParameters:
    paths: int = 512
    duration: float = 420.0
    burn_in: float = 180.0
    dt: float = 0.002
    sample_interval: float = 0.04
    confirmation_time: float = 0.50
    seed: int = 20260832
    hazard_min_energy: float = 0.18
    hazard_max_energy: float = 0.38
    hazard_bins: int = 60


def _initial_state(
    rng: np.random.Generator,
    simulation: SimulationParameters,
    model: ModelParameters,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    s = rng.normal(0.0, 0.08, size=simulation.paths)
    shifted = rng.normal(0.0, 0.35 * model.log_core, size=simulation.paths)
    r = shifted + model.shift_coupling * np.sin(s)
    initial_temperature = 0.010
    p_s = rng.normal(
        0.0,
        np.sqrt(model.structural_mass * initial_temperature),
        size=simulation.paths,
    )
    p_r = rng.normal(
        0.0,
        np.sqrt(model.log_mass * initial_temperature),
        size=simulation.paths,
    )
    return s, r, p_s, p_r


def simulate(
    simulation: SimulationParameters,
    model: ModelParameters,
    keep_trace: bool = True,
) -> dict[str, object]:
    """Integrate M45 without a prescribed slip rate or reset map."""
    rng = np.random.default_rng(simulation.seed)
    s, r, p_s, p_r = _initial_state(rng, simulation, model)

    steps = int(round(simulation.duration / simulation.dt))
    burn_steps = int(round(simulation.burn_in / simulation.dt))
    stride = max(1, int(round(simulation.sample_interval / simulation.dt)))
    confirmation_steps = max(
        1, int(round(simulation.confirmation_time / simulation.dt))
    )
    edges = np.linspace(
        simulation.hazard_min_energy,
        simulation.hazard_max_energy,
        simulation.hazard_bins + 1,
    )
    occupancy = np.zeros(simulation.hazard_bins)
    events = np.zeros(simulation.hazard_bins)

    pending_since = np.full(simulation.paths, np.nan)
    pending_recordable = np.zeros(simulation.paths, dtype=bool)
    ready_streak = np.zeros(simulation.paths, dtype=np.int32)
    previous_well = well_index(s)
    last_episode_time = np.full(simulation.paths, np.nan)

    ready_energy_samples: list[np.ndarray] = []
    ready_fraction_samples: list[float] = []
    ready_mean_samples: list[float] = []
    recovery_energies: list[np.ndarray] = []
    recovery_delays: list[np.ndarray] = []
    inter_episode_times: list[np.ndarray] = []
    event_energies: list[np.ndarray] = []
    recorded_crossings = 0
    recorded_episodes = 0
    recorded_recoveries = 0

    trace_time: list[float] = []
    trace_energy: list[float] = []
    trace_s: list[float] = []
    trace_r: list[float] = []
    active_power_samples: list[float] = []
    friction_power_samples: list[float] = []

    decay_s = np.exp(
        -model.gamma_s * simulation.dt / model.structural_mass
    )
    decay_r = np.exp(-model.gamma_r * simulation.dt / model.log_mass)
    noise_s = np.sqrt(
        model.structural_mass
        * model.bath_temperature
        * (1.0 - decay_s**2)
    )
    noise_r = np.sqrt(
        model.log_mass
        * model.bath_temperature
        * (1.0 - decay_r**2)
    )

    potential, force_s, force_r = potential_and_force(s, r, model)
    for step in range(steps):
        total_force_s = force_s + active_force(p_s, model)
        p_s += 0.5 * simulation.dt * total_force_s
        p_r += 0.5 * simulation.dt * force_r
        s += 0.5 * simulation.dt * p_s / model.structural_mass
        r += 0.5 * simulation.dt * p_r / model.log_mass

        p_s = decay_s * p_s + noise_s * rng.normal(size=simulation.paths)
        p_r = decay_r * p_r + noise_r * rng.normal(size=simulation.paths)

        s += 0.5 * simulation.dt * p_s / model.structural_mass
        r += 0.5 * simulation.dt * p_r / model.log_mass
        potential, force_s, force_r = potential_and_force(s, r, model)
        total_force_s = force_s + active_force(p_s, model)
        p_s += 0.5 * simulation.dt * total_force_s
        p_r += 0.5 * simulation.dt * force_r

        energy = (
            potential
            + 0.5 * p_s**2 / model.structural_mass
            + 0.5 * p_r**2 / model.log_mass
        )
        time = (step + 1) * simulation.dt
        current_well = well_index(s)
        crossings = np.abs(current_well - previous_well).astype(np.int32)
        slipped = crossings > 0
        pending_before = np.isfinite(pending_since)
        new_episode = slipped & ~pending_before

        if step >= burn_steps:
            indices = np.searchsorted(edges, energy, side="right") - 1
            available = ~pending_before
            valid = (
                (indices >= 0)
                & (indices < simulation.hazard_bins)
                & available
            )
            occupancy += (
                np.bincount(indices[valid], minlength=simulation.hazard_bins)
                * simulation.dt
            )
            recorded_crossings += int(np.sum(crossings))
            recorded_episodes += int(np.sum(new_episode))
            if np.any(new_episode):
                event_indices = np.searchsorted(
                    edges, energy[new_episode], side="right"
                ) - 1
                valid_events = (
                    (event_indices >= 0)
                    & (event_indices < simulation.hazard_bins)
                )
                events += np.bincount(
                    event_indices[valid_events],
                    minlength=simulation.hazard_bins,
                )
                event_energies.append(energy[new_episode].copy())

        if np.any(new_episode):
            previous_time = last_episode_time[new_episode]
            valid_previous = np.isfinite(previous_time)
            if step >= burn_steps and np.any(valid_previous):
                inter_episode_times.append(time - previous_time[valid_previous])
            last_episode_time[new_episode] = time
            pending_since[new_episode] = time
            pending_recordable[new_episode] = step >= burn_steps

        ready_streak[slipped] = 0
        pending = np.isfinite(pending_since)
        below_separatrix = energy < model.separatrix_energy
        ready_streak = np.where(
            pending & below_separatrix,
            ready_streak + 1,
            0,
        )
        recovered = pending & (ready_streak >= confirmation_steps)
        if np.any(recovered):
            recordable = recovered & pending_recordable
            if np.any(recordable):
                recovery_energies.append(energy[recordable].copy())
                recovery_delays.append(time - pending_since[recordable])
                recorded_recoveries += int(np.sum(recordable))
            pending_since[recovered] = np.nan
            pending_recordable[recovered] = False
            ready_streak[recovered] = 0

        previous_well = current_well
        if step >= burn_steps and (step - burn_steps) % stride == 0:
            ready_sector = ~np.isfinite(pending_since)
            ready_energy = energy[ready_sector].copy()
            ready_energy_samples.append(ready_energy)
            ready_fraction_samples.append(float(np.mean(ready_sector)))
            ready_mean_samples.append(
                float(np.mean(ready_energy)) if ready_energy.size else np.nan
            )
            velocity_s = p_s / model.structural_mass
            velocity_r = p_r / model.log_mass
            active_power_samples.append(
                float(
                    np.mean(
                        model.active_gain
                        * (1.0 - (velocity_s / model.active_speed) ** 2)
                        * velocity_s**2
                    )
                )
            )
            friction_power_samples.append(
                float(
                    np.mean(
                        model.gamma_s * velocity_s**2
                        + model.gamma_r * velocity_r**2
                    )
                )
            )
            if keep_trace:
                trace_time.append(time)
                trace_energy.append(float(energy[0]))
                trace_s.append(float(s[0]))
                trace_r.append(float(r[0]))

    def concatenate(values: list[np.ndarray]) -> np.ndarray:
        return np.concatenate(values) if values else np.empty(0)

    ready_energy = concatenate(ready_energy_samples)
    recovery_energy = concatenate(recovery_energies)
    recovery_delay = concatenate(recovery_delays)
    inter_episode = concatenate(inter_episode_times)
    event_energy = concatenate(event_energies)
    def finite_statistic(function: object, values: np.ndarray) -> float:
        if values.size == 0:
            return float("nan")
        return float(function(values))

    block_means = [
        float(np.nanmean(block))
        for block in np.array_split(np.asarray(ready_mean_samples), 4)
    ]
    centers = 0.5 * (edges[:-1] + edges[1:])
    hazard = np.divide(
        events,
        occupancy,
        out=np.full_like(occupancy, np.nan),
        where=occupancy > 0.0,
    )
    thermal_return = (
        model.gamma_s * model.bath_temperature / model.structural_mass
        + model.gamma_r * model.bath_temperature / model.log_mass
    )
    return {
        "simulation_parameters": asdict(simulation),
        "model_parameters": asdict(model),
        "ready_energy": ready_energy,
        "event_energy": event_energy,
        "recovery_energy": recovery_energy,
        "recovery_delay": recovery_delay,
        "inter_episode_time": inter_episode,
        "hazard_centers": centers,
        "hazard_rate": hazard,
        "hazard_occupancy": occupancy,
        "hazard_events": events,
        "trace": {
            "time": np.asarray(trace_time),
            "energy": np.asarray(trace_energy),
            "s": np.asarray(trace_s),
            "r": np.asarray(trace_r),
        },
        "energy_balance": {
            "mean_active_power": float(np.mean(active_power_samples)),
            "mean_friction_power": float(np.mean(friction_power_samples)),
            "ito_thermal_return": float(thermal_return),
            "mean_balance_residual": float(
                np.mean(active_power_samples)
                - np.mean(friction_power_samples)
                + thermal_return
            ),
        },
        "summary": {
            "mean_ready_energy": float(np.mean(ready_energy)),
            "std_ready_energy": float(np.std(ready_energy)),
            "median_ready_energy": float(np.median(ready_energy)),
            "ready_sector_fraction": float(np.mean(ready_fraction_samples)),
            "stationary_block_means": block_means,
            "near_separatrix_fraction": float(
                np.mean(
                    np.abs(ready_energy - model.separatrix_energy)
                    <= 0.5 * model.theta
                )
            ),
            "crossing_rate_per_path": float(
                recorded_crossings
                / (simulation.paths * (simulation.duration - simulation.burn_in))
            ),
            "episode_rate_per_path": float(
                recorded_episodes
                / (simulation.paths * (simulation.duration - simulation.burn_in))
            ),
            "recorded_crossings": recorded_crossings,
            "recorded_episodes": recorded_episodes,
            "recorded_recoveries": recorded_recoveries,
            "recovery_per_episode": float(
                recorded_recoveries / recorded_episodes
                if recorded_episodes else np.nan
            ),
            "mean_event_energy": finite_statistic(np.mean, event_energy),
            "mean_recovery_energy": finite_statistic(np.mean, recovery_energy),
            "std_recovery_energy": finite_statistic(np.std, recovery_energy),
            "median_recovery_delay": finite_statistic(np.median, recovery_delay),
            "median_inter_episode_time": finite_statistic(np.median, inter_episode),
        },
    }
