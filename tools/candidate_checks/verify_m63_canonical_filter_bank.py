#!/usr/bin/env python3
from __future__ import annotations

from math import isclose, sqrt

SQRT2 = sqrt(2.0)

samples = [
    (1.2, -0.7, 0.4, 2.1),
    (-3.0, 0.5, -1.4, 0.9),
    (0.0, 2.0, 3.0, -4.0),
]

for phi0, phi1, pi0, pi1 in samples:
    u = (phi0 + phi1) / SQRT2
    v = (phi0 - phi1) / SQRT2
    p = (pi0 + pi1) / SQRT2
    q = (pi0 - pi1) / SQRT2

    phi0_r = (u + v) / SQRT2
    phi1_r = (u - v) / SQRT2
    pi0_r = (p + q) / SQRT2
    pi1_r = (p - q) / SQRT2

    assert isclose(phi0, phi0_r, rel_tol=0.0, abs_tol=1e-12)
    assert isclose(phi1, phi1_r, rel_tol=0.0, abs_tol=1e-12)
    assert isclose(pi0, pi0_r, rel_tol=0.0, abs_tol=1e-12)
    assert isclose(pi1, pi1_r, rel_tol=0.0, abs_tol=1e-12)

    kinetic_micro = 0.5 * (pi0 * pi0 + pi1 * pi1)
    kinetic_branch = 0.5 * (p * p + q * q)
    assert isclose(kinetic_micro, kinetic_branch, rel_tol=0.0, abs_tol=1e-12)

a = 1.0 / SQRT2
rows = [(a, a), (a, -a)]
for i in range(2):
    for j in range(2):
        dot = sum(rows[i][k] * rows[j][k] for k in range(2))
        assert isclose(dot, 1.0 if i == j else 0.0, abs_tol=1e-12)

print("m63_canonical_filter_bank_ok")
