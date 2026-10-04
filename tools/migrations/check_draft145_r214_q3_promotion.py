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
    enh = read("ENHANCEMENT_TARGETS.md")
    validation = read("VALIDATION.md")

    require(a29, "**定理（R214A：三次元伸縮dumbbellのphase-volume osmotic force）**", "R214A promoted")
    require(a29, "**定理（R214B：finite-bath dumbbellの動的osmotic縮約とQ3-2 compatibility）**", "R214B promoted")
    require(a29, "R209Cは用いない", "R214B small-mass independence")
    require(a29, "Y_t=X_t^M+\epsilon_MV_t^M", "R214B direct small-mass transform")
    require(a29, "\zeta_{\rm db}^{\rm abs}", "R214B absolute covariance ledger")

    require(a27, "R209A：M67 generic local-flow compatibility", "R209A generic")
    require(a27, "R209B：generic finite harmonic bath / Markov--FDT reduction", "R209B generic")
    require(a27, "R210A：phase-invariant generic coherent-load finite-time compatibility", "R210A generic")
    require(a27, "R208D：M67 profileからM64 Q3 lawへのstructural bridge", "R208D dispatch")
    require(a27, "AA.14.2 R214 dumbbell specialization", "R210A dumbbell specialization")

    # PR1 boundary: old results remain active until the retirement PR.
    for rid in ("R208B", "R208C", "R209C"):
        require(ps, f"| {rid} |", f"{rid} retained in PR1")
        if not re.search(rf"\*\*定理（{rid}：", a27):
            raise AssertionError(f"{rid} theorem must remain active in PR1")

    # Promoted verifiers are required and no longer live under candidate_checks.
    for name in (
        "verify_r214a_dumbbell_partition.py",
        "verify_r214b_dumbbell_dynamic_bridge.py",
    ):
        if not (ROOT / "tools" / name).is_file():
            raise AssertionError(f"required verifier missing: {name}")
        if (ROOT / "tools" / "candidate_checks" / name).exists():
            raise AssertionError(f"promoted verifier still candidate: {name}")

    q32 = next(x for x in ps.splitlines() if x.startswith("| Q3-2 |"))
    require(q32, "R214A", "Q3-2 direct dependency")
    require(q32, "R214B", "Q3-2 direct dependency")
    forbid(q32, "R208A--R209C", "Q3-2 old aggregate dependency")
    forbid(q32, "R209C", "Q3-2 old process theorem dependency")

    # Finite-graph fixed goals must not acquire R214.
    for qid in ("Q3-4A", "Q3-4B", "Q3-5"):
        line = next(x for x in ps.splitlines() if x.startswith(f"| {qid} |"))
        forbid(line, "R214", f"{qid} finite-graph boundary")

    require(ps, "| R214A | required", "R214A status")
    require(ps, "| R214B | required", "R214B status")
    require(enh, "R214A--R214BをQ3-2 continuous-tracerのrequired physical bridge", "enhancement sync")
    require(validation, "tools/verify_r214a_dumbbell_partition.py", "validation required path")

    # Global fixed-goal / strengthening states stay unchanged.
    expected = {
        "Q1-1": "達成", "Q1-2": "達成", "Q2-1": "達成", "Q2-2": "達成",
        "Q2-3": "達成", "Q2-4": "条件付き達成", "Q3-1": "達成",
        "Q3-2": "達成", "Q3-4A": "達成", "Q3-4B": "達成",
        "Q3-5": "達成", "Q3-6": "未達",
    }
    for qid, want in expected.items():
        got = status(ps, qid)
        if got != want:
            raise AssertionError(f"{qid}: expected {want}, got {got}")

    require(ps, "R213A--R213D", "R213 candidate retained")
    require(ps, "M0", "M0 retained")
    print("draft145_r214_q3_promotion_ok")


if __name__ == "__main__":
    main()
