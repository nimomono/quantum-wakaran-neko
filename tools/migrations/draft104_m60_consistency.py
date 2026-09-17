#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

FORBIDDEN = {
    "sections/00_overview_and_contents.md": ["M57"],
    "sections/02_common_canonical_modules.md": ["M57"],
    "sections/06_m37_spatial_envelope.md": ["M57"],
    "sections/07_q3_finite_graph_phenomena.md": ["M57", r"\varepsilon_{57}"],
    "sections/08_errors_resources_open_targets.md": ["M57", r"\\varepsilon_{57}", "C_{57}"],
    "sections/09_conclusion.md": ["M57"],
}

REQUIRED = {
    "sections/00_overview_and_contents.md": ["M60", "R199A", "R198A--R198D/R197A"],
    "sections/02_common_canonical_modules.md": ["M60/R198A--R198D", "R199A", "M60 chiral-medium moving-bath tracer"],
    "sections/06_m37_spatial_envelope.md": ["R198A--R198D/R197A", "R199A・R196A--R196C"],
    "sections/07_q3_finite_graph_phenomena.md": [r"\varepsilon_{\rm path}^{60}", "M60/R196C"],
    "sections/08_errors_resources_open_targets.md": [r"\varepsilon_{\rm tr}^{60}", "M60 transport--R161--R185", "R199A"],
    "sections/09_conclusion.md": ["M60", "R199A", "R198A--R198D/R197A"],
    "VALIDATION.md": ["tools/candidate_checks/verify_chiral_shell_response.py", "M60固有文字列契約を追加しない"],
    "MANIFEST.md": ["tools/candidate_checks/verify_chiral_shell_response.py", "draft-104：M60 post-merge consistency cleanup"],
    "notes/r161_q1_q2_q3_realization_equivalence.md": ["M60 unified-chiral-medium moving-bath tracer"],
    "notes/brownian_spin_q1_q3_unification.md": ["draft-103以後、現行Q3-2のミクロ物理主線"],
}


def main() -> None:
    failures: list[str] = []

    for rel, needles in FORBIDDEN.items():
        text = (ROOT / rel).read_text(encoding="utf-8")
        for needle in needles:
            if needle in text:
                failures.append(f"{rel}: forbidden current-model marker remains: {needle}")

    for rel, needles in REQUIRED.items():
        text = (ROOT / rel).read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                failures.append(f"{rel}: required M60 marker missing: {needle}")

    if failures:
        for failure in failures:
            print("ERROR:", failure)
        raise SystemExit(1)

    print("draft104_m60_consistency_ok")


if __name__ == "__main__":
    main()
