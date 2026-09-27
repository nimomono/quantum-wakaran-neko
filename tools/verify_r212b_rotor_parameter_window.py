#!/usr/bin/env python3
"""Required regression for the R212B S^2 rotor parameter window.

This check is intentionally lightweight. It verifies one explicit finite
parameter point for the R207 choice eta=1/4, epsilon=eta/8, k=2/eta, together
with a finite Drude-mode discretization. The direct S^2 x S^2 mixing witness
lives in simulations/m67/run_r212b_rotor_mixing_witness.py.
"""

import math
import numpy as np


def langevin_function(k: float) -> float:
    return 1.0 / math.tanh(k) - 1.0 / k


def main() -> None:
    eta = 0.25
    epsilon = eta / 8.0
    k = 2.0 / eta

    kT = 1.0
    gamma = 1.0
    inertia = 0.01
    theta_b = 5.0e-4
    t_mix = 12.0
    t_prep = 15.0
    target_recurrence = 100.0
    omega_max = 4.0e4

    tau_i = inertia / gamma
    D_rot = kT / gamma
    Lk = langevin_function(k)
    r207_error = 2.0 * epsilon + 0.5 * (1.0 - Lk)

    assert r207_error < eta / 2.0
    assert theta_b / tau_i <= 0.05 + 1e-15
    assert tau_i < t_mix < t_prep < target_recurrence
    assert 1.0 / (D_rot * k) > 10.0 * tau_i

    delta_omega = 2.0 * math.pi / target_recurrence
    n_bath = math.ceil(omega_max / delta_omega)
    omega = (np.arange(n_bath, dtype=float) + 0.5) * delta_omega
    weights = (2.0 * gamma / math.pi) * delta_omega / (
        1.0 + (omega * theta_b) ** 2
    )

    recurrence = 2.0 * math.pi / delta_omega
    retained_mass = float(np.sum(weights))
    continuum_mass_to_cutoff = (
        2.0 * gamma / (math.pi * theta_b)
    ) * math.atan(omega_max * theta_b)

    assert n_bath == 636620
    assert abs(recurrence - 100.0) < 1e-12
    assert abs(retained_mass - continuum_mass_to_cutoff) < 5e-5
    assert continuum_mass_to_cutoff / (gamma / theta_b) > 0.968

    for multiple, tolerance in ((1.0, 0.01), (2.0, 0.01)):
        t = multiple * theta_b
        finite_kernel = float(np.dot(weights, np.cos(omega * t)))
        drude_kernel = gamma / theta_b * math.exp(-t / theta_b)
        rel = abs(finite_kernel - drude_kernel) / drude_kernel
        assert rel < tolerance, (
            multiple,
            finite_kernel,
            drude_kernel,
            rel,
        )

    print(
        "r212b_rotor_parameter_window_ok",
        f"eta={eta}",
        f"epsilon={epsilon}",
        f"k={k}",
        f"r207_error={r207_error:.9g}",
        f"theta_B={theta_b}",
        f"I_over_gamma={tau_i}",
        f"t_mix={t_mix}",
        f"T_prep={t_prep}",
        f"T_rec={recurrence}",
        f"N_B={n_bath}",
    )


if __name__ == "__main__":
    main()
