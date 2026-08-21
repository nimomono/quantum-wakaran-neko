#!/usr/bin/env python3
"""Run and save the reference calculation for the current M45 model."""

from __future__ import annotations

import argparse
import csv
import json
import os
from dataclasses import asdict, replace
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/m45-open-quasicritical")

import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np

from m45.entropy import PhaseVolumeTable, entropy_audit
from m45.integrator import SimulationParameters, simulate
from m45.model import ModelParameters
from m45.observables import compact_result
from m45.operator_audit import OperatorParameters, run_operator_audit


ROOT = Path(__file__).resolve().parent
REPOSITORY = ROOT.parents[1]
REFERENCE = ROOT / "reference"
FIGURES = REPOSITORY / "figures"
FONT = REPOSITORY / "fonts" / "NotoSansJP-Regular.ttf"


def configure_plot_font() -> None:
    font_manager.fontManager.addfont(str(FONT))
    plt.rcParams["font.family"] = font_manager.FontProperties(
        fname=FONT
    ).get_name()
    plt.rcParams["axes.unicode_minus"] = False


def load_simulation(path: Path) -> SimulationParameters:
    return SimulationParameters(**json.loads(path.read_text(encoding="utf-8")))


def json_ready(value: object) -> object:
    if isinstance(value, dict):
        return {key: json_ready(item) for key, item in value.items()}
    if isinstance(value, list):
        return [json_ready(item) for item in value]
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, (float, np.floating)):
        number = float(value)
        return number if np.isfinite(number) else None
    if isinstance(value, np.integer):
        return int(value)
    return value


def convergence_audit(
    base: SimulationParameters,
    model: ModelParameters,
) -> list[dict[str, object]]:
    reduced = replace(
        base,
        paths=min(base.paths, 160),
        duration=min(base.duration, 360.0),
        burn_in=min(base.burn_in, 180.0),
    )
    cases = (
        ("reference_dt", reduced),
        ("half_dt", replace(reduced, dt=0.5 * reduced.dt)),
        ("independent_seed", replace(reduced, seed=reduced.seed + 2000)),
    )
    return [
        {
            "label": label,
            **compact_result(simulate(parameters, model, keep_trace=False)),
        }
        for label, parameters in cases
    ]


def save_curves(
    entropy: dict[str, object],
    curves: dict[str, dict[str, np.ndarray]],
) -> None:
    REFERENCE.mkdir(parents=True, exist_ok=True)
    with (REFERENCE / "curves.csv").open(
        "w", newline="", encoding="utf-8"
    ) as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(
            [
                "kind",
                "coordinate",
                "target",
                "prepared",
                "auxiliary",
            ]
        )
        for z, target, ratio, fixed in zip(
            entropy["z"],
            entropy["target"],
            entropy["ratio"],
            entropy["fixed_ratio"],
        ):
            writer.writerow(["entropy", z, target, ratio, fixed])
        for name, data in curves.items():
            for x, target, prepared, potential in zip(
                data["x"],
                data["target"],
                data["prepared"],
                data["potential"],
            ):
                writer.writerow([name, x, target, prepared, potential])


def save_figures(
    active: dict[str, object],
    entropy: dict[str, object],
    curves: dict[str, dict[str, np.ndarray]],
) -> None:
    configure_plot_font()
    FIGURES.mkdir(exist_ok=True)
    trace = active["trace"]
    show = trace["time"] <= trace["time"][0] + 100.0
    figure, axes = plt.subplots(1, 3, figsize=(13.4, 4.0))
    axes[0].plot(trace["time"][show], trace["energy"][show], lw=0.9)
    axes[0].axhline(0.25, color="black", ls="--", lw=1)
    axes[0].set(
        xlabel="時間",
        ylabel="局所エネルギー",
        title="M45の直接軌道",
    )
    axes[1].hist(active["ready_energy"], bins=140, density=True)
    axes[1].axvline(0.25, color="black", ls="--", lw=1)
    axes[1].set(
        xlabel="局所エネルギー",
        ylabel="密度",
        title="準備領域のエネルギー",
    )
    axes[2].plot(entropy["z"], entropy["target"], color="black", label="exp(-z)")
    axes[2].plot(
        entropy["z"],
        entropy["ratio"],
        ls="--",
        label="M45位相体積",
    )
    axes[2].set(xlabel="z", ylabel="比", title="捕捉エントロピー比")
    axes[2].legend(fontsize=8)
    for axis in axes:
        axis.grid(alpha=0.2)
    figure.tight_layout()
    figure.savefig(FIGURES / "m45_open_trap_diagnostics.png", dpi=180)
    plt.close(figure)

    figure, axes = plt.subplots(1, 2, figsize=(11.2, 4.2))
    for axis, name in zip(axes, ("harmonic", "double_well")):
        data = curves[name]
        axis.plot(
            data["x"],
            data["target"],
            color="black",
            label="量子基底密度",
        )
        axis.plot(
            data["x"],
            data["prepared"],
            ls="--",
            label="条件付きM45作用素",
        )
        title = "調和型" if name == "harmonic" else "二重井戸型"
        axis.set(xlabel="X", ylabel="密度", title=title)
        axis.grid(alpha=0.2)
        axis.legend(fontsize=8)
    figure.tight_layout()
    figure.savefig(FIGURES / "m45_conditional_ground_comparison.png", dpi=180)
    plt.close(figure)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        type=Path,
        default=ROOT / "configs" / "reference.json",
    )
    parser.add_argument("--skip-convergence", action="store_true")
    args = parser.parse_args()

    simulation = load_simulation(args.config)
    model = ModelParameters()
    active = simulate(simulation, model)
    passive = simulate(
        replace(simulation, seed=simulation.seed + 1),
        replace(model, active_gain=0.0),
        keep_trace=False,
    )
    table = PhaseVolumeTable.build(model)
    entropy = entropy_audit(active["ready_energy"], model, table)
    operator, curves = run_operator_audit(
        active["ready_energy"],
        table,
        OperatorParameters(),
    )
    metrics = {
        "model": "M45_open_quasicritical_preparation",
        "direct_langevin": compact_result(active),
        "passive_control": compact_result(passive),
        "capture_entropy": {
            key: value
            for key, value in entropy.items()
            if key not in {"z", "ratio", "fixed_ratio", "target"}
        },
        "conditional_position_operator": operator,
        "claim_boundary": {
            "direct": "explicit_s_r_langevin_and_phase_volume",
            "conditional": "position_diffusion_slice_scaling_and_marginal_reversibility",
        },
    }
    convergence = (
        [] if args.skip_convergence else convergence_audit(simulation, model)
    )
    REFERENCE.mkdir(parents=True, exist_ok=True)
    (REFERENCE / "metrics.json").write_text(
        json.dumps(json_ready(metrics), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (REFERENCE / "convergence.json").write_text(
        json.dumps(json_ready(convergence), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    save_curves(entropy, curves)
    save_figures(active, entropy, curves)
    print(json.dumps(json_ready(metrics), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
