#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"{label}: missing {needle!r}")


def forbid(text: str, needle: str, label: str) -> None:
    if needle in text:
        raise AssertionError(f"{label}: stale {needle!r}")


def status(text: str, qid: str) -> str:
    m = re.search(rf"^\|\s*{re.escape(qid)}\s*\|\s*(達成|条件付き達成|部分達成|未達)\s*\|", text, re.M)
    if not m:
        raise AssertionError(f"status row missing: {qid}")
    return m.group(1)


def main() -> None:
    a27 = read("sections/A27_m67_two_entity_structured_reservoir.md")
    a29 = read("sections/A29_m67_dumbbell_q3_tracer.md")
    ps = read("PROJECT_STATUS.md")
    idx = read("notes/superseded_result_index.md")
    note = read("notes/superseded_r208bc_r209c_q3_phase_volume_bridge.md")

    for rid in ("R208B", "R208C", "R209C"):
        forbid(a27, f"**定理（{rid}：", f"{rid} theorem retired")
        if re.search(rf"^\|\s*{rid}\s*\|", ps, re.M):
            raise AssertionError(f"{rid} must be absent from current result table")
        require(idx, f"| {rid} |", f"{rid} superseded index")
        require(note, rid, f"{rid} retirement note")

    require(a27, "**定理（R208D：M67 profileからM64 Q3 lawへのstructural bridge）**", "R208D retained")
    require(a27, "**定理（R209A：M67 generic local-flow compatibility）**", "R209A retained")
    require(a27, "**定理（R209B：generic finite harmonic bath / Markov--FDT reduction）**", "R209B retained")
    require(a27, "**定理（R210A：phase-invariant generic coherent-load finite-time compatibility）**", "R210A retained")
    require(a29, "**定理（R214A：三次元伸縮dumbbellのphase-volume osmotic force）**", "R214A retained")
    require(a29, "**定理（R214B：finite-bath dumbbellの動的osmotic縮約とQ3-2 compatibility）**", "R214B retained")

    for path in (
        "tools/verify_r208_phase_volume_backreaction.py",
        "tools/verify_r208_local_moving_bath.py",
        "tools/verify_r209c_process_compatibility.py",
        "simulations/m67/run_full_compatibility_witness.py",
    ):
        if (ROOT / path).exists():
            raise AssertionError(f"retired active file still exists: {path}")

    if not (ROOT / "tools/verify_r208_m64_reduction.py").is_file():
        raise AssertionError("R208D profile-dispatch verifier missing")

    q32 = status_line(ps, "Q3-2")
    require(q32, "R214A", "Q3-2 R214A")
    require(q32, "R214B", "Q3-2 R214B")
    forbid(q32, "R208B", "Q3-2 retired result")
    forbid(q32, "R208C", "Q3-2 retired result")
    forbid(q32, "R209C", "Q3-2 retired result")

    for qid in ("Q3-4A", "Q3-4B", "Q3-5"):
        line = status_line(ps, qid)
        forbid(line, "R214", f"{qid} finite-graph must not use R214")

    expected = {
        "Q1-1": "達成", "Q1-2": "達成",
        "Q2-1": "達成", "Q2-2": "達成", "Q2-3": "達成", "Q2-4": "条件付き達成",
        "Q3-1": "達成", "Q3-2": "達成", "Q3-4A": "達成", "Q3-4B": "達成",
        "Q3-5": "達成", "Q3-6": "未達",
    }
    for qid, want in expected.items():
        got = status(ps, qid)
        if got != want:
            raise AssertionError(f"{qid}: expected {want}, got {got}")

    require(ps, "R213A--R213D", "R213 candidate retained")
    require(ps, "M0", "M0 retained")
    print("draft146_retire_legacy_q3_phase_volume_bridge_ok")


if __name__ == "__main__":
    main()
