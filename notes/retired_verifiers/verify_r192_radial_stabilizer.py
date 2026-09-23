#!/usr/bin/env python3
from __future__ import annotations

import numpy as np

TOL = 5.0e-11


def exact_action(s0: float, s_star: float, gain: float, tau: float) -> float:
    return s_star / (1.0 + (s_star / s0 - 1.0) * np.exp(-2.0 * gain * s_star * tau))


def main() -> None:
    rng = np.random.default_rng(20260912)
    dimension = 16
    z0 = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
    z0 /= np.linalg.norm(z0)
    s_star = 1.7
    gain = 0.83
    tau = 2.4

    failures: list[str] = []

    for s0 in (0.08, 0.31, 1.0, 1.7, 2.8):
        s = exact_action(s0, s_star, gain, tau)
        z_in = np.sqrt(s0) * z0
        z_out = np.sqrt(s / s0) * z_in
        ray_error = np.linalg.norm(
            z_out / np.linalg.norm(z_out) - z_in / np.linalg.norm(z_in)
        )
        action_error = abs(float(np.vdot(z_out, z_out).real) - s)
        if ray_error > TOL:
            failures.append(f"ray preservation s0={s0}: {ray_error}")
        if action_error > TOL:
            failures.append(f"action formula s0={s0}: {action_error}")

    low = exact_action(0.31, s_star, gain, tau)
    high = exact_action(2.8, s_star, gain, tau)
    if not (0.31 < low < s_star):
        failures.append("sub-target action is not monotone increasing")
    if not (s_star < high < 2.8):
        failures.append("super-target action is not monotone decreasing")

    s_min = 0.12 * s_star
    eta = 2.0e-3
    tau_bound = np.log((s_star / s_min - 1.0) / eta) / (2.0 * gain * s_star)
    grid = np.linspace(s_min, s_star, 257)
    deficits = np.array([1.0 - exact_action(x, s_star, gain, tau_bound) / s_star for x in grid])
    if float(np.max(deficits)) > eta + 5.0e-13:
        failures.append("uniform finite-time bound failed")

    phase = np.exp(1j * 0.731)
    s = exact_action(0.42, s_star, gain, tau)
    z_a = np.sqrt(s / 0.42) * (np.sqrt(0.42) * z0)
    z_b = np.sqrt(s / 0.42) * (phase * np.sqrt(0.42) * z0)
    if np.linalg.norm(z_b - phase * z_a) > TOL:
        failures.append("global phase covariance failed")

    # A projector-selected component remains in the same projector image.
    projector = np.zeros((dimension, dimension), dtype=complex)
    projector[:5, :5] = np.eye(5)
    selected = projector @ (rng.normal(size=dimension) + 1j * rng.normal(size=dimension))
    selected_action = float(np.vdot(selected, selected).real)
    target = 2.1
    selected_final = exact_action(selected_action, target, 0.55, 0.7)
    stabilized = np.sqrt(selected_final / selected_action) * selected
    image_error = np.linalg.norm((np.eye(dimension) - projector) @ stabilized)
    if image_error > TOL:
        failures.append(f"projector image changed: {image_error}")

    # Zero action is not rescued by the model; it remains outside the theorem domain.
    if exact_action(1.0e-15, s_star, gain, tau) <= 0.0:
        failures.append("positive seed should remain positive")

    if failures:
        raise SystemExit("\n".join(failures))
    print("r192_radial_stabilizer_ok")


if __name__ == "__main__":
    main()
