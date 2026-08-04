#!/usr/bin/env python3
from __future__ import annotations

import json
import math

import numpy as np


SEED = 20260804
TOLERANCES = {
    "inertia_inverse": 2.0e-12,
    "chart_legendre": 2.0e-12,
    "band_count": 0.0,
    "slow_limit": 3.0e-3,
    "fast_limit": 3.0e-3,
    "projector_idempotence": 2.0e-8,
    "projector_invariance": 2.0e-8,
    "exchange_exact": 5.0e-14,
    "exchange_bound": 2.0e-14,
    "semidefinite_zero_mode": 2.0e-8,
    "semidefinite_fast": 2.0e-10,
    "normalization_scaling": 2.0e-14,
}


def tangent_basis(size: int) -> np.ndarray:
    raw = np.zeros((size, size - 1))
    for index in range(size - 1):
        raw[index, index] = 1.0
        raw[-1, index] = -1.0
    basis, _ = np.linalg.qr(raw)
    return basis[:, : size - 1]


def symmetric_sqrt(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    return (vectors * np.sqrt(values)) @ vectors.T


def hamiltonian_generator(
    eps: float,
    coupling: float,
    stiffness_x: np.ndarray,
    stiffness_y: np.ndarray,
) -> np.ndarray:
    size = stiffness_x.shape[0]
    identity = np.eye(size)
    hessian = np.zeros((4 * size, 4 * size))
    x = slice(0, size)
    y = slice(size, 2 * size)
    px = slice(2 * size, 3 * size)
    py = slice(3 * size, 4 * size)

    hessian[x, x] = stiffness_x + coupling**2 * identity / eps
    hessian[y, y] = stiffness_y
    hessian[px, px] = identity / eps
    hessian[py, py] = identity / eps
    hessian[x, py] = -coupling * identity / eps
    hessian[py, x] = -coupling * identity / eps

    symplectic = np.block(
        [
            [np.zeros((2 * size, 2 * size)), np.eye(2 * size)],
            [-np.eye(2 * size), np.zeros((2 * size, 2 * size))],
        ]
    )
    return symplectic @ hessian


def energy_norm(vector: np.ndarray, frequencies: np.ndarray) -> float:
    repeated = np.repeat(frequencies, 2)
    return float(np.sqrt(np.sum(repeated * vector**2)))


def main() -> None:
    rng = np.random.default_rng(SEED)
    results: dict[str, float] = {}

    cells = 6
    basis = tangent_basis(cells)
    q = rng.uniform(0.2, 1.4, size=cells)
    q /= q.sum()
    diagonal = np.diag(q)
    g_q = basis.T @ np.diag(1.0 / q) @ basis
    g_phi = basis.T @ (diagonal - np.outer(q, q)) @ basis
    results["inertia_inverse"] = float(
        np.linalg.norm(np.linalg.inv(g_q) - g_phi, ord=2)
    )

    eps = 0.037
    mass = 1.7
    inertia = 0.8
    action = -0.9
    xi_dot = rng.normal(size=cells - 1)
    phi_dot = rng.normal(size=cells - 1)
    p_xi = eps * mass * (g_q @ xi_dot) / 4.0
    p_phi = action * rng.normal(size=cells - 1)
    xi = p_phi / action - eps * inertia * (g_phi @ phi_dot) / action
    p_phi = action * xi + eps * inertia * (g_phi @ phi_dot)
    lagrangian_kinetic = (
        action * xi @ phi_dot
        + eps * mass * xi_dot @ g_q @ xi_dot / 8.0
        + eps * inertia * phi_dot @ g_phi @ phi_dot / 2.0
    )
    hamiltonian_kinetic = (
        2.0 * p_xi @ np.linalg.solve(g_q, p_xi) / (eps * mass)
        + (p_phi - action * xi)
        @ np.linalg.solve(g_phi, p_phi - action * xi)
        / (2.0 * eps * inertia)
    )
    results["chart_legendre"] = float(
        abs(p_xi @ xi_dot + p_phi @ phi_dot - lagrangian_kinetic - hamiltonian_kinetic)
    )

    modes = 3
    raw_a = rng.normal(size=(modes, modes))
    raw_b = rng.normal(size=(modes, modes))
    stiffness_x = raw_a.T @ raw_a + 0.7 * np.eye(modes)
    stiffness_y = raw_b.T @ raw_b + 0.6 * np.eye(modes)
    coupling = 1.3
    eps_spec = 1.0e-4
    generator = hamiltonian_generator(
        eps_spec, coupling, stiffness_x, stiffness_y
    )
    eigenvalues, eigenvectors = np.linalg.eig(generator)
    positive = np.sort(eigenvalues.imag[eigenvalues.imag > 1.0e-7])
    split = eps_spec ** -0.5
    low = positive[positive < split]
    fast = positive[positive > split]
    results["band_count"] = float(abs(low.size - modes) + abs(fast.size - modes))

    root_a = symmetric_sqrt(stiffness_x)
    limiting_squared = np.linalg.eigvalsh(
        root_a @ stiffness_y @ root_a / coupling**2
    )
    limiting_low = np.sqrt(np.sort(limiting_squared))
    results["slow_limit"] = float(
        np.max(np.abs(low - limiting_low) / limiting_low)
    )
    results["fast_limit"] = float(
        np.max(np.abs(eps_spec * fast - abs(coupling))) / abs(coupling)
    )

    selected = np.abs(eigenvalues.imag) > split
    inverse_vectors = np.linalg.inv(eigenvectors)
    projector = (
        eigenvectors
        @ np.diag(selected.astype(complex))
        @ inverse_vectors
    )
    results["projector_idempotence"] = float(
        np.linalg.norm(projector @ projector - projector, ord=2)
    )
    generator_scale = max(np.linalg.norm(generator, ord=2), 1.0)
    results["projector_invariance"] = float(
        np.linalg.norm(generator @ projector - projector @ generator, ord=2)
        / generator_scale
    )

    frequencies = fast
    target = rng.normal(size=2 * modes)
    auxiliary = np.zeros_like(target)
    angle = math.pi / 2.0
    target_out = math.cos(angle) * target - math.sin(angle) * auxiliary
    results["exchange_exact"] = energy_norm(target_out, frequencies)

    delta = 0.017
    auxiliary = 0.03 * rng.normal(size=2 * modes)
    target_out = (
        math.cos(math.pi / 2.0 + delta) * target
        - math.sin(math.pi / 2.0 + delta) * auxiliary
    )
    left = energy_norm(target_out, frequencies)
    right = (
        abs(math.cos(math.pi / 2.0 + delta))
        * energy_norm(target, frequencies)
        + abs(math.sin(math.pi / 2.0 + delta))
        * energy_norm(auxiliary, frequencies)
    )
    results["exchange_bound"] = float(max(left - right, 0.0))

    scalar_a = np.array([[2.4]])
    scalar_b = np.zeros((1, 1))
    eps_zero = 0.07
    scalar_generator = hamiltonian_generator(
        eps_zero, coupling, scalar_a, scalar_b
    )
    scalar_eigenvalues = np.linalg.eigvals(scalar_generator)
    ordered_abs = np.sort(np.abs(scalar_eigenvalues))
    results["semidefinite_zero_mode"] = float(ordered_abs[1])
    observed_fast = float(np.max(np.abs(scalar_eigenvalues.imag)))
    expected_fast = math.sqrt(
        coupling**2 + eps_zero * scalar_a[0, 0]
    ) / eps_zero
    results["semidefinite_fast"] = float(abs(observed_fast - expected_fast))

    eps_one = 4.0e-4
    eps_two = eps_one / 4.0
    lambda_norm = 3.2
    mass_norm = 1.1
    omega_one = math.sqrt(lambda_norm / (eps_one * mass_norm))
    omega_two = math.sqrt(lambda_norm / (eps_two * mass_norm))
    results["normalization_scaling"] = float(abs(omega_two / omega_one - 2.0))

    checks = {
        name: {
            "value": value,
            "tolerance": TOLERANCES[name],
            "passed": value <= TOLERANCES[name],
        }
        for name, value in results.items()
    }
    passed = all(item["passed"] for item in checks.values())
    print(
        json.dumps(
            {
                "seed": SEED,
                "checks": checks,
                "passed": passed,
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
