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


def total_variation(first: np.ndarray, second: np.ndarray) -> float:
    return float(0.5 * np.sum(np.abs(first - second)))


def random_unitary(rng: np.random.Generator, size: int) -> np.ndarray:
    matrix = rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))
    q_matrix, r_matrix = np.linalg.qr(matrix)
    diagonal = np.diag(r_matrix)
    phases = np.where(np.abs(diagonal) > 0.0, diagonal / np.abs(diagonal), 1.0)
    return q_matrix @ np.diag(phases.conj())


def path_sum(paths: list[tuple[complex, np.ndarray, np.ndarray]]) -> np.ndarray:
    return sum(
        coefficient * np.outer(left, right)
        for coefficient, left, right in paths
    )


def cnot_paths(
    paths: list[tuple[complex, np.ndarray, np.ndarray]],
) -> list[tuple[complex, np.ndarray, np.ndarray]]:
    p0 = np.diag([1.0, 0.0]).astype(complex)
    p1 = np.diag([0.0, 1.0]).astype(complex)
    x_gate = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    children: list[tuple[complex, np.ndarray, np.ndarray]] = []
    for coefficient, left, right in paths:
        children.append((coefficient, p0 @ left, right))
        children.append((coefficient, p1 @ left, x_gate @ right))
    return children


def cnot_matrix() -> np.ndarray:
    return np.array(
        [
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
            [0.0, 0.0, 1.0, 0.0],
        ],
        dtype=complex,
    )


def main() -> None:
    seed = 20260902
    rng = np.random.default_rng(seed)
    checks: list[CheckResult] = []
    cx = cnot_matrix()

    maximum_reconstruction_error = 0.0
    maximum_local_covariance_error = 0.0
    maximum_cnot_path_error = 0.0
    maximum_inverse_error = 0.0
    maximum_permutation_error = 0.0
    maximum_phase_error = 0.0

    for _ in range(1_000):
        matrix = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        matrix /= np.linalg.norm(matrix)
        u_matrix, singular_values, vh_matrix = np.linalg.svd(matrix)
        paths = [
            (singular_values[index], u_matrix[:, index], vh_matrix[index, :].T)
            for index in range(2)
        ]
        reconstructed = path_sum(paths)
        maximum_reconstruction_error = max(
            maximum_reconstruction_error,
            float(np.linalg.norm(reconstructed - matrix)),
        )

        unitary_a = random_unitary(rng, 2)
        unitary_b = random_unitary(rng, 2)
        transformed_paths = [
            (coefficient, unitary_a @ left, unitary_b @ right)
            for coefficient, left, right in paths
        ]
        expected_local = unitary_a @ matrix @ unitary_b.T
        maximum_local_covariance_error = max(
            maximum_local_covariance_error,
            float(np.linalg.norm(path_sum(transformed_paths) - expected_local)),
        )

        cnot_output_paths = cnot_paths(paths)
        expected_cnot = (cx @ matrix.reshape(4)).reshape(2, 2)
        maximum_cnot_path_error = max(
            maximum_cnot_path_error,
            float(np.linalg.norm(path_sum(cnot_output_paths) - expected_cnot)),
        )
        inverse_output = path_sum(cnot_paths(cnot_output_paths))
        maximum_inverse_error = max(
            maximum_inverse_error,
            float(np.linalg.norm(inverse_output - matrix)),
        )

        maximum_permutation_error = max(
            maximum_permutation_error,
            float(np.linalg.norm(path_sum(list(reversed(paths))) - matrix)),
        )
        phase = np.exp(1j * rng.uniform(-np.pi, np.pi))
        phased = [(phase * coefficient, left, right) for coefficient, left, right in paths]
        maximum_phase_error = max(
            maximum_phase_error,
            float(np.linalg.norm(path_sum(phased) - phase * matrix)),
        )

    checks.append(record_max("finite_path_svd_reconstruction_error", maximum_reconstruction_error, 2.0e-14))
    checks.append(record_max("local_path_covariance_error", maximum_local_covariance_error, 3.0e-14))
    checks.append(record_max("pathwise_cnot_error", maximum_cnot_path_error, 2.0e-14))
    checks.append(record_max("double_cnot_inverse_error", maximum_inverse_error, 3.0e-14))
    checks.append(record_max("path_permutation_invariance_error", maximum_permutation_error, 2.0e-14))
    checks.append(record_max("common_path_phase_covariance_error", maximum_phase_error, 2.0e-14))

    identity_2 = np.eye(2, dtype=complex)
    checks.append(record_max("cnot_unitarity_error", float(np.linalg.norm(cx.conj().T @ cx - np.eye(4))), 0.0))
    checks.append(record_max("cnot_involution_error", float(np.linalg.norm(cx @ cx - np.eye(4))), 0.0))

    plus = np.array([1.0, 1.0], dtype=complex) / sqrt(2.0)
    zero = np.array([1.0, 0.0], dtype=complex)
    bell_paths = cnot_paths([(1.0, plus, zero)])
    bell_matrix = path_sum(bell_paths)
    checks.append(record_max("bell_path_matrix_error", float(np.linalg.norm(bell_matrix - identity_2 / sqrt(2.0))), 2.0e-15))
    checks.append(record_max("bell_determinant_error", abs(abs(np.linalg.det(bell_matrix)) - 0.5), 2.0e-15))
    selected_branch = bell_paths[0][0] * np.outer(bell_paths[0][1], bell_paths[0][2])
    checks.append(record_max("single_branch_rank_one_determinant", abs(np.linalg.det(selected_branch)), 0.0))

    reference_dimension = 5
    reference_state = rng.normal(size=4 * reference_dimension) + 1j * rng.normal(size=4 * reference_dimension)
    reference_state /= np.linalg.norm(reference_state)
    direct_reference = np.kron(cx, np.eye(reference_dimension)) @ reference_state
    reshaped = reference_state.reshape(4, reference_dimension)
    path_reference = (cx @ reshaped).reshape(-1)
    checks.append(record_max("reference_stability_error", float(np.linalg.norm(direct_reference - path_reference)), 3.0e-14))

    h_gate = np.array([[1.0, 1.0], [1.0, -1.0]], dtype=complex) / sqrt(2.0)
    t_gate = np.diag([1.0, np.exp(1j * np.pi / 4.0)])
    cx_ab = np.kron(cx, identity_2)
    cx_bc = np.zeros((8, 8), dtype=complex)
    for a_bit in range(2):
        for b_bit in range(2):
            for c_bit in range(2):
                source = 4 * a_bit + 2 * b_bit + c_bit
                target = 4 * a_bit + 2 * b_bit + (c_bit ^ b_bit)
                cx_bc[target, source] = 1.0
    h_a = np.kron(np.kron(h_gate, identity_2), identity_2)
    t_a = np.kron(np.kron(t_gate, identity_2), identity_2)
    state_000 = np.eye(8, dtype=complex)[:, 0]
    ghz = cx_bc @ cx_ab @ h_a @ state_000
    expected_ghz = (np.eye(8)[:, 0] + np.eye(8)[:, 7]) / sqrt(2.0)
    checks.append(record_max("two_gate_ghz_error", float(np.linalg.norm(ghz - expected_ghz)), 2.0e-15))

    coherent_final = h_a @ cx_ab @ cx_bc @ t_a @ ghz
    coherent_probabilities = np.abs(coherent_final) ** 2
    expected_coherent = np.zeros(8)
    expected_coherent[0] = np.cos(np.pi / 8.0) ** 2
    expected_coherent[4] = np.sin(np.pi / 8.0) ** 2
    checks.append(record_max("ghz_t_inverse_probability_error", float(np.max(np.abs(coherent_probabilities - expected_coherent))), 3.0e-15))

    mixed_input = np.zeros((8, 8), dtype=complex)
    mixed_input[0, 0] = 0.5
    mixed_input[7, 7] = 0.5
    inverse_unitary = h_a @ cx_ab @ cx_bc @ t_a
    mixed_output = inverse_unitary @ mixed_input @ inverse_unitary.conj().T
    mixed_probabilities = np.real(np.diag(mixed_output))
    expected_mixed = np.zeros(8)
    expected_mixed[0] = 0.5
    expected_mixed[4] = 0.5
    checks.append(record_max("dephased_inverse_probability_error", float(np.max(np.abs(mixed_probabilities - expected_mixed))), 3.0e-15))

    coherence_gap = total_variation(coherent_probabilities, mixed_probabilities)
    checks.append(record_max("coherence_tv_gap_formula_error", abs(coherence_gap - 1.0 / (2.0 * sqrt(2.0))), 3.0e-15))
    checks.append(record_min("coherence_positive_margin", coherence_gap - 0.12, 0.2))

    decoded = bell_matrix.reshape(4)
    born_probabilities = np.abs(decoded) ** 2
    checks.append(record_max("terminal_decoder_born_error", float(np.max(np.abs(born_probabilities - np.array([0.5, 0.0, 0.0, 0.5])))), 2.0e-15))
    q_reference = np.array([0.1, 0.2, 0.3, 0.4])
    delta = 0.017
    regularized = (born_probabilities + delta * q_reference) / (1.0 + delta)
    regularization_tv = total_variation(regularized, born_probabilities)
    checks.append(record_max("r164_regularization_tv_bound_excess", max(0.0, regularization_tv - delta / (1.0 + delta)), 2.0e-15))

    no_response = 0.006
    complete_observed = np.concatenate(((1.0 - no_response) * born_probabilities, [no_response]))
    complete_ideal = np.concatenate((born_probabilities, [0.0]))
    checks.append(record_max("no_response_complete_space_formula_error", abs(total_variation(complete_observed, complete_ideal) - no_response), 2.0e-15))

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
