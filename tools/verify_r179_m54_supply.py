#!/usr/bin/env python3
from __future__ import annotations

import json
from math import ceil, log, sqrt

import numpy as np


TOL = 3.0e-12


def total_variation(left: np.ndarray, right: np.ndarray) -> float:
    return 0.5 * float(np.sum(np.abs(left - right)))


def main() -> None:
    rng = np.random.default_rng(20260905)
    checks: dict[str, float] = {}

    # One fixed two-mode rotation implements every partial SWAP in the bank.
    rho = 0.63
    sigma = sqrt(1.0 - rho**2)
    rotation = np.array([[rho, sigma], [-sigma, rho]])
    checks["partial_swap_orthogonality_error"] = float(
        np.linalg.norm(rotation.T @ rotation - np.eye(2), 2)
    )
    checks["partial_swap_determinant_error"] = abs(
        float(np.linalg.det(rotation)) - 1.0
    )

    dimension = 64
    rounds = 31
    eta_cold = 2.0e-5
    active = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
    active *= 4.7 / np.linalg.norm(active)
    initial_norm = float(np.linalg.norm(active))
    maximum_full_action_error = 0.0
    spent: list[np.ndarray] = []
    for _ in range(rounds):
        cold = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
        cold *= eta_cold / np.linalg.norm(cold)
        before = float(np.linalg.norm(active) ** 2 + np.linalg.norm(cold) ** 2)
        next_active = rho * active + sigma * cold
        next_spent = -sigma * active + rho * cold
        after = float(
            np.linalg.norm(next_active) ** 2 + np.linalg.norm(next_spent) ** 2
        )
        maximum_full_action_error = max(
            maximum_full_action_error, abs(after - before)
        )
        active = next_active
        spent.append(next_spent)
    residual_bound = rho**rounds * initial_norm + eta_cold / (1.0 - rho)
    checks["bank_residual_bound_excess"] = max(
        0.0, float(np.linalg.norm(active)) - residual_bound
    )
    checks["spent_action_conservation_error"] = maximum_full_action_error
    checks["spent_history_retained"] = max(
        0.0, 1.0e-6 - float(sum(np.linalg.norm(item) for item in spent))
    )

    # The number of identical rounds is logarithmic in the requested blank width.
    target = 1.0e-9
    required_rounds = ceil(log(target / initial_norm) / log(rho))
    achieved = rho**required_rounds * initial_norm
    previous = rho ** (required_rounds - 1) * initial_norm
    checks["round_count_sufficiency"] = max(0.0, achieved - target)
    checks["round_count_minimality"] = max(0.0, target - previous)

    # A constant per-mode noise floor is not an aggregate-cold guarantee.
    small_dimension = 16
    large_dimension = 256
    per_mode_floor = 3.0e-4
    small_aggregate = per_mode_floor * sqrt(small_dimension)
    large_aggregate = per_mode_floor * sqrt(large_dimension)
    checks["independent_noise_sqrt_dimension_law"] = abs(
        large_aggregate / small_aggregate
        - sqrt(large_dimension / small_dimension)
    )
    checks["aggregate_noise_growth_detected"] = max(
        0.0, small_aggregate - large_aggregate
    )

    # Root loading and downstream deterministic routing do not increase TV error.
    root_blank = np.zeros(32, dtype=complex)
    source = 0.7 - 0.2j
    loaded = root_blank.copy()
    loaded[0] = source
    checks["root_mode_load_error"] = abs(loaded[0] - source)
    checks["nonroot_blank_error"] = float(np.linalg.norm(loaded[1:]))

    ideal = np.full(16, 1.0 / 16.0)
    bias = np.linspace(-1.0, 1.0, 16)
    actual = ideal + 1.0e-3 * bias
    actual /= np.sum(actual)
    input_tv = total_variation(actual, ideal)
    routing = np.array([index.bit_count() % 3 for index in range(16)])
    output_ideal = np.array([
        np.sum(ideal[routing == value]) for value in range(3)
    ])
    output_actual = np.array([
        np.sum(actual[routing == value]) for value in range(3)
    ])
    output_tv = total_variation(output_actual, output_ideal)
    checks["supply_error_data_processing_excess"] = max(
        0.0, output_tv - input_tv
    )

    failures = {name: value for name, value in checks.items() if value > TOL}
    print(json.dumps({
        "seed": 20260905,
        "check_count": len(checks),
        "bank_residual": float(np.linalg.norm(active)),
        "bank_residual_bound": residual_bound,
        "required_rounds": required_rounds,
        "small_aggregate_noise": small_aggregate,
        "large_aggregate_noise": large_aggregate,
        "input_tv": input_tv,
        "output_tv": output_tv,
        "checks": checks,
        "passed": not failures,
    }, indent=2))
    if failures:
        raise SystemExit(f"failed checks: {failures}")


if __name__ == "__main__":
    main()
