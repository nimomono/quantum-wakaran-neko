#!/usr/bin/env python3
"""Numerical regression checks for R123--R125 and Q3-3--Q3-5."""

from __future__ import annotations

from itertools import product

import numpy as np


TOL = 2.0e-11
checks = 0


def check(condition: bool, message: str) -> None:
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def unitary_from_hermitian(h: np.ndarray, time: float, action: float = 1.0) -> np.ndarray:
    values, vectors = np.linalg.eigh(h)
    return (vectors * np.exp(-1j * values * time / action)) @ vectors.conj().T


def sign_changes(vector: np.ndarray) -> int:
    real = np.real_if_close(vector).real
    signs = np.sign(real)
    signs = signs[signs != 0]
    return int(np.count_nonzero(signs[1:] * signs[:-1] < 0))


def square_well_checks() -> tuple[float, float]:
    length = 1.0
    errors: list[float] = []
    for sites in (80, 160):
        spacing = length / (sites + 1)
        diagonal = np.full(sites, 1.0 / spacing**2)
        off_diagonal = np.full(sites - 1, -0.5 / spacing**2)
        h = np.diag(diagonal) + np.diag(off_diagonal, 1) + np.diag(off_diagonal, -1)
        values, vectors = np.linalg.eigh(h)

        mode = np.arange(1, 5)
        exact_discrete = 2.0 / spacing**2 * np.sin(
            mode * np.pi / (2.0 * (sites + 1))
        ) ** 2
        exact_continuum = 0.5 * (mode * np.pi / length) ** 2
        check(np.max(np.abs(values[:4] - exact_discrete)) < 5.0e-10, "well eigenvalue formula")
        check(np.all(np.diff(values[:5]) > 0.0), "well low spectrum is nondegenerate")
        check([sign_changes(vectors[:, k]) for k in range(4)] == [0, 1, 2, 3], "well nodes")

        x = spacing * np.arange(1, sites + 1)
        exact_ground = np.sqrt(2.0 / (sites + 1)) * np.sin(np.pi * x / length)
        overlap = abs(np.vdot(exact_ground, vectors[:, 0]))
        check(abs(overlap - 1.0) < 2.0e-11, "well density eigenvector")
        errors.append(float(np.max(np.abs(values[:4] - exact_continuum))))

    ratio = errors[0] / errors[1]
    check(ratio > 3.8, "well second-order convergence")
    return errors[-1], ratio


def harmonic_checks() -> tuple[float, float]:
    half_width = 8.0
    errors: list[float] = []
    for sites in (240, 480):
        spacing = 2.0 * half_width / (sites + 1)
        x = -half_width + spacing * np.arange(1, sites + 1)
        diagonal = 1.0 / spacing**2 + 0.5 * x**2
        off_diagonal = np.full(sites - 1, -0.5 / spacing**2)
        h = np.diag(diagonal) + np.diag(off_diagonal, 1) + np.diag(off_diagonal, -1)
        values, vectors = np.linalg.eigh(h)
        exact = np.arange(4, dtype=float) + 0.5

        check(np.all(np.diff(values[:5]) > 0.0), "harmonic low spectrum is nondegenerate")
        check([sign_changes(vectors[:, k]) for k in range(4)] == [0, 1, 2, 3], "harmonic nodes")
        errors.append(float(np.max(np.abs(values[:4] - exact))))

    ratio = errors[0] / errors[1]
    check(ratio > 3.7, "harmonic second-order convergence")
    check(errors[-1] < 3.0e-3, "harmonic low eigenvalues")
    return errors[-1], ratio


def dephasing_checks() -> tuple[float, float]:
    action = 1.0
    coupling = 0.07
    bath_momentum = 1.3
    energies = np.array([0.4, 1.1, 2.0, 3.2])
    amplitudes = np.array([1.0, 0.7j, -0.4 + 0.2j, 0.3 - 0.1j], dtype=complex)
    amplitudes /= np.linalg.norm(amplitudes)
    correlation_zero = np.outer(amplitudes, amplitudes.conj())

    time_decoherence = np.pi * action / (2.0 * coupling * bath_momentum)
    time_recurrence = 2.0 * time_decoherence

    def reduced_correlation(time: float) -> np.ndarray:
        result = np.zeros_like(correlation_zero)
        for signs in product((-1.0, 1.0), repeat=len(energies)):
            momenta = bath_momentum * np.asarray(signs)
            phase = np.exp(-1j * (energies + coupling * momenta) * time / action)
            evolved = phase * amplitudes
            result += np.outer(evolved, evolved.conj())
        return result / 2 ** len(energies)

    decohered = reduced_correlation(time_decoherence)
    recurred = reduced_correlation(time_recurrence)
    diagonal = np.diag(correlation_zero)
    check(np.max(np.abs(np.diag(decohered) - diagonal)) < TOL, "dephasing populations at decay")
    check(np.max(np.abs(np.diag(recurred) - diagonal)) < TOL, "dephasing populations at recurrence")
    off_diagonal = decohered - np.diag(np.diag(decohered))
    check(np.max(np.abs(off_diagonal)) < TOL, "exact finite-time dephasing")

    system_phase = np.exp(-1j * energies * time_recurrence / action)
    expected_recurrence = (
        system_phase[:, None]
        * correlation_zero
        * system_phase.conj()[None, :]
    )
    check(np.max(np.abs(recurred - expected_recurrence)) < TOL, "coherence recurrence")

    probe_time = 0.37 * time_decoherence
    reduced = reduced_correlation(probe_time)
    system_phase = np.exp(-1j * energies * probe_time / action)
    factor = np.cos(coupling * bath_momentum * probe_time / action) ** 2
    expected = system_phase[:, None] * correlation_zero * system_phase.conj()[None, :]
    expected = np.diag(np.diag(expected)) + factor * (expected - np.diag(np.diag(expected)))
    check(np.max(np.abs(reduced - expected)) < TOL, "dephasing characteristic function")

    actions = action * np.abs(amplitudes) ** 2
    reduced_actions = action * np.real(np.diag(reduced))
    initial_energy = float(np.dot(energies, actions))
    reduced_energy = float(np.dot(energies, reduced_actions))
    check(abs(reduced_energy - initial_energy) < TOL, "system energy conserved")
    return time_decoherence, time_recurrence


def tunnelling_checks() -> tuple[float, float, float]:
    hopping = 1.0
    barrier = 8.0
    h = np.array(
        [[0.0, -hopping, 0.0], [-hopping, barrier, -hopping], [0.0, -hopping, 0.0]]
    )
    values, vectors = np.linalg.eigh(h)
    lower = 0.5 * (barrier - np.sqrt(barrier**2 + 8.0 * hopping**2))
    alpha = 1.0 / np.sqrt(1.0 + lower**2 / (2.0 * hopping**2))
    antisymmetric = np.array([1.0, 0.0, -1.0]) / np.sqrt(2.0)
    symmetric_low = np.array(
        [alpha / np.sqrt(2.0), -lower * alpha / (np.sqrt(2.0) * hopping), alpha / np.sqrt(2.0)]
    )
    initial = (antisymmetric + symmetric_low) / np.sqrt(2.0)
    time = np.pi / abs(lower)
    final = unitary_from_hermitian(h, time) @ initial

    check(abs(values[0] - lower) < TOL, "barrier lower eigenvalue")
    check(abs(values[1]) < TOL and values[2] > barrier, "barrier spectral ordering")
    high_projector = vectors[:, values >= barrier] @ vectors[:, values >= barrier].conj().T
    check(np.linalg.norm(high_projector @ initial) < TOL, "strictly sub-barrier support")
    initial_right = float(abs(initial[2]) ** 2)
    final_right = float(abs(final[2]) ** 2)
    increment = final_right - initial_right
    check(abs(increment - alpha) < TOL, "right probability increment")
    check(increment > 0.0, "positive tunnelling increment")
    check(abs(float(abs(initial[1]) ** 2) - lower**2 * alpha**2 / (4.0 * hopping**2)) < TOL, "barrier occupancy")

    readout_error = 0.1
    check(increment - 2.0 * readout_error > 0.0, "readout margin for tunnelling")
    return initial_right, increment, time


def interference_checks() -> tuple[float, float]:
    coupling = 1.0
    h = coupling * np.array([[0.0, 1.0], [1.0, 0.0]])
    time = np.pi / (4.0 * coupling)
    unitary = unitary_from_hermitian(h, time)
    expected_unitary = (np.eye(2) - 1j * np.array([[0.0, 1.0], [1.0, 0.0]])) / np.sqrt(2.0)
    check(np.max(np.abs(unitary - expected_unitary)) < TOL, "two-path recombiner")

    def distribution(phase: float) -> np.ndarray:
        state = np.array([1.0, np.exp(1j * phase)]) / np.sqrt(2.0)
        return np.abs(unitary @ state) ** 2

    mixed = 0.5 * np.abs(unitary[:, 0]) ** 2 + 0.5 * np.abs(unitary[:, 1]) ** 2
    plus = distribution(np.pi / 2.0)
    minus = distribution(-np.pi / 2.0)
    coherent_tv = 0.5 * float(np.sum(np.abs(plus - mixed)))
    phase_tv = 0.5 * float(np.sum(np.abs(plus - minus)))
    check(np.max(np.abs(mixed - np.array([0.5, 0.5]))) < TOL, "incoherent mixture")
    check(np.max(np.abs(plus - np.array([1.0, 0.0]))) < TOL, "positive-phase fringe")
    check(np.max(np.abs(minus - np.array([0.0, 1.0]))) < TOL, "negative-phase fringe")
    check(abs(coherent_tv - 0.5) < TOL, "coherent versus mixed distance")
    check(abs(phase_tv - 1.0) < TOL, "relative-phase distance")

    readout_error = 0.1
    check(coherent_tv - 2.0 * readout_error > 0.0, "readout margin for coherence")
    check(phase_tv - 2.0 * readout_error > 0.0, "readout margin for phase")
    return coherent_tv, phase_tv


def main() -> None:
    well_error, well_ratio = square_well_checks()
    harmonic_error, harmonic_ratio = harmonic_checks()
    decoherence_time, recurrence_time = dephasing_checks()
    initial_right, increment, tunnelling_time = tunnelling_checks()
    coherent_tv, phase_tv = interference_checks()

    print(f"checks={checks}")
    print(f"well_max_error={well_error:.6e} well_ratio={well_ratio:.6f}")
    print(f"harmonic_max_error={harmonic_error:.6e} harmonic_ratio={harmonic_ratio:.6f}")
    print(f"decoherence_time={decoherence_time:.6f} recurrence_time={recurrence_time:.6f}")
    print(
        f"initial_right={initial_right:.6e} tunnelling_increment={increment:.6f} "
        f"tunnelling_time={tunnelling_time:.6f}"
    )
    print(f"coherent_tv={coherent_tv:.6f} phase_tv={phase_tv:.6f}")


if __name__ == "__main__":
    main()
