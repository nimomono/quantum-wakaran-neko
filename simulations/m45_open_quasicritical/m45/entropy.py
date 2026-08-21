"""Phase-volume audit of the logarithmic entropy reservoir in M45."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.polynomial.legendre import leggauss

from .model import ModelParameters


def phase_volume(
    energy: float,
    parameters: ModelParameters,
    quadrature_points: int = 72,
) -> float:
    """Liouville sublevel volume on one periodic selector cell.

    Constant mass factors cancel from all ratios and are omitted.
    """
    if energy <= 0.0:
        return 0.0
    nodes, weights = leggauss(quadrature_points)
    angle = np.pi * nodes
    angle_weights = np.pi * weights
    structural = parameters.pendulum_scale * (1.0 - np.cos(angle))
    total = 0.0
    for structural_energy, angle_weight in zip(structural, angle_weights):
        available = energy - structural_energy
        if available <= 0.0:
            continue
        turning = parameters.log_core * np.sqrt(
            np.expm1(2.0 * available / parameters.theta)
        )
        shifted = turning * nodes
        shifted_weights = turning * weights
        logarithmic = 0.5 * parameters.theta * np.log1p(
            (shifted / parameters.log_core) ** 2
        )
        momentum_volume = np.maximum(available - logarithmic, 0.0)
        total += angle_weight * float(
            np.sum(shifted_weights * momentum_volume)
        )
    return total


@dataclass(frozen=True)
class PhaseVolumeTable:
    energy: np.ndarray
    volume: np.ndarray

    @classmethod
    def build(
        cls,
        parameters: ModelParameters,
        maximum_energy: float = 0.36,
        points: int = 721,
        quadrature_points: int = 64,
    ) -> "PhaseVolumeTable":
        energy = np.linspace(0.0, maximum_energy, points)
        volume = np.asarray(
            [
                phase_volume(value, parameters, quadrature_points)
                for value in energy
            ]
        )
        return cls(energy=energy, volume=volume)

    def __call__(self, energy: np.ndarray | float) -> np.ndarray:
        return np.interp(
            np.asarray(energy),
            self.energy,
            self.volume,
            left=0.0,
            right=self.volume[-1],
        )


def shell_factor(
    potential: np.ndarray,
    ready_energy: np.ndarray,
    table: PhaseVolumeTable,
    maximum_samples: int = 100_000,
) -> np.ndarray:
    if ready_energy.size > maximum_samples:
        indices = np.linspace(
            0,
            ready_energy.size - 1,
            maximum_samples,
            dtype=np.int64,
        )
        energy = ready_energy[indices]
    else:
        energy = ready_energy
    denominator = np.maximum(table(energy), 1.0e-300)
    return np.asarray(
        [
            np.mean(table(energy - value) / denominator)
            for value in potential
        ]
    )


def entropy_audit(
    ready_energy: np.ndarray,
    parameters: ModelParameters,
    table: PhaseVolumeTable,
) -> dict[str, object]:
    z = np.linspace(0.0, 1.5, 31)
    potential = z * parameters.theta
    ratio = shell_factor(potential, ready_energy, table)
    fixed_denominator = float(table(parameters.separatrix_energy))
    fixed_ratio = table(parameters.separatrix_energy - potential) / max(
        fixed_denominator, 1.0e-300
    )
    target = np.exp(-z)
    return {
        "z": z,
        "ratio": ratio,
        "fixed_ratio": fixed_ratio,
        "target": target,
        "log_slope": float(np.polyfit(z, np.log(ratio), 1)[0]),
        "max_error": float(np.max(np.abs(ratio - target))),
        "fixed_log_slope": float(
            np.polyfit(z, np.log(fixed_ratio), 1)[0]
        ),
        "fixed_max_error": float(np.max(np.abs(fixed_ratio - target))),
    }
