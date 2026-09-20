#!/usr/bin/env python3
from __future__ import annotations

from math import cos, isclose

modes = [
    (1.3, 2.1, 0.7, 0.8),
    (0.9, 3.4, 1.2, 1.15),
    (2.0, 0.8, 0.5, 0.63),
]

for m, omega, g, lam in modes:
    Omega = lam*omega
    C = g*lam
    assert isclose(
        C*C/(m*Omega*Omega),
        g*g/(m*omega*omega),
        rel_tol=1e-13,
        abs_tol=1e-13,
    )

kBT = 0.37
for t in (0.0, 0.17, 0.41, 0.83):
    gamma = 0.0
    covariance = 0.0
    for m, omega, g, lam in modes:
        Omega = lam*omega
        amp = g*g/(m*omega*omega)
        gamma += amp*cos(Omega*t)
        C = g*lam
        xvar = kBT/(m*Omega*Omega)
        covariance += C*C*xvar*cos(Omega*t)
    assert isclose(covariance, kBT*gamma, rel_tol=1e-13, abs_tol=1e-13)

print("m63_relative_gle_ok")
