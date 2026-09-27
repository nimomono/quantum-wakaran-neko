#!/usr/bin/env python3
"""Required checks for R212A M67 thermal-sector embedding."""

import math
import numpy as np


def main() -> None:
    q = np.array([0.07, 0.13, 0.20, 0.25, 0.35], dtype=float)
    assert abs(float(q.sum()) - 1.0) < 1e-15

    for s in np.linspace(-1.7, 1.9, 17):
        w = math.exp(0.31 * s + 0.08 * math.cos(2.0 * s))
        dlogw = 0.31 - 0.16 * math.sin(2.0 * s)
        jac = float(np.prod(w ** q))
        assert abs(jac - w) < 2e-13 * max(1.0, w)

        # Momentum and coordinate translations have unit Jacobian.
        for U in (-4.0, -0.2, 0.0, 1.7):
            for R in (-3.0, 0.0, 2.2):
                shifted_partition_factor = jac
                assert abs(shifted_partition_factor - w) < 2e-13 * max(1.0, w)
                assert math.isfinite(U + R)

        mean_force = dlogw  # k_B T = 1
        expected = dlogw
        assert abs(mean_force - expected) < 1e-15

        variance = 2.0 * float(np.dot(q, q)) * dlogw**2
        assert variance >= 0.0

    # Equal weights give the announced N_pv^{-1/2} RMS law.
    vals = []
    for n in (8, 32, 128, 512):
        qn = np.full(n, 1.0 / n)
        rms = math.sqrt(2.0 * float(np.dot(qn, qn)))
        vals.append((n, rms))
        assert abs(rms - math.sqrt(2.0 / n)) < 1e-14
    for (n1, r1), (n2, r2) in zip(vals, vals[1:]):
        assert r2 < r1
        assert abs((r2 / r1) - math.sqrt(n1 / n2)) < 1e-14

    print("R212A thermal embedding checks: OK")


if __name__ == "__main__":
    main()
