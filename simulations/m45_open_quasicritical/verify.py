#!/usr/bin/env python3
"""Fast regression checks for the current M45 model."""

from __future__ import annotations

import argparse
import json
from dataclasses import replace
from pathlib import Path

import numpy as np

from m45.entropy import PhaseVolumeTable, entropy_audit
from m45.integrator import SimulationParameters, simulate
from m45.model import ModelParameters, potential_and_force
from m45.observables import monotone_hazard_score
from m45.operator_audit import OperatorParameters, run_operator_audit


ROOT = Path(__file__).resolve().parent


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_quick() -> SimulationParameters:
    values = json.loads(
        (ROOT / "configs" / "quick.json").read_text(encoding="utf-8")
    )
    return SimulationParameters(**values)


def force_check(model: ModelParameters) -> float:
    s = np.linspace(-2.4, 2.4, 17)
    r = np.linspace(-0.08, 0.08, 17)
    step = 1.0e-6
    _, force_s, force_r = potential_and_force(s, r, model)
    plus_s, _, _ = potential_and_force(s + step, r, model)
    minus_s, _, _ = potential_and_force(s - step, r, model)
    plus_r, _, _ = potential_and_force(s, r + step, model)
    minus_r, _, _ = potential_and_force(s, r - step, model)
    error = max(
        float(np.max(np.abs(force_s + (plus_s - minus_s) / (2.0 * step)))),
        float(np.max(np.abs(force_r + (plus_r - minus_r) / (2.0 * step)))),
    )
    check(error < 2.0e-8, f"force-gradient error: {error}")
    return error


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()
    simulation = load_quick()
    if not args.quick:
        simulation = replace(
            simulation,
            paths=192,
            duration=260.0,
            burn_in=120.0,
            dt=0.002,
            sample_interval=0.04,
        )
    model = ModelParameters()
    gradient_error = force_check(model)
    active = simulate(simulation, model, keep_trace=False)
    passive = simulate(
        replace(simulation, seed=simulation.seed + 1),
        replace(model, active_gain=0.0),
        keep_trace=False,
    )
    summary = active["summary"]
    passive_summary = passive["summary"]
    hazard = monotone_hazard_score(active)

    check(np.all(np.isfinite(active["ready_energy"])), "non-finite active trajectory")
    check(0.55 < summary["ready_sector_fraction"] < 0.92, "ready fraction")
    check(summary["near_separatrix_fraction"] > 0.65, "separatrix shell")
    check(summary["recorded_episodes"] >= 20, "too few slip episodes")
    check(summary["recovery_per_episode"] > 0.85, "autonomous recovery")
    check(summary["std_recovery_energy"] < 0.015, "broad recovery energy")
    check(
        summary["median_recovery_delay"]
        < summary["median_inter_episode_time"],
        "recovery is slower than renewal",
    )
    check(
        max(summary["stationary_block_means"])
        - min(summary["stationary_block_means"])
        < 0.012,
        "stationary shell drift",
    )
    check(
        passive_summary["near_separatrix_fraction"]
        < 0.35 * summary["near_separatrix_fraction"],
        "passive control unexpectedly forms the shell",
    )
    check(hazard["correlation"] > 0.55, "slip hazard is not increasing")

    table = PhaseVolumeTable.build(model, points=481, quadrature_points=56)
    entropy = entropy_audit(active["ready_energy"], model, table)
    check(abs(entropy["log_slope"] + 1.0) < 0.15, "entropy slope")
    check(entropy["max_error"] < 0.04, "entropy factor error")

    operator, _ = run_operator_audit(
        active["ready_energy"],
        table,
        OperatorParameters(grid_points=101, slices=32),
    )
    for name, limit in (("harmonic", 0.006), ("double_well", 0.010)):
        values = operator["potentials"][name]
        check(values["operator_asymmetry"] < 1.0e-13, f"{name} asymmetry")
        check(values["doob_row_error"] < 2.0e-8, f"{name} Doob rows")
        check(
            values["detailed_balance_error"] < 1.0e-12,
            f"{name} detailed balance",
        )
        check(values["total_variation"] < limit, f"{name} ground density")
        check(
            values["stationary_nelson_residual"] < 1.0e-10,
            f"{name} stationary Nelson identity",
        )

    print(
        "M45 checks passed: "
        f"gradient_error={gradient_error:.3e} "
        f"ready_fraction={summary['ready_sector_fraction']:.4f} "
        f"near_separatrix={summary['near_separatrix_fraction']:.4f} "
        f"recovery={summary['recovery_per_episode']:.4f} "
        f"entropy_slope={entropy['log_slope']:.4f} "
        f"hazard_correlation={hazard['correlation']:.4f}"
    )


if __name__ == "__main__":
    main()
