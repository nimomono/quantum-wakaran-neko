#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def rewrite(path: str, replacements: list[tuple[str, str]]) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    original = text
    for old, new in replacements:
        if old not in text:
            raise SystemExit(f"required cleanup fragment not found in {path}: {old!r}")
        text = text.replace(old, new)
    if text == original:
        raise SystemExit(f"no cleanup change made in {path}")
    p.write_text(text, encoding="utf-8")


# Current canonical prose only. Historical draft records and notes are intentionally untouched.
rewrite(
    "sections/01_scope_and_cycle.md",
    [
        (
            "Q1/Q2のR191射影読出しとQ3のM57--R195--R161/R162位置輸送は結果形成として分離しつつ",
            "Q1/Q2のR191射影読出しとQ3のM57/R195A・R196A--R196C--R161位置輸送は結果形成として分離し、R162はideal referenceとして扱いつつ",
        ),
    ],
)

rewrite(
    "sections/02_common_canonical_modules.md",
    [
        ("M57/R195A--R195Dを現行ミクロ物理実現", "M57/R195A・R196A--R196Cを現行ミクロ物理実現"),
        ("同じ局在tracerをR195D/R161へ渡す", "同じ局在tracerをR196C/R161へ渡す"),
        ("M57/R195A--R195Dの経路", "M57/R195A・R196A--R196Cの経路"),
    ],
)

rewrite(
    "sections/06_m37_spatial_envelope.md",
    [
        ("R195D/R161", "R196C/R161"),
    ],
)

rewrite(
    "sections/07_q3_finite_graph_phenomena.md",
    [
        ("M57/R195D--R161", "M57/R196C--R161"),
    ],
)

rewrite(
    "sections/08_errors_resources_open_targets.md",
    [
        (
            "Q3のM57--R195--R161/R162--R185経路",
            "Q3のM57/R195A・R196A--R196C--R161--R185経路（R162はideal reference）",
        ),
    ],
)

rewrite(
    "ENHANCEMENT_TARGETS.md",
    [
        ("M57、R195A--R195D、R161、R185", "M57、R195A、R196A--R196C、R161、R185"),
    ],
)

rewrite(
    "sections/A14_m54_spatial_moving_matching.md",
    [
        ("@title: M54空間移動状態構成とNelson型縮約", "@title: R161空間参照過程とNelson型縮約"),
        (
            "@status: M54共通親模型の空間移動状態構成を定義し、Q1型局所正準信号とQ2型辺結合から得る $(\\pi,j)$ をR161へ接続する。現行 $T_{ij}^\\delta$ は許容される対称活動量の1選択として位置づけ、R184のM37開始作用保持機構実装とR185のNelson型前後平均微分・時間対称Newton則を証明する。局所有向率の開放jump実現は共通R162へ置く。",
            "@status: R161が定める空間移動参照過程を定義し、Q1型局所正準信号とQ2型辺結合から得る $(\\pi,j)$ をR161へ接続する。現行 $T_{ij}^\\delta$ は許容される対称活動量の1選択として位置づけ、R184のM37開始作用保持機構実装とR185のNelson型前後平均微分・時間対称Newton則を証明する。R162は同じ局所有向率を実現するideal open-jump referenceであり、Q3の基礎的ミクロ存在論とは扱わない。",
        ),
        ("## N.1 M54空間移動状態構成と因果規約", "## N.1 R161空間参照過程と因果規約"),
        ("Q3で直接使う1試行状態断面を", "R161/R185のideal参照過程で使う状態断面を"),
        (
            "$Q_i,P_i$ は実正準信号自由度、$X_t\\in V$ は1個の実在粒子位置である。位置jumpはR162の開放Poisson reservoirが担い、有限衝突素子とその微視的履歴を能動状態へ持たない。",
            "$Q_i,P_i$ は実正準信号自由度、$X_t\\in V$ はR161生成子に従う参照位置座標である。R162は同じ局所有向率を実現するideal open-jump referenceとして利用できるが、M57 tracerとは別の実在粒子やQ3の基礎的ミクロ存在論を追加するものではない。",
        ),
        ("## N.2 厳密信号部分系とR164型移動対象", "## N.2 厳密信号部分系とR161移動特殊化"),
        (
            "R161/R162が定める同じ前向き開放経路法則からR185のBayes後退率を作るため",
            "R161が定める前向き経路法則（R162はそのideal open-jump reference）からR185のBayes後退率を作るため",
        ),
    ],
)

# The active Q3 regression must no longer use the retired R170 implementation margin.
verifier = (ROOT / "tools/verify_q3_completion.py").read_text(encoding="utf-8")
for forbidden in ("EPSILON_170", "R170 margin"):
    if forbidden in verifier:
        raise SystemExit(f"retired verifier dependency remains: {forbidden}")

# Record the cleanup without rewriting historical draft entries.
for path, heading in (
    ("CHANGELOG.md", "# 変更履歴"),
    ("VALIDATION.md", "# 検算記録"),
    ("MANIFEST.md", "# MANIFEST"),
):
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    if "draft-99" in text:
        continue
    marker = text.find("\n", text.find(heading))
    if marker < 0:
        raise SystemExit(f"cannot locate heading in {path}")
    if path == "CHANGELOG.md":
        block = "\n\n## draft-99：旧Q3主線を現行骨格から分離\n\n- 現行本文のR195B--R195D残骸をR195A・R196A--R196Cへ同期し、R162を物理主線ではなくideal open-jump referenceとして明示した。\n- 付録NをM57とは別の実在粒子模型として読めないよう、R161/R185の数学参照過程へ責務を縮約した。R184/R164の定理内容自体は変更しない。\n- `tools/verify_q3_completion.py` から退役R170の誤差marginを削除し、R123--R125の現象回帰と現行M57実装検算を分離した。\n- 理論的な再検証が必要なR164/R184の完全退役、R162の結果一覧からの削除、M57のedge-localからglobal tracerへの合成監査は本改訂に含めない。\n"
    elif path == "VALIDATION.md":
        block = "\n\n## draft-99：Q3 spine cleanup\n\n- 現行正本で旧R195B--R195Dを依存先として参照しないことを確認する。履歴節・notes・退役索引の旧IDは保存する。\n- 付録Nでは $X_t$ をR161/R185のideal参照位置座標として扱い、R162をM57とは別の実在粒子模型として解釈しない。\n- `tools/verify_q3_completion.py` はR170誤差marginを使用せず、トンネル・干渉の数学回帰だけを検査する。M57の物理実装誤差は `tools/verify_m57_ballistic_tracer.py` で別に検査する。\n- `tools/check_source.py`、`tools/check_terminology.py`、全physics checks、論文再生成・生成物同期を通す。\n"
    else:
        block = "\n\n## draft-99のQ3 spine cleanup\n\n- 現行Q3主線を `M37/M54 signal -> R195A -> R196A--R196C -> R161 -> R185` として表記同期し、R162はideal referenceへ限定する。\n- 付録Nの存在論をR161/R185参照過程へ縮約し、退役R195D/R170の現行依存残骸を除去する。\n- 歴史記録、notes、退役索引の旧模型記述は保存する。\n"
    text = text[: marker + 1] + block + text[marker + 1 :]
    p.write_text(text, encoding="utf-8")

# Regenerate canonical manuscript artifacts from the updated section sources.
subprocess.run(["python", "tools/build_paper.py"], cwd=ROOT, check=True)

# Temporary finalization plumbing removes itself before commit.
(ROOT / "tools/finalize_q3_spine_cleanup.py").unlink(missing_ok=True)
(ROOT / ".github/workflows/q3-spine-finalize.yml").unlink(missing_ok=True)
