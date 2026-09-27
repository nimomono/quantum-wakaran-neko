#!/usr/bin/env python3
"""Required geometry and canonical-marginal checks for R212B-rot."""

import math
import numpy as np


def f_eps(t, eps):
    return np.sqrt(t * t + eps * eps * (1.0 - t * t))


def fibonacci_sphere(n):
    i = np.arange(n, dtype=float)
    z = 1.0 - 2.0 * (i + 0.5) / n
    phi = (math.pi * (3.0 - math.sqrt(5.0))) * i
    r = np.sqrt(np.maximum(0.0, 1.0 - z * z))
    return np.column_stack((r * np.cos(phi), r * np.sin(phi), z))


def main() -> None:
    rng = np.random.default_rng(212)
    for _ in range(200):
        lam = rng.normal(size=3)
        lam /= np.linalg.norm(lam)
        P = np.eye(3) - np.outer(lam, lam)
        assert np.linalg.norm(P @ lam) < 2e-14
        assert np.linalg.norm(P @ P - P) < 2e-14
        assert abs(np.trace(P) - 2.0) < 2e-14

        # Ito curvature drift -2 D lambda cancels quadratic variation 2 D Tr(P).
        D = 0.73
        radial_generator = 2.0 * np.dot(lam, -2.0 * D * lam) + 2.0 * D * np.trace(P)
        assert abs(radial_generator) < 2e-14

    # Canonical R207A orientation marginal: partition is setting independent.
    eps = 1.0 / 32.0
    k = 8.0
    pts = fibonacci_sphere(1200)
    pairs = [(0.0, 0.0), (0.0, math.pi / 4), (0.0, math.pi / 2), (0.0, math.pi)]
    zvals = []
    # Product quadrature is too large; exploit exact inner integral of exp(k la.lb).
    G = 4.0 * math.pi * math.sinh(k) / k
    F = 2.0 * math.pi * (2.0 / len(pts)) * float(np.sum(f_eps(pts[:, 2], eps)))
    expected = 2.0 * G * F
    for _, th in pairs:
        b = np.array([math.sin(th), 0.0, math.cos(th)])
        Fa = 4.0 * math.pi * float(np.mean(f_eps(pts[:, 2], eps)))
        Fb = 4.0 * math.pi * float(np.mean(f_eps(pts @ b, eps)))
        zvals.append(G * (Fa + Fb))
    for z in zvals:
        assert abs(z - expected) / expected < 3e-3
    assert max(zvals) - min(zvals) < 3e-3 * expected

    # R207 parameter point remains strictly positive and within the fixed-goal kernel bound.
    assert 2.0 * eps > 0.0
    Lk = 1.0 / math.tanh(k) - 1.0 / k
    err = 2.0 * eps + 0.5 * (1.0 - Lk)
    assert err < 0.125

    print("R212B rotor geometry checks: OK")


if __name__ == "__main__":
    main()
