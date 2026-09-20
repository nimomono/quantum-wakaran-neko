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
    assert isclose(phi0, (u + v) / SQRT2, abs_tol=1e-12)
    assert isclose(phi1, (u - v) / SQRT2, abs_tol=1e-12)
    assert isclose(pi0, (p + q) / SQRT2, abs_tol=1e-12)
    assert isclose(pi1, (p - q) / SQRT2, abs_tol=1e-12)
    assert isclose(0.5 * (pi0*pi0 + pi1*pi1), 0.5 * (p*p + q*q), abs_tol=1e-12)

r3, r2, r6 = sqrt(3.0), sqrt(2.0), sqrt(6.0)
O = [
    [1.0/r3, 1.0/r3, 1.0/r3],
    [1.0/r2, -1.0/r2, 0.0],
    [1.0/r6, 1.0/r6, -2.0/r6],
]
for i in range(3):
    for j in range(3):
        dot = sum(O[i][k] * O[j][k] for k in range(3))
        assert isclose(dot, 1.0 if i == j else 0.0, abs_tol=1e-12)

v = [0.7, -1.1, 2.0]
q = [1.3, 0.2, -0.8]
V = [sum(O[i][k] * v[k] for k in range(3)) for i in range(3)]
Q = [sum(O[i][k] * q[k] for k in range(3)) for i in range(3)]
assert isclose(sum(x*x for x in v), sum(x*x for x in V), abs_tol=1e-12)
assert isclose(sum(x*x for x in q), sum(x*x for x in Q), abs_tol=1e-12)

print("m63_canonical_filter_bank_ok")
