#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from math import sqrt

import numpy as np


@dataclass
class CheckResult:
    name: str
    value: float
    threshold: float
    criterion: str
    passed: bool


def record_max(name: str, value: float, threshold: float) -> CheckResult:
    return CheckResult(name, float(value), float(threshold), "<=", bool(value <= threshold))


def record_min(name: str, value: float, threshold: float) -> CheckResult:
    return CheckResult(name, float(value), float(threshold), ">=", bool(value >= threshold))


def random_unitary(rng: np.random.Generator, size: int) -> np.ndarray:
    matrix = rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))
    unitary, diagonal = np.linalg.qr(matrix)
    phases = np.diag(diagonal).copy()
    phases /= np.abs(phases)
    return unitary @ np.diag(phases.conj())


def normalize(vector: np.ndarray) -> np.ndarray:
    return vector / np.linalg.norm(vector)


def joint_distribution(
    signal: np.ndarray,
    basis_a: np.ndarray,
    basis_b: np.ndarray,
) -> np.ndarray:
    return np.array([
        [
            abs(np.vdot(np.kron(basis_a[:, a], basis_b[:, b]), signal)) ** 2
            for b in range(2)
        ]
        for a in range(2)
    ])


def main() -> None:
    seed = 20260904
    rng = np.random.default_rng(seed)
    checks: list[CheckResult] = []
    identity_2 = np.eye(2, dtype=complex)

    hadamard = np.array([[1.0, 1.0], [1.0, -1.0]], dtype=complex) / sqrt(2.0)
    pauli_x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    pauli_z = np.diag([1.0, -1.0]).astype(complex)
    controlled_x = np.array(
        [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0],
         [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]],
        dtype=complex,
    )
    source = np.array([1.0, 0.0, 0.0, 0.0], dtype=complex)
    source = np.kron(hadamard, identity_2) @ source
    source = controlled_x @ source
    source = np.kron(identity_2, pauli_x) @ source
    source = np.kron(pauli_z, identity_2) @ source
    singlet = np.array([0.0, 1.0, -1.0, 0.0], dtype=complex) / sqrt(2.0)
    checks.append(record_max(
        "m54_singlet_gate_sequence_error",
        np.linalg.norm(source - singlet),
        3.0e-14,
    ))

    maximum_block_error = 0.0
    maximum_projector_error = 0.0
    maximum_completeness_error = 0.0
    maximum_b_marginal_error = 0.0
    maximum_joint_born_error = 0.0
    maximum_normalization_lipschitz_excess = 0.0
    maximum_radial_ratio_error = 0.0
    tau = 0.08
    maximum_cutoff_excess = 0.0

    for _ in range(500):
        signal = normalize(rng.normal(size=4) + 1j * rng.normal(size=4))
        coefficient = signal.reshape(2, 2, order="C")
        basis_a = random_unitary(rng, 2)
        basis_b = random_unitary(rng, 2)
        transformed = np.kron(basis_a.conj().T, identity_2) @ signal

        branch_weights: list[float] = []
        b_marginal = np.zeros((2, 2), dtype=complex)
        for branch in range(2):
            direction_a = basis_a[:, branch]
            block = coefficient.T @ direction_a.conj()
            routed_block = transformed[2 * branch:2 * branch + 2]
            maximum_block_error = max(
                maximum_block_error,
                float(np.linalg.norm(block - routed_block)),
            )
            projector = np.outer(direction_a, direction_a.conj())
            projector_weight = float(
                np.vdot(signal, np.kron(projector, identity_2) @ signal).real
            )
            block_weight = float(np.vdot(block, block).real)
            maximum_projector_error = max(
                maximum_projector_error,
                abs(projector_weight - block_weight),
            )
            branch_weights.append(block_weight)
            b_marginal += np.outer(block, block.conj())

            for outcome_b in range(2):
                direction_b = basis_b[:, outcome_b]
                sequential_weight = abs(np.vdot(direction_b, block)) ** 2
                direct_amplitude = np.vdot(
                    np.kron(direction_a, direction_b), signal
                )
                maximum_joint_born_error = max(
                    maximum_joint_born_error,
                    abs(sequential_weight - abs(direct_amplitude) ** 2),
                )

            if block_weight >= tau:
                perturbation = 1.0e-5 * normalize(
                    rng.normal(size=2) + 1j * rng.normal(size=2)
                )
                perturbed = block + perturbation
                lhs = np.linalg.norm(
                    block / np.linalg.norm(block)
                    - perturbed / np.linalg.norm(perturbed)
                )
                rhs = 2.0 * np.linalg.norm(perturbation) / sqrt(tau)
                maximum_normalization_lipschitz_excess = max(
                    maximum_normalization_lipschitz_excess,
                    float(lhs - rhs),
                )

        maximum_completeness_error = max(
            maximum_completeness_error,
            abs(sum(branch_weights) - 1.0),
        )
        expected_b_marginal = coefficient.T @ coefficient.conj()
        maximum_b_marginal_error = max(
            maximum_b_marginal_error,
            float(np.linalg.norm(b_marginal - expected_b_marginal)),
        )
        discarded = sum(weight for weight in branch_weights if weight < tau)
        maximum_cutoff_excess = max(maximum_cutoff_excess, discarded - 2.0 * tau)
        radial = float(np.exp(rng.uniform(-1.2, 1.2)))
        physical_signal = radial * signal
        physical_capacities = np.array([
            float(np.vdot(
                physical_signal,
                np.kron(
                    np.outer(basis_a[:, branch], basis_a[:, branch].conj()),
                    identity_2,
                ) @ physical_signal,
            ).real)
            for branch in range(2)
        ])
        physical_ratios = physical_capacities / np.sum(physical_capacities)
        maximum_radial_ratio_error = max(
            maximum_radial_ratio_error,
            float(np.max(np.abs(physical_ratios - np.asarray(branch_weights)))),
        )

    checks.extend([
        record_max("r180a_row_major_block_error", maximum_block_error, 8.0e-14),
        record_max("r180a_projector_action_error", maximum_projector_error, 8.0e-14),
        record_max("r180a_branch_completeness_error", maximum_completeness_error, 8.0e-14),
        record_max("r180a_b_marginal_error", maximum_b_marginal_error, 8.0e-14),
        record_max("r180a_joint_born_error", maximum_joint_born_error, 8.0e-14),
        record_max("r180a_node_cutoff_excess", maximum_cutoff_excess, 2.0e-15),
        record_max(
            "r180a_physical_capacity_radial_ratio_error",
            maximum_radial_ratio_error,
            8.0e-14,
        ),
        record_max(
            "r180a_normalization_lipschitz_excess",
            maximum_normalization_lipschitz_excess,
            2.0e-15,
        ),
    ])

    antisymmetric = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    singlet_matrix = antisymmetric / sqrt(2.0)
    maximum_singlet_weight_error = 0.0
    maximum_spin_flip_error = 0.0
    for _ in range(100):
        basis_a = random_unitary(rng, 2)
        for branch in range(2):
            direction_a = basis_a[:, branch]
            block = singlet_matrix.T @ direction_a.conj()
            maximum_singlet_weight_error = max(
                maximum_singlet_weight_error,
                abs(float(np.vdot(block, block).real) - 0.5),
            )
            expected_partner = -antisymmetric @ direction_a.conj()
            maximum_spin_flip_error = max(
                maximum_spin_flip_error,
                float(np.linalg.norm(block / np.linalg.norm(block) - expected_partner)),
            )
    checks.append(record_max(
        "r180a_singlet_equal_branch_error",
        maximum_singlet_weight_error,
        5.0e-14,
    ))
    checks.append(record_max(
        "r180a_singlet_spin_flip_ray_error",
        maximum_spin_flip_error,
        5.0e-14,
    ))
    input_a = normalize(np.array([1.0 + 0.2j, -0.31 + 0.77j]))
    input_b = normalize(np.array([0.44 - 0.12j, 0.19 + 0.88j]))
    initial_signal = np.kron(input_a, input_b)
    anti_register = initial_signal.conj()
    phase_a = np.diag([1.0, np.exp(0.61j)])
    phase_b = np.diag([1.0, np.exp(0.37j)])
    controlled_phase = np.diag([1.0, 1.0, 1.0, np.exp(0.83j)])
    general_gate = (
        np.kron(hadamard, phase_b)
        @ controlled_phase
        @ controlled_x
        @ np.kron(phase_a, hadamard)
    )
    terminal_signal = general_gate @ initial_signal

    receiver_basis_a = np.array(
        [[1.0, 1.0], [1.0j, -1.0j]],
        dtype=complex,
    ) / sqrt(2.0)
    receiver_basis_b = random_unitary(rng, 2)
    direct_terminal = joint_distribution(
        terminal_signal,
        receiver_basis_a,
        receiver_basis_b,
    )
    terminal_coefficient = terminal_signal.reshape(2, 2, order="C")
    receiver_terminal = np.array([
        [
            abs(np.vdot(
                receiver_basis_b[:, b],
                terminal_coefficient.T @ receiver_basis_a[:, a].conj(),
            )) ** 2
            for b in range(2)
        ]
        for a in range(2)
    ])
    stale_terminal = anti_register.conj()
    stale_distribution = joint_distribution(
        stale_terminal,
        receiver_basis_a,
        receiver_basis_b,
    )
    stale_total_variation = 0.5 * float(
        np.sum(np.abs(stale_distribution - direct_terminal))
    )

    checks.extend([
        record_max(
            "m54_general_gate_unitarity_error",
            np.linalg.norm(general_gate.conj().T @ general_gate - np.eye(4)),
            3.0e-14,
        ),
        record_min("m54_general_gate_nonreal_norm", np.linalg.norm(general_gate.imag), 0.5),
        record_min(
            "m54_general_gate_nonsymmetry_norm",
            np.linalg.norm(general_gate - general_gate.T),
            0.5,
        ),
        record_min(
            "m54_terminal_anti_mismatch",
            np.linalg.norm(anti_register - terminal_signal.conj()),
            0.5,
        ),
        record_max(
            "r180_actual_terminal_receiver_error",
            np.max(np.abs(receiver_terminal - direct_terminal)),
            8.0e-14,
        ),
        record_min(
            "r180_stale_anti_receiver_tv_gap",
            stale_total_variation,
            0.1,
        ),
    ])

    payload = {
        "seed": seed,
        "check_count": len(checks),
        "checks": [asdict(check) for check in checks],
        "passed": all(check.passed for check in checks),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
