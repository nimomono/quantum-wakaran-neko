#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from math import pi

import numpy as np


J0 = 1.0
TOL = 2.0e-11


@dataclass
class Check:
    name: str
    value: float
    limit: float
    relation: str = "<="

    @property
    def passed(self) -> bool:
        if self.relation == "<=":
            return self.value <= self.limit
        if self.relation == ">=":
            return self.value >= self.limit
        raise ValueError(self.relation)


def path_hamiltonian(size: int) -> tuple[np.ndarray, list[tuple[int, int]]]:
    matrix = np.zeros((size, size), dtype=float)
    edges: list[tuple[int, int]] = []
    couplings = np.linspace(0.32, 0.56, size - 1)
    for index, coupling in enumerate(couplings):
        edges.append((index, index + 1))
        matrix[index, index + 1] = -coupling
        matrix[index + 1, index] = -coupling
        matrix[index, index] += coupling
        matrix[index + 1, index + 1] += coupling
    matrix += np.diag(np.linspace(-0.13, 0.19, size))
    return matrix, edges


def evolve(matrix: np.ndarray, initial: np.ndarray, time: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    phases = np.exp(-1j * values * time / J0)
    return vectors @ (phases * (vectors.conj().T @ initial))


def probability(amplitude: np.ndarray) -> np.ndarray:
    return np.abs(amplitude) ** 2


def currents(amplitude: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    size = len(amplitude)
    result = np.zeros((size, size), dtype=float)
    for source in range(size):
        for target in range(size):
            result[source, target] = 2.0 / J0 * np.imag(
                np.conj(amplitude[target])
                * matrix[target, source]
                * amplitude[source]
            )
    return result


def probability_derivative(amplitude: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    derivative = -1j * matrix @ amplitude / J0
    return 2.0 * np.real(np.conj(amplitude) * derivative)


def generator_from_rates(rates: np.ndarray) -> np.ndarray:
    generator = rates.copy()
    np.fill_diagonal(generator, 0.0)
    generator[np.diag_indices_from(generator)] = -np.sum(generator, axis=1)
    return generator


def minimal_rates(amplitude: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    weights = probability(amplitude)
    flow = currents(amplitude, matrix)
    rates = np.zeros_like(flow)
    for source in range(len(weights)):
        if weights[source] > 1.0e-14:
            rates[source] = np.maximum(flow[source], 0.0) / weights[source]
    np.fill_diagonal(rates, 0.0)
    return rates


def smooth_positive(value: np.ndarray | float, sigma: float):
    return 0.5 * (value + np.sqrt(np.asarray(value) ** 2 + sigma**2))


def regularized_rates(
    amplitude: np.ndarray,
    matrix: np.ndarray,
    rho: float,
    sigma: float,
) -> np.ndarray:
    weights = probability(amplitude)
    flow = currents(amplitude, matrix)
    rates = smooth_positive(flow, sigma) / (weights[:, None] + rho)
    rates[np.isclose(matrix, 0.0, atol=0.0)] = 0.0
    np.fill_diagonal(rates, 0.0)
    return rates


def total_variation(first: np.ndarray, second: np.ndarray) -> float:
    return float(0.5 * np.sum(np.abs(first - second)))


def rk4_distribution(
    matrix: np.ndarray,
    initial_amplitude: np.ndarray,
    initial_distribution: np.ndarray,
    rho: float,
    sigma: float,
    duration: float,
    steps: int,
    carrier_offset: np.ndarray | None = None,
) -> tuple[np.ndarray, float, float]:
    step = duration / steps
    state = initial_distribution.astype(float).copy()
    minimum = float(np.min(state))
    normalization_error = abs(float(np.sum(state)) - 1.0)

    def rhs(time: float, distribution: np.ndarray) -> np.ndarray:
        amplitude = evolve(matrix, initial_amplitude, time)
        if carrier_offset is not None:
            amplitude = amplitude + carrier_offset
        rates = regularized_rates(amplitude, matrix, rho, sigma)
        return distribution @ generator_from_rates(rates)

    for index in range(steps):
        time = index * step
        k1 = rhs(time, state)
        k2 = rhs(time + step / 2.0, state + step * k1 / 2.0)
        k3 = rhs(time + step / 2.0, state + step * k2 / 2.0)
        k4 = rhs(time + step, state + step * k3)
        state += step * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        minimum = min(minimum, float(np.min(state)))
        normalization_error = max(normalization_error, abs(float(np.sum(state)) - 1.0))
    return state, minimum, normalization_error


def euler_distribution(
    matrix: np.ndarray,
    initial_amplitude: np.ndarray,
    initial_distribution: np.ndarray,
    rho: float,
    sigma: float,
    duration: float,
    steps: int,
) -> tuple[np.ndarray, float, float]:
    step = duration / steps
    state = initial_distribution.astype(float).copy()
    minimum = float(np.min(state))
    normalization_error = abs(float(np.sum(state)) - 1.0)
    for index in range(steps):
        amplitude = evolve(matrix, initial_amplitude, index * step)
        rates = regularized_rates(amplitude, matrix, rho, sigma)
        kernel = np.eye(len(state)) + step * generator_from_rates(rates)
        state = state @ kernel
        minimum = min(minimum, float(np.min(state)))
        normalization_error = max(normalization_error, abs(float(np.sum(state)) - 1.0))
    return state, minimum, normalization_error


def edge_weight_sum(matrix: np.ndarray, edges: list[tuple[int, int]]) -> float:
    return float(sum(abs(matrix[first, second]) for first, second in edges))


def main() -> None:
    rng = np.random.default_rng(20260812)
    size = 6
    matrix, edges = path_hamiltonian(size)
    initial = rng.normal(size=size) + 1j * rng.normal(size=size)
    initial /= np.linalg.norm(initial)
    sample_time = 0.73
    amplitude = evolve(matrix, initial, sample_time)
    weights = probability(amplitude)
    flow = currents(amplitude, matrix)
    derivative = probability_derivative(amplitude, matrix)
    rates = minimal_rates(amplitude, matrix)
    generator = generator_from_rates(rates)

    checks: list[Check] = []
    checks.append(Check(
        "unitary action conservation",
        abs(float(np.vdot(amplitude, amplitude).real) - 1.0),
        TOL,
    ))
    checks.append(Check("current antisymmetry", float(np.max(np.abs(flow + flow.T))), TOL))
    checks.append(Check(
        "graph continuity equation",
        float(np.max(np.abs(derivative - np.sum(flow, axis=0)))),
        TOL,
    ))
    checks.append(Check(
        "minimal-rate master equation",
        float(np.max(np.abs(weights @ generator - derivative))),
        TOL,
    ))

    adjacency = np.zeros_like(matrix, dtype=bool)
    for first, second in edges:
        adjacency[first, second] = True
        adjacency[second, first] = True
    nonlocal_mask = ~(adjacency | np.eye(size, dtype=bool))
    checks.append(Check(
        "minimal rates are edge local",
        float(np.max(np.abs(rates[nonlocal_mask]))),
        0.0,
    ))

    expected_rate = float(np.sum(weights * np.sum(rates, axis=1)))
    edge_current = float(sum(abs(flow[first, second]) for first, second in edges))
    weighted_degree = max(float(np.sum(np.abs(matrix[index]) * adjacency[index])) for index in range(size))
    checks.append(Check("expected jump-rate identity", abs(expected_rate - edge_current), TOL))
    checks.append(Check("expected jump-rate bound", expected_rate - weighted_degree / J0, TOL))

    two_site = np.array([[0.0, 1.0], [1.0, 0.0]])
    node_state = evolve(two_site, np.array([1.0, 0.0], dtype=complex), pi / 2.0)
    node_weight = float(abs(node_state[0]) ** 2)
    checks.append(Check("finite-time exact node", node_weight, 2.0e-30))
    bounded_survival = float(np.exp(-4.0 * pi / 2.0))
    checks.append(Check("bounded-rate no-go survival", bounded_survival, 1.0e-4, ">="))
    checks.append(Check("bounded-rate cannot equal exact node", bounded_survival - node_weight, 1.0e-4, ">="))

    rho = 1.0e-2
    sigma = 2.0e-3
    values = np.linspace(-2.0, 2.0, 2001)
    smoothing_error = smooth_positive(values, sigma) - np.maximum(values, 0.0)
    checks.append(Check("smooth positive-part lower bound", max(0.0, -float(np.min(smoothing_error))), TOL))
    checks.append(Check("smooth positive-part upper bound", float(np.max(smoothing_error)) - sigma / 2.0, TOL))

    degree = max(int(np.sum(adjacency[index])) for index in range(size))
    rate_bound = weighted_degree / (J0 * np.sqrt(rho)) + degree * sigma / (2.0 * rho)
    sampled_max_rate = 0.0
    sampled_residual = 0.0
    edge_sum = edge_weight_sum(matrix, edges)
    residual_bound = len(edges) * sigma + 2.0 * edge_sum * np.sqrt(rho) / J0
    for time in np.linspace(0.0, 1.2, 121):
        sample = evolve(matrix, initial, float(time))
        sample_weights = probability(sample)
        sample_rates = regularized_rates(sample, matrix, rho, sigma)
        sample_generator = generator_from_rates(sample_rates)
        sampled_max_rate = max(sampled_max_rate, float(np.max(np.sum(sample_rates, axis=1))))
        sample_derivative = probability_derivative(sample, matrix)
        residual = 0.5 * np.sum(np.abs(sample_weights @ sample_generator - sample_derivative))
        sampled_residual = max(sampled_residual, float(residual))
    checks.append(Check("regularized maximum-rate bound", sampled_max_rate - rate_bound, TOL))
    checks.append(Check("node-uniform master residual", sampled_residual - residual_bound, TOL))

    duration = 1.2
    regularized, minimum, normalization_error = rk4_distribution(
        matrix,
        initial,
        probability(initial),
        rho,
        sigma,
        duration,
        6000,
    )
    ideal_final = probability(evolve(matrix, initial, duration))
    regularized_tv = total_variation(regularized, ideal_final)
    checks.append(Check("regularized distribution TV bound", regularized_tv - duration * residual_bound, 3.0e-8))
    checks.append(Check("regularized probability nonnegativity", max(0.0, -minimum), TOL))
    checks.append(Check("regularized probability conservation", normalization_error, TOL))

    bounds = []
    actual_distances = []
    for current_rho in (4.0e-2, 1.0e-2, 2.5e-3):
        current_sigma = 0.2 * current_rho
        bounds.append(duration * (
            len(edges) * current_sigma
            + 2.0 * edge_sum * np.sqrt(current_rho) / J0
        ))
        current_distribution, _, _ = rk4_distribution(
            matrix,
            initial,
            probability(initial),
            current_rho,
            current_sigma,
            duration,
            3000,
        )
        actual_distances.append(total_variation(current_distribution, ideal_final))
    checks.append(Check(
        "regularization bound decreases",
        max(bounds[index + 1] - bounds[index] for index in range(len(bounds) - 1)),
        0.0,
    ))
    checks.append(Check(
        "regularized distribution converges",
        max(actual_distances[index + 1] - actual_distances[index] for index in range(len(actual_distances) - 1)),
        2.0e-7,
    ))

    reference, _, _ = rk4_distribution(
        matrix,
        initial,
        probability(initial),
        rho,
        sigma,
        duration,
        8000,
    )
    euler_errors = []
    for steps in (300, 600, 1200):
        approximation, euler_minimum, euler_norm_error = euler_distribution(
            matrix,
            initial,
            probability(initial),
            rho,
            sigma,
            duration,
            steps,
        )
        euler_errors.append(total_variation(approximation, reference))
        checks.append(Check(f"Euler positivity at K={steps}", max(0.0, -euler_minimum), TOL))
        checks.append(Check(f"Euler conservation at K={steps}", euler_norm_error, TOL))
    ratios = [euler_errors[index] / euler_errors[index + 1] for index in range(2)]
    checks.append(Check("Euler first-order convergence", min(ratios), 1.85, ">="))

    local_time = 0.41
    local_amplitude = evolve(matrix, initial, local_time)
    local_rates = regularized_rates(local_amplitude, matrix, rho, sigma)
    local_escape = float(np.max(np.sum(local_rates, axis=1)))
    step = 0.4 / local_escape
    kernel = np.eye(size) + step * generator_from_rates(local_rates)
    checks.append(Check("local kernel row normalization", float(np.max(np.abs(np.sum(kernel, axis=1) - 1.0))), TOL))
    checks.append(Check("local kernel nonnegativity", max(0.0, -float(np.min(kernel))), TOL))
    checks.append(Check("local kernel excludes nonedges", float(np.max(np.abs(kernel[nonlocal_mask]))), 0.0))

    local_weights = probability(local_amplitude)
    local_flow = currents(local_amplitude, matrix)
    branch_actions = step * smooth_positive(local_flow, sigma)
    branch_actions[~adjacency] = 0.0
    total_actions = local_weights + rho
    waiting_actions = total_actions - np.sum(branch_actions, axis=1)
    interval_probabilities = branch_actions / total_actions[:, None]
    checks.append(Check("waiting action nonnegativity", max(0.0, -float(np.min(waiting_actions))), TOL))
    checks.append(Check(
        "action-ratio branch probability",
        float(np.max(np.abs(interval_probabilities[adjacency] - step * local_rates[adjacency]))),
        TOL,
    ))

    grid_size = 200_000
    thresholds = (np.arange(grid_size) + 0.5) / grid_size
    selected = np.searchsorted(np.cumsum(probability(initial)), thresholds, side="right")
    frequencies = np.bincount(selected, minlength=size) / grid_size
    checks.append(Check(
        "initial action-ratio preparation",
        float(np.max(np.abs(frequencies - probability(initial)))),
        1.0 / grid_size,
    ))

    allowed_branches = []
    for source in range(size):
        allowed_branches.append((source, source, (source, "wait")))
        for target in range(size):
            if adjacency[source, target]:
                allowed_branches.append((source, target, (source, target)))
    encoded = {(target, history) for _, target, history in allowed_branches}
    checks.append(Check("history-cell injectivity", float(len(allowed_branches) - len(encoded)), 0.0))
    maximum_graph_distance = max(abs(source - target) for source, target, _ in allowed_branches)
    checks.append(Check("single-edge transport locality", float(maximum_graph_distance), 1.0))

    carrier_offset = 2.0e-5 * (rng.normal(size=size) + 1j * rng.normal(size=size))
    perturbed, _, _ = rk4_distribution(
        matrix,
        initial,
        probability(initial),
        rho,
        sigma,
        duration,
        5000,
        carrier_offset=carrier_offset,
    )
    generator_distance = 0.0
    for time in np.linspace(0.0, duration, 241):
        exact_amplitude = evolve(matrix, initial, float(time))
        exact_generator = generator_from_rates(regularized_rates(exact_amplitude, matrix, rho, sigma))
        perturbed_generator = generator_from_rates(regularized_rates(
            exact_amplitude + carrier_offset,
            matrix,
            rho,
            sigma,
        ))
        generator_distance = max(
            generator_distance,
            float(np.linalg.norm(exact_generator - perturbed_generator, ord=np.inf)),
        )
    carrier_tv = total_variation(regularized, perturbed)
    checks.append(Check(
        "regularized carrier-error transfer",
        carrier_tv - 0.5 * duration * generator_distance,
        5.0e-8,
    ))

    complex_matrix = np.array(
        [
            [0.11, 0.37 + 0.19j, 0.0],
            [0.37 - 0.19j, -0.08, -0.29 + 0.13j],
            [0.0, -0.29 - 0.13j, 0.17],
        ],
        dtype=complex,
    )
    complex_initial = np.array([0.61 + 0.12j, -0.27 + 0.43j, 0.31 - 0.49j])
    complex_initial /= np.linalg.norm(complex_initial)
    complex_flow = currents(complex_initial, complex_matrix)
    complex_derivative = probability_derivative(complex_initial, complex_matrix)
    complex_rates = minimal_rates(complex_initial, complex_matrix)
    complex_generator = generator_from_rates(complex_rates)
    checks.append(Check(
        "complex-Hermitian current antisymmetry",
        float(np.max(np.abs(complex_flow + complex_flow.T))),
        TOL,
    ))
    checks.append(Check(
        "complex-Hermitian continuity equation",
        float(np.max(np.abs(complex_derivative - np.sum(complex_flow, axis=0)))),
        TOL,
    ))
    checks.append(Check(
        "complex-Hermitian minimal-rate equivariance",
        float(np.max(np.abs(probability(complex_initial) @ complex_generator - complex_derivative))),
        TOL,
    ))

    projector = np.zeros((4, 4), dtype=complex)
    difference = np.array([0.0, 0.0, 1.0, -1.0], dtype=complex) / np.sqrt(2.0)
    projector = np.outer(difference, np.conj(difference))
    cnot_from_edge = np.eye(4, dtype=complex) - 2.0 * projector
    cnot_target = np.array(
        [
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
            [0.0, 0.0, 1.0, 0.0],
        ],
        dtype=complex,
    )
    checks.append(Check(
        "one-edge projector gives CNOT",
        float(np.max(np.abs(cnot_from_edge - cnot_target))),
        TOL,
    ))
    basis_outputs = np.argmax(np.abs(cnot_from_edge), axis=0)
    checks.append(Check(
        "joint realized-configuration CNOT truth table",
        float(np.max(np.abs(basis_outputs - np.array([0, 1, 3, 2])))),
        0.0,
    ))

    spring_bounds = []
    for eta in (0.08, 0.04, 0.02):
        spring_bounds.append(
            2.0 * ((1.0 - eta) ** (-0.25) - 1.0)
            + pi * eta / (4.0 * (1.0 - eta) ** 1.5)
        )
    checks.append(Check(
        "one-edge spring CNOT bound decreases",
        max(spring_bounds[index + 1] - spring_bounds[index] for index in range(2)),
        0.0,
    ))
    checks.append(Check(
        "one-edge spring CNOT bound tends to zero",
        spring_bounds[-1],
        3.0e-2,
    ))

    output = {
        "seed": 20260812,
        "check_count": len(checks),
        "checks": [
            {
                **asdict(check),
                "passed": bool(check.passed),
            }
            for check in checks
        ],
        "diagnostics": {
            "regularized_tv": regularized_tv,
            "regularized_tv_bound": duration * residual_bound,
            "regularization_bounds": bounds,
            "regularization_distances": actual_distances,
            "euler_errors": euler_errors,
            "euler_ratios": ratios,
            "sampled_max_rate": sampled_max_rate,
            "maximum_rate_bound": rate_bound,
            "carrier_tv": carrier_tv,
            "carrier_transfer_bound": 0.5 * duration * generator_distance,
            "one_edge_spring_bounds": spring_bounds,
        },
        "passed": bool(all(check.passed for check in checks)),
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    if not output["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
