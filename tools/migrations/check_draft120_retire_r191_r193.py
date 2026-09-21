#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def require(path: str, *tokens: str) -> None:
    text=(ROOT/path).read_text(encoding="utf-8")
    missing=[token for token in tokens if token not in text]
    if missing:
        raise AssertionError(f"{path}: missing draft-120 markers: {missing}")

def forbid(path: str, *tokens: str) -> None:
    text=(ROOT/path).read_text(encoding="utf-8")
    hits=[token for token in tokens if token in text]
    if hits:
        raise AssertionError(f"{path}: stale active R191/R193 mainline wording: {hits}")

def main() -> None:
    for path in (
        "sections/A20_m54_brownian_macrospin_projective_instrument.md",
        "sections/A21_q1_r193_macrospin_bridge.md",
        "tools/verify_r191_macrospin.py",
        "tools/verify_q1_r193_macrospin_bridge.py",
    ):
        if (ROOT/path).exists():
            raise AssertionError(f"draft-120 active retirement target still exists: {path}")

    for path in (
        "notes/superseded_r191_brownian_macrospin_projective_instrument.md",
        "notes/superseded_r193_q1_macrospin_bridge.md",
        "notes/retired_verifiers/verify_r191_macrospin.py",
        "notes/retired_verifiers/verify_q1_r193_macrospin_bridge.py",
    ):
        if not (ROOT/path).exists():
            raise AssertionError(f"draft-120 retired artifact missing: {path}")

    require(
        "sections/02_common_canonical_modules.md",
        "M65/R204D--R204FをQ1/Q2 fixed-goalの現行selector",
        "現行M65実装では",
    )
    require(
        "sections/03_m47_controlled_w_instrument.md",
        r"\varepsilon_{189B}^{\rm dist}",
        r"\varepsilon_{65}^{\rm mid}",
        "M65 decision",
        "Q1-2 | 達成",
    )
    require(
        "sections/04_m54_q2_specializations.md",
        "M65--R181D",
        "2端M65受信機構",
    )
    require(
        "sections/05_m54_setting_pre_receiver.md",
        "現行fixed-goal証人としてA/B両端M65",
    )
    require(
        "PROJECT_STATUS.md",
        "draft-120：R191/R193退役・M65 fixed-goal主線化",
        "R187によるM37のW2制御用信号系＋M65 open selector",
        "A/B二つの物理M65読出し端",
    )
    require(
        "notes/superseded_result_index.md",
        "draft-120で退役したR191/R193測定経路",
        "| R191 |",
        "| R193 |",
    )

    checks={
        "sections/00_overview_and_contents.md":(
            r"\xrightarrow{\mathrm{R191}}",
            r"\mathrm{R191}_A",
            r"\mathrm{R191}_B",
        ),
        "sections/01_scope_and_cycle.md":(
            r"\xrightarrow{\mathrm{R191}}",
            r"\xrightarrow{\mathrm{R193}}",
            "fixed-goalの現行selectorはR191",
        ),
        "sections/03_m47_controlled_w_instrument.md":(
            "R191主線",
            "R193 decision",
            r"\varepsilon_{191}^{\rm mid}",
        ),
        "sections/04_m54_q2_specializations.md":(
            "2端R191",
            "R191--R181D",
        ),
        "sections/05_m54_setting_pre_receiver.md":(
            "現行証人ではR191",
            "A/B両端R191",
        ),
        "sections/08_errors_resources_open_targets.md":(
            "R193の直接decision接続誤差",
            "現行Q2-2はA端R191",
        ),
        "sections/09_conclusion.md":(
            "Q1/Q2の2結果測定はR191へ統一",
            "A端R191で",
        ),
    }
    for path,tokens in checks.items():
        forbid(path,*tokens)

    print("draft120_retire_r191_r193_ok")

if __name__=="__main__":
    main()
