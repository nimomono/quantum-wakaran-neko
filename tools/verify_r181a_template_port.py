#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass

import numpy as np


TOL = 5.0e-11


@dataclass(frozen=True)
class Check:
    name: str
    value: float
    tolerance: float = TOL


def normalized(vector: np.ndarray) -> np.ndarray:
    return vector / np.linalg.norm(vector)


def covariance(samples: np.ndarray) -> np.ndarray:
    numerator = np.einsum("ni,nj->ij", samples, samples.conj())
    denominator = float(np.sum(np.abs(samples) ** 2))
    return numerator / denominator


def trace_distance(left: np.ndarray, right: np.ndarray) -> float:
    eigenvalues = np.linalg.eigvalsh(left - right)
    return 0.5 * float(np.sum(np.abs(eigenvalues)))


def pure_distance(vector: np.ndarray, ray: np.ndarray) -> float:
    overlap = abs(np.vdot(ray, vector)) ** 2 / float(np.vdot(vector, vector).real)
    return float(np.sqrt(max(0.0, 1.0 - overlap)))


def unitary_from_hermitian(generator: np.ndarray, time: float, action: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(generator)
    phases = np.exp(-1j * values * time / action)
    return (vectors * phases) @ vectors.conj().T


def exact_preparation(
    samples: np.ndarray,
    ray: np.ndarray,
    pump: float,
    sink: float,
    tau: float,
) -> np.ndarray:
    amplitudes = samples @ ray.conj()
    parallel = amplitudes[:, None] * ray[None, :]
    transverse = samples - parallel
    transverse_ratio = np.sum(np.abs(transverse) ** 2, axis=1) / np.abs(amplitudes) ** 2
    inverse_radius = 1.0 / np.abs(amplitudes) ** 2
    if abs(pump - sink) > 1.0e-14:
        inverse_radius_t = (
            1.0
            + (inverse_radius - 1.0) * np.exp(-2.0 * pump * tau)
            + pump
            * transverse_ratio
            / (pump - sink)
            * (np.exp(-2.0 * sink * tau) - np.exp(-2.0 * pump * tau))
        )
    else:
        inverse_radius_t = (
            1.0
            + (inverse_radius - 1.0) * np.exp(-2.0 * pump * tau)
            + 2.0 * pump * transverse_ratio * tau * np.exp(-2.0 * pump * tau)
        )
    amplitudes_t = np.exp(1j * np.angle(amplitudes)) / np.sqrt(inverse_radius_t)
    transverse_t = (
        amplitudes_t[:, None]
        * (transverse / amplitudes[:, None])
        * np.exp(-sink * tau)
    )
    return amplitudes_t[:, None] * ray[None, :] + transverse_t


def m50_distribution(samples: np.ndarray, delta: float, reference: np.ndarray) -> np.ndarray:
    action = np.sum(np.abs(samples) ** 2, axis=1)
    weights = np.abs(samples) ** 2 / action[:, None]
    return (weights + delta * reference[None, :]) / (1.0 + delta)


def main() -> None:
    rng = np.random.default_rng(20260830)
    dimension = 4
    action = 1.7
    pump = 0.8
    sink = 1.3
    tau = 3.2

    ray = normalized(rng.normal(size=dimension) + 1j * rng.normal(size=dimension))
    projector = np.outer(ray, ray.conj())

    real_symmetric = rng.normal(size=(dimension, dimension))
    real_symmetric = 0.5 * (real_symmetric + real_symmetric.T)
    real_antisymmetric = rng.normal(size=(dimension, dimension))
    real_antisymmetric = 0.5 * (real_antisymmetric - real_antisymmetric.T)
    generator = real_symmetric + 1j * real_antisymmetric

    q = rng.normal(size=dimension)
    p = rng.normal(size=dimension)
    z = (q + 1j * p) / np.sqrt(2.0 * action)
    dq = (real_symmetric @ p + real_antisymmetric @ q) / action
    dp = (-real_symmetric @ q + real_antisymmetric @ p) / action
    dz_real = (dq + 1j * dp) / np.sqrt(2.0 * action)
    dz_complex = -1j * generator @ z / action

    count = 256
    phases = rng.uniform(-np.pi, np.pi, size=count)
    magnitudes = rng.uniform(0.35, 1.25, size=count)
    amplitudes = magnitudes * np.exp(1j * phases)
    raw = rng.normal(size=(count, dimension)) + 1j * rng.normal(size=(count, dimension))
    transverse = raw - (raw @ ray.conj())[:, None] * ray[None, :]
    transverse = transverse / np.linalg.norm(transverse, axis=1)[:, None]
    transverse_scale = rng.uniform(0.0, 0.65, size=count)
    samples_0 = amplitudes[:, None] * ray[None, :] + transverse_scale[:, None] * transverse
    samples_t = exact_preparation(samples_0, ray, pump, sink, tau)

    template_scale = 1.9
    physical_template = template_scale * ray
    kappa = sink / template_scale**2
    test_signal = samples_0[0]
    test_action = float(np.vdot(test_signal, test_signal).real)
    physical_template_drift = (
        pump * (1.0 - test_action) * test_signal
        - kappa
        * (
            np.vdot(physical_template, physical_template) * test_signal
            - physical_template * np.vdot(physical_template, test_signal)
        )
    )
    normalized_ray_drift = (
        pump * (1.0 - test_action) * test_signal
        - sink * (test_signal - ray * np.vdot(ray, test_signal))
    )

    radial_initial = 0.23
    radial_duration = 2.1
    radial_final = 1.0 / (
        1.0 + (1.0 / radial_initial - 1.0) * np.exp(-2.0 * pump * radial_duration)
    )
    radial_seed = np.sqrt(radial_initial) * ray
    radial_repumped = np.sqrt(radial_final / radial_initial) * radial_seed

    a0 = samples_0 @ ray.conj()
    p0 = samples_0 - a0[:, None] * ray[None, :]
    at = samples_t @ ray.conj()
    pt = samples_t - at[:, None] * ray[None, :]
    ratio_0 = np.linalg.norm(p0, axis=1) / np.abs(a0)
    ratio_t = np.linalg.norm(pt, axis=1) / np.abs(at)

    a_star = float(np.min(np.abs(a0)))
    radius_star = float(np.max(np.linalg.norm(samples_0, axis=1)))
    q_star = (radius_star**2 - a_star**2) / a_star**2
    ray_bound = np.sqrt(q_star) * np.exp(-sink * tau)
    sample_ray_distances = np.array([pure_distance(item, ray) for item in samples_t])

    covariance_t = covariance(samples_t)
    covariance_distance = trace_distance(covariance_t, projector)

    delta = 0.07
    reference = np.full(dimension, 1.0 / dimension)
    observed = np.mean(m50_distribution(samples_t, delta, reference), axis=0)
    target = (np.abs(ray) ** 2 + delta * reference) / (1.0 + delta)
    tv_distance = 0.5 * float(np.sum(np.abs(observed - target)))
    mean_ray_bound = float(np.mean(sample_ray_distances)) / (1.0 + delta)

    unitary = unitary_from_hermitian(generator, 0.43, action)
    propagated = samples_t @ unitary.T
    covariance_propagated = covariance(propagated)
    covariance_expected = unitary @ covariance_t @ unitary.conj().T

    real_generator = rng.normal(size=(dimension, dimension))
    real_generator = 0.5 * (real_generator + real_generator.T)
    real_unitary = unitary_from_hermitian(real_generator, 0.31, action)

    equal_rate_samples = exact_preparation(samples_0, ray, pump, pump, tau)
    equal_rate_a = equal_rate_samples @ ray.conj()
    equal_rate_p = equal_rate_samples - equal_rate_a[:, None] * ray[None, :]

    unsafe_mask = np.abs(a0) < 0.6
    safe_probability = 1.0 - float(np.mean(unsafe_mask))
    complete_distribution = np.zeros(dimension + 1)
    if np.any(~unsafe_mask):
        complete_distribution[:dimension] = safe_probability * np.mean(
            m50_distribution(samples_t[~unsafe_mask], delta, reference), axis=0
        )
    complete_distribution[-1] = 1.0 - safe_probability

    phase = np.exp(1j * 0.71)
    scale = 2.4

    checks = [
        Check("projector_hermitian", np.linalg.norm(projector - projector.conj().T)),
        Check("projector_idempotent", np.linalg.norm(projector @ projector - projector)),
        Check("projector_trace", abs(np.trace(projector) - 1.0)),
        Check("real_complex_drift_equivalence", np.linalg.norm(dz_real - dz_complex)),
        Check("hermitian_generator", np.linalg.norm(generator - generator.conj().T)),
        Check(
            "physical_nonnormalized_template_equivalence",
            np.linalg.norm(physical_template_drift - normalized_ray_drift),
        ),
        Check(
            "radial_only_repump_ray_preservation",
            pure_distance(radial_repumped, ray),
        ),
        Check(
            "radial_only_repump_action_formula",
            abs(float(np.vdot(radial_repumped, radial_repumped).real) - radial_final),
        ),
        Check("transverse_initial_orthogonality", np.max(np.abs(transverse @ ray.conj()))),
        Check("transverse_final_orthogonality", np.max(np.abs(pt @ ray.conj()))),
        Check(
            "exact_transverse_ratio",
            np.max(np.abs(ratio_t - ratio_0 * np.exp(-sink * tau))),
        ),
        Check("ray_bound", max(0.0, float(np.max(sample_ray_distances)) - ray_bound)),
        Check("covariance_hermitian", np.linalg.norm(covariance_t - covariance_t.conj().T)),
        Check("covariance_trace", abs(np.trace(covariance_t) - 1.0)),
        Check("covariance_positive", max(0.0, -float(np.min(np.linalg.eigvalsh(covariance_t))))),
        Check("covariance_ray_bound", max(0.0, covariance_distance - ray_bound)),
        Check("m50_probability_normalization", abs(float(np.sum(observed)) - 1.0)),
        Check("m50_ray_average_bound", max(0.0, tv_distance - mean_ray_bound)),
        Check(
            "global_phase_invariance",
            np.linalg.norm(
                m50_distribution(samples_t * phase, delta, reference)
                - m50_distribution(samples_t, delta, reference)
            ),
        ),
        Check(
            "radial_scale_invariance",
            np.linalg.norm(
                m50_distribution(samples_t * scale, delta, reference)
                - m50_distribution(samples_t, delta, reference)
            ),
        ),
        Check("unitary", np.linalg.norm(unitary.conj().T @ unitary - np.eye(dimension))),
        Check(
            "cut_covariance_transport",
            np.linalg.norm(covariance_propagated - covariance_expected),
        ),
        Check(
            "cut_action_conservation",
            np.max(
                np.abs(
                    np.sum(np.abs(propagated) ** 2, axis=1)
                    - np.sum(np.abs(samples_t) ** 2, axis=1)
                )
            ),
        ),
        Check("real_symmetric_special_unitary", np.linalg.norm(real_unitary.imag - real_unitary.imag.T)),
        Check(
            "equal_rate_ratio",
            np.max(
                np.abs(
                    np.linalg.norm(equal_rate_p, axis=1) / np.abs(equal_rate_a)
                    - ratio_0 * np.exp(-pump * tau)
                )
            ),
        ),
        Check("complete_result_normalization", abs(float(np.sum(complete_distribution)) - 1.0)),
        Check("no_response_mass", abs(complete_distribution[-1] - float(np.mean(unsafe_mask)))),
        Check("finite_positive_radii", max(0.0, -float(np.min(np.linalg.norm(samples_t, axis=1))))),
    ]

    failures = [item for item in checks if item.value > item.tolerance]
    for item in checks:
        status = "ok" if item.value <= item.tolerance else "FAIL"
        print(f"{status:4s} {item.name:36s} {item.value:.6e}")
    if failures:
        raise SystemExit(f"{len(failures)} checks failed")
    print(f"all {len(checks)} checks passed")


if __name__ == "__main__":
    main()
