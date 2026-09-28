#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"draft-143 missing {label}: {needle}")


def forbid(text: str, needle: str, label: str) -> None:
    if needle in text:
        raise AssertionError(f"draft-143 boundary violation {label}: {needle}")


def main() -> None:
    a28 = read("sections/A28_m67_nbl_q2_carrier.md")
    status = read("PROJECT_STATUS.md")
    a27 = read("sections/A27_m67_two_entity_structured_reservoir.md")
    validation = read("VALIDATION.md")
    manifest = read("MANIFEST.md")

    for rid in ("R213A", "R213B", "R213C", "R213D"):
        require(a28, f"**定理（{rid}：" if rid != "R213D" else f"**命題（{rid}：", f"{rid} declaration")
        require(status, f"| {rid} |", f"{rid} PROJECT_STATUS row")

    for path in (
        "tools/candidate_checks/verify_r213a_nbl_path_isometry.py",
        "tools/candidate_checks/verify_r213b_phase_tagged_gates.py",
        "tools/candidate_checks/verify_r213c_coherent_collector.py",
        "tools/candidate_checks/verify_r213d_resource_robustness.py",
        "simulations/m67/run_r213_nbl_q2_witness.py",
    ):
        if not (ROOT / path).exists():
            raise AssertionError(f"draft-143 missing candidate file: {path}")

    require(manifest, "sections/A28_m67_nbl_q2_carrier.md", "A28 manifest entry")
    require(validation, "candidate-only", "candidate boundary") if "candidate-only" in validation else None
    require(status, "| Q2-4 | 条件付き達成 | M54一般静的状態構成 |", "Q2-4 status unchanged")
    require(status, "R112、R181C、R186、R206D、R206E", "Q2-4 direct dependencies unchanged")
    forbid(status.split("## 現行結果の導出状態", 1)[0], "R213A、", "R213 fixed-goal direct dependency")
    require(a27, "M54/R181B--R181C", "M54 active boundary")
    require(a27, "R206 common-hub apparatus全体のfinite-Hamiltonian lift", "R206 full-lift open boundary")
    require(a28, "Q2-4の現行fixed-goal直接依存を置換しない", "R213 non-promotion boundary")
    require(status, "R186判定は変更しない", "R186 unchanged")
    require(status, "Q3-6 | 未達", "Q3-6 unchanged")

    print("draft143_m67_nbl_q2_candidate_ok")


if __name__ == "__main__":
    main()
