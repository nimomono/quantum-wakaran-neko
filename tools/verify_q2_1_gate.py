#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from math import pi

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


def unitary_from_hermitian(generator: np.ndarray) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(generator)
    return eigenvectors @ np.diag(np.exp(-1j * eigenvalues)) @ eigenvectors.conj().T


def random_unitary(rng: np.random.Generator, size: int) -> np.ndarray:
    matrix = rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))
    q_matrix, r_matrix = np.linalg.qr(matrix)
    phases = np.diag(r_matrix)
    phases = np.where(np.abs(phases) > 0.0, phases / np.abs(phases), 1.0)
    return q_matrix @ np.diag(phases.conj())


def complex_to_real(unitary: np.ndarray) -> np.ndarray:
    return np.block([
        [unitary.real, -unitary.imag],
        [unitary.imag, unitary.real],
    ])


def operator_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.norm(matrix, ord=2))


def main() -> None:
    seed = 20260810
    rng = np.random.default_rng(seed)
    identity_2 = np.eye(2, dtype=complex)
    identity_4 = np.eye(4, dtype=complex)
    sigma_x, sigma_y, sigma_z = pauli_matrices()
    pauli = (sigma_x, sigma_y, sigma_z)
    local_a = tuple(np.kron(matrix, identity_2) for matrix in pauli)
    local_b = tuple(np.kron(identity_2, matrix) for matrix in pauli)
    checks: list[CheckResult] = []

    # The two local control algebras commute and each closes as su(2).
    local_commutators = [
        operator_norm(matrix_a @ matrix_b - matrix_b @ matrix_a)
        for matrix_a in local_a
        for matrix_b in local_b
    ]
    checks.append(record_max(
        "local_algebra_commutator_error",
        max(local_commutators),
        2.0e-14,
    ))
    axes = np.eye(3)
    su2_errors = []
    for algebra in (local_a, local_b):
        for i in range(3):
            for j in range(3):
                cross = np.cross(axes[i], axes[j])
                expected = sum(2j * cross[k] * algebra[k] for k in range(3))
                su2_errors.append(operator_norm(
                    algebra[i] @ algebra[j] - algebra[j] @ algebra[i] - expected
                ))
    checks.append(record_max("local_su2_closure_error", max(su2_errors), 2.0e-14))

    # Local operations preserve the rank-one product-state condition.
    factor_a = rng.normal(size=2) + 1j * rng.normal(size=2)
    factor_b = rng.normal(size=2) + 1j * rng.normal(size=2)
    factor_a /= np.linalg.norm(factor_a)
    factor_b /= np.linalg.norm(factor_b)
    product_state = np.kron(factor_a, factor_b)
    unitary_a = random_unitary(rng, 2)
    unitary_b = random_unitary(rng, 2)
    local_output = np.kron(unitary_a, unitary_b) @ product_state
    checks.append(record_max(
        "local_product_determinant_error",
        abs(np.linalg.det(local_output.reshape(2, 2))),
        2.0e-14,
    ))

    # Difference-mode projector and exact controlled-NOT flow.
    difference_mode = np.array([0.0, 0.0, 1.0, -1.0], dtype=complex) / np.sqrt(2.0)
    projector = np.outer(difference_mode, difference_mode.conj())
    checks.append(record_max(
        "cx_projector_idempotency_error",
        operator_norm(projector @ projector - projector),
        2.0e-14,
    ))
    cnot = np.array([
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        [0.0, 0.0, 1.0, 0.0],
    ], dtype=complex)
    cx_flow = identity_4 - 2.0 * projector
    checks.append(record_max("exact_cnot_matrix_error", operator_norm(cx_flow - cnot), 2.0e-14))

    truth_table_error = max(
        np.linalg.norm(cx_flow @ identity_4[:, index] - cnot[:, index])
        for index in range(4)
    )
    checks.append(record_max("cnot_truth_table_error", truth_table_error, 2.0e-14))
    checks.append(record_max(
        "cnot_action_conservation_error",
        operator_norm(cx_flow.conj().T @ cx_flow - identity_4),
        2.0e-14,
    ))

    real_cnot = complex_to_real(cx_flow)
    symplectic_form = np.block([
        [np.zeros((4, 4)), np.eye(4)],
        [-np.eye(4), np.zeros((4, 4))],
    ])
    checks.append(record_max(
        "cnot_real_symplectic_error",
        operator_norm(real_cnot.T @ symplectic_form @ real_cnot - symplectic_form),
        3.0e-14,
    ))

    # A product input becomes a maximally nonfactorized logical state.
    plus_zero = np.array([1.0, 0.0, 1.0, 0.0], dtype=complex) / np.sqrt(2.0)
    phi_plus_output = cx_flow @ plus_zero
    nonfactorization = 2.0 * abs(np.linalg.det(phi_plus_output.reshape(2, 2)))
    checks.append(record_max(
        "maximal_nonfactorization_error",
        abs(nonfactorization - 1.0),
        2.0e-14,
    ))
    correlations = np.array([
        np.vdot(phi_plus_output, np.kron(sigma_x, sigma_x) @ phi_plus_output).real,
        np.vdot(phi_plus_output, np.kron(sigma_y, sigma_y) @ phi_plus_output).real,
        np.vdot(phi_plus_output, np.kron(sigma_z, sigma_z) @ phi_plus_output).real,
    ])
    checks.append(record_max(
        "logical_correlation_error",
        np.max(np.abs(correlations - np.array([1.0, -1.0, 1.0]))),
        2.0e-14,
    ))

    # Exact pulse-area error formulas over several principal-value errors.
    area_errors = np.linspace(-0.9 * pi, 0.9 * pi, 17)
    worst_formula_errors = []
    average_formula_errors = []
    truth_formula_errors = []
    output_formula_errors = []
    indicator_formula_errors = []
    matrix_distance_errors = []
    projective_distance_errors = []
    for delta_area in area_errors:
        relative = identity_4 + (np.exp(-1j * delta_area) - 1.0) * projector
        implemented = cx_flow @ relative
        expected_sine = np.sin(delta_area / 2.0) ** 2

        probabilities = np.linspace(0.0, 1.0, 2001)
        sampled_fidelities = np.abs(
            1.0 - probabilities + probabilities * np.exp(-1j * delta_area)
        ) ** 2
        worst_infidelity = 1.0 - np.min(sampled_fidelities)
        worst_formula_errors.append(abs(worst_infidelity - expected_sine))

        average_fidelity = (abs(np.trace(relative)) ** 2 + 4.0) / 20.0
        average_formula_errors.append(abs(
            average_fidelity - (1.0 - 3.0 * expected_sine / 5.0)
        ))

        control_one_output = implemented @ identity_4[:, 2]
        truth_error = 1.0 - abs(np.vdot(identity_4[:, 3], control_one_output)) ** 2
        truth_formula_errors.append(abs(truth_error - expected_sine))

        actual_output = implemented @ plus_zero
        output_fidelity = abs(np.vdot(phi_plus_output, actual_output)) ** 2
        output_formula_errors.append(abs(
            (1.0 - output_fidelity) - 3.0 * expected_sine / 4.0
        ))
        actual_indicator = 2.0 * abs(np.linalg.det(actual_output.reshape(2, 2)))
        indicator_formula_errors.append(abs(
            actual_indicator - abs(np.cos(delta_area / 2.0))
        ))

        matrix_distance = operator_norm(implemented - cx_flow)
        matrix_distance_errors.append(abs(
            matrix_distance - 2.0 * abs(np.sin(delta_area / 2.0))
        ))
        midpoint_phase = np.exp(-0.5j * delta_area)
        projective_distance = operator_norm(relative - midpoint_phase * identity_4)
        projective_distance_errors.append(abs(
            projective_distance - 2.0 * np.sin(abs(delta_area) / 4.0)
        ))

    checks.append(record_max("worst_input_infidelity_formula_error", max(worst_formula_errors), 2.0e-14))
    checks.append(record_max("average_gate_fidelity_formula_error", max(average_formula_errors), 2.0e-14))
    checks.append(record_max("truth_table_area_error_formula_error", max(truth_formula_errors), 2.0e-14))
    checks.append(record_max("plus_zero_output_fidelity_formula_error", max(output_formula_errors), 2.0e-14))
    checks.append(record_max("nonfactorization_area_formula_error", max(indicator_formula_errors), 2.0e-14))
    checks.append(record_max("fixed_gauge_distance_formula_error", max(matrix_distance_errors), 2.0e-14))
    checks.append(record_max("projective_distance_formula_error", max(projective_distance_errors), 2.0e-14))

    # A small time-dependent Hermitian perturbation obeys the Duhamel bound.
    steps = 80
    duration = 1.0
    step_size = duration / steps
    ideal_generator = pi * projector
    actual_propagator = identity_4.copy()
    eta_bound = 0.0
    for _ in range(steps):
        random_matrix = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
        perturbation = 2.0e-3 * (random_matrix + random_matrix.conj().T) / 2.0
        perturbation -= np.trace(perturbation).real * identity_4 / 4.0
        eta_bound += operator_norm(perturbation) * step_size
        step_unitary = unitary_from_hermitian((ideal_generator + perturbation) * step_size)
        actual_propagator = step_unitary @ actual_propagator
    duhamel_excess = max(0.0, operator_norm(actual_propagator - cx_flow) - eta_bound)
    checks.append(record_max("duhamel_operator_bound_excess", duhamel_excess, 2.0e-14))

    # Explicit resource upper bounds.
    checks.append(record_equal("m39_gate_pair_count_error", 4 + 1, 5))
    checks.append(record_equal("m35_l4_pair_count_error", 3 * 4 + 4, 16))

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
