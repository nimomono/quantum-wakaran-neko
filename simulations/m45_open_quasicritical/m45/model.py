"""Local potential and forces for the current M45 model."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ModelParameters:
    separatrix_energy: float = 0.25
    theta: float = 0.05
    log_core: float = 0.02
    shift_coupling: float = 0.50
    structural_mass: float = 0.80
    log_mass: float = 0.25
    bath_temperature: float = 0.004
    gamma_s: float = 0.010
    gamma_r: float = 0.060
    active_gain: float = 0.085
    active_speed: float = 0.70

    @property
    def pendulum_scale(self) -> float:
        return 0.5 * self.separatrix_energy


def potential_and_force(
    s: np.ndarray,
    r: np.ndarray,
    parameters: ModelParameters,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return U_C and the forces -dU_C/ds and -dU_C/dr."""
    shifted = r - parameters.shift_coupling * np.sin(s)
    structural = parameters.pendulum_scale * (1.0 - np.cos(s))
    logarithmic = 0.5 * parameters.theta * np.log1p(
        (shifted / parameters.log_core) ** 2
    )
    log_gradient = parameters.theta * shifted / (
        parameters.log_core**2 + shifted**2
    )
    force_s = (
        -parameters.pendulum_scale * np.sin(s)
        + parameters.shift_coupling * np.cos(s) * log_gradient
    )
    force_r = -log_gradient
    return structural + logarithmic, force_s, force_r


def total_energy(
    s: np.ndarray,
    r: np.ndarray,
    p_s: np.ndarray,
    p_r: np.ndarray,
    parameters: ModelParameters,
) -> np.ndarray:
    potential, _, _ = potential_and_force(s, r, parameters)
    return (
        potential
        + 0.5 * p_s**2 / parameters.structural_mass
        + 0.5 * p_r**2 / parameters.log_mass
    )


def active_force(
    p_s: np.ndarray,
    parameters: ModelParameters,
) -> np.ndarray:
    velocity = p_s / parameters.structural_mass
    return (
        parameters.active_gain
        * (1.0 - (velocity / parameters.active_speed) ** 2)
        * velocity
    )


def well_index(s: np.ndarray) -> np.ndarray:
    """Integer winding cell used only for post-integration slip detection."""
    return np.floor((s + np.pi) / (2.0 * np.pi)).astype(np.int64)
