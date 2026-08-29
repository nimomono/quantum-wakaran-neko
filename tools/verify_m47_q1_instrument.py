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


def pauli_matrices() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    sigma_x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sigma_y = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
    sigma_z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    return sigma_x, sigma_y, sigma_z


def unitary_from_hermitian(generator: np.ndarray) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(generator)
    return eigenvectors @ np.diag(np.exp(-1j * eigenvalues)) @ eigenvectors.conj().T


def complex_to_real(unitary: np.ndarray) -> np.ndarray:
    return np.block([
        [unitary.real, -unitary.imag],
        [unitary.imag, unitary.real],
    ])


def projector(axis: np.ndarray, sign: float, pauli: tuple[np.ndarray, ...]) -> np.ndarray:
    return 0.5 * (
        np.eye(2, dtype=complex)
        + sign * sum(axis[index] * pauli[index] for index in range(3))
    )


def total_variation(first: np.ndarray, second: np.ndarray) -> float:
    return float(0.5 * np.sum(np.abs(first - second)))


def main() -> None:
    seed = 20260825
    rng = np.random.default_rng(seed)
    sigma_x, sigma_y, sigma_z = pauli_matrices()
    pauli = (sigma_x, sigma_y, sigma_z)
    identity_2 = np.eye(2, dtype=complex)
    checks: list[CheckResult] = []

    # R135: rank-one normalized second moment and its two-dimensional reduction.
    state = rng.normal(size=2) + 1j * rng.normal(size=2)
    state /= np.linalg.norm(state)
    covariance = np.outer(state, state.conj())
    bloch = np.array([
        np.trace(covariance @ matrix).real
        for matrix in pauli
    ])
    reconstructed = 0.5 * (
        identity_2
        + sum(bloch[index] * pauli[index] for index in range(3))
    )
    checks.append(record_max("rank_one_covariance_hermitian_error", np.linalg.norm(covariance - covariance.conj().T), 2.0e-14))
    checks.append(record_max("rank_one_covariance_trace_error", abs(np.trace(covariance) - 1.0), 2.0e-14))
    checks.append(record_min("rank_one_covariance_minimum_eigenvalue", np.min(np.linalg.eigvalsh(covariance)), -2.0e-14))
    checks.append(record_max("rank_one_covariance_determinant", abs(np.linalg.det(covariance)), 2.0e-14))
    checks.append(record_max("bloch_unit_norm_error", abs(np.linalg.norm(bloch) - 1.0), 2.0e-14))
    checks.append(record_max("bloch_reconstruction_error", np.linalg.norm(reconstructed - covariance), 2.0e-14))

    common_phase = np.exp(1j * rng.uniform(-pi, pi))
    phased_covariance = np.outer(common_phase * state, (common_phase * state).conj())
    checks.append(record_max("common_phase_covariance_invariance_error", np.linalg.norm(phased_covariance - covariance), 2.0e-14))

    random_hermitian = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    random_hermitian = 0.5 * (random_hermitian + random_hermitian.conj().T)
    action_scale = 1.7
    state_dot = -1j * random_hermitian @ state / action_scale
    covariance_dot_direct = np.outer(state_dot, state.conj()) + np.outer(state, state_dot.conj())
    covariance_dot_commutator = -1j * (
        random_hermitian @ covariance - covariance @ random_hermitian
    ) / action_scale
    checks.append(record_max("covariance_commutator_equation_error", np.linalg.norm(covariance_dot_direct - covariance_dot_commutator), 3.0e-14))

    propagator = unitary_from_hermitian(random_hermitian / action_scale)
    evolved_covariance = propagator @ covariance @ propagator.conj().T
    checks.append(record_max("covariance_unitary_trace_error", abs(np.trace(evolved_covariance) - 1.0), 3.0e-14))
    checks.append(record_max("covariance_unitary_rank_error", abs(np.linalg.det(evolved_covariance)), 3.0e-14))

    # R140: parity-to-localized W generator, controllability, and detuned Rabi law.
    energy_0, energy_1 = -0.37, 0.81
    mean_energy = 0.5 * (energy_0 + energy_1)
    tunnel = 0.5 * (energy_1 - energy_0)
    parity_to_local = np.array([[1.0, 1.0], [1.0, -1.0]]) / sqrt(2.0)
    localized_generator = parity_to_local.T @ np.diag([energy_0, energy_1]) @ parity_to_local
    expected_localized = mean_energy * identity_2 - tunnel * sigma_x
    checks.append(record_max("localized_w_generator_error", np.linalg.norm(localized_generator - expected_localized), 2.0e-14))

    position_matrix_element = 0.63
    parity_position = np.array([[0.0, position_matrix_element], [position_matrix_element, 0.0]])
    localized_position = parity_to_local.T @ parity_position @ parity_to_local
    checks.append(record_max("localized_tilt_offdiagonal_error", abs(localized_position[0, 1]), 2.0e-14))
    checks.append(record_max("localized_tilt_energy_gap_error", abs(abs(localized_position[0, 0] - localized_position[1, 1]) - 2.0 * position_matrix_element), 2.0e-14))

    commutator_y = sigma_x @ sigma_z - sigma_z @ sigma_x
    checks.append(record_max("tilt_control_commutator_error", np.linalg.norm(commutator_y + 2j * sigma_y), 2.0e-14))
    lie_vectors = np.stack([
        sigma_x.reshape(-1),
        sigma_z.reshape(-1),
        (0.5j * commutator_y).reshape(-1),
    ])
    checks.append(record_min("tilt_control_lie_rank", np.linalg.matrix_rank(lie_vectors), 3.0))

    epsilon = 0.74
    tunnel = 0.29
    action_scale = 1.31
    duration = 3.7
    controlled_generator = -tunnel * sigma_x + 0.5 * epsilon * sigma_z
    controlled_propagator = unitary_from_hermitian(controlled_generator * duration / action_scale)
    left_state = np.array([1.0, 0.0], dtype=complex)
    transition_numeric = abs((controlled_propagator @ left_state)[1]) ** 2
    transition_formula = (
        4.0 * tunnel**2 / (epsilon**2 + 4.0 * tunnel**2)
        * np.sin(sqrt(epsilon**2 + 4.0 * tunnel**2) * duration / (2.0 * action_scale)) ** 2
    )
    checks.append(record_max("detuned_rabi_transition_formula_error", abs(transition_numeric - transition_formula), 3.0e-14))
    checks.append(record_max("controlled_propagator_unitarity_error", np.linalg.norm(controlled_propagator.conj().T @ controlled_propagator - identity_2), 3.0e-14))

    # R140: simultaneous fast/slow switching window and locking bound.
    tunnel = 1.0e-4
    high_mode_gap = 1.0
    action_scale = 1.0
    measurement_tilt = sqrt(tunnel * high_mode_gap)
    switching_time = action_scale / sqrt(tunnel * high_mode_gap)
    hierarchy_ratios = np.array([
        tunnel / measurement_tilt,
        measurement_tilt / high_mode_gap,
        action_scale / (high_mode_gap * switching_time),
        tunnel * switching_time / action_scale,
    ])
    checks.append(record_max("tilt_switching_hierarchy_ratio_error", np.max(np.abs(hierarchy_ratios - sqrt(tunnel / high_mode_gap))), 2.0e-14))

    leakage_constant = 1.8
    leakage_bound = leakage_constant * (
        (measurement_tilt / high_mode_gap) ** 2
        + (action_scale / (high_mode_gap * switching_time)) ** 2
    )
    checks.append(record_max("two_mode_leakage_bound", leakage_bound, 4.0e-4))

    lock_bound = 4.0 * tunnel**2 / (measurement_tilt**2 + 4.0 * tunnel**2)
    sample_times = np.linspace(0.0, 50_000.0, 20_001)
    transitions = lock_bound * np.sin(
        sqrt(measurement_tilt**2 + 4.0 * tunnel**2) * sample_times / (2.0 * action_scale)
    ) ** 2
    checks.append(record_max("tilt_lock_probability_bound_excess", max(0.0, float(np.max(transitions)) - lock_bound), 2.0e-14))

    uniform_lock_bound = 2.0 * tunnel / sqrt(measurement_tilt**2 + 4.0 * tunnel**2)
    localized_projector = np.diag([1.0, 0.0]).astype(complex)
    uniform_excess = 0.0
    lock_generator = -tunnel * sigma_x + 0.5 * measurement_tilt * sigma_z
    for sample_time in np.linspace(0.0, 20_000.0, 401):
        lock_propagator = unitary_from_hermitian(lock_generator * sample_time / action_scale)
        effect_change = (
            lock_propagator.conj().T @ localized_projector @ lock_propagator
            - localized_projector
        )
        uniform_excess = max(
            uniform_excess,
            np.linalg.norm(effect_change, ord=2) - uniform_lock_bound,
        )
    checks.append(record_max("uniform_population_lock_bound_excess", max(0.0, uniform_excess), 3.0e-14))

    tunnel_family = np.array([1.0e-1, 1.0e-2, 1.0e-3, 1.0e-4])
    family_tilt = np.sqrt(tunnel_family * high_mode_gap)
    family_lock = 4.0 * tunnel_family**2 / (family_tilt**2 + 4.0 * tunnel_family**2)
    family_uniform_lock = 2.0 * tunnel_family / np.sqrt(family_tilt**2 + 4.0 * tunnel_family**2)
    family_rotation_time = pi * action_scale / (2.0 * tunnel_family)
    checks.append(record_max("deep_w_lock_error_monotonicity", np.max(np.diff(family_lock)), 0.0))
    checks.append(record_max("deep_w_uniform_lock_error_monotonicity", np.max(np.diff(family_uniform_lock)), 0.0))
    checks.append(record_min("deep_w_rotation_time_monotonicity", np.min(np.diff(family_rotation_time)), 0.0))

    # R143: finite-contrast spatial effect and Born-weight error.
    eta_w = 0.037
    left_effect = np.diag([1.0 - eta_w, eta_w]).astype(complex)
    checks.append(record_max("left_effect_eigenvalue_error", np.max(np.abs(np.linalg.eigvalsh(left_effect) - np.array([eta_w, 1.0 - eta_w]))), 2.0e-14))
    born_weights = rng.uniform(0.0, 1.0, size=10_000)
    observed_left = eta_w + (1.0 - 2.0 * eta_w) * born_weights
    checks.append(record_max("finite_contrast_born_error_bound_excess", max(0.0, float(np.max(np.abs(observed_left - born_weights))) - eta_w), 2.0e-14))
    checks.append(record_max("left_right_effect_completeness_error", np.linalg.norm(left_effect + (identity_2 - left_effect) - identity_2), 2.0e-14))

    # An arbitrary Bloch axis is rotated to the localized readout basis.
    initial_axis = rng.normal(size=3)
    initial_axis /= np.linalg.norm(initial_axis)
    measurement_axis = rng.normal(size=3)
    measurement_axis /= np.linalg.norm(measurement_axis)
    input_covariance = projector(initial_axis, 1.0, pauli)
    axis_operator = sum(measurement_axis[index] * pauli[index] for index in range(3))
    axis_values, axis_vectors = np.linalg.eigh(axis_operator)
    order = np.argsort(axis_values)[::-1]
    analyzer = axis_vectors[:, order].conj().T
    analyzed_covariance = analyzer @ input_covariance @ analyzer.conj().T
    expected_plus_weight = 0.5 * (1.0 + np.dot(initial_axis, measurement_axis))
    checks.append(record_max("arbitrary_axis_analyzer_weight_error", abs(analyzed_covariance[0, 0].real - expected_plus_weight), 3.0e-14))

    # Rank one survives conditioning on an independently assigned realized branch;
    # conditioning alone therefore does not create two post-measurement directions.
    sample_count = 120_000
    amplitudes = (0.4 + rng.random(sample_count)) * np.exp(1j * rng.uniform(-pi, pi, sample_count))
    bath_samples = amplitudes[:, None] * state[None, :]
    branch_plus = rng.random(sample_count) < expected_plus_weight
    conditional_covariances = []
    for mask in (branch_plus, ~branch_plus):
        branch_covariance = bath_samples[mask].T @ bath_samples[mask].conj()
        branch_covariance /= np.trace(branch_covariance).real
        conditional_covariances.append(branch_covariance)
    checks.append(record_max("rank_one_conditioning_direction_error", max(np.linalg.norm(item - covariance) for item in conditional_covariances), 4.0e-14))
    branch_separation = np.linalg.norm(conditional_covariances[0] - conditional_covariances[1])
    checks.append(record_max("conditioning_only_branch_separation", branch_separation, 4.0e-14))

    # R143: local canonical record shear and branch-conditioned template SWAP.
    canonical_form_2 = np.array([
        [0.0, 1.0, 0.0, 0.0],
        [-1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        [0.0, 0.0, -1.0, 0.0],
    ])
    record_shear = np.array([
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, -1.0],
        [1.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ])
    checks.append(record_max("local_record_shear_symplectic_error", np.linalg.norm(record_shear.T @ canonical_form_2 @ record_shear - canonical_form_2), 2.0e-14))
    empty_record_input = np.array([0.31, -0.27, 0.0, 0.0])
    empty_record_output = record_shear @ empty_record_input
    checks.append(record_max("empty_local_record_backreaction_error", np.linalg.norm(empty_record_output[:2] - empty_record_input[:2]), 2.0e-14))
    checks.append(record_max("local_record_pointer_copy_error", abs(empty_record_output[2] - empty_record_input[0]), 2.0e-14))

    swap_unitary = np.block([
        [np.zeros((2, 2)), np.eye(2)],
        [-np.eye(2), np.zeros((2, 2))],
    ]).astype(complex)
    swap_real = complex_to_real(swap_unitary)
    canonical_form_4 = np.block([
        [np.zeros((4, 4)), np.eye(4)],
        [-np.eye(4), np.zeros((4, 4))],
    ])
    checks.append(record_max("template_swap_symplectic_error", np.linalg.norm(swap_real.T @ canonical_form_4 @ swap_real - canonical_form_4), 3.0e-14))

    left_template = np.array([1.0, 0.0], dtype=complex)
    right_template = np.array([0.0, 1.0], dtype=complex)
    for label, template in (("left", left_template), ("right", right_template)):
        swapped = swap_unitary @ np.concatenate([state, template])
        output_covariance = np.outer(swapped[:2], swapped[:2].conj())
        target_covariance = np.outer(template, template.conj())
        checks.append(record_max(f"{label}_branch_template_covariance_error", np.linalg.norm(output_covariance - target_covariance), 2.0e-14))

    # Same-axis repeatability and distinct-axis sequential Born law.
    second_axis = rng.normal(size=3)
    second_axis /= np.linalg.norm(second_axis)
    signs = (1.0, -1.0)
    joint = np.zeros((2, 2))
    first_weights = np.zeros(2)
    for first_index, first_sign in enumerate(signs):
        first_projection = projector(measurement_axis, first_sign, pauli)
        first_weights[first_index] = np.trace(first_projection @ input_covariance).real
        for second_index, second_sign in enumerate(signs):
            second_projection = projector(second_axis, second_sign, pauli)
            conditional_weight = np.trace(second_projection @ first_projection).real
            joint[first_index, second_index] = first_weights[first_index] * conditional_weight
    checks.append(record_max("sequential_born_normalization_error", abs(np.sum(joint) - 1.0), 3.0e-14))
    checks.append(record_max("sequential_born_first_marginal_error", np.max(np.abs(np.sum(joint, axis=1) - first_weights)), 3.0e-14))
    same_axis_wrong = np.trace(projector(measurement_axis, -1.0, pauli) @ projector(measurement_axis, 1.0, pauli)).real
    checks.append(record_max("same_axis_repeat_wrong_weight", abs(same_axis_wrong), 3.0e-14))

    # Error composition keeps no-response mass and obeys total-variation triangle bounds.
    distribution_chain = [
        np.array([0.56, 0.44, 0.0]),
        np.array([0.55, 0.44, 0.01]),
        np.array([0.55, 0.425, 0.025]),
        np.array([0.543, 0.425, 0.032]),
    ]
    step_distances = [
        total_variation(distribution_chain[index], distribution_chain[index + 1])
        for index in range(len(distribution_chain) - 1)
    ]
    endpoint_distance = total_variation(distribution_chain[0], distribution_chain[-1])
    checks.append(record_max("instrument_tv_triangle_bound_excess", max(0.0, endpoint_distance - sum(step_distances)), 2.0e-14))
    checks.append(record_max("no_response_mass_preservation_error", abs(distribution_chain[-1][2] - 0.032), 2.0e-14))

    # R144: weak-open exchange reset and its recurrence bound.
    reset_angle = 0.47
    reset_rotation = np.array([
        [np.cos(reset_angle), np.sin(reset_angle)],
        [-np.sin(reset_angle), np.cos(reset_angle)],
    ])
    checks.append(record_max("reset_exchange_orthogonality_error", np.linalg.norm(reset_rotation.T @ reset_rotation - np.eye(2)), 2.0e-14))
    contraction = abs(np.cos(reset_angle))
    injection = 0.003 + abs(np.sin(reset_angle)) * 0.02
    residual = 0.8
    step_count = 200
    for _ in range(step_count):
        residual = contraction * residual + injection
    asymptotic_bound = injection / (1.0 - contraction)
    finite_bound = contraction**step_count * 0.8 + (1.0 - contraction**step_count) * asymptotic_bound
    checks.append(record_max("reset_recurrence_bound_excess", max(0.0, residual - finite_bound), 2.0e-14))

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
