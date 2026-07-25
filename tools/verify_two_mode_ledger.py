#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import asdict, dataclass

import numpy as np


@dataclass
class CheckResult:
    name: str
    value: float
    tolerance: float
    passed: bool


def record(name: str, value: float, tolerance: float) -> CheckResult:
    return CheckResult(
        name=name,
        value=float(value),
        tolerance=float(tolerance),
        passed=bool(value <= tolerance),
    )


def main() -> None:
    rng = np.random.default_rng(20260724)
    sample_count = 600_000
    checks: list[CheckResult] = []

    # Isotropic S^3 sampling gives J_s / (J_s + J_0) ~ Uniform[0, 1].
    sphere = rng.normal(size=(sample_count, 4))
    sphere /= np.linalg.norm(sphere, axis=1, keepdims=True)
    h_fraction = sphere[:, 0] ** 2 + sphere[:, 1] ** 2
    ordered = np.sort(h_fraction)
    empirical = np.arange(1, sample_count + 1) / sample_count
    ks_error = np.max(
        np.maximum(
            np.abs(empirical - ordered),
            np.abs((empirical - 1 / sample_count) - ordered),
        )
    )
    checks.append(record("two_mode_uniform_ks", ks_error, 0.0030))

    # Direct quadratic geometry versus the analytic difference-action formula.
    geometry_count = 200_000
    theta_a = rng.uniform(-np.pi, np.pi, geometry_count)
    theta_b = rng.uniform(-np.pi, np.pi, geometry_count)
    radius_a = rng.uniform(0.2, 2.0, geometry_count)
    radius_b = rng.uniform(0.2, 2.0, geometry_count)
    sign_a = rng.choice(np.array([-1.0, 1.0]), geometry_count)
    sign_b = rng.choice(np.array([-1.0, 1.0]), geometry_count)
    u_a = np.column_stack(
        (sign_a * radius_a * np.cos(theta_a), sign_a * radius_a * np.sin(theta_a))
    )
    u_b = np.column_stack(
        (sign_b * radius_b * np.cos(theta_b), sign_b * radius_b * np.sin(theta_b))
    )
    direct_action = 0.25 * np.sum((u_a - u_b) ** 2, axis=1)
    analytic_action = 0.25 * (
        radius_a**2
        + radius_b**2
        - 2
        * sign_a
        * sign_b
        * radius_a
        * radius_b
        * np.cos(theta_a - theta_b)
    )
    geometry_error = np.max(np.abs(direct_action - analytic_action))
    checks.append(record("difference_action_max_error", geometry_error, 2.0e-14))

    # The center-relative clock transformation preserves the canonical one-form.
    clock_count = 200_000
    rho_a = rng.normal(size=clock_count)
    rho_b = rng.normal(size=clock_count)
    d_tau_a = rng.normal(size=clock_count)
    d_tau_b = rng.normal(size=clock_count)
    p_center = rho_a + rho_b
    pi_relative = 0.5 * (rho_a - rho_b)
    d_tau_center = 0.5 * (d_tau_a + d_tau_b)
    d_y_relative = d_tau_a - d_tau_b
    one_form_direct = rho_a * d_tau_a + rho_b * d_tau_b
    one_form_transformed = (
        p_center * d_tau_center + pi_relative * d_y_relative
    )
    canonical_error = np.max(np.abs(one_form_direct - one_form_transformed))
    checks.append(record("clock_canonical_one_form_error", canonical_error, 2.0e-14))

    # The corrected finite-width comparator readout remains exact while Y_R drifts.
    pulse_count = 5_000
    pulse_steps = 1_024
    pulse_dt = 1.0 / pulse_steps
    pulse_h = rng.uniform(0.0, 4.0, size=pulse_count)
    pulse_action = rng.uniform(0.0, 3.0, size=pulse_count)
    pulse_coupling = 0.8
    pulse_mass = 1.7
    initial_pi = rng.uniform(0.1, 1.0, size=pulse_count)
    pulse_pi = initial_pi.copy()
    pulse_y = rng.normal(size=pulse_count)
    for step in range(pulse_steps):
        midpoint = (step + 0.5) * pulse_dt
        pulse_profile = 2.0 * np.sin(np.pi * midpoint) ** 2
        pulse_pi += (
            pulse_dt
            * pulse_profile
            * (pulse_coupling * pulse_action - pulse_h)
        )
        pulse_y += pulse_dt * 2.0 * pulse_pi / pulse_mass
    expected_pi = initial_pi + pulse_coupling * pulse_action - pulse_h
    comparator_error = np.max(np.abs(pulse_pi - expected_pi))
    checks.append(
        record(
            "finite_pulse_comparator_with_y_drift_error",
            comparator_error,
            2.0e-12,
        )
    )

    # On P_c = 0, the terminal half-space is exactly ordered clock orientation.
    clock_h = rng.uniform(0.0, 4.0, size=clock_count)
    clock_action = rng.uniform(0.0, 3.0, size=clock_count)
    clock_margin = 0.35
    clock_coupling = 0.8
    final_pi = clock_margin + clock_coupling * clock_action - clock_h
    final_rho_a = final_pi
    final_rho_b = -final_pi
    half_space = final_pi >= 0.0
    ordered_orientation = (final_rho_a >= 0.0) & (final_rho_b <= 0.0)
    orientation_error = np.mean(half_space != ordered_orientation)
    checks.append(record("clock_orientation_equivalence_error", orientation_error, 0.0))

    # Naively averaging the two complementary half-spaces removes x-dependence.
    orientation_x = np.linspace(0.0, 4.0, 1001)
    f_plus = orientation_x / 4.0
    f_minus = 1.0 - f_plus
    orientation_average_error = np.max(
        np.abs(0.5 * (f_plus + f_minus) - 0.5)
    )
    checks.append(
        record("orientation_average_nogo_error", orientation_average_error, 1.0e-15)
    )

    # Monte Carlo terminal compatibility versus the analytic Bell joint law.
    energy_shell = 4.0
    baseline = 0.35
    coupling = 0.8
    action = 1.0
    visibility = 0.86
    angle_grid = np.linspace(-np.pi, np.pi, 13)
    signs = np.array([-1.0, 1.0])
    max_probability_error = 0.0
    max_marginal_error = 0.0
    for angle in angle_grid:
        raw = np.empty((2, 2))
        for i, a_sign in enumerate(signs):
            for j, b_sign in enumerate(signs):
                threshold = baseline + coupling * action * (
                    1 - a_sign * b_sign * visibility * np.cos(angle)
                )
                accepted = h_fraction * energy_shell <= threshold
                raw[i, j] = accepted.mean() / 4
        estimated = raw / raw.sum()
        effective_visibility = coupling * action * visibility / (
            baseline + coupling * action
        )
        expected = np.empty((2, 2))
        for i, a_sign in enumerate(signs):
            for j, b_sign in enumerate(signs):
                expected[i, j] = 0.25 * (
                    1
                    - a_sign
                    * b_sign
                    * effective_visibility
                    * np.cos(angle)
                )
        max_probability_error = max(
            max_probability_error, np.max(np.abs(estimated - expected))
        )
        max_marginal_error = max(
            max_marginal_error,
            np.max(np.abs(estimated.sum(axis=0) - 0.5)),
            np.max(np.abs(estimated.sum(axis=1) - 0.5)),
        )
    checks.append(record("bell_probability_max_error", max_probability_error, 0.0025))
    checks.append(record("no_signalling_marginal_error", max_marginal_error, 0.0025))

    # N ledger modes give a Beta(1, N) soft fraction and nonlinear CDF.
    ledger_mode_count = 4
    exponentials = rng.exponential(
        scale=1.0, size=(sample_count, ledger_mode_count + 1)
    )
    simplex = exponentials / exponentials.sum(axis=1, keepdims=True)
    soft = simplex[:, 0]
    x_grid = np.linspace(0.05, 0.95, 19)
    empirical_cdf = np.array([(soft <= x).mean() for x in x_grid])
    expected_cdf = 1 - (1 - x_grid) ** ledger_mode_count
    multimode_error = np.max(np.abs(empirical_cdf - expected_cdf))
    checks.append(record("multimode_cdf_max_error", multimode_error, 0.0025))

    # CHSH value from the analytic joint law.
    effective_visibility = coupling * action * visibility / (
        baseline + coupling * action
    )
    chsh = 2 * np.sqrt(2) * effective_visibility
    chsh_direct = sum(
        coefficient * (-effective_visibility * np.cos(angle))
        for coefficient, angle in (
            (1, -np.pi / 4),
            (1, np.pi / 4),
            (1, np.pi / 4),
            (-1, 3 * np.pi / 4),
        )
    )
    checks.append(record("chsh_identity_error", abs(abs(chsh_direct) - chsh), 1.0e-14))

    payload = {
        "seed": 20260724,
        "sample_count": sample_count,
        "all_passed": all(item.passed for item in checks),
        "checks": [asdict(item) for item in checks],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if not payload["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
