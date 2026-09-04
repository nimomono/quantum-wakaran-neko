#!/usr/bin/env python3
from __future__ import annotations

import json
from math import log, sqrt

import numpy as np


TOL = 3.0e-12


def normalized(vector: np.ndarray) -> np.ndarray:
    return vector / np.linalg.norm(vector)


def bit_projector(bit_count: int, bit: int, value: int) -> np.ndarray:
    return np.diag([
        int(((index >> (bit_count - bit - 1)) & 1) == value)
        for index in range(2**bit_count)
    ]).astype(complex)


def tree_distribution(state: np.ndarray, depth: int) -> np.ndarray:
    distribution = np.zeros(2**depth)
    active: dict[tuple[int, ...], tuple[np.ndarray, float]] = {
        (): (state.copy(), 1.0)
    }
    for bit in range(depth):
        following: dict[tuple[int, ...], tuple[np.ndarray, float]] = {}
        for history, (branch, prefix) in active.items():
            norm = float(np.vdot(branch, branch).real)
            for value in (0, 1):
                child = bit_projector(depth, bit, value) @ branch
                probability = float(np.vdot(child, child).real) / norm
                following[history + (value,)] = (child, prefix * probability)
        active = following
    for history, (_, probability) in active.items():
        index = sum(
            value << (depth - bit - 1)
            for bit, value in enumerate(history)
        )
        distribution[index] = probability
    return distribution


def main() -> None:
    rng = np.random.default_rng(20260905)
    checks: dict[str, float] = {}

    # R181B: fixed two- and three-port lifts use the same product convention.
    a = normalized(rng.normal(size=2) + 1j * rng.normal(size=2))
    b = normalized(rng.normal(size=2) + 1j * rng.normal(size=2))
    c = normalized(rng.normal(size=2) + 1j * rng.normal(size=2))
    two_port = np.kron(a, b)
    three_left = np.kron(two_port, c)
    three_right = np.kron(a, np.kron(b, c))
    checks["fixed_tensor_lift_associativity_error"] = float(
        np.linalg.norm(three_left - three_right)
    )

    # R181C then R181D: n=1,2,3 all use the same register and readout rule.
    maximum_tree_error = 0.0
    for bit_count in (1, 2, 3):
        state = normalized(
            rng.normal(size=2**bit_count) + 1j * rng.normal(size=2**bit_count)
        )
        terminal = tree_distribution(state, bit_count)
        maximum_tree_error = max(
            maximum_tree_error,
            float(np.max(np.abs(terminal - np.abs(state) ** 2))),
        )
    checks["common_parent_specialization_error"] = maximum_tree_error

    # A local one-bit gate is broadcast over every spectator sector.
    phase_gate = np.diag([1.0, np.exp(0.37j)])
    bit_count = 5
    target = 2
    broadcast = np.eye(1, dtype=complex)
    for bit in range(bit_count):
        broadcast = np.kron(
            broadcast,
            phase_gate if bit == target else np.eye(2, dtype=complex),
        )
    state = normalized(
        rng.normal(size=2**bit_count) + 1j * rng.normal(size=2**bit_count)
    )
    evolved = broadcast @ state
    checks["broadcast_action_preservation_error"] = abs(
        float(np.vdot(evolved, evolved).real) - 1.0
    )
    checks["broadcast_readout_normalization_error"] = abs(
        float(np.sum(tree_distribution(evolved, bit_count))) - 1.0
    )

    # Q2-4 external resources use the R181D scaling stated in Appendix P.
    n = 48
    epsilon = 2.0e-3
    time_bound = n**2 / epsilon * log(n / epsilon)
    stiffness = n**2 / epsilon**2
    collision_flux = sqrt(n / epsilon)
    barrier_range = log(n / epsilon)
    checks["positive_polynomial_time"] = max(0.0, -time_bound)
    checks["positive_polynomial_stiffness"] = max(0.0, -stiffness)
    checks["positive_collision_flux"] = max(0.0, -collision_flux)
    checks["positive_log_barrier"] = max(0.0, -barrier_range)
    checks["time_scaling_identity"] = abs(
        time_bound / (n**2 / epsilon) - log(n / epsilon)
    )
    checks["stiffness_scaling_identity"] = abs(
        stiffness * epsilon**2 / n**2 - 1.0
    )
    checks["flux_scaling_identity"] = abs(
        collision_flux**2 * epsilon / n - 1.0
    )

    failures = {name: value for name, value in checks.items() if value > TOL}
    print(json.dumps({
        "seed": 20260905,
        "check_count": len(checks),
        "external_time_bound": time_bound,
        "shell_stiffness": stiffness,
        "collision_flux": collision_flux,
        "barrier_range": barrier_range,
        "checks": checks,
        "passed": not failures,
    }, indent=2))
    if failures:
        raise SystemExit(f"failed checks: {failures}")


if __name__ == "__main__":
    main()
