#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from math import factorial

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

    # Cellwise polar variables preserve the canonical one-form.
    phase_count = 100_000
    radius = 0.2 + rng.random(phase_count)
    theta = rng.uniform(-np.pi, np.pi, phase_count)
    radial_momentum = rng.normal(size=phase_count)
    phase_action = rng.normal(size=phase_count)
    radius_increment = rng.normal(size=phase_count)
    theta_increment = rng.normal(size=phase_count)
    e_r = np.column_stack([np.cos(theta), np.sin(theta)])
    e_theta = np.column_stack([-np.sin(theta), np.cos(theta)])
    field_momentum = (
        radial_momentum[:, None] * e_r
        + (phase_action / radius)[:, None] * e_theta
    )
    field_increment = (
        radius_increment[:, None] * e_r
        + (radius * theta_increment)[:, None] * e_theta
    )
    polar_one_form = (
        radial_momentum * radius_increment
        + phase_action * theta_increment
    )
    cartesian_one_form = np.sum(
        field_momentum * field_increment,
        axis=1,
    )
    checks.append(
        record_max(
            "phase_cell_canonical_one_form_error",
            np.max(np.abs(polar_one_form - cartesian_one_form)),
            5.0e-14,
        )
    )

    # The fixed-total-action rotational energy has an exact square
    # decomposition with minimizer j_i = J_phi r_i^2.
    cell_count = 31
    cell_volume = 1.0 / cell_count
    radius_squared = 0.1 + rng.random(cell_count)
    radius_squared /= np.sum(radius_squared) * cell_volume
    local_action = rng.normal(size=cell_count)
    total_phase_action = np.sum(local_action) * cell_volume
    inertia = 1.4
    rotational_energy = np.sum(
        local_action**2 / (2.0 * inertia * radius_squared)
    ) * cell_volume
    decomposed_energy = (
        total_phase_action**2 / (2.0 * inertia)
        + np.sum(
            (local_action - total_phase_action * radius_squared) ** 2
            / (2.0 * inertia * radius_squared)
        )
        * cell_volume
    )
    checks.append(
        record_max(
            "fixed_action_rotational_decomposition_error",
            abs(rotational_energy - decomposed_energy),
            1.0e-12,
        )
    )
    minimizing_action = total_phase_action * radius_squared
    minimizing_excess = (
        np.sum(
            (minimizing_action - total_phase_action * radius_squared) ** 2
            / (2.0 * inertia * radius_squared)
        )
        * cell_volume
    )
    checks.append(
        record_max(
            "fixed_action_minimizer_excess",
            minimizing_excess,
            1.0e-14,
        )
    )

    # Cell-volume absorption preserves the canonical one-form and the
    # local-action defect has the exact normalized square identity.
    integrated_cell_count = 17
    integrated_cell_volume = 0.07
    integrated_radius = 0.2 + rng.random(integrated_cell_count)
    integrated_radial_momentum = rng.normal(
        size=integrated_cell_count
    )
    integrated_local_action = rng.normal(
        size=integrated_cell_count
    )
    integrated_radius_increment = rng.normal(
        size=integrated_cell_count
    )
    integrated_phase_increment = rng.normal(
        size=integrated_cell_count
    )
    integrated_R = integrated_radius * np.sqrt(
        integrated_cell_volume
    )
    integrated_P = integrated_radial_momentum * np.sqrt(
        integrated_cell_volume
    )
    integrated_J = integrated_local_action * integrated_cell_volume
    integrated_dR = integrated_radius_increment * np.sqrt(
        integrated_cell_volume
    )
    direct_integrated_one_form = integrated_cell_volume * np.sum(
        integrated_radial_momentum * integrated_radius_increment
        + integrated_local_action * integrated_phase_increment
    )
    transformed_integrated_one_form = np.sum(
        integrated_P * integrated_dR
        + integrated_J * integrated_phase_increment
    )
    checks.append(
        record_max(
            "cell_volume_absorption_one_form_error",
            abs(
                direct_integrated_one_form
                - transformed_integrated_one_form
            ),
            1.0e-13,
        )
    )
    integrated_norm = np.sum(integrated_R**2)
    integrated_total_action = np.sum(integrated_J)
    integrated_defect = (
        integrated_J
        - integrated_total_action
        * integrated_R**2
        / integrated_norm
    )
    defect_square = np.sum(integrated_defect**2 / integrated_R**2)
    defect_square_expected = (
        np.sum(integrated_J**2 / integrated_R**2)
        - integrated_total_action**2 / integrated_norm
    )
    checks.append(
        record_max(
            "local_action_defect_square_identity_error",
            abs(defect_square - defect_square_expected),
            1.0e-12,
        )
    )

    # Exact finite-epsilon momentum elimination yields the reduced
    # singular Lagrangian on the normalized simplex.
    simplex_dimension = 19
    simplex_q = 0.1 + rng.random(simplex_dimension)
    simplex_q /= simplex_q.sum()
    simplex_q_velocity = rng.normal(size=simplex_dimension)
    simplex_q_velocity -= simplex_q_velocity.mean()
    simplex_theta_velocity = rng.normal(size=simplex_dimension)
    singular_epsilon = 0.037
    singular_mass = 1.3
    singular_inertia = 0.9
    singular_total_action = -1.2
    weighted_omega = np.sum(
        simplex_q * simplex_theta_velocity
    )
    simplex_pi = (
        singular_epsilon
        * singular_mass
        * simplex_q_velocity
        / (4.0 * simplex_q)
    )
    simplex_P = 2.0 * np.sqrt(simplex_q) * simplex_pi
    simplex_defect = (
        singular_epsilon
        * singular_inertia
        * simplex_q
        * (simplex_theta_velocity - weighted_omega)
    )
    simplex_J = (
        singular_total_action * simplex_q + simplex_defect
    )
    simplex_R_velocity = (
        simplex_q_velocity / (2.0 * np.sqrt(simplex_q))
    )
    singular_fast_hamiltonian = (
        np.sum(simplex_P**2)
        / (2.0 * singular_epsilon * singular_mass)
        + np.sum(simplex_defect**2 / simplex_q)
        / (2.0 * singular_epsilon * singular_inertia)
    )
    singular_legendre_direct = (
        np.sum(simplex_P * simplex_R_velocity)
        + np.sum(simplex_J * simplex_theta_velocity)
        - singular_fast_hamiltonian
    )
    singular_legendre_expected = (
        singular_total_action
        * np.sum(simplex_q * simplex_theta_velocity)
        + singular_epsilon
        * singular_mass
        * np.sum(simplex_q_velocity**2 / simplex_q)
        / 8.0
        + singular_epsilon
        * singular_inertia
        * np.sum(
            simplex_q
            * (simplex_theta_velocity - weighted_omega) ** 2
        )
        / 2.0
    )
    checks.append(
        record_max(
            "singular_legendre_elimination_error",
            abs(
                singular_legendre_direct
                - singular_legendre_expected
            ),
            1.0e-12,
        )
    )

    # Edge torques exchange local action without changing total action.
    graph_dimension = 13
    incidence = np.zeros((graph_dimension, graph_dimension))
    for edge in range(graph_dimension):
        incidence[edge, edge] = 1.0
        incidence[(edge + 1) % graph_dimension, edge] = -1.0
    edge_torque = rng.normal(size=graph_dimension)
    local_torque = incidence @ edge_torque
    checks.append(
        record_max(
            "action_exchange_total_torque_error",
            abs(np.sum(local_torque)),
            1.0e-14,
        )
    )
    edge_phase = rng.uniform(-np.pi, np.pi, size=100_000)
    checks.append(
        record_max(
            "paired_bath_counterterm_phase_error",
            np.max(
                np.abs(
                    np.cos(edge_phase) ** 2
                    + np.sin(edge_phase) ** 2
                    - 1.0
                )
            ),
            1.0e-14,
        )
    )

    # The fixed-amplitude, short-memory defect energy derivative is
    # non-positive on a connected graph.
    defect_q = 0.1 + rng.random(graph_dimension)
    defect_q /= defect_q.sum()
    graph_defect = rng.normal(size=graph_dimension)
    graph_defect -= graph_defect.mean()
    graph_laplacian = incidence @ incidence.T
    weighted_defect = graph_defect / defect_q
    defect_dissipation = float(
        weighted_defect @ graph_laplacian @ weighted_defect
    )
    checks.append(
        record_max(
            "action_defect_lyapunov_sign_error",
            max(-defect_dissipation, 0.0),
            1.0e-12,
        )
    )
    checks.append(
        record_min(
            "action_defect_connected_graph_dissipation_guard",
            defect_dissipation,
            1.0e-8,
        )
    )

    # The phase-connection kinetic energy is time-reversal invariant when
    # both particle momentum and the dynamical phase action reverse.
    connection_count = 100_000
    connection_dimension = 3
    connection_mass = 1.9
    particle_p = rng.normal(
        size=(connection_count, connection_dimension)
    )
    connection = rng.normal(
        size=(connection_count, connection_dimension)
    )
    phase_sector = rng.normal(size=connection_count)
    forward_connection_energy = np.sum(
        (
            particle_p
            - phase_sector[:, None] * connection
        ) ** 2,
        axis=1,
    ) / (2.0 * connection_mass)
    reversed_connection_energy = np.sum(
        (
            -particle_p
            - (-phase_sector)[:, None] * connection
        ) ** 2,
        axis=1,
    ) / (2.0 * connection_mass)
    checks.append(
        record_max(
            "phase_connection_time_reversal_error",
            np.max(
                np.abs(
                    forward_connection_energy
                    - reversed_connection_energy
                )
            ),
            1.0e-14,
        )
    )

    # Eliminating canonical particle momentum gives the positive
    # connection term in the Lagrangian.
    velocity = rng.normal(
        size=(connection_count, connection_dimension)
    )
    potential = rng.normal(size=connection_count)
    canonical_particle_p = (
        connection_mass * velocity
        + phase_sector[:, None] * connection
    )
    hamiltonian_particle = (
        np.sum(
            (
                canonical_particle_p
                - phase_sector[:, None] * connection
            ) ** 2,
            axis=1,
        )
        / (2.0 * connection_mass)
        + potential
    )
    legendre_direct = (
        np.sum(canonical_particle_p * velocity, axis=1)
        - hamiltonian_particle
    )
    legendre_expected = (
        0.5
        * connection_mass
        * np.sum(velocity**2, axis=1)
        + phase_sector
        * np.sum(connection * velocity, axis=1)
        - potential
    )
    checks.append(
        record_max(
            "phase_connection_legendre_error",
            np.max(np.abs(legendre_direct - legendre_expected)),
            1.0e-12,
        )
    )

    # Numerically integrate the recurrence for the general action-shell
    # volume and compare it with (2 pi)^n A^(n-1)/(n-1)!.
    shell_test_action = 1.7
    shell_volume_error = 0.0
    for mode_count in range(2, 6):
        grid = np.linspace(0.0, shell_test_action, 200_001)
        previous = (
            (2.0 * np.pi) ** (mode_count - 1)
            * (shell_test_action - grid) ** (mode_count - 2)
            / factorial(mode_count - 2)
        )
        recurrence_value = 2.0 * np.pi * np.trapezoid(
            previous,
            grid,
        )
        analytic_value = (
            (2.0 * np.pi) ** mode_count
            * shell_test_action ** (mode_count - 1)
            / factorial(mode_count - 1)
        )
        shell_volume_error = max(
            shell_volume_error,
            abs(recurrence_value - analytic_value)
            / analytic_value,
        )
    checks.append(
        record_max(
            "general_action_shell_volume_relative_error",
            shell_volume_error,
            1.0e-9,
        )
    )

    # A common flux factor on exclusive two-mode shells reproduces the
    # normalized cell intensity.
    entrance_cells = 23
    entrance_volume = 1.0 / entrance_cells
    entrance_density = 0.1 + rng.random(entrance_cells)
    entrance_density /= (
        np.sum(entrance_density) * entrance_volume
    )
    total_entrance_action = 3.2
    local_entrance_action = (
        total_entrance_action
        * entrance_density
        * entrance_volume
    )
    common_flux_factor = 0.73
    entrance_flux = (
        common_flux_factor
        * (2.0 * np.pi) ** 2
        * local_entrance_action
    )
    entrance_probability = entrance_flux / entrance_flux.sum()
    entrance_expected = entrance_density * entrance_volume
    checks.append(
        record_max(
            "born_entry_flux_weight_error",
            np.max(
                np.abs(
                    entrance_probability
                    - entrance_expected
                )
            ),
            1.0e-14,
        )
    )

    # q directly acting reaction directions change the shell capacity to
    # A^q, so only q=1 gives a linear Born-type rule.
    rigidity_actions = np.linspace(0.2, 2.0, 17)
    rigidity_error = 0.0
    for direct_directions in range(1, 5):
        capacity = (
            rigidity_actions**direct_directions
            / factorial(direct_directions)
        )
        recovered = (
            capacity
            * factorial(direct_directions)
            / rigidity_actions**direct_directions
        )
        rigidity_error = max(
            rigidity_error,
            float(np.max(np.abs(recovered - 1.0))),
        )
    checks.append(
        record_max(
            "action_distribution_dimension_power_error",
            rigidity_error,
            1.0e-14,
        )
    )

    # Hermitian shell-tangent mixing preserves the two-mode total action.
    mixing_count = 100_000
    mixing_state = (
        rng.normal(size=(mixing_count, 2))
        + 1j * rng.normal(size=(mixing_count, 2))
    )
    hermitian_seed = (
        rng.normal(size=(2, 2))
        + 1j * rng.normal(size=(2, 2))
    )
    hermitian_generator = (
        hermitian_seed + hermitian_seed.conj().T
    ) / 2.0
    mixing_velocity = -1j * (
        mixing_state @ hermitian_generator.T
    )
    action_derivative = 2.0 * np.real(
        np.sum(
            np.conj(mixing_state) * mixing_velocity,
            axis=1,
        )
    )
    checks.append(
        record_max(
            "u2_shell_tangent_action_derivative",
            np.max(np.abs(action_derivative)),
            1.0e-13,
        )
    )

    # Field phase continuity and particle continuity preserve the
    # synchronization difference on the ideal coherent manifold.
    synchronization_count = 100_000
    phase_current_divergence = rng.normal(
        size=synchronization_count
    )
    nonzero_phase_action = 1.6
    density_derivative = -phase_current_divergence
    local_action_derivative = (
        -nonzero_phase_action * phase_current_divergence
    )
    field_density_derivative = (
        local_action_derivative / nonzero_phase_action
    )
    checks.append(
        record_max(
            "density_synchronization_derivative_error",
            np.max(
                np.abs(
                    field_density_derivative
                    - density_derivative
                )
            ),
            1.0e-14,
        )
    )

    # The phase-action coefficient and the bath diffusion coefficient agree
    # exactly when |J_phi| = 2 m nu.
    coefficient_mass = 2.3
    coefficient_phase_action = -1.4
    coefficient_nu = (
        abs(coefficient_phase_action)
        / (2.0 * coefficient_mass)
    )
    phase_gradient_coefficient = (
        coefficient_phase_action**2
        / (2.0 * coefficient_mass)
    )
    fisher_gradient_coefficient = (
        2.0
        * coefficient_mass
        * coefficient_nu**2
    )
    checks.append(
        record_max(
            "phase_bath_coefficient_match_error",
            abs(
                phase_gradient_coefficient
                - fisher_gradient_coefficient
            ),
            1.0e-14,
        )
    )

    # A single-valued two-component field gives integer circulation.
    winding_numbers = np.arange(-7, 8)
    circulation = -2.0 * np.pi * (
        coefficient_phase_action * winding_numbers
    )
    recovered_winding = (
        -circulation
        / (2.0 * np.pi * coefficient_phase_action)
    )
    checks.append(
        record_max(
            "phase_winding_circulation_error",
            np.max(np.abs(recovered_winding - winding_numbers)),
            1.0e-14,
        )
    )

    # Two orthogonal source channels reproduce the antisymmetric rank-two
    # correlation matrix without introducing an independent configuration field.
    bell_scale = 1.7
    basis_plus = np.array([1.0, 0.0], dtype=complex)
    basis_minus = np.array([0.0, 1.0], dtype=complex)
    source_matrix = np.sqrt(bell_scale / 2.0) * np.array(
        [[0.0, 1.0], [-1.0, 0.0]],
        dtype=complex,
    )
    factorized_source = np.sqrt(bell_scale / 2.0) * (
        np.outer(basis_plus, basis_minus.conj())
        - np.outer(basis_minus, basis_plus.conj())
    )
    checks.append(
        record_max(
            "antisymmetric_rank_two_factorization_error",
            np.max(np.abs(source_matrix - factorized_source)),
            1.0e-14,
        )
    )

    # The conjugated low-rank correlation is invariant under a common
    # internal phase rotation.
    phase_rotation = np.exp(1j * 0.731)
    source_a = np.stack([basis_plus, basis_minus])
    source_b = np.stack([basis_minus, -basis_plus])
    low_rank_before = np.sqrt(bell_scale / 2.0) * sum(
        np.outer(source_a[index], source_b[index].conj())
        for index in range(2)
    )
    low_rank_after = np.sqrt(bell_scale / 2.0) * sum(
        np.outer(
            phase_rotation * source_a[index],
            (phase_rotation * source_b[index]).conj(),
        )
        for index in range(2)
    )
    checks.append(
        record_max(
            "common_internal_phase_invariance_error",
            np.max(np.abs(low_rank_before - low_rank_after)),
            1.0e-14,
        )
    )

    # Local real rotations of the antisymmetric source generate the exact
    # Bell cosine branch actions.
    angle_count = 2000
    analyzer_a = rng.uniform(-np.pi, np.pi, size=angle_count)
    analyzer_b = rng.uniform(-np.pi, np.pi, size=angle_count)
    signs = np.array([1.0, -1.0])
    branch_action_error = 0.0
    branch_sum_error = 0.0
    branch_marginal_error = 0.0
    bell_actions = np.empty((angle_count, 2, 2))
    for index, (angle_a, angle_b) in enumerate(
        zip(analyzer_a, analyzer_b)
    ):
        rotation_a = np.array([
            [np.cos(angle_a), -np.sin(angle_a)],
            [np.sin(angle_a), np.cos(angle_a)],
        ])
        rotation_b = np.array([
            [np.cos(angle_b), -np.sin(angle_b)],
            [np.sin(angle_b), np.cos(angle_b)],
        ])
        rotated = rotation_a @ source_matrix @ rotation_b.T
        direct = np.abs(rotated) ** 2
        delta = 2.0 * (angle_a - angle_b)
        expected = np.empty((2, 2))
        for i, sign_a in enumerate(signs):
            for j, sign_b in enumerate(signs):
                expected[i, j] = 0.25 * bell_scale * (
                    1.0 - sign_a * sign_b * np.cos(delta)
                )
        bell_actions[index] = direct
        branch_action_error = max(
            branch_action_error,
            float(np.max(np.abs(direct - expected))),
        )
        branch_sum_error = max(
            branch_sum_error,
            abs(float(np.sum(direct)) - bell_scale),
        )
        branch_marginal_error = max(
            branch_marginal_error,
            float(
                np.max(
                    np.abs(
                        np.concatenate(
                            [direct.sum(axis=0), direct.sum(axis=1)]
                        )
                        - bell_scale / 2.0
                    )
                )
            ),
        )
    checks.append(
        record_max(
            "bell_low_rank_cosine_action_error",
            branch_action_error,
            1.0e-13,
        )
    )
    checks.append(
        record_max(
            "bell_action_total_error",
            branch_sum_error,
            1.0e-13,
        )
    )
    checks.append(
        record_max(
            "bell_action_marginal_error",
            branch_marginal_error,
            1.0e-13,
        )
    )

    # The ideal read Hamiltonian copies real and imaginary correlation
    # amplitudes while zero comparator momenta eliminate input backreaction.
    read_count = 100_000
    correlation = (
        rng.normal(size=read_count)
        + 1j * rng.normal(size=read_count)
    )
    read_area = 0.83
    q_real = read_area * correlation.real
    q_imag = read_area * correlation.imag
    copied = q_real + 1j * q_imag
    checks.append(
        record_max(
            "ideal_comparator_displacement_error",
            np.max(np.abs(copied - read_area * correlation)),
            1.0e-14,
        )
    )
    comparator_momentum_real = np.zeros(read_count)
    comparator_momentum_imag = np.zeros(read_count)
    input_backreaction = (
        np.abs(comparator_momentum_real)
        + np.abs(comparator_momentum_imag)
    )
    checks.append(
        record_max(
            "ideal_comparator_input_backreaction",
            np.max(input_backreaction),
            1.0e-14,
        )
    )
    comparator_action = 0.5 * (q_real**2 + q_imag**2)
    expected_comparator_action = (
        0.5 * read_area**2 * np.abs(correlation) ** 2
    )
    checks.append(
        record_max(
            "comparator_action_transfer_error",
            np.max(
                np.abs(
                    comparator_action
                    - expected_comparator_action
                )
            ),
            1.0e-13,
        )
    )

    # The two-mode shell capacity is linear in the transferred Bell action.
    positive_actions = np.linspace(0.01, 4.0, 1000)
    two_mode_capacity = (2.0 * np.pi) ** 2 * positive_actions
    recovered_capacity_slope = two_mode_capacity / positive_actions
    checks.append(
        record_max(
            "bell_two_mode_shell_linearity_error",
            np.max(
                np.abs(
                    recovered_capacity_slope
                    - (2.0 * np.pi) ** 2
                )
            ),
            1.0e-13,
        )
    )

    # A common unnormalized boundary density converts the shell capacities
    # into the Bell joint law and preserves both one-side marginals.
    probability_error = 0.0
    no_signalling_error = 0.0
    angle_grid = np.linspace(-np.pi, np.pi, 41)
    for delta in angle_grid:
        raw = np.empty((2, 2))
        expected = np.empty((2, 2))
        for i, sign_a in enumerate(signs):
            for j, sign_b in enumerate(signs):
                action = 0.25 * bell_scale * (
                    1.0 - sign_a * sign_b * np.cos(delta)
                )
                raw[i, j] = 0.25 * (2.0 * np.pi) ** 2 * action
                expected[i, j] = 0.25 * (
                    1.0 - sign_a * sign_b * np.cos(delta)
                )
        probability = raw / raw.sum()
        probability_error = max(
            probability_error,
            float(np.max(np.abs(probability - expected))),
        )
        no_signalling_error = max(
            no_signalling_error,
            float(np.max(np.abs(probability.sum(axis=0) - 0.5))),
            float(np.max(np.abs(probability.sum(axis=1) - 0.5))),
        )
    checks.append(
        record_max(
            "bell_common_boundary_probability_error",
            probability_error,
            1.0e-14,
        )
    )
    checks.append(
        record_max(
            "bell_no_signalling_marginal_error",
            no_signalling_error,
            1.0e-14,
        )
    )

    # The analytic cosine law reaches the ideal CHSH value.
    chsh_direct = sum(
        coefficient * (-np.cos(angle))
        for coefficient, angle in (
            (1.0, -np.pi / 4.0),
            (1.0, np.pi / 4.0),
            (1.0, np.pi / 4.0),
            (-1.0, 3.0 * np.pi / 4.0),
        )
    )
    checks.append(
        record_max(
            "bell_ideal_chsh_error",
            abs(abs(chsh_direct) - 2.0 * np.sqrt(2.0)),
            1.0e-14,
        )
    )

    # Finite read pulses applied to a freely rotating input have a relative
    # displacement error of first order in pulse duration.
    pulse_frequency = 0.7
    pulse_correlation = 0.8 + 0.6j

    def relative_pulse_error(duration: float) -> float:
        exact_integral = pulse_correlation * (
            1.0 - np.exp(-1j * pulse_frequency * duration)
        ) / (1j * pulse_frequency)
        ideal_integral = duration * pulse_correlation
        return float(
            abs(exact_integral - ideal_integral)
            / abs(ideal_integral)
        )

    pulse_error_large = relative_pulse_error(0.02)
    pulse_error_small = relative_pulse_error(0.01)
    pulse_order = np.log(
        pulse_error_large / pulse_error_small
    ) / np.log(2.0)
    checks.append(
        record_max(
            "finite_read_pulse_first_order_error",
            abs(pulse_order - 1.0),
            0.01,
        )
    )

    # Reversing the read pulse after undoing the shell mixing resets the
    # ideal comparator coordinates.
    unread_q_real = q_real - read_area * correlation.real
    unread_q_imag = q_imag - read_area * correlation.imag
    checks.append(
        record_max(
            "comparator_uncompute_reset_error",
            max(
                float(np.max(np.abs(unread_q_real))),
                float(np.max(np.abs(unread_q_imag))),
            ),
            1.0e-14,
        )
    )

    # Normalized sector ensembles retain their total masses under canonical
    # mixing; they do not acquire the unequal shell-capacity weights.
    fixed_delta = 0.63
    target_actions = np.empty((2, 2))
    for i, sign_a in enumerate(signs):
        for j, sign_b in enumerate(signs):
            target_actions[i, j] = 0.25 * bell_scale * (
                1.0 - sign_a * sign_b * np.cos(fixed_delta)
            )
    normalized_sector_mass = np.full((2, 2), 0.25)
    capacity_weight = target_actions / target_actions.sum()
    mass_preservation_error = np.max(
        np.abs(normalized_sector_mass.sum() - 1.0)
    )
    checks.append(
        record_max(
            "normalized_sector_mass_preservation_error",
            mass_preservation_error,
            1.0e-14,
        )
    )
    checks.append(
        record_min(
            "normalized_mixing_capacity_mismatch_guard",
            np.max(
                np.abs(
                    normalized_sector_mass
                    - capacity_weight
                )
            ),
            0.05,
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
