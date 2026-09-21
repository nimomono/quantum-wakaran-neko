#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

ACTIVE_PATHS = (
    "PROJECT_STANCE.md",
    "PROJECT_GUIDE.md",
    "ENHANCEMENT_TARGETS.md",
    "sections/01_scope_and_cycle.md",
    "sections/02_common_canonical_modules.md",
    "sections/03_m47_controlled_w_instrument.md",
    "sections/08_errors_resources_open_targets.md",
    "sections/09_conclusion.md",
    "sections/A11_common_collision_bath_thermodynamics.md",
    "sections/A25_m64_three_entity_open_q3_model.md",
    "simulations/README.md",
    "notes/brownian_spin_q1_q3_unification.md",
)

FORBIDDEN = ("採用open", "採用開放", "採用ミクロ方程式")


def main() -> None:
    terminology = (ROOT / "TERMINOLOGY.md").read_text(encoding="utf-8")
    required = (
        "直接定めた開放ミクロ方程式",
        "開放ミクロ方程式として直接定める",
        "Hamiltonian浴から導出した開放方程式",
    )
    missing = [token for token in required if token not in terminology]
    if missing:
        raise AssertionError(f"TERMINOLOGY.md: missing standard open-equation wording: {missing}")

    status = (ROOT / "PROJECT_STATUS.md").read_text(encoding="utf-8")
    status_required = (
        "規約を満たす開放ミクロ方程式を基本方程式として直接定めてもよい",
        "開放古典ミクロ方程式を基本方程式として直接定めることを許す",
        "開放ミクロ方程式として直接定める部分",
        "直接定めた開放SDEに対する厳密結果",
    )
    missing_status = [token for token in status_required if token not in status]
    if missing_status:
        raise AssertionError(f"PROJECT_STATUS.md: current terminology not synchronized: {missing_status}")

    for rel in ACTIVE_PATHS:
        text = (ROOT / rel).read_text(encoding="utf-8")
        hits = [token for token in FORBIDDEN if token in text]
        if hits:
            raise AssertionError(f"{rel}: legacy adopted-open compound remains: {hits}")

    print("draft116_open_equation_terminology_ok")


if __name__ == "__main__":
    main()
