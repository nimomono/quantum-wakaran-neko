#!/usr/bin/env python3
"""Candidate numerical witness for R207A/R207B.

This is not a required fixed-goal verifier and not an A2 direct SDE simulation.
"""

import math
import numpy as np

PAIRS = ((0, 0), (0, 1), (1, 0), (1, 1))
ALPHA = (0.0, math.pi / 2.0)
BETA = (math.pi / 4.0, -math.pi / 4.0)


def sign_grid(value: np.ndarray) -> np.ndarray:
    return np.where(value >= 0.0, 1.0, -1.0)


def strong_lock(kappa: float, n: int = 32768):
    theta = (np.arange(n) + 0.5) * (2.0 * math.pi / n)
    dx = 2.0 * math.pi / n
    correlations = []
    means = []
    cond = []
    partitions = []
    for x, y in PAIRS:
        sa = 1.0 if x == 0 else -1.0
        sb = 1.0 if y == 0 else -1.0
        u = kappa * (sa * np.cos(2.0 * theta) + sb * np.sin(2.0 * theta))
        umax = float(np.max(u))
        w = np.exp(u - umax)
        partitions.append(float(np.sum(w) * dx * math.exp(umax)))
        p = w / (np.sum(w) * dx)
        r = sign_grid(np.cos(theta - ALPHA[x]))
        s = -sign_grid(np.cos(theta - BETA[y]))
        correlations.append(float(np.sum(p * r * s) * dx))
        means.append((float(np.sum(p * r) * dx), float(np.sum(p * s) * dx)))
        cond.append(p)
    s_chsh = correlations[0] + correlations[1] + correlations[2] - correlations[3]
    marginal = sum(cond) / 4.0
    mutual_info = 0.0
    for p in cond:
        mutual_info += 0.25 * float(np.sum(p * np.log2(p / marginal)) * dx)
    return np.array(correlations), s_chsh, np.array(means), mutual_info, np.array(partitions)


def solve_kappa():
    target = 2.0 * math.sqrt(2.0)
    lo, hi = 0.0, 1.0
    for _ in range(42):
        mid = 0.5 * (lo + hi)
        _, s_chsh, _, _, _ = strong_lock(mid)
        if abs(s_chsh) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def finite_lock(klock: float, gamma: float, n: int = 240):
    theta = (np.arange(n) + 0.5) * (2.0 * math.pi / n)
    ta, tb = np.meshgrid(theta, theta, indexing="ij")
    lock = klock * np.cos(ta - tb)
    correlations = []
    means = []
    partitions = []
    for x, y in PAIRS:
        sa = 1.0 if x == 0 else -1.0
        sb = 1.0 if y == 0 else -1.0
        u = lock + gamma * (sa * np.cos(2.0 * ta) + sb * np.sin(2.0 * tb))
        umax = float(np.max(u))
        w = np.exp(u - umax)
        norm = float(np.sum(w))
        partitions.append(norm * math.exp(umax))
        r = sign_grid(np.cos(ta - ALPHA[x]))
        s = -sign_grid(np.cos(tb - BETA[y]))
        correlations.append(float(np.sum(w * r * s) / norm))
        means.append((float(np.sum(w * r) / norm), float(np.sum(w * s) / norm)))
    s_chsh = correlations[0] + correlations[1] + correlations[2] - correlations[3]
    return np.array(correlations), s_chsh, np.array(means), np.array(partitions)


def solve_gamma(klock: float):
    target = 2.0 * math.sqrt(2.0)
    lo, hi = 0.0, 2.0
    for _ in range(30):
        mid = 0.5 * (lo + hi)
        _, s_chsh, _, _ = finite_lock(klock, mid)
        if abs(s_chsh) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main() -> None:
    kappa = solve_kappa()
    corr, s_chsh, means, mutual_info, partitions = strong_lock(kappa, n=65536)
    assert abs(kappa - 0.3684351) < 3.0e-5
    assert abs(abs(s_chsh) - 2.0 * math.sqrt(2.0)) < 2.0e-5
    assert np.max(np.abs(np.abs(corr) - 1.0 / math.sqrt(2.0))) < 1.0e-5
    assert np.max(np.abs(means)) < 2.0e-4
    assert np.max(np.abs(partitions / np.mean(partitions) - 1.0)) < 1.0e-10
    assert 0.08 < mutual_info < 0.11

    gamma = solve_gamma(5.0)
    _, s2, means2, z2 = finite_lock(5.0, gamma, n=360)
    assert 0.54 < gamma < 0.58
    assert abs(abs(s2) - 2.0 * math.sqrt(2.0)) < 2.0e-3
    assert np.max(np.abs(means2)) < 2.0e-3
    assert np.max(np.abs(z2 / np.mean(z2) - 1.0)) < 1.0e-10

    print(
        "R207 candidate witness: "
        f"kappa*={kappa:.9f}, I={mutual_info:.6f} bit, "
        f"finite-lock gamma(k=5)={gamma:.6f}, |S|={abs(s2):.9f}"
    )


if __name__ == "__main__":
    main()
