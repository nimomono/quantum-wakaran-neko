#!/usr/bin/env python3
"""Numerical regression checks for M44 and the idealized parts of R126."""

from __future__ import annotations

import numpy as np


TOL = 2.0e-10
checks = 0


def check(condition: bool, message: str) -> None:
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def symmetric_exponential(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    return (vectors * np.exp(values)) @ vectors.T


def dirichlet_grid(sites: int, half_width: float) -> tuple[np.ndarray, float, np.ndarray]:
    spacing = 2.0 * half_width / (sites + 1)
    x = -half_width + spacing * np.arange(1, sites + 1)
    laplacian = (
        np.diag(np.full(sites, -2.0))
        + np.diag(np.ones(sites - 1), 1)
        + np.diag(np.ones(sites - 1), -1)
    ) / spacing**2
    return x, spacing, laplacian


def normalized_positive(vector: np.ndarray) -> np.ndarray:
    result = np.real_if_close(vector).real
    if np.sum(result) < 0.0:
        result = -result
    return result / np.linalg.norm(result)


def capture_entropy_checks() -> tuple[float, float]:
    mass = 1.3
    diffusivity = 0.42
    step = 0.08
    potential = np.linspace(0.0, 3.0, 31)
    target_log = -step * potential / (4.0 * mass * diffusivity)
    errors: list[float] = []

    for modes in (8, 32, 128):
        capacity = 4.0 * mass * diffusivity * modes / step
        factor = (1.0 - potential / capacity) ** modes
        error = float(np.max(np.abs(np.log(factor) - target_log)))
        errors.append(error)
        check(np.all((factor > 0.0) & (factor <= 1.0)), "finite-R capture factor range")

    check(errors[0] > errors[1] > errors[2], "finite-R capture convergence")
    check(errors[0] / errors[1] > 3.8, "capture error has inverse-R scaling")
    check(errors[1] / errors[2] > 3.8, "capture error scaling persists")

    modes = 64
    capacity = 4.0 * mass * diffusivity * modes / step
    exact_log = modes * np.log1p(-potential / capacity)
    second_order = target_log - step**2 * potential**2 / (
        32.0 * mass**2 * diffusivity**2 * modes
    )
    remainder = float(np.max(np.abs(exact_log - second_order)))
    check(remainder < 1.2e-7, "capture logarithm second-order expansion")
    return errors[-1], remainder


def ready_operator_checks() -> tuple[float, float, float, float]:
    mass = 0.9
    diffusivity = 0.36
    frequency = 0.8
    sites = 151
    x, spacing, laplacian = dirichlet_grid(sites, 5.5)
    potential = 0.5 * mass * frequency**2 * x**2
    hamiltonian = -2.0 * mass * diffusivity**2 * laplacian + np.diag(potential)
    energy, states = np.linalg.eigh(hamiltonian)
    ground = normalized_positive(states[:, 0])

    eigenvector_errors: list[float] = []
    operators: list[tuple[float, np.ndarray, float, np.ndarray, np.ndarray]] = []
    for step in (0.08, 0.04, 0.02):
        free_kernel = symmetric_exponential(step * diffusivity * laplacian)
        factor = np.exp(-step * potential / (4.0 * mass * diffusivity))
        ready = factor[:, None] * free_kernel * factor[None, :]
        values, vectors = np.linalg.eigh(ready)
        principal = normalized_positive(vectors[:, -1])
        overlap = abs(float(np.dot(principal, ground)))
        eigenvector_errors.append(np.sqrt(max(0.0, 2.0 - 2.0 * overlap)))
        operators.append((step, ready, float(values[-1]), principal, free_kernel))

        generator = (np.eye(sites) - ready) / step
        expected = hamiltonian / (2.0 * mass * diffusivity)
        probe = ground
        residual = np.linalg.norm((generator - expected) @ probe)
        check(residual < 0.12 * step + 2.0e-3, "ready generator converges on ground state")

    check(
        eigenvector_errors[0] > eigenvector_errors[1] > eigenvector_errors[2],
        "ready principal eigenvector converges",
    )
    check(eigenvector_errors[-1] < 2.0e-4, "ready eigenvector matches ground state")

    step, ready, principal_value, principal, free_kernel = operators[-1]
    doob = ready * principal[None, :] / (principal_value * principal[:, None])
    row_error = float(np.max(np.abs(np.sum(doob, axis=1) - 1.0)))
    check(row_error < 2.0e-8, "Doob kernel row sums")

    density = principal**2
    density /= np.sum(density)
    stationarity_error = float(np.max(np.abs(density @ doob - density)))
    check(stationarity_error < 2.0e-11, "Doob invariant density")
    detailed_balance_error = float(
        np.max(np.abs(density[:, None] * doob - density[None, :] * doob.T))
    )
    check(detailed_balance_error < 2.0e-12, "Doob detailed balance")

    indices = (64, 67, 70, 73)
    direct = 1.0
    reference = 1.0
    factor = np.exp(-step * potential / (4.0 * mass * diffusivity))
    for left, right in zip(indices[:-1], indices[1:]):
        direct *= ready[left, right]
        reference *= factor[left] * free_kernel[left, right] * factor[right]
    check(abs(direct - reference) < TOL * max(1.0, abs(direct)), "path endpoint factorization")

    left = np.ones(sites)
    right = np.linspace(0.8, 1.2, sites)
    for _ in range(1000):
        left = ready @ left
        right = ready @ right
        left /= np.linalg.norm(left)
        right /= np.linalg.norm(right)
    occupation = left * right
    occupation /= np.sum(occupation)
    formation_retention_error = float(np.max(np.abs(occupation - density)))
    check(formation_retention_error < 2.0e-8, "formation-retention product gives h squared")

    predicted_eigenvalue = np.exp(
        -step * (energy[0] - np.min(potential)) / (2.0 * mass * diffusivity)
    )
    semigroup_error = abs(principal_value - predicted_eigenvalue)
    check(semigroup_error < 3.0e-6, "Strang ready eigenvalue")
    return eigenvector_errors[-1], row_error, detailed_balance_error, formation_retention_error


def nelson_checks() -> tuple[float, float, float]:
    mass = 1.1
    diffusivity = 0.37
    frequency = 0.74
    half_width = 7.0
    sites = 1601
    x = np.linspace(-half_width, half_width, sites)
    spacing = x[1] - x[0]
    phi = np.exp(-frequency * x**2 / (4.0 * diffusivity))
    phi /= np.sqrt(np.trapezoid(phi**2, x))
    density = phi**2
    u = 2.0 * diffusivity * np.gradient(np.log(phi), spacing, edge_order=2)
    du = np.gradient(u, spacing, edge_order=2)
    ddu = np.gradient(du, spacing, edge_order=2)
    acceleration = -u * du - diffusivity * ddu
    force_acceleration = -frequency**2 * x
    interior = np.abs(x) < 3.0
    newton_error = float(np.max(np.abs(acceleration[interior] - force_acceleration[interior])))
    check(newton_error < 2.0e-8, "Nelson acceleration equals harmonic Newton force")

    sqrt_density_second = np.gradient(
        np.gradient(phi, spacing, edge_order=2), spacing, edge_order=2
    )
    quantum_potential = -2.0 * mass * diffusivity**2 * sqrt_density_second / phi
    potential = 0.5 * mass * frequency**2 * x**2
    expected_energy = mass * diffusivity * frequency
    eigen_error = float(
        np.max(np.abs((quantum_potential + potential)[interior] - expected_energy))
    )
    check(eigen_error < 3.0e-4, "quantum potential stationary identity")

    derivative = np.gradient(phi, spacing, edge_order=2)
    fisher_energy = 2.0 * mass * diffusivity**2 * np.trapezoid(derivative**2, x)
    potential_energy = np.trapezoid(potential * density, x)
    variational_energy = float(fisher_energy + potential_energy)
    energy_error = abs(variational_energy - expected_energy)
    check(energy_error < 1.0e-5, "Fisher variational ground energy")

    b_plus = u
    b_minus = -u
    check(np.max(np.abs(0.5 * (b_plus + b_minus))) < TOL, "stationary current velocity")
    check(
        np.max(
            np.abs(
                0.5 * (b_plus - b_minus)
                - diffusivity * np.gradient(np.log(density), spacing, edge_order=2)
            )
        )
        < 2.0e-10,
        "osmotic velocity identity",
    )
    return newton_error, eigen_error, energy_error


def main() -> None:
    capture_error, capture_remainder = capture_entropy_checks()
    eigenvector_error, row_error, balance_error, branch_error = ready_operator_checks()
    newton_error, eigen_error, energy_error = nelson_checks()

    print(f"checks={checks}")
    print(
        f"capture_error_R128={capture_error:.6e} "
        f"capture_third_order_remainder={capture_remainder:.6e}"
    )
    print(
        f"ready_eigenvector_error={eigenvector_error:.6e} "
        f"doob_row_error={row_error:.6e} detailed_balance_error={balance_error:.6e} "
        f"formation_retention_error={branch_error:.6e}"
    )
    print(
        f"nelson_newton_error={newton_error:.6e} "
        f"stationary_eigen_error={eigen_error:.6e} "
        f"fisher_energy_error={energy_error:.6e}"
    )


if __name__ == "__main__":
    main()
