#!/usr/bin/env python3
from __future__ import annotations

from math import exp, isclose, log

s = [0.0, 0.03, 0.17, 0.46, 0.79, 0.96, 1.0]
gamma = [s[i+1] - s[i] for i in range(len(s)-1)]
assert all(g >= -1e-15 for g in gamma)
assert isclose(sum(gamma), 1.0, abs_tol=1e-14)

r = [0.42, 0.57, 0.83, 1.21, 1.64, 2.05]
r_star = 1.0
log_rk = sum(g * log(ri/r_star) for ri, g in zip(r, gamma))
r_k = r_star * exp(log_rk)

w = [0.11, 0.23, 0.29, 0.37]
assert isclose(sum(w), 1.0, abs_tol=1e-14)
lam = [(r_k/r_star) ** (-wi) for wi in w]
assert all(x > 0.0 for x in lam)

jacobian_ratio = 1.0
for x in lam:
    jacobian_ratio *= 1.0/x
assert isclose(jacobian_ratio, r_k/r_star, rel_tol=1e-13, abs_tol=1e-13)

R = 1.7
shifts = [0.3*R, -0.2*R, 0.5*R, 0.1*R]
for la, sh in zip(lam, shifts):
    zeta = 0.8
    c = la*zeta - sh
    assert isclose(zeta, (c + sh)/la, abs_tol=1e-14)

print("m63_topological_partition_ok", r_k, jacobian_ratio)
