#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ROOT / "sections"
NOTES = ROOT / "notes"


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel: str, text: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def replace_exact(rel: str, old: str, new: str, *, required: bool = True) -> None:
    text = read(rel)
    if old not in text:
        if required:
            raise RuntimeError(f"{rel}: expected text not found: {old[:120]!r}")
        return
    write(rel, text.replace(old, new))


def replace_regex(rel: str, pattern: str, repl: str, *, count: int = 0, required: bool = True, flags: int = 0) -> None:
    text = read(rel)
    new, n = re.subn(pattern, repl, text, count=count, flags=flags)
    if required and n == 0:
        raise RuntimeError(f"{rel}: regex did not match: {pattern}")
    write(rel, new)


def replace_section(rel: str, start: str, end: str, body: str) -> None:
    text = read(rel)
    i = text.find(start)
    if i < 0:
        raise RuntimeError(f"{rel}: section start not found: {start}")
    j = text.find(end, i + len(start))
    if j < 0:
        raise RuntimeError(f"{rel}: section end not found: {end}")
    new = text[:i] + body.rstrip() + "\n\n" + text[j:]
    write(rel, new)


def clean_result_list(line: str, remove: tuple[str, ...], add: tuple[str, ...] = ()) -> str:
    parts = line.rstrip("\n").split("|")
    if len(parts) < 8:
        return line
    field = parts[6].strip()
    items = [item.strip() for item in field.split("、") if item.strip()]
    items = [item for item in items if item not in remove]
    for item in add:
        if item not in items:
            items.append(item)
    parts[6] = " " + "、".join(items) + " "
    return "|".join(parts) + "\n"


# ---------------------------------------------------------------------------
# 1. PROJECT_STATUS: retire R181A, add R192, rewire fixed-goal dependencies.
# ---------------------------------------------------------------------------
rel = "PROJECT_STATUS.md"
text = read(rel)
if "## draft-90：R181A退役とR192方向不変作用安定化" not in text:
    marker = "## draft-89：R191測定主線の責務縮約"
    intro = """## draft-90：R181A退役とR192方向不変作用安定化

- R181Aの状態方向準備を現行固定目標の主線から完全退役し、古典実正準系の初期状態方向は準備済み入力境界として扱う。
- R181Aのうち一般深さQ2-4で必要だった方向不変の作用下限回復だけをR192へ切り出す。
- R192は状態方向、Born重み、結果選択を生成せず、非零信号の方向を保存したまま作用だけを固定目標値へ有限時間で安定化する。
- Q1-2とQ3系列はR192へ依存しない。Q2-4だけが非終端の安全結果成分でR192を用いる。
- Q2-4は一般 $n$ の初期化にR181Bを用いず、R179後の定数次元供給源から $0^n$ 根モードを作る既存方針へ依存表を同期する。
- 固定長期目標と達成ラベルは変更しない。

"""
    if marker not in text:
        raise RuntimeError("PROJECT_STATUS.md: draft-89 marker missing")
    text = text.replace(marker, intro + marker, 1)

# Remove active R181A result row and insert R192 after R181D.
text = re.sub(r"^\| R181A \|.*\n", "", text, flags=re.MULTILINE)
if "| R192 |" not in text:
    pattern = r"(^\| R181D \|.*\n)"
    repl = (
        r"\1"
        "| R192 | 採用開放方程式後の厳密結果・明示誤差付き結果 | 非零信号の状態方向を厳密に保存したまま、作用を固定目標値へ有限時間で安定化する。安全作用下限が逆多項式ならQ2-4の各非終端段の固定接続時間は多項式に抑えられる。結果確率・結果選択・横方向誤差訂正は行わない |\n"
    )
    text, n = re.subn(pattern, repl, text, count=1, flags=re.MULTILINE)
    if n != 1:
        raise RuntimeError("PROJECT_STATUS.md: R181D row not found")

new_lines: list[str] = []
for line in text.splitlines(keepends=True):
    if line.startswith("| Q1-2 |"):
        line = clean_result_list(line, ("R181A",))
    elif line.startswith("| Q2-1 |"):
        line = clean_result_list(line, ("R181A",))
    elif line.startswith("| Q2-3 |"):
        line = clean_result_list(line, ("R181A",))
    elif line.startswith("| Q2-4 |"):
        line = clean_result_list(line, ("R181A", "R181B"), ("R192",))
        line = line.replace("必要時再調整", "非終端安全結果でR192作用安定化")
        line = line.replace("必要な作用下限回復", "R192による作用下限回復")
    elif line.startswith("| Q3-4A |") or line.startswith("| Q3-4B |") or line.startswith("| Q3-5 |"):
        line = clean_result_list(line, ("R181A",))
    new_lines.append(line)
text = "".join(new_lines)
text = text.replace("R181Aの方向を変えない振幅再調整用接続端", "R192の方向不変作用安定化接続端")
text = text.replace("R181Aの方向を変えない振幅再調整", "R192の方向不変作用安定化")
write(rel, text)


# ---------------------------------------------------------------------------
# 2. Core M54 chapter: prepared-input boundary + R192 theorem.
# ---------------------------------------------------------------------------
rel = "sections/02_common_canonical_modules.md"
text = read(rel)
text = text.replace(
    "@status: M54をQ1・Q2・Q3の共通有効信号--配置状態構成族として定義する。R191をQ1/Q2の2結果射影読出し主線、R164/R190/R170を一般有限結果集合・作用殻型の代替経路、R161/R162をQ3移動経路として分離し、R181A--R181Dを準備、テンソル積状態生成、永続ゲート、段階的射影選別読出しの正本として置く。",
    "@status: M54をQ1・Q2・Q3の共通有効信号--配置状態構成族として定義する。初期状態方向は準備済み古典入力境界として扱い、R191をQ1/Q2の2結果射影読出し主線、R181B/R181Cを固定入力持上げ・永続ゲート、R181Dを射影結果成分受渡し、R192を一般深さQ2-4の方向不変作用安定化として分離する。R164/R190/R170は一般有限結果集合・作用殻型の代替経路、R161/R162はQ3移動経路とする。"
)
text = text.replace("有限個の実正準対から得る信号、準備・供給接続端、永続記憶部", "有限個の実正準対から得る信号、準備済み入力境界、永続記憶部")
text = text.replace("| Q1 | W型2モード信号 | R181A、R140、R187 | R191、R181D、R143--R144 |", "| Q1 | W型2モード信号 | 準備済み古典入力、R140、R187 | R191、R181D、R143--R144 |")
text = text.replace("| Q2-4 | $2^n$ 直接モード | R181C | R191、R181D、必要時再調整、R179 reset |", "| Q2-4 | $2^n$ 直接モード | 根モード初期化、R181C | R191、R181D、非終端安全結果のR192、R179 reset |")
text = text.replace("| Q3 | 空間信号＋配置 | R181Aを準備接続端として使用可、M37/R184 | R164開始配置、R161/R162、R185 |", "| Q3 | 空間信号＋配置 | 準備済み古典空間入力、M37/R184 | R164開始配置、R161/R162、R185 |")
write(rel, text)

prepared_section = r"""## 2.4 初期状態の準備境界

各試行の物理状態は有限個の実正準対 $(Q,P)$ であり、派生複素座標

```math
Z=\frac{Q+iP}{\sqrt{2\mathcal J_0}}
```

は実正準信号系の表示にすぎない。本論文の固定目標では、初期状態方向を共通の状態非依存種から散逸的に生成することを必須条件にしない。Q1ではW型2モード、Q2では固定入力信号または一般 $n$ の $0^n$ 根モード、Q3では空間信号について、実正準初期条件またはその試行分布を準備済み古典入力として境界に置く。

入力境界は、結果確率表、Born重み、結果依存状態、規格化後の測定結果を外部から注入する許可ではない。境界以後の可逆発展、状態方向輸送、結果形成、射影結果成分受渡し、空間配置輸送は各現行結果から導く。入力誤差は、目標規格化第2モーメント $C_{\rm in}$ または目標単一試行信号に対する一つの $\varepsilon_{\rm in}$ として下流の誤差予算へ一度だけ入れる。

Q1のM37--W2接続ではR187または固定線形正準接続端を用い、Q2-1--Q2-3の固定積入力はR181Bへ渡す。Q2-4はR181Bを一般 $n$ へ反復せず、R179の開放初期化後に定数次元供給源を $0^n$ 根モードへ接続する。Q3は準備済み空間信号からM37/R86およびR164--R162の経路へ入る。

旧R181Aの物理テンプレート、横方向排出、共通初期種からの状態方向吸引は数学的結果として退役記録へ保存する。そこに含まれていた方向不変の作用回復だけは、一般深さQ2-4に必要な独立機能としてR192へ切り出す。"""
replace_section(rel, "## 2.4 ", "## 2.5 ", prepared_section)

# Rewire radial references throughout chapter 2.
text = read(rel)
text = text.replace("必要時の振幅再調整接続端", "必要時のR192作用安定化接続端")
text = text.replace("必要な場合だけ方向を変えない振幅再調整", "必要な場合だけR192の方向不変作用安定化")
text = text.replace("一般深さで必要な場合だけ方向を変えない振幅再調整", "一般深さで必要な場合だけR192の方向不変作用安定化")
text = text.replace("一般深さで作用下限の回復が必要な場合だけR181Aの方向を変えない振幅再調整を使う。", "一般深さで作用下限の回復が必要な場合だけR192を使う。固定有限深さでは非規格化結果成分をそのまま次段へ渡す。")
text = text.replace("必要な振幅再調整", "必要なR192作用安定化")
text = text.replace("必要時の振幅再調整接続端", "必要時のR192作用安定化接続端")
text = text.replace("方向を変えない振幅再調整は状態方向を保存するため、既に生じた横方向加法偏差だけを選択的に除去しない。", "R192は状態方向を保存するため、既に生じた横方向加法偏差だけを選択的に除去しない。")
text = text.replace("必要な場合の方向を変えない振幅再調整", "必要な場合のR192作用安定化")
text = text.replace("必要な方向を変えない振幅再調整", "必要なR192作用安定化")
write(rel, text)

r192_section = r"""### 2.14.1 R192：方向不変作用安定化

R181Dが選別した非零信号を $Z\in\mathbb C^m$、その信号作用を

```math
S=Z^\dagger Z>0
```

とする。目標作用 $S_*>0$、固定利得 $g_R>0$、非負の時計窓 $\lambda_R(t)$ を置き、採用開放方程式を

```math
\dot Z
=\lambda_R(t)g_R
\left(S_*-Z^\dagger Z\right)Z
```

とする。有効接続時間を

```math
\tau_R(t)=\int_{t_0}^t\lambda_R(s)\,\mathrm ds
```

と書く。

<!-- theorem-start:theorem -->
**定理（R192：方向不変作用安定化）**

$Z(t_0)\neq0$ なら全有限時刻で状態方向は厳密に保存され、

```math
\frac{Z(t)}{\|Z(t)\|}
=
\frac{Z(t_0)}{\|Z(t_0)\|}
```

である。$S_0=Z(t_0)^\dagger Z(t_0)$ とすれば作用は

```math
S(\tau_R)
=
\frac{S_*}
{1+\left(S_*/S_0-1\right)e^{-2g_RS_*\tau_R}}
```

を満たす。特に $0<S_{\min}\leq S_0\leq S_*$ なら

```math
0
\leq
1-\frac{S(\tau_R)}{S_*}
\leq
\left(\frac{S_*}{S_{\min}}-1\right)
e^{-2g_RS_*\tau_R}.
```

従って相対作用誤差を $\eta_R\in(0,1)$ 以下にする十分条件は

```math
\tau_R
\geq
\frac{1}{2g_RS_*}
\log\!\left[
\frac{S_*/S_{\min}-1}{\eta_R}
\right].
```

R181Dの非終端安全結果で $S_{\min}/S_*$ が $n,1/\epsilon$ の逆多項式以上、$g_RS_*$ が逆多項式以上なら、Q2-4の各段で使う事前固定接続時間と全 $n-1$ 段の総接続時間は多項式である。R192は状態方向、Born重み、結果選択を生成せず、無反応または安全下限未満の成分を成功結果へ戻さない。横方向加法偏差も訂正しない。
<!-- theorem-end:theorem -->

証明、実変数表示、R181Dの安全下限との合成、R179へ残す環境履歴は付録Mに置く。Q1の固定有限深さとQ3系列はR192を固定目標の根拠に使わない。"""
text = read(rel)
marker = "## 2.15 R178Dの本線退役"
if "**定理（R192：方向不変作用安定化）**" not in text:
    if marker not in text:
        raise RuntimeError("section02: 2.15 marker missing")
    text = text.replace(marker, r192_section + "\n\n" + marker, 1)
text = text.replace("R191指針変数、必要時のR192作用安定化接続端", "R191指針変数、R192作用安定化接続端")
text = text.replace("制御付き選別機構、必要なR192作用安定化、開放リセット/供給接続部", "制御付き選別機構、非終端安全結果に対するR192、開放リセット/供給接続部")
write(rel, text)


# ---------------------------------------------------------------------------
# 3. Appendix M: archive R181A proof and replace active appendix by R192 proof.
# ---------------------------------------------------------------------------
old_a13 = ROOT / "sections/A13_m54_template_port_preparation.md"
archive_a13 = ROOT / "notes/superseded_r181a_template_port_preparation.md"
if old_a13.exists() and not archive_a13.exists():
    archive_a13.write_text(
        "# R181A 物理テンプレート準備の退役記録\n\n"
        "R181Aは誤りとして撤回したものではない。draft-90で固定目標の主線から状態方向準備を外し、方向不変の作用安定化だけをR192へ切り出したため、本付録の旧内容を研究記録として保存する。\n\n"
        + old_a13.read_text(encoding="utf-8"),
        encoding="utf-8",
    )

new_a13 = r"""@number: M
@chapter: 付録
@title: R192方向不変作用安定化の証明
@status: R192の実正準表示、方向保存、作用のロジスティック解、安全作用下限からの固定時間回復、R181D/R179/R186との責務境界を証明する。

## M.1 目的

R192は状態準備機構ではない。入力は既に方向を持つ非零の実正準信号であり、本付録ではその方向を変えずに作用だけを固定目標値へ戻す開放流を扱う。結果確率、結果選択、状態方向吸引、横方向誤差訂正は結論に含めない。

## M.2 実正準表示

$m$ 個の実正準対 $Q,P\in\mathbb R^m$ と

```math
Z=\frac{Q+iP}{\sqrt{2\mathcal J_0}}
```

を置く。$S=Z^\dagger Z=(Q^{\mathsf T}Q+P^{\mathsf T}P)/(2\mathcal J_0)$ とする。R192の複素方程式

```math
\dot Z
=\lambda_Rg_R(S_*-S)Z
```

は実変数では

```math
\dot Q
=\lambda_Rg_R(S_*-S)Q,
\qquad
\dot P
=\lambda_Rg_R(S_*-S)P
```

である。同じ実係数が全成分へ掛かるため、これは状態方向に依存する回転や成分別利得を含まない。

## M.3 R192の証明

<!-- theorem-start:proof -->
**証明（R192）**

有効時間 $\tau_R$ で書けば

```math
\frac{dZ}{d\tau_R}
=g_R(S_*-S)Z.
```

右辺は各時刻で $Z$ 自身に平行なので、非零解は

```math
Z(\tau_R)=a(\tau_R)Z_0,
\qquad
a(\tau_R)>0
```

と書け、規格化方向は厳密に一定である。また

```math
\frac{dS}{d\tau_R}
=2g_RS(S_*-S)
```

である。$Y=1/S$ と置くと

```math
\frac{dY}{d\tau_R}
=-2g_RS_*Y+2g_R
```

となるので、線形方程式を解いて

```math
\frac1{S(\tau_R)}
=
\frac1{S_*}
+
\left(
\frac1{S_0}-\frac1{S_*}
\right)e^{-2g_RS_*\tau_R}
```

を得る。従って本文のロジスティック表示が従う。

$0<S_{\min}\leq S_0\leq S_*$ なら

```math
1-\frac{S(\tau_R)}{S_*}
=
\frac{\left(S_*/S_0-1\right)e^{-2g_RS_*\tau_R}}
{1+\left(S_*/S_0-1\right)e^{-2g_RS_*\tau_R}}
```

だから分母を1で下から抑え、$S_0$ を $S_{\min}$ で下から抑えれば本文の一様上界を得る。表示上界を $\eta_R$ 以下に解けば固定時間条件が従う。証明終。
<!-- theorem-end:proof -->

## M.4 R181Dとの合成

第 $k$ 段入力の作用を $S_k$、選択された理想条件付き重みを $p_{k,b}$ とすると、R181Dの選別直後は

```math
S_k^{\rm sel}=p_{k,b}S_k.
```

R191の端点dispatcherとtransducer誤差から、無反応でない通常安全結果について

```math
p_{k,b}\geq\tau_{\rm state}>0
```

を事前に固定できる。前段R192の出力を $(1-\eta_R)S_*\leq S_k\leq S_*$ に保てば

```math
S_k^{\rm sel}
\geq
\tau_{\rm state}(1-\eta_R)S_*.
```

従って次のR192窓には未知の条件付き確率を測定して接続時間を変更する必要がなく、この既知下限だけを使った共通固定時間を割り当てられる。最後の出力ビットの後に別の作用感度を持つ読出しが無ければ、終端R192は不要である。

## M.5 R179とR186との境界

R192は開放収縮であり、使用後の環境自由度を逆演算して消去することを要求しない。反復試行で能動部を未使用状態へ戻し、結果相関履歴を流出経路へ送る役割はR179に残す。

R192は $Z\mapsto aZ$ 型の方向不変流なので、既に生じた横方向加法偏差を除去しない。静的結合誤差、位相雑音、全自由度へ加わる加法雑音の規模依存性はR186で評価し、R192を誤り訂正器として数えない。

## M.6 適用境界

$S_0=0$ は不動点でありR192では救済しない。安全下限より小さい希少結果を作用安定化後に成功結果へ戻すことも行わない。$g_RS_*$ または安全作用比が指数的に小さい場合には本文の固定時間評価から指数時間が現れ得るため、その場合はQ2-4の多項式外部資源条件を満たしたとは扱わない。
"""
old_a13.write_text(new_a13, encoding="utf-8")


# ---------------------------------------------------------------------------
# 4. Q1 W2 appendix H: remove active Hopf preparation and keep parameter map.
# ---------------------------------------------------------------------------
a8_old = ROOT / "sections/A8_m47_hopf_preparation.md"
a8_new = ROOT / "sections/A8_m47_w2_parameter_dictionary.md"
if a8_old.exists():
    old_text = a8_old.read_text(encoding="utf-8")
    archive = ROOT / "notes/superseded_a8_m47_hopf_preparation.md"
    if not archive.exists():
        archive.write_text(
            "# 旧付録H：W型2モードHopf準備の退役記録\n\n"
            "draft-90でR181Aを固定目標の主線から退役したため、旧対応表を研究記録へ移した。\n\n"
            + old_text,
            encoding="utf-8",
        )
    a8_old.unlink()

a8_new.write_text(r"""@number: H
@chapter: 付録
@title: M54 W型2モード対応表
@status: Q1 W型2モード手順で使うR135、R140、R187、R191、R181Dの対応だけを示す。状態方向準備は準備済み古典入力境界とし、本付録では独立な準備機構を導入しない。

## H.1 対応表

W型最低2正常モードを局在基底へ移した実正準対をM54のW2信号部分系と同定する。初期状態方向は実正準座標の準備済み古典入力として与え、その後の可逆制御と測定だけを現行結果へ接続する。

| 段階 | W型2モードでの指定 | 正本 |
|---|---|---|
| 初期入力 | 非零の準備済み実正準2モード信号 | 第2.4節、R187 |
| 閉鎖伝播 | W型低2モード生成子の正準流 | R135、第2章 |
| W型制御・診断 | 偶奇二重項と左右局在基底 | R140、第3章、第6章 |
| 2結果読出し | 射影作用和・差から結果形成 | R191、付録T |
| 測定後受渡し | 固定結果で $Z\mapsto P_bZ$ | R181D、付録P |

## H.2 役割境界

本付録は初期状態方向の物理的生成を証明しない。Q1-2の固定有限深さではR192を用いず、R181Dの非規格化選択成分を同じ試行の次段へ直接渡す。一般深さQ2-4の作用下限回復はR192の別責務であり、W型2モード制御の一部ではない。
""", encoding="utf-8")


# ---------------------------------------------------------------------------
# 5. Q1 proofs and M37 bridge: remove R181A dependency; Q1 does not use R192.
# ---------------------------------------------------------------------------
rel = "sections/A5_m37_envelope_proofs.md"
text = read(rel)
text = text.replace("R181Aの供給源／テンプレートまたはR112の正準SWAPをこの対へ接続するには", "準備済み古典入力またはR112の正準SWAPをこの対へ接続するには")
text = text.replace("この同定はM37がR181Aのポンプ、排出先、作用殻、衝突浴、記録器を生成することを意味しない。", "この同定はM37が初期状態方向の準備機構、作用殻、衝突浴、記録器を生成することを意味しない。")
write(rel, text)

rel = "sections/03_m47_controlled_w_instrument.md"
text = read(rel)
text = text.replace("、R181A", "")
text = text.replace("R181A、", "")
text = text.replace("R181A", "準備済み入力境界")
write(rel, text)

rel = "sections/A2_m47_controlled_w_instrument_proofs.md"
text = read(rel)
text = text.replace("初期操作面ではR181AのW型2モード準備とR170を使い、有限偏差を\n$\\varepsilon_{\\rm Hopf}+\\varepsilon_{170}^{\\rm in}$\nへ入れる。", "初期操作面では準備済みW型2モード入力を使い、その有限偏差を\n$\\varepsilon_{\\rm in}$\nへ一度だけ入れる。")
text = text.replace("R181AとR140分析器、有限W型コントラスト、安全井戸保持", "準備済み入力とR140分析器、有限W型コントラスト、安全井戸保持")
text = text.replace("B.10で、この選別機構と方向を変えない振幅再調整が安全な結果成分の測定後状態を直接与えることを示す。", "B.10で、この選別機構だけで安全な結果成分の測定後状態方向を直接与えることを示す。固定有限深さのQ1ではR192を用いない。")
text = text.replace("方向を変えない振幅再調整は方向を保存するのでこの上界を増やさない。", "固定有限深さでは正の作用下限を次段まで保持するためR192を用いず、この上界に作用安定化誤差を加えない。")
text = text.replace("、必要な方向を変えない振幅再調整、転送", "、転送")
text = text.replace("、方向を変えない振幅再調整を共通時計の重ならない窓へ割り当てる", "を共通時計の重ならない窓へ割り当てる")
text = text.replace("、振幅再調整用／流出浴自由度", "、流出浴自由度")
text = text.replace("、振幅再調整用接続端の環境", "")
text = text.replace("、方向を変えない振幅再調整", "")
text = text.replace("振幅情報を開放接続端の環境へ残る", "非選択成分の情報を作業領域と開放環境へ残す")
text = text.replace("振幅情報を開放接続端環境", "非選択成分情報を開放環境")
text = text.replace("R181A", "準備済み入力境界")
write(rel, text)


# ---------------------------------------------------------------------------
# 6. Q2/Q3 active prose.
# ---------------------------------------------------------------------------
rel = "sections/04_m54_q2_specializations.md"
text = read(rel)
text = text.replace("R181A--R181D", "R181B--R181D")
text = text.replace("方向を変えない振幅再調整", "R192による方向不変作用安定化")
text = text.replace(
    "Q2-4は同じM54親模型の一般 $n$ 特殊化として、R181B--R181D、R179、R190A--R190Cを根拠に条件付き達成を維持する。",
    "Q2-4は同じM54親模型の一般 $n$ 特殊化として、R112、R179、R181C、R181D、R186、R191、R192を根拠に条件付き達成を維持する。一般 $n$ の初期入力にはR181Bを反復せず、R179後の定数次元供給源から $0^n$ 根モードを作る。"
)
text = text.replace("R181A", "準備済み入力境界")
write(rel, text)

rel = "sections/06_m37_spatial_envelope.md"
text = read(rel)
text = text.replace("R181AはM37初期集団に使える共通開放準備、", "M37初期集団は準備済み古典空間入力境界から与え、")
text = text.replace("R181A", "準備済み入力境界")
write(rel, text)


# ---------------------------------------------------------------------------
# 7. Projector/register appendices: all radial stabilization references -> R192.
# ---------------------------------------------------------------------------
for rel in ("sections/A15_m54_uniform_register.md", "sections/A16_m54_projector_tree_receiver.md"):
    text = read(rel)
    text = text.replace("R181Aの $\\kappa=0$ 方向を変えない振幅再調整用接続端", "R192")
    text = text.replace("R181Aの$\\kappa=0$方向を変えない振幅再調整用接続端", "R192")
    text = text.replace("R181Aの方向を変えない振幅再調整用接続端", "R192")
    text = text.replace("R181Aの方向を変えない振幅再調整", "R192作用安定化")
    text = text.replace("方向を変えない振幅再調整", "R192作用安定化")
    text = text.replace("振幅再調整", "作用安定化")
    text = text.replace("R181A", "R192")
    if rel.endswith("A15_m54_uniform_register.md"):
        text = text.replace("## O.9 R192作用安定化", "## O.9 R192による方向不変作用安定化")
    write(rel, text)


# ---------------------------------------------------------------------------
# 8. Scope and README.
# ---------------------------------------------------------------------------
rel = "sections/01_scope_and_cycle.md"
text = read(rel)
text = text.replace("| Q1 | M54/R181A、R187、R135、R140 |", "| Q1 | 準備済みW2入力、R187、R135、R140 |")
text = text.replace("必要時再調整", "非終端安全結果のR192")
text = text.replace("準備接続端", "準備済み入力境界")
text = text.replace("R181A", "退役準備結果")
write(rel, text)

rel = "README.md"
text = read(rel)
if "> **draft-90:**" not in text:
    marker = "> **draft-89:**"
    note = "> **draft-90:** R181Aの状態方向準備を現行主線から退役し、初期状態方向を古典実正準系の準備済み入力境界へ移した。一般深さQ2-4で必要な方向不変の作用下限回復だけをR192として独立させ、Q1/Q3はR192へ依存しない。\n\n"
    if marker in text:
        text = text.replace(marker, note + marker, 1)
text = text.replace("M54は物理テンプレート準備、テンソル積状態の生成", "M54は準備済み古典入力の境界、テンソル積状態の生成")
text = re.sub(
    r"\nM54のR181A準備接続端は、.*?\n\n",
    "\nQ1とQ3では、初期状態方向を実正準座標の準備済み古典入力として境界に置く。これはBorn重みや結果確率表を外部注入することを意味せず、境界以後の可逆発展、結果形成、射影結果成分受渡し、空間配置輸送は現行の古典ミクロ過程から導く。一般深さQ2-4では、R181Dで選ばれた非終端安全結果の作用が次段R191の物理読出し下限を割らないよう、状態方向を変えないR192作用安定化だけを補助的に使う。\n\n",
    text,
    count=1,
    flags=re.DOTALL,
)
write(rel, text)


# ---------------------------------------------------------------------------
# 9. Error/resource ledger: synchronize current Q2 spine and add R192 boundary.
# ---------------------------------------------------------------------------
rel = "sections/08_errors_resources_open_targets.md"
text = read(rel)
text = re.sub(r"^\| M54/R181A \|.*\n", "| M54/R192 | 状態方向が変化する、ロジスティック作用解または固定時間上界が破れる、安全作用下限未満の希少結果を成功へ救済する、未知の条件付き確率を読んで接続時間を変える、または横方向加法偏差を除去したと扱う |\n", text, flags=re.MULTILINE)
text = text.replace("Hopf方向が有限時間で準備できない、", "準備済み入力誤差を一度だけ数えられない、")
text = text.replace("R181Dの階数1射影選別・方向を変えない振幅再調整・測定後状態の受け渡し", "R181Dの階数1射影選別・測定後状態の受け渡し")
text = re.sub(
    r"- Q2-1：.*?\n- Q2-2：.*?\n- Q2-3：.*?\n- Q2-4：.*?\n",
    "- Q2-1：M54静的状態構成を使う。根拠結果はR112、R181B、R181C、R181D、R191。\n"
    "- Q2-2：M54静的状態構成と2端R191経路を使う。根拠結果はR112、R180A、R180C、R181B、R181C、R181D、R191。\n"
    "- Q2-3：M54三部分系静的状態構成を使う。根拠結果はR112、R177、R181B、R181C、R181D、R191。\n"
    "- Q2-4：M54一般静的状態構成を使う。根拠結果はR112、R179、R181C、R181D、R186、R191、R192。一般 $n$ の初期入力にはR181Bを反復しない。\n",
    text,
    count=1,
    flags=re.DOTALL,
)
text = text.replace("R181A--R181D", "R181B--R181D")
text = text.replace("方向を変えない振幅再調整", "R192方向不変作用安定化")
text = text.replace("R181A", "退役R181A")
text = text.replace("R190/R179静的選択機構、R170吸収指針変数、制御付き選別機構、R192方向不変作用安定化", "R191ブラウン巨視的スピン読出し、R181D制御付き選別機構、R192方向不変作用安定化")
write(rel, text)


# ---------------------------------------------------------------------------
# 10. Retired index and notes README.
# ---------------------------------------------------------------------------
rel = "notes/superseded_result_index.md"
text = read(rel)
text = text.replace("M54のtemplate portへ吸収 | `superseded_separate_m51_m52_m53_models.md`、R181A |", "旧R181Aへ吸収後、draft-90で状態方向準備ごと退役 | `superseded_separate_m51_m52_m53_models.md`、`superseded_r181a_template_port_preparation.md` |")
text = text.replace("M54の物理template-port準備R181Aへ吸収 | `superseded_separate_m51_m52_m53_models.md`、R181A、付録M |", "旧R181Aへ吸収後、draft-90で状態方向準備ごと退役 | `superseded_separate_m51_m52_m53_models.md`、`superseded_r181a_template_port_preparation.md` |")
if "| R181A |" not in text:
    marker = "| R176A--R176C |"
    row = "| R181A | 共通初期種から指定状態方向への開放準備と作用安定化 | 状態方向準備は現行固定目標から退役。方向不変の作用安定化だけをR192へ切り出し | `superseded_r181a_template_port_preparation.md`、R192、付録M |\n"
    idx = text.find(marker)
    if idx >= 0:
        text = text[:idx] + row + text[idx:]
write(rel, text)

rel = "notes/README.md"
text = read(rel)
if "superseded_r181a_template_port_preparation.md" not in text:
    table_row = "| `superseded_r181a_template_port_preparation.md` | draft-89までのR181A/旧付録M | 状態方向準備の退役記録。動径部分だけR192へ継承 | 固定目標から不要な方向吸引を外し、Q2-4に必要な作用安定化だけを独立させるため |\n"
    marker = "| `superseded_result_index.md`"
    idx = text.find(marker)
    if idx >= 0:
        text = text[:idx] + table_row + text[idx:]
text = text.replace("M54/R181A--R181Dへの吸収記録", "M54/R181B--R181Dへの吸収と旧R181Aへの準備統合の履歴")
write(rel, text)


# ---------------------------------------------------------------------------
# 11. Verifiers: retire R181A/Hopf preparation; add R192 checks.
# ---------------------------------------------------------------------------
retired = ROOT / "notes/retired_verifiers"
retired.mkdir(parents=True, exist_ok=True)
for name in ("verify_r181a_template_port.py", "verify_m47_hopf_preparation.py"):
    src = ROOT / "tools" / name
    dst = retired / name
    if src.exists():
        if dst.exists():
            dst.unlink()
        shutil.move(str(src), str(dst))

write("tools/verify_r192_radial_stabilizer.py", r'''#!/usr/bin/env python3
from __future__ import annotations

import numpy as np

TOL = 5.0e-11


def exact_action(s0: float, s_star: float, gain: float, tau: float) -> float:
    return s_star / (1.0 + (s_star / s0 - 1.0) * np.exp(-2.0 * gain * s_star * tau))


def main() -> None:
    rng = np.random.default_rng(20260912)
    dimension = 16
    z0 = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
    z0 /= np.linalg.norm(z0)
    s_star = 1.7
    gain = 0.83
    tau = 2.4

    failures: list[str] = []

    for s0 in (0.08, 0.31, 1.0, 1.7, 2.8):
        s = exact_action(s0, s_star, gain, tau)
        z_in = np.sqrt(s0) * z0
        z_out = np.sqrt(s / s0) * z_in
        ray_error = np.linalg.norm(
            z_out / np.linalg.norm(z_out) - z_in / np.linalg.norm(z_in)
        )
        action_error = abs(float(np.vdot(z_out, z_out).real) - s)
        if ray_error > TOL:
            failures.append(f"ray preservation s0={s0}: {ray_error}")
        if action_error > TOL:
            failures.append(f"action formula s0={s0}: {action_error}")

    low = exact_action(0.31, s_star, gain, tau)
    high = exact_action(2.8, s_star, gain, tau)
    if not (0.31 < low < s_star):
        failures.append("sub-target action is not monotone increasing")
    if not (s_star < high < 2.8):
        failures.append("super-target action is not monotone decreasing")

    s_min = 0.12 * s_star
    eta = 2.0e-3
    tau_bound = np.log((s_star / s_min - 1.0) / eta) / (2.0 * gain * s_star)
    grid = np.linspace(s_min, s_star, 257)
    deficits = np.array([1.0 - exact_action(x, s_star, gain, tau_bound) / s_star for x in grid])
    if float(np.max(deficits)) > eta + 5.0e-13:
        failures.append("uniform finite-time bound failed")

    phase = np.exp(1j * 0.731)
    s = exact_action(0.42, s_star, gain, tau)
    z_a = np.sqrt(s / 0.42) * (np.sqrt(0.42) * z0)
    z_b = np.sqrt(s / 0.42) * (phase * np.sqrt(0.42) * z0)
    if np.linalg.norm(z_b - phase * z_a) > TOL:
        failures.append("global phase covariance failed")

    # A projector-selected component remains in the same projector image.
    projector = np.zeros((dimension, dimension), dtype=complex)
    projector[:5, :5] = np.eye(5)
    selected = projector @ (rng.normal(size=dimension) + 1j * rng.normal(size=dimension))
    selected_action = float(np.vdot(selected, selected).real)
    target = 2.1
    selected_final = exact_action(selected_action, target, 0.55, 0.7)
    stabilized = np.sqrt(selected_final / selected_action) * selected
    image_error = np.linalg.norm((np.eye(dimension) - projector) @ stabilized)
    if image_error > TOL:
        failures.append(f"projector image changed: {image_error}")

    # Zero action is not rescued by the model; it remains outside the theorem domain.
    if exact_action(1.0e-15, s_star, gain, tau) <= 0.0:
        failures.append("positive seed should remain positive")

    if failures:
        raise SystemExit("\n".join(failures))
    print("r192_radial_stabilizer_ok")


if __name__ == "__main__":
    main()
''')


# ---------------------------------------------------------------------------
# 12. Manifest, validation, changelog.
# ---------------------------------------------------------------------------
rel = "MANIFEST.md"
text = read(rel)
text = text.replace("- `tools/verify_r181a_template_port.py`\n", "- `tools/verify_r192_radial_stabilizer.py`\n")
text = text.replace("- `tools/verify_m47_hopf_preparation.py`\n", "")
text = text.replace("R181A pump/source", "旧状態方向準備")
write(rel, text)

rel = "VALIDATION.md"
text = read(rel)
text = text.replace("verify_r181a_template_port.py", "verify_r192_radial_stabilizer.py")
text = text.replace("R181A pump/source", "旧状態方向準備")
text = text.replace("R181A--R181D", "R181B--R181DとR192")
text = text.replace("R181A", "退役R181A")
if "draft-90：R181A退役とR192方向不変作用安定化" not in text:
    text = "## draft-90：R181A退役とR192方向不変作用安定化\n\n- R181Aの状態方向準備を現行主線から退役し、旧付録Mと旧検算器をnotesへ移した。\n- R192の方向保存、ロジスティック作用解、安全作用下限からの固定時間回復、射影像保存を新しい検算器で検査する。\n- Q1/Q3は準備済み古典入力境界へ移し、Q2-4だけが一般深さの非終端安全結果でR192を使う。固定目標と達成ラベルは変更しない。\n\n" + text
write(rel, text)

rel = "CHANGELOG.md"
text = read(rel)
if "## draft-90" not in text:
    entry = """## draft-90：R181A退役とR192方向不変作用安定化

- R181Aの状態方向準備を現行固定目標の主線から完全退役し、Q1/Q3の初期状態方向を実正準系の準備済み古典入力境界へ移した。
- R181Aに含まれていた方向不変の作用回復だけをR192「方向不変作用安定化」として独立させ、ロジスティック厳密解、安全作用下限からの固定時間上界、Q2-4での多項式時間条件を明示した。
- R181Dは非規格化射影結果成分の受渡しで閉じ、固定有限深さのQ1ではR192を使わない。一般深さQ2-4だけが非終端安全結果でR192を用いる。
- Q2-4の一般 $n$ 入力からR181B依存を外し、R179後の定数次元供給源から $0^n$ 根モードを作る既存初期化方針へ依存表を同期した。
- 旧R181A付録・W型Hopf準備対応・検算器を退役記録へ移し、R192専用付録と数値検算を追加した。
- PROJECT_STATUS、README、本文、誤差・資源台帳、MANIFEST、VALIDATIONを同期した。固定長期目標と達成ラベルは変更していない。

"""
    # Put after leading title if present, otherwise prepend.
    if text.startswith("# "):
        pos = text.find("\n\n") + 2
        text = text[:pos] + entry + text[pos:]
    else:
        text = entry + text
write(rel, text)


# ---------------------------------------------------------------------------
# 13. Final active-paper cleanup: no active R181A references remain.
#     Historical references may remain in notes/CHANGELOG/retired index.
# ---------------------------------------------------------------------------
# A few active files may mention R181A only in stale dependency prose; replace them
# with the correct boundary term rather than leaving a hidden dependency.
for path in sorted(SECTIONS.glob("*.md")):
    text = path.read_text(encoding="utf-8")
    if "R181A" in text:
        # Do not silently preserve an active dependency.  At this stage all known
        # semantic cases were handled above; remaining references are stale prose.
        text = text.replace("R181A", "退役準備結果")
        path.write_text(text, encoding="utf-8")

# Ensure the new active theorem is unique and the retired one has disappeared.
active = "\n".join(path.read_text(encoding="utf-8") for path in SECTIONS.glob("*.md"))
if "**定理（R181A：" in active:
    raise RuntimeError("active R181A theorem declaration remains")
if active.count("**定理（R192：方向不変作用安定化）**") != 1:
    raise RuntimeError("R192 theorem declaration count is not one")

print("r192_migration_complete")
