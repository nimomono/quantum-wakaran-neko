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
        raise AssertionError(f"{path}: missing draft-121 markers: {missing}")


def forbid(path: str, *tokens: str) -> None:
    text = read(path)
    hits = [token for token in tokens if token in text]
    if hits:
        raise AssertionError(f"{path}: stale pre-draft-121 wording: {hits}")


def status(path_text: str, qid: str) -> str:
    m = re.search(rf"^\|\s*{re.escape(qid)}\s*\|\s*(達成|条件付き達成|部分達成|未達)\s*\|", path_text, re.M)
    if not m:
        raise AssertionError(f"PROJECT_STATUS.md: status row missing for {qid}")
    return m.group(1)


def main() -> None:
    ps = read("PROJECT_STATUS.md")
    require(
        "PROJECT_STATUS.md",
        "draft-121：固定目標の一試行物理interface原則への統一",
        "### 共通達成判定規則",
        "次試行renewal",
    )

    expected = {
        "Q2-1": "達成",
        "Q2-2": "達成",
        "Q2-3": "達成",
        "Q2-4": "条件付き達成",
        "Q3-4A": "達成",
        "Q3-4B": "達成",
        "Q3-5": "達成",
        "Q3-6": "未達",
    }
    for qid, want in expected.items():
        got = status(ps, qid)
        if got != want:
            raise AssertionError(f"{qid}: expected {want}, got {got}")

    require(
        "PROJECT_STANCE.md",
        "一試行内で明示的な物理interface",
        "次試行へのrenewal",
        "現行Q2-4はこの例外",
    )
    require(
        "PROJECT_GUIDE.md",
        "固定有限深さでは",
        "同一試行中に使用済み補助自由度",
        "解析上の状態ベクトル",
        "Q2-4の一様有限規則",
    )
    require(
        "sections/04_m54_q2_specializations.md",
        "Q2-1では、実際の1試行末端信号",
        "固定3入力の二段ゲート合成として達成",
    )
    require(
        "sections/05_m54_setting_pre_receiver.md",
        "同じ一試行の有限な順序付き操作窓",
        "固定一重項・固定有限設定族・非空間分離という固定範囲でQ2-2を達成",
    )
    require(
        "sections/07_q3_finite_graph_phenomena.md",
        "従ってQ3-4Aは達成である",
        "従ってQ3-4Bは達成である",
        "Q3-5は達成である",
    )
    require(
        "sections/08_errors_resources_open_targets.md",
        "固定目標上の未完成事項は、Q3-6の位相量子化とQ2-4の一様装置族・資源条件",
        "Q2-4は条件付き達成",
    )
    require(
        "README.md",
        "固定目標は、その目標が要求する現象を一試行内で明示的な物理interface",
        "固定目標上の未完成はQ2-4",
    )

    forbid(
        "sections/04_m54_q2_specializations.md",
        "Q2-1は条件付き達成を維持",
        "Q2-3も同じ理由で条件付き達成",
    )
    forbid(
        "sections/05_m54_setting_pre_receiver.md",
        "Q2-2の条件付き達成ラベルは維持",
    )
    forbid(
        "sections/07_q3_finite_graph_phenomena.md",
        "Q3-4Aは条件付き達成",
        "Q3-4Bは条件付き達成",
        "Q3-5は改訂後の固定範囲で条件付き達成",
    )
    forbid(
        "sections/08_errors_resources_open_targets.md",
        "Q2-1/Q2-3の末端M65--R181Dと永続記憶部の単一装置統合",
    )

    print("draft121_single_trial_fixed_goal_policy_ok")


if __name__ == "__main__":
    main()
