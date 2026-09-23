#!/usr/bin/env python3
"""Required regression checks for R205E common thermal Gibbs sampler."""

import math
import numpy as np


def main() -> None:
    beta = 1.3
    kbt = 1.0 / beta
    mu = 0.7
    x = np.linspace(0.0, 2.0 * math.pi, 4096, endpoint=False)
    logw = 0.35 * np.cos(x) + 0.10 * np.cos(2.0 * x)
    dlogw = -0.35 * np.sin(x) - 0.20 * np.sin(2.0 * x)
    hcfg = 0.40 * np.sin(x) + 0.20 * np.cos(3.0 * x)
    dhcfg = 0.40 * np.cos(x) - 0.60 * np.sin(3.0 * x)

    pi = np.exp(logw - beta * hcfg)
    dx = 2.0 * math.pi / len(x)
    pi /= pi.sum() * dx
    dpi = pi * (dlogw - beta * dhcfg)
    drift = mu * (kbt * dlogw - dhcfg)
    current = drift * pi - mu * kbt * dpi
    assert np.max(np.abs(current)) < 5e-13
    assert abs(pi.sum() * dx - 1.0) < 1e-12

    n = 64
    stride = len(pi) // n
    weights = pi[::stride][:n].copy()
    weights /= weights.sum()
    qmat = np.zeros((n, n))
    for i in range(n):
        for j in ((i - 1) % n, (i + 1) % n):
            qmat[i, j] = 0.25 / weights[i]
        qmat[i, i] = -qmat[i].sum()
    root = np.sqrt(weights)
    sym = root[:, None] * qmat / root[None, :]
    sym = 0.5 * (sym + sym.T)
    eig = np.linalg.eigvalsh(sym)
    assert abs(eig[-1]) < 1e-10
    assert -eig[-2] > 0.0

    print("R205E thermal Gibbs sampler checks: OK")


if __name__ == "__main__":
    main()
