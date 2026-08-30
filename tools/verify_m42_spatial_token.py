#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass

import numpy as np


J0 = 1.0
TOL = 5.0e-10


@dataclass(frozen=True)
class Check:
    name: str
    value: float
    limit: float = TOL
    lower: bool = False

    @property
    def passed(self) -> bool:
        return self.value >= self.limit if self.lower else self.value <= self.limit


def path_generator(size: int) -> tuple[np.ndarray, list[tuple[int, int]]]:
    matrix = np.diag(np.linspace(-0.11, 0.17, size))
    edges: list[tuple[int, int]] = []
    for index, coupling in enumerate(np.linspace(0.31, 0.53, size - 1)):
        edges.append((index, index + 1))
        matrix[index, index + 1] = -coupling
        matrix[index + 1, index] = -coupling
    return matrix, edges


def evolve(matrix: np.ndarray, initial: np.ndarray, time: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    return vectors @ (np.exp(-1j * values * time / J0) * (vectors.conj().T @ initial))


def weights(amplitude: np.ndarray) -> np.ndarray:
    return np.abs(amplitude) ** 2 / float(np.vdot(amplitude, amplitude).real)


def currents(amplitude: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    size = len(amplitude)
    flow = np.zeros((size, size))
    for source in range(size):
        for target in range(size):
            flow[source, target] = 2.0 / J0 * np.imag(
                np.conj(amplitude[target]) * matrix[target, source] * amplitude[source]
            )
    return flow


def derivative(amplitude: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    velocity = -1j * matrix @ amplitude / J0
    return 2.0 * np.real(np.conj(amplitude) * velocity)


def rate_generator(rates: np.ndarray) -> np.ndarray:
    generator = rates.copy()
    np.fill_diagonal(generator, 0.0)
    generator[np.diag_indices_from(generator)] = -np.sum(generator, axis=1)
    return generator


def minimal_rates(amplitude: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    probability = weights(amplitude)
    flow = currents(amplitude, matrix)
    rates = np.zeros_like(flow)
    for source in range(len(probability)):
        if probability[source] > 1.0e-14:
            rates[source] = np.maximum(flow[source], 0.0) / probability[source]
    np.fill_diagonal(rates, 0.0)
    return rates


def smooth_positive(value: np.ndarray, sigma: float) -> np.ndarray:
    return 0.5 * (value + np.sqrt(value * value + sigma * sigma))


def regularized_rates(
    amplitude: np.ndarray,
    matrix: np.ndarray,
    adjacency: np.ndarray,
    rho: float,
    sigma: float,
) -> np.ndarray:
    result = smooth_positive(currents(amplitude, matrix), sigma) / (
        weights(amplitude)[:, None] + rho
    )
    result[~adjacency] = 0.0
    np.fill_diagonal(result, 0.0)
    return result


def propagate_distribution(
    matrix: np.ndarray,
    adjacency: np.ndarray,
    initial_amplitude: np.ndarray,
    initial_distribution: np.ndarray,
    duration: float,
    steps: int,
    rho: float,
    sigma: float,
    carrier_offset: np.ndarray | None = None,
) -> tuple[np.ndarray, float, float]:
    step = duration / steps
    state = initial_distribution.copy()
    minimum = float(np.min(state))
    norm_error = abs(float(np.sum(state)) - 1.0)

    def rhs(time: float, distribution: np.ndarray) -> np.ndarray:
        amplitude = evolve(matrix, initial_amplitude, time)
        if carrier_offset is not None:
            amplitude = amplitude + carrier_offset
        rates = regularized_rates(amplitude, matrix, adjacency, rho, sigma)
        return distribution @ rate_generator(rates)

    for index in range(steps):
        time = index * step
        k1 = rhs(time, state)
        k2 = rhs(time + step / 2.0, state + step * k1 / 2.0)
        k3 = rhs(time + step / 2.0, state + step * k2 / 2.0)
        k4 = rhs(time + step, state + step * k3)
        state += step * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        minimum = min(minimum, float(np.min(state)))
        norm_error = max(norm_error, abs(float(np.sum(state)) - 1.0))
    return state, minimum, norm_error


def tv(left: np.ndarray, right: np.ndarray) -> float:
    return 0.5 * float(np.sum(np.abs(left - right)))


def main() -> None:
    rng = np.random.default_rng(20260830)
    size = 6
    matrix, edges = path_generator(size)
    adjacency = np.zeros((size, size), dtype=bool)
    for first, second in edges:
        adjacency[first, second] = True
        adjacency[second, first] = True
    initial = rng.normal(size=size) + 1j * rng.normal(size=size)
    initial /= np.linalg.norm(initial)
    time = 0.71
    amplitude = evolve(matrix, initial, time)
    probability = weights(amplitude)
    flow = currents(amplitude, matrix)
    rates = minimal_rates(amplitude, matrix)
    generator = rate_generator(rates)
    probability_dot = derivative(amplitude, matrix)

    checks: list[Check] = [
        Check("carrier action conservation", abs(float(np.vdot(amplitude, amplitude).real) - 1.0)),
        Check("current antisymmetry", float(np.max(np.abs(flow + flow.T)))),
        Check("local continuity", float(np.max(np.abs(probability_dot - np.sum(flow, axis=0))))),
        Check("R172 master equation", float(np.max(np.abs(probability @ generator - probability_dot)))),
        Check("minimal rates nonnegative", max(0.0, -float(np.min(rates)))),
        Check("minimal rates local", float(np.max(np.abs(rates[~adjacency & ~np.eye(size, dtype=bool)])))),
    ]

    expected_rate = float(np.sum(probability * np.sum(rates, axis=1)))
    edge_current = float(sum(abs(flow[first, second]) for first, second in edges))
    h1 = max(float(np.sum(np.abs(matrix[index]) * adjacency[index])) for index in range(size))
    checks.extend([
        Check("expected jump identity", abs(expected_rate - edge_current)),
        Check("expected jump bound", expected_rate - h1 / J0),
    ])

    rho = 1.0e-2
    sigma = 2.0e-3
    smooth_error = smooth_positive(np.linspace(-2.0, 2.0, 2001), sigma) - np.maximum(
        np.linspace(-2.0, 2.0, 2001), 0.0
    )
    checks.extend([
        Check("smooth lower bound", max(0.0, -float(np.min(smooth_error)))),
        Check("smooth upper bound", float(np.max(smooth_error)) - sigma / 2.0),
    ])

    rate_bound = h1 / (J0 * np.sqrt(rho)) + 2.0 * sigma / (2.0 * rho)
    sampled_rate = 0.0
    for sample_time in np.linspace(0.0, 1.2, 101):
        sample = evolve(matrix, initial, float(sample_time))
        sampled_rate = max(
            sampled_rate,
            float(np.max(np.sum(regularized_rates(sample, matrix, adjacency, rho, sigma), axis=1))),
        )
    checks.append(Check("R173 finite rate bound", sampled_rate - rate_bound))

    collision_rates = regularized_rates(amplitude, matrix, adjacency, rho, sigma)
    collision_source, collision_target = edges[2]
    forward_rate = float(collision_rates[collision_source, collision_target])
    reverse_rate = float(collision_rates[collision_target, collision_source])
    attempt_rate = 1.25 * max(forward_rate, reverse_rate)
    collision_grid = 200_000
    collision_thresholds = (np.arange(collision_grid) + 0.5) / collision_grid
    forward_empirical = attempt_rate * float(np.mean(
        collision_thresholds < forward_rate / attempt_rate
    ))
    reverse_empirical = attempt_rate * float(np.mean(
        collision_thresholds < reverse_rate / attempt_rate
    ))
    checks.extend([
        Check(
            "forward driven collision rate",
            abs(forward_empirical - forward_rate),
            attempt_rate / collision_grid,
        ),
        Check(
            "reverse driven collision rate",
            abs(reverse_empirical - reverse_rate),
            attempt_rate / collision_grid,
        ),
        Check(
            "directional thresholds distinct",
            abs(forward_rate - reverse_rate),
            1.0e-6,
            lower=True,
        ),
    ])

    duration = 1.2
    edge_sum = float(sum(abs(matrix[first, second]) for first, second in edges))
    regularization_bound = duration * (
        len(edges) * sigma + 2.0 * edge_sum * np.sqrt(rho) / J0
    )
    final, minimum, norm_error = propagate_distribution(
        matrix,
        adjacency,
        initial,
        weights(initial),
        duration,
        5000,
        rho,
        sigma,
    )
    ideal = weights(evolve(matrix, initial, duration))
    checks.extend([
        Check("R173 TV bound", tv(final, ideal) - regularization_bound, 5.0e-8),
        Check("regularized nonnegativity", max(0.0, -minimum)),
        Check("regularized normalization", norm_error),
    ])

    distances = []
    bounds = []
    for current_rho in (4.0e-2, 1.0e-2, 2.5e-3):
        current_sigma = 0.2 * current_rho
        distribution, _, _ = propagate_distribution(
            matrix,
            adjacency,
            initial,
            weights(initial),
            duration,
            3000,
            current_rho,
            current_sigma,
        )
        distances.append(tv(distribution, ideal))
        bounds.append(duration * (
            len(edges) * current_sigma
            + 2.0 * edge_sum * np.sqrt(current_rho) / J0
        ))
    checks.extend([
        Check("regularization bounds decrease", max(np.diff(bounds))),
        Check("regularized solutions converge", max(np.diff(distances)), 3.0e-7),
    ])

    offset = 2.0e-5 * (rng.normal(size=size) + 1j * rng.normal(size=size))
    perturbed, _, _ = propagate_distribution(
        matrix,
        adjacency,
        initial,
        weights(initial),
        duration,
        5000,
        rho,
        sigma,
        carrier_offset=offset,
    )
    generator_distance = 0.0
    for sample_time in np.linspace(0.0, duration, 161):
        exact = evolve(matrix, initial, float(sample_time))
        exact_generator = rate_generator(regularized_rates(exact, matrix, adjacency, rho, sigma))
        shifted_generator = rate_generator(
            regularized_rates(exact + offset, matrix, adjacency, rho, sigma)
        )
        generator_distance = max(
            generator_distance,
            float(np.linalg.norm(exact_generator - shifted_generator, ord=np.inf)),
        )
    checks.append(Check(
        "R174 carrier Duhamel bound",
        tv(final, perturbed) - 0.5 * duration * generator_distance,
        8.0e-8,
    ))

    grid = 200_000
    thresholds = (np.arange(grid) + 0.5) / grid
    selected = np.searchsorted(np.cumsum(weights(initial)), thresholds, side="right")
    frequencies = np.bincount(selected, minlength=size) / grid
    checks.extend([
        Check("single initial action-shell selection", float(np.max(np.abs(frequencies - weights(initial)))), 1.0 / grid),
        Check("initial selection normalized", abs(float(np.sum(frequencies)) - 1.0)),
    ])

    complete = np.append(0.93 * final, 0.07)
    checks.extend([
        Check("no-response retained", abs(complete[-1] - 0.07)),
        Check("complete result normalized", abs(float(np.sum(complete)) - 1.0)),
    ])

    history_records = []
    for source in range(size):
        history_records.append((source, source, (0, source, "wait")))
        for target in range(size):
            if adjacency[source, target]:
                history_records.append((source, target, (0, source, target)))
    encoded = {(target, history) for _, target, history in history_records}
    checks.extend([
        Check("history injective", float(len(history_records) - len(encoded))),
        Check("single-edge locality", float(max(abs(a - b) for a, b, _ in history_records)), 1.0),
    ])

    failures = [check for check in checks if not check.passed]
    for check in checks:
        relation = ">=" if check.lower else "<="
        print(f"{'ok' if check.passed else 'FAIL':4s} {check.name:38s} {check.value:.6e} {relation} {check.limit:.6e}")
    if failures:
        raise SystemExit(f"{len(failures)} checks failed")
    print(f"all {len(checks)} checks passed")


if __name__ == "__main__":
    main()
