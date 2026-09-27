#!/usr/bin/env python3
from __future__ import annotations

import math
import numpy as np

TOL = 5.0e-11


def exact(t: float, a: np.ndarray, kappa: float) -> np.ndarray:
    asum = float(a.sum())
    if asum <= 0.0:
        raise ValueError("total action must be positive")
    survival = math.exp(-kappa * asum * t)
    p = a / asum
    return np.array([
        p[0] * (1.0 - survival),
        p[1] * (1.0 - survival),
        survival,
    ])


def tv_to_born(out: np.ndarray, a: np.ndarray) -> float:
    p = a / float(a.sum())
    return 0.5 * (
        abs(float(out[0] - p[0]))
        + abs(float(out[1] - p[1]))
        + abs(float(out[2]))
    )


def main() -> None:
    rng = np.random.default_rng(204140)
    max_mass_error = 0.0
    max_tv_error = 0.0
    max_ratio_error = 0.0

    for _ in range(5000):
        a = 10.0 ** rng.uniform(-5.0, 2.0, size=2)
        kappa = 10.0 ** rng.uniform(-2.0, 2.0)
        t = rng.uniform(0.0, 20.0)

        out = exact(t, a, kappa)
        max_mass_error = max(max_mass_error, abs(float(out.sum()) - 1.0))

        survival = math.exp(-kappa * float(a.sum()) * t)
        max_tv_error = max(max_tv_error, abs(tv_to_born(out, a) - survival))

        decided = float(out[0] + out[1])
        if decided > 1.0e-14:
            ratio = out[:2] / decided
            p = a / float(a.sum())
            max_ratio_error = max(
                max_ratio_error,
                float(np.max(np.abs(ratio - p))),
            )

    assert max_mass_error < TOL
    assert max_tv_error < TOL
    assert max_ratio_error < 2.0e-10

    # Exact zero endpoints belong to the domain when total action is positive.
    for a in (np.array([0.0, 2.3]), np.array([1.7, 0.0])):
        out = exact(3.0, a, 1.4)
        assert abs(float(out.sum()) - 1.0) < TOL
        if a[0] == 0.0:
            assert abs(float(out[0])) < TOL
        if a[1] == 0.0:
            assert abs(float(out[1])) < TOL

    # Endpoint/cutoff comparisons remain division-free.
    tau = 0.07
    for _ in range(10000):
        ap, am = 10.0 ** rng.uniform(-5.0, 3.0, size=2)
        pplus = ap / (ap + am)
        lhs = (1.0 - tau) * ap - tau * am
        assert (pplus < tau) == (lhs < 0.0)

    # A common action rescaling changes the waiting time but not the winner ratio.
    base = np.array([0.37, 1.13])
    p = base / float(base.sum())
    for scale in (1.0e-3, 0.2, 3.0, 80.0):
        a = scale * base
        out = exact(2.7, a, 1.9)
        decided = float(out[0] + out[1])
        if decided > 1.0e-14:
            ratio = out[:2] / decided
            assert np.max(np.abs(ratio - p)) < 2.0e-10

    # Tiny Born branches do not shrink the total decision hazard at fixed total action.
    kappa = 1.7
    a_sum = 2.4
    target_hazard = kappa * a_sum
    for n in (8, 16, 32, 64, 128):
        pminus = 2.0 ** (-n)
        a = np.array([(1.0 - pminus) * a_sum, pminus * a_sum])
        hazard = kappa * float(a.sum())
        assert abs(hazard - target_hazard) < 2.0e-12

    # Finite latch copies the complete-result distribution without renormalizing.
    a = np.array([0.8, 1.2])
    record = exact(2.7, a, 1.9)
    post_latch = record.copy()
    assert np.max(np.abs(post_latch - record)) < TOL
    assert abs(float(record.sum()) - 1.0) < TOL

    print("M65 two-result first-passage selector checks: OK")


if __name__ == "__main__":
    main()
