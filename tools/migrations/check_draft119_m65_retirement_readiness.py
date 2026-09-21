#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def require(path: str, *tokens: str) -> None:
    text=(ROOT/path).read_text(encoding="utf-8")
    missing=[token for token in tokens if token not in text]
    if missing:
        raise AssertionError(f"{path}: missing draft-119 markers: {missing}")

def forbid(path: str, *tokens: str) -> None:
    text=(ROOT/path).read_text(encoding="utf-8")
    hits=[token for token in tokens if token in text]
    if hits:
        raise AssertionError(f"{path}: legacy mainline wording remains: {hits}")

def main() -> None:
    require(
        "sections/A26_m65_phase_volume_projective_instrument.md",
        r"A_\pm\geq0",
        r"A_\Sigma=A_++A_->0",
        "decision終了時の有限record/latch",
        "R112型の有限局所record",
        "Q1 retirement-readiness合成",
        r"\mathrm{R189A}",
        "空操作対照",
    )
    require(
        "sections/A12_common_action_shell_state_count.md",
        "代替作用殻研究線",
        "現行Q1/Q2 binary-selector主線へこの台帳を重複加算しない",
        "R164--R190--R170の静的作用殻経路はこの現行Q2-4主線へ戻さない",
    )
    forbid(
        "sections/A12_common_action_shell_state_count.md",
        "R189A--R189Cは同じR164/R170選択原理",
        "正則化容量 $A_{u,b}^\\delta$ をR164作用殻からR190/R179静的選択へ渡す",
    )

    # This PR prepares retirement but must not retire the current witnesses yet.
    for path in (
        "sections/A20_m54_brownian_macrospin_projective_instrument.md",
        "sections/A21_q1_r193_macrospin_bridge.md",
        "tools/verify_r191_macrospin.py",
        "tools/verify_q1_r193_macrospin_bridge.py",
    ):
        if not (ROOT/path).exists():
            raise AssertionError(f"draft-119 must keep current R191/R193 artifact: {path}")

    require(
        "README.md",
        "exact endpoint",
        "R112型record/latch",
        "R191/R193",
    )
    require(
        "PROJECT_STATUS.md",
        "draft-119：M65 retirement-readiness整理",
    )

    print("draft119_m65_retirement_readiness_ok")

if __name__ == "__main__":
    main()
