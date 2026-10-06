#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require(cond: bool, message: str) -> None:
    if not cond:
        raise AssertionError(message)


def main() -> None:
    a29 = read("sections/A29_m67_dumbbell_q3_tracer.md")
    status = read("PROJECT_STATUS.md")
    enh = read("ENHANCEMENT_TARGETS.md")
    v214b = read("tools/verify_r214b_dumbbell_dynamic_bridge.py")
    v210a = read("tools/verify_r210a_m67_coherent_compatibility.py")
    q3 = read("sections/07_q3_finite_graph_phenomena.md")

    require("generic density/flow port" in a29, "generic R214 port declaration missing")
    require(
        "generic port phase-volume / reciprocal mean force" in a29,
        "generic R214A theorem missing",
    )
    require(
        "generic density/flow-port動的osmotic縮約" in a29,
        "generic R214B theorem missing",
    )
    require(
        "port-stabilityからscore/drift-stability" in a29,
        "port stability lemma missing",
    )
    require("Stratonovich" in a29 and "Itô" in a29,
            "stochastic convention boundary missing")

    core = (
        a29.split("## AC.8 R214B", 1)[1]
        .split("### AC.8.1 current M37/M64 specialization", 1)[0]
    )
    for stale in ("M37", "M64", "R210A", "N_0"):
        require(
            stale not in core,
            f"source-specific dependency remains in generic R214B core: {stale}",
        )

    spec = (
        a29.split("### AC.8.1 current M37/M64 specialization", 1)[1]
        .split("## AC.9", 1)[0]
    )
    require(
        "R210A" in spec and "R209A" in spec and "M64" in spec,
        "current M37/M64 specialization not preserved",
    )

    require("| R214A | required" in status, "R214A required status changed")
    require("| R214B | required" in status, "R214B required status changed")
    require("| M37 |" in status and "| M64 |" in status, "M37/M64 model rows missing")
    require(
        "R214 generic density/flow port一般化" in status,
        "draft-149 project status entry missing",
    )
    require(
        "generic density/flow port theorem" in enh,
        "enhancement target not synchronized",
    )

    require(
        "relative_load" not in v214b and "n0 =" not in v214b,
        "M37 N0 load regression still lives in R214B verifier",
    )
    require(
        "qload" in v210a and "dumbbell" in v210a,
        "M37-specific dumbbell load regression missing from R210A verifier",
    )

    for qid in ("Q3-4A", "Q3-4B", "Q3-5"):
        line = next(x for x in status.splitlines() if x.startswith(f"| {qid} |"))
        require("R214" not in line, f"{qid} finite-graph boundary changed")
    require("R208D" in q3 and "R214" in q3,
            "Q3 continuous/finite-graph split lost")

    require("| Q3-1 | 達成 |" in status, "Q3-1 status changed")
    require("| Q3-2 | 達成 |" in status, "Q3-2 status changed")
    require("| Q3-6 | 未達 |" in status, "Q3-6 status changed")
    require("| Q2-4 | 条件付き達成 |" in status, "Q2-4 status changed")

    print("draft149_r214_generic_ports_ok")


if __name__ == "__main__":
    main()
