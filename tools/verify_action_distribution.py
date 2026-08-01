#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import asdict, dataclass

import numpy as np


@dataclass
class CheckResult:
    name: str
    value: float
    threshold: float
    criterion: str
    passed: bool


def record_max(name: str, value: float, threshold: float) -> CheckResult:
    return CheckResult(
        name=name,
        value=float(value),
        threshold=float(threshold),
        criterion="<=",
        passed=bool(value <= threshold),
    )


def record_min(name: str, value: float, threshold: float) -> CheckResult:
    return CheckResult(
        name=name,
        value=float(value),
        threshold=float(threshold),
        criterion=">=",
        passed=bool(value >= threshold),
    )


def kolmogorov_smirnov_error(
    samples: np.ndarray,
    analytic_cdf,
) -> float:
    ordered = np.sort(samples)
    count = ordered.size
    upper = np.arange(1, count + 1) / count
    lower = np.arange(0, count) / count
    expected = analytic_cdf(ordered)
    return float(
        np.max(
            np.maximum(
                np.abs(upper - expected),
                np.abs(lower - expected),
            )
        )
    )


def main() -> None:
    seed = 20260802
    rng = np.random.default_rng(seed)
    sample_count = 600_000
    checks: list[CheckResult] = []

    # An orthogonal change applied to bath coordinates and momenta preserves
    # the canonical one-form.
    bath_dimension = 8
    orthogonal, _ = np.linalg.qr(
        rng.normal(size=(bath_dimension, bath_dimension))
    )
    canonical_count = 100_000
    momentum = rng.normal(size=(canonical_count, bath_dimension))
    coordinate_increment = rng.normal(
        size=(canonical_count, bath_dimension)
    )
    transformed_momentum = momentum @ orthogonal.T
    transformed_increment = coordinate_increment @ orthogonal.T
    direct_one_form = np.sum(momentum * coordinate_increment, axis=1)
    transformed_one_form = np.sum(
        transformed_momentum * transformed_increment,
        axis=1,
    )
    checks.append(
        record_max(
            "bath_canonical_one_form_error",
            np.max(np.abs(direct_one_form - transformed_one_form)),
            5.0e-14,
        )
    )

    # The momentum-coupled kinetic block is positive exactly when its
    # Schur complement is positive, and square completion preserves its
    # value. Simultaneous reversal of both momenta leaves it invariant.
    particle_dimension = 3
    momentum_bath_dimension = 5
    particle_mass = 1.7
    coupling = 0.08 * rng.normal(
        size=(particle_dimension, momentum_bath_dimension)
    )
    base = rng.normal(
        size=(momentum_bath_dimension, momentum_bath_dimension)
    )
    schur = base.T @ base + 0.4 * np.eye(momentum_bath_dimension)
    inverse_bath_mass = (
        schur + particle_mass * coupling.T @ coupling
    )
    kinetic_block = np.block([
        [
            np.eye(particle_dimension) / particle_mass,
            coupling,
        ],
        [coupling.T, inverse_bath_mass],
    ])
    checks.append(
        record_min(
            "momentum_coupling_block_min_eigenvalue",
            np.min(np.linalg.eigvalsh(kinetic_block)),
            1.0e-8,
        )
    )
    kinetic_count = 100_000
    particle_momentum = rng.normal(
        size=(kinetic_count, particle_dimension)
    )
    bath_momentum = rng.normal(
        size=(kinetic_count, momentum_bath_dimension)
    )
    stacked_momentum = np.concatenate(
        [particle_momentum, bath_momentum],
        axis=1,
    )
    direct_kinetic = 0.5 * np.einsum(
        "bi,ij,bj->b",
        stacked_momentum,
        kinetic_block,
        stacked_momentum,
    )
    shifted_particle = (
        particle_momentum
        + particle_mass * bath_momentum @ coupling.T
    )
    completed_kinetic = (
        0.5
        * np.sum(shifted_particle**2, axis=1)
        / particle_mass
        + 0.5
        * np.einsum(
            "bi,ij,bj->b",
            bath_momentum,
            schur,
            bath_momentum,
        )
    )
    checks.append(
        record_max(
            "momentum_coupling_square_completion_error",
            np.max(np.abs(direct_kinetic - completed_kinetic)),
            1.0e-12,
        )
    )
    reversed_kinetic = 0.5 * np.einsum(
        "bi,ij,bj->b",
        -stacked_momentum,
        kinetic_block,
        -stacked_momentum,
    )
    checks.append(
        record_max(
            "momentum_coupling_time_reversal_error",
            np.max(np.abs(direct_kinetic - reversed_kinetic)),
            1.0e-14,
        )
    )

    # For the canonical Gaussian bath, the exact free velocity covariance
    # reduces to Theta C cos[Omega(t-s)] C^T.
    covariance_dimension = 6
    covariance_particle_dimension = 2
    covariance_base = rng.normal(
        size=(covariance_dimension, covariance_dimension)
    )
    stiffness = (
        covariance_base.T @ covariance_base
        + 0.7 * np.eye(covariance_dimension)
    )
    eigenvalues, eigenvectors = np.linalg.eigh(stiffness)
    frequencies = np.sqrt(eigenvalues)
    covariance_coupling = 0.05 * rng.normal(
        size=(covariance_particle_dimension, covariance_dimension)
    )
    energy_scale = 1.3

    def spectral_function(values: np.ndarray) -> np.ndarray:
        return (eigenvectors * values) @ eigenvectors.T

    time_t = 0.73
    time_s = 0.21
    cosine_t = spectral_function(np.cos(frequencies * time_t))
    cosine_s = spectral_function(np.cos(frequencies * time_s))
    omega_sine_t = spectral_function(
        frequencies * np.sin(frequencies * time_t)
    )
    omega_sine_s = spectral_function(
        frequencies * np.sin(frequencies * time_s)
    )
    inverse_stiffness = spectral_function(1.0 / eigenvalues)
    coefficient_pi_t = covariance_coupling @ cosine_t
    coefficient_pi_s = covariance_coupling @ cosine_s
    coefficient_q_t = -covariance_coupling @ omega_sine_t
    coefficient_q_s = -covariance_coupling @ omega_sine_s
    covariance_direct = energy_scale * (
        coefficient_pi_t @ coefficient_pi_s.T
        + coefficient_q_t @ inverse_stiffness @ coefficient_q_s.T
    )
    covariance_expected = energy_scale * (
        covariance_coupling
        @ spectral_function(
            np.cos(frequencies * (time_t - time_s))
        )
        @ covariance_coupling.T
    )
    checks.append(
        record_max(
            "free_velocity_covariance_error",
            np.max(np.abs(covariance_direct - covariance_expected)),
            1.0e-12,
        )
    )

    # The static sum/difference basis preserves total action and reproduces
    # the direct quadratic definitions.
    geometry_count = 200_000
    u_a = rng.normal(size=(geometry_count, 2))
    u_b = rng.normal(size=(geometry_count, 2))
    plus_direct = 0.25 * np.sum((u_a + u_b) ** 2, axis=1)
    minus_direct = 0.25 * np.sum((u_a - u_b) ** 2, axis=1)
    input_action = 0.5 * (
        np.sum(u_a**2, axis=1) + np.sum(u_b**2, axis=1)
    )
    action_error = np.max(
        np.abs(plus_direct + minus_direct - input_action)
    )
    checks.append(
        record_max("sum_difference_action_error", action_error, 2.0e-14)
    )

    # Haar sampling on S^5: squared complex component moduli are
    # Dirichlet(1,1,1), so J_+/C has Beta(1,2) CDF 1-(1-x)^2.
    sphere = rng.normal(size=(sample_count, 6))
    sphere /= np.linalg.norm(sphere, axis=1, keepdims=True)
    j_plus_fraction = sphere[:, 0] ** 2 + sphere[:, 1] ** 2
    shell_ks = kolmogorov_smirnov_error(
        j_plus_fraction,
        lambda x: 1.0 - (1.0 - x) ** 2,
    )
    checks.append(record_max("s5_jplus_beta_ks", shell_ks, 0.0030))

    # Conditional on J_+, U(2) isotropy makes the split between the two
    # residual complex modes uniform.
    j_soft = sphere[:, 2] ** 2 + sphere[:, 3] ** 2
    j_residual = sphere[:, 4] ** 2 + sphere[:, 5] ** 2
    residual_fraction = j_soft / (j_soft + j_residual)
    residual_ks = kolmogorov_smirnov_error(
        residual_fraction,
        lambda x: x,
    )
    checks.append(
        record_max("residual_u2_uniform_ks", residual_ks, 0.0030)
    )

    # U(2) invariance leaves an arbitrary f(J_+) factor. Verify the exact
    # weight formula and require a visible departure from the bare shell
    # weights for a nonconstant f.
    shell_action = 2.4
    x_grid = np.linspace(0.2 * shell_action, 0.8 * shell_action, 9)
    arbitrary_factor = 1.0 + 0.6 * x_grid / shell_action
    bare_weights = shell_action - x_grid
    modified_weights = arbitrary_factor * bare_weights
    recovered_factor = modified_weights / bare_weights
    checks.append(
        record_max(
            "u2_counterexample_formula_error",
            np.max(np.abs(recovered_factor - arbitrary_factor)),
            1.0e-14,
        )
    )
    normalized_bare = bare_weights / bare_weights.sum()
    normalized_modified = modified_weights / modified_weights.sum()
    u2_distortion = np.max(
        np.abs(normalized_modified - normalized_bare)
    )
    checks.append(
        record_min(
            "u2_insufficiency_distortion_guard",
            u2_distortion,
            0.01,
        )
    )

    # Monte Carlo fiber length versus the analytic Bell joint law.
    # After the shell delta constraint, one residual action ranges over
    # [0, C0-I_+], so a common uniform coordinate estimates the fiber length.
    baseline_action = 0.4
    source_action = 1.0
    visibility = 0.86
    total_action = baseline_action + 2.0 * source_action
    residual_coordinate = rng.uniform(
        0.0,
        total_action,
        size=sample_count,
    )
    angle_grid = np.linspace(-np.pi, np.pi, 13)
    signs = np.array([-1.0, 1.0])
    max_probability_error = 0.0
    max_marginal_error = 0.0
    effective_visibility = (
        source_action
        * visibility
        / (baseline_action + source_action)
    )
    for angle in angle_grid:
        raw = np.empty((2, 2))
        expected = np.empty((2, 2))
        for i, a_sign in enumerate(signs):
            for j, b_sign in enumerate(signs):
                residual_action = baseline_action + source_action * (
                    1.0
                    - a_sign
                    * b_sign
                    * visibility
                    * np.cos(angle)
                )
                raw[i, j] = (
                    np.mean(residual_coordinate <= residual_action) / 4.0
                )
                expected[i, j] = 0.25 * (
                    1.0
                    - a_sign
                    * b_sign
                    * effective_visibility
                    * np.cos(angle)
                )
        estimated = raw / raw.sum()
        max_probability_error = max(
            max_probability_error,
            float(np.max(np.abs(estimated - expected))),
        )
        max_marginal_error = max(
            max_marginal_error,
            float(np.max(np.abs(estimated.sum(axis=0) - 0.5))),
            float(np.max(np.abs(estimated.sum(axis=1) - 0.5))),
        )
    checks.append(
        record_max(
            "bell_fiber_probability_max_error",
            max_probability_error,
            0.0025,
        )
    )
    checks.append(
        record_max(
            "no_signalling_marginal_error",
            max_marginal_error,
            0.0025,
        )
    )

    # A symmetric narrow radial shell changes the mean linear fiber weight
    # only through sampling error; nonlinear observables would receive width
    # corrections.
    radial_count = 400_000
    radial_sigma = 0.03 * total_action
    radial_action = rng.normal(
        total_action,
        radial_sigma,
        size=radial_count,
    )
    target_plus_actions = np.linspace(
        0.25 * total_action,
        0.75 * total_action,
        7,
    )
    radial_error = max(
        abs(
            np.mean(radial_action - target)
            - (total_action - target)
        )
        for target in target_plus_actions
    )
    checks.append(
        record_max("radial_shell_linear_mean_error", radial_error, 5.0e-4)
    )

    # CHSH identity for the analytic cosine law.
    chsh = 2.0 * np.sqrt(2.0) * effective_visibility
    chsh_direct = sum(
        coefficient * (-effective_visibility * np.cos(angle))
        for coefficient, angle in (
            (1.0, -np.pi / 4.0),
            (1.0, np.pi / 4.0),
            (1.0, np.pi / 4.0),
            (-1.0, 3.0 * np.pi / 4.0),
        )
    )
    checks.append(
        record_max(
            "chsh_identity_error",
            abs(abs(chsh_direct) - chsh),
            1.0e-14,
        )
    )

    payload = {
        "seed": seed,
        "sample_count": sample_count,
        "all_passed": all(item.passed for item in checks),
        "checks": [asdict(item) for item in checks],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if not payload["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
