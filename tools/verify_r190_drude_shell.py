#!/usr/bin/env python3
import math
import numpy as np

TOL = 5e-12

def check(cond, label):
    if not cond:
        raise AssertionError(label)

def cross_matrix(n):
    x, y, z = n
    return np.array([[0.0, -z, y], [z, 0.0, -x], [-y, x, 0.0]])

rng = np.random.default_rng(190)

for _ in range(40):
    z = rng.normal(size=2) + 1j * rng.normal(size=2)
    j0 = 1.7
    k = j0 * abs(z[0]) ** 2
    i = j0 * abs(z[1]) ** 2
    sx = j0 * (np.conj(z[0]) * z[1] + np.conj(z[1]) * z[0]).real / 2.0
    sy = (j0 * (np.conj(z[0]) * z[1] - np.conj(z[1]) * z[0]) / (2.0j)).real
    sz = (k - i) / 2.0
    a = k + i
    check(abs(sx * sx + sy * sy + sz * sz - a * a / 4.0) < 2e-11, "Schwinger action identity")

for g in (0.0, 0.3, 1.0, 2.0):
    for _ in range(20):
        n = rng.normal(size=3)
        n /= np.linalg.norm(n)
        c = cross_matrix(n)
        p = np.eye(3) - np.outer(n, n)
        check(np.linalg.norm(c.T + c) < TOL, "C antisymmetric")
        check(np.linalg.norm(c @ c + p) < TOL, "C^2=-P")
        b = math.sqrt(2.0 / (1.0 + g * g)) * (g * p + c)
        check(np.linalg.norm(b @ b.T - 2.0 * p) < 2e-11, "BBT=2P")

c0 = math.sqrt(3.0) + math.sqrt(13.0 / 3.0)
cG = math.sqrt(18.0)
bstr = 4.0 * c0 * c0 + 4.0 * c0 * cG + cG * cG

def cstr(g, s):
    cR = 16.43 * math.sqrt(1.0 + g * g)
    astr = 4.0 * c0 + 2.0 * cR + 4.0 * cG
    return c0 + 0.5 * (astr * s + math.sqrt(astr * astr * s * s + 4.0 * (c0 * c0 + bstr * s)))

for g in (0.0, 0.5, 1.0, 2.0):
    for s in (0.1, 1.0, 3.0):
        check(math.isfinite(cstr(g, s)) and cstr(g, s) > 0.0, "finite C_str")
        errs = [cstr(g, s) * math.sqrt(tau) for tau in (1e-4, 1e-6, 1e-8)]
        check(errs[2] < errs[1] < errs[0], "memory convergence")

def emix(s):
    q = math.exp(-4.0 * s)
    return min(1.0, math.sqrt(q * (3.0 - q)) / (2.0 * (1.0 - q)))

vals = [emix(s) for s in (0.2, 0.5, 1.0, 2.0, 4.0)]
check(all(b < a for a, b in zip(vals, vals[1:])), "mixing bound decreases")

for _ in range(50):
    ai = 0.2 + 3.0 * rng.random()
    aj = 0.2 + 3.0 * rng.random()
    cap = 0.7 * min(math.sqrt(ai / aj), math.sqrt(aj / ai))
    pij = cap * math.sqrt(aj / ai)
    pji = cap * math.sqrt(ai / aj)
    check(0.0 <= pij <= 1.0 and 0.0 <= pji <= 1.0, "safe aperture")
    check(abs(ai * pij - aj * pji) < 2e-12, "action detailed balance")

for delta in (1e-3, 1e-2, 0.1, 0.5):
    qmin = 0.2
    cstar = math.sqrt(delta * qmin / (1.0 + delta))
    amin = delta * qmin
    amax = 1.0 + delta
    check(cstar * math.sqrt(amax / amin) <= 1.0 + 2e-12, "uniform aperture bound")

print("R190 Drude action-shell checks: OK")
