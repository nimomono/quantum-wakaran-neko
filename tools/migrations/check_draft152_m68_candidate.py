#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def main() -> None:
    ae = read("sections/A31_m68_spatial_information_medium.md")
    status = read("PROJECT_STATUS.md")
    validation = read("VALIDATION.md")
    enhancement = read("ENHANCEMENT_TARGETS.md")
    lineage = read("notes/theory_lineage.md")
    conclusion = read("sections/09_conclusion.md")

    require("R216A：M68 finite-lattice spatial-information medium" in ae, "R216A missing")
    require("R216B：R215C + R215A Nelson closure" in ae, "R216B missing")
    require("R216C：intensive score / reciprocal" in ae, "R216C missing")
    require("R216D：adapted-feedback R214 stability" in ae, "R216D missing")
    require("finite-capacity annealed equivariance" in ae, "annealed equivariance missing")
    require("mean reciprocal load" in ae and "information stress" in ae, "stress/load boundary missing")

    require("| R214A | required" in status, "R214A required status changed")
    require("| R214B | required" in status, "R214B required status changed")
    require("| R215A | candidate" in status, "R215A candidate status missing")
    require("| R215B | candidate" in status, "R215B candidate status missing")
    require("| R215C | candidate" in status, "R215C candidate status missing")
    for rid in ("R216A", "R216B", "R216C", "R216D"):
        require(f"| {rid} | candidate" in status, f"{rid} candidate status missing")

    for name in (
        "verify_r216a_m68_lattice_medium.py",
        "verify_r216b_nelson_closure.py",
        "verify_r216c_capacity_reciprocal_scaling.py",
        "verify_r216d_feedback_equivariance.py",
    ):
        rel = f"tools/candidate_checks/{name}"
        require(rel in validation, f"{name} not registered")
        require((ROOT / rel).is_file(), f"{name} missing")
        require(not (ROOT / "tools" / name).exists(), f"{name} incorrectly promoted to required")

    require("M68 / R216A finite-lattice spatial-information medium [candidate]" in lineage, "M68 lineage missing")
    require("primitive" in enhancement and "M37" in enhancement, "M68 open boundary missing")
    require("M68は現行Q3 required主線をまだ置換しないcandidate" in conclusion, "current-mainline boundary missing")
    require("M_X=m" in ae and "\\mathcal J_{\\rm SI}=\\mathcal J_0" in ae, "parameter matching boundary missing")
    require("Q3-6" in ae, "Q3-6 boundary missing")

    print("draft152_m68_candidate_migration_ok")


if __name__ == "__main__":
    main()
