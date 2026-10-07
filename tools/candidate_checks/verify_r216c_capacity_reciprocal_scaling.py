#!/usr/bin/env python3
from __future__ import annotations

import math
import numpy as np


def main() -> None:
    rng = np.random.default_rng(216)
    l = 12
    raw = rng.uniform(0.5, 1.5, size=l)
    p = raw / np.sum(raw)
    chi = rng.uniform(0.2, 1.0, size=l)
    chi /= np.sum(chi)
    kbt = 1.3
    p_t = 0.03
    w = float(np.dot(chi, p) + p_t)
    grad_p = -kbt * chi / w
    projected = grad_p - float(np.dot(p, grad_p))

    capacities = np.array([10.0, 20.0, 40.0, 80.0, 160.0])
    loads = []
    homogeneity = []
    for c in capacities:
        q = c * p
        grad_q = projected / c
        loads.append(float(np.max(np.abs(grad_q))))
        homogeneity.append(abs(float(np.dot(q, grad_q))))
    loads = np.asarray(loads)
    slope = float(np.polyfit(np.log(capacities), np.log(loads), 1)[0])
    assert -1.01 < slope < -0.99, slope
    assert max(homogeneity) < 2e-14

    score_proxy = -kbt * math.log(w)
    for c in capacities:
        q = c * p
        pp = q / np.sum(q)
        ww = float(np.dot(chi, pp) + p_t)
        assert abs(-kbt * math.log(ww) - score_proxy) < 2e-14

    length = 2.0 * math.pi
    n = 200000
    x = np.linspace(0.0, length, n, endpoint=False)
    pi = (1.0 + 0.23 * np.cos(x) + 0.04 * np.sin(2.0 * x)) / length
    pix = (-0.23 * np.sin(x) + 0.08 * np.cos(2.0 * x)) / length
    force = -kbt * pix / pi
    mean_force = float(length * np.mean(pi * force))
    fisher = float(length * np.mean(pix**2 / pi))
    force2 = float(length * np.mean(pi * force**2))
    assert abs(mean_force) < 2e-10
    assert abs(force2 - kbt**2 * fisher) < 2e-10

    mass = 0.71
    nu = 0.28
    gamma = kbt / nu
    f_si = 0.5 * mass * nu**2 * fisher
    f_from_force = mass * force2 / (2.0 * gamma**2)
    assert abs(f_si - f_from_force) < 2e-12

    print(
        "r216c_capacity_ok "
        f"load_slope={slope:.6f} "
        f"mean_force={mean_force:.3e} "
        f"fisher_identity={abs(force2-kbt**2*fisher):.3e}"
    )


if __name__ == "__main__":
    main()
