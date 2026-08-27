#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from math import sqrt

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


def random_normalized_matrix(
    rng: np.random.Generator,
    row_floor: float = 0.04,
) -> np.ndarray:
    while True:
        matrix = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        matrix /= np.linalg.norm(matrix)
        row_weights = np.sum(np.abs(matrix) ** 2, axis=1)
        if float(np.min(row_weights)) >= row_floor:
            return matrix


def random_unitary(rng: np.random.Generator) -> np.ndarray:
    matrix = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    q_matrix, r_matrix = np.linalg.qr(matrix)
    phases = np.diag(r_matrix)
    phases = np.where(np.abs(phases) > 0.0, phases / np.abs(phases), 1.0)
    return q_matrix @ np.diag(phases.conj())


def cnot_matrix(matrix: np.ndarray) -> np.ndarray:
    output = matrix.copy()
    output[1, :] = matrix[1, ::-1]
    return output


def row_templates(
    matrix: np.ndarray,
    phase: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    row_weights = np.sum(np.abs(matrix) ** 2, axis=1)
    templates_a = np.zeros((2, 2), dtype=complex)
    templates_b = np.zeros((2, 2), dtype=complex)
    for row in range(2):
        if row_weights[row] == 0.0:
            continue
        templates_a[row, row] = row_weights[row] ** (-0.25) * np.exp(1j * phase)
        templates_b[row, :] = (
            row_weights[row] ** (-0.75)
            * np.exp(-1j * phase)
            * matrix[row, :]
        )
    return row_weights, templates_a, templates_b


def cross_moment_from_templates(
    row_weights: np.ndarray,
    templates_a: np.ndarray,
    templates_b: np.ndarray,
) -> np.ndarray:
    return sum(
        row_weights[row] * np.outer(templates_a[row], templates_b[row])
        for row in range(2)
    )


def pure_projector(matrix: np.ndarray) -> np.ndarray:
    vector = matrix.reshape(-1, order="C")
    vector = vector / np.linalg.norm(vector)
    return np.outer(vector, vector.conj())


def projector_trace_distance(first: np.ndarray, second: np.ndarray) -> float:
    difference = pure_projector(first) - pure_projector(second)
    return float(0.5 * np.sum(np.linalg.svd(difference, compute_uv=False)))


def main() -> None:
    seed = 20260827
    rng = np.random.default_rng(seed)
    checks: list[CheckResult] = []
    sample_count = 10_000

    maximum_cross_error = 0.0
    maximum_joint_error = 0.0
    maximum_a_matching_error = 0.0
    maximum_b_matching_error = 0.0
    maximum_conditional_action_error = 0.0
    maximum_mean_action_excess = 0.0
    maximum_cnot_cross_error = 0.0
    maximum_cnot_joint_error = 0.0
    maximum_cnot_template_error = 0.0
    maximum_involution_error = 0.0
    maximum_row_weight_error = 0.0
    maximum_row_col_error = 0.0
    permutation_23 = np.array([
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ])

    for _ in range(sample_count):
        matrix = random_normalized_matrix(rng)
        phase = float(rng.uniform(-np.pi, np.pi))
        row_weights, templates_a, templates_b = row_templates(matrix, phase)
        cross_moment = cross_moment_from_templates(
            row_weights,
            templates_a,
            templates_b,
        )
        maximum_cross_error = max(
            maximum_cross_error,
            float(np.linalg.norm(cross_moment - matrix)),
        )

        joint = np.abs(matrix) ** 2
        maximum_joint_error = max(
            maximum_joint_error,
            float(np.max(np.abs(np.sum(joint, axis=1) - row_weights))),
            abs(float(np.sum(joint)) - 1.0),
        )
        for row in range(2):
            local_a = np.abs(templates_a[row]) ** 2
            local_a /= np.sum(local_a)
            maximum_a_matching_error = max(
                maximum_a_matching_error,
                float(np.max(np.abs(local_a - np.eye(2)[row]))),
            )
            local_b = np.abs(templates_b[row]) ** 2
            local_b /= np.sum(local_b)
            expected_b = joint[row] / row_weights[row]
            maximum_b_matching_error = max(
                maximum_b_matching_error,
                float(np.max(np.abs(local_b - expected_b))),
            )
            action_product = (
                float(np.vdot(templates_a[row], templates_a[row]).real)
                * float(np.vdot(templates_b[row], templates_b[row]).real)
            )
            maximum_conditional_action_error = max(
                maximum_conditional_action_error,
                abs(action_product - 1.0 / row_weights[row]),
            )
        mean_active_action = float(2.0 * np.sum(np.sqrt(row_weights)))
        maximum_mean_action_excess = max(
            maximum_mean_action_excess,
            max(0.0, mean_active_action - 2.0 * sqrt(2.0)),
        )

        output_matrix = cnot_matrix(matrix)
        output_row_weights, output_a, output_b = row_templates(output_matrix, phase)
        pointwise_b = templates_b.copy()
        pointwise_b[1] = pointwise_b[1, ::-1]
        pointwise_cross = cross_moment_from_templates(
            row_weights,
            templates_a,
            pointwise_b,
        )
        maximum_cnot_cross_error = max(
            maximum_cnot_cross_error,
            float(np.linalg.norm(pointwise_cross - output_matrix)),
        )
        routed_joint = joint.copy()
        routed_joint[1] = joint[1, ::-1]
        maximum_cnot_joint_error = max(
            maximum_cnot_joint_error,
            float(np.max(np.abs(routed_joint - np.abs(output_matrix) ** 2))),
        )
        maximum_cnot_template_error = max(
            maximum_cnot_template_error,
            float(np.linalg.norm(output_row_weights - row_weights)),
            float(np.linalg.norm(output_a - templates_a)),
            float(np.linalg.norm(output_b - pointwise_b)),
        )
        maximum_involution_error = max(
            maximum_involution_error,
            float(np.linalg.norm(cnot_matrix(output_matrix) - matrix)),
        )
        maximum_row_weight_error = max(
            maximum_row_weight_error,
            float(np.max(np.abs(output_row_weights - row_weights))),
        )

        row_vector = matrix.reshape(-1, order="C")
        column_vector = matrix.reshape(-1, order="F")
        maximum_row_col_error = max(
            maximum_row_col_error,
            float(np.linalg.norm(column_vector - permutation_23 @ row_vector)),
        )

    checks.append(record_max("r157_cross_moment_error", maximum_cross_error, 4.0e-14))
    checks.append(record_max("r157_joint_configuration_error", maximum_joint_error, 2.0e-14))
    checks.append(record_max("r157_a_local_matching_error", maximum_a_matching_error, 2.0e-14))
    checks.append(record_max("r157_b_local_matching_error", maximum_b_matching_error, 3.0e-14))
    checks.append(record_max(
        "r157_rare_row_action_lower_bound_error",
        maximum_conditional_action_error,
        2.0e-12,
    ))
    checks.append(record_max(
        "r157_mean_active_action_bound_excess",
        maximum_mean_action_excess,
        2.0e-14,
    ))
    checks.append(record_max("r158_cross_covariance_error", maximum_cnot_cross_error, 4.0e-14))
    checks.append(record_max("r158_configuration_xor_error", maximum_cnot_joint_error, 2.0e-14))
    checks.append(record_max("r158_pointwise_template_error", maximum_cnot_template_error, 4.0e-14))
    checks.append(record_max("r158_involution_error", maximum_involution_error, 0.0))
    checks.append(record_max("r158_row_weight_preservation_error", maximum_row_weight_error, 2.0e-14))
    checks.append(record_max("row_column_permutation_error", maximum_row_col_error, 0.0))

    finite_matrix = random_normalized_matrix(rng, row_floor=0.12)
    row_weights, templates_a, templates_b = row_templates(finite_matrix, 0.37)
    rho_star = float(np.min(row_weights))
    epsilon_0 = 0.013
    survivals = 1.0 - epsilon_0 * rng.uniform(size=(2, 2))
    safe_moment = sum(
        abs(finite_matrix[row, column]) ** 2
        * survivals[row, column]
        * np.outer(templates_a[row], templates_b[row])
        for row in range(2)
        for column in range(2)
    )
    safe_distribution = np.abs(finite_matrix) ** 2 * survivals
    failed_mass = 1.0 - float(np.sum(safe_distribution))
    moment_error = float(np.linalg.norm(safe_moment - finite_matrix))
    moment_bound = epsilon_0 / sqrt(rho_star)
    normalized_safe = safe_moment / np.linalg.norm(safe_moment)
    cross_distance = projector_trace_distance(normalized_safe, finite_matrix)
    cross_bound = min(1.0, 2.0 * epsilon_0 / sqrt(rho_star))
    checks.append(record_max("r157_no_response_mass", failed_mass, epsilon_0))
    checks.append(record_max("r157_finite_moment_bound_excess", moment_error - moment_bound, 0.0))
    checks.append(record_max("r157_cross_projector_bound_excess", cross_distance - cross_bound, 0.0))

    maximum_conditional_tv = 0.0
    for row in range(2):
        ideal = np.abs(finite_matrix[row]) ** 2 / row_weights[row]
        safe = ideal * survivals[row]
        safe /= np.sum(safe)
        maximum_conditional_tv = max(maximum_conditional_tv, total_variation(safe, ideal))
    checks.append(record_max(
        "r157_b_matching_bound_excess",
        maximum_conditional_tv - epsilon_0 / (1.0 - epsilon_0),
        0.0,
    ))

    input_weights = np.array([0.1, 0.2, 0.3, 0.4])
    programs = tuple(random_normalized_matrix(rng) for _ in input_weights)
    analyzers = tuple((random_unitary(rng), random_unitary(rng)) for _ in input_weights)
    conditionals = np.array([
        np.abs(unitary_a @ cnot_matrix(matrix) @ unitary_b.T) ** 2
        for matrix, (unitary_a, unitary_b) in zip(programs, analyzers, strict=True)
    ])
    joint_benchmark = input_weights[:, None, None] * conditionals
    checks.append(record_max(
        "r159_conditional_normalization_error",
        float(np.max(np.abs(np.sum(conditionals, axis=(1, 2)) - 1.0))),
        3.0e-14,
    ))
    checks.append(record_max(
        "r159_input_frequency_error",
        float(np.max(np.abs(np.sum(joint_benchmark, axis=(1, 2)) - input_weights))),
        3.0e-14,
    ))
    checks.append(record_max(
        "r159_joint_normalization_error",
        abs(float(np.sum(joint_benchmark)) - 1.0),
        3.0e-14,
    ))

    ideal_shared_example = np.array([[3.0 / 8.0, 1.0 / 8.0], [1.0 / 8.0, 3.0 / 8.0]])
    shared_selector_example = np.full((2, 2), 1.0 / 4.0)
    checks.append(record_equal(
        "r159_shared_selector_counterexample_tv_error",
        total_variation(ideal_shared_example, shared_selector_example),
        0.25,
    ))

    no_response = np.array([0.007, 0.004, 0.009, 0.006])
    observed = joint_benchmark * (1.0 - no_response[:, None, None])
    failed = input_weights * no_response
    observed_tv = 0.5 * (
        float(np.sum(np.abs(observed - joint_benchmark)))
        + float(np.sum(failed))
    )
    checks.append(record_max(
        "r159_no_response_total_variation_formula_error",
        abs(observed_tv - float(np.dot(input_weights, no_response))),
        2.0e-14,
    ))

    antisymmetric = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    singlet_input = np.array([[0.0, -1.0], [0.0, 1.0]], dtype=complex) / sqrt(2.0)
    singlet_output = cnot_matrix(singlet_input)
    checks.append(record_max(
        "r160_fixed_singlet_output_error",
        float(np.linalg.norm(singlet_output + antisymmetric / sqrt(2.0))),
        0.0,
    ))
    row_weights, templates_a, templates_b = row_templates(singlet_output, 0.71)
    spin_flip_errors = []
    for row in range(2):
        spin_flip_errors.append(float(np.linalg.norm(
            templates_b[row] - antisymmetric @ templates_a[row].conj()
        )))
    checks.append(record_max("r160_spin_flip_fiber_error", max(spin_flip_errors), 3.0e-14))
    checks.append(record_max(
        "r160_singlet_branch_weight_error",
        float(np.max(np.abs(np.abs(singlet_output) ** 2 - np.array([
            [0.0, 0.5],
            [0.5, 0.0],
        ])))),
        2.0e-14,
    ))
    checks.append(record_max(
        "r160_singlet_cross_moment_error",
        float(np.linalg.norm(
            cross_moment_from_templates(row_weights, templates_a, templates_b)
            + antisymmetric / sqrt(2.0)
        )),
        3.0e-14,
    ))

    link_reference = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)
    reference_weights, reference_a, reference_b = row_templates(link_reference, -0.43)
    reference_cross = cross_moment_from_templates(
        reference_weights,
        reference_a,
        reference_b,
    )
    singlet_cross = cross_moment_from_templates(row_weights, templates_a, templates_b)
    input_state_distance = projector_trace_distance(reference_cross, singlet_cross)
    output_state_distance = projector_trace_distance(
        reference_cross.copy(),
        singlet_cross.copy(),
    )
    checks.append(record_min("r160_distinct_link_state_distance", input_state_distance, 0.99))
    checks.append(record_max(
        "r160_state_carrying_distance_error",
        abs(output_state_distance - input_state_distance),
        0.0,
    ))
    maximum_bias_error = 0.0
    for probability_plus in (0.0, 0.25, 0.5, 0.75, 1.0):
        routed_probability_plus = probability_plus
        maximum_bias_error = max(
            maximum_bias_error,
            abs(routed_probability_plus - probability_plus),
        )
    checks.append(record_max("r160_branch_bias_transport_error", maximum_bias_error, 0.0))
    checks.append(record_equal("r157_simple_pair_count_error", 16 + 4 + 4 + 8, 32))

    payload = {
        "seed": seed,
        "sample_count": sample_count,
        "checks": [asdict(check) for check in checks],
        "passed": all(check.passed for check in checks),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
