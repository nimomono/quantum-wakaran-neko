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


def random_unit_vector(rng: np.random.Generator, size: int) -> np.ndarray:
    vector = rng.normal(size=size) + 1j * rng.normal(size=size)
    return vector / np.linalg.norm(vector)


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


def controlled_x(size: int, control: int, target: int) -> np.ndarray:
    dimension = 2**size
    matrix = np.zeros((dimension, dimension), dtype=complex)
    for source in range(dimension):
        bits = [(source >> (size - 1 - index)) & 1 for index in range(size)]
        if bits[control]:
            bits[target] ^= 1
        destination = sum(bit << (size - 1 - index) for index, bit in enumerate(bits))
        matrix[destination, source] = 1.0
    return matrix


def main() -> None:
    seed = 20260903
    rng = np.random.default_rng(seed)
    checks: list[CheckResult] = []
    tolerance = 4.0e-14

    # R181B: real symplectic splitter and the corrected sqrt(2) lift normalization.
    s0 = np.array(
        [
            [1.0, 0.0, 0.0, -1.0],
            [0.0, 1.0, 1.0, 0.0],
            [1.0, 0.0, 0.0, 1.0],
            [0.0, 1.0, -1.0, 0.0],
        ]
    ) / sqrt(2.0)
    j2 = np.array([[0.0, 1.0], [-1.0, 0.0]])
    symplectic_form = np.kron(np.eye(2), j2)
    checks.append(record_max("s0_symplectic_error", np.linalg.norm(s0.T @ symplectic_form @ s0 - symplectic_form), tolerance))
    checks.append(record_max("s0_determinant_error", abs(np.linalg.det(s0) - 1.0), tolerance))
    checks.append(record_max("s0_inverse_error", np.linalg.norm(np.linalg.inv(s0) @ s0 - np.eye(4)), tolerance))

    maximum_lift_error = 0.0
    maximum_anti_error = 0.0
    maximum_lift_inverse_error = 0.0
    maximum_norm_product_error = 0.0
    for _ in range(1_000):
        a = random_unit_vector(rng, 2)
        b = random_unit_vector(rng, 2)
        lifted = np.empty(4, dtype=complex)
        anti = np.empty(4, dtype=complex)
        for index, product in enumerate(np.kron(a, b)):
            # s_C cancels: w_x=sqrt(2) Re(product), w_y=sqrt(2) Im(product).
            wx = sqrt(2.0) * product.real
            wy = sqrt(2.0) * product.imag
            initial = np.array([wx, 0.0, wy, 0.0])
            transformed = s0 @ initial
            lifted[index] = transformed[0] + 1j * transformed[1]
            anti[index] = transformed[2] + 1j * transformed[3]
            recovered = np.linalg.inv(s0) @ transformed
            maximum_lift_inverse_error = max(maximum_lift_inverse_error, float(np.linalg.norm(recovered - initial)))
        expected = np.kron(a, b)
        maximum_lift_error = max(maximum_lift_error, float(np.linalg.norm(lifted - expected)))
        maximum_anti_error = max(maximum_anti_error, float(np.linalg.norm(anti - expected.conj())))
        maximum_norm_product_error = max(
            maximum_norm_product_error,
            abs(np.linalg.norm(lifted) - np.linalg.norm(a) * np.linalg.norm(b)),
        )
    checks.append(record_max("tensor_lift_normalization_error", maximum_lift_error, tolerance))
    checks.append(record_max("tensor_lift_anti_register_error", maximum_anti_error, tolerance))
    checks.append(record_max("tensor_lift_inverse_error", maximum_lift_inverse_error, tolerance))
    checks.append(record_max("tensor_lift_norm_product_error", maximum_norm_product_error, tolerance))

    # R181C: difference-mode projector and persistent-register composition.
    cx = cnot_matrix()
    difference = np.array([0.0, 0.0, 1.0, -1.0], dtype=complex) / sqrt(2.0)
    projector = np.outer(difference, difference.conj())
    cx_from_projector = np.eye(4) - 2.0 * projector
    checks.append(record_max("difference_projector_idempotence_error", np.linalg.norm(projector @ projector - projector), tolerance))
    checks.append(record_max("cnot_projector_formula_error", np.linalg.norm(cx_from_projector - cx), tolerance))
    checks.append(record_max("cnot_unitarity_error", np.linalg.norm(cx.conj().T @ cx - np.eye(4)), 0.0))
    checks.append(record_max("cnot_involution_error", np.linalg.norm(cx @ cx - np.eye(4)), 0.0))

    maximum_product_cnot_error = 0.0
    for _ in range(1_000):
        a = random_unit_vector(rng, 2)
        b = random_unit_vector(rng, 2)
        persistent_register = np.kron(a, b)
        maximum_product_cnot_error = max(
            maximum_product_cnot_error,
            float(np.linalg.norm(cx_from_projector @ persistent_register - cx @ np.kron(a, b))),
        )
    checks.append(record_max("persistent_register_cnot_error", maximum_product_cnot_error, tolerance))

    reference_dimension = 5
    reference_state = random_unit_vector(rng, 4 * reference_dimension)
    direct_reference = np.kron(cx, np.eye(reference_dimension)) @ reference_state
    reshaped_reference = reference_state.reshape(4, reference_dimension)
    checks.append(record_max("reference_stability_error", np.linalg.norm(direct_reference - (cx @ reshaped_reference).reshape(-1)), tolerance))

    plus = np.array([1.0, 1.0], dtype=complex) / sqrt(2.0)
    zero = np.array([1.0, 0.0], dtype=complex)
    bell = cx @ np.kron(plus, zero)
    expected_bell = np.array([1.0, 0.0, 0.0, 1.0], dtype=complex) / sqrt(2.0)
    checks.append(record_max("bell_state_error", np.linalg.norm(bell - expected_bell), tolerance))
    checks.append(record_max("bell_inverse_error", np.linalg.norm(cx @ bell - np.kron(plus, zero)), tolerance))

    h_gate = np.array([[1.0, 1.0], [1.0, -1.0]], dtype=complex) / sqrt(2.0)
    h_a_two = np.kron(h_gate, np.eye(2))
    coherent_inverse = h_a_two @ cx @ bell
    coherent_probabilities_two = np.abs(coherent_inverse) ** 2
    dephased_bell = np.diag(np.abs(bell) ** 2)
    dephased_inverse = h_a_two @ cx @ dephased_bell @ cx.conj().T @ h_a_two.conj().T
    dephased_probabilities_two = np.real(np.diag(dephased_inverse))
    checks.append(record_max("q2_1_coherent_inverse_error", np.max(np.abs(coherent_probabilities_two - np.array([1.0, 0.0, 0.0, 0.0]))), tolerance))
    checks.append(record_max("q2_1_dephase_tv_gap_error", abs(total_variation(coherent_probabilities_two, dephased_probabilities_two) - 0.5), tolerance))

    # R181B/R181C and R177 for the same mechanism at three inputs.
    maximum_associativity_error = 0.0
    for _ in range(1_000):
        a = random_unit_vector(rng, 2)
        b = random_unit_vector(rng, 2)
        c = random_unit_vector(rng, 2)
        maximum_associativity_error = max(
            maximum_associativity_error,
            float(np.linalg.norm(np.kron(np.kron(a, b), c) - np.kron(a, np.kron(b, c)))),
        )
    checks.append(record_max("iterated_tensor_lift_associativity_error", maximum_associativity_error, tolerance))

    cx_ab = controlled_x(3, 0, 1)
    cx_bc = controlled_x(3, 1, 2)
    checks.append(record_max("ab_slice_cnot_error", np.linalg.norm(cx_ab - np.kron(cx, np.eye(2))), tolerance))
    checks.append(record_max("three_mode_gate_unitarity_error", max(np.linalg.norm(cx_ab.conj().T @ cx_ab - np.eye(8)), np.linalg.norm(cx_bc.conj().T @ cx_bc - np.eye(8))), 0.0))

    h_a = np.kron(np.kron(h_gate, np.eye(2)), np.eye(2))
    t_gate = np.diag([1.0, np.exp(1j * np.pi / 4.0)])
    t_a = np.kron(np.kron(t_gate, np.eye(2)), np.eye(2))
    state_000 = np.eye(8, dtype=complex)[:, 0]
    ghz = cx_bc @ cx_ab @ h_a @ state_000
    expected_ghz = (np.eye(8)[:, 0] + np.eye(8)[:, 7]) / sqrt(2.0)
    checks.append(record_max("two_gate_ghz_error", np.linalg.norm(ghz - expected_ghz), tolerance))

    coherent_final = h_a @ cx_ab @ cx_bc @ t_a @ ghz
    coherent_probabilities = np.abs(coherent_final) ** 2
    expected_coherent = np.zeros(8)
    expected_coherent[0] = np.cos(np.pi / 8.0) ** 2
    expected_coherent[4] = np.sin(np.pi / 8.0) ** 2
    checks.append(record_max("ghz_t_inverse_probability_error", np.max(np.abs(coherent_probabilities - expected_coherent)), tolerance))

    mixed_input = np.zeros((8, 8), dtype=complex)
    mixed_input[0, 0] = 0.5
    mixed_input[7, 7] = 0.5
    inverse_unitary = h_a @ cx_ab @ cx_bc @ t_a
    mixed_output = inverse_unitary @ mixed_input @ inverse_unitary.conj().T
    mixed_probabilities = np.real(np.diag(mixed_output))
    expected_mixed = np.zeros(8)
    expected_mixed[0] = 0.5
    expected_mixed[4] = 0.5
    checks.append(record_max("dephased_inverse_probability_error", np.max(np.abs(mixed_probabilities - expected_mixed)), tolerance))
    coherence_gap = total_variation(coherent_probabilities, mixed_probabilities)
    checks.append(record_max("coherence_tv_gap_formula_error", abs(coherence_gap - 1.0 / (2.0 * sqrt(2.0))), tolerance))
    checks.append(record_min("coherence_positive_margin", coherence_gap - 0.12, 0.2))

    # R181D: capacity latch, regularization, ray invariance, and no-response mass.
    v = random_unit_vector(rng, 4)
    radial = 2.7
    phase = np.exp(0.83j)
    born_probabilities = np.abs(v) ** 2
    transformed_born = np.abs(radial * phase * v) ** 2 / np.linalg.norm(radial * phase * v) ** 2
    checks.append(record_max("terminal_ray_invariance_error", np.max(np.abs(transformed_born - born_probabilities)), tolerance))

    q_reference = np.array([0.1, 0.2, 0.3, 0.4])
    delta = 0.017
    capacities = np.abs(v) ** 2 + delta * q_reference * np.linalg.norm(v) ** 2
    regularized = capacities / np.sum(capacities)
    expected_regularized = (born_probabilities + delta * q_reference) / (1.0 + delta)
    checks.append(record_max("capacity_latch_formula_error", np.max(np.abs(regularized - expected_regularized)), tolerance))
    regularization_tv = total_variation(regularized, born_probabilities)
    checks.append(record_max("r181d_regularization_tv_bound_excess", max(0.0, regularization_tv - delta / (1.0 + delta)), tolerance))

    no_response = 0.006
    complete_observed = np.concatenate(((1.0 - no_response) * born_probabilities, [no_response]))
    complete_ideal = np.concatenate((born_probabilities, [0.0]))
    checks.append(record_max("no_response_complete_space_formula_error", abs(total_variation(complete_observed, complete_ideal) - no_response), tolerance))

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
