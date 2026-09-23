#!/usr/bin/env python3
"""Candidate checks for M66/R205 common phase-volume identities."""

import math

def main():
    for w in (0.01, 0.2, 1.0, 3.0, 100.0):
        q = [0.2, 0.3, 0.5]
        jac = math.prod(w ** qi for qi in q)
        assert abs(jac - w) <= 1e-12 * max(1.0, abs(w))

    V0, G0, VH0 = 2.0, 3.0, 5.0
    for s in (0.01, 0.5, 1.0, 20.0):
        V = V0 * s
        G = G0 * s
        assert abs(G / V - G0 / V0) < 1e-14
        assert abs(G / VH0 - (G0 / VH0) * s) < 1e-14

    print("M66/R205 common phase-volume checks: OK")

if __name__ == "__main__":
    main()
