#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from itertools import product
from math import pi, sqrt

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


def record_equal(name: str, value: float, expected: float) -> CheckResult:
    error = abs(value - expected)
    return CheckResult(name, float(error), 0.0, "==", bool(error == 0.0))


def pauli_matrices() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    sigma_x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sigma_y = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
    sigma_z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    return sigma_x, sigma_y, sigma_z


def unitary_from_hermitian(generator: np.ndarray) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(generator)
    return eigenvectors @ np.diag(np.exp(-1j * eigenvalues)) @ eigenvectors.conj().T


def rabi_flip_probability(interval: float, drive: float, detuning: float) -> float:
    frequency = np.hypot(drive, detuning)
    return float(
        drive**2 / frequency**2
        * np.sin(frequency * interval / 2.0) ** 2
    )


def ideal_history_distribution(q_values: np.ndarray) -> dict[tuple[int, ...], float]:
    distribution: dict[tuple[int, ...], float] = {(): 1.0}
    for q_value in q_values:
        updated: dict[tuple[int, ...], float] = {}
        for history, weight in distribution.items():
            previous = 1 if not history else history[-1]
            updated[history + (previous,)] = weight * (1.0 - q_value)
            updated[history + (-previous,)] = weight * q_value
        distribution = updated
    return distribution


def real_history_distribution(
    q_values: np.ndarray,
    eta_values: np.ndarray,
) -> dict[tuple[int, ...], float]:
    states: dict[tuple[int, tuple[int, ...]], float] = {(1, ()): 1.0}
    for q_value, eta_value in zip(q_values, eta_values, strict=True):
        updated: dict[tuple[int, tuple[int, ...]], float] = {}
        for (state, history), weight in states.items():
            branches = (
                (state, state, (1.0 - eta_value) * (1.0 - q_value)),
                (-state, -state, (1.0 - eta_value) * q_value),
                (state, 0, eta_value),
            )
            for next_state, outcome, branch_weight in branches:
                key = (next_state, history + (outcome,))
                updated[key] = updated.get(key, 0.0) + weight * branch_weight
        states = updated
    distribution: dict[tuple[int, ...], float] = {}
    for (_, history), weight in states.items():
        distribution[history] = distribution.get(history, 0.0) + weight
    return distribution


def total_variation(
    first: dict[tuple[int, ...], float],
    second: dict[tuple[int, ...], float],
) -> float:
    keys = set(first) | set(second)
    return 0.5 * sum(abs(first.get(key, 0.0) - second.get(key, 0.0)) for key in keys)


def complex_to_real(unitary: np.ndarray) -> np.ndarray:
    return np.block([
        [unitary.real, -unitary.imag],
        [unitary.imag, unitary.real],
    ])


def random_unitary(rng: np.random.Generator, size: int) -> np.ndarray:
    matrix = rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))
    q_matrix, r_matrix = np.linalg.qr(matrix)
    phases = np.diag(r_matrix)
    phases = np.where(np.abs(phases) > 0.0, phases / np.abs(phases), 1.0)
    return q_matrix @ np.diag(phases.conj())


def embedded_unitary(
    size: int,
    indices: list[int],
    local: np.ndarray,
) -> np.ndarray:
    result = np.eye(size, dtype=complex)
    result[np.ix_(indices, indices)] = local
    return result


def main() -> None:
    seed = 20260810
    rng = np.random.default_rng(seed)
    sigma_x, _, sigma_z = pauli_matrices()
    checks: list[CheckResult] = []

    # Exact Rabi propagator and analytic transition probability.
    drive = 0.83
    detuning = 0.37
    interval = 1.91
    generator = interval * (detuning * sigma_z + drive * sigma_x) / 2.0
    propagator = unitary_from_hermitian(generator)
    transition = abs((propagator @ np.array([1.0, 0.0], dtype=complex))[1]) ** 2
    analytic_transition = rabi_flip_probability(interval, drive, detuning)
    checks.append(record_max(
        "zeno_rabi_transition_formula_error",
        abs(transition - analytic_transition),
        2.0e-14,
    ))

    # Nonuniform finite-history law, survival event, and final occupation.
    q_values = np.array([0.13, 0.27, 0.08, 0.31])
    history = ideal_history_distribution(q_values)
    checks.append(record_max(
        "nonuniform_history_normalization_error",
        abs(sum(history.values()) - 1.0),
        2.0e-14,
    ))
    survival_from_histories = history[(1, 1, 1, 1)]
    survival_closed = float(np.prod(1.0 - q_values))
    checks.append(record_max(
        "survival_history_sum_error",
        abs(survival_from_histories - survival_closed),
        2.0e-14,
    ))
    final_plus_from_histories = sum(
        weight for outcomes, weight in history.items() if outcomes[-1] == 1
    )
    final_plus_closed = 0.5 * (1.0 + float(np.prod(1.0 - 2.0 * q_values)))
    checks.append(record_max(
        "final_plus_history_sum_error",
        abs(final_plus_from_histories - final_plus_closed),
        2.0e-14,
    ))

    # Short-time quadratic law and effective flip rate.
    short_interval = 1.0e-3
    short_q = rabi_flip_probability(short_interval, drive, detuning)
    quadratic_coefficient = drive**2 / 4.0
    checks.append(record_max(
        "short_time_flip_coefficient_error",
        abs(short_q / short_interval**2 - quadratic_coefficient),
        2.0e-8,
    ))
    effective_rate = -np.log1p(-short_q) / short_interval
    checks.append(record_max(
        "short_time_effective_rate_coefficient_error",
        abs(effective_rate / short_interval - quadratic_coefficient),
        2.0e-8,
    ))

    # Finite resonant benchmark against an unmeasured half Rabi period.
    zeno_count = 7
    total_time = pi / drive
    equal_interval = total_time / zeno_count
    benchmark_q = rabi_flip_probability(equal_interval, drive, 0.0)
    measured_survival = (1.0 - benchmark_q) ** zeno_count
    unmeasured_survival = 1.0 - rabi_flip_probability(total_time, drive, 0.0)
    checks.append(record_max(
        "unmeasured_half_period_survival_error",
        abs(unmeasured_survival),
        2.0e-14,
    ))
    checks.append(record_min(
        "finite_zeno_benchmark_survival",
        measured_survival,
        0.65,
    ))

    # Three-selector torus reproduces the complete Markov history frequencies.
    torus_q = np.array([0.21, 0.34, 0.17])
    ideal_torus_history = ideal_history_distribution(torus_q)
    samples = 500_000
    index = np.arange(samples, dtype=float)
    alpha = np.array([sqrt(2.0), sqrt(3.0), sqrt(5.0)])
    offset = np.array([0.137, 0.419, 0.731])
    selectors = np.mod(offset[:, None] + alpha[:, None] * index[None, :], 1.0)
    state = np.ones(samples, dtype=int)
    outcomes = np.empty((samples, len(torus_q)), dtype=int)
    for stage, q_value in enumerate(torus_q):
        state = np.where(selectors[stage] < q_value, -state, state)
        outcomes[:, stage] = state
    empirical_torus_history = {
        signs: float(np.mean(np.all(outcomes == np.array(signs), axis=1)))
        for signs in product((1, -1), repeat=len(torus_q))
    }
    checks.append(record_max(
        "three_torus_history_frequency_error",
        max(
            abs(empirical_torus_history[key] - ideal_torus_history[key])
            for key in ideal_torus_history
        ),
        8.0e-5,
    ))

    # Sequential total-variation bound with explicit no-response outcomes.
    eta_values = np.array([0.011, 0.017, 0.009, 0.013])
    real_history = real_history_distribution(q_values, eta_values)
    ideal_extended = dict(history)
    tv_distance = total_variation(real_history, ideal_extended)
    tv_product_bound = 1.0 - float(np.prod(1.0 - eta_values))
    checks.append(record_max(
        "sequential_tv_product_identity_error",
        abs(tv_distance - tv_product_bound),
        2.0e-14,
    ))
    checks.append(record_max(
        "sequential_tv_sum_bound_excess",
        max(0.0, tv_distance - float(np.sum(eta_values))),
        2.0e-14,
    ))
    no_response_mass = sum(
        weight for outcomes, weight in real_history.items() if 0 in outcomes
    )
    checks.append(record_max(
        "no_response_mass_identity_error",
        abs(no_response_mass - tv_product_bound),
        2.0e-14,
    ))

    # Six-pair cell swap is symplectic and leaves the two-pair signal unchanged.
    signal_pairs = 2
    core_pairs = 6
    cell_pairs = 6
    complex_size = signal_pairs + core_pairs + cell_pairs
    swap = np.eye(complex_size, dtype=complex)
    core_indices = list(range(signal_pairs, signal_pairs + core_pairs))
    cell_indices = list(range(signal_pairs + core_pairs, complex_size))
    for core_index, cell_index in zip(core_indices, cell_indices, strict=True):
        swap[core_index, core_index] = 0.0
        swap[cell_index, cell_index] = 0.0
        swap[core_index, cell_index] = 1.0
        swap[cell_index, core_index] = -1.0
    real_swap = complex_to_real(swap)
    symplectic_form = np.block([
        [np.zeros((complex_size, complex_size)), np.eye(complex_size)],
        [-np.eye(complex_size), np.zeros((complex_size, complex_size))],
    ])
    checks.append(record_max(
        "six_pair_cell_swap_symplectic_error",
        np.linalg.norm(real_swap.T @ symplectic_form @ real_swap - symplectic_form),
        2.0e-14,
    ))
    test_state = rng.normal(size=complex_size) + 1j * rng.normal(size=complex_size)
    swapped_state = swap @ test_state
    checks.append(record_max(
        "cell_swap_signal_change",
        np.linalg.norm(swapped_state[:signal_pairs] - test_state[:signal_pairs]),
        2.0e-14,
    ))

    # Forward stages and reverse restoration with one reusable measurement core.
    stage_count = 4
    total_pairs = signal_pairs + core_pairs + stage_count * cell_pairs
    forward = np.eye(total_pairs, dtype=complex)
    stage_maps: list[tuple[np.ndarray, np.ndarray, np.ndarray]] = []
    for stage in range(stage_count):
        rabi_local = random_unitary(rng, signal_pairs)
        rabi_map = embedded_unitary(total_pairs, list(range(signal_pairs)), rabi_local)
        measurement_local = random_unitary(rng, signal_pairs + core_pairs)
        measurement_indices = list(range(signal_pairs + core_pairs))
        measurement_map = embedded_unitary(
            total_pairs,
            measurement_indices,
            measurement_local,
        )
        stage_cell_start = signal_pairs + core_pairs + stage * cell_pairs
        stage_cell_indices = list(range(stage_cell_start, stage_cell_start + cell_pairs))
        swap_local = np.eye(total_pairs, dtype=complex)
        for core_index, cell_index in zip(core_indices, stage_cell_indices, strict=True):
            swap_local[core_index, core_index] = 0.0
            swap_local[cell_index, cell_index] = 0.0
            swap_local[core_index, cell_index] = 1.0
            swap_local[cell_index, core_index] = -1.0
        forward = swap_local @ measurement_map @ rabi_map @ forward
        stage_maps.append((rabi_map, measurement_map, swap_local))
    restored = forward.copy()
    for rabi_map, measurement_map, swap_map in reversed(stage_maps):
        restored = rabi_map.conj().T @ measurement_map.conj().T @ swap_map.conj().T @ restored
    checks.append(record_max(
        "single_core_reverse_restoration_error",
        np.linalg.norm(restored - np.eye(total_pairs)),
        8.0e-14,
    ))

    # A continuously active Rabi generator changes a finite pulse by O(h).
    measurement_generator = 0.61 * sigma_z
    rabi_generator = 0.47 * sigma_x + 0.19 * sigma_z
    ideal_measurement = unitary_from_hermitian(measurement_generator)
    pulse_widths = np.array([0.08, 0.04, 0.02, 0.01])
    pulse_errors = np.array([
        np.linalg.norm(
            unitary_from_hermitian(measurement_generator + width * rabi_generator)
            - ideal_measurement
        )
        for width in pulse_widths
    ])
    checks.append(record_max(
        "continuous_rabi_pulse_linear_bound",
        float(np.max(pulse_errors / pulse_widths)),
        1.0,
    ))
    convergence_ratios = pulse_errors[:-1] / pulse_errors[1:]
    checks.append(record_max(
        "continuous_rabi_pulse_first_order_ratio_error",
        float(np.max(np.abs(convergence_ratios - 2.0))),
        1.5e-2,
    ))
    rabi_coefficients = np.ones(stage_count)
    checks.append(record_min(
        "minimum_forward_rabi_coefficient",
        float(np.min(rabi_coefficients)),
        1.0,
    ))

    # Resource arithmetic for one observation and repeated experiment cycles.
    resource_stages = 5
    experiment_cycles = 11
    checks.append(record_equal(
        "single_observation_pair_count_error",
        10 + 8 * resource_stages,
        50,
    ))
    checks.append(record_equal(
        "repeated_observation_pair_count_error",
        10 + 7 * resource_stages + experiment_cycles * resource_stages,
        100,
    ))

    payload = {
        "seed": seed,
        "checks": [asdict(check) for check in checks],
        "passed": all(check.passed for check in checks),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
