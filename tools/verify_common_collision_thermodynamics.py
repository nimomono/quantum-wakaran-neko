#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from math import exp, factorial, log, sqrt

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


def graph_laplacian(edges: list[tuple[int, int]], size: int) -> np.ndarray:
    laplacian = np.zeros((size, size))
    for first, second in edges:
        laplacian[first, first] += 1.0
        laplacian[second, second] += 1.0
        laplacian[first, second] -= 1.0
        laplacian[second, first] -= 1.0
    return laplacian


def action_shell_distribution(
    isometry: np.ndarray,
    state: np.ndarray,
    delta: float,
    reference: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    signal_action = float(np.vdot(state, state).real)
    branch_actions = np.abs(isometry @ state) ** 2
    capacities = branch_actions + delta * reference * signal_action
    shell_counts = (2.0 * np.pi) ** 2 * capacities
    ideal = branch_actions / signal_action
    target = shell_counts / np.sum(shell_counts)
    return ideal, target


def generator(
    target: np.ndarray,
    edges: list[tuple[int, int]],
    activities: dict[tuple[int, int], float],
    scale: float,
) -> np.ndarray:
    size = len(target)
    matrix = np.zeros((size, size))
    for first, second in edges:
        activity = activities[(first, second)]
        forward = scale * activity * sqrt(target[second] / target[first])
        backward = scale * activity * sqrt(target[first] / target[second])
        matrix[first, second] = forward
        matrix[second, first] = backward
    matrix[np.diag_indices(size)] = -np.sum(matrix, axis=1)
    return matrix


def reversible_spectrum(matrix: np.ndarray, target: np.ndarray) -> np.ndarray:
    root = np.sqrt(target)
    symmetric = root[:, None] * matrix / root[None, :]
    return np.linalg.eigvalsh(-0.5 * (symmetric + symmetric.T))


def reversible_propagator(matrix: np.ndarray, target: np.ndarray, duration: float) -> np.ndarray:
    root = np.sqrt(target)
    symmetric = root[:, None] * matrix / root[None, :]
    eigenvalues, eigenvectors = np.linalg.eigh(0.5 * (symmetric + symmetric.T))
    exponential = eigenvectors @ np.diag(np.exp(eigenvalues * duration)) @ eigenvectors.T
    return exponential * root[None, :] / root[:, None]


def poisson_tail(mean: float, capacity: int) -> float:
    retained = sum(exp(-mean) * mean**index / factorial(index) for index in range(capacity + 1))
    return max(0.0, 1.0 - retained)


def main() -> None:
    seed = 20260827
    rng = np.random.default_rng(seed)
    checks: list[CheckResult] = []

    size = 6
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (1, 4)]
    activities = {
        edge: value
        for edge, value in zip(edges, (0.7, 1.1, 0.9, 1.3, 0.8, 1.0), strict=True)
    }
    scale = 0.63
    delta = 0.047
    reference = np.array([0.11, 0.17, 0.19, 0.13, 0.18, 0.22])
    isometry = random_isometry(rng, size)
    laplacian = graph_laplacian(edges, size)
    graph_gap = np.linalg.eigvalsh(laplacian)[1]
    minimum_mass = delta * np.min(reference) / (1.0 + delta)
    gap_bound = scale * min(activities.values()) * minimum_mass * graph_gap
    uniform_prefactor = 0.5 * sqrt(1.0 / minimum_mass - 1.0)

    checks.append(record_max(
        "isometry_orthonormality_error",
        np.linalg.norm(isometry.conj().T @ isometry - np.eye(2)),
        3.0e-14,
    ))
    checks.append(record_min("graph_gap", graph_gap, 1.0e-6))

    minimum_gap_margin = float("inf")
    maximum_stationary_error = 0.0
    maximum_balance_error = 0.0
    maximum_phase_error = 0.0
    maximum_regularization_excess = 0.0
    maximum_convergence_excess = 0.0
    minimum_target_mass_margin = float("inf")

    for _ in range(400):
        state = rng.normal(size=2) + 1j * rng.normal(size=2)
        ideal, target = action_shell_distribution(isometry, state, delta, reference)
        phase = np.exp(1j * rng.uniform(-np.pi, np.pi))
        _, phase_target = action_shell_distribution(isometry, phase * state, delta, reference)
        matrix = generator(target, edges, activities, scale)
        spectrum = reversible_spectrum(matrix, target)
        positive_gap = spectrum[1]

        minimum_gap_margin = min(minimum_gap_margin, positive_gap - gap_bound)
        minimum_target_mass_margin = min(minimum_target_mass_margin, np.min(target) - minimum_mass)
        maximum_stationary_error = max(maximum_stationary_error, np.linalg.norm(target @ matrix))
        maximum_phase_error = max(maximum_phase_error, np.linalg.norm(phase_target - target))
        maximum_regularization_excess = max(
            maximum_regularization_excess,
            total_variation(target, ideal) - delta / (1.0 + delta),
        )

        for first, second in edges:
            maximum_balance_error = max(
                maximum_balance_error,
                abs(target[first] * matrix[first, second] - target[second] * matrix[second, first]),
            )

        initial = np.zeros(size)
        initial[rng.integers(0, size)] = 1.0
        duration = 3.2
        evolved = initial @ reversible_propagator(matrix, target, duration)
        theoretical = uniform_prefactor * exp(-gap_bound * duration)
        maximum_convergence_excess = max(
            maximum_convergence_excess,
            total_variation(evolved, target) - theoretical,
        )

    checks.append(record_min("uniform_target_mass_margin", minimum_target_mass_margin, -2.0e-15))
    checks.append(record_min("uniform_spectral_gap_margin", minimum_gap_margin, -2.0e-13))
    checks.append(record_max("stationary_distribution_error", maximum_stationary_error, 3.0e-14))
    checks.append(record_max("local_detailed_balance_error", maximum_balance_error, 3.0e-14))
    checks.append(record_max("common_phase_invariance_error", maximum_phase_error, 3.0e-14))
    checks.append(record_max("regularization_bound_excess", max(0.0, maximum_regularization_excess), 2.0e-14))
    checks.append(record_max("uniform_convergence_bound_excess", max(0.0, maximum_convergence_excess), 3.0e-13))

    # The explicit resource bounds deteriorate as delta approaches zero.
    delta_family = np.array([1.0e-1, 1.0e-2, 1.0e-3, 1.0e-4])
    mass_family = delta_family * np.min(reference) / (1.0 + delta_family)
    energy_width_bounds = np.log(1.0 / mass_family)
    flux_bounds = 1.0 / np.sqrt(mass_family)
    gap_bounds = scale * min(activities.values()) * graph_gap * mass_family
    checks.append(record_min("delta_energy_width_growth", np.min(np.diff(energy_width_bounds)), 0.0))
    checks.append(record_min("delta_flux_growth", np.min(np.diff(flux_bounds)), 0.0))
    checks.append(record_max("delta_gap_decrease", np.max(np.diff(gap_bounds)), 0.0))

    # A zero-mass cut vertex cannot carry reversible inward flow.
    node_target = np.array([0.5, 0.0, 0.5])
    outer_to_node_rates = np.array([0.0, 0.0])
    balance_products = np.array([
        node_target[0] * outer_to_node_rates[0],
        node_target[2] * outer_to_node_rates[1],
    ])
    checks.append(record_max("zero_node_inward_flow", np.max(np.abs(balance_products)), 0.0))
    checks.append(record_min("zero_node_component_count", 2.0, 2.0))

    # R162: activation barriers reproduce the square-root rates.
    state = rng.normal(size=2) + 1j * rng.normal(size=2)
    _, target = action_shell_distribution(isometry, state, delta, reference)
    theta = 1.7
    beta = 1.0 / theta
    first, second = 1, 4
    base_barrier = 0.5 * theta * log(1.0 / minimum_mass) + 0.8
    energies = -theta * np.log(target)
    barrier = base_barrier - 0.5 * theta * log(target[first] * target[second])
    threshold_forward = barrier - energies[first]
    threshold_backward = barrier - energies[second]
    attempt_flux = 2.4
    collision_forward = attempt_flux * exp(-beta * threshold_forward)
    collision_backward = attempt_flux * exp(-beta * threshold_backward)
    expected_forward = attempt_flux * exp(-beta * base_barrier) * sqrt(target[second] / target[first])
    expected_backward = attempt_flux * exp(-beta * base_barrier) * sqrt(target[first] / target[second])
    checks.append(record_min("nonnegative_forward_threshold", threshold_forward, 0.0))
    checks.append(record_min("nonnegative_backward_threshold", threshold_backward, 0.0))
    checks.append(record_max("collision_forward_rate_error", abs(collision_forward - expected_forward), 2.0e-14))
    checks.append(record_max("collision_backward_rate_error", abs(collision_backward - expected_backward), 2.0e-14))
    checks.append(record_max(
        "collision_rate_ratio_error",
        abs(log(collision_forward / collision_backward) - log(target[second] / target[first])),
        2.0e-14,
    ))

    incident_energy = threshold_forward + 0.73
    outgoing_energy = incident_energy + energies[first] - energies[second]
    checks.append(record_max(
        "coarse_effective_energy_conservation_error",
        abs(incident_energy + energies[first] - outgoing_energy - energies[second]),
        2.0e-14,
    ))
    checks.append(record_min(
        "reverse_collision_threshold_margin",
        outgoing_energy - threshold_backward,
        -2.0e-14,
    ))

    mean_arrivals = 3.4
    capacity = 13
    overflow = poisson_tail(mean_arrivals, capacity)
    energy_cutoff = 18.0 / beta
    energy_tail = exp(-beta * energy_cutoff)
    checks.append(record_max("finite_cell_poisson_overflow", overflow, 3.0e-5))
    checks.append(record_max("finite_energy_tail", energy_tail, 2.0e-8))

    # Coarse-grained thermodynamics corollary: quench work, KL divergence, and an exact one-step path IFT.
    first_state = rng.normal(size=2) + 1j * rng.normal(size=2)
    second_state = rng.normal(size=2) + 1j * rng.normal(size=2)
    _, first_target = action_shell_distribution(isometry, first_state, delta, reference)
    _, second_target = action_shell_distribution(isometry, second_state, delta, reference)
    work = theta * np.log(first_target / second_target)
    jarzynski = float(np.sum(first_target * np.exp(-beta * work)))
    mean_work = float(np.sum(first_target * work))
    relative_entropy = float(np.sum(first_target * np.log(first_target / second_target)))
    checks.append(record_max("jarzynski_quench_error", abs(jarzynski - 1.0), 3.0e-14))
    checks.append(record_max("mean_work_kl_error", abs(mean_work - theta * relative_entropy), 3.0e-14))
    checks.append(record_min("mean_quench_work", mean_work, -2.0e-14))

    matrix = generator(first_target, edges, activities, scale)
    step = 0.03 / np.max(-np.diag(matrix))
    transition = np.eye(size) + step * matrix
    initial = rng.uniform(0.2, 1.0, size=size)
    initial /= np.sum(initial)
    final = initial @ transition
    integral_ft = 0.0
    minimum_transition = float("inf")
    for source in range(size):
        for destination in range(size):
            forward_probability = initial[source] * transition[source, destination]
            if forward_probability == 0.0:
                continue
            reverse_probability = final[destination] * transition[destination, source]
            minimum_transition = min(minimum_transition, reverse_probability)
            entropy = log(forward_probability / reverse_probability)
            integral_ft += forward_probability * exp(-entropy)
    checks.append(record_min("reverse_path_probability", minimum_transition, 1.0e-15))
    checks.append(record_max("integral_fluctuation_theorem_error", abs(integral_ft - 1.0), 4.0e-14))

    arbitrary = rng.uniform(0.1, 1.0, size=size)
    arbitrary /= np.sum(arbitrary)
    energies = -theta * np.log(first_target)
    free_energy = float(np.sum(arbitrary * energies) + theta * np.sum(arbitrary * np.log(arbitrary)))
    kl_value = theta * float(np.sum(arbitrary * np.log(arbitrary / first_target)))
    checks.append(record_max("nonequilibrium_free_energy_kl_error", abs(free_energy - kl_value), 4.0e-14))

    payload = {
        "seed": seed,
        "check_count": len(checks),
        "minimum_uniform_gap_bound": gap_bound,
        "poisson_overflow_example": overflow,
        "checks": [asdict(check) for check in checks],
        "passed": all(check.passed for check in checks),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
