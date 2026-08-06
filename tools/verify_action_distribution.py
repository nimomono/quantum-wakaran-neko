#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
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


def rotation(angle: float) -> np.ndarray:
    return np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)],
    ])


def random_unitary(rng: np.random.Generator, size: int) -> np.ndarray:
    matrix = rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))
    unitary, triangular = np.linalg.qr(matrix)
    diagonal = np.diag(triangular)
    phases = np.ones_like(diagonal)
    nonzero = np.abs(diagonal) > 0.0
    phases[nonzero] = diagonal[nonzero] / np.abs(diagonal[nonzero])
    return unitary @ np.diag(phases.conj())


def interval_outcomes(fractions: np.ndarray, shares: np.ndarray) -> np.ndarray:
    cumulative = np.cumsum(shares, axis=1)
    return np.sum(fractions[:, None] >= cumulative, axis=1)


def main() -> None:
    seed = 20260806
    rng = np.random.default_rng(seed)
    checks: list[CheckResult] = []

    sample_count = 120_000
    mode_count = 7

    # A fixed-action, high-rank ensemble. Each row is one trial amplitude.
    amplitudes = rng.normal(size=(sample_count, mode_count)) + 1j * rng.normal(
        size=(sample_count, mode_count)
    )
    amplitudes /= np.linalg.norm(amplitudes, axis=1)[:, None]
    correlation = amplitudes.T @ amplitudes.conj() / sample_count
    eigenvalues = np.linalg.eigvalsh(correlation)
    checks.append(record_min(
        "high_rank_second_eigenvalue",
        np.sort(eigenvalues)[-2],
        8.0e-2,
    ))

    action_shares = np.abs(amplitudes) ** 2
    selector_expectation = np.mean(action_shares, axis=0)
    correlation_diagonal = np.real(np.diag(correlation)) / np.trace(correlation).real
    checks.append(record_max(
        "fixed_action_selector_correlation_error",
        np.max(np.abs(selector_expectation - correlation_diagonal)),
        3.0e-14,
    ))

    uniform_fractions = rng.random(sample_count)
    outcomes = interval_outcomes(uniform_fractions, action_shares)
    empirical = np.bincount(outcomes, minlength=mode_count) / sample_count
    checks.append(record_max(
        "uniform_selector_empirical_error",
        np.max(np.abs(empirical - selector_expectation)),
        6.0e-3,
    ))

    # An arbitrary finite orthonormal basis has the same fixed-action formula.
    unitary = random_unitary(rng, mode_count)
    transformed = amplitudes @ unitary.T
    transformed_shares = np.abs(transformed) ** 2
    transformed_selector = np.mean(transformed_shares, axis=0)
    transformed_correlation = unitary @ correlation @ unitary.conj().T
    transformed_expected = np.real(np.diag(transformed_correlation)) / np.trace(
        transformed_correlation
    ).real
    checks.append(record_max(
        "unitary_basis_selector_error",
        np.max(np.abs(transformed_selector - transformed_expected)),
        3.0e-14,
    ))
    checks.append(record_max(
        "unitary_basis_action_normalization_error",
        np.max(np.abs(np.sum(transformed_shares, axis=1) - 1.0)),
        3.0e-14,
    ))

    # Variable total action: selector mean and correlation ratio differ by covariance.
    variable_count = 90_000
    total_action = np.exp(0.55 * rng.normal(size=variable_count))
    logits = rng.normal(size=(variable_count, 4))
    standardized_total = (total_action - np.mean(total_action)) / np.std(total_action)
    logits[:, 0] += 1.1 * standardized_total
    logits -= np.max(logits, axis=1)[:, None]
    shares = np.exp(logits)
    shares /= np.sum(shares, axis=1)[:, None]
    actions = total_action[:, None] * shares

    selector_probability = np.mean(shares, axis=0)
    ratio_of_means = np.mean(actions, axis=0) / np.mean(total_action)
    covariance = np.mean(
        (total_action - np.mean(total_action))[:, None]
        * (shares - np.mean(shares, axis=0)),
        axis=0,
    )
    covariance_corrected = ratio_of_means - covariance / np.mean(total_action)
    checks.append(record_max(
        "variable_action_covariance_identity_error",
        np.max(np.abs(selector_probability - covariance_corrected)),
        3.0e-14,
    ))
    checks.append(record_min(
        "variable_action_naive_ratio_mismatch",
        np.max(np.abs(selector_probability - ratio_of_means)),
        2.0e-2,
    ))

    # A selector correlated with the first share breaks interval-length sampling.
    biased_fractions = 0.5 * shares[:, 0]
    biased_outcomes = interval_outcomes(biased_fractions, shares)
    biased_empirical = np.bincount(biased_outcomes, minlength=shares.shape[1]) / variable_count
    checks.append(record_min(
        "conditional_selector_bias_detection",
        np.max(np.abs(biased_empirical - selector_probability)),
        2.0e-1,
    ))

    # The mass near comparison boundaries decreases with the comparator width.
    internal_boundaries = np.cumsum(action_shares, axis=1)[:, :-1]
    boundary_distance = np.min(
        np.abs(uniform_fractions[:, None] - internal_boundaries),
        axis=1,
    )
    widths = np.array([4.0e-2, 2.0e-2, 1.0e-2])
    boundary_masses = np.array([np.mean(boundary_distance <= width) for width in widths])
    checks.append(record_max(
        "finite_comparator_boundary_mass_monotonicity",
        np.max(np.diff(boundary_masses)),
        0.0,
    ))
    checks.append(record_max(
        "finite_comparator_small_width_mass",
        boundary_masses[-1],
        1.5e-1,
    ))

    # Cell probabilities already include cell volume after b_i=sqrt(dV)a_i.
    cell_count = 41
    cell_volume = 0.07
    continuous_amplitude = rng.normal(size=cell_count) + 1j * rng.normal(size=cell_count)
    continuous_amplitude /= np.sqrt(
        np.sum(np.abs(continuous_amplitude) ** 2) * cell_volume
    )
    canonical_amplitude = np.sqrt(cell_volume) * continuous_amplitude
    cell_correlation = np.outer(canonical_amplitude, canonical_amplitude.conj())
    cell_probability = np.real(np.diag(cell_correlation)) / np.trace(cell_correlation).real
    expected_cell_probability = np.abs(continuous_amplitude) ** 2 * cell_volume
    checks.append(record_max(
        "cell_volume_probability_error",
        np.max(np.abs(cell_probability - expected_cell_probability)),
        2.0e-14,
    ))

    # Antisymmetric Bell cross correlation and local rotations.
    bell_scale = 2.3
    xi_zero = sqrt(bell_scale / 2.0) * np.array([[0.0, 1.0], [-1.0, 0.0]])
    source_a = [np.array([1.0, 0.0]), np.array([0.0, 1.0])]
    source_b = [np.array([0.0, 1.0]), np.array([-1.0, 0.0])]
    reconstructed = sqrt(bell_scale / 2.0) * sum(
        np.outer(left, right) for left, right in zip(source_a, source_b)
    )
    checks.append(record_max(
        "antisymmetric_cross_correlation_factorization_error",
        np.max(np.abs(reconstructed - xi_zero)),
        2.0e-14,
    ))

    max_cosine_error = 0.0
    max_sum_error = 0.0
    max_marginal_action_error = 0.0
    labels = np.array([1.0, -1.0])
    for _ in range(1000):
        alpha_x, beta_y = rng.uniform(-pi, pi, size=2)
        xi = rotation(alpha_x) @ xi_zero @ rotation(beta_y).T
        branch_action = np.abs(xi) ** 2
        delta = 2.0 * (alpha_x - beta_y)
        expected = np.empty((2, 2))
        for ia, label_a in enumerate(labels):
            for ib, label_b in enumerate(labels):
                expected[ia, ib] = bell_scale * (
                    1.0 - label_a * label_b * np.cos(delta)
                ) / 4.0
        max_cosine_error = max(
            max_cosine_error,
            float(np.max(np.abs(branch_action - expected))),
        )
        max_sum_error = max(max_sum_error, abs(float(np.sum(branch_action)) - bell_scale))
        marginal = np.sum(branch_action, axis=1)
        max_marginal_action_error = max(
            max_marginal_action_error,
            float(np.max(np.abs(marginal - bell_scale / 2.0))),
        )
    checks.append(record_max("bell_cosine_branch_action_error", max_cosine_error, 3.0e-14))
    checks.append(record_max("bell_total_branch_action_error", max_sum_error, 3.0e-14))
    checks.append(record_max(
        "bell_marginal_branch_action_error",
        max_marginal_action_error,
        3.0e-14,
    ))

    # Common baseline sector density yields interval-length Bell probabilities.
    alpha_x, beta_y = 0.37, -0.29
    xi = rotation(alpha_x) @ xi_zero @ rotation(beta_y).T
    branch_action = np.abs(xi) ** 2
    ideal_joint = branch_action / np.sum(branch_action)
    delta = 2.0 * (alpha_x - beta_y)
    expected_joint = np.empty((2, 2))
    for ia, label_a in enumerate(labels):
        for ib, label_b in enumerate(labels):
            expected_joint[ia, ib] = (
                1.0 - label_a * label_b * np.cos(delta)
            ) / 4.0
    checks.append(record_max(
        "bell_common_baseline_probability_error",
        np.max(np.abs(ideal_joint - expected_joint)),
        2.0e-14,
    ))
    checks.append(record_max(
        "bell_no_signalling_marginal_error",
        max(
            np.max(np.abs(np.sum(ideal_joint, axis=0) - 0.5)),
            np.max(np.abs(np.sum(ideal_joint, axis=1) - 0.5)),
        ),
        2.0e-14,
    ))

    # Unequal baseline sector density distorts both the joint law and a marginal.
    unequal_baseline = np.array([[1.0, 1.4], [0.7, 1.8]])
    distorted_joint = unequal_baseline * branch_action
    distorted_joint /= np.sum(distorted_joint)
    checks.append(record_min(
        "bell_unequal_baseline_joint_distortion",
        np.max(np.abs(distorted_joint - expected_joint)),
        3.0e-2,
    ))
    checks.append(record_min(
        "bell_unequal_baseline_marginal_distortion",
        max(
            np.max(np.abs(np.sum(distorted_joint, axis=0) - 0.5)),
            np.max(np.abs(np.sum(distorted_joint, axis=1) - 0.5)),
        ),
        2.0e-2,
    ))

    # Standard planar settings attain 2 sqrt(2).
    def bell_correlation(angle_x: float, angle_y: float) -> float:
        return -np.cos(angle_x - angle_y)

    angle_x0, angle_x1 = 0.0, pi / 2.0
    angle_y0, angle_y1 = pi / 4.0, -pi / 4.0
    chsh = abs(
        bell_correlation(angle_x0, angle_y0)
        + bell_correlation(angle_x0, angle_y1)
        + bell_correlation(angle_x1, angle_y0)
        - bell_correlation(angle_x1, angle_y1)
    )
    checks.append(record_max(
        "chsh_tsirelson_value_error",
        abs(chsh - 2.0 * sqrt(2.0)),
        2.0e-14,
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
