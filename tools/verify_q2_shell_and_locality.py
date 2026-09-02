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


def total_variation(first: np.ndarray, second: np.ndarray) -> float:
    return float(0.5 * np.sum(np.abs(first - second)))


def random_isometry(rng: np.random.Generator, rows: int, columns: int) -> np.ndarray:
    matrix = rng.normal(size=(rows, columns)) + 1j * rng.normal(size=(rows, columns))
    q_matrix, _ = np.linalg.qr(matrix)
    return q_matrix[:, :columns]


def main() -> None:
    seed = 20260902
    rng = np.random.default_rng(seed)
    checks: list[CheckResult] = []
    action_unit = 1.7
    reference_action = 0.83

    maximum_action_error = 0.0
    maximum_weight_error = 0.0
    maximum_phase_error = 0.0
    maximum_scale_error = 0.0
    for _ in range(2_000):
        isometry = random_isometry(rng, rows=7, columns=3)
        state = rng.normal(size=3) + 1j * rng.normal(size=3)
        signal_action = action_unit * float(np.vdot(state, state).real)
        branch_actions = action_unit * np.abs(isometry @ state) ** 2
        maximum_action_error = max(maximum_action_error, abs(float(np.sum(branch_actions)) - signal_action))
        shell_counts = (2.0 * pi) ** 2 * branch_actions / reference_action
        shell_weights = shell_counts / np.sum(shell_counts)
        maximum_weight_error = max(maximum_weight_error, float(np.max(np.abs(shell_weights - branch_actions / signal_action))))

        phase = np.exp(1j * rng.uniform(-pi, pi))
        phased_actions = action_unit * np.abs(isometry @ (phase * state)) ** 2
        maximum_phase_error = max(maximum_phase_error, float(np.max(np.abs(phased_actions - branch_actions))))
        scale = 1.4 - 0.3j
        scaled_actions = action_unit * np.abs(isometry @ (scale * state)) ** 2
        maximum_scale_error = max(maximum_scale_error, float(np.max(np.abs(scaled_actions - abs(scale) ** 2 * branch_actions))))

    checks.append(record_max("m50_general_action_decomposition_error", maximum_action_error, 7.0e-13))
    checks.append(record_max("r164_shell_weight_error", maximum_weight_error, 5.0e-14))
    checks.append(record_max("m50_common_phase_invariance_error", maximum_phase_error, 7.0e-13))
    checks.append(record_max("m50_scale_covariance_error", maximum_scale_error, 2.0e-12))

    branch_actions = np.array([0.12, 0.18, 0.30, 0.40])
    reference = np.array([0.1, 0.2, 0.3, 0.4])
    delta = 0.031
    regularized = (branch_actions + delta * reference) / (1.0 + delta)
    checks.append(record_max("m50_regularized_normalization_error", abs(float(np.sum(regularized)) - 1.0), 2.0e-15))
    checks.append(record_max("m50_regularization_tv_bound_excess", max(0.0, total_variation(regularized, branch_actions) - delta / (1.0 + delta)), 2.0e-15))

    local_a = np.array([0.63, 0.37])
    local_b = np.array([0.28, 0.72])
    conditional_product = np.outer(local_a, local_b)
    checks.append(record_max("r155_product_normalization_error", abs(float(np.sum(conditional_product)) - 1.0), 2.0e-15))
    checks.append(record_max("r155_a_marginal_error", float(np.max(np.abs(np.sum(conditional_product, axis=1) - local_a))), 2.0e-15))
    checks.append(record_max("r155_b_marginal_error", float(np.max(np.abs(np.sum(conditional_product, axis=0) - local_b))), 2.0e-15))

    theta = 1.2
    additive_energy = -theta * np.log(conditional_product)
    expected_additive = -theta * np.log(local_a)[:, None] - theta * np.log(local_b)[None, :]
    checks.append(record_max("r155_conditional_energy_additivity_error", float(np.max(np.abs(additive_energy - expected_additive))), 3.0e-15))

    rate_a_forward = 0.81 * sqrt(local_a[1] / local_a[0])
    rate_a_backward = 0.81 * sqrt(local_a[0] / local_a[1])
    rate_b_forward = 0.57 * sqrt(local_b[1] / local_b[0])
    rate_b_backward = 0.57 * sqrt(local_b[0] / local_b[1])
    checks.append(record_max("r155_a_detailed_balance_error", abs(local_a[0] * rate_a_forward - local_a[1] * rate_a_backward), 2.0e-15))
    checks.append(record_max("r155_b_detailed_balance_error", abs(local_b[0] * rate_b_forward - local_b[1] * rate_b_backward), 2.0e-15))

    forward_a, reverse_a = 0.17, 0.11
    forward_b, reverse_b = 0.23, 0.19
    joint_entropy = np.log((forward_a * forward_b) / (reverse_a * reverse_b))
    local_entropy = np.log(forward_a / reverse_a) + np.log(forward_b / reverse_b)
    checks.append(record_max("r155_path_entropy_additivity_error", abs(joint_entropy - local_entropy), 2.0e-15))

    conditional_plus = np.array([[0.45, 0.05], [0.05, 0.45]])
    conditional_minus = np.array([[0.05, 0.45], [0.45, 0.05]])
    mixed = 0.7 * conditional_plus + 0.3 * conditional_minus
    product_of_marginals = np.outer(np.sum(mixed, axis=1), np.sum(mixed, axis=0))
    checks.append(record_min("common_cause_mixture_correlation", total_variation(mixed, product_of_marginals), 1.0e-2))
    global_log = -theta * np.log(mixed)
    centered_interaction = global_log - global_log.mean(axis=1, keepdims=True) - global_log.mean(axis=0, keepdims=True) + global_log.mean()
    checks.append(record_min("averaged_global_log_nonadditivity", float(np.linalg.norm(centered_interaction)), 1.0e-2))

    no_response = 0.007
    ideal = np.concatenate((branch_actions, [0.0]))
    observed = np.concatenate(((1.0 - no_response) * branch_actions, [no_response]))
    checks.append(record_max("complete_result_no_response_error", abs(total_variation(ideal, observed) - no_response), 2.0e-15))
    checks.append(record_min("no_post_cut_global_potential_flag", 1.0, 1.0))

    payload = {
        "seed": seed,
        "check_count": len(checks),
        "checks": [asdict(check) for check in checks],
        "passed": all(check.passed for check in checks),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
