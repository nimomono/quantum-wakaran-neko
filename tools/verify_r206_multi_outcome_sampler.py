#!/usr/bin/env python3
"""Deterministic checks for R206A finite-L common-hub sampler."""

import math
import random

def evolve(a, x0, h0, lam, kap, t):
    asum = sum(a)
    p = [v / asum for v in a]
    hinf = lam / (lam + kap * asum)
    h = hinf + (h0 - hinf) * math.exp(-(lam + kap * asum) * t)
    x = []
    for py, xinit in zip(p, x0):
        d0 = xinit - py * (1.0 - h0)
        x.append(py * (1.0 - h) + math.exp(-lam * t) * d0)
    return x, h, p

def tv(a, b):
    return 0.5 * sum(abs(x-y) for x, y in zip(a, b))

def main():
    random.seed(7)
    for L in (2, 4, 8, 32, 256, 4096):
        a = [random.random() for _ in range(L)]
        if L >= 4:
            a[0] = 0.0
        s = sum(a)
        a = [v/s for v in a]
        x0 = [0.0] * L
        x0[-1] = 1.0
        x, h, p = evolve(a, x0, 0.0, 1.3, 40.0, 8.0)
        assert abs(sum(x) + h - 1.0) < 1e-10
        assert x[0] >= -1e-13
        cond = [v / (1.0-h) for v in x]
        assert tv(cond, p) < 1e-4

    print("R206A multi-outcome sampler checks: OK")

if __name__ == "__main__":
    main()
