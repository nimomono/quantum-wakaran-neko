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


def pauli_matrices() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    sigma_x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sigma_y = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
    sigma_z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    return sigma_x, sigma_y, sigma_z


def setting_operator(axis: np.ndarray, pauli: tuple[np.ndarray, ...]) -> np.ndarray:
    return sum(axis[index] * pauli[index] for index in range(3))


def bright_dark(
    state_a: np.ndarray,
    state_b: np.ndarray,
    antisymmetric: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    bright = 0.5 * (state_a - antisymmetric @ state_b.conj())
    dark = 0.5 * (state_a + antisymmetric @ state_b.conj())
    return bright, dark


def paired_state(
    bright: np.ndarray,
    dark: np.ndarray,
    antisymmetric: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    return bright + dark, antisymmetric @ (bright - dark).conj()


def hopf_field(
    bright: np.ndarray,
    setting: np.ndarray,
    gain: float,
    alignment: float,
) -> np.ndarray:
    norm_squared = float(np.vdot(bright, bright).real)
    h_value = float(np.vdot(bright, setting @ bright).real / norm_squared)
    return (
        gain * (1.0 - norm_squared) * bright
        + alignment * h_value * (setting - h_value * np.eye(2)) @ bright
    )


def rk4_step(field, state: np.ndarray, step: float) -> np.ndarray:
    k1 = field(state)
    k2 = field(state + 0.5 * step * k1)
    k3 = field(state + 0.5 * step * k2)
    k4 = field(state + step * k3)
    return state + step * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0


def eigenvector(setting: np.ndarray, sign: int) -> np.ndarray:
    values, vectors = np.linalg.eigh(setting)
    index = int(np.argmax(values)) if sign == 1 else int(np.argmin(values))
    return vectors[:, index]


def projector_trace_distance(first: np.ndarray, second: np.ndarray) -> float:
    overlap = abs(np.vdot(first, second)) ** 2
    return float(sqrt(max(0.0, 1.0 - overlap)))


def total_variation(first: np.ndarray, second: np.ndarray) -> float:
    return float(0.5 * np.sum(np.abs(first - second)))


def analyzer_probability(state: np.ndarray, setting: np.ndarray, outcome: int) -> float:
    effect = 0.5 * (np.eye(2) + outcome * setting)
    return float(np.vdot(state, effect @ state).real)


def main() -> None:
    seed = 20260826
    rng = np.random.default_rng(seed)
    checks: list[CheckResult] = []
    pauli = pauli_matrices()
    identity_2 = np.eye(2, dtype=complex)
    antisymmetric = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)

    checks.append(record_max(
        "antisymmetric_transpose_error",
        np.linalg.norm(antisymmetric.T + antisymmetric),
        2.0e-14,
    ))
    checks.append(record_max(
        "antisymmetric_square_error",
        np.linalg.norm(antisymmetric @ antisymmetric + identity_2),
        2.0e-14,
    ))

    state_a = rng.normal(size=2) + 1j * rng.normal(size=2)
    state_b = rng.normal(size=2) + 1j * rng.normal(size=2)
    bright, dark = bright_dark(state_a, state_b, antisymmetric)
    reconstructed_a, reconstructed_b = paired_state(bright, dark, antisymmetric)
    checks.append(record_max(
        "bright_dark_inverse_a_error",
        np.linalg.norm(reconstructed_a - state_a),
        3.0e-14,
    ))
    checks.append(record_max(
        "bright_dark_inverse_b_error",
        np.linalg.norm(reconstructed_b - state_b),
        3.0e-14,
    ))

    axes = (
        np.array([0.0, 0.0, 1.0]),
        np.array([1.0, 0.0, 0.0]),
        np.array([0.3, -0.4, sqrt(0.75)]),
        np.array([cos(0.37), sin(0.37), 0.0]),
    )
    covariance_representatives: list[np.ndarray] = []
    for axis_index, axis in enumerate(axes):
        axis = axis / np.linalg.norm(axis)
        setting = setting_operator(axis, pauli)
        checks.append(record_max(
            f"setting_{axis_index}_involution_error",
            np.linalg.norm(setting @ setting - identity_2),
            3.0e-14,
        ))
        checks.append(record_max(
            f"setting_{axis_index}_spin_flip_error",
            np.linalg.norm(
                antisymmetric @ setting.conj() + setting @ antisymmetric
            ),
            3.0e-14,
        ))

        branch_sum = np.zeros((2, 2), dtype=complex)
        for sign in (1, -1):
            selected = eigenvector(setting, sign)
            partner = antisymmetric @ selected.conj()
            checks.append(record_max(
                f"setting_{axis_index}_branch_{sign}_eigenvector_error",
                np.linalg.norm(setting @ selected - sign * selected),
                3.0e-14,
            ))
            checks.append(record_max(
                f"setting_{axis_index}_branch_{sign}_partner_antialignment_error",
                np.linalg.norm(setting @ partner + sign * partner),
                4.0e-14,
            ))
            branch_sum += np.outer(selected, partner)
        cross_covariance = 0.5 * branch_sum
        expected_cross_covariance = -0.5 * antisymmetric
        checks.append(record_max(
            f"setting_{axis_index}_singlet_cross_covariance_error",
            np.linalg.norm(cross_covariance - expected_cross_covariance),
            4.0e-14,
        ))
        normalized = cross_covariance / np.linalg.norm(cross_covariance)
        covariance_representatives.append(normalized)

    checks.append(record_max(
        "finite_setting_cross_covariance_independence_error",
        max(
            np.linalg.norm(item - covariance_representatives[0])
            for item in covariance_representatives[1:]
        ),
        4.0e-14,
    ))

    normalized_cross = -antisymmetric / sqrt(2.0)
    singlet = np.array([0.0, 1.0, -1.0, 0.0], dtype=complex) / sqrt(2.0)
    column_vectorization = normalized_cross.reshape(-1, order="F")
    row_vectorization = normalized_cross.reshape(-1, order="C")
    checks.append(record_max(
        "column_vectorized_singlet_error",
        np.linalg.norm(column_vectorization - singlet),
        2.0e-14,
    ))
    checks.append(record_max(
        "m39_row_vectorized_singlet_ray_error",
        np.linalg.norm(
            np.outer(row_vectorization, row_vectorization.conj())
            - np.outer(singlet, singlet.conj())
        ),
        3.0e-14,
    ))
    checks.append(record_min(
        "singlet_coefficient_matrix_rank",
        np.linalg.matrix_rank(singlet.reshape(2, 2)),
        2.0,
    ))
    product_first = rng.normal(size=2) + 1j * rng.normal(size=2)
    product_second = rng.normal(size=2) + 1j * rng.normal(size=2)
    product_matrix = np.outer(product_first, product_second)
    checks.append(record_max(
        "product_sample_coefficient_matrix_rank",
        np.linalg.matrix_rank(product_matrix),
        1.0,
    ))
    singlet_projector = np.outer(singlet, singlet.conj())
    orthogonal_projector = np.eye(4) - singlet_projector
    product_vector = product_matrix.reshape(-1)
    product_vector /= np.linalg.norm(product_vector)
    checks.append(record_min(
        "product_sample_distance_from_singlet_line",
        np.vdot(product_vector, orthogonal_projector @ product_vector).real,
        1.0e-6,
    ))

    axis = np.array([0.51, -0.33, sqrt(1.0 - 0.51**2 - 0.33**2)])
    setting = setting_operator(axis, pauli)
    gain = 0.8
    alignment = 1.1
    dark_damping = 0.9
    h_guard = 0.2
    radial_min = 0.45
    radial_max = 1.65
    dark_max = 0.35
    step = 0.002
    final_time = 8.0
    bright_initial = np.array([0.9 + 0.1j, 0.21 - 0.18j])
    bright_initial *= 1.13 / np.linalg.norm(bright_initial)
    initial_h = float(
        np.vdot(bright_initial, setting @ bright_initial).real
        / np.vdot(bright_initial, bright_initial).real
    )
    if abs(initial_h) < h_guard:
        bright_initial = eigenvector(setting, 1) + 0.31 * eigenvector(setting, -1)
        bright_initial *= 1.13 / np.linalg.norm(bright_initial)
        initial_h = float(
            np.vdot(bright_initial, setting @ bright_initial).real
            / np.vdot(bright_initial, bright_initial).real
        )
    dark_initial = np.array([0.12 - 0.07j, -0.08 + 0.03j])
    branch_sign = 1 if initial_h > 0.0 else -1
    target = eigenvector(setting, branch_sign)
    bright_state = bright_initial.copy()
    dark_state = dark_initial.copy()
    step_count = int(final_time / step)
    for _ in range(step_count):
        bright_state = rk4_step(
            lambda item: hopf_field(item, setting, gain, alignment),
            bright_state,
            step,
        )
        dark_state *= exp(-dark_damping * step)

    initial_norm_squared = float(np.vdot(bright_initial, bright_initial).real)
    exact_norm_squared = 1.0 / (
        1.0 + (1.0 / initial_norm_squared - 1.0) * exp(-2.0 * gain * final_time)
    )
    exact_h_squared = 1.0 / (
        1.0 + (1.0 / initial_h**2 - 1.0) * exp(-4.0 * alignment * final_time)
    )
    final_norm_squared = float(np.vdot(bright_state, bright_state).real)
    final_h = float(
        np.vdot(bright_state, setting @ bright_state).real / final_norm_squared
    )
    checks.append(record_max(
        "bright_radial_logistic_error",
        abs(final_norm_squared - exact_norm_squared),
        2.0e-10,
    ))
    checks.append(record_max(
        "bright_alignment_logistic_error",
        abs(final_h**2 - exact_h_squared),
        3.0e-10,
    ))
    checks.append(record_max(
        "dark_exact_damping_error",
        np.linalg.norm(dark_state - exp(-dark_damping * final_time) * dark_initial),
        3.0e-14,
    ))
    trace_distance = projector_trace_distance(
        bright_state / np.linalg.norm(bright_state),
        target,
    )
    trace_bound = exp(-2.0 * alignment * final_time) / (sqrt(2.0) * h_guard)
    checks.append(record_max(
        "bright_projector_finite_rate_bound_excess",
        max(0.0, trace_distance - trace_bound),
        2.0e-10,
    ))

    radial_constant = max(
        radial_min**-2 - 1.0,
        radial_max**2 - 1.0,
        0.0,
    )
    cross_constant = (
        radial_constant
        + 1.0 / h_guard
        + 2.0 * max(1.0, radial_max) * dark_max
        + dark_max**2
    )
    convergence_rate = min(2.0 * gain, 2.0 * alignment, dark_damping)
    paired_constant = sqrt(2.0) * (
        radial_constant
        + max(1.0, radial_max) / h_guard
        + dark_max
    )
    overlap_phase = np.vdot(target, bright_state)
    overlap_phase /= abs(overlap_phase)
    attractor_a = overlap_phase * target
    attractor_b = antisymmetric @ attractor_a.conj()
    final_a, final_b = paired_state(bright_state, dark_state, antisymmetric)
    paired_distance = sqrt(
        np.linalg.norm(final_a - attractor_a) ** 2
        + np.linalg.norm(final_b - attractor_b) ** 2
    )
    checks.append(record_max(
        "paired_attractor_finite_rate_bound_excess",
        max(
            0.0,
            paired_distance - paired_constant * exp(-convergence_rate * final_time),
        ),
        2.0e-10,
    ))
    cross_sample = np.outer(final_a, final_b)
    cross_target = -np.outer(target, target.conj()) @ antisymmetric
    checks.append(record_max(
        "paired_cross_covariance_finite_rate_bound_excess",
        max(
            0.0,
            np.linalg.norm(cross_sample - cross_target)
            - cross_constant * exp(-convergence_rate * final_time),
        ),
        2.0e-10,
    ))
    checks.append(record_min(
        "paired_cross_covariance_bound_constant",
        cross_constant,
        1.0,
    ))
    checks.append(record_min(
        "paired_finite_convergence_rate",
        convergence_rate,
        0.1,
    ))

    sample_count = 240_000
    gaussian = rng.normal(size=(sample_count, 4))
    haar_states = gaussian[:, :2] + 1j * gaussian[:, 2:]
    haar_states /= np.linalg.norm(haar_states, axis=1)[:, None]
    h_values = np.einsum(
        "ni,ij,nj->n",
        haar_states.conj(),
        setting,
        haar_states,
    ).real
    guard_mass = float(np.mean(np.abs(h_values) < h_guard))
    positive_mass = float(np.mean(h_values >= h_guard))
    negative_mass = float(np.mean(h_values <= -h_guard))
    checks.append(record_max(
        "haar_guard_mass_error",
        abs(guard_mass - h_guard),
        4.5e-3,
    ))
    checks.append(record_max(
        "haar_safe_branch_symmetry_error",
        abs(positive_mass - negative_mass),
        4.5e-3,
    ))

    x_angle = 0.27
    y_angle = -0.83
    axis_x = np.array([sin(x_angle), 0.0, cos(x_angle)])
    axis_y = np.array([sin(y_angle), 0.0, cos(y_angle)])
    setting_x = setting_operator(axis_x, pauli)
    setting_y = setting_operator(axis_y, pauli)
    joint = np.zeros((2, 2))
    signs = (1, -1)
    conditional_factorization_error = 0.0
    for index_a, outcome_a in enumerate(signs):
        local_a = eigenvector(setting_x, outcome_a)
        local_b = antisymmetric @ local_a.conj()
        probability_a = 0.5
        for index_b, outcome_b in enumerate(signs):
            probability_b = analyzer_probability(local_b, setting_y, outcome_b)
            expected_b = 0.5 * (
                1.0 - outcome_a * outcome_b * np.dot(axis_x, axis_y)
            )
            conditional_factorization_error = max(
                conditional_factorization_error,
                abs(probability_b - expected_b),
            )
            joint[index_a, index_b] = probability_a * probability_b
    ideal_joint = np.array([
        [0.25 * (1.0 - np.dot(axis_x, axis_y)), 0.25 * (1.0 + np.dot(axis_x, axis_y))],
        [0.25 * (1.0 + np.dot(axis_x, axis_y)), 0.25 * (1.0 - np.dot(axis_x, axis_y))],
    ])
    checks.append(record_max(
        "local_conditional_probability_error",
        conditional_factorization_error,
        4.0e-14,
    ))
    checks.append(record_max(
        "singlet_joint_cosine_error",
        np.max(np.abs(joint - ideal_joint)),
        4.0e-14,
    ))
    checks.append(record_max(
        "singlet_marginal_nonsignalling_error",
        max(
            np.max(np.abs(np.sum(joint, axis=0) - 0.5)),
            np.max(np.abs(np.sum(joint, axis=1) - 0.5)),
        ),
        4.0e-14,
    ))

    chsh_angles_a = (0.0, pi / 2.0)
    chsh_angles_b = (pi / 4.0, -pi / 4.0)
    correlations = np.array([
        [-cos(angle_a - angle_b) for angle_b in chsh_angles_b]
        for angle_a in chsh_angles_a
    ])
    chsh = correlations[0, 0] + correlations[0, 1] + correlations[1, 0] - correlations[1, 1]
    checks.append(record_max(
        "singlet_chsh_value_error",
        abs(abs(chsh) - 2.0 * sqrt(2.0)),
        3.0e-14,
    ))

    no_response = h_guard
    augmented_ideal = np.concatenate([ideal_joint.reshape(-1), [0.0]])
    augmented_observed = np.concatenate([
        (1.0 - no_response) * ideal_joint.reshape(-1),
        np.array([no_response]),
    ])
    checks.append(record_max(
        "guard_no_response_total_variation_error",
        abs(total_variation(augmented_ideal, augmented_observed) - no_response),
        3.0e-14,
    ))

    epsilon = 0.01
    nonsignalling_difference = 2.0 * epsilon
    chsh_drift = 8.0 * epsilon
    checks.append(record_max(
        "finite_error_nonsignalling_bound",
        nonsignalling_difference,
        2.0 * epsilon,
    ))
    checks.append(record_max(
        "finite_error_chsh_drift_bound",
        chsh_drift,
        8.0 * epsilon,
    ))
    checks.append(record_min(
        "finite_error_chsh_violation_margin",
        2.0 * sqrt(2.0) - 2.0 - chsh_drift,
        0.0,
    ))

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
