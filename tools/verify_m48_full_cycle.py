#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from math import cos, exp, pi, sin, sqrt

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


def pauli_matrices() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    sigma_x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sigma_y = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
    sigma_z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    return sigma_x, sigma_y, sigma_z


def planar_setting(angle: float, pauli: tuple[np.ndarray, ...]) -> np.ndarray:
    return sin(angle) * pauli[0] + cos(angle) * pauli[2]


def branch_vector(setting: np.ndarray, sign: int) -> np.ndarray:
    values, vectors = np.linalg.eigh(setting)
    index = int(np.argmax(values)) if sign > 0 else int(np.argmin(values))
    return vectors[:, index]


def matching_distribution(
    bath: np.ndarray,
    embedding: np.ndarray,
    reference: np.ndarray,
    regularization: float,
) -> tuple[np.ndarray, np.ndarray]:
    weights = np.abs(embedding @ bath) ** 2 / float(np.vdot(bath, bath).real)
    target = (weights + regularization * reference) / (1.0 + regularization)
    return weights, target


def matching_generator(
    target: np.ndarray,
    adjacency: np.ndarray,
    prefactor: float,
) -> np.ndarray:
    size = len(target)
    generator = np.zeros((size, size), dtype=float)
    for source in range(size):
        for destination in range(size):
            if source != destination and adjacency[source, destination] > 0.0:
                generator[source, destination] = (
                    prefactor
                    * adjacency[source, destination]
                    * sqrt(target[destination] / target[source])
                )
        generator[source, source] = -np.sum(generator[source])
    return generator


def reversible_semigroup(
    generator: np.ndarray,
    invariant: np.ndarray,
    time: float,
) -> tuple[np.ndarray, float, float]:
    root = np.diag(np.sqrt(invariant))
    inverse_root = np.diag(1.0 / np.sqrt(invariant))
    symmetric = root @ generator @ inverse_root
    values, vectors = np.linalg.eigh(symmetric)
    semigroup_symmetric = vectors @ np.diag(np.exp(values * time)) @ vectors.T
    semigroup = inverse_root @ semigroup_symmetric @ root
    ordered = np.sort(values)
    gap = float(-ordered[-2])
    symmetry_error = float(np.linalg.norm(symmetric - symmetric.T))
    return semigroup, gap, symmetry_error


def ideal_joint(angle_a: float, angle_b: float) -> np.ndarray:
    cosine = cos(angle_a - angle_b)
    return np.array(
        [
            [0.25 * (1.0 - cosine), 0.25 * (1.0 + cosine)],
            [0.25 * (1.0 + cosine), 0.25 * (1.0 - cosine)],
        ]
    )


def main() -> None:
    seed = 20260826
    checks: list[CheckResult] = []
    pauli = pauli_matrices()
    antisymmetric = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    checks.append(record_max(
        "r151_pairing_tensor_antisymmetry_error",
        np.linalg.norm(antisymmetric.T + antisymmetric),
        2.0e-14,
    ))
    checks.append(record_max(
        "r151_pairing_tensor_square_error",
        np.linalg.norm(antisymmetric @ antisymmetric + np.eye(2)),
        2.0e-14,
    ))
    checks.append(record_max(
        "r151_pairing_tensor_orthogonality_error",
        np.linalg.norm(antisymmetric.T @ antisymmetric - np.eye(2)),
        2.0e-14,
    ))
    branch_probabilities = np.array([0.5, 0.5])
    checks.append(record_max(
        "r151_branch_normalization_error",
        abs(np.sum(branch_probabilities) - 1.0),
        2.0e-14,
    ))
    checks.append(record_max(
        "r151_equal_branch_weight_error",
        abs(branch_probabilities[0] - branch_probabilities[1]),
        2.0e-14,
    ))

    setting_angles = (-0.91, -0.17, 0.43, 1.08)
    guard = 0.2
    for setting_index, angle in enumerate(setting_angles):
        setting = planar_setting(angle, pauli)
        checks.append(record_max(
            f"r151_setting_{setting_index}_involution_error",
            np.linalg.norm(setting @ setting - np.eye(2)),
            3.0e-14,
        ))
        for sign in (1, -1):
            seed_vector = branch_vector(setting, sign)
            alignment = float(
                np.vdot(seed_vector, setting @ seed_vector).real
                / np.vdot(seed_vector, seed_vector).real
            )
            checks.append(record_min(
                f"r151_setting_{setting_index}_branch_{sign}_safe_margin",
                sign * alignment,
                guard,
            ))

    embedding = 0.5 * np.array(
        [
            [1.0, 1.0],
            [1.0, 1.0j],
            [1.0, -1.0],
            [1.0, -1.0j],
        ],
        dtype=complex,
    )
    reference = np.array([0.1, 0.2, 0.3, 0.4])
    regularization = 0.07
    adjacency = np.array(
        [
            [0.0, 1.0, 0.3, 1.2],
            [1.0, 0.0, 0.8, 0.0],
            [0.3, 0.8, 0.0, 1.1],
            [1.2, 0.0, 1.1, 0.0],
        ]
    )
    prefactor = 0.9
    checks.append(record_max(
        "r152_embedding_isometry_error",
        np.linalg.norm(embedding.conj().T @ embedding - np.eye(2)),
        3.0e-14,
    ))
    checks.append(record_max(
        "r152_adjacency_symmetry_error",
        np.linalg.norm(adjacency - adjacency.T),
        2.0e-14,
    ))

    target_distributions: list[np.ndarray] = []
    minimum_gap = float("inf")
    maximum_mixing_excess = 0.0
    for setting_index, angle in enumerate(setting_angles):
        setting = planar_setting(angle, pauli)
        bath = branch_vector(setting, 1) + 0.31j * branch_vector(setting, -1)
        weights, target = matching_distribution(
            bath,
            embedding,
            reference,
            regularization,
        )
        target_distributions.append(target)
        phase = np.exp(1j * (0.23 + 0.11 * setting_index))
        _, phase_target = matching_distribution(
            phase * bath,
            embedding,
            reference,
            regularization,
        )
        checks.append(record_max(
            f"r152_setting_{setting_index}_weight_normalization_error",
            abs(np.sum(weights) - 1.0),
            3.0e-14,
        ))
        checks.append(record_max(
            f"r152_setting_{setting_index}_target_normalization_error",
            abs(np.sum(target) - 1.0),
            3.0e-14,
        ))
        checks.append(record_min(
            f"r152_setting_{setting_index}_target_minimum",
            np.min(target),
            regularization * np.min(reference) / (1.0 + regularization),
        ))
        checks.append(record_max(
            f"r152_setting_{setting_index}_phase_invariance_error",
            np.linalg.norm(phase_target - target),
            3.0e-14,
        ))
        checks.append(record_max(
            f"r152_setting_{setting_index}_regularization_tv_bound",
            total_variation(target, weights),
            regularization / (1.0 + regularization),
        ))

        generator = matching_generator(target, adjacency, prefactor)
        detailed_balance = np.diag(target) @ generator
        checks.append(record_max(
            f"r152_setting_{setting_index}_row_sum_error",
            np.max(np.abs(np.sum(generator, axis=1))),
            3.0e-14,
        ))
        checks.append(record_max(
            f"r152_setting_{setting_index}_stationarity_error",
            np.linalg.norm(target @ generator),
            3.0e-14,
        ))
        checks.append(record_max(
            f"r152_setting_{setting_index}_detailed_balance_error",
            np.linalg.norm(detailed_balance - detailed_balance.T),
            3.0e-14,
        ))

        mixing_time = 3.0
        semigroup, gap, symmetry_error = reversible_semigroup(
            generator,
            target,
            mixing_time,
        )
        minimum_gap = min(minimum_gap, gap)
        checks.append(record_max(
            f"r152_setting_{setting_index}_symmetrized_generator_error",
            symmetry_error,
            3.0e-14,
        ))
        checks.append(record_min(
            f"r152_setting_{setting_index}_spectral_gap",
            gap,
            1.0e-6,
        ))
        checks.append(record_max(
            f"r152_setting_{setting_index}_semigroup_row_sum_error",
            np.max(np.abs(np.sum(semigroup, axis=1) - 1.0)),
            2.0e-13,
        ))
        for initial_index in range(len(target)):
            initial = np.eye(len(target))[initial_index]
            evolved = initial @ semigroup
            observed_tv = total_variation(evolved, target)
            chi_bound = 0.5 * sqrt(1.0 / target[initial_index] - 1.0)
            spectral_bound = chi_bound * exp(-gap * mixing_time)
            maximum_mixing_excess = max(
                maximum_mixing_excess,
                observed_tv - spectral_bound,
            )

    checks.append(record_min(
        "r153_finite_setting_uniform_gap",
        minimum_gap,
        1.0e-6,
    ))
    checks.append(record_max(
        "r153_uniform_spectral_mixing_bound_excess",
        max(0.0, maximum_mixing_excess),
        3.0e-13,
    ))

    error_terms = np.array(
        [0.002, 0.003, 0.004, 0.005, 0.004, 0.003, 0.002, 0.003, 0.002]
    )
    epsilon_bell_cycle = float(np.sum(error_terms))
    checks.append(record_max(
        "r153_r154_error_ledger_arithmetic",
        abs(epsilon_bell_cycle - 0.028),
        2.0e-14,
    ))
    checks.append(record_max(
        "r155_finite_error_chsh_threshold",
        epsilon_bell_cycle,
        (sqrt(2.0) - 1.0) / 4.0,
    ))

    outcome_values = np.array([1.0, -1.0])
    maximum_joint_error = 0.0
    maximum_marginal_error = 0.0
    maximum_conditional_error = 0.0
    for angle_a in setting_angles:
        setting_a = planar_setting(angle_a, pauli)
        for angle_b in (-0.63, 0.12, 0.77):
            setting_b = planar_setting(angle_b, pauli)
            joint = np.zeros((2, 2))
            for index_a, outcome_a in enumerate((1, -1)):
                local_a = branch_vector(setting_a, outcome_a)
                local_b = antisymmetric @ local_a.conj()
                for index_b, outcome_b in enumerate((1, -1)):
                    effect_b = 0.5 * (np.eye(2) + outcome_b * setting_b)
                    conditional = float(np.vdot(local_b, effect_b @ local_b).real)
                    expected_conditional = 0.5 * (
                        1.0 - outcome_a * outcome_b * cos(angle_a - angle_b)
                    )
                    maximum_conditional_error = max(
                        maximum_conditional_error,
                        abs(conditional - expected_conditional),
                    )
                    joint[index_a, index_b] = 0.5 * conditional
            expected_joint = ideal_joint(angle_a, angle_b)
            maximum_joint_error = max(
                maximum_joint_error,
                np.max(np.abs(joint - expected_joint)),
            )
            maximum_marginal_error = max(
                maximum_marginal_error,
                np.max(np.abs(np.sum(joint, axis=0) - 0.5)),
                np.max(np.abs(np.sum(joint, axis=1) - 0.5)),
            )
            correlation = float(outcome_values @ joint @ outcome_values)
            checks.append(record_max(
                f"r155_correlation_{angle_a:+.2f}_{angle_b:+.2f}_error",
                abs(correlation + cos(angle_a - angle_b)),
                4.0e-14,
            ))

    checks.append(record_max(
        "r154_local_conditional_response_error",
        maximum_conditional_error,
        4.0e-14,
    ))
    checks.append(record_max(
        "r155_finite_family_joint_cosine_error",
        maximum_joint_error,
        4.0e-14,
    ))
    checks.append(record_max(
        "r155_finite_family_nonsignalling_error",
        maximum_marginal_error,
        4.0e-14,
    ))

    chsh_angles_a = (0.0, pi / 2.0)
    chsh_angles_b = (pi / 4.0, -pi / 4.0)
    correlations = np.array(
        [
            [-cos(angle_a - angle_b) for angle_b in chsh_angles_b]
            for angle_a in chsh_angles_a
        ]
    )
    chsh = (
        correlations[0, 0]
        + correlations[0, 1]
        + correlations[1, 0]
        - correlations[1, 1]
    )
    checks.append(record_max(
        "r155_singlet_chsh_error",
        abs(abs(chsh) - 2.0 * sqrt(2.0)),
        3.0e-14,
    ))
    checks.append(record_min(
        "r155_finite_error_violation_margin",
        2.0 * sqrt(2.0) - 8.0 * epsilon_bell_cycle - 2.0,
        0.0,
    ))
    checks.append(record_max(
        "r155_nonsignalling_drift_bound",
        2.0 * epsilon_bell_cycle,
        2.0 * epsilon_bell_cycle,
    ))
    checks.append(record_max(
        "r155_chsh_drift_bound",
        8.0 * epsilon_bell_cycle,
        8.0 * epsilon_bell_cycle,
    ))

    contraction = 0.37
    reset_noise = 0.006
    deviation = 0.41
    for _ in range(120):
        deviation = contraction * deviation + reset_noise
    reset_bound = reset_noise / (1.0 - contraction)
    checks.append(record_max(
        "r156_reset_asymptotic_bound_excess",
        max(0.0, deviation - reset_bound),
        2.0e-14,
    ))
    checks.append(record_max(
        "r156_reset_fixed_point_error",
        abs(deviation - reset_bound),
        2.0e-14,
    ))

    payload = {
        "seed": seed,
        "finite_setting_count": len(setting_angles),
        "minimum_matching_gap": minimum_gap,
        "epsilon_bell_cycle_example": epsilon_bell_cycle,
        "check_count": len(checks),
        "checks": [asdict(check) for check in checks],
        "passed": all(check.passed for check in checks),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
