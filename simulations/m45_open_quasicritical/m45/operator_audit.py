"""Conditional position-operator audit for M45.

This module does not infer the position kernel from the local Langevin
trajectory.  It checks the consequences of the three bridge assumptions:
unbiased position diffusion, time-proportional preparation rate, and marginal
reversibility.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass

import numpy as np

from .entropy import PhaseVolumeTable, shell_factor


@dataclass(frozen=True)
class OperatorParameters:
    total_time: float = 12.0
    nu: float = 0.1510484882090294
    mass: float = 0.9930585984576129
    grid_min: float = -12.0
    grid_max: float = 12.0
    grid_points: int = 121
    slices: int = 32

    @property
    def theta(self) -> float:
        return 4.0 * self.mass * self.nu / self.total_time


def particle_potential(name: str, x: np.ndarray) -> np.ndarray:
    if name == "harmonic":
        omega = 0.025
        return 0.5 * omega**2 * x**2
    if name == "double_well":
        well = 4.0
        barrier = 0.035
        return barrier * (x**2 - well**2) ** 2 / well**4
    raise ValueError(name)


def normalized_density(x: np.ndarray, vector: np.ndarray) -> np.ndarray:
    density = np.maximum(np.real(vector), 0.0) ** 2
    return density / np.trapezoid(density, x)


def quantum_ground_density(
    x: np.ndarray,
    potential: np.ndarray,
    parameters: OperatorParameters,
) -> tuple[np.ndarray, float, np.ndarray]:
    dx = x[1] - x[0]
    kinetic = 2.0 * parameters.mass * parameters.nu**2 / dx**2
    hamiltonian = np.diag(2.0 * kinetic + potential)
    off_diagonal = -kinetic * np.ones(x.size - 1)
    hamiltonian += np.diag(off_diagonal, 1) + np.diag(off_diagonal, -1)
    eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
    vector = eigenvectors[:, 0]
    if np.sum(vector) < 0.0:
        vector = -vector
    return normalized_density(x, vector), float(eigenvalues[0]), vector


def prepared_density(
    x: np.ndarray,
    full_factor: np.ndarray,
    parameters: OperatorParameters,
) -> tuple[np.ndarray, dict[str, float], np.ndarray]:
    dx = x[1] - x[0]
    step_time = parameters.total_time / parameters.slices
    displacement = x[:, None] - x[None, :]
    free = (
        np.exp(-displacement**2 / (4.0 * parameters.nu * step_time))
        / np.sqrt(4.0 * np.pi * parameters.nu * step_time)
        * dx
    )
    endpoint_factor = np.maximum(full_factor, 1.0e-300) ** (
        1.0 / parameters.slices
    )
    operator = endpoint_factor[:, None] * free * endpoint_factor[None, :]
    eigenvalues, eigenvectors = np.linalg.eigh(operator)
    eigenvalue = float(eigenvalues[-1])
    vector = eigenvectors[:, -1]
    if np.sum(vector) < 0.0:
        vector = -vector
    vector = np.abs(vector)
    density = normalized_density(x, vector)
    support = vector > 1.0e-12 * np.max(vector)
    doob = np.zeros_like(operator)
    doob[support] = (
        operator[support]
        * vector[None, :]
        / (eigenvalue * vector[support, None])
    )
    stationary = vector**2 / np.sum(vector**2)
    detailed_balance = stationary[:, None] * doob
    supported_balance = detailed_balance[np.ix_(support, support)]
    audit = {
        "operator_asymmetry": float(
            np.linalg.norm(operator - operator.T)
            / max(np.linalg.norm(operator), 1.0e-300)
        ),
        "doob_row_error": float(
            np.max(np.abs(np.sum(doob[support], axis=1) - 1.0))
        ),
        "detailed_balance_error": float(
            np.max(np.abs(supported_balance - supported_balance.T))
        ),
        "doob_supported_rows": int(np.sum(support)),
    }
    return density, audit, vector


def total_variation(
    x: np.ndarray,
    first: np.ndarray,
    second: np.ndarray,
) -> float:
    return float(0.5 * np.trapezoid(np.abs(first - second), x))


def run_operator_audit(
    ready_energy: np.ndarray,
    table: PhaseVolumeTable,
    parameters: OperatorParameters | None = None,
) -> tuple[dict[str, object], dict[str, dict[str, np.ndarray]]]:
    parameters = parameters or OperatorParameters()
    x = np.linspace(
        parameters.grid_min,
        parameters.grid_max,
        parameters.grid_points,
    )
    metrics: dict[str, object] = {
        "classification": "conditional_bridge_assumption_audit",
        "parameters": asdict(parameters),
        "theta_scale": parameters.theta,
        "potentials": {},
    }
    curves: dict[str, dict[str, np.ndarray]] = {}
    for name in ("harmonic", "double_well"):
        potential = particle_potential(name, x)
        factor = shell_factor(potential, ready_energy, table)
        prepared, stochastic_audit, _ = prepared_density(
            x, factor, parameters
        )
        target, energy, ground_vector = quantum_ground_density(
            x, potential, parameters
        )
        dx = x[1] - x[0]
        laplacian = np.zeros_like(ground_vector)
        laplacian[1:-1] = (
            ground_vector[2:]
            - 2.0 * ground_vector[1:-1]
            + ground_vector[:-2]
        ) / dx**2
        quantum_potential = np.full_like(ground_vector, np.nan)
        quantum_potential[1:-1] = (
            -2.0
            * parameters.mass
            * parameters.nu**2
            * laplacian[1:-1]
            / np.maximum(ground_vector[1:-1], 1.0e-300)
        )
        relevant = target > 1.0e-4 * np.max(target)
        eigen_residual = quantum_potential + potential - energy
        potential_metrics = {
            "total_variation": total_variation(x, prepared, target),
            "ground_energy": energy,
            "stationary_nelson_residual": float(
                np.nanmax(np.abs(eigen_residual[relevant]))
            ),
            **stochastic_audit,
        }
        metrics["potentials"][name] = potential_metrics
        curves[name] = {
            "x": x,
            "target": target,
            "prepared": prepared,
            "potential": potential,
            "factor": factor,
        }
    return metrics, curves
