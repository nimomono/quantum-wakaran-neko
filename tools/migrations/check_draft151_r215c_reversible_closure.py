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
    ad = read("sections/A30_m67_spatial_information_free_energy.md")
    status = read("PROJECT_STATUS.md")
    validation = read("VALIDATION.md")
    enhancement = read("ENHANCEMENT_TARGETS.md")
    lineage = read("notes/theory_lineage.md")

    require("R215C：可逆information-free-energy closure" in ad, "R215C section missing")
    require("R215C：reversible information-free-energy closure" in ad, "R215C theorem missing")
    require("R215C local information stress" in ad, "R215C local stress lemma missing")
    require("R215C Madelung closure" in ad, "R215C Madelung theorem missing")
    require("R215C Schrödinger representation" in ad, "R215C Schrödinger theorem missing")
    require("Q3-6の未達課題" in ad, "circulation/Q3-6 boundary missing")

    require("| R214A | required" in status, "R214A required status changed")
    require("| R214B | required" in status, "R214B required status changed")
    require("| R215A | candidate" in status, "R215A candidate status missing")
    require("| R215B | candidate" in status, "R215B candidate status missing")
    require("| R215C | candidate" in status, "R215C candidate status missing")

    require(
        "tools/candidate_checks/verify_r215c_reversible_information_closure.py" in validation,
        "R215C candidate verifier not registered",
    )
    require(
        not (ROOT / "tools/verify_r215c_reversible_information_closure.py").exists(),
        "R215C verifier incorrectly promoted to required",
    )
    require("M68" in enhancement and "後続課題" in enhancement, "M68 future boundary missing")
    require(
        "R215C reversible medium closure / Schrödinger representation [candidate]" in lineage,
        "R215C lineage not promoted to candidate",
    )
    require(
        "M68 finite-Hamiltonian joint medium/tracer parent [future]" in lineage,
        "M68 future lineage missing",
    )
    require(
        "$M_X=m$ / $\\mathcal J_{\\rm SI}=\\mathcal J_0$ matching" in ad,
        "parameter-matching boundary missing",
    )

    print("draft151_r215c_migration_ok")


if __name__ == "__main__":
    main()
