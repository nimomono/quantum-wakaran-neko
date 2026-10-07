#!/usr/bin/env python3
from __future__ import annotations

import math
import numpy as np


def main() -> None:
    length = 2.0 * math.pi
    n = 32768
    x = np.linspace(0.0, length, n, endpoint=False)
    dx_grid = length / n
    modes = 2.0 * math.pi * np.fft.fftfreq(n, d=dx_grid)

    mass = 0.7
    nu = 0.4
    j_si = 2.0 * mass * nu
    k = 2.0
    c0 = math.sqrt(0.8)
    c1 = math.sqrt(0.2)
    omega = j_si * k * k / (2.0 * mass)

    def deriv(f: np.ndarray, order: int = 1) -> np.ndarray:
        return np.fft.ifft((1j * modes) ** order * np.fft.fft(f))

    def integral(f: np.ndarray) -> float:
        return float(np.real(np.mean(f)) * length)

    def fields(t: float):
        phase = k * x - omega * t
        psi = (c0 + c1 * np.exp(1j * phase)) / math.sqrt(length)
        psi_t = (-1j * omega * c1 * np.exp(1j * phase)) / math.sqrt(length)
        psi_x = deriv(psi)
        psi_xx = deriv(psi, 2)

        pi = np.abs(psi) ** 2
        pi_t = 2.0 * np.real(np.conj(psi) * psi_t)
        current = (j_si / mass) * np.imag(np.conj(psi) * psi_x)
        flow = current / pi

        root = np.sqrt(pi)
        root_x = np.real(deriv(root))
        root_xx = np.real(deriv(root, 2))
        root_xxx = np.real(deriv(root, 3))
        mu_si = -2.0 * mass * nu**2 * root_xx / root

        return psi, psi_t, psi_x, psi_xx, pi, pi_t, flow, root, root_x, root_xx, root_xxx, mu_si

    t = 0.37
    psi, psi_t, psi_x, psi_xx, pi, pi_t, flow, root, root_x, root_xx, root_xxx, mu_si = fields(t)

    assert float(np.min(pi)) > 2.0e-2
    assert abs(integral(pi) - 1.0) < 2.0e-12

    continuity = pi_t + np.real(deriv(pi * flow))
    assert float(np.max(np.abs(continuity))) < 2.0e-7
    assert abs(integral(flow)) < 2.0e-10

    s_x = mass * flow
    s_t = j_si * np.imag(psi_t / psi)
    hj_residual = s_t + s_x**2 / (2.0 * mass) + mu_si
    assert float(np.max(np.abs(hj_residual))) < 2.0e-7

    force = -pi * np.real(deriv(mu_si))
    sigma = 2.0 * mass * nu**2 * (root * root_xx - root_x**2)
    sigma_x = np.real(deriv(sigma))
    assert float(np.max(np.abs(force - sigma_x))) < 2.0e-6

    force_explicit = 2.0 * mass * nu**2 * (root * root_xxx - root_x * root_xx)
    assert float(np.max(np.abs(force - force_explicit))) < 2.0e-6

    f_si = 2.0 * mass * nu**2 * integral(root_x**2)
    flow_ke = 0.5 * mass * integral(pi * flow**2)
    quantum_ke = (j_si**2 / (2.0 * mass)) * integral(np.abs(psi_x) ** 2)
    assert abs(flow_ke + f_si - quantum_ke) < 2.0e-10

    _, _, psi_x2, _, pi2, _, flow2, _, root_x2, _, _, _ = fields(t + 0.31)
    f_si2 = 2.0 * mass * nu**2 * integral(root_x2**2)
    flow_ke2 = 0.5 * mass * integral(pi2 * flow2**2)
    energy_drift = abs((flow_ke2 + f_si2) - (flow_ke + f_si))
    assert energy_drift < 2.0e-10
    quantum_ke2 = (j_si**2 / (2.0 * mass)) * integral(np.abs(psi_x2) ** 2)
    assert abs(quantum_ke2 - quantum_ke) < 2.0e-10

    schr_residual = 1j * j_si * psi_t + (j_si**2 / (2.0 * mass)) * psi_xx
    assert float(np.max(np.abs(schr_residual))) < 2.0e-7

    print(
        "r215c_candidate_ok "
        f"min_pi={np.min(pi):.6e} "
        f"continuity={np.max(np.abs(continuity)):.6e} "
        f"stress={np.max(np.abs(force-sigma_x)):.6e} "
        f"hj={np.max(np.abs(hj_residual)):.6e} "
        f"energy_drift={energy_drift:.6e}"
    )


if __name__ == "__main__":
    main()
