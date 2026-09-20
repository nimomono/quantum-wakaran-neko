#!/usr/bin/env python3
from __future__ import annotations

from math import isclose, sqrt

def beta_star(r: float) -> float:
    if abs(r) < 1e-15:
        return 0.0
    return r/(1.0 + sqrt(1.0-r*r))

def force_shape(beta: float, r: float) -> float:
    return r*(1.0+beta*beta) - 2.0*beta

for r in (-0.8, -0.4, -0.1, 0.0, 0.1, 0.4, 0.8):
    b = beta_star(r)
    assert abs(b) < 1.0
    assert isclose(force_shape(b, r), 0.0, abs_tol=1e-13)
    assert 2.0*r*b - 2.0 < 0.0

for r in (0.02, 0.05, 0.1, 0.2):
    b = beta_star(r)
    assert abs(b - 0.5*r) < 0.2*r**3

r = 0.35
target = beta_star(r)
beta = -0.2
dt = 2e-3
rate = 1.7
for _ in range(6000):
    beta += dt*rate*force_shape(beta, r)
assert abs(beta-target) < 2e-6

print("m63_scatterer_tracking_ok", target, beta)
