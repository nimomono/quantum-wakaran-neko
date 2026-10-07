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
    ac = read("sections/A29_m67_dumbbell_q3_tracer.md")
    status = read("PROJECT_STATUS.md")
    validation = read("VALIDATION.md")
    manifest = read("MANIFEST.md")

    require("@number: AD" in ad, "A30 appendix label missing")
    require("R215A：compatible-port equivariance / Bayes score" in ad, "R215A missing")
    require("R215B：spatial-information free-energy identities" in ad, "R215B missing")
    require("R215C" in ad and "本付録では" in ad, "R215C boundary missing")
    require("M68" in ad, "M68 future boundary missing")

    require("| R214A | required" in status, "R214A required status changed")
    require("| R214B | required" in status, "R214B required status changed")
    require("R215A" in status and "candidate" in status, "R215A candidate status missing")
    require("R215B" in status and "candidate" in status, "R215B candidate status missing")

    require(
        "tools/candidate_checks/verify_r215a_compatible_port_score.py" in validation,
        "R215A candidate verifier not registered",
    )
    require(
        "tools/candidate_checks/verify_r215b_spatial_information_free_energy.py" in validation,
        "R215B candidate verifier not registered",
    )
    require("R215C" in manifest and "M68" in manifest, "future boundary absent from manifest")

    require(
        "W_1" in ac and "\\pi_t" in ac,
        "AC.8.1 probability-density bridge not normalized",
    )
    require(
        "\\widetilde\\rho(t)" not in ac,
        "stale undefined tilde-rho remains in AC",
    )

    # Candidate checks must remain non-required.
    require(
        not (ROOT / "tools/verify_r215a_compatible_port_score.py").exists(),
        "R215A verifier incorrectly promoted to required",
    )
    require(
        not (ROOT / "tools/verify_r215b_spatial_information_free_energy.py").exists(),
        "R215B verifier incorrectly promoted to required",
    )

    print("draft150_r215_migration_ok")


if __name__ == "__main__":
    main()
