"""Analysis helpers for M45 trajectories."""

from __future__ import annotations

import numpy as np


def monotone_hazard_score(result: dict[str, object]) -> dict[str, float]:
    centers = np.asarray(result["hazard_centers"])
    rates = np.asarray(result["hazard_rate"])
    occupancy = np.asarray(result["hazard_occupancy"])
    valid = (
        np.isfinite(rates)
        & (occupancy > 2.0)
        & (centers >= 0.22)
        & (centers <= 0.32)
    )
    if np.sum(valid) < 4:
        return {"correlation": float("nan"), "upper_lower_ratio": float("nan")}
    selected_centers = centers[valid]
    selected_rates = rates[valid]
    correlation = float(np.corrcoef(selected_centers, selected_rates)[0, 1])
    midpoint = float(np.median(selected_centers))
    lower = float(np.mean(selected_rates[selected_centers <= midpoint]))
    upper = float(np.mean(selected_rates[selected_centers > midpoint]))
    return {
        "correlation": correlation,
        "upper_lower_ratio": upper / max(lower, 1.0e-12),
    }


def compact_result(result: dict[str, object]) -> dict[str, object]:
    return {
        "simulation_parameters": result["simulation_parameters"],
        "model_parameters": result["model_parameters"],
        "summary": result["summary"],
        "energy_balance": result["energy_balance"],
        "hazard_monotonicity": monotone_hazard_score(result),
    }
