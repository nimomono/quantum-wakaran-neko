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


def total_variation(first: np.ndarray, second: np.ndarray) -> float:
    return float(0.5 * np.sum(np.abs(first - second)))


def random_isometry(rng: np.random.Generator, rows: int, columns: int) -> np.ndarray:
    matrix = rng.normal(size=(rows, columns)) + 1j * rng.normal(size=(rows, columns))
    q_matrix, _ = np.linalg.qr(matrix)
    return q_matrix[:, :columns]


def main() -> None:
    seed = 20260902
    rng = np.random.default_rng(seed)
    checks: list[CheckResult] = []
    action_unit = 1.7

    maximum_action_error = 0.0
    maximum_phase_error = 0.0
    maximum_scale_error = 0.0
    for _ in range(2_000):
        isometry = random_isometry(rng, rows=7, columns=3)
        state = rng.normal(size=3) + 1j * rng.normal(size=3)
        signal_action = action_unit * float(np.vdot(state, state).real)
        branch_actions = action_unit * np.abs(isometry @ state) ** 2
        maximum_action_error = max(
            maximum_action_error,
            abs(float(np.sum(branch_actions)) - signal_action),
        )

        phase = np.exp(1j * rng.uniform(-pi, pi))
        phased_actions = action_unit * np.abs(isometry @ (phase * state)) ** 2
        maximum_phase_error = max(
            maximum_phase_error,
            float(np.max(np.abs(phased_actions - branch_actions))),
        )
        scale = 1.4 - 0.3j
        scaled_actions = action_unit * np.abs(isometry @ (scale * state)) ** 2
        maximum_scale_error = max(
            maximum_scale_error,
            float(np.max(np.abs(scaled_actions - abs(scale) ** 2 * branch_actions))),
        )

    checks.append(record_max(
        "m54_static_general_action_decomposition_error",
        maximum_action_error,
        7.0e-13,
    ))
    checks.append(record_max(
        "m54_static_common_phase_invariance_error",
        maximum_phase_error,
        7.0e-13,
    ))
    checks.append(record_max(
        "m54_static_scale_covariance_error",
        maximum_scale_error,
        2.0e-12,
    ))

    branch_actions = np.array([0.12, 0.18, 0.30, 0.40])
    reference = np.array([0.1, 0.2, 0.3, 0.4])
    delta = 0.031
    regularized = (branch_actions + delta * reference) / (1.0 + delta)
    checks.append(record_max(
        "m54_static_regularized_normalization_error",
        abs(float(np.sum(regularized)) - 1.0),
        2.0e-15,
    ))
    checks.append(record_max(
        "m54_static_regularization_tv_bound_excess",
        max(
            0.0,
            total_variation(regularized, branch_actions) - delta / (1.0 + delta),
        ),
        2.0e-15,
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
