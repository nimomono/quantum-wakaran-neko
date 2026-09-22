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
        raise AssertionError(f"{path}: missing draft-122 markers: {missing}")


def forbid(path: str, *tokens: str) -> None:
    text = read(path)
    hits = [token for token in tokens if token in text]
    if hits:
        raise AssertionError(f"{path}: stale pre-draft-122 dependency wording: {hits}")


def status(path_text: str, qid: str) -> str:
    m = re.search(rf"^\|\s*{re.escape(qid)}\s*\|\s*(達成|条件付き達成|部分達成|未達)\s*\|", path_text, re.M)
    if not m:
        raise AssertionError(f"PROJECT_STATUS.md: status row missing for {qid}")
    return m.group(1)


def main() -> None:
    ps = read("PROJECT_STATUS.md")
    require(
        "PROJECT_STATUS.md",
        "draft-122：現行依存グラフの同期",
        "達成判定で直接参照する定理・interfaceだけを列挙する",
        "| Q1-2 | 達成 |",
        "| Q2-2 | 達成 |",
        "R112、R180C、R181D、R204D--R204E",
    )
    for qid, want in {
        "Q1-1": "達成",
        "Q1-2": "達成",
        "Q2-1": "達成",
        "Q2-2": "達成",
        "Q2-3": "達成",
        "Q2-4": "条件付き達成",
        "Q3-4A": "達成",
        "Q3-4B": "達成",
        "Q3-5": "達成",
        "Q3-6": "未達",
    }.items():
        got = status(ps, qid)
        if got != want:
            raise AssertionError(f"{qid}: expected {want}, got {got}")

    require(
        "sections/A1_common_action_finite_basis.md",
        "Q1/Q2の現行2結果形成はM65/R204D--R204F",
        "結果成分受渡しはR181D",
        "作用殻型代替研究線",
    )
    forbid(
        "sections/A1_common_action_finite_basis.md",
        "Born型結果生成はM54整合状態構成のR164へ分離する",
        "Q2-3ではM54静的状態構成のR164/R190/R179/R170",
        "Born型状態数はR164、静的平方根kernelはR161",
    )

    require(
        "sections/03_m47_controlled_w_instrument.md",
        "Q3の実在粒子位置はM37/R86からM64/R203A--R203Dを介してR161/R185",
        "| Q1-2 | 達成 | R140、R143--R144、R181D、R187",
    )
    forbid(
        "sections/03_m47_controlled_w_instrument.md",
        "Q3の実在粒子位置はR164--R161/R162",
        "| Q1-2 | 達成 | R140、R143--R144、R168、",
    )

    require(
        "sections/06_m37_spatial_envelope.md",
        "Q2はM54の永続記憶部とM65/R181D受信機構",
        "M64/R203B--R203Dのinitial preparationと位置更新則",
    )
    forbid(
        "sections/06_m37_spatial_envelope.md",
        "固定時刻の一般結果成分測定機構はM54静的/R170",
        "初期M54空間状態構成位置",
    )

    require(
        "sections/A7_q3_completion_proofs.md",
        "位置読出しは付録YのM64/R203D finite-graph tracer",
        "\\varepsilon_{64,G}",
        "1/[4(1+\\delta)]",
    )
    forbid(
        "sections/A7_q3_completion_proofs.md",
        "M54空間/R161--R184",
        "M54空間/R184",
        "\\varepsilon_{184}",
    )

    require(
        "sections/07_q3_finite_graph_phenomena.md",
        "R123--R125とR182の完全証明は付録G",
        "完全な干渉代数証明は付録G.4",
    )
    forbid(
        "sections/07_q3_finite_graph_phenomena.md",
        "完全証明は付録F、G",
        "付録F.7、G.4",
    )

    require(
        "sections/08_errors_resources_open_targets.md",
        "達成判定で直接参照する結果だけを列挙",
        "- Q2-2：M54静的状態構成と2端M65経路を使う。根拠結果はR112、R180C、R181D、M65/R204D--R204E。",
    )
    forbid(
        "sections/08_errors_resources_open_targets.md",
        "根拠結果はR112、R180A、R180C、R181B、R181C、R181D、M65/R204D--R204E",
    )

    for path in [
        "sections/A12_common_action_shell_state_count.md",
        "sections/A11_common_collision_bath_thermodynamics.md",
        "sections/A14_m54_spatial_moving_matching.md",
    ]:
        if not (ROOT / path).exists():
            raise AssertionError(f"{path}: retirement was pulled into draft-122 unexpectedly")
    require("sections/A14_m54_spatial_moving_matching.md", "R184")
    require("sections/A11_common_collision_bath_thermodynamics.md", "R170")

    print("draft122_active_dependency_sync_ok")


if __name__ == "__main__":
    main()
