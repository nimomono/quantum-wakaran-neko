#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from math import erf, exp, factorial, log, pi, sqrt

import numpy as np


@dataclass
class CheckResult:
    name: str
    value: float
    threshold: float
    criterion: str
    passed: bool


def record_max(name: str, value: float, threshold: float) -> CheckResult:
    return CheckResult(name, float(value), float(threshold), "<=", bool(value <= threshold))


def record_min(name: str, value: float, threshold: float) -> CheckResult:
    return CheckResult(name, float(value), float(threshold), ">=", bool(value >= threshold))


def total_variation(first: np.ndarray, second: np.ndarray) -> float:
    return float(0.5 * np.sum(np.abs(first - second)))


def random_isometry(rng: np.random.Generator, rows: int) -> np.ndarray:
    matrix = rng.normal(size=(rows, 2)) + 1j * rng.normal(size=(rows, 2))
    q_matrix, _ = np.linalg.qr(matrix)
    return q_matrix[:, :2]


def action_capacities(
    isometry: np.ndarray,
    state: np.ndarray,
    action_unit: float,
    delta: float,
    reference: np.ndarray,
) -> tuple[float, np.ndarray, np.ndarray]:
    signal_action = action_unit * float(np.vdot(state, state).real)
    branch_actions = action_unit * np.abs(isometry @ state) ** 2
    capacities = branch_actions + delta * reference * signal_action
    return signal_action, branch_actions, capacities


def shell_count(capacity: np.ndarray, modes: int, reference_action: float) -> np.ndarray:
    return (
        (2.0 * pi) ** modes
        / factorial(modes - 1)
        * (capacity / reference_action) ** (modes - 1)
    )


def smooth_partition(capacity: np.ndarray, beta: float, stiffness: float) -> np.ndarray:
    a_value = 0.5 * beta * stiffness
    x_value = np.sqrt(a_value) * capacity
    error_function = np.array([erf(float(value)) for value in x_value])
    return (2.0 * pi) ** 2 * (
        np.exp(-(x_value**2)) / (2.0 * a_value)
        + capacity * sqrt(pi) / (2.0 * sqrt(a_value)) * (1.0 + error_function)
    )


def main() -> None:
    seed = 20260828
    rng = np.random.default_rng(seed)
    checks: list[CheckResult] = []

    support_ray = rng.normal(size=2) + 1j * rng.normal(size=2)
    support_ray /= np.linalg.norm(support_ray)
    amplitudes = rng.normal(size=4096) + 1j * rng.normal(size=4096)
    supported_samples = amplitudes[:, None] * support_ray[None, :]
    supported_covariance = supported_samples.T @ supported_samples.conj()
    supported_covariance /= np.trace(supported_covariance).real
    support_projector = np.outer(support_ray, support_ray.conj())
    perpendicular = np.eye(2) - support_projector
    checks.append(record_max(
        "rank_one_covariance_factor_error",
        np.linalg.norm(supported_covariance - support_projector),
        3.0e-14,
    ))
    checks.append(record_max(
        "rank_one_sample_support_error",
        np.max(np.linalg.norm(supported_samples @ perpendicular.T, axis=1)),
        3.0e-14,
    ))

    orthogonal_ray = np.array([-support_ray[1].conjugate(), support_ray[0].conjugate()])
    leakage = 0.07 * (rng.normal(size=4096) + 1j * rng.normal(size=4096))
    approximate_samples = supported_samples + leakage[:, None] * orthogonal_ray[None, :]
    approximate_covariance = approximate_samples.T @ approximate_samples.conj()
    total_action = np.trace(approximate_covariance).real
    approximate_covariance /= total_action
    support_trace_error = float(np.trace(perpendicular @ approximate_covariance).real)
    support_sample_error = float(
        np.sum(np.linalg.norm(approximate_samples @ perpendicular.T, axis=1) ** 2)
        / total_action
    )
    checks.append(record_max(
        "approximate_support_identity_error",
        abs(support_trace_error - support_sample_error),
        3.0e-14,
    ))

    size = 7
    isometry = random_isometry(rng, size)
    state = rng.normal(size=2) + 1j * rng.normal(size=2)
    action_unit = 1.73
    reference_action = 0.91
    delta = 0.037
    reference = rng.uniform(0.2, 1.0, size=size)
    reference /= np.sum(reference)

    signal_action, branch_actions, capacities = action_capacities(
        isometry,
        state,
        action_unit,
        delta,
        reference,
    )
    counts = shell_count(capacities, 2, reference_action)
    shell_target = counts / np.sum(counts)
    born_target = (
        branch_actions / signal_action + delta * reference
    ) / (1.0 + delta)

    checks.append(record_max(
        "isometry_orthonormality_error",
        np.linalg.norm(isometry.conj().T @ isometry - np.eye(2)),
        3.0e-14,
    ))
    checks.append(record_max(
        "signal_action_decomposition_error",
        abs(np.sum(branch_actions) - signal_action),
        3.0e-14,
    ))
    checks.append(record_max(
        "regularized_capacity_sum_error",
        abs(np.sum(capacities) - (1.0 + delta) * signal_action),
        3.0e-14,
    ))
    checks.append(record_min("regularized_capacity_minimum", np.min(capacities), 1.0e-12))

    phase = np.exp(1j * rng.uniform(-pi, pi))
    _, _, phase_capacities = action_capacities(
        isometry, phase * state, action_unit, delta, reference
    )
    checks.append(record_max(
        "capacity_common_phase_invariance_error",
        np.linalg.norm(phase_capacities - capacities),
        3.0e-14,
    ))

    amplitude = 2.31 * np.exp(0.37j)
    _, _, scaled_capacities = action_capacities(
        isometry, amplitude * state, action_unit, delta, reference
    )
    checks.append(record_max(
        "capacity_scale_covariance_error",
        np.linalg.norm(scaled_capacities - abs(amplitude) ** 2 * capacities),
        2.0e-13,
    ))
    supported_signal = amplitudes[0] * support_ray
    _, supported_branches, supported_capacities = action_capacities(
        isometry, supported_signal, action_unit, delta, reference
    )
    supported_target = supported_capacities / np.sum(supported_capacities)
    ray_signal, ray_branches, ray_capacities = action_capacities(
        isometry, support_ray, action_unit, delta, reference
    )
    ray_target = ray_capacities / np.sum(ray_capacities)
    checks.append(record_max(
        "single_trial_ray_weight_invariance_error",
        np.linalg.norm(supported_target - ray_target)
        + abs(np.sum(ray_branches) - ray_signal),
        4.0e-14,
    ))

    two_mode_expected = (2.0 * pi) ** 2 * capacities / reference_action
    checks.append(record_max(
        "two_action_shell_formula_error",
        np.linalg.norm(counts - two_mode_expected),
        3.0e-13,
    ))

    capacity_probe = np.array([0.31, 0.72, 1.19])
    general_formula_error = 0.0
    for modes in (2, 3, 4, 5):
        count = shell_count(capacity_probe, modes, reference_action)
        coefficient = (2.0 * pi) ** modes / factorial(modes - 1)
        expected = coefficient * (capacity_probe / reference_action) ** (modes - 1)
        general_formula_error = max(general_formula_error, float(np.max(np.abs(count - expected))))
    checks.append(record_max("general_action_shell_formula_error", general_formula_error, 3.0e-12))
    checks.append(record_max(
        "action_shell_born_weight_error",
        np.linalg.norm(shell_target - born_target),
        3.0e-14,
    ))
    checks.append(record_max("action_shell_weight_normalization_error", abs(np.sum(shell_target) - 1.0), 2.0e-15))

    phase_counts = shell_count(phase_capacities, 2, reference_action)
    phase_target = phase_counts / np.sum(phase_counts)
    scaled_counts = shell_count(scaled_capacities, 2, reference_action)
    scaled_target = scaled_counts / np.sum(scaled_counts)
    checks.append(record_max("shell_weight_phase_invariance_error", np.linalg.norm(phase_target - shell_target), 3.0e-14))
    checks.append(record_max("shell_weight_scale_invariance_error", np.linalg.norm(scaled_target - shell_target), 3.0e-14))

    theta = 1.37
    effective_energy = -theta * np.log(shell_target)
    shell_free_energy = -theta * np.log(counts)
    equilibrium_free_energy = -theta * log(float(np.sum(counts)))
    checks.append(record_max(
        "effective_free_energy_gauge_error",
        np.linalg.norm(effective_energy - (shell_free_energy - equilibrium_free_energy)),
        3.0e-14,
    ))
    gibbs_target = np.exp(-effective_energy / theta)
    gibbs_target /= np.sum(gibbs_target)
    checks.append(record_max("effective_gibbs_recovery_error", np.linalg.norm(gibbs_target - shell_target), 3.0e-14))

    linear_counts = shell_count(capacity_probe, 2, reference_action)
    linear_ratio = linear_counts / capacity_probe
    checks.append(record_max("one_reaction_direction_linearity_error", np.ptp(linear_ratio), 3.0e-13))

    quadratic_target = shell_count(capacities, 3, reference_action)
    quadratic_target /= np.sum(quadratic_target)
    checks.append(record_min(
        "multiple_reaction_direction_nonborn_distance",
        total_variation(quadratic_target, shell_target),
        1.0e-3,
    ))

    common_spectator = 4.73
    spectator_target = common_spectator * counts
    spectator_target /= np.sum(spectator_target)
    checks.append(record_max("common_spectator_cancellation_error", np.linalg.norm(spectator_target - shell_target), 3.0e-14))

    branch_spectator = np.linspace(0.8, 1.2, size)
    distorted_target = branch_spectator * counts
    distorted_target /= np.sum(distorted_target)
    checks.append(record_min(
        "branch_spectator_detectable_distortion",
        total_variation(distorted_target, shell_target),
        1.0e-3,
    ))

    common_flux = 2.19 * counts
    common_flux /= np.sum(common_flux)
    checks.append(record_max("common_flux_born_weight_error", np.linalg.norm(common_flux - shell_target), 3.0e-14))

    symmetry_error = 0.08
    eta = rng.uniform(-symmetry_error, symmetry_error, size=size)
    perturbed_flux = (1.0 + eta) * counts
    perturbed_flux /= np.sum(perturbed_flux)
    flux_bound = symmetry_error / (1.0 - symmetry_error)
    checks.append(record_max(
        "branch_flux_total_variation_bound_excess",
        max(0.0, total_variation(perturbed_flux, shell_target) - flux_bound),
        2.0e-15,
    ))

    beta = 0.83
    stiffness = 190.0
    smooth_capacities = np.array([0.43, 0.77, 1.11])
    analytic_partition = smooth_partition(smooth_capacities, beta, stiffness)
    a_value = 0.5 * beta * stiffness
    numeric_partition = []
    for capacity in smooth_capacities:
        upper = capacity + 12.0 / sqrt(a_value)
        grid = np.linspace(0.0, upper, 300_001)
        integrand = grid * np.exp(-a_value * (grid - capacity) ** 2)
        numeric_partition.append((2.0 * pi) ** 2 * np.trapezoid(integrand, grid))
    numeric_partition_array = np.array(numeric_partition)
    checks.append(record_max(
        "smooth_partition_quadrature_error",
        np.max(np.abs(analytic_partition - numeric_partition_array)),
        2.0e-8,
    ))
    checks.append(record_min("smooth_partition_positivity", np.min(analytic_partition), 1.0e-12))

    normalization = (2.0 * pi) ** 2 * sqrt(pi / a_value)
    relative_remainder = analytic_partition / (normalization * smooth_capacities) - 1.0
    x_value = sqrt(a_value) * smooth_capacities
    remainder_bound = np.exp(-(x_value**2)) / (2.0 * sqrt(pi) * x_value)
    checks.append(record_min("smooth_remainder_nonnegativity", np.min(relative_remainder), -3.0e-14))
    checks.append(record_max(
        "smooth_remainder_bound_excess",
        max(0.0, float(np.max(relative_remainder - remainder_bound))),
        3.0e-14,
    ))

    smooth_target = analytic_partition / np.sum(analytic_partition)
    ideal_smooth_target = smooth_capacities / np.sum(smooth_capacities)
    smooth_tv_bound = 0.5 * float(np.max(relative_remainder))
    checks.append(record_max(
        "smooth_target_total_variation_bound_excess",
        max(0.0, total_variation(smooth_target, ideal_smooth_target) - smooth_tv_bound),
        2.0e-14,
    ))

    delta_family = np.array([0.1, 0.03, 0.01, 0.003])
    stiffness_family = 7.0 / delta_family**2
    action_floor_family = action_unit * delta_family * np.min(reference) * 0.61
    x_floor_family = np.sqrt(0.5 * beta * stiffness_family) * action_floor_family
    checks.append(record_max(
        "delta_inverse_square_stiffness_uniformity_error",
        np.ptp(x_floor_family),
        3.0e-14,
    ))

    node_partition = float(smooth_partition(np.array([0.0]), beta, stiffness)[0])
    checks.append(record_min("finite_stiffness_zero_capacity_background", node_partition, 1.0e-12))

    zero_state = np.zeros(2, dtype=complex)
    zero_signal, _, zero_capacities = action_capacities(
        isometry, zero_state, action_unit, delta, reference
    )
    zero_seed_is_undefined = zero_signal == 0.0 and float(np.sum(zero_capacities)) == 0.0
    checks.append(record_min("zero_seed_no_response_flag", float(zero_seed_is_undefined), 1.0))

    first, second = 1, 5
    base_barrier = 2.7
    barrier = base_barrier + 0.5 * (effective_energy[first] + effective_energy[second])
    gauge_shift = -0.64
    shifted_energy = effective_energy + gauge_shift
    shifted_barrier = barrier + gauge_shift
    threshold_error = max(
        abs((shifted_barrier - shifted_energy[first]) - (barrier - effective_energy[first])),
        abs((shifted_barrier - shifted_energy[second]) - (barrier - effective_energy[second])),
    )
    checks.append(record_max("barrier_gauge_invariance_error", threshold_error, 2.0e-15))

    activity = 0.71
    forward = activity * sqrt(shell_target[second] / shell_target[first])
    backward = activity * sqrt(shell_target[first] / shell_target[second])
    checks.append(record_max(
        "r161_shell_detailed_balance_error",
        abs(shell_target[first] * forward - shell_target[second] * backward),
        2.0e-15,
    ))

    response_mass = 0.947
    no_response_categories = np.array([0.019, 0.011, 0.014, 0.009])
    complete_mass = response_mass + float(np.sum(no_response_categories))
    checks.append(record_max("complete_outcome_mass_error", abs(complete_mass - 1.0), 2.0e-15))

    payload = {
        "seed": seed,
        "check_count": len(checks),
        "minimum_regularized_capacity": float(np.min(capacities)),
        "maximum_smooth_remainder": float(np.max(relative_remainder)),
        "checks": [asdict(check) for check in checks],
        "passed": all(check.passed for check in checks),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
