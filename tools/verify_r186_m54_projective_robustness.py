#!/usr/bin/env python3
"""Deterministic regression checks for R186 M54 projective robustness."""

from __future__ import annotations

import numpy as np


def opnorm(a: np.ndarray) -> float:
    return float(np.linalg.norm(a, 2))


def check_direct_sum() -> None:
    blocks = [
        np.array([[0.0, 0.01], [0.01, 0.0]], dtype=float),
        np.array([[0.0, -0.02], [-0.02, 0.0]], dtype=float),
        np.array([[0.015, 0.0], [0.0, -0.015]], dtype=float),
    ]
    big = np.zeros((6, 6), dtype=float)
    for j, block in enumerate(blocks):
        big[2*j:2*j+2, 2*j:2*j+2] = block
    assert abs(opnorm(big) - max(opnorm(b) for b in blocks)) < 1e-12


def check_sparse_bound() -> None:
    n = 16
    mu = 2.0e-3
    v = np.zeros((n, n), dtype=float)
    for j in range(n):
        v[j, (j + 1) % n] = mu
        v[(j + 1) % n, j] = mu
    degree = 2
    assert opnorm(v) <= degree * mu + 1e-12


def check_phase_noise_formula() -> None:
    p = np.array([0.40, 0.30, 0.20, 0.10], dtype=float)
    sigma = 0.13
    t = 2.5
    ef = np.exp(-sigma*sigma*t) + (1.0 - np.exp(-sigma*sigma*t)) * np.sum(p*p)
    loss = 1.0 - ef
    assert loss >= 0.0
    assert loss <= sigma*sigma*t + 1e-12


def check_projector_latch() -> None:
    z = np.array([1.0+0.2j, 0.5-0.1j, -0.7+0.3j, 0.2+0.4j])
    weights = np.abs(z) ** 2
    mask = np.array([True, False, True, False])
    mu = 0.03
    delta = np.array([0.02, -0.01, -0.03, 0.01])
    j = float(np.sum(weights[mask]))
    jt = float(np.sum((1.0 + delta[mask]) * weights[mask]))
    assert abs(jt - j) <= mu * j + 1e-12


def check_additive_trace() -> None:
    sigma = 0.07
    for nbits in range(1, 9):
        dim = 2 ** nbits
        p = np.zeros((dim, dim), dtype=float)
        p[0, 0] = 1.0
        q = sigma * sigma * np.eye(dim)
        transverse = float(np.trace((np.eye(dim) - p) @ q))
        expected = (dim - 1) * sigma * sigma
        assert abs(transverse - expected) < 1e-10


def main() -> None:
    check_direct_sum()
    check_sparse_bound()
    check_phase_noise_formula()
    check_projector_latch()
    check_additive_trace()
    print("R186 projective robustness checks: OK")


if __name__ == "__main__":
    main()
