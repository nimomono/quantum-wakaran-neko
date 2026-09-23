#!/usr/bin/env python3
"""Candidate checks for R206B/R206C passive L-channel scaling."""

import random

def tv(a, b):
    return 0.5 * sum(abs(x-y) for x, y in zip(a, b))

def normalize(v):
    s = sum(v)
    return [x/s for x in v]

def main():
    random.seed(11)
    delta = 1e-2
    eta = 2e-2
    b = 1e-3
    vals = []
    for L in (4, 16, 64, 256, 1024, 4096, 16384):
        p = normalize([random.expovariate(1.0) for _ in range(L)])
        s = [delta + L*x for x in p]
        preg = normalize(s)
        expected = [(x + delta/L)/(1.0+delta) for x in p]
        assert tv(preg, expected) < 1e-12
        rates = [x/L for x in s]
        assert abs(sum(rates) - (1.0+delta)) < 1e-12

        pert = []
        for x in s:
            eps = random.uniform(-eta, eta)
            off = random.uniform(-b, b)
            pert.append(max(1e-15, x*(1.0+eps)+off))
        err = tv(normalize(pert), preg)
        bound = (eta + b/delta) / (1.0 - eta - b/delta)
        assert err <= bound + 1e-12
        vals.append((L, err))

    assert max(v for _, v in vals) < 0.02
    print("R206B/R206C passive scaling checks: OK")
    print("TV scan:", vals)

if __name__ == "__main__":
    main()
