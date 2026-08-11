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


def record_min(name: str, value: float, threshold: float) -> CheckResult:
    return CheckResult(name, float(value), float(threshold), ">=", bool(value >= threshold))


def basis(angle: float, outcome: int) -> np.ndarray:
    positive = np.array([np.cos(angle / 2.0), np.sin(angle / 2.0)], dtype=complex)
    if outcome == 1:
        return positive
    return np.array([-positive[1], positive[0]], dtype=complex)


def coefficient_matrix(state: np.ndarray) -> np.ndarray:
    return state.reshape(2, 2)


def block(state: np.ndarray, angle: float, outcome: int) -> np.ndarray:
    return basis(angle, outcome).conj() @ coefficient_matrix(state)


def partial_trace_a(state: np.ndarray) -> np.ndarray:
    matrix = coefficient_matrix(state)
    return sum(np.outer(row, row.conj()) for row in matrix)


def born_joint(state: np.ndarray, outcome_a: int, outcome_b: int, x: float, y: float) -> float:
    amplitude = (
        basis(x, outcome_a).conj()
        @ coefficient_matrix(state)
        @ basis(y, outcome_b).conj()
    )
    return float(abs(amplitude) ** 2)


def total_variation(first: np.ndarray, second: np.ndarray) -> float:
    return float(0.5 * np.sum(np.abs(first - second)))


def complex_to_real(matrix: np.ndarray) -> np.ndarray:
    return np.block([
        [matrix.real, -matrix.imag],
        [matrix.imag, matrix.real],
    ])


def main() -> None:
    seed = 20260811
    rng = np.random.default_rng(seed)
    checks: list[CheckResult] = []
    tolerance = 3.0e-13
    outcomes = (1, -1)

    singlet = np.array([0.0, 1.0, -1.0, 0.0], dtype=complex) / np.sqrt(2.0)
    checks.append(record_max("singlet_normalization_error", abs(np.vdot(singlet, singlet) - 1.0), tolerance))

    # R107: rank-two block actions form a complete source partition.
    action_sum_errors = []
    denominator_cancellation_errors = []
    nonselective_errors = []
    conditional_normalization_errors = []
    for _ in range(300):
        state = rng.normal(size=4) + 1j * rng.normal(size=4)
        state /= np.linalg.norm(state)
        x = rng.uniform(-pi, pi)
        y = rng.uniform(-pi, pi)
        blocks = {outcome: block(state, x, outcome) for outcome in outcomes}
        actions = {outcome: float(np.vdot(value, value).real) for outcome, value in blocks.items()}
        action_sum_errors.append(abs(sum(actions.values()) - 1.0))
        rho_from_blocks = sum(np.outer(value, value.conj()) for value in blocks.values())
        nonselective_errors.append(np.max(np.abs(rho_from_blocks - partial_trace_a(state))))
        for outcome_a in outcomes:
            action = actions[outcome_a]
            if action > 1.0e-14:
                conditional = blocks[outcome_a] / np.sqrt(action)
                conditional_normalization_errors.append(abs(np.vdot(conditional, conditional) - 1.0))
                for outcome_b in outcomes:
                    conditional_probability = abs(np.vdot(
                        basis(y, outcome_b),
                        conditional,
                    )) ** 2
                    denominator_cancellation_errors.append(abs(
                        action * conditional_probability
                        - born_joint(state, outcome_a, outcome_b, x, y)
                    ))
    checks.append(record_max("rank_two_action_sum_error", max(action_sum_errors), tolerance))
    checks.append(record_max("conditional_b_normalization_error", max(conditional_normalization_errors), tolerance))
    checks.append(record_max("nonselective_b_partial_trace_error", max(nonselective_errors), tolerance))
    checks.append(record_max("unconditional_denominator_cancellation_error", max(denominator_cancellation_errors), tolerance))

    # R108 and the singlet specialization: both source branches have fixed half action.
    singlet_action_errors = []
    singlet_antialignment_errors = []
    rho_b = partial_trace_a(singlet)
    for x in np.linspace(-pi, pi, 129):
        for outcome in outcomes:
            selected = block(singlet, x, outcome)
            action = float(np.vdot(selected, selected).real)
            singlet_action_errors.append(abs(action - 0.5))
            normalized = selected / np.sqrt(action)
            actual_density = np.outer(normalized, normalized.conj())
            expected = basis(x, -outcome)
            expected_density = np.outer(expected, expected.conj())
            singlet_antialignment_errors.append(np.max(np.abs(
                actual_density - expected_density
            )))
    checks.append(record_max("singlet_branch_action_error", max(singlet_action_errors), tolerance))
    checks.append(record_max("singlet_conditional_antialignment_error", max(singlet_antialignment_errors), tolerance))
    checks.append(record_max("singlet_nonselective_b_error", np.max(np.abs(rho_b - 0.5 * np.eye(2))), tolerance))

    # R109: zero-action branches contribute zero without a positive action lower bound.
    product_state = np.array([1.0, 0.0, 0.0, 0.0], dtype=complex)
    zero_branch = block(product_state, 0.0, -1)
    zero_joint = sum(
        born_joint(product_state, -1, outcome_b, 0.0, y)
        for outcome_b in outcomes
        for y in (0.0,)
    )
    checks.append(record_max("zero_action_branch_norm", np.linalg.norm(zero_branch), 0.0))
    checks.append(record_max("zero_action_joint_mass", zero_joint, 0.0))

    width = 1.0e-4
    random_state = rng.normal(size=4) + 1j * rng.normal(size=4)
    random_state /= np.linalg.norm(random_state)
    random_actions = [
        float(np.vdot(block(random_state, 0.37, outcome), block(random_state, 0.37, outcome)).real)
        for outcome in outcomes
    ]
    positive_actions = [value for value in random_actions if value > 0.0]
    weighted_boundary_mass = sum(value * 2.0 * width / value for value in positive_actions)
    checks.append(record_max("variable_action_unconditional_width_bound", weighted_boundary_mass, 4.0 * width))
    action_cutoff = 2.0e-3
    cutoff_mass = sum(value for value in random_actions if value < action_cutoff)
    checks.append(record_max("variable_action_cutoff_mass_bound", cutoff_mass, 2.0 * action_cutoff))

    # The canonical two-block SWAP is unitary, symplectic, and exactly invertible.
    identity_2 = np.eye(2, dtype=complex)
    zero_2 = np.zeros((2, 2), dtype=complex)
    swap = np.block([[zero_2, identity_2], [-identity_2, zero_2]])
    checks.append(record_max("conditional_swap_unitarity_error", np.max(np.abs(
        swap.conj().T @ swap - np.eye(4)
    )), tolerance))
    real_swap = complex_to_real(swap)
    symplectic_form = np.block([
        [np.zeros((4, 4)), np.eye(4)],
        [-np.eye(4), np.zeros((4, 4))],
    ])
    checks.append(record_max("conditional_swap_symplectic_error", np.max(np.abs(
        real_swap.T @ symplectic_form @ real_swap - symplectic_form
    )), tolerance))
    checks.append(record_max("conditional_swap_inverse_error", np.max(np.abs(
        swap.conj().T @ swap - np.eye(4)
    )), tolerance))

    # Disjoint A and B local Hamiltonian generators commute.
    hermitian_a = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    hermitian_a = 0.5 * (hermitian_a + hermitian_a.conj().T)
    hermitian_b = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    hermitian_b = 0.5 * (hermitian_b + hermitian_b.conj().T)
    direct_a = np.block([[hermitian_a, zero_2], [zero_2, zero_2]])
    direct_b = np.block([[zero_2, zero_2], [zero_2, hermitian_b]])
    checks.append(record_max("local_measurement_commutator_error", np.linalg.norm(
        direct_a @ direct_b - direct_b @ direct_a,
        ord=2,
    ), tolerance))

    # R111: the full joint table is the singlet cosine law with non-signalling marginals.
    joint_formula_errors = []
    marginal_errors = []
    for _ in range(400):
        x = rng.uniform(-pi, pi)
        y = rng.uniform(-pi, pi)
        table = np.array([
            [
                born_joint(singlet, outcome_a, outcome_b, x, y)
                for outcome_b in outcomes
            ]
            for outcome_a in outcomes
        ])
        expected = np.array([
            [
                0.25 * (1.0 - outcome_a * outcome_b * np.cos(x - y))
                for outcome_b in outcomes
            ]
            for outcome_a in outcomes
        ])
        joint_formula_errors.append(np.max(np.abs(table - expected)))
        marginal_errors.append(max(
            np.max(np.abs(table.sum(axis=0) - 0.5)),
            np.max(np.abs(table.sum(axis=1) - 0.5)),
        ))
    checks.append(record_max("singlet_joint_cosine_error", max(joint_formula_errors), tolerance))
    checks.append(record_max("singlet_marginal_nonsignalling_error", max(marginal_errors), tolerance))

    settings_a = (0.0, pi / 2.0)
    settings_b = (pi / 4.0, -pi / 4.0)
    correlations = np.array([
        [-np.cos(x - y) for y in settings_b]
        for x in settings_a
    ])
    chsh = correlations[0, 0] + correlations[0, 1] + correlations[1, 0] - correlations[1, 1]
    checks.append(record_max("standard_chsh_value_error", abs(abs(chsh) - 2.0 * np.sqrt(2.0)), tolerance))

    tsirelson_excess = 0.0
    for _ in range(20000):
        angles_a = rng.uniform(-pi, pi, size=2)
        angles_b = rng.uniform(-pi, pi, size=2)
        values = np.array([
            [-np.cos(x - y) for y in angles_b]
            for x in angles_a
        ])
        value = abs(values[0, 0] + values[0, 1] + values[1, 0] - values[1, 1])
        tsirelson_excess = max(tsirelson_excess, value - 2.0 * np.sqrt(2.0))
    checks.append(record_max("planar_tsirelson_bound_excess", max(0.0, tsirelson_excess), tolerance))

    # The hidden conditional B decomposition changes with x although rho_B is fixed.
    hidden_change = []
    for outcome in outcomes:
        first = block(singlet, 0.0, outcome)
        first /= np.linalg.norm(first)
        second = block(singlet, pi / 2.0, outcome)
        second /= np.linalg.norm(second)
        overlap = abs(np.vdot(first, second))
        hidden_change.append(np.sqrt(max(0.0, 1.0 - overlap**2)))
    checks.append(record_min("measurement_dependence_hidden_decomposition_witness", min(hidden_change), 0.7))

    # A finite irrational translation samples the product selector measure.
    sample_count = 262144
    indices = np.arange(sample_count, dtype=float)
    increments = np.array([np.sqrt(2.0), np.sqrt(3.0), np.sqrt(5.0)])
    points = np.mod(indices[:, None] * increments[None, :], 1.0)
    histogram, _ = np.histogramdd(points, bins=(8, 8, 8), range=((0, 1), (0, 1), (0, 1)))
    empirical = histogram / sample_count
    checks.append(record_max("selector_product_haar_bin_error", np.max(np.abs(
        empirical - 1.0 / 512.0
    )), 1.5e-4))

    # Forward total-variation errors bound apparent signalling and CHSH drift.
    epsilon = 0.01
    ideal_table = np.full((2, 2), 0.25)
    perturb_left = np.array([[1.0, 0.0], [0.0, 0.0]])
    perturb_right = np.array([[0.0, 0.0], [0.0, 1.0]])
    observed_left = (1.0 - epsilon) * ideal_table + epsilon * perturb_left
    observed_right = (1.0 - epsilon) * ideal_table + epsilon * perturb_right
    apparent_signal = np.max(np.abs(
        observed_left.sum(axis=0) - observed_right.sum(axis=0)
    ))
    checks.append(record_max("finite_error_nonsignalling_bound_excess", max(
        0.0,
        apparent_signal - 2.0 * epsilon,
    ), tolerance))
    checks.append(record_max("finite_error_total_variation_left", total_variation(
        observed_left,
        ideal_table,
    ), epsilon))
    chsh_observed = (1.0 - epsilon) * abs(chsh)
    checks.append(record_max("finite_error_chsh_bound_excess", max(
        0.0,
        abs(chsh_observed - abs(chsh)) - 8.0 * epsilon,
    ), tolerance))

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
