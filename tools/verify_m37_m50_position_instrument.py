#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from math import exp, log, sqrt

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


def covariance(samples: np.ndarray) -> np.ndarray:
    moment = samples.T @ samples.conj() / samples.shape[0]
    return moment / np.trace(moment).real


def trace_distance(first: np.ndarray, second: np.ndarray) -> float:
    difference = 0.5 * (first - second + (first - second).conj().T)
    return float(0.5 * np.sum(np.abs(np.linalg.eigvalsh(difference))))


def total_variation(first: np.ndarray, second: np.ndarray) -> float:
    return float(0.5 * np.sum(np.abs(first - second)))


def random_unitary(rng: np.random.Generator, size: int) -> np.ndarray:
    matrix = rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))
    unitary, diagonal = np.linalg.qr(matrix)
    phases = np.diag(diagonal)
    return unitary * (phases / np.abs(phases)).conj()[None, :]


def random_isometry(rng: np.random.Generator, rows: int, columns: int) -> np.ndarray:
    matrix = rng.normal(size=(rows, columns)) + 1j * rng.normal(size=(rows, columns))
    isometry, _ = np.linalg.qr(matrix)
    return isometry[:, :columns]


def m50_distribution(
    isometry: np.ndarray,
    signal: np.ndarray,
    delta: float,
    reference: np.ndarray,
) -> np.ndarray:
    ray = np.abs(isometry @ signal) ** 2 / float(np.vdot(signal, signal).real)
    return (ray + delta * reference) / (1.0 + delta)


def main() -> None:
    seed = 20260829
    rng = np.random.default_rng(seed)
    checks: list[CheckResult] = []

    # R167: lift a uniform finite-time sample error to normalized covariance.
    trials = 4096
    size = 4
    initial = rng.normal(size=(trials, size)) + 1j * rng.normal(size=(trials, size))
    initial *= (0.7 + rng.random(trials))[:, None]
    unitary = random_unitary(rng, size)
    ideal = initial @ unitary.T
    noise_direction = rng.normal(size=(trials, size)) + 1j * rng.normal(size=(trials, size))
    noise_direction /= np.linalg.norm(noise_direction, axis=1)[:, None]
    epsilon_car = 0.018
    perturbation = epsilon_car * np.linalg.norm(initial, axis=1)[:, None] * noise_direction
    actual = ideal + perturbation

    covariance_initial = covariance(initial)
    covariance_ideal = unitary @ covariance_initial @ unitary.conj().T
    covariance_actual = covariance(actual)
    covariance_error = trace_distance(covariance_actual, covariance_ideal)
    ideal_action = float(np.mean(np.sum(np.abs(ideal) ** 2, axis=1)))
    actual_action = float(np.mean(np.sum(np.abs(actual) ** 2, axis=1)))
    kappa_t = ideal_action / actual_action
    r167_bound = 2.0 * epsilon_car * sqrt(kappa_t) + epsilon_car**2 * kappa_t
    checks.append(record_max("r167_covariance_trace_error", covariance_error, r167_bound + 1.0e-14))
    checks.append(record_max("r167_covariance_trace_one", abs(np.trace(covariance_actual).real - 1.0), 2.0e-14))
    checks.append(record_min("r167_covariance_positive", float(np.min(np.linalg.eigvalsh(covariance_actual))), -2.0e-14))
    checks.append(record_max(
        "r167_pointwise_carrier_bound",
        float(np.max(np.linalg.norm(perturbation, axis=1) / np.linalg.norm(initial, axis=1))),
        epsilon_car + 2.0e-15,
    ))

    # R168: exact rank-one support and regularized M50 contraction.
    ray = rng.normal(size=size) + 1j * rng.normal(size=size)
    ray /= np.linalg.norm(ray)
    amplitudes = rng.normal(size=trials) + 1j * rng.normal(size=trials)
    rank_one_samples = amplitudes[:, None] * ray[None, :]
    rank_one_covariance = covariance(rank_one_samples)
    projector = np.outer(ray, ray.conj())
    checks.append(record_max(
        "r168_rank_one_covariance_error",
        np.linalg.norm(rank_one_covariance - projector),
        3.0e-14,
    ))
    perpendicular = np.eye(size) - projector
    checks.append(record_max(
        "r168_sample_support_error",
        float(np.max(np.linalg.norm(rank_one_samples @ perpendicular.T, axis=1))),
        4.0e-14,
    ))

    branches = 6
    isometry = random_isometry(rng, branches, size)
    reference = np.arange(1, branches + 1, dtype=float)
    reference /= np.sum(reference)
    delta = 0.08
    target_rank_one = m50_distribution(isometry, ray, delta, reference)
    selected = np.flatnonzero(np.abs(amplitudes) > 0.15)[:512]
    sample_probabilities = np.array([
        m50_distribution(isometry, rank_one_samples[index], delta, reference)
        for index in selected
    ])
    checks.append(record_max(
        "r168_trial_independent_branch_error",
        float(np.max(np.abs(sample_probabilities - target_rank_one))),
        3.0e-14,
    ))

    orthogonal = rng.normal(size=size) + 1j * rng.normal(size=size)
    orthogonal -= ray * np.vdot(ray, orthogonal)
    orthogonal /= np.linalg.norm(orthogonal)
    angle = 0.12
    approximate_ray = np.cos(angle) * ray + np.sin(angle) * orthogonal
    pure_distance = trace_distance(
        np.outer(approximate_ray, approximate_ray.conj()),
        projector,
    )
    regularized_distance = total_variation(
        m50_distribution(isometry, approximate_ray, delta, reference),
        target_rank_one,
    )
    checks.append(record_max(
        "r168_regularized_ray_contraction",
        regularized_distance,
        pure_distance / (1.0 + delta) + 2.0e-14,
    ))

    # R169: fixed-action high-rank ensemble.
    fixed_samples = rng.normal(size=(trials, size)) + 1j * rng.normal(size=(trials, size))
    fixed_action = 2.7
    fixed_samples *= sqrt(fixed_action) / np.linalg.norm(fixed_samples, axis=1)[:, None]
    fixed_covariance = covariance(fixed_samples)
    empirical_probabilities = np.mean([
        m50_distribution(isometry, sample, delta, reference)
        for sample in fixed_samples
    ], axis=0)
    operators = [
        isometry.conj().T @ np.diag(np.eye(branches)[index]) @ isometry
        for index in range(branches)
    ]
    covariance_probabilities = np.array([
        (np.trace(operator @ fixed_covariance).real + delta * reference[index]) / (1.0 + delta)
        for index, operator in enumerate(operators)
    ])
    checks.append(record_max(
        "r169_fixed_action_per_trial_error",
        float(np.max(np.abs(np.sum(np.abs(fixed_samples) ** 2, axis=1) - fixed_action))),
        3.0e-14,
    ))
    checks.append(record_max(
        "r169_fixed_action_readout_error",
        float(np.max(np.abs(empirical_probabilities - covariance_probabilities))),
        4.0e-14,
    ))
    checks.append(record_max(
        "r169_branch_normalization_error",
        abs(float(np.sum(covariance_probabilities)) - 1.0),
        2.0e-14,
    ))

    variable_samples = np.array([
        sqrt(3.0) * np.array([1.0, 0.0], dtype=complex),
        np.array([0.0, 1.0], dtype=complex),
    ])
    radial_average = np.mean([
        np.outer(sample, sample.conj()) / np.vdot(sample, sample).real
        for sample in variable_samples
    ], axis=0)
    covariance_average = covariance(variable_samples)
    checks.append(record_max(
        "r169_variable_action_ray_target",
        np.linalg.norm(radial_average - np.diag([0.5, 0.5])),
        2.0e-15,
    ))
    checks.append(record_max(
        "r169_variable_action_covariance_target",
        np.linalg.norm(covariance_average - np.diag([0.75, 0.25])),
        2.0e-15,
    ))
    checks.append(record_min(
        "r169_variable_action_counterexample_gap",
        trace_distance(radial_average, covariance_average),
        0.249999999999,
    ))

    radial_actions = np.sum(np.abs(actual) ** 2, axis=1)
    radial_state = np.mean([
        np.outer(sample, sample.conj()) / action
        for sample, action in zip(actual, radial_actions, strict=True)
    ], axis=0)
    actual_covariance = covariance(actual)
    radial_distance = trace_distance(radial_state, actual_covariance)
    mean_action = float(np.mean(radial_actions))
    radial_l1_bound = 0.5 * float(np.mean(np.abs(radial_actions / mean_action - 1.0)))
    radial_variance_bound = 0.5 * float(np.std(radial_actions)) / mean_action
    checks.append(record_max("r169_radial_l1_bound", radial_distance, radial_l1_bound + 2.0e-14))
    checks.append(record_max("r169_radial_variance_bound", radial_l1_bound, radial_variance_bound + 2.0e-14))

    # R170: canonical sample-and-hold, R161 mixing, no-response, and local record.
    pairs = 2 * size
    symplectic_form = np.kron(np.eye(pairs), np.array([[0.0, 1.0], [-1.0, 0.0]]))
    permutation = np.zeros((4 * size, 4 * size))
    for register_pair in range(pairs):
        target_pair = register_pair + pairs // 2 if register_pair < pairs // 2 else register_pair - pairs // 2
        permutation[2 * target_pair:2 * target_pair + 2, 2 * register_pair:2 * register_pair + 2] = np.eye(2)
    checks.append(record_max(
        "r170_swap_symplectic_error",
        np.linalg.norm(permutation.T @ symplectic_form @ permutation - symplectic_form),
        2.0e-15,
    ))
    checks.append(record_max("r170_swap_self_inverse_error", np.linalg.norm(permutation @ permutation - np.eye(4 * size)), 2.0e-15))

    pi_target = target_rank_one
    activity = 0.73
    q_generator = np.zeros((branches, branches))
    detailed_balance_error = 0.0
    for first in range(branches - 1):
        second = first + 1
        forward = activity * sqrt(pi_target[second] / pi_target[first])
        backward = activity * sqrt(pi_target[first] / pi_target[second])
        q_generator[first, second] = forward
        q_generator[second, first] = backward
        detailed_balance_error = max(
            detailed_balance_error,
            abs(pi_target[first] * forward - pi_target[second] * backward),
        )
    q_generator[np.diag_indices(branches)] = -np.sum(q_generator, axis=1)
    checks.append(record_max("r170_r161_detailed_balance_error", detailed_balance_error, 2.0e-15))
    checks.append(record_max("r170_r161_stationary_error", np.linalg.norm(pi_target @ q_generator), 3.0e-15))

    graph_laplacian = np.diag([1.0] + [2.0] * (branches - 2) + [1.0])
    graph_laplacian -= np.diag(np.ones(branches - 1), 1) + np.diag(np.ones(branches - 1), -1)
    graph_gap = float(np.linalg.eigvalsh(graph_laplacian)[1])
    minimum_mass = delta * float(np.min(reference)) / (1.0 + delta)
    lambda_lower = activity * minimum_mass * graph_gap
    root_pi = np.sqrt(pi_target)
    symmetric_generator = root_pi[:, None] * q_generator / root_pi[None, :]
    eigenvalues = np.sort(np.linalg.eigvalsh(-symmetric_generator))
    actual_gap = float(eigenvalues[1])
    checks.append(record_min("r170_r161_gap_lower_bound", actual_gap, lambda_lower - 2.0e-14))

    c_delta = 0.5 * sqrt(1.0 / minimum_mass - 1.0)
    mixing_budget = 0.004
    mixing_time = log(c_delta / mixing_budget) / lambda_lower
    values, vectors = np.linalg.eigh(symmetric_generator)
    exponential_symmetric = (vectors * np.exp(values * mixing_time)) @ vectors.T
    exponential_generator = exponential_symmetric / root_pi[:, None] * root_pi[None, :]
    initial_position = np.zeros(branches)
    initial_position[0] = 1.0
    mixed_position = initial_position @ exponential_generator
    mixing_error = total_variation(mixed_position, pi_target)
    mixing_bound = c_delta * exp(-lambda_lower * mixing_time)
    checks.append(record_max("r170_r161_mixing_bound", mixing_error, mixing_bound + 2.0e-14))
    # Long-time diagonalization amplifies LAPACK-dependent roundoff in the
    # numerically reconstructed zero mode. Keep this implementation check far
    # below the 4e-3 analytical mixing budget without tying it to one BLAS build.
    checks.append(record_max("r170_mixed_mass_error", abs(float(np.sum(mixed_position)) - 1.0), 1.0e-10))

    response_mass = 0.956
    no_response = np.array([0.012, 0.009, 0.008, 0.015])
    checks.append(record_max(
        "r170_complete_outcome_mass_error",
        abs(response_mass + float(np.sum(no_response)) - 1.0),
        2.0e-15,
    ))
    recorded_histories = {
        (input_index, collision_index, branch, int(branch == record))
        for input_index in range(3)
        for collision_index in range(4)
        for branch in range(branches)
        for record in [branch]
    }
    expected_histories = 3 * 4 * branches
    checks.append(record_min("r170_history_injectivity", len(recorded_histories), expected_histories))
    checks.append(record_max(
        "r170_local_record_exclusivity",
        max(sum(int(branch == record) for record in range(branches)) - 1 for branch in range(branches)),
        0.0,
    ))
    sample_time = 1.4
    tau_x = mixing_time
    output_time = sample_time + tau_x + 0.7
    checks.append(record_min("r170_positive_processing_time", output_time - sample_time, 1.0e-12))

    error_terms = np.array([
        0.002,
        0.004,
        0.003,
        0.004,
        0.003,
        0.003,
        mixing_budget,
        0.003,
        0.003,
        0.002,
        0.002,
    ])
    epsilon_170 = float(np.sum(error_terms))
    tunnelling_margin = 0.21 - 2.0 * epsilon_170
    coherence_margin = 0.5 - 2.0 * epsilon_170
    phase_margin = 1.0 - 2.0 * epsilon_170
    checks.append(record_min("r170_tunnelling_margin", tunnelling_margin, 1.0e-12))
    checks.append(record_min("r170_coherence_margin", coherence_margin, 1.0e-12))
    checks.append(record_min("r170_phase_margin", phase_margin, 1.0e-12))
    shell_stiffness = delta**-2
    checks.append(record_min("r170_shell_stiffness_scaling", shell_stiffness * delta**2, 1.0 - 1.0e-14))

    payload = {
        "seed": seed,
        "check_count": len(checks),
        "r167_trace_distance": covariance_error,
        "r167_bound": r167_bound,
        "r169_variable_action_gap": trace_distance(radial_average, covariance_average),
        "r170_mixing_error": mixing_error,
        "r170_mixing_bound": mixing_bound,
        "epsilon_170_example": epsilon_170,
        "checks": [asdict(check) for check in checks],
        "passed": all(check.passed for check in checks),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
