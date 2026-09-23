#!/usr/bin/env python3
"""Candidate checks for R207C/R207D causal separation and Bell-local control."""

import math
import numpy as np


def r205f_defect(rdist: float, x: float, y: float):
    mu_a, mu_b = 0.8, 1.1
    k = math.exp(-rdist)
    c = 0.2 * math.exp(-2.0 * rdist)
    dva = -math.sin(x - y)
    dvb = math.sin(x - y)
    dfa = math.cos(x) * math.cos(y)
    dfb = -math.sin(x) * math.sin(y)
    mixed = -math.cos(x) * math.sin(y)
    defect = -k * (mu_a * dva * dfa + mu_b * dvb * dfb) + 2.0 * c * mixed
    bound = abs(k) * (mu_a * abs(dva * dfa) + mu_b * abs(dvb * dfb)) + 2.0 * abs(c * mixed)
    return defect, bound


def local_control(n: int = 131072):
    theta = (np.arange(n) + 0.5) * (2.0 * math.pi / n)
    alpha = (0.0, math.pi / 2.0)
    beta = (math.pi / 4.0, -math.pi / 4.0)
    corr = []
    for x, y in ((0, 0), (0, 1), (1, 0), (1, 1)):
        r = np.where(np.cos(theta - alpha[x]) >= 0.0, 1.0, -1.0)
        s = -np.where(np.cos(theta - beta[y]) >= 0.0, 1.0, -1.0)
        corr.append(float(np.mean(r * s)))
    s_chsh = corr[0] + corr[1] + corr[2] - corr[3]
    return np.array(corr), s_chsh


def main() -> None:
    worst = []
    for rdist in (0.0, 1.0, 2.0, 4.0, 8.0):
        value = 0.0
        for x in (0.2, 1.1, 2.4):
            for y in (0.4, 1.7, 2.8):
                defect, bound = r205f_defect(rdist, x, y)
                assert abs(defect) <= bound + 1e-15
                value = max(value, abs(defect))
        worst.append(value)
    assert all(b < a for a, b in zip(worst, worst[1:]))

    corr, s_chsh = local_control()
    assert np.max(np.abs(corr - np.array([-0.5, -0.5, -0.5, 0.5]))) < 2.0e-5
    assert abs(abs(s_chsh) - 2.0) < 5.0e-5
    print("R207 separation/control candidate checks: OK")


if __name__ == "__main__":
    main()
