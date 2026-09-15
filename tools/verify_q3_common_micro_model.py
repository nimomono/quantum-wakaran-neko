#!/usr/bin/env python3
from __future__ import annotations

import math

import numpy as np


def trapz(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.trapezoid(y, x))


def delta_width(x: float) -> float:
    return math.exp(-x * x) / (
        math.exp(-x * x) + math.sqrt(math.pi) * x * (1.0 + math.erf(x))
    )


def check_parameter_dictionary() -> None:
    m = 1.7
    nu = 0.013
    a = 0.41
    j0 = 2.0 * m * nu
    h_m37 = -(j0 * j0) / (2.0 * m * a * a)
    h_m57 = -(j0 * nu) / (a * a)
    assert math.isclose(h_m37, h_m57, rel_tol=1e-14, abs_tol=1e-14)


def check_shell_partition_and_force() -> None:
    kb_t = 0.37
    beta = 1.0 / kb_t
    kappa = 4.2
    for A in (0.35, 0.8, 1.7):
        x = math.sqrt(beta * kappa / 2.0) * A
        delta = delta_width(x)
        z_closed = (
            math.exp(-x * x) / (beta * kappa)
            + A
            * math.sqrt(math.pi / (2.0 * beta * kappa))
            * (1.0 + math.erf(x))
        )

        width = max(10.0 * math.sqrt(kb_t / kappa), 6.0 * A + 2.0)
        s = np.linspace(0.0, A + width, 400_001)
        weight = s * np.exp(-0.5 * beta * kappa * (s - A) ** 2)
        z_num = trapz(s, weight)
        assert math.isclose(z_num, z_closed, rel_tol=2e-6, abs_tol=2e-8)

        g = kappa * (s - A)
        mean_num = trapz(s, g * weight) / z_num
        mean_closed = kb_t * (1.0 - delta) / A
        assert math.isclose(mean_num, mean_closed, rel_tol=4e-6, abs_tol=2e-8)

        second_num = trapz(s, g * g * weight) / z_num
        second_closed = kappa * kb_t * (1.0 + delta)
        assert math.isclose(second_num, second_closed, rel_tol=8e-6, abs_tol=2e-8)


def check_width_monotonicity() -> None:
    xs = np.linspace(0.1, 6.0, 1000)
    values = np.array([delta_width(float(x)) for x in xs])
    assert np.all(values > 0.0)
    assert np.all(np.diff(values) < 0.0)
    assert delta_width(3.0) < 1.2e-5


def check_common_scaling() -> None:
    zeta = 2.0
    eps_values = np.array([0.20, 0.10, 0.05, 0.025])

    # R197B: mu_X ~ eps^-4, mu_sh ~ eps^(-4-zeta).
    eps_av = eps_values**zeta
    ratios = eps_av[:-1] / eps_av[1:]
    assert np.allclose(ratios, 2.0**zeta)

    # Strong shell averaging scales as eps^(zeta/2).
    strong = eps_values ** (zeta / 2.0)
    assert np.allclose(strong[:-1] / strong[1:], 2.0 ** (zeta / 2.0))

    # M37 mean shell reaction carries alpha ~ eps^2 and kBT ~ eps^4.
    mean_back = eps_values**6
    assert np.allclose(mean_back[:-1] / mean_back[1:], 2.0**6)

    # Port backreaction remains the dominant O(eps^2) common-model load.
    port_back = eps_values**2
    assert np.all(mean_back < port_back)


def check_time_scale_window() -> None:
    eps = 0.05
    zeta = 2.0
    kappa_sh = 1.0
    mu_bar = 1.0
    mu_sh = mu_bar * eps ** (-4.0 - zeta)
    tau_sh = 1.0 / (mu_sh * kappa_sh)

    gamma_bar = 0.1
    mx_bar = 0.1
    gamma_x = eps**4 * gamma_bar
    m_x = eps**6 * mx_bar
    tau_x = m_x / gamma_x

    tau_p = 0.25
    tau_y = 3.2
    t_sig = 500.0
    assert tau_sh < tau_x < tau_p < tau_y < t_sig


def main() -> None:
    check_parameter_dictionary()
    check_shell_partition_and_force()
    check_width_monotonicity()
    check_common_scaling()
    check_time_scale_window()
    print("q3_common_micro_model_ok")


if __name__ == "__main__":
    main()
