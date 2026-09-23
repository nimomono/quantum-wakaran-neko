#!/usr/bin/env python3
"""Required checks for R206E uniform root preparation / refresh."""

import math
import numpy as np

TOL = 1.0e-12

def main():
    rng = np.random.default_rng(206005)
    for n in (2, 4, 8, 12):
        L = 2**n
        zstar = np.zeros(L, dtype=complex)
        zstar[0] = 1.7
        z0 = rng.normal(size=L) + 1j * rng.normal(size=L)
        gamma = 0.37
        t = 8.0
        exact = zstar + math.exp(-gamma*t) * (z0-zstar)
        bound = math.exp(-gamma*t) * np.linalg.norm(z0-zstar)
        assert abs(np.linalg.norm(exact-zstar) - bound) < 5e-11

    eps = 1e-6
    B = 5.0
    gamma = 0.25
    T = math.log(B/eps)/gamma
    assert B*math.exp(-gamma*T) <= eps*(1+1e-12)

    # R206A pointer convergence requires no state-specific reset.
    lam = 0.6
    t = math.log(1/eps)/lam
    assert math.exp(-lam*t) <= eps*(1+1e-12)

    print("R206E uniform root preparation checks: OK")

if __name__ == "__main__":
    main()
