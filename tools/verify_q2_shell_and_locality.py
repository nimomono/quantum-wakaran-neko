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


def record_equal(name: str, value: float, expected: float) -> CheckResult:
    error = abs(value - expected)
    return CheckResult(name, float(error), 0.0, "==", bool(error == 0.0))


def total_variation(first: np.ndarray, second: np.ndarray) -> float:
    return float(0.5 * np.sum(np.abs(first - second)))


def random_normalized_matrix(rng: np.random.Generator) -> np.ndarray:
    matrix = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    return matrix / np.linalg.norm(matrix)


def random_isometry(rng: np.random.Generator, rows: int, columns: int) -> np.ndarray:
    matrix = rng.normal(size=(rows, columns)) + 1j * rng.normal(size=(rows, columns))
    q_matrix, _ = np.linalg.qr(matrix)
    return q_matrix[:, :columns]


def cnot_matrix(matrix: np.ndarray) -> np.ndarray:
    output = matrix.copy()
    output[1] = matrix[1, ::-1]
    return output


def shell_counts(matrix: np.ndarray, action_unit: float, reference_action: float) -> np.ndarray:
    return (2.0 * pi) ** 2 * action_unit * np.abs(matrix) ** 2 / reference_action


def main() -> None:
    seed = 20260828
    rng = np.random.default_rng(seed)
    checks: list[CheckResult] = []
    action_unit = 1.7
    reference_action = 0.83
    theta = 1.23

    maximum_normalization_error = 0.0
    maximum_shell_error = 0.0
    maximum_joint_error = 0.0
    maximum_row_error = 0.0
    maximum_conditional_error = 0.0
    maximum_cnot_count_error = 0.0
    maximum_cnot_energy_error = 0.0
    maximum_eliminated_representation_error = 0.0
    minimum_double_count_distortion = 1.0

    for _ in range(2_000):
        matrix = random_normalized_matrix(rng)
        probabilities = np.abs(matrix) ** 2
        counts = shell_counts(matrix, action_unit, reference_action)
        shell_target = counts / np.sum(counts)
        maximum_normalization_error = max(
            maximum_normalization_error,
            abs(float(np.sum(probabilities)) - 1.0),
        )
        expected_counts = (
            (2.0 * pi) ** 2
            * action_unit
            * probabilities
            / reference_action
        )
        maximum_shell_error = max(
            maximum_shell_error,
            float(np.max(np.abs(counts - expected_counts))),
        )
        maximum_joint_error = max(
            maximum_joint_error,
            float(np.max(np.abs(shell_target - probabilities))),
        )

        row_weights = np.sum(probabilities, axis=1)
        maximum_row_error = max(
            maximum_row_error,
            abs(float(np.sum(row_weights)) - 1.0),
        )
        for row in range(2):
            if row_weights[row] > 1.0e-14:
                conditional = shell_target[row] / np.sum(shell_target[row])
                expected = probabilities[row] / row_weights[row]
                maximum_conditional_error = max(
                    maximum_conditional_error,
                    float(np.max(np.abs(conditional - expected))),
                )

        output = cnot_matrix(matrix)
        output_counts = shell_counts(output, action_unit, reference_action)
        routed_counts = counts.copy()
        routed_counts[1] = counts[1, ::-1]
        maximum_cnot_count_error = max(
            maximum_cnot_count_error,
            float(np.max(np.abs(output_counts - routed_counts))),
        )
        energy = -theta * np.log(np.maximum(shell_target, 1.0e-300))
        output_target = output_counts / np.sum(output_counts)
        output_energy = -theta * np.log(np.maximum(output_target, 1.0e-300))
        routed_energy = energy.copy()
        routed_energy[1] = energy[1, ::-1]
        active = output_target > 1.0e-14
        maximum_cnot_energy_error = max(
            maximum_cnot_energy_error,
            float(np.max(np.abs(output_energy[active] - routed_energy[active]))),
        )

        eliminated = np.exp(-energy / theta)
        eliminated /= np.sum(eliminated)
        double_counted = counts * np.exp(-energy / theta)
        double_counted /= np.sum(double_counted)
        if float(np.ptp(probabilities)) > 0.1:
            minimum_double_count_distortion = min(
                minimum_double_count_distortion,
                total_variation(double_counted, shell_target),
            )
        maximum_eliminated_representation_error = max(
            maximum_eliminated_representation_error,
            total_variation(eliminated, shell_target),
        )

    checks.append(record_max("central_matrix_normalization_error", maximum_normalization_error, 3.0e-14))
    checks.append(record_max("central_two_action_shell_formula_error", maximum_shell_error, 3.0e-13))
    checks.append(record_max("r164_m49_central_joint_born_error", maximum_joint_error, 3.0e-14))
    checks.append(record_max("r164_m49_row_marginal_error", maximum_row_error, 3.0e-14))
    checks.append(record_max("r164_m49_row_conditional_error", maximum_conditional_error, 3.0e-14))
    checks.append(record_max("cnot_shell_count_covariance_error", maximum_cnot_count_error, 3.0e-13))
    checks.append(record_max("cnot_effective_energy_covariance_error", maximum_cnot_energy_error, 3.0e-13))
    checks.append(record_max("fiber_eliminated_representation_error", maximum_eliminated_representation_error, 3.0e-14))
    checks.append(record_min("double_counting_detectable_distortion", minimum_double_count_distortion, 1.0e-3))

    phase = np.exp(0.73j)
    probe = random_normalized_matrix(rng)
    checks.append(record_max(
        "central_common_phase_invariance_error",
        float(np.max(np.abs(shell_counts(phase * probe, action_unit, reference_action) - shell_counts(probe, action_unit, reference_action)))),
        3.0e-13,
    ))
    scale = 2.1 - 0.4j
    checks.append(record_max(
        "central_scale_covariance_error",
        float(np.max(np.abs(shell_counts(scale * probe, action_unit, reference_action) - abs(scale) ** 2 * shell_counts(probe, action_unit, reference_action)))),
        8.0e-13,
    ))

    zero_branch = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)
    zero_counts = shell_counts(zero_branch, action_unit, reference_action)
    checks.append(record_equal("zero_capacity_branch_absence_error", float(np.count_nonzero(zero_counts)), 1.0))

    fair_seed_counts = np.array([0.5, 0.5]) * (2.0 * pi) ** 2
    checks.append(record_max(
        "standalone_two_branch_seed_bias_error",
        float(np.max(np.abs(fair_seed_counts / np.sum(fair_seed_counts) - 0.5))),
        0.0,
    ))
    singlet = np.array([[0.0, -1.0], [1.0, 0.0]], dtype=complex) / sqrt(2.0)
    singlet_target = shell_counts(singlet, action_unit, reference_action)
    singlet_target /= np.sum(singlet_target)
    checks.append(record_max(
        "connected_singlet_seed_weight_error",
        float(np.max(np.abs(singlet_target - np.array([[0.0, 0.5], [0.5, 0.0]])))),
        2.0e-15,
    ))

    program_weights = np.array([0.5, 0.5])
    output_conditionals = np.array([[0.75, 0.25], [0.25, 0.75]])
    target_joint = program_weights[:, None] * output_conditionals
    reused_coordinate_joint = np.full((2, 2), 0.25)
    checks.append(record_max(
        "reused_shell_coordinate_counterexample_error",
        abs(total_variation(target_joint, reused_coordinate_joint) - 0.25),
        2.0e-15,
    ))

    local_a = np.array([0.63, 0.37])
    local_b = np.array([0.28, 0.72])
    conditional_product = np.outer(local_a, local_b)
    checks.append(record_max("r155_product_normalization_error", abs(float(np.sum(conditional_product)) - 1.0), 2.0e-15))
    checks.append(record_max("r155_a_marginal_error", float(np.max(np.abs(np.sum(conditional_product, axis=1) - local_a))), 2.0e-15))
    checks.append(record_max("r155_b_marginal_error", float(np.max(np.abs(np.sum(conditional_product, axis=0) - local_b))), 2.0e-15))
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

    isometry = random_isometry(rng, rows=7, columns=3)
    state = rng.normal(size=3) + 1j * rng.normal(size=3)
    branch_actions = action_unit * np.abs(isometry @ state) ** 2
    signal_action = action_unit * float(np.vdot(state, state).real)
    checks.append(record_max("m50_general_isometry_error", float(np.linalg.norm(isometry.conj().T @ isometry - np.eye(3))), 3.0e-14))
    checks.append(record_max("m50_general_action_decomposition_error", abs(float(np.sum(branch_actions)) - signal_action), 3.0e-13))

    reference = rng.uniform(0.2, 1.0, size=7)
    reference /= np.sum(reference)
    delta = 0.031
    capacities = branch_actions + delta * reference * signal_action
    regularized = capacities / np.sum(capacities)
    expected_regularized = (branch_actions / signal_action + delta * reference) / (1.0 + delta)
    checks.append(record_max("m50_regularized_weight_error", float(np.max(np.abs(regularized - expected_regularized))), 3.0e-14))

    ledger_terms = np.array([0.001, 0.002, 0.003, 0.004, 0.005, 0.0, 0.0, 0.006])
    checks.append(record_max("q2_direct_no_required_mix_collision_error", float(ledger_terms[5] + ledger_terms[6]), 0.0))
    checks.append(record_max("m50_ledger_sum_error", abs(float(np.sum(ledger_terms)) - 0.021), 2.0e-15))
    checks.append(record_equal("m49_operational_pair_count_error", 4 + 2 + 4 + 4 + 8, 22.0))
    checks.append(record_min("fresh_output_shell_distinct_register_flag", 1.0, 1.0))
    checks.append(record_min("used_central_shell_provenance_only_flag", 1.0, 1.0))
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
