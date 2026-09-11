#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from math import exp

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


def exact_y(y0: float, q0: float, gain: float, damping: float, tau: float) -> float:
    if abs(gain - damping) < 1.0e-14:
        return (
            1.0
            + (y0 - 1.0) * exp(-2.0 * gain * tau)
            + 2.0 * gain * q0 * tau * exp(-2.0 * gain * tau)
        )
    return (
        1.0
        + (y0 - 1.0) * exp(-2.0 * gain * tau)
        + gain * q0 / (gain - damping)
        * (exp(-2.0 * damping * tau) - exp(-2.0 * gain * tau))
    )


def exact_state(
    a0: complex,
    p0: np.ndarray,
    gain: float,
    damping: float,
    tau: float,
) -> tuple[complex, np.ndarray]:
    q0 = float(np.vdot(p0, p0).real / abs(a0) ** 2)
    y = exact_y(1.0 / abs(a0) ** 2, q0, gain, damping, tau)
    amplitude = a0 / abs(a0) / np.sqrt(y)
    transverse = amplitude * (p0 / a0) * exp(-damping * tau)
    return amplitude, transverse


def vector_field(
    state: np.ndarray,
    target: np.ndarray,
    gain: float,
    damping: float,
) -> np.ndarray:
    projector = np.outer(target, target.conj())
    return (
        gain * (1.0 - np.vdot(state, state).real) * state
        - damping * (np.eye(2) - projector) @ state
    )


def distance_to_target_circle(state: np.ndarray, target: np.ndarray) -> float:
    overlap = np.vdot(target, state)
    phase = 1.0 if abs(overlap) == 0.0 else overlap / abs(overlap)
    return float(np.linalg.norm(state - phase * target))


def main() -> None:
    seed = 20260826
    rng = np.random.default_rng(seed)
    checks: list[CheckResult] = []

    target = rng.normal(size=2) + 1j * rng.normal(size=2)
    target /= np.linalg.norm(target)
    projector = np.outer(target, target.conj())
    state0 = rng.normal(size=2) + 1j * rng.normal(size=2)
    amplitude0 = np.vdot(target, state0)
    transverse0 = (np.eye(2) - projector) @ state0
    reconstructed = amplitude0 * target + transverse0
    checks.append(record_max(
        "orthogonal_decomposition_reconstruction_error",
        np.linalg.norm(reconstructed - state0),
        3.0e-14,
    ))
    checks.append(record_max(
        "orthogonal_component_overlap_error",
        abs(np.vdot(target, transverse0)),
        3.0e-14,
    ))

    for label, gain, damping in (
        ("distinct_rates", 0.73, 1.19),
        ("equal_rates", 0.91, 0.91),
        ("slow_transverse", 1.27, 0.42),
    ):
        a0 = 0.61 * np.exp(0.37j)
        orthogonal = np.array([-target[1].conj(), target[0].conj()])
        p0 = 0.48 * np.exp(-0.29j) * orthogonal
        q0 = float(np.vdot(p0, p0).real / abs(a0) ** 2)
        y0 = 1.0 / abs(a0) ** 2
        initial_y_error = abs(exact_y(y0, q0, gain, damping, 0.0) - y0)
        checks.append(record_max(f"{label}_initial_y_error", initial_y_error, 2.0e-14))

        ratio_errors: list[float] = []
        differential_errors: list[float] = []
        scaled_distances: list[float] = []
        convergence_rate = min(2.0 * gain, damping)
        for tau in np.linspace(0.0, 12.0, 121):
            amplitude, transverse = exact_state(a0, p0, gain, damping, float(tau))
            state = amplitude * target + transverse
            ratio = np.linalg.norm(transverse) / abs(amplitude)
            expected_ratio = np.linalg.norm(p0) / abs(a0) * exp(-damping * tau)
            ratio_errors.append(abs(ratio - expected_ratio))

            step = 1.0e-6
            amplitude_plus, transverse_plus = exact_state(
                a0, p0, gain, damping, float(tau + step)
            )
            amplitude_minus, transverse_minus = exact_state(
                a0, p0, gain, damping, float(max(0.0, tau - step))
            )
            state_plus = amplitude_plus * target + transverse_plus
            state_minus = amplitude_minus * target + transverse_minus
            if tau == 0.0:
                derivative = (state_plus - state) / step
            else:
                derivative = (state_plus - state_minus) / (2.0 * step)
            differential_errors.append(np.linalg.norm(
                derivative - vector_field(state, target, gain, damping)
            ))
            scaled_distances.append(
                distance_to_target_circle(state, target) * exp(convergence_rate * tau)
            )

        checks.append(record_max(
            f"{label}_transverse_ratio_formula_error",
            max(ratio_errors),
            2.0e-13,
        ))
        checks.append(record_max(
            f"{label}_exact_solution_differential_error",
            max(differential_errors),
            1.5e-6,
        ))
        checks.append(record_max(
            f"{label}_finite_rate_scaled_distance",
            max(scaled_distances),
            12.0,
        ))
        final_amplitude, final_transverse = exact_state(a0, p0, gain, damping, 40.0)
        final_state = final_amplitude * target + final_transverse
        checks.append(record_max(
            f"{label}_target_circle_convergence_error",
            distance_to_target_circle(final_state, target),
            3.0e-7,
        ))

    phase = np.exp(1.23j)
    a_phase, p_phase = exact_state(
        phase * amplitude0,
        phase * transverse0,
        0.8,
        1.1,
        2.3,
    )
    a_plain, p_plain = exact_state(amplitude0, transverse0, 0.8, 1.1, 2.3)
    checks.append(record_max(
        "common_phase_equivariance_error",
        np.linalg.norm(a_phase * target + p_phase - phase * (a_plain * target + p_plain)),
        3.0e-14,
    ))

    orthogonal_seed = np.array([-target[1].conj(), target[0].conj()])
    seed_field = vector_field(orthogonal_seed, target, 0.6, 1.4)
    checks.append(record_max(
        "zero_target_seed_invariant_subspace_error",
        abs(np.vdot(target, seed_field)),
        3.0e-14,
    ))
    checks.append(record_min(
        "nonzero_seed_requirement",
        abs(amplitude0),
        1.0e-6,
    ))

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
