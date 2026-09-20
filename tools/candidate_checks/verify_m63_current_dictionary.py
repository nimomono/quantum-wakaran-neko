#!/usr/bin/env python3
from __future__ import annotations

import cmath
from math import isclose, sin, sqrt

SQRT2 = sqrt(2.0)

def chiral_pair(z_i: complex, z_j: complex) -> tuple[float, float]:
    c_plus = (z_i - 1j*z_j)/SQRT2
    c_minus = (z_i + 1j*z_j)/SQRT2
    return abs(c_plus)**2, abs(c_minus)**2

tests = [
    (1.2 + 0.4j, -0.3 + 0.8j),
    (0.7 - 1.1j, 1.4 + 0.2j),
    (2.0 + 0.0j, 0.0 + 0.5j),
]
for zi, zj in tests:
    ip, im = chiral_pair(zi, zj)
    assert isclose(ip + im, abs(zi)**2 + abs(zj)**2, rel_tol=1e-13, abs_tol=1e-13)
    assert isclose(ip - im, 2.0*(zi.conjugate()*zj).imag, rel_tol=1e-13, abs_tol=1e-13)

for theta in (0.01, 0.03, 0.08, 0.15):
    zi = 2.3 + 0j
    zj = zi * cmath.exp(1j*theta)
    ip, im = chiral_pair(zi, zj)
    ratio = (ip-im)/(ip+im)
    assert isclose(ratio, sin(theta), rel_tol=1e-13, abs_tol=1e-13)
    assert abs(ratio-theta) <= theta**3/5.0

print("m63_current_dictionary_ok")
