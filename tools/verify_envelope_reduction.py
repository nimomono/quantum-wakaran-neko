#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import dataclass

import numpy as np


TOL = 5.0e-12
J0 = 1.0
M_OSC = 1.0
L = 8


@dataclass
class Check:
    name: str
    value: float
    limit: float
    relation: str = "<="

    @property
    def passed(self) -> bool:
        if self.relation == "<=":
            return self.value <= self.limit
        if self.relation == ">=":
            return self.value >= self.limit
        raise ValueError(self.relation)


def hermitian_function(matrix: np.ndarray, function) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    return (vectors * function(values)) @ vectors.conj().T


def unitary_evolution(generator: np.ndarray, time: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(generator)
    return (vectors * np.exp(-1j * values * time / J0)) @ vectors.conj().T


def path_laplacian(size: int) -> np.ndarray:
    laplacian = np.zeros((size, size))
    for index in range(size - 1):
        laplacian[index, index] += 1.0
        laplacian[index + 1, index + 1] += 1.0
        laplacian[index, index + 1] -= 1.0
        laplacian[index + 1, index] -= 1.0
    return laplacian


def target_generator() -> np.ndarray:
    sites = np.arange(L) - (L - 1) / 2
    potential = 0.025 * sites**2
    return 0.45 * path_laplacian(L) + np.diag(potential)


def local_to_physical(local: np.ndarray, omega: float) -> tuple[np.ndarray, np.ndarray]:
    amplitude = np.sqrt(2.0 * J0)
    q = amplitude * local.real / np.sqrt(M_OSC * omega)
    p = amplitude * local.imag * np.sqrt(M_OSC * omega)
    return q, p


def physical_to_local(q: np.ndarray, p: np.ndarray, omega: float, time: float) -> np.ndarray:
    Q = np.sqrt(M_OSC * omega) * q
    P = p / np.sqrt(M_OSC * omega)
    return np.exp(1j * omega * time) * (Q + 1j * P) / np.sqrt(2.0 * J0)


def physical_to_exact(
    q: np.ndarray,
    p: np.ndarray,
    omega_matrix: np.ndarray,
    carrier_omega: float,
    time: float,
) -> np.ndarray:
    omega_half = hermitian_function(omega_matrix, np.sqrt)
    omega_minus_half = hermitian_function(omega_matrix, lambda value: 1.0 / np.sqrt(value))
    c = (
        np.sqrt(M_OSC) * omega_half @ q
        + 1j * omega_minus_half @ p / np.sqrt(M_OSC)
    ) / np.sqrt(2.0 * J0)
    return np.exp(1j * carrier_omega * time) * c


def evolve_physical(
    q0: np.ndarray,
    p0: np.ndarray,
    omega_matrix: np.ndarray,
    time: float,
) -> tuple[np.ndarray, np.ndarray]:
    cosine = hermitian_function(omega_matrix, lambda value: np.cos(value * time))
    sine_over = hermitian_function(omega_matrix, lambda value: np.sin(value * time) / value)
    omega_sine = hermitian_function(omega_matrix, lambda value: value * np.sin(value * time))
    q = cosine @ q0 + sine_over @ p0 / M_OSC
    p = -M_OSC * omega_sine @ q0 + cosine @ p0
    return q, p


def total_variation(probability_a: np.ndarray, probability_b: np.ndarray) -> float:
    return float(0.5 * np.sum(np.abs(probability_a - probability_b)))


def random_unitary(rng: np.random.Generator, size: int) -> np.ndarray:
    raw = rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))
    q_matrix, r_matrix = np.linalg.qr(raw)
    phases = np.diag(r_matrix)
    phases = phases / np.abs(phases)
    return q_matrix @ np.diag(phases.conj())


def run_case(omega: float, local0: np.ndarray) -> dict[str, float]:
    h_target = target_generator()
    h_norm = float(np.linalg.norm(h_target, 2))
    perturbation = 2.0 * M_OSC * omega * h_target / J0
    stiffness = omega**2 * np.eye(L) + perturbation / M_OSC
    omega_matrix = hermitian_function(stiffness, np.sqrt)
    h_exact = J0 * (omega_matrix - omega * np.eye(L))
    eta = 2.0 * h_norm / (J0 * omega)
    operator_error = float(np.linalg.norm(h_exact - h_target, 2))
    operator_bound = h_norm**2 / (2.0 * J0 * omega * (1.0 - eta) ** 1.5)
    natural_time = J0 / h_norm

    q0, p0 = local_to_physical(local0, omega)
    exact0 = physical_to_exact(q0, p0, omega_matrix, omega, 0.0)
    q_time, p_time = evolve_physical(q0, p0, omega_matrix, natural_time)
    local_time = physical_to_local(q_time, p_time, omega, natural_time)
    exact_time = physical_to_exact(q_time, p_time, omega_matrix, omega, natural_time)
    effective_time = unitary_evolution(h_target, natural_time) @ local0
    effective_from_exact = unitary_evolution(h_target, natural_time) @ exact0

    exact_state_error = float(np.linalg.norm(exact_time - effective_from_exact))
    exact_state_bound = natural_time * operator_bound * np.linalg.norm(exact0) / J0
    local_state_error = float(np.linalg.norm(local_time - effective_time))
    delta_transform = (1.0 - eta) ** (-0.25) - 1.0
    local_state_bound = (
        2.0 * delta_transform + natural_time * operator_bound / J0
    ) * np.linalg.norm(exact0)

    local_normalized = local_time / np.linalg.norm(local_time)
    effective_normalized = effective_time / np.linalg.norm(effective_time)
    overlap = abs(np.vdot(local_normalized, effective_normalized))
    trace_distance = float(np.sqrt(max(0.0, 1.0 - overlap**2)))

    return {
        "omega": omega,
        "eta": eta,
        "operator_error": operator_error,
        "operator_bound": operator_bound,
        "exact_state_error": exact_state_error,
        "exact_state_bound": exact_state_bound,
        "local_state_error": local_state_error,
        "local_state_bound": local_state_bound,
        "trace_distance": trace_distance,
        "local_action": float(np.vdot(local_time, local_time).real),
        "exact_action": float(np.vdot(exact_time, exact_time).real),
        "delta_transform": delta_transform,
        "h0_mapping_error": float(
            np.linalg.norm(J0 * perturbation / (2.0 * M_OSC * omega) - h_target, 2)
        ),
        "stiffness_min": float(np.min(np.linalg.eigvalsh(stiffness))),
    }


def main() -> None:
    rng = np.random.default_rng(20260809)
    local0 = rng.normal(size=L) + 1j * rng.normal(size=L)
    local0 = local0 / np.linalg.norm(local0)
    cases = [run_case(omega, local0) for omega in (20.0, 40.0, 80.0)]

    checks: list[Check] = []
    for case in cases:
        omega = case["omega"]
        checks.extend([
            Check(f"omega={omega:g}: stability", case["stiffness_min"], 1.0, ">="),
            Check(f"omega={omega:g}: h0 mapping", case["h0_mapping_error"], TOL),
            Check(
                f"omega={omega:g}: operator bound",
                case["operator_error"] - case["operator_bound"],
                TOL,
            ),
            Check(
                f"omega={omega:g}: exact state bound",
                case["exact_state_error"] - case["exact_state_bound"],
                TOL,
            ),
            Check(
                f"omega={omega:g}: local state bound",
                case["local_state_error"] - case["local_state_bound"],
                TOL,
            ),
        ])

    operator_ratios = [
        cases[index]["operator_error"] / cases[index + 1]["operator_error"]
        for index in range(len(cases) - 1)
    ]
    state_ratios = [
        cases[index]["local_state_error"] / cases[index + 1]["local_state_error"]
        for index in range(len(cases) - 1)
    ]
    checks.append(Check("operator error first-order ratio", min(operator_ratios), 1.8, ">="))
    checks.append(Check("local state error asymptotic ratio", state_ratios[-1], 1.75, ">="))

    selected = cases[1]
    h_target = target_generator()
    time = J0 / np.linalg.norm(h_target, 2)
    effective = unitary_evolution(h_target, time) @ local0
    perturbation = 2.0 * M_OSC * selected["omega"] * h_target / J0
    omega_matrix = hermitian_function(
        selected["omega"] ** 2 * np.eye(L) + perturbation / M_OSC,
        np.sqrt,
    )
    q0, p0 = local_to_physical(local0, selected["omega"])
    q_time, p_time = evolve_physical(q0, p0, omega_matrix, time)
    local_time = physical_to_local(q_time, p_time, selected["omega"], time)
    local_normalized = local_time / np.linalg.norm(local_time)
    effective_normalized = effective / np.linalg.norm(effective)
    basis = random_unitary(rng, L)
    probability_local = np.abs(basis @ local_normalized) ** 2
    probability_effective = np.abs(basis @ effective_normalized) ** 2
    tv_distance = total_variation(probability_local, probability_effective)
    overlap = abs(np.vdot(local_normalized, effective_normalized))
    trace_distance = float(np.sqrt(max(0.0, 1.0 - overlap**2)))
    checks.append(Check("Born TV bounded by trace distance", tv_distance - trace_distance, TOL))

    action_relative_error = abs(selected["local_action"] / selected["exact_action"] - 1.0)
    action_bound = 2.0 * selected["delta_transform"] + selected["delta_transform"] ** 2
    checks.append(Check("local action variation bound", action_relative_error - action_bound, TOL))

    output = {
        "checks": [
            {
                "name": check.name,
                "value": check.value,
                "limit": check.limit,
                "relation": check.relation,
                "passed": bool(check.passed),
            }
            for check in checks
        ],
        "cases": cases,
        "born_interface": {
            "tv_distance": tv_distance,
            "trace_distance": trace_distance,
        },
        "passed": bool(all(check.passed for check in checks)),
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    if not output["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
