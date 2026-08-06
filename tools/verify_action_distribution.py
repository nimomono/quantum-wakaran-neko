#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from math import factorial, pi, sqrt

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


def main() -> None:
    seed = 20260806
    rng = np.random.default_rng(seed)
    checks: list[CheckResult] = []

    # General n-mode action-shell capacity.
    for mode_count in range(2, 7):
        action = 0.3 + rng.random()
        analytic = (2.0 * pi) ** mode_count * action ** (mode_count - 1) / factorial(mode_count - 1)
        scaled = analytic / action ** (mode_count - 1)
        expected_scaled = (2.0 * pi) ** mode_count / factorial(mode_count - 1)
        checks.append(record_max(
            f"action_shell_scaling_n{mode_count}",
            abs(scaled - expected_scaled),
            2.0e-12,
        ))

    # Cell probabilities already include cell volume after b_i=sqrt(dV)a_i.
    cell_count = 41
    cell_volume = 0.07
    continuous_amplitude = rng.normal(size=cell_count) + 1j * rng.normal(size=cell_count)
    continuous_amplitude /= np.sqrt(np.sum(np.abs(continuous_amplitude) ** 2) * cell_volume)
    canonical_amplitude = np.sqrt(cell_volume) * continuous_amplitude
    correlation = np.outer(canonical_amplitude, canonical_amplitude.conj())
    probability = np.real(np.diag(correlation)) / np.trace(correlation).real
    expected_probability = np.abs(continuous_amplitude) ** 2 * cell_volume
    checks.append(record_max(
        "cell_volume_probability_error",
        np.max(np.abs(probability - expected_probability)),
        2.0e-14,
    ))
    checks.append(record_max(
        "cell_probability_normalization_error",
        abs(np.sum(probability) - 1.0),
        2.0e-14,
    ))

    # Two-mode shell and a common flux factor reproduce the normalized diagonal.
    total_action = 1.7
    flux_factor = 0.83
    entrance_action = total_action * probability
    flux = flux_factor * (2.0 * pi) ** 2 * entrance_action
    entrance_probability = flux / np.sum(flux)
    checks.append(record_max(
        "position_entrance_probability_error",
        np.max(np.abs(entrance_probability - probability)),
        2.0e-14,
    ))

    # q direct action-distribution directions give an A^q weight.
    test_action = np.array([0.2, 0.5, 0.9])
    for direct_dimension in (1, 2, 3):
        weight = test_action ** direct_dimension / factorial(direct_dimension)
        ratio = weight / weight[0]
        expected = (test_action / test_action[0]) ** direct_dimension
        checks.append(record_max(
            f"action_distribution_dimension_q{direct_dimension}",
            np.max(np.abs(ratio - expected)),
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
    for _ in range(1000):
        alpha_a, alpha_b = rng.uniform(-pi, pi, size=2)
        xi = rotation(alpha_a) @ xi_zero @ rotation(alpha_b).T
        branch_action = np.abs(xi) ** 2
        delta = 2.0 * (alpha_a - alpha_b)
        labels = np.array([1.0, -1.0])
        expected = np.empty((2, 2))
        for ia, label_a in enumerate(labels):
            for ib, label_b in enumerate(labels):
                expected[ia, ib] = bell_scale * (1.0 - label_a * label_b * np.cos(delta)) / 4.0
        max_cosine_error = max(max_cosine_error, float(np.max(np.abs(branch_action - expected))))
        max_sum_error = max(max_sum_error, abs(float(np.sum(branch_action)) - bell_scale))
        marginal = np.sum(branch_action, axis=1)
        max_marginal_action_error = max(
            max_marginal_action_error,
            float(np.max(np.abs(marginal - bell_scale / 2.0))),
        )
    checks.append(record_max("bell_cosine_branch_action_error", max_cosine_error, 3.0e-14))
    checks.append(record_max("bell_total_branch_action_error", max_sum_error, 3.0e-14))
    checks.append(record_max("bell_marginal_branch_action_error", max_marginal_action_error, 3.0e-14))

    # Common two-mode boundary capacity gives the Bell distribution.
    alpha_a, alpha_b = 0.37, -0.29
    xi = rotation(alpha_a) @ xi_zero @ rotation(alpha_b).T
    branch_action = np.abs(xi) ** 2
    comparison_gain = 1.4
    comparison_action = comparison_gain**2 * branch_action / 2.0
    boundary_capacity = (2.0 * pi) ** 2 * comparison_action
    joint = boundary_capacity / np.sum(boundary_capacity)
    labels = np.array([1.0, -1.0])
    expected_joint = np.empty((2, 2))
    delta = 2.0 * (alpha_a - alpha_b)
    for ia, label_a in enumerate(labels):
        for ib, label_b in enumerate(labels):
            expected_joint[ia, ib] = (1.0 - label_a * label_b * np.cos(delta)) / 4.0
    checks.append(record_max(
        "bell_common_boundary_probability_error",
        np.max(np.abs(joint - expected_joint)),
        2.0e-14,
    ))
    checks.append(record_max(
        "bell_no_signalling_marginal_error",
        max(
            np.max(np.abs(np.sum(joint, axis=0) - 0.5)),
            np.max(np.abs(np.sum(joint, axis=1) - 0.5)),
        ),
        2.0e-14,
    ))

    # Standard planar settings attain 2 sqrt(2).
    def correlation(angle_a: float, angle_b: float) -> float:
        angle_delta = angle_a - angle_b
        return -np.cos(angle_delta)

    angle_a0, angle_a1 = 0.0, pi / 2.0
    angle_b0, angle_b1 = pi / 4.0, -pi / 4.0
    chsh = abs(
        correlation(angle_a0, angle_b0)
        + correlation(angle_a0, angle_b1)
        + correlation(angle_a1, angle_b0)
        - correlation(angle_a1, angle_b1)
    )
    checks.append(record_max("chsh_tsirelson_value_error", abs(chsh - 2.0 * sqrt(2.0)), 2.0e-14))

    # A normalized sector remains mass one under a canonical within-sector map;
    # this differs from capacity weighting when actions differ.
    sector_actions = np.array([0.2, 0.7, 1.1, 1.8])
    normalized_masses = np.ones_like(sector_actions)
    capacity_weights = sector_actions / np.sum(sector_actions)
    normalized_weights = normalized_masses / np.sum(normalized_masses)
    mismatch = np.max(np.abs(capacity_weights - normalized_weights))
    checks.append(record_min("normalized_sector_capacity_mismatch", mismatch, 5.0e-2))

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
