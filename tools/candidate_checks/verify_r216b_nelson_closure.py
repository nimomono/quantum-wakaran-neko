#!/usr/bin/env python3
from __future__ import annotations

import math
import numpy as np


def main() -> None:
    length = 2.0 * math.pi
    n = 8192
    x = np.linspace(0.0, length, n, endpoint=False)
    dx = length / n
    modes = 2.0 * math.pi * np.fft.fftfreq(n, d=dx)

    def deriv(f, order=1):
        return np.real(np.fft.ifft((1j * modes) ** order * np.fft.fft(f)))

    nu = 0.31
    mx = 0.73
    pi = (1.0 + 0.21 * np.cos(x) + 0.05 * np.cos(2.0 * x)) / length
    root = np.sqrt(pi)
    u = nu * deriv(np.log(pi))
    score_term = u * deriv(u) + nu * deriv(u, 2)
    qgrad = 2.0 * nu**2 * deriv(deriv(root, 2) / root)
    identity = float(np.max(np.abs(score_term - qgrad)))
    assert identity < 2e-8, identity

    v = 0.19 * np.cos(x) - 0.07 * np.cos(3.0 * x)
    vx = deriv(v)

    mmed = mx
    medium_acc = -vx / mmed + (mx / mmed) * qgrad
    nelson_acc = medium_acc - score_term
    equal_res = float(np.max(np.abs(mx * nelson_acc + vx)))
    assert equal_res < 2e-8, equal_res

    mismatch = 1.17 * mx
    medium_acc_m = -vx / mismatch + (mx / mismatch) * qgrad
    nelson_m = medium_acc_m - score_term
    predicted = -vx / mismatch + (mx / mismatch - 1.0) * qgrad
    mismatch_res = float(np.max(np.abs(nelson_m - predicted)))
    assert mismatch_res < 2e-8, mismatch_res
    assert float(np.max(np.abs(nelson_m + vx / mismatch))) > 1e-4

    print(
        "r216b_nelson_ok "
        f"score_identity={identity:.3e} "
        f"equal_mass_residual={equal_res:.3e} "
        f"mismatch_formula={mismatch_res:.3e}"
    )


if __name__ == "__main__":
    main()
