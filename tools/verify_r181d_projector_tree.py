#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json

import numpy as np


TOL = 3.0e-12


def random_unitary(rng: np.random.Generator, size: int) -> np.ndarray:
    matrix = rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))
    unitary, triangular = np.linalg.qr(matrix)
    phases = np.diag(triangular)
    return unitary @ np.diag(np.conj(phases) / np.abs(phases))


def projector(bit_count: int, bit: int, value: int) -> np.ndarray:
    diagonal = [
        int(((index >> (bit_count - bit - 1)) & 1) == value)
        for index in range(2**bit_count)
    ]
    return np.diag(diagonal).astype(complex)


def normalized(vector: np.ndarray) -> np.ndarray:
    return vector / np.linalg.norm(vector)


def main() -> None:
    rng = np.random.default_rng(20260905)
    checks: dict[str, float] = {}

    # R181C: a shared local gate is a direct sum over spectator sectors.
    local = random_unitary(rng, 4)
    sectors = 8
    ideal = np.kron(np.eye(sectors), local)
    blocks: list[np.ndarray] = []
    block_errors: list[float] = []
    for _ in range(sectors):
        perturbation = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
        perturbation *= 1.0e-7 / np.linalg.norm(perturbation, 2)
        blocks.append(local + perturbation)
        block_errors.append(float(np.linalg.norm(perturbation, 2)))
    actual = np.zeros_like(ideal)
    for index, block in enumerate(blocks):
        actual[4 * index : 4 * (index + 1), 4 * index : 4 * (index + 1)] = block
    checks["sector_direct_sum_max_block_error"] = abs(
        float(np.linalg.norm(actual - ideal, 2)) - max(block_errors)
    )

    bit_count = 5
    state = normalized(
        rng.normal(size=2**bit_count) + 1j * rng.normal(size=2**bit_count)
    )
    p0 = projector(bit_count, 2, 0)
    p1 = projector(bit_count, 2, 1)

    # R181D filter: the rejected component remains in work and the map is involutive.
    filter_matrix = np.block([[p0, p1], [p1, -p0]])
    identity = np.eye(2 ** (bit_count + 1))
    routed = filter_matrix @ np.concatenate((state, np.zeros_like(state)))
    checks["filter_unitarity_error"] = float(
        np.linalg.norm(filter_matrix.conj().T @ filter_matrix - identity, 2)
    )
    checks["filter_involution_error"] = float(
        np.linalg.norm(filter_matrix @ filter_matrix - identity, 2)
    )
    checks["filter_selected_route_error"] = float(
        np.linalg.norm(routed[: 2**bit_count] - p0 @ state)
    )
    checks["filter_rejected_route_error"] = float(
        np.linalg.norm(routed[2**bit_count :] - p1 @ state)
    )


    # Rank-one Q1 specialization: selected signal is already the outcome eigenray.
    rank_one_state = normalized(np.array([0.61 + 0.29j, -0.37 + 0.64j]))
    q1_p0 = np.diag([1.0, 0.0]).astype(complex)
    q1_p1 = np.diag([0.0, 1.0]).astype(complex)
    rank_one_filter = np.block([[q1_p0, q1_p1], [q1_p1, -q1_p0]])
    maximum_rank_one_state_error = 0.0
    maximum_rank_one_scale_error = 0.0
    maximum_rank_one_work_error = 0.0
    for branch, selected_projector in enumerate((q1_p0, q1_p1)):
        rejected_projector = (q1_p1, q1_p0)[branch]
        if branch == 0:
            branch_filter = rank_one_filter
        else:
            branch_filter = np.block([[q1_p1, q1_p0], [q1_p0, -q1_p1]])
        routed_q1 = branch_filter @ np.concatenate(
            (rank_one_state, np.zeros_like(rank_one_state))
        )
        selected_q1 = routed_q1[:2]
        rejected_q1 = routed_q1[2:]
        post_covariance = np.outer(selected_q1, selected_q1.conj())
        post_covariance /= np.trace(post_covariance).real
        maximum_rank_one_state_error = max(
            maximum_rank_one_state_error,
            float(np.linalg.norm(post_covariance - selected_projector)),
        )
        maximum_rank_one_work_error = max(
            maximum_rank_one_work_error,
            float(np.linalg.norm(rejected_q1 - rejected_projector @ rank_one_state)),
        )

        transformed_q1 = 3.4 * np.exp(-0.71j) * rank_one_state
        transformed_route = branch_filter @ np.concatenate(
            (transformed_q1, np.zeros_like(transformed_q1))
        )
        transformed_selected = transformed_route[:2]
        transformed_covariance = np.outer(
            transformed_selected, transformed_selected.conj()
        )
        transformed_covariance /= np.trace(transformed_covariance).real
        maximum_rank_one_scale_error = max(
            maximum_rank_one_scale_error,
            float(np.linalg.norm(transformed_covariance - selected_projector)),
        )

    checks["rank_one_post_state_error"] = maximum_rank_one_state_error
    checks["rank_one_phase_radial_invariance_error"] = maximum_rank_one_scale_error
    checks["rank_one_rejected_work_error"] = maximum_rank_one_work_error

    # Conditional ensemble averaging keeps the same rank-one projector.
    samples = []
    for _ in range(2000):
        scale_q1 = 0.2 + 2.0 * rng.random()
        phase_q1 = np.exp(1j * rng.uniform(-np.pi, np.pi))
        sample = q1_p0 @ (scale_q1 * phase_q1 * rank_one_state)
        samples.append(np.outer(sample, sample.conj()))
    conditional_moment = np.mean(samples, axis=0)
    conditional_moment /= np.trace(conditional_moment).real
    checks["rank_one_conditional_moment_error"] = float(
        np.linalg.norm(conditional_moment - q1_p0)
    )

    # Raw capacities determine cutoff; regularized capacities only feed R164/R170.
    raw = np.array([
        float(np.vdot(p0 @ state, p0 @ state).real),
        float(np.vdot(p1 @ state, p1 @ state).real),
    ])
    raw_probability = raw / np.sum(raw)
    delta = 0.037
    reference = np.array([0.31, 0.69])
    regularized_capacity = raw + delta * reference * np.sum(raw)
    regularized_probability = regularized_capacity / np.sum(regularized_capacity)
    expected_regularized = (raw_probability + delta * reference) / (1.0 + delta)
    checks["regularized_capacity_formula_error"] = float(
        np.max(np.abs(regularized_probability - expected_regularized))
    )
    regularization_tv = 0.5 * float(
        np.sum(np.abs(regularized_probability - raw_probability))
    )
    checks["regularization_tv_bound_excess"] = max(
        0.0, regularization_tv - delta / (1.0 + delta)
    )
    scale = 4.7
    scaled_raw = scale**2 * raw
    checks["raw_cutoff_scale_invariance"] = float(
        np.max(np.abs(scaled_raw / np.sum(scaled_raw) - raw_probability))
    )

    # Sequential conditional kernels telescope to the complete Born distribution.
    born = np.abs(state) ** 2
    sequential = np.zeros_like(born)
    for outcome in itertools.product((0, 1), repeat=bit_count):
        branch = state.copy()
        probability = 1.0
        for bit, value in enumerate(outcome):
            child = projector(bit_count, bit, value) @ branch
            conditional = float(np.vdot(child, child).real / np.vdot(branch, branch).real)
            probability *= conditional
            branch = child
        index = sum(
            value << (bit_count - bit - 1)
            for bit, value in enumerate(outcome)
        )
        sequential[index] = probability
    checks["projector_tree_telescoping_error"] = float(
        np.max(np.abs(sequential - born))
    )

    tau = 0.045
    gamma = 0.006
    removed_mass = 0.0
    cutoff_state = np.array([1.0 + 0.0j])
    for probability_one in (0.02, 0.20, 0.50, 0.35, 0.65):
        cutoff_state = np.kron(
            cutoff_state,
            np.array([np.sqrt(1.0 - probability_one), np.sqrt(probability_one)]),
        )
    active = {(): (cutoff_state, 1.0)}
    for bit in range(bit_count):
        following: dict[tuple[int, ...], tuple[np.ndarray, float]] = {}
        for history, (branch, prefix_probability) in active.items():
            norm = float(np.vdot(branch, branch).real)
            for value in (0, 1):
                child = projector(bit_count, bit, value) @ branch
                conditional = float(np.vdot(child, child).real) / norm
                if conditional < tau + gamma:
                    removed_mass += prefix_probability * conditional
                else:
                    following[history + (value,)] = (
                        child,
                        prefix_probability * conditional,
                    )
        active = following
    checks["raw_cutoff_mass_bound_excess"] = max(
        0.0, removed_mass - 2.0 * bit_count * (tau + gamma)
    )
    checks["raw_cutoff_nontrivial_mass"] = max(0.0, 0.01 - removed_mass)

    # Accepted-branch normalization obeys the stated filter perturbation bound.
    accepted = p0 @ state if raw_probability[0] >= tau else p1 @ state
    eta_filter = 0.01
    perturbation = normalized(
        rng.normal(size=accepted.size) + 1j * rng.normal(size=accepted.size)
    )
    perturbation *= eta_filter * np.linalg.norm(state)
    implemented = accepted + perturbation
    ray_error = float(
        np.linalg.norm(normalized(implemented) - normalized(accepted))
    )
    ray_bound = 2.0 * eta_filter / (np.sqrt(tau) - eta_filter)
    checks["filter_ray_bound_excess"] = max(0.0, ray_error - ray_bound)

    # Radial-only repump changes the norm but preserves the selected ray.
    target_action = 1.8
    initial_action = float(np.vdot(accepted, accepted).real)
    gain = 0.73
    duration = 4.2
    final_action = target_action / (
        1.0
        + (target_action / initial_action - 1.0)
        * np.exp(-2.0 * gain * target_action * duration)
    )
    repumped = accepted * np.sqrt(final_action / initial_action)
    checks["radial_repump_ray_error"] = float(
        np.linalg.norm(normalized(repumped) - normalized(accepted))
    )
    checks["radial_repump_target_excess"] = max(
        0.0, abs(final_action - target_action) - abs(initial_action - target_action)
    )

    # One explicit complete-result budget remains below epsilon without postselection.
    epsilon = 1.0e-3
    depth = 40
    epsilon_in = epsilon / 16.0
    budget_delta = epsilon / (16.0 * depth)
    budget_tau = epsilon / (64.0 * depth)
    budget_gamma = epsilon / (64.0 * depth)
    node_error = epsilon / (16.0 * depth)
    total_bound = (
        epsilon_in
        + depth * budget_delta / (1.0 + budget_delta)
        + 2.0 * depth * (budget_tau + budget_gamma)
        + depth * node_error
    )
    checks["complete_result_budget_excess"] = max(0.0, total_bound - epsilon)

    failures = {name: value for name, value in checks.items() if value > TOL}
    print(json.dumps({
        "seed": 20260905,
        "check_count": len(checks),
        "removed_mass": removed_mass,
        "removed_mass_bound": 2.0 * bit_count * (tau + gamma),
        "filter_ray_error": ray_error,
        "filter_ray_bound": ray_bound,
        "complete_result_bound": total_bound,
        "checks": checks,
        "passed": not failures,
    }, indent=2))
    if failures:
        raise SystemExit(f"failed checks: {failures}")


if __name__ == "__main__":
    main()
