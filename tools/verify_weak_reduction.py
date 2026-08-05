#!/usr/bin/env python3
from __future__ import annotations

import json

import numpy as np


SEED = 20260806
TOLERANCE = 2.0e-12


def hermitian_matrix(rng: np.random.Generator, size: int) -> np.ndarray:
    raw = rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))
    return 0.5 * (raw + raw.conj().T)


def energy_norm(vector: np.ndarray, metric: np.ndarray) -> float:
    value = np.vdot(vector, metric @ vector).real
    return float(np.sqrt(max(value, 0.0)))


def hminus_norm(vector: np.ndarray, inverse_metric: np.ndarray) -> float:
    value = np.vdot(vector, inverse_metric @ vector).real
    return float(np.sqrt(max(value, 0.0)))


def make_check(name: str, value: float, tolerance: float = TOLERANCE) -> dict:
    return {
        "name": name,
        "value": float(value),
        "tolerance": float(tolerance),
        "passed": bool(value <= tolerance),
    }


def main() -> None:
    rng = np.random.default_rng(SEED)
    size = 7
    hbar = 1.7
    time = 0.63

    hamiltonian = hermitian_matrix(rng, size)
    hamiltonian += 2.5 * np.eye(size)
    metric = np.eye(size) + hamiltonian @ hamiltonian

    values, vectors = np.linalg.eigh(hamiltonian)
    propagator = (
        vectors * np.exp(-1j * values * time / hbar)
    ) @ vectors.conj().T
    inverse_hamiltonian = np.linalg.inv(hamiltonian)

    u0 = rng.normal(size=size) + 1j * rng.normal(size=size)
    v0 = rng.normal(size=size) + 1j * rng.normal(size=size)
    residual_u = 0.03 * (
        rng.normal(size=size) + 1j * rng.normal(size=size)
    )
    residual_v = 0.03 * (
        rng.normal(size=size) + 1j * rng.normal(size=size)
    )

    response = inverse_hamiltonian @ (propagator - np.eye(size))
    u_t = propagator @ u0 + response @ residual_u
    v_t = propagator @ v0 + response @ residual_v
    initial_difference = u0 - v0
    residual_difference = residual_u - residual_v
    stability_bound = (
        energy_norm(initial_difference, metric)
        + time * energy_norm(residual_difference, metric) / hbar
    )
    stability_violation = max(
        energy_norm(u_t - v_t, metric) - stability_bound,
        0.0,
    )

    phase = 1.13
    perturbation = 1.0e-3 * (
        rng.normal(size=size) + 1j * rng.normal(size=size)
    )
    reference = rng.normal(size=size) + 1j * rng.normal(size=size)
    sample = np.exp(1j * phase) * reference + perturbation
    estimated_phase = np.angle(np.vdot(reference, sample))
    aligned = np.exp(-1j * estimated_phase) * sample
    projective_alignment_violation = max(
        energy_norm(aligned - reference, metric)
        - energy_norm(sample - reference, metric),
        0.0,
    )

    intensity_left = np.sum(
        np.abs(np.abs(u_t) ** 2 - np.abs(v_t) ** 2)
    )
    intensity_right = (
        np.linalg.norm(u_t) + np.linalg.norm(v_t)
    ) * np.linalg.norm(u_t - v_t)
    intensity_violation = max(intensity_left - intensity_right, 0.0)

    gradient = rng.normal(size=(size, size))
    current_u = np.imag(np.conj(u_t) * (gradient @ u_t))
    current_v = np.imag(np.conj(v_t) * (gradient @ v_t))
    current_left = np.sum(np.abs(current_u - current_v))
    current_right = (
        np.linalg.norm(u_t - v_t) * np.linalg.norm(gradient @ u_t)
        + np.linalg.norm(v_t) * np.linalg.norm(gradient @ (u_t - v_t))
    )
    current_violation = max(current_left - current_right, 0.0)

    flux_size = 5
    divergence = rng.normal(size=(size, flux_size))
    hminus_metric = np.eye(size) + divergence @ divergence.T
    inverse_hminus_metric = np.linalg.inv(hminus_metric)
    density_initial = rng.normal(size=size)
    integrated_flux = rng.normal(size=flux_size)
    integrated_source = 0.1 * rng.normal(size=size)
    density_final = (
        density_initial
        - divergence @ integrated_flux
        + integrated_source
    )
    density_bound = (
        hminus_norm(density_initial, inverse_hminus_metric)
        + np.linalg.norm(integrated_flux)
        + hminus_norm(integrated_source, inverse_hminus_metric)
    )
    density_violation = max(
        hminus_norm(density_final, inverse_hminus_metric) - density_bound,
        0.0,
    )

    angle = 0.73
    outcomes = np.array(
        [
            1.0 - np.cos(angle),
            1.0 + np.cos(angle),
            1.0 + np.cos(angle),
            1.0 - np.cos(angle),
        ]
    ) / 4.0
    scale = 2.3
    raw_perturbation = 0.015 * rng.normal(size=4)
    weights = np.maximum(scale * outcomes + raw_perturbation, 1.0e-9)
    epsilon = np.sum(np.abs(weights - scale * outcomes)) / scale
    distribution = weights / np.sum(weights)
    total_variation = 0.5 * np.sum(np.abs(distribution - outcomes))
    total_variation_bound = epsilon / (1.0 - epsilon)
    total_variation_violation = max(
        total_variation - total_variation_bound,
        0.0,
    )

    checks = [
        make_check("energy_duhamel_bound_violation", stability_violation),
        make_check(
            "projective_phase_alignment_violation",
            projective_alignment_violation,
        ),
        make_check("intensity_product_bound_violation", intensity_violation),
        make_check("current_product_bound_violation", current_violation),
        make_check("weak_density_bound_violation", density_violation),
        make_check(
            "bell_total_variation_bound_violation",
            total_variation_violation,
        ),
    ]
    result = {
        "seed": SEED,
        "all_passed": all(check["passed"] for check in checks),
        "checks": checks,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    if not result["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
