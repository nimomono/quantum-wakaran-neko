#!/usr/bin/env python3
from __future__ import annotations

from math import exp, isclose, log

s = [0.0, 0.03, 0.17, 0.46, 0.79, 0.96, 1.0]
gamma = [s[i + 1] - s[i] for i in range(len(s) - 1)]
assert all(g >= -1e-15 for g in gamma)
assert isclose(sum(gamma), 1.0, rel_tol=0.0, abs_tol=1e-14)

r = [0.42, 0.57, 0.83, 1.21, 1.64, 2.05]
r_star = 1.0
lam = [(ri / r_star) ** (-g) for ri, g in zip(r, gamma)]
assert all(x > 0.0 for x in lam)

jacobian_ratio = 1.0
for x in lam:
    jacobian_ratio *= 1.0 / x

formula_ratio = exp(sum(g * log(ri / r_star) for ri, g in zip(r, gamma)))
assert isclose(jacobian_ratio, formula_ratio, rel_tol=1e-13, abs_tol=1e-13)

uniform_r = 3.7
uniform_ratio = exp(sum(g * log(uniform_r / r_star) for g in gamma))
assert isclose(uniform_ratio, uniform_r / r_star, rel_tol=1e-13, abs_tol=1e-13)

print("m63_topological_partition_ok")
