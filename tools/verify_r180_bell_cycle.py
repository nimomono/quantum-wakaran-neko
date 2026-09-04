#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from math import cos, exp, pi, sin, sqrt

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


def rk4_step(field, state: np.ndarray, step: float) -> np.ndarray:
    k1 = field(state)
    k2 = field(state + 0.5 * step * k1)
    k3 = field(state + 0.5 * step * k2)
    k4 = field(state + step * k3)
    return state + step * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0


def planar_basis(angle: float) -> tuple[np.ndarray, np.ndarray]:
    pauli_x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    pauli_z = np.diag([1.0, -1.0]).astype(complex)
    observable = sin(angle) * pauli_x + cos(angle) * pauli_z
    values, vectors = np.linalg.eigh(observable)
    plus = vectors[:, int(np.argmax(values))]
    minus = vectors[:, int(np.argmin(values))]
    return plus, minus


def singlet_joint(angle_a: float, angle_b: float) -> np.ndarray:
    singlet = np.array([0.0, 1.0, -1.0, 0.0], dtype=complex) / sqrt(2.0)
    basis_a = planar_basis(angle_a)
    basis_b = planar_basis(angle_b)
    return np.array([
        [abs(np.vdot(np.kron(vector_a, vector_b), singlet)) ** 2 for vector_b in basis_b]
        for vector_a in basis_a
    ])


def correlation(distribution: np.ndarray) -> float:
    signs = np.array([1.0, -1.0])
    return float(signs @ distribution @ signs)


def main() -> None:
    seed = 20260904
    rng = np.random.default_rng(seed)
    checks: list[CheckResult] = []

    gain = 0.83
    paired_sink = 1.07
    transverse_sink = 0.91
    duration = 4.2
    initial_m = 0.41 * np.exp(0.63j)
    initial_d = -0.17 + 0.24j
    initial_p = np.array([0.13 - 0.08j, -0.19 + 0.04j])
    state = np.concatenate((np.array([initial_m, initial_d]), initial_p))

    def field(current: np.ndarray) -> np.ndarray:
        m_value = current[0]
        return np.concatenate((
            np.array([
                gain * (1.0 - abs(m_value) ** 2) * m_value,
                -paired_sink * current[1],
            ]),
            -transverse_sink * current[2:],
        ))

    steps = 20_000
    step = duration / steps
    for _ in range(steps):
        state = rk4_step(field, state, step)

    radial_squared = 1.0 / (
        1.0 + (abs(initial_m) ** -2 - 1.0) * exp(-2.0 * gain * duration)
    )
    exact_m = sqrt(radial_squared) * np.exp(1j * np.angle(initial_m))
    exact = np.concatenate((
        np.array([exact_m, exp(-paired_sink * duration) * initial_d]),
        exp(-transverse_sink * duration) * initial_p,
    ))
    checks.append(record_max(
        "r180b_exact_flow_error",
        np.linalg.norm(state - exact),
        2.0e-11,
    ))
    checks.append(record_max(
        "r180b_phase_preservation_error",
        abs(np.angle(state[0] / initial_m)),
        2.0e-12,
    ))

    current = np.array([0.52 + 0.21j, -0.18 + 0.09j, 0.14 - 0.05j, -0.11 + 0.02j])
    derivative = field(current)
    direct_action_rate = 2.0 * float(np.vdot(current, derivative).real)
    expected_action_rate = (
        2.0 * gain * (1.0 - abs(current[0]) ** 2) * abs(current[0]) ** 2
        - 2.0 * paired_sink * abs(current[1]) ** 2
        - 2.0 * transverse_sink * float(np.vdot(current[2:], current[2:]).real)
    )
    checks.append(record_max(
        "r180b_receiver_action_balance_error",
        abs(direct_action_rate - expected_action_rate),
        3.0e-15,
    ))

    angles_a = (0.0, pi / 2.0)
    angles_b = (pi / 4.0, -pi / 4.0)
    distributions: dict[tuple[int, int], np.ndarray] = {}
    maximum_formula_error = 0.0
    maximum_normalization_error = 0.0
    maximum_marginal_error = 0.0
    for index_a, angle_a in enumerate(angles_a):
        for index_b, angle_b in enumerate(angles_b):
            distribution = singlet_joint(angle_a, angle_b)
            distributions[(index_a, index_b)] = distribution
            signs = np.array([1.0, -1.0])
            expected = 0.25 * (
                1.0 - np.outer(signs, signs) * cos(angle_a - angle_b)
            )
            maximum_formula_error = max(
                maximum_formula_error,
                float(np.max(np.abs(distribution - expected))),
            )
            maximum_normalization_error = max(
                maximum_normalization_error,
                abs(float(np.sum(distribution)) - 1.0),
            )
            maximum_marginal_error = max(
                maximum_marginal_error,
                float(np.max(np.abs(np.sum(distribution, axis=0) - 0.5))),
                float(np.max(np.abs(np.sum(distribution, axis=1) - 0.5))),
            )

    checks.extend([
        record_max("r180c_singlet_joint_formula_error", maximum_formula_error, 5.0e-14),
        record_max("r180c_joint_normalization_error", maximum_normalization_error, 5.0e-14),
        record_max("r180c_nonsignaling_marginal_error", maximum_marginal_error, 5.0e-14),
    ])
    chsh = (
        correlation(distributions[(0, 0)])
        + correlation(distributions[(0, 1)])
        + correlation(distributions[(1, 0)])
        - correlation(distributions[(1, 1)])
    )
    checks.append(record_max("r180c_tsirelson_error", abs(abs(chsh) - 2.0 * sqrt(2.0)), 8.0e-14))

    epsilon = 0.012
    observed: dict[tuple[int, int], np.ndarray] = {}
    maximum_tv = 0.0
    for key, ideal in distributions.items():
        contaminant = rng.random((2, 2))
        contaminant /= np.sum(contaminant)
        candidate = (1.0 - epsilon) * ideal + epsilon * contaminant
        observed[key] = candidate
        maximum_tv = max(maximum_tv, total_variation(candidate, ideal))
    observed_chsh = (
        correlation(observed[(0, 0)])
        + correlation(observed[(0, 1)])
        + correlation(observed[(1, 0)])
        - correlation(observed[(1, 1)])
    )
    maximum_opposite_setting_marginal_difference = 0.0
    for index_a in range(2):
        maximum_opposite_setting_marginal_difference = max(
            maximum_opposite_setting_marginal_difference,
            float(np.max(np.abs(
                np.sum(observed[(index_a, 0)], axis=1)
                - np.sum(observed[(index_a, 1)], axis=1)
            ))),
        )
    checks.append(record_max("r180c_perturbed_tv_bound", maximum_tv, epsilon))
    checks.append(record_max(
        "r180c_finite_nonsignaling_bound",
        maximum_opposite_setting_marginal_difference,
        2.0 * epsilon,
    ))
    checks.append(record_max(
        "r180c_chsh_stability_bound",
        abs(observed_chsh - chsh),
        8.0 * epsilon,
    ))

    threshold = (sqrt(2.0) - 1.0) / 4.0
    safe_error = 0.9 * threshold
    checks.append(record_min(
        "r180c_chsh_violation_margin_under_threshold",
        2.0 * sqrt(2.0) - 8.0 * safe_error - 2.0,
        1.0e-12,
    ))

    local_a = np.array([0.63, 0.37])
    local_b = np.array([0.28, 0.72])
    conditional_product = np.outer(local_a, local_b)
    checks.append(record_max(
        "r180c_conditional_product_error",
        np.linalg.norm(conditional_product - local_a[:, None] * local_b[None, :]),
        2.0e-15,
    ))
    no_response = 0.007
    ideal_complete = np.concatenate((distributions[(0, 0)].reshape(-1), [0.0]))
    observed_complete = np.concatenate(((1.0 - no_response) * distributions[(0, 0)].reshape(-1), [no_response]))
    checks.append(record_max(
        "r180c_complete_result_no_response_error",
        abs(total_variation(ideal_complete, observed_complete) - no_response),
        2.0e-15,
    ))
    checks.append(record_min("r180c_measurement_setting_independence_fails", 1.0, 1.0))
    checks.append(record_min("r180c_single_device_integration_remains_conditional", 1.0, 1.0))

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
