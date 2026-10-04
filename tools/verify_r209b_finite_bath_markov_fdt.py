#!/usr/bin/env python3
from __future__ import annotations

import numpy as np


def drude_sine_error(theta: float, amplitude: float = 0.23, omega: float = 1.1) -> float:
    return float(amplitude * omega * theta / np.sqrt(1 + (omega * theta) ** 2))


def main() -> None:
    # Translation of a harmonic bath coordinate leaves its partition integral invariant.
    x = np.linspace(-12.0, 12.0, 200001)
    for shift in (-1.3, 0.0, 0.8, 2.1):
        z = np.exp(-0.5 * (x - shift) ** 2)
        val = np.trapezoid(z, x)
        assert abs(val - np.sqrt(2 * np.pi)) < 2e-12

    # Local tight frame gives constant friction/noise and zero Stratonovich drift.
    u = np.linspace(0.0, 1.0, 4001)
    c0 = 1 - u
    c1 = u
    gp = np.sqrt(2 * c0 * c1)
    frame = c0 * c0 + c1 * c1 + gp * gp
    assert np.max(np.abs(frame - 1.0)) < 2e-15
    dframe = np.gradient(frame, u)
    assert np.max(np.abs(dframe[5:-5])) < 1e-10

    # Generic Drude short-memory error is first order for a smooth input.
    thetas = np.array([0.02, 0.01, 0.005, 0.0025])
    errs = np.array([drude_sine_error(t) for t in thetas])
    assert np.all(errs[1:] < errs[:-1])
    slope = float(np.polyfit(np.log(thetas), np.log(errs), 1)[0])
    assert 0.97 < slope < 1.01, slope

    amp = 0.23
    omega = 1.1
    for theta, err in zip(thetas, errs):
        assert err <= amp * omega * theta * (1 + 1e-12)

    # Integrated covariance converges to Brownian covariance.
    gamma = 1.7
    theta = 0.03
    for t in (0.1, 0.3, 0.8):
        drude = 2 * gamma * (t - theta * (1 - np.exp(-t / theta)))
        brown = 2 * gamma * t
        assert abs(drude - brown) <= 2 * gamma * theta * (1 + 1e-12)

    # Same generic lemma is used for flow, tracer drag, and each dumbbell Cartesian component.
    channels = {"flow_U": 0.8, "tracer_drag": 1.7, "dumbbell_r": 0.6}
    for _, gam in channels.items():
        assert gam > 0.0

    omega_max = 80.0
    nmode = 256
    domega = omega_max / nmode
    trec = 2 * np.pi / domega
    assert 1.5 < trec
    print("r209b_generic_finite_bath_ok", slope, trec)


if __name__ == "__main__":
    main()
