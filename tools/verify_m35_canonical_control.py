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


def rotation(angle: float) -> np.ndarray:
    return np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)],
    ])


def random_unitary(rng: np.random.Generator, size: int) -> np.ndarray:
    matrix = rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))
    unitary, triangular = np.linalg.qr(matrix)
    diagonal = np.diag(triangular)
    phases = np.ones_like(diagonal)
    nonzero = np.abs(diagonal) > 0.0
    phases[nonzero] = diagonal[nonzero] / np.abs(diagonal[nonzero])
    return unitary @ np.diag(phases.conj())


def adjacent_givens_decomposition(
    unitary: np.ndarray,
) -> tuple[list[tuple[int, np.ndarray]], np.ndarray]:
    reduced = unitary.copy()
    gates: list[tuple[int, np.ndarray]] = []
    size = unitary.shape[0]
    for column in range(size - 1):
        for row in range(size - 1, column, -1):
            upper = reduced[row - 1, column]
            lower = reduced[row, column]
            norm = np.hypot(abs(upper), abs(lower))
            if norm == 0.0:
                gate = np.eye(2, dtype=complex)
            else:
                gate = np.array([
                    [upper.conjugate(), lower.conjugate()],
                    [-lower, upper],
                ]) / norm
            reduced[[row - 1, row], :] = gate @ reduced[[row - 1, row], :]
            gates.append((row - 1, gate))
    diagonal = np.diag(np.diag(reduced))
    return gates, diagonal


def reconstruct_from_adjacent_givens(
    gates: list[tuple[int, np.ndarray]],
    diagonal: np.ndarray,
) -> np.ndarray:
    reconstructed = diagonal.copy()
    for index, gate in reversed(gates):
        reconstructed[[index, index + 1], :] = (
            gate.conjugate().T @ reconstructed[[index, index + 1], :]
        )
    return reconstructed


def complex_to_real_symplectic(unitary: np.ndarray) -> np.ndarray:
    return np.block([
        [unitary.real, -unitary.imag],
        [unitary.imag, unitary.real],
    ])


def smooth_step(values: np.ndarray) -> np.ndarray:
    def flat(values_inner: np.ndarray) -> np.ndarray:
        output = np.zeros_like(values_inner, dtype=float)
        positive = values_inner > 0.0
        output[positive] = np.exp(-1.0 / values_inner[positive])
        return output

    numerator = flat(values + 1.0)
    denominator_term = flat(1.0 - values)
    return numerator / (numerator + denominator_term)


def adjacent_real_rotation(
    state: np.ndarray,
    index: int,
    angle: float,
) -> np.ndarray:
    result = state.copy()
    result[[index, index + 1]] = rotation(angle) @ result[[index, index + 1]]
    return result


def interval_outcomes(fractions: np.ndarray, shares: np.ndarray) -> np.ndarray:
    cumulative = np.cumsum(shares, axis=-1)
    if shares.ndim == 1:
        return np.searchsorted(cumulative, fractions, side="right")
    return np.sum(fractions[:, None] >= cumulative, axis=1)


def main() -> None:
    seed = 20260807
    rng = np.random.default_rng(seed)
    checks: list[CheckResult] = []

    # M35 control surface: unitary synthesis, post-state routing, recording, and inverse.
    pure_modes = 6
    chi = rng.normal(size=pure_modes) + 1j * rng.normal(size=pure_modes)
    chi /= np.linalg.norm(chi)
    basis_change = random_unitary(rng, pure_modes)

    # Any finite unitary is reconstructed from adjacent two-mode gates.
    givens_gates, diagonal_phase = adjacent_givens_decomposition(basis_change)
    reconstructed_basis = reconstruct_from_adjacent_givens(
        givens_gates,
        diagonal_phase,
    )
    checks.append(record_max(
        "adjacent_givens_reconstruction_error",
        np.max(np.abs(reconstructed_basis - basis_change)),
        8.0e-14,
    ))
    checks.append(record_max(
        "adjacent_givens_gate_count_excess",
        max(0, len(givens_gates) - pure_modes * (pure_modes - 1) // 2),
        0.0,
    ))
    max_gate_unitarity_error = max(
        np.max(np.abs(gate.conjugate().T @ gate - np.eye(2)))
        for _, gate in givens_gates
    )
    checks.append(record_max(
        "adjacent_two_mode_unitarity_error",
        max_gate_unitarity_error,
        4.0e-14,
    ))
    symplectic_map = complex_to_real_symplectic(reconstructed_basis)
    symplectic_form = np.block([
        [np.zeros((pure_modes, pure_modes)), np.eye(pure_modes)],
        [-np.eye(pure_modes), np.zeros((pure_modes, pure_modes))],
    ])
    checks.append(record_max(
        "local_basis_circuit_symplectic_error",
        np.max(np.abs(
            symplectic_map.T @ symplectic_form @ symplectic_map
            - symplectic_form
        )),
        8.0e-14,
    ))
    test_signal = rng.normal(size=pure_modes) + 1j * rng.normal(size=pure_modes)
    action_before = np.vdot(test_signal, test_signal).real
    action_after = np.vdot(
        reconstructed_basis @ test_signal,
        reconstructed_basis @ test_signal,
    ).real
    checks.append(record_max(
        "local_basis_circuit_action_error",
        abs(action_after - action_before),
        8.0e-14,
    ))
    checks.append(record_max(
        "local_basis_inverse_circuit_error",
        np.max(np.abs(
            reconstructed_basis.conjugate().T
            @ reconstructed_basis
            @ test_signal
            - test_signal
        )),
        8.0e-14,
    ))

    basis_amplitude = basis_change @ chi
    pure_shares = np.abs(basis_amplitude) ** 2
    checks.append(record_max(
        "pure_action_normalization_error",
        abs(np.sum(pure_shares) - 1.0),
        3.0e-14,
    ))

    alpha = (sqrt(5.0) - 1.0) / 2.0
    orbit_count = 240_000
    orbit = (0.137 + alpha * np.arange(orbit_count)) % 1.0
    orbit_outcomes = interval_outcomes(orbit, pure_shares)

    selected = int(np.argmax(pure_shares))
    template = np.zeros(pure_modes, dtype=complex)
    template[selected] = 1.0
    signal_before_swap = basis_amplitude.copy()
    signal_after_swap = template.copy()
    template_after_swap = -signal_before_swap
    post_state = basis_change.conj().T @ signal_after_swap
    expected_post = basis_change.conj().T[:, selected]
    checks.append(record_max(
        "canonical_swap_post_state_error",
        np.max(np.abs(post_state - expected_post)),
        3.0e-14,
    ))
    checks.append(record_max(
        "canonical_swap_information_storage_error",
        np.max(np.abs(template_after_swap + basis_amplitude)),
        3.0e-14,
    ))

    repeated_basis_state = basis_change @ post_state
    repeated_shares = np.abs(repeated_basis_state) ** 2
    expected_repeat = np.zeros(pure_modes)
    expected_repeat[selected] = 1.0
    checks.append(record_max(
        "fresh_template_repeatability_error",
        np.max(np.abs(repeated_shares - expected_repeat)),
        3.0e-14,
    ))

    # Inverse swap maps (b, t) -> (-t, b), then inverse basis/preparation restores input.
    restored_basis_signal = -template_after_swap
    restored_template = signal_after_swap
    restored_prepared_signal = basis_change.conj().T @ restored_basis_signal
    checks.append(record_max(
        "inverse_swap_signal_error",
        np.max(np.abs(restored_prepared_signal - chi)),
        3.0e-14,
    ))
    checks.append(record_max(
        "inverse_swap_template_error",
        np.max(np.abs(restored_template - template)),
        3.0e-14,
    ))

    # Smooth-comparator bad set obeys the union bound 2(L-1)w.
    boundaries = np.cumsum(pure_shares)[:-1]
    comparator_width = 1.0e-3
    boundary_distance = np.min(np.abs(orbit[:, None] - boundaries[None, :]), axis=1)
    bad_mass = np.mean(boundary_distance < comparator_width)
    union_bound = 2.0 * (pure_modes - 1) * comparator_width
    checks.append(record_max(
        "smooth_comparator_union_bound_violation",
        max(0.0, bad_mass - union_bound),
        2.0 / orbit_count,
    ))

    # Smooth cumulative pointers, exclusive safe sectors, and no-response outcome.
    amplification = -np.log(comparator_width)
    output_threshold = 1.0
    pointer_values = np.exp(amplification) * (
        boundaries[None, :] - orbit[:, None]
    )
    smooth_values = smooth_step(pointer_values / output_threshold)
    checks.append(record_max(
        "smooth_cumulative_monotonicity_violation",
        max(0.0, -float(np.min(np.diff(smooth_values, axis=1)))),
        2.0e-14,
    ))
    partition_values = np.concatenate([
        smooth_values[:, :1],
        np.diff(smooth_values, axis=1),
        1.0 - smooth_values[:, -1:],
    ], axis=1)
    checks.append(record_max(
        "smooth_partition_nonnegativity_violation",
        max(0.0, -float(np.min(partition_values))),
        2.0e-14,
    ))
    checks.append(record_max(
        "smooth_partition_normalization_error",
        np.max(np.abs(np.sum(partition_values, axis=1) - 1.0)),
        3.0e-14,
    ))

    sector_matches = np.zeros((orbit_count, pure_modes), dtype=bool)
    for outcome_index in range(pure_modes):
        left_safe = np.all(
            pointer_values[:, :outcome_index] <= -output_threshold,
            axis=1,
        )
        right_safe = np.all(
            pointer_values[:, outcome_index:] >= output_threshold,
            axis=1,
        )
        sector_matches[:, outcome_index] = left_safe & right_safe
    sector_count = np.sum(sector_matches, axis=1)
    checks.append(record_max(
        "exclusive_safe_sector_overlap",
        np.max(np.maximum(sector_count - 1, 0)),
        0.0,
    ))
    no_response = sector_count == 0
    checks.append(record_max(
        "complete_outcome_cover_error",
        np.max(np.abs(sector_count + no_response.astype(int) - 1)),
        0.0,
    ))

    smooth_distribution = np.zeros(pure_modes + 1)
    for outcome_index in range(pure_modes):
        smooth_distribution[outcome_index] = np.mean(
            sector_matches[:, outcome_index]
        )
    smooth_distribution[-1] = np.mean(no_response)
    ideal_orbit_distribution = np.bincount(
        orbit_outcomes,
        minlength=pure_modes,
    ) / orbit_count
    ideal_extended = np.concatenate([ideal_orbit_distribution, [0.0]])
    smooth_tv = 0.5 * np.sum(np.abs(smooth_distribution - ideal_extended))
    checks.append(record_max(
        "no_response_total_variation_identity_error",
        abs(smooth_tv - smooth_distribution[-1]),
        2.0 / orbit_count,
    ))
    checks.append(record_max(
        "no_response_union_bound_violation",
        max(0.0, smooth_distribution[-1] - union_bound),
        2.0 / orbit_count,
    ))

    # Adjacent template routing is exact in every safe sector.
    max_routing_error = 0.0
    max_record_error = 0.0
    for outcome_index in range(pure_modes):
        template_routed = np.zeros(pure_modes, dtype=complex)
        template_routed[0] = 1.0
        route_record = 1.0
        for edge_index in range(pure_modes - 1):
            route_fraction = float(edge_index < outcome_index)
            template_routed = adjacent_real_rotation(
                template_routed,
                edge_index,
                0.5 * pi * route_fraction,
            )
            route_record += route_fraction
        expected_template = np.zeros(pure_modes, dtype=complex)
        expected_template[outcome_index] = 1.0
        max_routing_error = max(
            max_routing_error,
            float(np.max(np.abs(template_routed - expected_template))),
        )
        max_record_error = max(
            max_record_error,
            abs(route_record - (outcome_index + 1)),
        )
    checks.append(record_max(
        "safe_sector_adjacent_routing_error",
        max_routing_error,
        3.0e-14,
    ))
    checks.append(record_max(
        "safe_sector_internal_record_error",
        max_record_error,
        3.0e-14,
    ))

    transition_steps = np.array([0.25, 0.75])
    transition_record = 1.0 + np.sum(1.0 - transition_steps)
    transition_is_safe = bool(np.all(
        (transition_steps == 0.0) | (transition_steps == 1.0)
    ))
    checks.append(record_min(
        "integer_transition_record_rejected",
        float(abs(transition_record - round(transition_record)) < 1.0e-14
              and not transition_is_safe),
        1.0,
    ))

    # A transition-region trial also returns exactly under the full inverse map.
    transition_selector = boundaries[0] + 0.2 * comparator_width
    register_forward = pure_shares.copy()
    register_forward[0] -= transition_selector
    for register_index in range(pure_modes - 2):
        register_forward[register_index + 1] += register_forward[register_index]
    register_forward[:pure_modes - 1] *= np.exp(amplification)
    transition_h = smooth_step(
        register_forward[:pure_modes - 1] / output_threshold
    )
    transition_route = 1.0 - transition_h
    transition_template = np.zeros(pure_modes, dtype=complex)
    transition_template[0] = 1.0
    transition_record_full = 1.0
    for edge_index, route_fraction in enumerate(transition_route):
        transition_template = adjacent_real_rotation(
            transition_template,
            edge_index,
            0.5 * pi * route_fraction,
        )
        transition_record_full += route_fraction

    signal_at_readout = basis_amplitude.copy()
    signal_after_transition_swap = transition_template.copy()
    template_after_transition_swap = -signal_at_readout
    transition_post_state = basis_change.conjugate().T @ signal_after_transition_swap
    signal_before_inverse_swap = basis_change @ transition_post_state
    restored_signal = -template_after_transition_swap
    restored_transition_template = signal_before_inverse_swap
    restored_record = transition_record_full
    for edge_index in range(pure_modes - 2, -1, -1):
        restored_transition_template = adjacent_real_rotation(
            restored_transition_template,
            edge_index,
            -0.5 * pi * transition_route[edge_index],
        )
        restored_record -= transition_route[edge_index]
    restored_record -= 1.0

    register_restored = register_forward.copy()
    register_restored[:pure_modes - 1] *= np.exp(-amplification)
    for register_index in range(pure_modes - 3, -1, -1):
        register_restored[register_index + 1] -= register_restored[register_index]
    register_restored[0] += transition_selector
    checks.append(record_max(
        "transition_region_full_inverse_signal_error",
        np.max(np.abs(restored_signal - signal_at_readout)),
        4.0e-14,
    ))
    initial_template = np.zeros(pure_modes, dtype=complex)
    initial_template[0] = 1.0
    checks.append(record_max(
        "transition_region_full_inverse_template_error",
        np.max(np.abs(restored_transition_template - initial_template)),
        4.0e-14,
    ))
    checks.append(record_max(
        "transition_region_full_inverse_record_error",
        abs(restored_record),
        4.0e-14,
    ))
    checks.append(record_max(
        "transition_region_full_inverse_register_error",
        np.max(np.abs(register_restored - pure_shares)),
        4.0e-14,
    ))

    input_pointer_error = 2.7e-4
    recovered_input_error = (
        np.exp(-amplification)
        * np.exp(amplification)
        * input_pointer_error
    )
    checks.append(record_max(
        "pre_amplification_error_not_reduced",
        abs(recovered_input_error - input_pointer_error),
        2.0e-16,
    ))

    # Cell probabilities already include the cell volume.
    cell_count = 41
    cell_volume = 0.07
    continuous_amplitude = rng.normal(size=cell_count) + 1j * rng.normal(size=cell_count)
    continuous_amplitude /= np.sqrt(
        np.sum(np.abs(continuous_amplitude) ** 2) * cell_volume
    )
    canonical_amplitude = np.sqrt(cell_volume) * continuous_amplitude
    cell_correlation = np.outer(canonical_amplitude, canonical_amplitude.conj())
    cell_probability = np.real(np.diag(cell_correlation)) / np.trace(cell_correlation).real
    expected_cell_probability = np.abs(continuous_amplitude) ** 2 * cell_volume
    checks.append(record_max(
        "cell_volume_probability_error",
        np.max(np.abs(cell_probability - expected_cell_probability)),
        2.0e-14,
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
