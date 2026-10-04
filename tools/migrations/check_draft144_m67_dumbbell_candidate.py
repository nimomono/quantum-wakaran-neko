#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"draft-144 missing {label}: {needle}")


def main() -> None:
    a29 = read("sections/A29_m67_dumbbell_q3_tracer.md")
    a27 = read("sections/A27_m67_two_entity_structured_reservoir.md")
    status = read("PROJECT_STATUS.md")
    validation = read("VALIDATION.md")
    manifest = read("MANIFEST.md")

    require(a29, "@number: AC", "A29 appendix label")
    require(a29, "**定理（R214A：", "R214A declaration")
    require(a29, "**定理（R214B：", "R214B declaration")
    require(a29, "R208B/R208D/R209A--R209C/R210Aをrequiredから外さない", "non-promotion boundary")
    require(a29, "finite-graph Q3-4A/Q3-4B/Q3-5へR214を流用しない", "finite-graph boundary")

    for path in (
        "tools/candidate_checks/verify_r214a_dumbbell_partition.py",
        "tools/candidate_checks/verify_r214b_dumbbell_dynamic_bridge.py",
        "simulations/m67/run_r214_dumbbell_q3_witness.py",
    ):
        if not (ROOT / path).exists():
            raise AssertionError(f"draft-144 missing candidate file: {path}")

    require(a27, "**定理（R208B：phase-volume osmotic forceと有限backreaction）**", "R208B retained")
    require(a27, "## AA.3 phase-volume sectorとsignal backreaction", "AA.3 phase-volume retained")
    require(status, "| Q3-2 | 達成 | M67 continuous-tracer profile |", "Q3-2 status retained")
    q3_row = next(line for line in status.splitlines() if line.startswith("| Q3-2 |"))
    if "R214" in q3_row:
        raise AssertionError("draft-144 must not promote R214 into Q3-2 fixed-goal direct dependency")

    require(status, "| R214A | candidate", "R214A status row")
    require(status, "| R214B | candidate", "R214B status row")
    require(status, "R213A--R213D", "R213 retained")
    require(validation, "verify_r214a_dumbbell_partition.py", "R214A validation entry")
    require(manifest, "sections/A29_m67_dumbbell_q3_tracer.md", "A29 manifest entry")

    print("draft144_m67_dumbbell_candidate_ok")


if __name__ == "__main__":
    main()
