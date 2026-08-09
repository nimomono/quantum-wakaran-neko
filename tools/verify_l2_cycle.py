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


def record_equal(name: str, value: float, expected: float) -> CheckResult:
    error = abs(value - expected)
    return CheckResult(name, float(error), 0.0, "==", bool(error == 0.0))


def pauli_matrices() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    sigma_x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sigma_y = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
    sigma_z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    return sigma_x, sigma_y, sigma_z


def rotation(generator: np.ndarray, angle: float) -> np.ndarray:
    identity = np.eye(2, dtype=complex)
    return np.cos(angle / 2.0) * identity - 1j * np.sin(angle / 2.0) * generator


def complex_to_real(unitary: np.ndarray) -> np.ndarray:
    return np.block([
        [unitary.real, -unitary.imag],
        [unitary.imag, unitary.real],
    ])


def main() -> None:
    seed = 20260810
    rng = np.random.default_rng(seed)
    sigma_x, sigma_y, sigma_z = pauli_matrices()
    pauli = (sigma_x, sigma_y, sigma_z)
    checks: list[CheckResult] = []

    # Fixed-action Hopf map and Pauli algebra.
    states = rng.normal(size=(1000, 2)) + 1j * rng.normal(size=(1000, 2))
    states /= np.linalg.norm(states, axis=1)[:, None]
    bloch = np.stack([
        np.einsum("bi,ij,bj->b", states.conj(), matrix, states).real
        for matrix in pauli
    ], axis=1)
    checks.append(record_max(
        "bloch_unit_norm_error",
        np.max(np.abs(np.sum(bloch * bloch, axis=1) - 1.0)),
        2.0e-14,
    ))

    common_phases = np.exp(1j * rng.uniform(0.0, 2.0 * pi, size=len(states)))
    phased_states = states * common_phases[:, None]
    phased_bloch = np.stack([
        np.einsum("bi,ij,bj->b", phased_states.conj(), matrix, phased_states).real
        for matrix in pauli
    ], axis=1)
    checks.append(record_max(
        "common_phase_invariance_error",
        np.max(np.abs(phased_bloch - bloch)),
        2.0e-14,
    ))

    commutator_errors = []
    coordinate_axes = np.eye(3)
    for i in range(3):
        for j in range(3):
            epsilon_ijk = np.cross(coordinate_axes[i], coordinate_axes[j])
            expected = sum(
                2j * epsilon_ijk[k] * pauli[k]
                for k in range(3)
            )
            commutator_errors.append(np.linalg.norm(
                pauli[i] @ pauli[j] - pauli[j] @ pauli[i] - expected
            ))
    checks.append(record_max("pauli_commutator_error", max(commutator_errors), 2.0e-14))

    # Euler SU(2) pulses and their real symplectic representation.
    alpha, beta, gamma = rng.uniform(-pi, pi, size=3)
    unitary = (
        rotation(sigma_z, alpha)
        @ rotation(sigma_x, beta)
        @ rotation(sigma_z, gamma)
    )
    checks.append(record_max(
        "su2_unitarity_error",
        np.linalg.norm(unitary.conj().T @ unitary - np.eye(2)),
        2.0e-14,
    ))
    checks.append(record_max(
        "su2_determinant_error",
        abs(np.linalg.det(unitary) - 1.0),
        2.0e-14,
    ))
    real_map = complex_to_real(unitary)
    symplectic_form = np.block([
        [np.zeros((2, 2)), np.eye(2)],
        [-np.eye(2), np.zeros((2, 2))],
    ])
    checks.append(record_max(
        "su2_real_symplectic_error",
        np.linalg.norm(real_map.T @ symplectic_form @ real_map - symplectic_form),
        3.0e-14,
    ))

    # Rabi analytic solution and exact Bloch precession.
    detuning, drive, time = 0.37, 0.83, 4.2
    rabi_frequency = np.hypot(detuning, drive)
    generator = detuning * sigma_z + drive * sigma_x
    propagator = (
        np.cos(rabi_frequency * time / 2.0) * np.eye(2)
        - 1j * np.sin(rabi_frequency * time / 2.0) * generator / rabi_frequency
    )
    evolved = propagator @ np.array([1.0, 0.0], dtype=complex)
    transition = abs(evolved[1]) ** 2
    expected_transition = (
        drive**2 / (drive**2 + detuning**2)
        * np.sin(rabi_frequency * time / 2.0) ** 2
    )
    checks.append(record_max(
        "rabi_transition_formula_error",
        abs(transition - expected_transition),
        2.0e-14,
    ))

    # Arbitrary-axis weights, same-axis repeatability, and distinct-axis joint law.
    def random_axis() -> np.ndarray:
        axis = rng.normal(size=3)
        return axis / np.linalg.norm(axis)

    initial_axis = random_axis()
    first_axis = random_axis()
    second_axis = random_axis()
    first_weights = np.array([
        (1.0 + np.dot(first_axis, initial_axis)) / 2.0,
        (1.0 - np.dot(first_axis, initial_axis)) / 2.0,
    ])
    checks.append(record_max(
        "arbitrary_axis_weight_normalization_error",
        abs(np.sum(first_weights) - 1.0),
        2.0e-14,
    ))
    same_axis_wrong_weight = (1.0 - np.dot(first_axis, first_axis)) / 2.0
    checks.append(record_max(
        "same_axis_wrong_safe_weight",
        abs(same_axis_wrong_weight),
        2.0e-14,
    ))

    joint = np.zeros((2, 2))
    signs = (1.0, -1.0)
    for i, sign_s in enumerate(signs):
        for j, sign_t in enumerate(signs):
            joint[i, j] = (
                (1.0 + sign_s * np.dot(first_axis, initial_axis)) / 2.0
                * (1.0 + sign_s * sign_t * np.dot(first_axis, second_axis)) / 2.0
            )
    checks.append(record_max(
        "sequential_joint_normalization_error",
        abs(np.sum(joint) - 1.0),
        2.0e-14,
    ))
    checks.append(record_max(
        "sequential_first_marginal_error",
        np.max(np.abs(np.sum(joint, axis=1) - first_weights)),
        2.0e-14,
    ))

    samples = 200_000
    alpha_1 = sqrt(2.0) - 1.0
    alpha_2 = sqrt(3.0) - 1.0
    index = np.arange(samples)
    selector_1 = np.mod(0.173 + index * alpha_1, 1.0)
    selector_2 = np.mod(0.419 + index * alpha_2, 1.0)
    first_plus = selector_1 < first_weights[0]
    conditional_plus = np.where(
        first_plus,
        (1.0 + np.dot(first_axis, second_axis)) / 2.0,
        (1.0 - np.dot(first_axis, second_axis)) / 2.0,
    )
    second_plus = selector_2 < conditional_plus
    empirical = np.array([
        [np.mean(first_plus & second_plus), np.mean(first_plus & ~second_plus)],
        [np.mean(~first_plus & second_plus), np.mean(~first_plus & ~second_plus)],
    ])
    checks.append(record_max(
        "two_torus_joint_frequency_error",
        np.max(np.abs(empirical - joint)),
        2.0e-4,
    ))

    # Canonical record shear generated by P_R q.
    record_shear = np.array([
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, -1.0],
        [1.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ])
    canonical_form = np.array([
        [0.0, 1.0, 0.0, 0.0],
        [-1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        [0.0, 0.0, -1.0, 0.0],
    ])
    checks.append(record_max(
        "record_shear_symplectic_error",
        np.linalg.norm(record_shear.T @ canonical_form @ record_shear - canonical_form),
        2.0e-14,
    ))
    test_point = np.array([0.31, -0.27, 0.0, 0.0])
    recorded_point = record_shear @ test_point
    checks.append(record_max(
        "empty_record_cell_backreaction_error",
        np.linalg.norm(recorded_point[:2] - test_point[:2]),
        2.0e-14,
    ))

    # Record, then exact internal uncomputation.
    signal = states[0]
    forward_signal = unitary @ signal
    restored_signal = unitary.conj().T @ forward_signal
    checks.append(record_max(
        "internal_uncompute_error",
        np.linalg.norm(restored_signal - signal),
        2.0e-14,
    ))

    # Reset rotation, perfect swap, and recurrence bound.
    phi = 0.47
    reset_rotation = np.array([
        [np.cos(phi), np.sin(phi)],
        [-np.sin(phi), np.cos(phi)],
    ])
    checks.append(record_max(
        "reset_rotation_orthogonality_error",
        np.linalg.norm(reset_rotation.T @ reset_rotation - np.eye(2)),
        2.0e-14,
    ))
    perfect_swap = np.array([
        [np.cos(pi / 2.0), np.sin(pi / 2.0)],
        [-np.sin(pi / 2.0), np.cos(pi / 2.0)],
    ])
    checks.append(record_max(
        "perfect_swap_device_output_error",
        abs((perfect_swap @ np.array([0.73, -0.11]))[0] + 0.11),
        2.0e-14,
    ))

    contraction = abs(np.cos(phi))
    injection = abs(np.sin(phi)) * 0.02 + 0.003
    state = 0.8
    reset_steps = 200
    for _ in range(reset_steps):
        state = contraction * state + injection
    recurrence_bound = injection / (1.0 - contraction)
    finite_step_bound = (
        contraction**reset_steps * 0.8
        + (1.0 - contraction**reset_steps) * recurrence_bound
    )
    checks.append(record_max(
        "reset_recurrence_bound_excess",
        max(0.0, state - finite_step_bound),
        2.0e-14,
    ))

    # Resource arithmetic, including the corrected L=2 count.
    checks.append(record_equal("m35_l2_pair_count_error", 3 * 2 + 4, 10))
    checks.append(record_equal("two_stage_active_pair_count_error", 2 + 2 * 7 + 1, 17))
    checks.append(record_equal("reset_cell_pair_count_error", 2 + 2 * 6, 14))
    trial_count = 11
    checks.append(record_equal(
        "finite_closed_embedding_pair_count_error",
        17 + 16 * trial_count,
        193,
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
