#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]

def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")

def require(path: str, *tokens: str) -> None:
    text = read(path)
    missing = [token for token in tokens if token not in text]
    if missing:
        raise AssertionError(f"{path}: missing draft-126 markers: {missing}")

def status(text: str, qid: str) -> str:
    m = re.search(
        rf"^\|\s*{re.escape(qid)}\s*\|\s*(達成|条件付き達成|部分達成|未達)\s*\|",
        text,
        re.M,
    )
    if not m:
        raise AssertionError(f"PROJECT_STATUS.md: status row missing for {qid}")
    return m.group(1)

def main() -> None:
    require(
        "sections/A26_m65_phase_volume_projective_instrument.md",
        "M66",
        "R205A",
        "R206A",
        "R206D",
        "現行fixed-goal依存からR181D/R192を外さない",
        "R186",
    )
    for path in (
        "tools/candidate_checks/verify_m66_common_phase_volume.py",
        "tools/candidate_checks/verify_r206_multi_outcome_sampler.py",
        "tools/candidate_checks/verify_r206_uniform_passive_scaling.py",
        "tools/candidate_checks/verify_r206_q2_resource_scaling.py",
    ):
        if not (ROOT / path).exists():
            raise AssertionError(f"missing candidate verifier: {path}")

    ps = read("PROJECT_STATUS.md")
    expected = {
        "Q2-1": "達成",
        "Q2-2": "達成",
        "Q2-3": "達成",
        "Q2-4": "条件付き達成",
    }
    for qid, want in expected.items():
        got = status(ps, qid)
        if got != want:
            raise AssertionError(f"{qid}: expected {want}, got {got}")

    require(
        "sections/01_scope_and_cycle.md",
        "M66/R206",
        "現行主線は変更しない",
    )
    require(
        "sections/08_errors_resources_open_targets.md",
        "M66/R206 candidate",
        "R186",
    )
    require(
        "notes/theory_lineage.md",
        "M66 / R205--R206",
        "candidate",
    )
    require(
        "MANIFEST.md",
        "draft-126",
        "M66",
        "R206",
    )

    print("draft126_m66_r206_candidate_ok")

if __name__ == "__main__":
    main()
