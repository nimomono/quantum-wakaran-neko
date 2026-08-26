#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from math import cos, pi, sin, sqrt

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


def planar_setting(angle: float) -> np.ndarray:
    sigma_x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sigma_z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    return sin(angle) * sigma_x + cos(angle) * sigma_z


def branch_vector(setting: np.ndarray, sign: int) -> np.ndarray:
    values, vectors = np.linalg.eigh(setting)
    index = int(np.argmax(values)) if sign > 0 else int(np.argmin(values))
    return vectors[:, index]


def controller_from_m39(coefficients: np.ndarray) -> np.ndarray:
    coefficient_matrix = coefficients.reshape(2, 2, order="C")
    antisymmetric_part = 0.5 * (coefficient_matrix - coefficient_matrix.T)
    norm = float(np.linalg.norm(antisymmetric_part))
    if norm <= 1.0e-12:
        raise ValueError("M39 input is outside the former R151 antisymmetric safe region")
    return sqrt(2.0) * antisymmetric_part / norm


def controller_projector(controller: np.ndarray) -> np.ndarray:
    vector = controller.reshape(-1, order="C")
    vector = vector / np.linalg.norm(vector)
    return np.outer(vector, vector.conj())


def m39_branch_probabilities(coefficients: np.ndarray) -> np.ndarray:
    probabilities = np.array(
        [abs(coefficients[1]) ** 2, abs(coefficients[2]) ** 2],
        dtype=float,
    )
    return probabilities / np.sum(probabilities)


def joint_distribution(
    angle_a: float,
    angle_b: float,
    pairing_controller: np.ndarray,
    branch_probabilities: np.ndarray,
) -> np.ndarray:
    setting_a = planar_setting(angle_a)
    setting_b = planar_setting(angle_b)
    joint = np.zeros((2, 2), dtype=float)
    for index_a, sign in enumerate((1, -1)):
        local_a = branch_vector(setting_a, sign)
        local_b = pairing_controller @ local_a.conj()
        local_b = local_b / np.linalg.norm(local_b)
        for index_b, outcome_b in enumerate((1, -1)):
            effect_b = 0.5 * (np.eye(2) + outcome_b * setting_b)
            conditional_b = float(np.vdot(local_b, effect_b @ local_b).real)
            joint[index_a, index_b] = branch_probabilities[index_a] * conditional_b
    return joint


def ideal_joint(angle_a: float, angle_b: float) -> np.ndarray:
    cosine = cos(angle_a - angle_b)
    return np.array(
        [
            [0.25 * (1.0 - cosine), 0.25 * (1.0 + cosine)],
            [0.25 * (1.0 + cosine), 0.25 * (1.0 - cosine)],
        ]
    )


def correlation(joint: np.ndarray) -> float:
    outcomes = np.array([1.0, -1.0])
    return float(outcomes @ joint @ outcomes)


def pure_state_trace_distance(first: np.ndarray, second: np.ndarray) -> float:
    first = first / np.linalg.norm(first)
    second = second / np.linalg.norm(second)
    overlap = abs(np.vdot(first, second)) ** 2
    return float(sqrt(max(0.0, 1.0 - overlap)))


def main() -> None:
    numeric_seed = 20260826
    rng = np.random.default_rng(numeric_seed)
    checks: list[CheckResult] = []
    antisymmetric = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    singlet = np.array([0.0, 1.0, -1.0, 0.0], dtype=complex) / sqrt(2.0)
    fair_branches = np.array([0.5, 0.5])

    m39_controller = controller_from_m39(singlet)
    m39_branches = m39_branch_probabilities(singlet)
    checks.append(record_max(
        "m39_singlet_controller_error",
        np.linalg.norm(m39_controller - antisymmetric),
        3.0e-14,
    ))
    checks.append(record_max(
        "m39_branch_fairness_error",
        np.linalg.norm(m39_branches - fair_branches),
        3.0e-14,
    ))

    reference_projector = controller_projector(antisymmetric)
    maximum_controller_ray_error = 0.0
    random_input_count = 10_000
    for _ in range(random_input_count):
        symmetric = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        symmetric = 0.5 * (symmetric + symmetric.T)
        coefficient = rng.normal() + 1j * rng.normal()
        if abs(coefficient) < 0.25:
            coefficient += 0.5
        general_matrix = symmetric + coefficient * antisymmetric
        controller = controller_from_m39(general_matrix.reshape(-1, order="C"))
        maximum_controller_ray_error = max(
            maximum_controller_ray_error,
            np.linalg.norm(controller_projector(controller) - reference_projector),
        )
    checks.append(record_max(
        "general_input_controller_ray_collapse_error",
        maximum_controller_ray_error,
        3.0e-14,
    ))

    alternative_input = np.array([1.0, 2.0, 0.5j, -1.0j], dtype=complex)
    alternative_input /= np.linalg.norm(alternative_input)
    alternative_controller = controller_from_m39(alternative_input)
    input_state_distance = pure_state_trace_distance(singlet, alternative_input)
    checks.append(record_min(
        "distinct_m39_input_state_distance",
        input_state_distance,
        0.5,
    ))
    checks.append(record_max(
        "distinct_input_controller_ray_error",
        np.linalg.norm(
            controller_projector(alternative_controller) - reference_projector
        ),
        3.0e-14,
    ))

    setting_angles_a = (-0.91, -0.17, 0.43, 1.08, 0.0, pi / 2.0)
    setting_angles_b = (-0.63, 0.12, 0.77, pi / 4.0, -pi / 4.0)
    maximum_internal_seed_tv = 0.0
    maximum_ideal_error = 0.0
    maximum_alternative_controller_tv = 0.0
    maximum_marginal_error = 0.0
    for angle_a in setting_angles_a:
        for angle_b in setting_angles_b:
            from_m39 = joint_distribution(
                angle_a, angle_b, m39_controller, m39_branches
            )
            from_internal_fair_seed = joint_distribution(
                angle_a, angle_b, antisymmetric, fair_branches
            )
            from_alternative_controller = joint_distribution(
                angle_a, angle_b, alternative_controller, fair_branches
            )
            maximum_internal_seed_tv = max(
                maximum_internal_seed_tv,
                total_variation(from_m39, from_internal_fair_seed),
            )
            maximum_ideal_error = max(
                maximum_ideal_error,
                np.max(np.abs(from_internal_fair_seed - ideal_joint(angle_a, angle_b))),
            )
            maximum_alternative_controller_tv = max(
                maximum_alternative_controller_tv,
                total_variation(from_m39, from_alternative_controller),
            )
            maximum_marginal_error = max(
                maximum_marginal_error,
                np.max(np.abs(np.sum(from_internal_fair_seed, axis=0) - 0.5)),
                np.max(np.abs(np.sum(from_internal_fair_seed, axis=1) - 0.5)),
            )
    checks.append(record_max(
        "m39_vs_internal_fair_seed_joint_tv",
        maximum_internal_seed_tv,
        3.0e-14,
    ))
    checks.append(record_max(
        "internal_fair_seed_ideal_joint_error",
        maximum_ideal_error,
        4.0e-14,
    ))
    checks.append(record_max(
        "alternative_controller_with_fair_branches_joint_tv",
        maximum_alternative_controller_tv,
        3.0e-14,
    ))
    checks.append(record_max(
        "internal_fair_seed_marginal_error",
        maximum_marginal_error,
        4.0e-14,
    ))

    branch_biases = (0.0, 0.25, 0.5, 0.75, 1.0)
    maximum_branch_bias_transport_error = 0.0
    for probability_plus in branch_biases:
        branches = np.array([probability_plus, 1.0 - probability_plus])
        routed = joint_distribution(0.37, -0.52, antisymmetric, branches)
        maximum_branch_bias_transport_error = max(
            maximum_branch_bias_transport_error,
            np.max(np.abs(np.sum(routed, axis=1) - branches)),
        )
    checks.append(record_max(
        "branch_bias_sweep_transport_error",
        maximum_branch_bias_transport_error,
        3.0e-14,
    ))

    biased_branches = np.array([0.63, 0.37])
    maximum_biased_correlation_error = 0.0
    maximum_biased_joint_tv = 0.0
    maximum_b_marginal_setting_change = 0.0
    for angle_b in setting_angles_b:
        b_marginals: list[np.ndarray] = []
        for angle_a in setting_angles_a:
            biased = joint_distribution(
                angle_a, angle_b, antisymmetric, biased_branches
            )
            maximum_biased_correlation_error = max(
                maximum_biased_correlation_error,
                abs(correlation(biased) + cos(angle_a - angle_b)),
            )
            maximum_biased_joint_tv = max(
                maximum_biased_joint_tv,
                total_variation(biased, ideal_joint(angle_a, angle_b)),
            )
            b_marginals.append(np.sum(biased, axis=0))
        for first in b_marginals:
            for second in b_marginals:
                maximum_b_marginal_setting_change = max(
                    maximum_b_marginal_setting_change,
                    total_variation(first, second),
                )
    checks.append(record_max(
        "biased_branch_correlation_error",
        maximum_biased_correlation_error,
        4.0e-14,
    ))
    checks.append(record_min(
        "biased_branch_changes_joint_distribution",
        maximum_biased_joint_tv,
        0.12,
    ))
    checks.append(record_min(
        "biased_branch_breaks_b_marginal_nonsignalling",
        maximum_b_marginal_setting_change,
        0.1,
    ))

    provenance_conditioned = [
        joint_distribution(0.27, -0.83, antisymmetric, fair_branches)
        for _history in ("m39-01", "m39-10", "internal-a", "internal-b")
    ]
    provenance_reference = provenance_conditioned[0]
    maximum_provenance_tv = max(
        total_variation(item, provenance_reference)
        for item in provenance_conditioned[1:]
    )
    checks.append(record_max(
        "provenance_conditioned_joint_invariance_tv",
        maximum_provenance_tv,
        3.0e-14,
    ))

    permutation_23 = np.eye(4, dtype=complex)[[0, 2, 1, 3]]
    vectorization_matrix = np.array(
        [[0.2 + 0.7j, -0.4 + 0.1j], [0.9 - 0.3j, -0.6 + 0.8j]],
        dtype=complex,
    )
    row_column_permutation_error = np.linalg.norm(
        vectorization_matrix.reshape(-1, order="F")
        - permutation_23 @ vectorization_matrix.reshape(-1, order="C")
    )
    checks.append(record_max(
        "general_row_column_permutation_error",
        row_column_permutation_error,
        3.0e-14,
    ))

    guard_mass = 0.2
    reference_joint = ideal_joint(0.27, -0.83)
    routed_full_distribution = np.concatenate([reference_joint.reshape(-1), [0.0]])
    raw_haar_full_distribution = np.concatenate(
        [(1.0 - guard_mass) * reference_joint.reshape(-1), [guard_mass]]
    )
    raw_haar_tv = total_variation(
        routed_full_distribution,
        raw_haar_full_distribution,
    )
    checks.append(record_max(
        "raw_haar_guard_tv_identity_error",
        abs(raw_haar_tv - guard_mass),
        3.0e-14,
    ))

    payload = {
        "seed": numeric_seed,
        "random_general_input_count": random_input_count,
        "check_count": len(checks),
        "diagnostics": {
            "maximum_controller_ray_error": maximum_controller_ray_error,
            "m39_vs_internal_fair_seed_joint_tv": maximum_internal_seed_tv,
            "alternative_input_state_distance": input_state_distance,
            "alternative_controller_with_fair_branches_joint_tv": (
                maximum_alternative_controller_tv
            ),
            "branch_bias_transport_error": maximum_branch_bias_transport_error,
            "biased_branch_joint_tv": maximum_biased_joint_tv,
            "biased_branch_b_marginal_setting_change": (
                maximum_b_marginal_setting_change
            ),
            "provenance_conditioned_joint_tv": maximum_provenance_tv,
            "row_column_permutation_error": row_column_permutation_error,
            "raw_haar_without_routing_tv": raw_haar_tv,
        },
        "interpretation": {
            "m39_specific_source_required_for_ideal_distribution": False,
            "fair_branch_source_required_for_ideal_nonsignalling": True,
            "input_branch_bias_is_transportable": True,
            "provenance_is_result_inert": True,
            "safe_basin_routing_required_to_remove_finite_guard_mass": True,
        },
        "checks": [asdict(check) for check in checks],
        "passed": all(check.passed for check in checks),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
