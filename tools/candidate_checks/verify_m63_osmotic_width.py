#!/usr/bin/env python3
from __future__ import annotations

from math import exp

def log_r(x: float) -> float:
    return 0.18 * x + 0.025 * x * x + 0.004 * x * x * x

def dlog_r(x: float) -> float:
    return 0.18 + 0.05 * x + 0.012 * x * x

def free_energy(X: float, sigma: float) -> float:
    dx = 0.01
    radius = max(1.0, 6.0 * sigma)
    n = int(radius / dx)
    xs = [X + j * dx for j in range(-n, n + 1)]
    ws = [exp(-0.5 * ((x - X) / sigma) ** 2) for x in xs]
    norm = sum(ws)
    return -sum(w * log_r(x) for w, x in zip(ws, xs)) / norm

def force(X: float, sigma: float) -> float:
    h = 1e-4
    return -(free_energy(X + h, sigma) - free_energy(X - h, sigma)) / (2.0 * h)

X = 0.7
errors = [abs(force(X, sigma) - dlog_r(X)) for sigma in (0.45, 0.30, 0.20, 0.12)]
assert errors[-1] < errors[0]
assert errors[-1] < 5e-4
print("m63_osmotic_width_ok", errors)
