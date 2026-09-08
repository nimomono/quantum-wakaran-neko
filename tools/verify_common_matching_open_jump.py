#!/usr/bin/env python3
import numpy as np

def generator_from_rates(rates):
    q = np.array(rates, dtype=float)
    np.fill_diagonal(q, 0.0)
    np.fill_diagonal(q, -q.sum(axis=1))
    return q

pi = np.array([0.2, 0.3, 0.5])
rates = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        if i != j:
            rates[i, j] = np.sqrt(pi[j] / pi[i])
Q = generator_from_rates(rates)
assert np.max(np.abs(Q.sum(axis=1))) < 1e-12
assert np.max(np.abs(pi @ Q)) < 1e-12

p = np.array([0.25, 0.35, 0.40])
j = np.array([[0, 0.02, -0.01], [-0.02, 0, 0.015], [0.01, -0.015, 0]])
t = np.abs(j) + 0.08
np.fill_diagonal(t, 0)
kp = np.zeros((3, 3))
km = np.zeros((3, 3))
for i in range(3):
    for k in range(3):
        if i != k:
            kp[i, k] = (t[i, k] + j[i, k]) / (2 * p[i])
            km[i, k] = (t[i, k] - j[i, k]) / (2 * p[i])

assert kp.min() >= -1e-14 and km.min() >= -1e-14
for i in range(3):
    for k in range(3):
        if i != k:
            assert abs(p[i] * kp[i, k] - p[k] * kp[k, i] - j[i, k]) < 1e-12
            assert abs(p[k] * kp[k, i] / p[i] - km[i, k]) < 1e-12

h = 1e-3
P = np.eye(3) + h * generator_from_rates(kp)
assert P.min() > -1e-12
assert np.max(np.abs(P.sum(axis=1) - 1)) < 1e-12
print("R161/R162 open-jump checks passed")
