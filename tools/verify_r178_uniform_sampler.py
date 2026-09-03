#!/usr/bin/env python3
from __future__ import annotations

import itertools

import numpy as np


TOL = 2.0e-12


def random_unitary(rng: np.random.Generator, size: int) -> np.ndarray:
    matrix = rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))
    q, r = np.linalg.qr(matrix)
    phase = np.diag(r)
    return q @ np.diag(np.conj(phase) / np.abs(phase))


def projector(bit_count: int, bit: int, value: int) -> np.ndarray:
    diagonal = [int(((index >> (bit_count - bit - 1)) & 1) == value) for index in range(2**bit_count)]
    return np.diag(diagonal).astype(complex)


def main() -> None:
    rng = np.random.default_rng(178)
    local = random_unitary(rng, 4)
    sectors = 8
    ideal = np.kron(np.eye(sectors), local)
    perturbations: list[np.ndarray] = []
    blocks: list[np.ndarray] = []
    for _ in range(sectors):
        delta = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
        delta *= 1.0e-7 / np.linalg.norm(delta, 2)
        perturbations.append(delta)
        blocks.append(local + delta)
    actual = np.zeros_like(ideal)
    for index, block in enumerate(blocks):
        actual[4 * index : 4 * (index + 1), 4 * index : 4 * (index + 1)] = block
    block_error = max(np.linalg.norm(delta, 2) for delta in perturbations)
    direct_sum_error = np.linalg.norm(actual - ideal, 2)
    assert abs(direct_sum_error - block_error) < TOL

    bit_count = 4
    p0 = projector(bit_count, 2, 0)
    p1 = projector(bit_count, 2, 1)
    filter_matrix = np.block([[p0, p1], [p1, -p0]])
    identity = np.eye(2 ** (bit_count + 1))
    assert np.linalg.norm(filter_matrix @ filter_matrix - identity, 2) < TOL
    assert np.linalg.norm(filter_matrix.conj().T @ filter_matrix - identity, 2) < TOL

    state = rng.normal(size=2**bit_count) + 1j * rng.normal(size=2**bit_count)
    state /= np.linalg.norm(state)
    born = np.abs(state) ** 2
    sequential = np.zeros_like(born)
    for outcome in itertools.product((0, 1), repeat=bit_count):
        branch = state.copy()
        probability = 1.0
        for bit, value in enumerate(outcome):
            projection = projector(bit_count, bit, value)
            weight = float(np.vdot(projection @ branch, projection @ branch).real)
            norm = float(np.vdot(branch, branch).real)
            conditional = weight / norm
            probability *= conditional
            branch = projection @ branch
        index = sum(value << (bit_count - bit - 1) for bit, value in enumerate(outcome))
        sequential[index] = probability
    assert np.max(np.abs(sequential - born)) < TOL

    tau = 0.07
    cut_mass = 0.0
    active = {(): (state, 1.0)}
    for bit in range(bit_count):
        following: dict[tuple[int, ...], tuple[np.ndarray, float]] = {}
        for history, (branch, parent_probability) in active.items():
            norm = float(np.vdot(branch, branch).real)
            for value in (0, 1):
                child = projector(bit_count, bit, value) @ branch
                conditional = float(np.vdot(child, child).real) / norm
                if conditional < tau:
                    cut_mass += parent_probability * conditional
                else:
                    following[history + (value,)] = (child, parent_probability * conditional)
        active = following
    assert cut_mass <= 2.0 * bit_count * tau + TOL

    print(f"sector direct-sum error = {direct_sum_error:.3e}")
    print(f"filter involution error = {np.linalg.norm(filter_matrix @ filter_matrix - identity, 2):.3e}")
    print(f"sequential Born error = {np.max(np.abs(sequential - born)):.3e}")
    print(f"rare-branch cut mass = {cut_mass:.6f} <= {2.0 * bit_count * tau:.6f}")


if __name__ == "__main__":
    main()
