#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ROOT / "sections"
NOTES = ROOT / "notes"


def read(path: str | Path) -> str:
    p = ROOT / path if isinstance(path, str) else path
    return p.read_text(encoding="utf-8")


def write(path: str | Path, text: str) -> None:
    p = ROOT / path if isinstance(path, str) else path
    p.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    p.write_text(text, encoding="utf-8")


def sub_required(text: str, pattern: str, repl: str, *, flags: int = 0, count: int = 1) -> str:
    out, n = re.subn(pattern, repl, text, count=count, flags=flags)
    if n != count:
        raise RuntimeError(f"expected {count} substitution(s): {pattern!r}, got {n}")
    return out


def remove_sentences(text: str, terms: tuple[str, ...]) -> str:
    # Prose-only cleanup: remove Japanese full-stop terminated sentences carrying retired IDs.
    for term in terms:
        text = re.sub(rf"(?m)(?<!\n)[^。\n]*{re.escape(term)}[^。\n]*。", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def replace_table_row(text: str, key: str, row: str) -> str:
    pattern = rf"(?m)^\| {re.escape(key)} \|.*$"
    out, n = re.subn(pattern, row, text, count=1)
    if n != 1:
        raise RuntimeError(f"table row not found: {key}")
    return out


# ---------------------------------------------------------------------------
# Preserve retired theory before removing it from the generated paper.
# ---------------------------------------------------------------------------
old_r190 = SECTIONS / "A19_m54_drude_action_shell_bridge.md"
if not old_r190.exists():
    raise RuntimeError("R190 appendix missing")
r190_text = old_r190.read_text(encoding="utf-8")
write(
    "notes/superseded_r190_drude_action_shell_bridge.md",
    """# 退役メモ：R190A--R190C Drude作用殻平方根bridge

この文書は draft-85 で導入した R190A--R190C の原文を保存する。
R191をQ1/Q2の2結果射影読出し主線へ採用したため、R190系列は固定目標の必須依存および生成論文から退役した。
内容は、2作用LC殻、無限Drude浴による作用保存型混合、有限時間一様化、対称作用開口からR161静的平方根核への接続を与える強化・代替構成として参照できる。
退役は反証や撤回を意味せず、現行主線の理解に不要なため本文外へ分離したものである。

---

""" + r190_text,
)
old_r190.unlink()

# R191 appendix moves from T/A20 to S/A19 after R190 leaves the paper.
r191_old = SECTIONS / "A20_m54_brownian_macrospin_projective_instrument.md"
r191_new = SECTIONS / "A19_m54_brownian_macrospin_projective_instrument.md"
if not r191_old.exists():
    raise RuntimeError("R191 appendix missing")
r191_text = r191_old.read_text(encoding="utf-8")
r191_text = r191_text.replace("@number: T", "@number: S", 1)
r191_text = r191_text.replace("付録T", "付録S")
r191_new.write_text(r191_text, encoding="utf-8")
r191_old.unlink()

# ---------------------------------------------------------------------------
# Common module: keep Q3 action/moving theory; make R191 the sole Q1/Q2 readout spine.
# ---------------------------------------------------------------------------
p = SECTIONS / "02_common_canonical_modules.md"
t = p.read_text(encoding="utf-8")
t = re.sub(
    r"(?m)^@status:.*$",
    "@status: M54をQ1・Q2・Q3の共通有効信号--配置状態構成族として定義する。Q1/Q2の2結果射影読出しはR191、測定後の可逆分岐はR181D、Q3の初期配置と移動はR164/R161/R162へ責務分離する。",
    t,
    count=1,
)
t = t.replace("$Y$ はR170の吸収指針変数", "$Y$ はR191等の吸収結果変数")
t = t.replace("R190/R179/R170は一般有限結果集合・作用殻型の代替経路として扱い、", "")
t = replace_table_row(t, "Q1", "| Q1 | W型2モード静的状態構成 | $|\\Lambda|=2$、2結果 | R181A、R140 | R191、R143/R181D |")
t = replace_table_row(t, "Q2-1", "| Q2-1 | 2ビット記憶部の静的状態構成 | $|\\Lambda|=4$ | R181B、R181C | R191、R181D |")
t = replace_table_row(t, "Q2-2", "| Q2-2 | 2ビット記憶部＋設定先行受信機構 | $|\\Lambda|=4$、2翼測定端 | R181B/R181C、R180 | 中央・局所R191、R180C |")
t = replace_table_row(t, "Q2-3", "| Q2-3 | 3ビット永続記憶部 | $|\\Lambda|=8$ | R181Bを2回、R181C、R177 | R191、R181D |")
t = replace_table_row(t, "Q2-4", "| Q2-4 | 一般 $n$ ビット記憶部 | $|\\Lambda|=2^n$ | R179、R181C | R191、R181D |")
# Scope R164 to Q3 in prose without changing theorem mathematics/name.
t = t.replace("## 2.7 M54共通条件付き作用容量と結果別状態数", "## 2.7 M54共通条件付き作用容量とQ3初期配置状態数")
# Remove the static j=0 specialization from R161 theorem; Q3 keeps the general moving statement.
t = re.sub(
    r"\n静的状態構成では \$j=0\$ とし、.*?\n空間状態構成では",
    "\n空間状態構成では",
    t,
    count=1,
    flags=re.S,
)
t = t.replace(
    "Poisson reservoirは本稿で採用する明示的な古典開放ミクロ方程式である。これを有限衝突Hamiltonian列または特定のHamiltonian無限浴から導くことは固定目標の必要条件とせず、有限閉鎖系への持上げは強化結果として論文外メモへ分離する。R162はQ3の移動過程を担い、Q1/Q2の静的平方根選択の物理実現はR190/R179へ分離する。",
    "Poisson reservoirは本稿で採用する明示的な古典開放ミクロ方程式である。これを有限衝突Hamiltonian列または特定のHamiltonian無限浴から導くことは固定目標の必要条件とせず、有限閉鎖系への持上げは強化結果として論文外メモへ分離する。R162はQ3の移動過程を担う。",
)
t = re.sub(
    r"\nR161は静的・移動の率構成を共通に保つが、.*?退役メモに保存する。\n",
    "\nR161/R162はQ3の配置輸送と時間反転率だけを担う。Q1/Q2の2結果測定には使用しない。\n",
    t,
    count=1,
    flags=re.S,
)
# Remove R190 theorem subsection wholesale.
t = sub_required(
    t,
    r"\n### 2\.8\.1 R190A--R190C：.*?(?=\n### 2\.8\.2 R191：)",
    "\n",
    flags=re.S,
)
t = t.replace("### 2.8.2 R191：", "### 2.8.1 R191：")
t = t.replace("付録T", "付録S")
t = t.replace("作用殻の多結果状態数を経由する経路とは別に、", "")
t = t.replace("R164/R190/R170は一般有限結果集合、作用殻型実現、独立な強化経路として残す。", "")
t = t.replace("混合評価、stochastic LLG、scale density、$q_{\\rm ret}$、$q_{\\rm time}$、端点dispatcher、熱力学、Q2-2で中央集約4結果samplerへ置換しない責務境界は付録Sに置く", "混合評価、stochastic LLG、scale density、$q_{\\rm ret}$、$q_{\\rm time}$、端点dispatcher、熱力学、Q2-2で中央集約4結果samplerへ置換しない責務境界は付録Sに置く")
# Extract R170 section to notes, then remove it from paper.
m = re.search(r"\n## 2\.9 R170：.*?(?=\n## 2\.10 )", t, flags=re.S)
if not m:
    raise RuntimeError("R170 section not found")
write(
    "notes/superseded_r170_static_selection.md",
    """# 退役メモ：R170 固定作用容量入力の静的選択・吸収指針変数固定

この文書はR191採用前にQ1/Q2の作用殻型静的選択を固定結果へ写していたR170の本文を保存する。
R191が2結果の確率生成と吸収固定を一つのBrownian macrospin instrumentで担うため、R170は現行固定目標の必須依存および生成論文から退役した。
一般有限結果集合へ作用殻型選択を再検討する場合の比較資料として残す。

---
""" + m.group(0).strip() + "\n",
)
t = t[:m.start()] + "\n" + t[m.end():]
# General register no longer advertises the retired shell reader.
t = remove_sentences(t, ("R190", "R170"))
t = re.sub(r"\n{3,}", "\n\n", t)
p.write_text(t, encoding="utf-8")

# ---------------------------------------------------------------------------
# R164 appendix: keep theorem, narrow application to Q3.
# ---------------------------------------------------------------------------
p = SECTIONS / "A12_common_action_shell_state_count.md"
t = p.read_text(encoding="utf-8")
t = re.sub(
    r"(?m)^@status:.*$",
    "@status: R164の作用殻状態数をQ3空間状態構成の開始面における条件付き配置分布の統計力学的起源として保持する。Q1/Q2の2結果射影読出しにはR191を使う。",
    t,
    count=1,
)
t = re.sub(r"\nR164をR143.*?Q1-2を達成とする。", "\nR164はQ3の開始面で必要な条件付き配置分布へ接続する。Q1/Q2の2結果射影測定には使用しない。", t, flags=re.S)
t = remove_sentences(t, ("R190", "R170"))
p.write_text(t, encoding="utf-8")

# R179 stays only as generic open supply/reset; drop old R190-specific prose.
for rel in ("sections/A17_m54_uniform_supply.md",):
    p = ROOT / rel
    t = p.read_text(encoding="utf-8")
    t = remove_sentences(t, ("R190", "R190B"))
    t = t.replace("作用殻の試行前状態を $x$ とし、R190Bの混合核を $K_m(x,\\cdot)$ とする。", "補助自由度の試行前状態を $x$ とし、開放reset核を $K_m(x,\\cdot)$ とする。")
    p.write_text(t, encoding="utf-8")

# R181D: remove alternative-path prose and merge duplicate subsection heading.
p = SECTIONS / "A16_m54_projector_tree_receiver.md"
t = p.read_text(encoding="utf-8")
t = re.sub(
    r"(?m)^@status:.*$",
    "@status: R181DはR191で結果が固定された後の可逆projector router、未規格化選択成分の次段受渡し、一般深さQ2-4で必要な場合だけの振幅再調整を合成する。",
    t,
    count=1,
)
t = remove_sentences(t, ("R164/R190/R170",))
t = t.replace("### P.5.1 階数1 射影子の測定後状態の受け渡し\n\n", "")
p.write_text(t, encoding="utf-8")

# ---------------------------------------------------------------------------
# Q1 and Q2 prose: remove retired static selector references without changing theorem IDs.
# ---------------------------------------------------------------------------
replacements = {
    "固定済み容量入力R170系": "R191",
    "初期R170": "R191読出し",
    "2つの局所R170": "2つの局所R191",
    "局所R170": "局所R191",
    "中央R170": "中央R191",
    "R170選択・固定": "R191選択・固定",
    "R170の固定済み容量入力系": "R191",
}
for rel in (
    "sections/03_m47_controlled_w_instrument.md",
    "sections/A2_m47_controlled_w_instrument_proofs.md",
    "sections/A8_m47_hopf_preparation.md",
    "sections/04_m54_q2_specializations.md",
    "sections/05_m54_setting_pre_receiver.md",
    "sections/A3_m54_q2_specialization_proofs.md",
    "sections/A4_m54_receiver_cycle_proofs.md",
    "sections/A9_m54_setting_pre_paired_hopf_receiver.md",
    "sections/08_errors_resources_open_targets.md",
):
    p = ROOT / rel
    t = p.read_text(encoding="utf-8")
    for a, b in replacements.items():
        t = t.replace(a, b)
    t = remove_sentences(t, ("R190", "R164/R190", "R164/R190/R170"))
    p.write_text(t, encoding="utf-8")

# Explicitly fix the old Q1 mapping sentence in A8 if still present.
p = SECTIONS / "A8_m47_hopf_preparation.md"
t = p.read_text(encoding="utf-8")
t = re.sub(
    r"粒子位置のBorn型分布.*?使わない。",
    "Q1の排他的2結果はR191が固定した射影作用から生成し、W型局所記録はR143、測定後状態の受け渡しはR181Dの深さ1特殊化が担う。",
    t,
    flags=re.S,
)
p.write_text(t, encoding="utf-8")

# Q2-2 keeps R180B/Hopf; only selector implementation is unified to R191.
for rel in ("sections/05_m54_setting_pre_receiver.md", "sections/A4_m54_receiver_cycle_proofs.md", "sections/A9_m54_setting_pre_paired_hopf_receiver.md"):
    p = ROOT / rel
    t = p.read_text(encoding="utf-8").replace("R170", "R191")
    p.write_text(t, encoding="utf-8")

# ---------------------------------------------------------------------------
# Overview is intentionally rewritten: one short spine per research series.
# ---------------------------------------------------------------------------
write(
    "sections/00_overview_and_contents.md",
    r'''@number: 0
@chapter: 概要
@title: 概要

本論文の中心的な問いは、明示的な古典力学モデルから、量子力学に似た状態空間、可逆操作、Born型測定統計、測定後状態、結合ゲート、Bell型共同統計、空間伝播がどこまで有効構造として現れるかである。有限閉鎖Hamiltonian模型、有限能動部分系とHamiltonian無限浴からなるミクロ模型、その縮約または採用ミクロ方程式としての開放古典模型を区別し、有限浴化それ自体は固定目標にしない。

共通有効層はM54である。実正準対から得る複素信号は派生表示であり、独立した物理実体ではない。R181Aが物理テンプレート準備、R181Bが固定入力のテンソル積状態生成、R181Cが永続記憶部上の局所ゲート、R112が有限正準制御・SWAP・記録を担う。

Q1/Q2の2結果測定は一本化する。直交射影 $P_0,P_1$ に対して

```math
J_b=\mathcal J_0 Z^\dagger P_b Z
```

を保持し、R191が作用和 $J_0+J_1$ と作用差 $J_0-J_1$ をBrownian macrospinの吸引域境界へ直接結合して排他的結果を生成する。有限混合、transducer誤差、保護帯、有限温度retreat、有限decision時間、無反応を一つの完全結果誤差へまとめる。結果固定後はR181Dの可逆projector router

```math
(Z,0)\longmapsto(P_bZ,P_{1-b}Z)
```

だけを作用し、固定小深度では未規格化の $P_bZ$ をそのまま次段へ渡す。物理的な状態依存規格化は必要ない。

Q1ではM37弱結合W型の最低2正常モードをR187でW2信号へ接続し、R140が有限 $SU(2)$ 制御を与える。R143/R144がR191とR181DをW型1段測定・固定有限段逐次測定へ特殊化する。R189A--R189Cは走行中Rabiを止めずに作用を保持し、R191で中間結果を決め、有限2回Rabi--Zeno比較を閉じる。Q1-1、Q1-2は達成である。

Q2-1とQ2-3では、4モードまたは8モードの永続信号上でR181B/R181Cの可逆ゲート列を作用し、末端測定をR191+R181Dで行う。Q2-4では一般 $n$ の受動 $2^n$ モードと一様局所ゲートを許し、外部プログラム長・制御チャネル・時間・精度・試行回数を多項式条件として監査する。一般深さでbranch作用が読出し下限を下回る場合だけ、方向を変えない振幅再調整を使う。

Q2-2は非空間分離・固定有限設定族の古典装置として量子共同統計を再現する。M54の実際の4モード末端信号をR180Aの設定先行受信機構へ渡し、R180Bの2端Hopf流で二つの物理測定端へ接続する。中央および各翼の排他的2結果はR191へ統一し、R180Cが条件付き積因子化、Born共同分布、非信号性、CHSH不等式の破れ、Bell前提監査をまとめる。空間分離したBell-local hidden-variable模型の説明は主張しない。

Q3は測定器ではなく粒子位置の時間発展を扱う。R164は開始面の条件付き配置状態数、R161は信号の確率流と活動量から前向き・後向き率を構成し、R162はその率を開放Poisson-jump過程として実現する。R185は同じ経路法則のBayes反転から前進・後退平均微分と時間対称Newton則を導く。したがってQ1/Q2の測定主線とQ3の位置輸送主線は、役割を混ぜずに独立に読むことができる。

現行の最短依存鎖は次である。

```text
Q1/Q2 signal:       M54 / M37 -> R181A--R181C / R140
Q1/Q2 measurement:  projector action -> R191 -> R181D
Q2-2 Bell:           R180A -> R180B -> R191 at the two-stage receiver -> R180C
Q3 position:         R164 -> R161 -> R162 -> R184/R185
```

旧作用殻型の静的平方根選択R190A--R190Cと、その結果を吸収指針へ固定するR170は、R191採用後の固定目標には不要になったため生成論文から外し、比較・強化用の退役メモとして `notes/` に保存する。これは反証や撤回ではなく、現行主線の理解に不要な代替構成の分離である。
''')

# ---------------------------------------------------------------------------
# Scope/status prose: remove stale dependency claims but keep fixed-goal wording/statuses.
# ---------------------------------------------------------------------------
p = SECTIONS / "01_scope_and_cycle.md"
t = p.read_text(encoding="utf-8")
for a, b in replacements.items():
    t = t.replace(a, b)
t = t.replace("M54、R112、R161、R164、R170、R179、R181A--R181D、R186、R190A--R190C", "M54、R112、R179、R181A--R181D、R186、R191")
t = t.replace("M54、R180A--R180C", "M54、R180A--R180C、R191")
t = remove_sentences(t, ("R190",))
t = t.replace("\\xrightarrow{\\mathrm{R170}}", "\\xrightarrow{\\mathrm{R191}}")
p.write_text(t, encoding="utf-8")

p = ROOT / "PROJECT_STATUS.md"
t = p.read_text(encoding="utf-8")
t = re.sub(r"(?m)^\| R170 \|.*\n", "", t)
t = re.sub(r"(?m)^\| R190A \|.*\n", "", t)
t = re.sub(r"(?m)^\| R190B \|.*\n", "", t)
t = re.sub(r"(?m)^\| R190C \|.*\n", "", t)
t = t.replace("Q1/Q2の静的状態構成ではR164、R190、R179、R170、Q3の空間移動状態構成ではR161、R162を使う。", "Q1/Q2の2結果射影読出しではR191、Q3の開始配置と空間移動ではR164、R161、R162を使う。")
t = t.replace("R161、R162、R164、R170、R181A--R181D", "R181A--R181D、R191")
t = t.replace("R112、R161、R164、R170、R179、R181A--R181D、R186、R190A--R190C", "R112、R179、R181A--R181D、R186、R191")
t = t.replace("R164、R190、R179、R170", "R191")
t = t.replace("R170", "R191")
t = remove_sentences(t, ("R190",))
p.write_text(t, encoding="utf-8")

# README: current story only; historical details live in CHANGELOG/notes.
p = ROOT / "README.md"
t = p.read_text(encoding="utf-8")
t = re.sub(r"> \*\*draft-88:\*\*.*?\n\n", "", t, count=1, flags=re.S)
insert = "> **draft-89:** R191をQ1/Q2の2結果射影読出しの単独主線とし、旧R190/R170静的選択経路を生成論文から退役させた。R164はQ3初期配置へ責務を限定し、退役内容は `notes/` に保存する。固定目標と達成ラベルは変更しない。\n\n"
# place after first title
parts = t.split("\n", 1)
t = parts[0] + "\n\n" + insert + (parts[1] if len(parts) > 1 else "")
t = t.replace("R170", "R191")
t = remove_sentences(t, ("R190",))
p.write_text(t, encoding="utf-8")

# Conclusion rewritten to mirror the compressed architecture; no new theorem/result.
write(
    "sections/09_conclusion.md",
    r'''@number: 9
@chapter: 本文
@title: 結論

本稿では、古典実正準系から量子力学的構造がどこまで現れるかを、準備、可逆信号力学、排他的測定、Bell型共同統計、粒子位置輸送に分けて検査した。複素振幅は実正準信号の派生表示であり、独立した物理実体とはしない。固定目標の達成判定と、全要素を一つのミクロ装置へ統合する強化課題を区別した。

## 9.1 Q1/Q2の共通信号と測定

M54は有限実正準信号、作業領域、記録、環境接続端の共通有効状態構成を与える。R181Aは物理テンプレート準備、R181Bは固定入力テンソル積状態の生成、R181Cは永続記憶部上の局所ゲート、R112は有限正準制御・SWAP・記録を担う。

Q1/Q2の2結果射影測定はR191へ一本化した。射影作用

```math
J_b=\mathcal J_0 Z^\dagger P_b Z
```

の和と差がBrownian macrospinのdecision potentialを決め、理想極限で

```math
P(b)=\frac{J_b}{J_0+J_1}
```

を与える。有限混合、transducer、保護帯、有限温度retreat、有限decision時間、吸収記録は同じ完全結果誤差へまとめられる。結果後はR181Dの可逆projector routerが

```math
(Z,0)\mapsto(P_bZ,P_{1-b}Z)
```

を実行する。固定小深度では選択された未規格化成分を次段へ直接渡せるため、物理的な状態依存規格化は不要である。一般深さQ2-4で作用が読出し下限を下回り得る場合だけ、方向を変えない振幅再調整を残す。

## 9.2 Q1とZeno比較

Q1ではR187がM37弱結合W型の最低2正常モードをW2信号へ接続し、R140が任意の有限 $SU(2)$ 制御とRabi型占有振動を与える。R143/R144はR191+R181Dを1段および固定有限段の射影測定へ接続する。R189A--R189Cは走行中Rabiを止めずに作用容量を保持し、R191で中間結果を固定して有限2回Rabi--Zeno比較を閉じる。Q1-1、Q1-2は達成である。

## 9.3 Q2のゲートとBell型共同統計

Q2-1では4モード、Q2-3では8モードの永続信号上でR181B/R181Cの可逆ゲート列を作用し、末端読出しをR191+R181Dへ共通化した。Q2-4では一般 $n$ の受動 $2^n$ モードを許す一方、外部プログラム、制御チャネル、時間、精度、試行回数を多項式条件として監査する。指数個の受動自由度や総製造費が量子計算機と同程度であるとは主張しない。

Q2-2は非空間分離・固定有限設定族に限定する。実際の4モード末端信号をR180Aへ渡し、R180Bの2端Hopf流で二つの物理測定端へ接続し、中央・局所の排他的選択はR191へ統一する。R180Cは条件付き積因子化、量子共同Born分布、非信号性、CHSH不等式の破れ、Bell前提監査を同じ装置鎖で扱う。空間分離したBell-local hidden-variable模型の説明は固定目標ではない。

## 9.4 Q3の位置輸送

Q3ではR191を使わない。R164は開始面の条件付き配置状態数、R161は確率流と対称活動量から前向き・後向き率を構成し、R162はその率を開放Poisson-jump過程として実現する。R185は同じ前向き経路法則のBayes反転から前進・後退平均微分と時間対称Newton則を導く。これによりQ3-2は固定有限時間・有限格子範囲で達成している。束縛状態、W型低位構造、有限障壁トンネル、干渉については各固定目標の達成判定を第7章と現在地表に分離して記録した。

## 9.5 現行主線と退役経路

現行の最短依存鎖は

```text
Q1/Q2 measurement: projector action -> R191 -> R181D
Q2-2 Bell:          R180A -> R180B -> R191 -> R180C
Q3 position:        R164 -> R161 -> R162 -> R184/R185
```

である。旧R190A--R190CのDrude作用殻平方根bridgeとR170の静的選択・吸収固定は、R191採用後の固定目標には不要になったため生成論文から退役した。内容は比較・強化用として `notes/superseded_r190_drude_action_shell_bridge.md` と `notes/superseded_r170_static_selection.md` に保存する。退役は結果の反証ではなく、現行理論の責務を狭くして理解コストを下げるための分離である。

## 9.6 残る強化課題

最大の未完成点は、Q1--Q3の有限能動部分系、準備、ゲート、R191測定、Q3位置浴、記録、resetを共通のHamiltonian無限浴interfaceを持つ一つのミクロ装置へ統合するM0である。Q2-2の2端Hopf受信機構をさらに単純化できるか、Q2-4一般深度のbranch作用下限をどの物理refresh機構で保証するかも独立した強化課題である。有限浴への持上げは、それ自体に物理的意味がある場合だけ追加検査とする。
''')

# ---------------------------------------------------------------------------
# Build/CI: stop requiring retired theorems; keep structural guards against regression.
# ---------------------------------------------------------------------------
p = ROOT / "tools/build_paper.py"
t = p.read_text(encoding="utf-8")
for line in (
    '    "R190A": {"R164"},\n',
    '    "R190B": {"R190A"},\n',
    '    "R190C": {"R161", "R190B"},\n',
    '    "R170": {"R190C", "R179"},\n',
):
    t = t.replace(line, "")
t = t.replace('        SECTIONS / "A19_m54_drude_action_shell_bridge.md",\n', "")
t = t.replace('        ROOT / "tools" / "verify_r190_drude_shell.py",\n', "")
# Remove R190 active validation block.
t = re.sub(r"\n    if active_text\.count\(\"定理（R190A：\"\).*?(?=\n    for forbidden_token in \()", "\n", t, count=1, flags=re.S)
# Remove R170-specific validation block near the common_text checks.
t = re.sub(r"\n    r170_block = common_text\.split\(\"\*\*定理（R170：\".*?(?=\n    if \"定理（R181D：)", "\n", t, count=1, flags=re.S)
t = t.replace('    if "R164/R190/R170は一般有限結果集合" not in common_text:\n        raise ValueError("R191と旧作用殻経路の責務境界がない")\n', "")
t = t.replace('        "R180A", "R180B", "R180C", "R161", "R162", "R164", "R170",\n', '        "R180A", "R180B", "R180C", "R161", "R162", "R164",\n')
# Add R191 to theorem uniqueness list if not already protected elsewhere.
t = t.replace('        "R123", "R124", "R125", "R182", "R187", "R189B", "R189C",\n', '        "R123", "R124", "R125", "R182", "R187", "R189B", "R189C", "R191",\n')
# Structural anti-regression checks.
needle = '    common_text = (SECTIONS / "02_common_canonical_modules.md").read_text(\n        encoding="utf-8"\n    )\n'
if needle in t:
    guard = needle + '    for retired_id in ("定理（R170：", "定理（R190A：", "補題（R190B：", "定理（R190C："):\n        if retired_id in common_text:\n            raise ValueError("退役した静的選択定理が第2章へ再混入: " + retired_id)\n'
    t = t.replace(needle, guard, 1)
t = t.replace("A20_m54_brownian_macrospin_projective_instrument.md", "A19_m54_brownian_macrospin_projective_instrument.md")
t = t.replace("付録T", "付録S")
p.write_text(t, encoding="utf-8")

# Remove retired active verifier; preserve it with the retired R190 material.
vr = ROOT / "tools/verify_r190_drude_shell.py"
if vr.exists():
    preserved = NOTES / "superseded_verify_r190_drude_shell.py"
    preserved.write_text("# Retired with R190A--R190C; preserved for historical regression.\n" + vr.read_text(encoding="utf-8"), encoding="utf-8")
    vr.unlink()

# Rename stale R170 diagnostic labels without changing numerical checks.
p = ROOT / "tools/verify_q3_completion.py"
if p.exists():
    t = p.read_text(encoding="utf-8").replace("R170_ERROR_TERMS", "POINTER_ERROR_TERMS")
    p.write_text(t, encoding="utf-8")
p = ROOT / "tools/verify_m54_static_instrument.py"
if p.exists():
    t = p.read_text(encoding="utf-8").replace('"r170_', '"legacy_static_')
    p.write_text(t, encoding="utf-8")

# Workflow checks.
p = ROOT / ".github/workflows/verify.yml"
t = p.read_text(encoding="utf-8")nt = t.replace('            sections/A19_m54_drude_action_shell_bridge.md \\\n', '')
t = t.replace('            sections/A20_m54_brownian_macrospin_projective_instrument.md \\\n', '            sections/A19_m54_brownian_macrospin_projective_instrument.md \\\n')
t = re.sub(r"(?m)^\s*test \"\$\(grep -Rho '(?:定理|補題)（R190.*$\n", "", t)
t = re.sub(r"(?m)^\s*grep -Fq '## S\.13 R179による反復再混合'.*$\n", "", t)
t = re.sub(r"(?m)^\s*test -f tools/verify_r190_drude_shell\.py\s*$\n", "", t)
t = re.sub(r"(?m)^\s*test \"\$\(grep -Rho '定理（R170：'.*$\n", "", t)
t = re.sub(r"(?m)^\s*grep -Fq '定理（R170：.*$\n", "", t)
t = re.sub(r"(?m)^\s*grep -Fq '\*\*系（R170選択結果の局所記録）\*\*'.*$\n", "", t)
t = t.replace("A20_m54_brownian_macrospin_projective_instrument.md", "A19_m54_brownian_macrospin_projective_instrument.md")
t = t.replace("付録T", "付録S")
# Replace old 'keep R170/R190' guard with anti-regression guards.
marker = "          test -f tools/verify_r191_macrospin.py\n"
if marker in t:
    t = t.replace(marker, marker + "          ! grep -R -Fq '定理（R170：' sections\n          ! grep -R -Fq '定理（R190A：' sections\n          ! grep -R -Fq '補題（R190B：' sections\n          ! grep -R -Fq '定理（R190C：' sections\n", 1)
t = t.replace("version: \"draft-88\"", "version: \"draft-89\"")
t = t.replace("draft-88 改訂稿", "draft-89 改訂稿")
p.write_text(t, encoding="utf-8")

# Metadata/version.
for rel in ("CITATION.cff", "tools/template.tex"):
    p = ROOT / rel
    t = p.read_text(encoding="utf-8").replace('version: "draft-88"', 'version: "draft-89"').replace("draft-88 改訂稿", "draft-89 改訂稿")
    p.write_text(t, encoding="utf-8")

# Manifest/notes indexes.
p = ROOT / "MANIFEST.md"
t = p.read_text(encoding="utf-8")
t = t.replace("- `sections/A19_m54_drude_action_shell_bridge.md`\n", "")
t = t.replace("- `sections/A20_m54_brownian_macrospin_projective_instrument.md`", "- `sections/A19_m54_brownian_macrospin_projective_instrument.md`")
t = t.replace("- `tools/verify_r190_drude_shell.py`\n", "")
if "superseded_r190_drude_action_shell_bridge.md" not in t:
    t += "\n## draft-89で退役した静的選択経路\n\n- `notes/superseded_r190_drude_action_shell_bridge.md`\n- `notes/superseded_r170_static_selection.md`\n- `notes/superseded_verify_r190_drude_shell.py`\n"
p.write_text(t, encoding="utf-8")

p = NOTES / "superseded_result_index.md"
t = p.read_text(encoding="utf-8")
if "R190A--R190C" not in t or "superseded_r190_drude_action_shell_bridge.md" not in t:
    t += "\n| R190A--R190C | 2作用LC殻Drude混合と静的平方根kernel | R191の2結果Brownian-macrospin読出しを主線化したため生成論文から退役 | `superseded_r190_drude_action_shell_bridge.md` |\n"
if "superseded_r170_static_selection.md" not in t:
    t += "| R170 | 固定作用容量からの静的選択・吸収指針固定 | R191が2結果の選択と吸収固定を一体で担うため生成論文から退役 | `superseded_r170_static_selection.md` |\n"
p.write_text(t, encoding="utf-8")

p = NOTES / "README.md"
t = p.read_text(encoding="utf-8")
if "superseded_r190_drude_action_shell_bridge.md" not in t:
    t += "\n- `superseded_r190_drude_action_shell_bridge.md`: R190A--R190Cの退役原文。R191採用前の作用殻型静的平方根選択。\n- `superseded_r170_static_selection.md`: R170の退役原文。静的選択結果の吸収固定。\n"
p.write_text(t, encoding="utf-8")

# Validation adds a new current entry; old run history remains archival.
p = ROOT / "VALIDATION.md"
t = p.read_text(encoding="utf-8")
entry = """\n## draft-89: R191主線圧縮\n\n- 新しいモデルID、結果ID、定理、補題、数値主張は追加しない。\n- Q1/Q2の2結果読出しをR191、測定後分岐をR181Dへ一本化した。\n- R190A--R190CとR170は生成論文から退役し、原文をnotesへ保存した。\n- R164はQ3開始配置の状態数へ責務を限定し、R161/R162はQ3移動専用とした。\n- Q2-2のR180B 2端Hopf受信機構は維持する。\n- R191付録をA19/付録Sへ繰り上げ、旧R190専用検算を履歴メモへ移した。\n\n"""
if "## draft-89: R191主線圧縮" not in t:
    t = entry + t
p.write_text(t, encoding="utf-8")

# Changelog current entry.
p = ROOT / "CHANGELOG.md"
t = p.read_text(encoding="utf-8")
entry = """## draft-89: R191主線圧縮と旧静的選択経路の退役\n\n- 新定理を追加せず、Q1/Q2の2結果読出しをR191、測定後分岐をR181Dへ一本化。\n- R190A--R190CとR170を生成論文から退役し、原文と専用検算を `notes/` へ保存。\n- R164をQ3開始配置、R161/R162をQ3位置輸送へ責務縮約。\n- Q2-2のR180B 2端Hopfは維持し、中央・局所selectorだけをR191へ統一。\n- R191付録をA19/付録Sへ繰り上げ。固定目標・達成ラベルは不変。\n\n"""
if not t.startswith("## draft-89"):
    t = entry + t
p.write_text(t, encoding="utf-8")

# q1 Zeno roadmap note should describe the current readout.
p = NOTES / "q1_2_zeno_integration.md"
if p.exists():
    t = p.read_text(encoding="utf-8")
    t = t.replace("R170の固定済み容量入力系", "R191")
    t = t.replace("R189BでR170の有限後段窓", "R189BでR191の有限decision後段窓")
    t = t.replace("R164作用殻、R161静的整合、R162有限衝突、選択結果固定をW2信号から切り離して実行する。", "R191の作用和・作用差読出しをW2信号から切り離して実行する。")
    p.write_text(t, encoding="utf-8")

# Final active-text cleanup: no R190/R170 theorem claims remain in generated sections.
active = "\n".join(x.read_text(encoding="utf-8") for x in SECTIONS.glob("*.md"))
for forbidden in ("定理（R170：", "定理（R190A：", "補題（R190B：", "定理（R190C："):
    if forbidden in active:
        raise RuntimeError("retired theorem still active: " + forbidden)

print("R191 simplification migration applied")
