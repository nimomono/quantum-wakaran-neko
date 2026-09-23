#!/usr/bin/env python3
"""Required checks for R207 projection phase-volume Q2-2 mainline."""

from __future__ import annotations
import math
import numpy as np


def f_eps(t, eps: float):
    t = np.asarray(t)
    return np.sqrt(t**2 + eps**2 * (1.0 - t**2))


def langevin(k: float) -> float:
    return 1.0 / math.tanh(k) - 1.0 / k


def singlet_tv_bound(eps: float, k: float) -> float:
    return 2.0 * eps + 0.5 * (1.0 - langevin(k))


def main() -> None:
    grid = np.linspace(-1.0, 1.0, 20001)
    for eps in (0.2, 0.05, 0.01, 0.002):
        f = f_eps(grid, eps)
        assert np.min(f) >= eps - 1e-15
        assert np.max(f - np.abs(grid)) <= eps + 2e-15
        assert np.min(f - np.abs(grid)) >= -2e-15

    x, w = np.polynomial.legendre.leggauss(256)
    abs_integral = 2.0 * math.pi * float(np.sum(w * np.abs(x)))
    assert abs(abs_integral - 2.0 * math.pi) < 8e-5

    for delta in np.linspace(0.0, math.pi, 17):
        numerical = 2.0 * math.pi * math.cos(delta) * float(np.sum(w * x * np.sign(x)))
        exact = 2.0 * math.pi * math.cos(delta)
        assert abs(numerical - exact) < 1.0e-4

    assert 2.0 * math.sqrt(2.0) * langevin(3.3877) < 2.0
    assert 2.0 * math.sqrt(2.0) * langevin(3.3879) > 2.0

    dots = np.array([1.0, 1.0, 1.0, -1.0]) / math.sqrt(2.0)
    for k in (4.0, 20.0, 100.0):
        L = langevin(k)
        corr = -L * dots
        schsh = corr[0] + corr[1] + corr[2] - corr[3]
        assert abs(abs(schsh) - 2.0 * math.sqrt(2.0) * L) < 1e-14
        assert 0.0 < L < 1.0

    for eps in (0.01, 0.1):
        F = float(np.sum(w * f_eps(x, eps)))
        assert F > 0.0
        for k in (1.0, 5.0, 20.0):
            G = 4.0 * math.pi * math.sinh(k) / k
            Z = 4.0 * math.pi * F * G
            assert math.isfinite(Z) and Z > 0.0

    eps = 0.01
    assert 2.0 / (2.0 * eps) > 50.0

    rng = np.random.default_rng(207)
    for _ in range(100):
        la, lb, a, b = (rng.normal(size=3) for _ in range(4))
        la /= np.linalg.norm(la)
        lb /= np.linalg.norm(lb)
        a /= np.linalg.norm(a)
        b /= np.linalg.norm(b)
        k = 7.0
        wt = math.exp(k * float(np.dot(la, lb))) * (
            float(f_eps(np.dot(a, la), eps)) + float(f_eps(np.dot(b, lb), eps))
        )
        wt_inv = math.exp(k * float(np.dot(-la, -lb))) * (
            float(f_eps(np.dot(a, -la), eps)) + float(f_eps(np.dot(b, -lb), eps))
        )
        assert abs(wt - wt_inv) <= 2e-12 * max(1.0, wt)
        r = 1 if np.dot(a, la) >= 0.0 else -1
        s = -1 if np.dot(b, lb) >= 0.0 else 1
        r_inv = 1 if np.dot(a, -la) >= 0.0 else -1
        s_inv = -1 if np.dot(b, -lb) >= 0.0 else 1
        assert r_inv == -r and s_inv == -s

    for target in (0.2, 0.1, 0.05, 0.02, 0.01):
        eps, k = target / 8.0, 2.0 / target
        assert singlet_tv_bound(eps, k) < 0.5 * target + 1e-12

    vals = (-1, 1)
    for a0 in vals:
        for a1 in vals:
            for b0 in vals:
                for b1 in vals:
                    chsh = a0*b0 + a0*b1 + a1*b0 - a1*b1
                    assert abs(chsh) <= 2

    print("R207 projection phase-volume required checks: OK")


if __name__ == "__main__":
    main()
