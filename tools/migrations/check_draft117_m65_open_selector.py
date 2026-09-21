#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

REQUIRED = {
    "sections/A26_m65_phase_volume_projective_instrument.md": (
        "@status: Q1/Q2二結果射影用の現行canonical open selector model",
        r"k_{+\to H}=k_{-\to H}=\Lambda",
        "R204E：M65はbinary selector contractを満たす",
        "R204Bのphase-volume chamber、R204CのHamiltonian--Brownian lift",
    ),
    "sections/A16_m54_projector_tree_receiver.md": (
        "## P.2 共通binary selector contract",
        "R181Dの結論はselectorの内部物理に依存しない",
    ),
    "sections/02_common_canonical_modules.md": (
        "### 2.9 M65：3状態open binary selector",
        "## 2.14 R181D：selector非依存の段階的射影選別・測定後状態受渡し",
    ),
    "sections/05_m54_setting_pre_receiver.md": (
        "binary selector",
        "現行証人ではR191",
    ),
    "tools/candidate_checks/README.md": (
        "M65本体の3状態open selectorはdraft-117で正本へ昇格",
    ),
}

FORBIDDEN = {
    "sections/A26_m65_phase_volume_projective_instrument.md": (
        "promotion gate",
        "replacement candidate",
        "R204Cは本draftのpromotion gate",
    ),
    "sections/A16_m54_projector_tree_receiver.md": (
        "## P.2 R191節点契約",
    ),
    "sections/01_scope_and_cycle.md": (
        "M65 phase-volume projective instrument replacement candidate",
    ),
    "sections/08_errors_resources_open_targets.md": (
        "## M65 candidate の誤差・資源台帳",
    ),
    "simulations/README.md": (
        "promotion前の次段",
    ),
}

def main() -> None:
    for rel, tokens in REQUIRED.items():
        text=(ROOT/rel).read_text(encoding="utf-8")
        missing=[token for token in tokens if token not in text]
        if missing:
            raise AssertionError(f"{rel}: missing draft-117 synchronization markers: {missing}")

    for rel, tokens in FORBIDDEN.items():
        text=(ROOT/rel).read_text(encoding="utf-8")
        hits=[token for token in tokens if token in text]
        if hits:
            raise AssertionError(f"{rel}: legacy draft-114 candidate wording remains: {hits}")

    candidate_dir=ROOT/"tools"/"candidate_checks"
    m65=sorted(p.name for p in candidate_dir.glob("verify_m65_*.py"))
    expected=[
        "verify_m65_brownian_reduction.py",
        "verify_m65_matched_conductance.py",
        "verify_m65_phase_volume_partition.py",
    ]
    if m65 != expected:
        raise AssertionError(f"unexpected M65 candidate checks: {m65}")

    required=ROOT/"tools"/"verify_m65_open_selector.py"
    if not required.exists():
        raise AssertionError("required M65 open-selector verifier is missing")

    print("draft117_m65_open_selector_migration_ok")


if __name__ == "__main__":
    main()
