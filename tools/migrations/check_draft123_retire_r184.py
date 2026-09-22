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
        raise AssertionError(f"{path}: missing draft-123 markers: {missing}")


def forbid(path: str, *tokens: str) -> None:
    text = read(path)
    hits = [token for token in tokens if token in text]
    if hits:
        raise AssertionError(f"{path}: stale R184 active wording: {hits}")


def status(path_text: str, qid: str) -> str:
    m = re.search(rf"^\|\s*{re.escape(qid)}\s*\|\s*(達成|条件付き達成|部分達成|未達)\s*\|", path_text, re.M)
    if not m:
        raise AssertionError(f"PROJECT_STATUS.md: status row missing for {qid}")
    return m.group(1)


def main() -> None:
    active_hits = []
    for path in sorted((ROOT / "sections").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if "R184" in text or "\\varepsilon_{184}" in text:
            active_hits.append(path.name)
    if active_hits:
        raise AssertionError(f"R184 remains in active sections: {active_hits}")

    require(
        "sections/A14_m54_spatial_moving_matching.md",
        "@title: R161空間参照過程とNelson型縮約",
        "## N.4 R161 後退率と前後平均微分",
        "## N.5 有限格子の前後速度",
        "## N.6 R185の時間対称Newton則と明示格子誤差",
        "## N.7 Q3-2の達成境界",
        "M64/R203A--R203DがM37 signalからR161過程への物理接続を担う",
    )
    forbid(
        "sections/A14_m54_spatial_moving_matching.md",
        "S_{\\rm ref}",
        "\\varepsilon_{184}",
        "開始作用保持機構",
    )

    require(
        "sections/06_m37_spatial_envelope.md",
        "@title: M37空間信号系、W型低2モード接続とM64粒子接続",
        "## 6.14 現行M64位置接続の責務境界",
        "M37からR161へ進む現行因果鎖に、開始作用を別の固定機構へ保存する補助経路は置かない",
        "R161--R185については",
    )

    require(
        "sections/A6_common_signal_statistics.md",
        "Q3-4A・Q3-4B・Q3-5判定は、R124/R182/R125のsignal分布を付録YのM64/R203D finite-graph tracerへ接続",
    )

    ps = read("PROJECT_STATUS.md")
    require(
        "PROJECT_STATUS.md",
        "draft-123：Q3旧R184率latch経路の退役",
        "notes/superseded_r184_m37_rate_latch.md",
    )
    current_results = ps.split("### Q3結果", 1)[1].split("## 物理的解釈と境界", 1)[0]
    if re.search(r"^\|\s*R184\s*\|", current_results, re.M):
        raise AssertionError("PROJECT_STATUS.md: R184 remains in current Q3 result table")

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
        "notes/superseded_r184_m37_rate_latch.md",
        "R184 M37開始作用保持機構の退役記録",
        "10401e6b3e2b787344866862c7f31f9a15c08597",
        "79e0564612885add4412afa6dfe617a4f0195f24",
        "完全な旧証明・旧検算コードはGit履歴を正本",
    )
    require(
        "notes/superseded_result_index.md",
        "draft-123で退役したR184 Q3旧率latch",
        "| R184 |",
    )
    require("notes/README.md", "superseded_r184_m37_rate_latch.md")

    require(
        "tools/verify_m54_spatial_matching.py",
        "R161 spatial current antisymmetry",
        "R185 same-measure time reversal",
        "R185 D+ decomposition",
        "R185 general-current delta residual",
    )
    forbid(
        "tools/verify_m54_spatial_matching.py",
        "latched_rates",
        "r184_",
        "latched Lipschitz",
        "ideal latch equals",
    )

    require("sections/A12_common_action_shell_state_count.md", "R164")
    require("sections/A11_common_collision_bath_thermodynamics.md", "R170")

    print("draft123_retire_r184_ok")


if __name__ == "__main__":
    main()
