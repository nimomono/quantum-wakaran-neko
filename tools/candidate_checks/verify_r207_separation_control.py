#!/usr/bin/env python3
"""Strengthening-only diagnostics for R207 finite-distance separation."""

import math


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
    assert worst[-1] < 1e-3

    # A numerical timing example only illustrates the strengthening inequality.
    # The candidate checker does not derive L or vmax from a concrete reservoir.
    L, vmax, t_meas = 10.0, 2.0, 1.0
    assert t_meas < L / vmax

    print("R207 finite-distance strengthening diagnostics: OK")


if __name__ == "__main__":
    main()
