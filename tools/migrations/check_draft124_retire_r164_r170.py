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
        raise AssertionError(f"{path}: missing draft-124 markers: {missing}")


def forbid(path: str, *tokens: str) -> None:
    text = read(path)
    hits = [token for token in tokens if token in text]
    if hits:
        raise AssertionError(f"{path}: stale action-shell route wording: {hits}")


def status(path_text: str, qid: str) -> str:
    m = re.search(
        rf"^\|\s*{re.escape(qid)}\s*\|\s*(達成|条件付き達成|部分達成|未達)\s*\|",
        path_text,
        re.M,
    )
    if not m:
        raise AssertionError(f"PROJECT_STATUS.md: status row missing for {qid}")
    return m.group(1)


def main() -> None:
    if (ROOT / "sections/A12_common_action_shell_state_count.md").exists():
        raise AssertionError("retired Appendix L still exists in active sections")

    active_hits = []
    for path in sorted((ROOT / "sections").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        stale = [token for token in ("R164", "R170", "R190") if token in text]
        if stale:
            active_hits.append((path.name, stale))
    if active_hits:
        raise AssertionError(f"retired action-shell IDs remain in active sections: {active_hits}")

    require(
        "sections/02_common_canonical_modules.md",
        "## 2.7 Q1/Q2局所構造からQ3空間信号への持ち上げ",
        r"R_i^\delta",
        r"\pi_i^\delta",
        "M64/R203Dがfinite-graph activityとgeneratorを与える",
        "## 2.8 R161の共通整合・Markov経路法則とM64/R162の物理・参照実現",
    )
    forbid(
        "sections/02_common_canonical_modules.md",
        "Born型殻状態数",
        "排他的2作用殻を置く",
    )

    require(
        "sections/A11_common_collision_bath_thermodynamics.md",
        "## K.2 R161の証明：確率流・活動量整合",
        "### K.2.1 有限状態canonical Markov経路法則の存在と一意性",
        "### K.2.2 活動量--親和力表示とR161実現同値",
        "## K.3 R162の証明：R161経路法則の独立Poisson-jump実現",
        "## K.4 境界と強化結果",
    )
    forbid(
        "sections/A11_common_collision_bath_thermodynamics.md",
        "静的 詳細釣り合い特殊化",
        "吸収指針変数固定",
        "作用殻sampler",
    )

    require(
        "sections/A6_common_signal_statistics.md",
        "@title: 共通信号集団と状態方向平均の証明",
        "R135とR168は集団統計を評価する定理",
        "## F.5 制御されたM37の共通位相と階数1診断",
    )
    forbid(
        "sections/A6_common_signal_statistics.md",
        "作用殻消去表示",
        "固定時刻代替診断",
    )

    require(
        "sections/03_m47_controlled_w_instrument.md",
        "## 3.6 M65のQ1二結果特殊化",
        "## 3.9 W型空間profileの有限コントラスト診断",
        "## 3.11 結果記録の責務",
        "現行Q1のBorn結果と測定後状態はM65/R181Dだけで形成",
    )

    require(
        "sections/08_errors_resources_open_targets.md",
        "## 8.8 現行regularizationの資源境界",
        "退役した旧作用殻測定経路",
    )

    ps = read("PROJECT_STATUS.md")
    require(
        "PROJECT_STATUS.md",
        "draft-124：R164/R170作用殻測定経路のactive paper退役",
        "R135/R168、R161/R162、R179、R181D、R192",
    )
    current_results = ps.split("### Q3結果", 1)[1].split("## 物理的解釈と境界", 1)[0]
    for rid in ("R164", "R170", "R190A--R190C"):
        if re.search(rf"^\|\s*{re.escape(rid)}\s*\|", current_results, re.M):
            raise AssertionError(f"PROJECT_STATUS.md: retired row remains: {rid}")
    for rid in ("R161", "R162", "R168", "R179"):
        if f"| {rid} |" not in ps:
            raise AssertionError(f"PROJECT_STATUS.md: active result missing: {rid}")

    for qid, want in {
        "Q1-1": "達成",
        "Q1-2": "達成",
        "Q2-1": "達成",
        "Q2-2": "達成",
        "Q2-3": "達成",
        "Q2-4": "条件付き達成",
        "Q3-1": "達成",
        "Q3-2": "達成",
        "Q3-4A": "達成",
        "Q3-4B": "達成",
        "Q3-5": "達成",
        "Q3-6": "未達",
    }.items():
        got = status(ps, qid)
        if got != want:
            raise AssertionError(f"{qid}: expected {want}, got {got}")

    require(
        "notes/superseded_r164_q1q2_measurement_role.md",
        "R164作用殻状態数結果の退役記録",
        "ce33c7e1722011261d87018790cf81893af03852",
        "完全な旧証明はGit履歴を正本",
    )
    require(
        "notes/superseded_r190_r170_measurement_path.md",
        "draft-124ではR164作用殻状態数とR170吸収pointerをactive paperから完全に退役",
        "d6657b3cebc5f417a998ae1a2628e3873e4a90b0",
    )
    require(
        "notes/superseded_result_index.md",
        "draft-124でactive paperから退役した作用殻測定経路",
        "| R164 |",
        "| R170 |",
    )

    forbid("README.md", "R164", "R170", "R190")
    require("README.md", "M65", "M64")

    print("draft124_retire_r164_r170_ok")


if __name__ == "__main__":
    main()
