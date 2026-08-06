#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import asdict, dataclass

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


def random_unitary(rng: np.random.Generator, dimension: int) -> np.ndarray:
    raw = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(size=(dimension, dimension))
    unitary, triangular = np.linalg.qr(raw)
    phases = np.diag(triangular).copy()
    phases /= np.where(np.abs(phases) > 0.0, np.abs(phases), 1.0)
    return unitary @ np.diag(phases.conj())


def main() -> None:
    seed = 20260806
    rng = np.random.default_rng(seed)
    checks: list[CheckResult] = []
    dimension = 7
    action_scale = 1.3

    # Real canonical Hamilton equations equal i J0 bdot=h b.
    symmetric = rng.normal(size=(dimension, dimension))
    real_part = 0.5 * (symmetric + symmetric.T)
    skew = rng.normal(size=(dimension, dimension))
    imaginary_part = 0.5 * (skew - skew.T)
    hamiltonian_matrix = real_part + 1j * imaginary_part
    coordinate = rng.normal(size=dimension)
    momentum = rng.normal(size=dimension)
    amplitude = (coordinate + 1j * momentum) / np.sqrt(2.0 * action_scale)
    coordinate_dot = (real_part @ momentum + imaginary_part @ coordinate) / action_scale
    momentum_dot = (-real_part @ coordinate + imaginary_part @ momentum) / action_scale
    amplitude_dot_real = (coordinate_dot + 1j * momentum_dot) / np.sqrt(2.0 * action_scale)
    amplitude_dot_complex = -1j * (hamiltonian_matrix @ amplitude) / action_scale
    checks.append(record_max(
        "real_canonical_complex_equation_error",
        np.max(np.abs(amplitude_dot_real - amplitude_dot_complex)),
        3.0e-14,
    ))

    # The correlation derivative closes as a commutator.
    sample_count = 5000
    samples = rng.normal(size=(sample_count, dimension)) + 1j * rng.normal(size=(sample_count, dimension))
    sample_derivative = -1j * samples @ hamiltonian_matrix.T / action_scale
    correlation = samples.T @ samples.conj() / sample_count
    derivative_direct = (
        sample_derivative.T @ samples.conj()
        + samples.T @ sample_derivative.conj()
    ) / sample_count
    derivative_expected = -1j * (hamiltonian_matrix @ correlation - correlation @ hamiltonian_matrix) / action_scale
    checks.append(record_max(
        "correlation_commutator_derivative_error",
        np.max(np.abs(derivative_direct - derivative_expected)),
        8.0e-14,
    ))

    # Unitary conjugation preserves trace, eigenvalues, rank, and purity.
    unitary = random_unitary(rng, dimension)
    evolved = unitary @ correlation @ unitary.conj().T
    checks.append(record_max(
        "correlation_trace_preservation_error",
        abs(np.trace(evolved) - np.trace(correlation)),
        4.0e-13,
    ))
    checks.append(record_max(
        "correlation_eigenvalue_preservation_error",
        np.max(np.abs(np.linalg.eigvalsh(evolved) - np.linalg.eigvalsh(correlation))),
        4.0e-12,
    ))
    purity = np.trace(correlation @ correlation).real / np.trace(correlation).real**2
    evolved_purity = np.trace(evolved @ evolved).real / np.trace(evolved).real**2
    checks.append(record_max("correlation_purity_preservation_error", abs(evolved_purity - purity), 4.0e-14))

    # A common source gives rank one even when the first moment vanishes.
    source_direction = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
    source_direction /= np.linalg.norm(source_direction)
    phase_count = 200_000
    phases = rng.uniform(-np.pi, np.pi, size=phase_count)
    source_samples = np.exp(1j * phases)[:, None] * source_direction[None, :]
    source_mean = np.mean(source_samples, axis=0)
    source_correlation = source_samples.T @ source_samples.conj() / phase_count
    expected_source_correlation = np.outer(source_direction, source_direction.conj())
    checks.append(record_max(
        "common_source_rank_one_correlation_error",
        np.max(np.abs(source_correlation - expected_source_correlation)),
        3.0e-14,
    ))
    checks.append(record_max(
        "random_absolute_phase_first_moment",
        np.linalg.norm(source_mean),
        7.0e-3,
    ))
    source_eigenvalues = np.linalg.eigvalsh(source_correlation)
    checks.append(record_max(
        "common_source_nonprincipal_eigenvalue",
        np.max(np.abs(source_eigenvalues[:-1])),
        3.0e-14,
    ))

    # Rank-one factor propagation agrees with correlation propagation.
    factor_evolved = unitary @ source_direction
    correlation_evolved_direct = unitary @ expected_source_correlation @ unitary.conj().T
    correlation_evolved_factor = np.outer(factor_evolved, factor_evolved.conj())
    checks.append(record_max(
        "rank_one_factor_propagation_error",
        np.max(np.abs(correlation_evolved_direct - correlation_evolved_factor)),
        3.0e-14,
    ))

    # Two-path interference produces an exact node.
    splitter = np.array([[1.0, 1.0], [1.0, -1.0]], dtype=complex) / np.sqrt(2.0)
    input_path = np.array([1.0, 0.0], dtype=complex)
    arms = splitter @ input_path
    phase_shift = np.diag([1.0, -1.0])
    output = splitter @ phase_shift @ arms
    checks.append(record_max("two_path_dark_port_probability", abs(output[0]) ** 2, 2.0e-30))
    checks.append(record_max("two_path_probability_normalization_error", abs(np.sum(np.abs(output) ** 2) - 1.0), 2.0e-14))

    # A positive rank defect bounds the residual intensity at the ideal node.
    principal = arms
    orthogonal = np.array([principal[1].conj(), -principal[0].conj()])
    orthogonal /= np.linalg.norm(orthogonal)
    epsilon_rank = 0.073
    mixed_correlation = (
        (1.0 - epsilon_rank) * np.outer(principal, principal.conj())
        + epsilon_rank * np.outer(orthogonal, orthogonal.conj())
    )
    recombiner = splitter @ phase_shift
    output_correlation = recombiner @ mixed_correlation @ recombiner.conj().T
    residual_node = output_correlation[0, 0].real
    checks.append(record_max("rank_defect_node_bound_violation", max(0.0, residual_node - epsilon_rank), 2.0e-14))

    # A graph Laplacian Hamiltonian is Hermitian, local, and action preserving.
    graph_size = 11
    edge_weight = 0.7 + rng.random(graph_size - 1)
    laplacian = np.zeros((graph_size, graph_size))
    for index, weight in enumerate(edge_weight):
        laplacian[index, index] += weight
        laplacian[index + 1, index + 1] += weight
        laplacian[index, index + 1] -= weight
        laplacian[index + 1, index] -= weight
    potential = np.diag(rng.normal(size=graph_size))
    local_hamiltonian = 0.4 * laplacian + potential
    graph_amplitude = rng.normal(size=graph_size) + 1j * rng.normal(size=graph_size)
    graph_derivative = -1j * local_hamiltonian @ graph_amplitude / action_scale
    action_derivative = 2.0 * np.real(np.vdot(graph_amplitude, graph_derivative))
    checks.append(record_max("graph_hamiltonian_hermiticity_error", np.max(np.abs(local_hamiltonian - local_hamiltonian.T)), 2.0e-14))
    checks.append(record_max("graph_total_action_derivative", abs(action_derivative), 2.0e-14))
    nonlocal_mask = np.fromfunction(lambda i, j: np.abs(i - j) > 1, (graph_size, graph_size), dtype=int)
    checks.append(record_max("graph_nonlocal_coupling_error", np.max(np.abs(local_hamiltonian[nonlocal_mask])), 2.0e-14))

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
