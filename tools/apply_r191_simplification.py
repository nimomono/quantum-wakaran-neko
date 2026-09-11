#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ROOT / "sections"
NOTES = ROOT / "notes"
TOOLS = ROOT / "tools"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing replacement target: {label}")
    return text.replace(old, new, 1)


def replace_regex(text: str, pattern: str, replacement: str, label: str) -> str:
    new, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"expected one regex replacement for {label}, got {count}")
    return new


def extract_regex(text: str, pattern: str, label: str) -> str:
    match = re.search(pattern, text, flags=re.S)
    if not match:
        raise RuntimeError(f"missing extract target: {label}")
    return match.group(0).strip() + "\n"


# ---------------------------------------------------------------------------
# Archive superseded material before shrinking the active paper.
# ---------------------------------------------------------------------------
NOTES.mkdir(exist_ok=True)
retired_verifiers = NOTES / "retired_verifiers"
retired_verifiers.mkdir(exist_ok=True)

common_path = SECTIONS / "02_common_canonical_modules.md"
common_old = read(common_path)
r190_section = extract_regex(
    common_old,
    r"### 2\.8\.1 R190A--R190C：.*?(?=\n### 2\.8\.2 R191：)",
    "R190 section",
)
r170_section = extract_regex(
    common_old,
    r"## 2\.9 R170：.*?(?=\n## 2\.10 )",
    "R170 section",
)
write(
    NOTES / "superseded_r190_r170_measurement_path.md",
    """# 退役したR190--R170作用殻型測定経路

このメモは、draft-88でR191がQ1/Q2の2結果射影読出しを直接担うようになった後も本文に残っていたR190A--R190CとR170の旧主線を保存する。今回の縮約では、固定Q1/Q2の必須因果鎖から外し、Q3の初期配置はR164、反復装置のopen resetはR179、2結果読出しはR191へ責務を分離した。

ここに保存する定理は反証されたものではない。2作用LC殻、Drude混合、対称作用開口、静的吸収pointerという別の物理実現候補として、比較・将来拡張用に保持する。現行Q1/Q2の誤差予算へ重複加算しない。

""" + r190_section + "\n" + r170_section,
)

q22_old_path = SECTIONS / "05_m54_setting_pre_receiver.md"
q22_old = read(q22_old_path)
write(
    NOTES / "superseded_q2_2_paired_hopf_receiver.md",
    """# 退役したQ2-2 paired-Hopf受信機構

このメモは、R180Aの中央選択後にR180Bの供給源駆動2端Hopf吸引で2翼信号を再準備し、切断後に両翼を再読出ししていた旧Q2-2章を保存する。R191の非規格化branch受渡しとLüders telescopingにより、固定・非空間分離・有限設定族という現行Q2-2の範囲では、A端R191の結果branchをprojector routerでB端へ直接渡せるためR180Bを必須主線から外した。

旧構成は反証されたものではない。物理的に2翼テンプレートを独立に再形成する強化案として参照できる。

---

""" + q22_old,
)

for src, dst_name in (
    (SECTIONS / "A9_m54_setting_pre_paired_hopf_receiver.md", "superseded_A9_paired_hopf_receiver.md"),
    (SECTIONS / "A19_m54_drude_action_shell_bridge.md", "superseded_A19_drude_action_shell_bridge.md"),
):
    if src.exists():
        shutil.move(str(src), str(NOTES / dst_name))

for name in (
    "verify_r190_drude_shell.py",
    "verify_r180_bell_cycle.py",
    "verify_m54_static_instrument.py",
):
    src = TOOLS / name
    if src.exists():
        shutil.move(str(src), str(retired_verifiers / name))

# ---------------------------------------------------------------------------
# Overview: make the new spine visible before any historical implementation.
# ---------------------------------------------------------------------------
write(
    SECTIONS / "00_overview_and_contents.md",
    r"""@number: 0
@chapter: 概要
@title: 概要

本論文の中心的な問いは、明示的な古典力学モデルから、量子力学に似た可逆操作、Born型測定統計、測定後状態、結合ゲート、Bell型共同統計、空間伝播がどこまで有効構造として現れるかである。複素振幅は独立した実体ではなく実正準信号の派生表示とし、単一試行の物理信号と試行集団の統計量を区別する。

M54をQ1--Q3の共通有効状態構成族、M37を空間信号とW型低2モードの物理実装層とする。状態準備・可逆操作と、排他的な測定結果形成を同一視しない。Q1/Q2の2結果射影読出しはR191ブラウン巨視的スピンinstrumentを正本とし、Q3の実在粒子位置はR164で開始面を準備した後にR161/R162で輸送する。

Q1/Q2の測定主線は

```math
Z
\longrightarrow
(J_+,J_-)
\xrightarrow{\mathrm{R191}}
r
\xrightarrow{\mathrm{R181D\ router}}
P_rZ
```

である。$J_\pm=\mathcal J_0Z^\dagger P_\pm Z$ を保持し、R191は作用和と作用差からブラウン巨視的スピンの吸引域境界を作る。理想極限では

```math
P(r=\pm)
=\frac{J_\pm}{J_++J_-}.
```

結果後は物理信号を非線形に規格化せず、R181Dの可逆projector routerが $P_rZ$ と補成分を分ける。次段R191は残った作用和で自動的に条件付き確率を読むため、固定有限深さでは振幅再調整を必須としない。一般深さQ2-4でbranch作用が読出し下限へ落ちる場合だけ補助的な再調整を許す。

Q1ではM37弱結合W型の最低2正常モードをR187でM54のW2信号へ接続し、R140が有限 $SU(2)$ 操作とRabi運動を与える。R143--R144は分析器、有限コントラスト、局所記録、逐次測定の系列固有部分を担い、結果確率はR191、測定後branchはR181Dへ委ねる。R189A--R189Cは走行中作用保持と有限2回Rabi--Zeno比較を与える。

Q2-1とQ2-3ではR181Bが固定入力のテンソル積信号を作り、R181Cが同じ永続記憶部上で局所gateと結合gateを作用する。末端測定はR191とR181Dだけを使う。Q2-4では同じ2結果nodeを逐次使用し、R179は結果相関履歴の排出とopen resetだけを担う。

Q2-2は固定一重項、固定有限設定族、準備先行、非空間分離の古典装置として扱う。末端4モード信号にA設定を作用し、A端R191で結果 $r$ を形成した後、非規格化branchをprojector routerでB端へ渡す。B設定をそこで作用し、B端R191で $s$ を形成する。

```math
Z_{AB}
\xrightarrow{x}
\mathrm{R191}_A
\longrightarrow
P_{A,r}Z_{AB}
\xrightarrow{y}
\mathrm{R191}_B
\longrightarrow
(r,s).
```

局所射影が可換なので共同分布は

```math
P(r,s\mid x,y)
=
\frac{\|P_{B,s}^{y}P_{A,r}^{x}Z_{AB}\|^2}{\|Z_{AB}\|^2}.
```

一重項型信号では余弦共同統計、非信号性、CHSH/Tsirelson値を回収する。A結果branchがB端へ物理的に渡るため、これは空間分離Bell局所模型ではない。自由設定・空間分離・loophole-free Bell実験の古典局所説明を主張しない。

Q3の位置主線は別である。

```math
Z_{t_0}
\xrightarrow{\mathrm{R164}}
X_{t_0}
\xrightarrow{\mathrm{R161/R162}}
X_T
\xrightarrow{\mathrm{record}}
D_{X_T}.
```

R161は確率流と活動量から前向き・後向き率を整合させ、R162はその有向率を開放Poisson-jump過程として実現する。R185は同じ前向き経路法則のBayes反転からNelson型の前進・後退平均微分と時間対称Newton則へ接続する。

この再編で、旧R190A--R190Cの2作用LC殻Drude混合、R170静的吸収pointer、R180B paired-Hopf受信機構は固定Q1/Q2の必須主線から退役した。内容は `notes/` とGit履歴へ保存し、反証されたものとして扱わない。論文本文では同じBorn結果を複数の物理経路で重複説明せず、現在の最小因果鎖だけを正本とする。
""",
)

# ---------------------------------------------------------------------------
# Chapter 1: current causal map only.
# ---------------------------------------------------------------------------
write(
    SECTIONS / "01_scope_and_cycle.md",
    r"""@number: 1
@chapter: 本文
@title: 問題設定、現行模型、達成範囲
@status: M54をQ1・Q2・Q3の共通有効状態構成族、M37を物理実装層として区別し、Q1/Q2のR191射影読出しとQ3のR164--R161/R162位置輸送を二つの現行因果鎖として整理する。

## 1.1 研究上の問い

本稿は、古典的な粒子、実振動子、熱浴、制御器、記録器から、量子力学に特徴的な状態空間、可逆力学、Born型排他的結果、測定後状態、複合系相関、空間力学がどこまで有効構造として現れるかを調べる。有限次元Schrödinger方程式を古典正準座標へ書き換えるだけでは、1回の試行で生じる排他的結果、Born則、記録、resetは得られないため、信号力学と測定instrumentを分けて構成する。

古典振動子・古典波で有限次元Hilbert空間、unitary、量子gateを模擬できること自体は先行研究がある。本稿の物理課題は、各試行の実信号から排他的結果を形成し、その結果branchを同じ試行の次操作へ渡すこと、有限時間・有限温度・無反応・誤差を装置境界まで含めて明示することにある。

## 1.2 現行因果鎖

Q1/Q2の2結果測定では、射影作用を

```math
J_\pm
=\mathcal J_0Z^\dagger P_\pm Z
```

として保持し、R191へ渡す。

```math
Z
\longrightarrow
(J_+,J_-)
\xrightarrow{\mathrm{R191}}
r
\xrightarrow{\mathrm{R181D}}
P_rZ.
```

R191が結果形成と吸収記録までを担い、R181Dは結果を生成せずprojector routerと測定後branch受渡しだけを担う。固定有限深さでは非規格化branchをそのまま次段R191へ渡す。一般深さで作用下限が不足する場合だけ方向を変えない振幅再調整を補助的に使う。

Q3では実在粒子位置を別の因果鎖で扱う。

```math
Z_{t_0}
\xrightarrow{\mathrm{R164}}
X_{t_0}
\xrightarrow{\mathrm{R161/R162}}
X_T
\xrightarrow{\mathrm{R112\ record}}
D_{X_T}.
```

R164はQ3開始面の条件付き配置を作り、R161/R162は同じ粒子を輸送する。Q1/Q2の測定結果を粒子位置の再平衡化で作る経路は現行主線に使わない。

## 1.3 現行模型と実装階層

| 識別 | 分類 | 現行責務 |
|---|---|---|
| M54 | 共通有効信号--配置状態構成族 | 有限実正準信号、準備接続端、永続記憶部、作業領域、時計、記録の共通型。Q1/Q2はR191、Q3はR164--R161/R162へ接続する |
| M37 | 物理Hamiltonian実装層 | Q3空間信号を局所ばね網で実装し、R187条件下ではW型最低2正常モードをQ1 W2制御信号へ接続する |
| M0 | 単一ミクロ装置統一目標 | transducer、macrospin、router、record、reset、M37信号系を共通接続端とHamiltonian無限浴へ統合する未完成の強化目標 |

M54の複素信号 $Z$ は実正準対の派生表示であり、独立した複素実体ではない。状態方向、規格化共分散、位置分布は解析上の統計量であり、単一試行の制御器へ書き戻さない。

## 1.4 系列ごとの最小構成

| 系列 | 信号準備・操作 | 結果形成・受渡し |
|---|---|---|
| Q1 | M54/R181A、R187、R135、R140 | R191、R181D、R143--R144、R189A--R189C |
| Q2-1 | R181B、R181C | R191を2段、R181D router |
| Q2-2 | 固定一重項4モード、A/B設定gate | A端R191、R181D型router、B端R191、R180A/R180C監査 |
| Q2-3 | R181Bを2回、R181C、R177 | R191逐次読出し、R181D router |
| Q2-4 | M54一般 $2^n$ 直接モード、R181C | R191逐次読出し、R181D、必要時repump、R179 open reset、R186資源監査 |
| Q3 | M54空間状態構成、M37、R184 | R164開始配置、R161/R162輸送、R185 |

旧R190A--R190C、R170、R180Bは固定Q1/Q2の必須依存から外す。旧構成の詳細は `notes/` とGit履歴に保存する。

## 1.5 達成範囲

固定目標と達成ラベルは `PROJECT_STATUS.md` を正本とする。本再編は固定目標を変更しない。Q1-1、Q1-2、Q3-1--Q3-3Cは現行判定を維持し、Q2-1--Q2-4、Q3-4A、Q3-4B、Q3-5は各文書に明記した単一装置統合条件付き、Q3-6は未達のままとする。

## 1.6 非主張

本稿は、量子力学全体を古典力学へ還元したこと、空間分離Bell局所模型を得たこと、指数的な内部受動自由度を除去したこと、全系列を同一製造済み装置へ統合したことを主張しない。R191はQ1/Q2の2結果読出しを単純化するが、transducer、macrospin、router、record、resetを単一閉鎖Hamiltonianへ統合したことまでは意味しない。
""",
)

# ---------------------------------------------------------------------------
# Chapter 2: remove the superseded R190 and R170 sections, keep R191/R181D.
# ---------------------------------------------------------------------------
common = common_old
common = replace_regex(
    common,
    r"## 2\.1 M54をQ1--Q3共通有効状態構成族とする範囲.*?(?=\n## 2\.2 )",
    r"""## 2.1 M54をQ1--Q3共通有効状態構成族とする範囲

M54は有限個の実正準対から得る信号、準備・供給接続端、永続記憶部、可逆作業領域、作用保持指針、実在配置、記録、時計自由度を共通化する有効状態構成族である。派生複素座標を

```math
Z=\frac{Q+iP}{\sqrt{2\mathcal J_0}}
```

とするが、$Z$ は独立した複素実体ではない。Q1/Q2では2結果射影作用をR191読出しinterfaceへ渡し、Q3ではR164が開始配置 $X$ を準備してR161/R162へ渡す。測定結果用の静的配置変数やR170専用pointerをM54共通状態へ置かない。

概念上の共通状態を

```math
\Gamma_{54}^{(\Lambda,\mathcal I)}
=
(Z,S_{\rm port},G,W,J,A^\delta,X,D,\tau,S_{\rm ref})
```

と書く。$X$ はQ3空間状態構成で使う実在配置であり、Q1/Q2の2値結果はR191の吸収記録が担う。$A^\delta$ はR164を使うQ3開始配置または独立な作用殻研究線のために残す。R191のBrownian macrospin、mixing/decision浴、R179のopen reset浴は接続interfaceとして扱い、常設のM54信号座標とは分ける。

| 系列 | M54状態構成 | 準備・操作 | 現行出力 |
|---|---|---|---|
| Q1 | W型2モード信号 | R181A、R140、R187 | R191、R181D、R143--R144 |
| Q2-1 | 4モード永続記憶部 | R181B、R181C | R191逐次読出し、R181D |
| Q2-2 | 4モード＋2物理測定端 | R181B/R181C、設定gate | A端R191、router、B端R191、R180A/R180C |
| Q2-3 | 8モード永続記憶部 | R181Bを2回、R181C、R177 | R191逐次読出し、R181D |
| Q2-4 | $2^n$ 直接モード | R181C | R191、R181D、必要時repump、R179 reset |
| Q3 | 空間信号＋配置 | R181Aを準備接続端として使用可、M37/R184 | R164開始配置、R161/R162、R185 |

M37はM54へ吸収しない。Q3では局所位置ばね網から空間信号を実装し、Q1ではR187の弱結合W型族に限って最低2正常モードをW2制御信号へ接続する。全系列を同一の製造済み装置・同一パラメータ・単一周期へ統合するM0は別の未完成目標である。
""",
    "chapter 2.1",
)
common = replace_regex(
    common,
    r"### 2\.8\.1 R190A--R190C：.*?(?=\n### 2\.8\.2 R191：)",
    "",
    "remove R190 active section",
)
common = replace_regex(
    common,
    r"## 2\.9 R170：.*?(?=\n## 2\.10 )",
    "",
    "remove R170 active section",
)
common = common.replace(
    "R162はQ3の移動過程を担い、Q1/Q2の静的平方根選択の物理実現はR190/R179へ分離する。",
    "R162はQ3の移動過程だけを担う。R161の静的 $j=0$ 特殊化は数学的比較用に残すが、Q1/Q2の2結果読出し主線ではR191を使う。",
)
common = common.replace(
    "R161は静的・移動の率構成を共通に保つが、物理実現を一種類の有限衝突装置へ統一しない。Q3では新R162の開放jump過程を直接使う。Q1/Q2の静的状態構成では、作用殻状態数をR164、平方根核の具体的混合・開口をR190、反復時のfreshnessをR179が担う。旧R162の有限衝突・熱的特殊化は有限閉鎖実装の強化結果として退役メモに保存する。",
    "R161は静的・移動の率構成を共通に保つが、現行の物理主線ではQ3がR162の開放jump過程を使う。Q1/Q2の2結果測定はR161静的鎖を経由せずR191へ直接接続する。旧有限衝突・静的作用殻実装は退役メモに保存する。",
)
common = common.replace(
    "成功試行だけを再規格化しない。結果固定後の射影成分生成と次段受渡しは既存の共通射影選別機構/R181Dが担い、一般深さで成分作用下限が必要な場合だけ方向を変えない振幅再調整を使う。R164/R190/R170は一般有限結果集合、作用殻型実現、独立な強化経路として残す。",
    "成功試行だけを再規格化しない。結果固定後の射影成分生成と次段受渡しは既存の共通射影選別機構/R181Dが担い、一般深さで成分作用下限が必要な場合だけ方向を変えない振幅再調整を使う。Q1/Q2の2結果読出しではR191を唯一の現行主線とし、Q3の開始配置はR164へ分離する。",
)
common = common.replace(
    "混合評価、stochastic LLG、scale density、$q_{\\rm ret}$、$q_{\\rm time}$、端点dispatcher、熱力学、Q2-2で中央集約4結果samplerへ置換しない責務境界は付録Tに置く [56--58]。",
    "混合評価、stochastic LLG、scale density、$q_{\\rm ret}$、$q_{\\rm time}$、端点dispatcher、熱力学、逐次branch受渡しは付録Tに置く [56--58]。",
)
common = common.replace(
    "M54の能動部は信号、逆演算用補助記憶部、選別機構用作業領域、方向を変えない振幅再調整接続端、未処理／正則化容量指針変数、一様ゲートバス、吸収指針変数、出力記録、時計自由度を持つ。Q1/Q2の2結果読出しはR191のブラウン巨視的スピン接続部を主線とする。作用殻混合、再混合、リセット、散逸履歴を使うR190/R179は一般有限結果集合と代替実現へ残す。",
    "M54の能動部は信号、逆演算用補助記憶部、選別機構用作業領域、必要時の振幅再調整接続端、一様ゲートバス、出力記録、時計自由度を持つ。Q1/Q2の2結果読出しはR191のブラウン巨視的スピン接続部を主線とし、R179は反復運転時のopen resetと履歴排出だけを担う。",
)
common = common.replace(
    "この補題自身は確率的な結果選択を行わない。2結果射影測定の排他的選択と固定はR191を主線とし、一般有限結果集合または作用殻型の代替実現はR170が担う。**共通射影選別機構** の主線は",
    "この補題自身は確率的な結果選択を行わない。2結果射影測定の排他的選択と固定はR191が担う。**共通射影選別機構** の主線は",
)
common = common.replace(
    "R181Dはこの列を段階的に合成する。R164/R190/R170経路を選ぶ場合は段階2だけを代替し、R191と同じ選択誤差を二重計上しない。R180Aは同じ作用保持補題と対合選別機構を中央潜在結果成分の受渡しへ使う兄弟特殊化である。",
    "R181Dはこの列を段階的に合成する。R180Aは同じ作用保持補題と対合選別機構をQ2-2のA端branch受渡しへ使う兄弟特殊化である。",
)
common = common.replace(
    "M54の反復運転では、補助作業領域、指針変数、振幅再調整用接続端を有限閉鎖貯蔵部から供給せず、固定した一様規則を持つ流入／流出浴接続部へ接続する。未使用状態へのリセットは開放収縮として扱い、結果相関情報と使用済み環境自由度は流出経路へ流す。R190の反復作用殻混合では、各試行が過去に装置と相互作用していない定常流入浴部分系を使う。",
    "M54の反復運転では、補助作業領域、R191指針変数、必要時の振幅再調整接続端を固定した一様規則を持つ流入／流出浴接続部へ接続する。未使用状態へのリセットは開放収縮として扱い、結果相関情報と使用済み環境自由度は流出経路へ流す。",
)
common = common.replace("**定理（R179：一様開放供給・リセット・再混合）**", "**定理（R179：一様開放供給・リセット）**")
write(common_path, common)

# ---------------------------------------------------------------------------
# Q1 chapter: replace only the responsibility/operation overview; keep the
# detailed W-mode, Rabi and Zeno derivations below 3.2 intact.
# ---------------------------------------------------------------------------
q1_path = SECTIONS / "03_m47_controlled_w_instrument.md"
q1 = read(q1_path)
q1 = re.sub(
    r"@status: .*?\n",
    "@status: 旧M47で扱ったQ1系列をM54のW2静的状態構成上の系列固有手順として整理し、R187のM37物理信号系、R181A準備、R140操作、R191読出し、R181D branch受渡し、R143--R144、R189A--R189Cの有限Rabi--Zeno比較へ接続する。\n",
    q1,
    count=1,
)
q1 = replace_regex(
    q1,
    r"## 3\.1 Q1 W型2モード手順の主張範囲.*?(?=\n## 3\.2 )",
    r"""## 3.1 Q1 W型2モード手順の主張範囲

物理的な導出の主線は、M37の実振動子運動から弱結合W型の最低2正常モードを経て、M54のW2信号とR140制御へ進む。R187がこの有限時間接続を与える。準備、結果形成、記録は別部分系として接続する。

Q1の1段測定は次の最小手順で行う。

1. R181Aで2モード信号方向を準備する。
2. R140/R143の分析器で測定軸の固有方向を左右射影成分へ写す。
3. 共通射影作用保持機構で $J_+,J_-$ を保持する。
4. R191を有限時間走らせ、結果 $r\in\{+,-,\varnothing\}$ を吸収記録へ固定する。
5. 安全な結果ではR181Dのprojector routerで $(P_rZ,(I-P_r)Z)$ を分け、非規格化 $P_rZ$ を次のR140区間へ直接渡す。
6. R143またはR112が必要な外部記録を作る。

固定有限深さでは、次段R191が残った作用和を分母として条件付き確率を読むので、選択branchを物理的に規格化し直さない。R144の同軸・異軸逐次分布はこのbranch受渡しを有限回合成する。R189CのZeno証人では中間R189Aが保持した2作用をR191へ渡し、中間記録や振幅再調整を挟まず走行中信号へbranchを返す。

W型ポテンシャル中の粒子位置は信号系の物理実装・空間診断として現れるが、Q1のBorn結果を粒子位置の再平衡化で生成する因果鎖は使わない。Q3の実在粒子位置はR164--R161/R162の別経路で扱う。従ってQ1測定の誤差台帳へR164、R190、R170の選択誤差を加えない。
""",
    "Q1 section 3.1",
)
write(q1_path, q1)

# Minimal cleanup in Q1 proof appendix: remove old-selection wording without
# rewriting the independent R140/R143/Zeno proofs.
a2_path = SECTIONS / "A2_m47_controlled_w_instrument_proofs.md"
a2 = read(a2_path)
a2 = a2.replace("R181Aと初期R170、R140分析器", "R181AとR140分析器")
a2 = a2.replace("固定済み容量入力R170系", "R191読出し")
a2 = a2.replace("R164/R190/R179/R170", "R191")
a2 = a2.replace("R164/R190/R170", "R191")
write(a2_path, a2)

# ---------------------------------------------------------------------------
# Q2-2: replace paired-Hopf branch re-preparation by sequential two-end R191.
# Keep result IDs R180A and R180C; remove R180B from the active paper.
# ---------------------------------------------------------------------------
write(
    q22_old_path,
    r"""@number: 5
@chapter: 本文
@title: M54駆動設定先行2端R191受信機構とBell前提監査
@status: 固定一重項4モード信号をA設定で分解し、A端R191の結果branchをprojector routerでB端へ直接渡し、B設定後のB端R191と組み合わせる。R180A/R180Cの責務をこの最小2端構成へ縮約し、旧R180B paired-Hopf再準備は退役する。

## 5.1 目的と模型の境界

Q2-2は、固定一重項、固定有限設定族、準備先行、非空間分離の古典装置として、二つの物理的な2値読出し端から量子一重項と同じ共同入出力統計を作ることを目標とする。空間分離Bell局所模型または自由設定loophole-free実験の古典説明は主張しない。

M54の実際の1試行末端信号を

```math
Z\in\mathbb C^4,
\qquad
Z\neq0
```

とする。解析上の規格化 $V=Z/\|Z\|$ は確率式を短く書くためだけに使い、物理制御器は状態依存除算を行わない。

## 5.2 固定一重項源と試行順序

固定ベンチマークではR181B/R181Cにより

```math
|00\rangle
\longrightarrow
\frac{|01\rangle-|10\rangle}{\sqrt2}
```

に対応する4モード信号を設定生成前に準備する。1周期の順序は次とする。

1. M54で固定一重項型末端信号 $Z$ を作る。
2. 設定生成器から $x,y$ を得る。
3. A側basis gate $U_x^\dagger\otimes I$ を同じ4モード信号へ作用する。
4. A結果射影作用 $J_{A,\pm}$ を保持し、A端R191を走らせて $r$ を固定・記録する。
5. R181Dと同じprojector routerで非規格化branch $P_{A,r}^{x}Z$ をB端へ渡す。
6. B端で $I\otimes U_y^\dagger$ を作用し、B結果射影作用を保持する。
7. B端R191を走らせて $s$ を固定・記録する。
8. 外部記録を残し、必要な能動部をR179のopen resetへ渡す。

A端とB端は別々のBrownian macrospin、mixing/decision浴、吸収記録を持つ。branchの物理転送があるため本装置は非空間分離である。

## 5.3 R180A：設定先行A端branch抽出

A設定 $x$ の固有基底を $u_{r,x}$、射影を

```math
P_{A,r}^{x}
=|u_{r,x}\rangle\langle u_{r,x}|\otimes I
```

とする。A端作用は

```math
J_{A,r}
=\mathcal J_0Z^\dagger P_{A,r}^{x}Z.
```

<!-- theorem-start:theorem -->
**定理（R180A：M54末端信号の設定先行条件付きブロック抽出定理）**

M54末端信号 $Z$ にA設定basis gateを作用し、直交射影子作用保持機構で $J_{A,+},J_{A,-}$ を保持してR191へ渡す。R191の結果を $r$ とし、その吸収記録で共通projector routerを制御する。理想極限では

```math
P(r\mid Z,x)
=\frac{J_{A,r}}{J_{A,+}+J_{A,-}}
=\frac{\|P_{A,r}^{x}Z\|^2}{\|Z\|^2},
```

かつB端へ渡る能動信号は非規格化branch

```math
Z_r=P_{A,r}^{x}Z
```

である。物理的な $Z_r/\|Z_r\|$ の生成を必要としない。作用保持、R191、routerの有限誤差は完全結果集合上で各1回だけ数える。
<!-- theorem-end:theorem -->

## 5.4 B端条件付き読出し

B設定 $y$ の射影を

```math
P_{B,s}^{y}
=I\otimes|u_{s,y}\rangle\langle u_{s,y}|
```

とする。A結果 $r$ 後のB端R191入力は

```math
J_{B,s\mid r}
=\mathcal J_0\|P_{B,s}^{y}P_{A,r}^{x}Z\|^2,
```

```math
S_r
=\mathcal J_0\|P_{A,r}^{x}Z\|^2.
```

従ってR191の逐次受渡し則から

```math
P(s\mid r,x,y)
=
\frac{\|P_{B,s}^{y}P_{A,r}^{x}Z\|^2}{\|P_{A,r}^{x}Z\|^2}.
```

A端の確率と掛けると分母がtelescopingし、

```math
P(r,s\mid x,y)
=
\frac{\|P_{B,s}^{y}P_{A,r}^{x}Z\|^2}{\|Z\|^2}.
```

## 5.5 R180C：2端合成とBell監査

<!-- theorem-start:theorem -->
**定理（R180C：M54駆動2端受信機構合成、有限誤差、局所性監査、帰還）**

R180AのA端作用保持・R191・projector router、B設定gate、B端作用保持・R191、二つの局所記録、および反復時のR179 open resetが同じ有限時計割当と安全集合上で実行できるとする。理想極限の完全結果共同分布は

```math
P(r,s\mid x,y)
=
\frac{\|P_{B,s}^{y}P_{A,r}^{x}Z\|^2}{\|Z\|^2}.
```

固定一重項型 $Z$ では

```math
P(r,s\mid x,y)
=
\frac14\left(1-rs\,\boldsymbol a_x\cdot\boldsymbol b_y\right),
```

```math
E(x,y)
=-\boldsymbol a_x\cdot\boldsymbol b_y.
```

従って標準CHSH設定で $|S|=2\sqrt2$ を得る。各翼の周辺は $1/2$ であり、理想共同分布は非信号性を満たす。

有限実装では、上流保持・basis gate、A端R191、router、B端basis gate、B端R191、記録の完全結果誤差を各1回加えた量を $\varepsilon_{180}$ とする。実共同分布は理想共同分布から全変動距離 $\varepsilon_{180}$ 以内にあり、周辺差とCHSH差はこの全変動誤差から従う標準安定性上界で抑えられる。

A端結果branchがB端へ物理的に渡るため、切断後局所factorizationやBell局所性は仮定しない。設定前の一重項源は $x,y$ に依存しないが、B端へ到達する内部状態はA設定とA結果に依存する。本結果は測定設定独立性・Bell局所性の前提監査を明示し、空間分離局所模型を主張しない。
<!-- theorem-end:theorem -->

## 5.6 責務境界

R180Bのpaired-Hopf再準備、中央潜在結果を2翼へ複製する工程、切断後のA側再読出しは現行必須主線に使わない。これらは `notes/superseded_q2_2_paired_hopf_receiver.md` と退役付録へ保存する。

Q2-2で新たに使う確率源はない。A端・B端とも共通R191を用い、共同確率はR191 T.8の逐次Lüders telescopingから得る。固定目標、条件付き達成ラベル、自由設定・空間分離を非主張とする境界は変更しない。
""",
)

write(
    SECTIONS / "A4_m54_receiver_cycle_proofs.md",
    r"""@number: D
@chapter: 付録
@title: M54駆動設定先行2端R191受信機構の証明
@status: R180AのA端branch抽出、R191逐次受渡し、共同Born分布、非信号性、CHSH値、有限全変動誤差、Bell前提監査を証明する。旧R180B paired-Hopf再準備は退役メモへ保存する。

## D.1 R180A

<!-- theorem-start:proof -->
**証明（R180A）**

$P_{A,+}^{x}+P_{A,-}^{x}=I$ なので

```math
J_{A,+}+J_{A,-}
=\mathcal J_0\|Z\|^2.
```

R191の理想2結果則を適用すると

```math
P(r\mid Z,x)
=\frac{\|P_{A,r}^{x}Z\|^2}{\|Z\|^2}.
```

結果固定後、共通対合router $F_{A,r}$ は未使用作業領域に対して

```math
F_{A,r}(Z,0)
=
(P_{A,r}^{x}Z,(I-P_{A,r}^{x})Z)
```

と作用する。従ってB端へ渡すbranchは $P_{A,r}^{x}Z$ であり、状態依存規格化を物理操作として行わない。
<!-- theorem-end:proof -->

## D.2 逐次共同分布

B端の理想条件付き確率は

```math
P(s\mid r,x,y)
=
\frac{\|P_{B,s}^{y}P_{A,r}^{x}Z\|^2}{\|P_{A,r}^{x}Z\|^2}.
```

従って

```math
P(r,s\mid x,y)
=P(r\mid x)P(s\mid r,x,y)
=
\frac{\|P_{B,s}^{y}P_{A,r}^{x}Z\|^2}{\|Z\|^2}.
```

これは付録Tの有限段Lüders telescopingの深さ2特殊化である。局所射影は異なるtensor因子へ作用するため可換であり、測定順序による理想共同分布の変更はない。

## D.3 一重項、非信号性、CHSH

固定一重項型信号ではPauli方向 $\boldsymbol a_x,\boldsymbol b_y$ に対し

```math
P(r,s\mid x,y)
=
\frac14\left(1-rs\,\boldsymbol a_x\cdot\boldsymbol b_y\right).
```

$s$ または$r$ を和すれば両周辺は $1/2$ であり、理想共同分布は非信号性を満たす。相関は

```math
E(x,y)
=-\boldsymbol a_x\cdot\boldsymbol b_y
```

であり、標準の4方向を取れば

```math
|S_{\rm CHSH}|=2\sqrt2.
```

これは非空間分離の共同装置の入出力統計であり、Bell局所factorizationから導いたものではない。

## D.4 有限誤差

A端保持・basis gate誤差を $\varepsilon_A^{\rm pre}$、A端R191を $\varepsilon_{191}^{A}$、routerを $\varepsilon_{\rm route}$、B端basis gateを $\varepsilon_B^{\rm basis}$、B端R191を $\varepsilon_{191}^{B}$、記録を $\varepsilon_{\rm rec}$ とする。同じ偏差を重複計上しなければkernel telescopingから

```math
\varepsilon_{180}
\leq
\varepsilon_A^{\rm pre}
+\varepsilon_{191}^{A}
+\varepsilon_{\rm route}
+\varepsilon_B^{\rm basis}
+\varepsilon_{191}^{B}
+\varepsilon_{\rm rec}.
```

完全結果分布の全変動距離が $\varepsilon_{180}$ 以下なら、任意の周辺事象の確率差も同じ上界以下である。また $rs\in[-1,1]$ なので各相関の差は $2\varepsilon_{180}$ 以下、4項CHSHの差は $8\varepsilon_{180}$ 以下である。

<!-- theorem-start:proof -->
**証明（R180C）**

D.1のA端R191とrouter、D.2の条件付きB端R191を合成すると理想共同分布を得る。有限実装では各段をMarkov kernelとして同じ完全結果集合へ埋め込み、kernelの全変動距離の三角不等式を順に適用すれば上の $\varepsilon_{180}$ が得られる。非信号性、CHSH安定性はD.3と有界観測量の全変動安定性から従う。A結果branchがB端へ転送されるため、切断後局所性は結論にも仮定にも含めない。
<!-- theorem-end:proof -->
""",
)

# ---------------------------------------------------------------------------
# Error/resource chapter: remove the legacy R170 section and replace Q2-2
# accounting. Preserve unrelated Q3 and resource analysis.
# ---------------------------------------------------------------------------
err_path = SECTIONS / "08_errors_resources_open_targets.md"
err = read(err_path)
err = re.sub(
    r"@status: .*?\n",
    "@status: Q1/Q2のR191 2結果読出し、R181D projector router、Q2-2の2端逐次R191、Q3のR164--R161/R162経路、M37物理実装層を横断して誤差・資源・反証条件を整理する。\n",
    err,
    count=1,
)
err = err.replace("R164/R190/R170代替経路の同じ選択偏差を重複加算しない。", "旧作用殻経路の選択偏差を現行R191誤差へ重複加算しない。")
err = replace_regex(err, r"## 8\.3 共通R170選択・吸収指針変数誤差.*?(?=\n## 8\.4 )", "", "remove 8.3 R170")
err = err.replace("R164/R190/R170の作用殻型実現は代替経路として残し、R191主線の誤差へ重複加算しない。", "旧作用殻型実現の偏差は現行R191主線へ重複加算しない。")
q22_err = r"""## 8.6 Q2-2の誤差とBell監査

現行Q2-2はA端R191、projector router、B端R191の深さ2逐次instrumentである。完全結果誤差を

```math
\varepsilon_{180}
\leq
\varepsilon_A^{\rm pre}
+\varepsilon_{191}^{A}
+\varepsilon_{\rm route}
+\varepsilon_B^{\rm basis}
+\varepsilon_{191}^{B}
+\varepsilon_{\rm rec}
```

とする。R191内部のmixing、transducer、guard、finite-temperature retreat、finite-time noncapture、captureは各 $\varepsilon_{191}^{A,B}$ に1回だけ含める。旧R180Bの方向吸引誤差、中央結果複製誤差、切断後A側再読出し誤差は現行台帳から除く。

理想一重項共同分布との全変動距離が $\varepsilon_{180}$ 以下なら、各周辺事象の確率差は $\varepsilon_{180}$ 以下、各二値相関の差は $2\varepsilon_{180}$ 以下、CHSH値の差は $8\varepsilon_{180}$ 以下である。A結果branchをB端へ物理的に渡すため、Bell局所factorizationまたは空間分離を誤差ゼロ極限の主張へ追加しない。

"""
err = replace_regex(err, r"## 8\.6 Q2-2の誤差とBell監査.*?(?=\n## 8\.7 )", q22_err, "replace 8.6 Q2-2")
write(err_path, err)

# ---------------------------------------------------------------------------
# R191 appendix responsibility clean-up.
# ---------------------------------------------------------------------------
a20_path = SECTIONS / "A20_m54_brownian_macrospin_projective_instrument.md"
a20 = read(a20_path)
a20 = a20.replace(
    "@status: Q1/Q2の2結果射影読出しを、既知のブラウン巨視的スピンと吸引域捕獲へ接続する採用開放模型。R164--R190--R170経路は一般有限結果集合・作用殻型の代替実現として残す。",
    "@status: Q1/Q2の2結果射影読出しを、既知のブラウン巨視的スピンと吸引域捕獲へ接続する現行共通instrument。結果後の非規格化branch受渡しをR181Dへ接続する。",
)
a20 = a20.replace(
    "R190Bと同じ球面スペクトル分解を使い、",
    "球面調和関数のスペクトル分解を使い、",
)
a20 = a20.replace(
    "R191ではこの混合評価だけを共通化し、R190Cの作用開口やR161の静的平方根率を使わない。",
    "R191はこの混合評価を2結果instrument内部で直接使い、作用開口やR161の静的平方根率を経由しない。",
)
a20 = replace_regex(
    a20,
    r"## T\.9 Q2-2での責務.*?(?=\n## T\.10 )",
    r"""## T.9 Q2-2での責務

Q2-2では同じR191契約を二つの物理測定端へ使う。A設定後のA端R191結果 $r$ でprojector routerを制御し、非規格化branch $P_{A,r}^{x}Z$ をB端へ渡す。B設定後のB端R191は

```math
P(s\mid r,x,y)
=
\frac{\|P_{B,s}^{y}P_{A,r}^{x}Z\|^2}{\|P_{A,r}^{x}Z\|^2}
```

を生成する。従ってT.8のtelescopingにより共同分布は $\|P_{B,s}^{y}P_{A,r}^{x}Z\|^2/\|Z\|^2$ となる。中央4結果sampler、paired-Hopf再準備、A側の二重読出しを必要としない。

""",
    "A20 T.9",
)
a20 = a20.replace("2. R164/R190/R170の一般有限結果集合または作用殻実現の不要性。\n", "")
write(a20_path, a20)

# Q1 W-preparation appendix: only replace the obsolete readout sentence.
a8_path = SECTIONS / "A8_m47_hopf_preparation.md"
a8 = read(a8_path)
a8 = a8.replace(
    "粒子位置のBorn型分布と有限熱化・排他的選択固定はR164、R190、R179、R170が構成し、W型局所記録はR143、測定後状態の受け渡しはR181Dの深さ1特殊化が担う。信号浴の統計核だけから単一試行粒子位置または連続位置率を作る規則は使わない。",
    "Q1のBorn型2値結果は射影作用をR191へ直接渡して形成し、W型局所記録はR143、測定後branchの受け渡しはR181Dの深さ1特殊化が担う。Q3の単一試行粒子位置はR164--R161/R162の別経路で扱う。",
)
write(a8_path, a8)

# R179 appendix: narrow the status and legacy wording to reset/renewal only.
a17_path = SECTIONS / "A17_m54_uniform_supply.md"
a17 = read(a17_path)
a17 = re.sub(
    r"@status: .*?\n",
    "@status: R179のopen reset、定常流入浴、流出履歴排出、補助作業領域とR191指針変数の反復再初期化を整理する。\n",
    a17,
    count=1,
)
a17 = a17.replace("R190反復時の履歴条件付き再混合", "反復時の履歴排出と再初期化")
a17 = a17.replace("R190", "退役作用殻経路")
write(a17_path, a17)

# ---------------------------------------------------------------------------
# Conclusion: report only the present spine.
# ---------------------------------------------------------------------------
write(
    SECTIONS / "09_conclusion.md",
    r"""@number: 9
@chapter: 本文
@title: 結論
@status: M54/M37の現行階層、Q1/Q2のR191 2結果読出し、Q2-2の2端逐次R191、Q3のR164--R161/R162位置経路、R184--R185を総括する。

本稿は、古典実正準信号の線形力学と、1試行1結果を作る開放古典instrumentを分離して構成した。有限次元Hilbert空間とunitaryを古典振動子へ写すこと自体ではなく、その同じ単一試行信号からBorn型排他的結果と測定後branchを作る物理接続を中心課題とした。

Q1/Q2の2結果測定はR191へ統一した。二つの射影作用

```math
J_\pm=\mathcal J_0Z^\dagger P_\pm Z
```

の和と差をブラウン巨視的スピンの一軸異方性とbiasへ結合すると、理想吸引域測度から

```math
P(\pm)=\frac{J_\pm}{J_++J_-}
```

を得る。R191は有限混合時間、transducer誤差、guard、有限温度retreat、有限decision時間、端点dispatcher、無反応、吸収記録を同じ完全結果誤差へまとめる。

結果後の状態更新はR181Dの可逆projector routerへ縮約した。物理信号を規格化し直さず

```math
Z\longmapsto P_rZ
```

を次段へ渡すだけで、次のR191が残った作用和を分母として条件付きBorn重みを読む。有限段では確率積がtelescopingしてLüders型共同分布を回収する。一般深さQ2-4でbranch作用が読出し下限を下回る場合だけ振幅再調整を補助手段として残す。

Q1ではR187がM37弱結合W型最低2正常モードをW2制御信号へ接続し、R140がBloch球型可逆操作とRabi運動を与える。R143--R144は分析器・記録・逐次測定、R189A--R189Cは走行中作用保持と有限Rabi--Zeno比較を担う。Born結果形成をW型粒子位置の再平衡化へ依存させない。

Q2-1とQ2-3ではR181B/R181Cが永続多モード信号上のテンソル積状態とgate列を作り、末端R191/R181Dが出力を標本化する。Q2-4では同じ2結果nodeを一般回路出力へ逐次適用し、R179はopen resetと履歴排出、R186は外部運用資源とノイズ境界を監査する。

Q2-2では、固定一重項4モード信号にA設定を作用し、A端R191で $r$ を形成してbranch $P_{A,r}^{x}Z$ をB端へ渡し、B設定後のB端R191で $s$ を形成する。共同分布は

```math
P(r,s\mid x,y)
=
\frac{\|P_{B,s}^{y}P_{A,r}^{x}Z\|^2}{\|Z\|^2}
```

であり、一重項型信号では余弦共同相関、非信号性、CHSH/Tsirelson値を再現する。この装置はA結果branchをB端へ渡す非空間分離装置であり、Bell局所性を主張しない。

Q3は別の位置因果鎖を持つ。R164が開始面の実在粒子配置を準備し、R161が信号確率流と活動量から有向率を作り、R162が開放Poisson-jump過程として同じ粒子を輸送する。R185は同じ前向き経路法則のBayes反転から前進・後退平均微分と時間対称Newton則へ接続する。Q3の位置問題をQ1/Q2の測定pointerへ混ぜない。

今回の縮約により、R190A--R190Cの2作用LC殻Drude混合、R170静的吸収pointer、R180B paired-Hopf再準備は固定Q1/Q2の必須主線から外れた。これらは反証されたのではなく、別の物理実現・強化案として `notes/` とGit履歴へ保存する。現行論文では同じBorn結果を複数経路で重複導出しない。

残る主要な物理課題は、R191の作用和・作用差transducer、Brownian macrospin、projector router、外部record、R179 resetを同じ具体装置へ統合すること、M37信号系との接続を含む単一ミクロ装置M0を構成すること、Q2-4の外部多項式資源条件を物理配線・較正・noiseまで閉じること、Q3-6の位相量子化を閉じることである。
""",
)

# ---------------------------------------------------------------------------
# PROJECT_STATUS: keep fixed goals; update only current-model/current-result rows.
# ---------------------------------------------------------------------------
status_path = ROOT / "PROJECT_STATUS.md"
status = read(status_path)
status = replace_regex(
    status,
    r"## draft-88：R191ブラウン巨視的スピン2結果読出し.*?(?=\n\nこの文書は)",
    """## draft-89：R191測定主線の責務縮約

- Q1/Q2の2結果射影測定はR191を唯一の現行主読出しとする。
- R181Dはprojector routerと非規格化branch受渡しへ責務を縮約し、固定有限深さでは振幅再調整を必須にしない。
- R164はQ3開始配置、R179はopen reset/履歴排出へ責務を分離する。
- R190A--R190C、R170、R180B paired-Hopf受信機構は固定Q1/Q2の必須主線から退役し、notes/Git履歴へ保存する。
- Q2-2はA端R191からB端R191へbranchを渡す非空間分離2端装置へ縮約する。
- 固定長期目標と達成ラベルは変更しない。""",
    "PROJECT_STATUS draft block",
)
lines = status.splitlines()
new_lines: list[str] = []
for line in lines:
    if line.startswith("| M54 | 共通有効信号--配置状態構成族 |"):
        line = "| M54 | 共通有効信号--配置状態構成族 | 現行Q1・Q2・Q3の共通有効層 | Q1/Q2ではR191 2結果読出しとR181D router、Q3ではR164開始配置とR161/R162輸送を使う。R181A--R181Cは準備・持ち上げ・gate、R179は反復時open resetを担う。全状態構成の単一装置統合を意味しない |"
    elif line.startswith("| Q2-2 | 条件付き達成 |"):
        line = "| Q2-2 | 条件付き達成 | M54静的状態構成 | 永続4モード記憶部とA/B二つの物理R191読出し端 | A設定gate、A端R191、projector router、B設定gate、B端R191 | R112、R180A、R180C、R191 | 固定一重項・固定有限設定族・非空間分離の範囲。transducer、2つのmacrospin、router、記録、resetの単一装置統合が残る。自由設定・空間分離は未達 |"
    elif line.startswith("| Q2-4 | 条件付き達成 |"):
        line = "| Q2-4 | 条件付き達成 | M54一般静的状態構成 | $2^n$ 受動直接モード記憶部＋一様開放浴 interface | 一般gate列、R191逐次読出し、R181D router、必要時repump、R179 open reset | R112、R179、R181A、R181B、R181C、R181D、R186、R191 | 静的配線、R191 transducer、router、必要な作用下限回復、open resetを一つの一様装置族へ接続し、R186の多項式精度条件を満たすこと |"
    new_lines.append(line)
status = "\n".join(new_lines) + "\n"
status = status.replace("R164/R190/R170は削除せず、一般有限結果集合、作用殻型の明示実現、Q3固定時刻診断などの代替・強化経路へ残す。\n", "R164はQ3開始配置へ残し、旧作用殻型測定経路はnotesへ退役する。\n")
write(status_path, status)

# README: replace the migration banner only; fixed-goal tables remain.
readme_path = ROOT / "README.md"
readme = read(readme_path)
readme = re.sub(
    r"> \*\*draft-88:\*\*.*?\n\n",
    "> **draft-89:** Q1/Q2の2結果測定をR191へ一本化し、R181Dをprojector routerへ縮約した。R190/R170とQ2-2のpaired-Hopf再準備は現行主線から退役し、Q3位置経路はR164--R161/R162へ分離した。退役内容は `notes/` とGit履歴から参照できる。\n\n",
    readme,
    count=1,
    flags=re.S,
)
write(readme_path, readme)

# ---------------------------------------------------------------------------
# Retired-result index and history docs.
# ---------------------------------------------------------------------------
index_path = NOTES / "superseded_result_index.md"
index = read(index_path)
append_block = """

## draft-89で退役した測定経路

| 結果・模型 | 旧責務 | 現行置換 | 保存先 |
|---|---|---|---|
| R190A--R190C | 2作用LC殻Drude混合と静的平方根選択 | Q1/Q2の2結果はR191が直接読出し | `superseded_r190_r170_measurement_path.md`, `superseded_A19_drude_action_shell_bridge.md` |
| R170 | 静的選択結果の吸収pointer固定 | R191のBrownian macrospin吸収記録 | `superseded_r190_r170_measurement_path.md` |
| R180B | 選択branchから2翼テンプレートをpaired-Hopfで再準備 | A端R191の非規格化branchをrouterでB端へ直接受渡し | `superseded_q2_2_paired_hopf_receiver.md`, `superseded_A9_paired_hopf_receiver.md` |

これらは反証ではなく責務縮約による退役である。固定Q1/Q2の誤差予算と必須依存には含めない。
"""
if "## draft-89で退役した測定経路" not in index:
    index += append_block
write(index_path, index)

for path, block in (
    (ROOT / "CHANGELOG.md", """\n## draft-89：R191測定主線の圧縮\n\n- 新定理を追加せず、Q1/Q2の2結果測定をR191へ一本化した。\n- R181Dをprojector routerと非規格化branch受渡しへ責務縮約した。\n- R190A--R190C、R170を固定Q1/Q2主線から退役し、旧定理本文とA19をnotesへ保存した。\n- Q2-2からR180B paired-Hopf再準備を外し、A端R191→router→B端R191の2端逐次instrumentへ縮約した。旧章・A9・検算器はnotesへ保存した。\n- R164はQ3開始配置、R179はopen reset/履歴排出へ責務を分離した。固定目標と達成ラベルは変更しない。\n"""),
    (ROOT / "MANIFEST.md", """\n## draft-89のR191測定主線圧縮\n\n- `sections/A9_m54_setting_pre_paired_hopf_receiver.md` と `sections/A19_m54_drude_action_shell_bridge.md` を現行論文から外し、notesへ退役保存。\n- Q1/Q2本文をR191主線へ同期し、Q2-2をA端R191→router→B端R191へ縮約。\n- 退役検算器は `notes/retired_verifiers/` へ保存。\n- `paper.md`、`main.tex`、`paper.pdf` は章別原稿から再生成する。\n"""),
    (ROOT / "VALIDATION.md", """\n## draft-89：R191測定主線圧縮の検算\n\n- R191の既存 `tools/verify_r191_macrospin.py` をBorn吸引域、有限温度、端点dispatcher、Lüders telescopingの正本検算として維持する。\n- Q2-2の現行検算は `tools/verify_r180_m54_receiver.py` でA端Born重み、非規格化branch、B条件付き重み、共同分布、非信号性、CHSH値を確認する。\n- 旧R190 Drude殻、R170 static instrument、R180B paired-Hopfの専用検算器は `notes/retired_verifiers/` へ移し、現行 `run_physics_checks.py` の対象から外す。\n- 固定目標・達成ラベルは変更せず、全 `verify_*.py`、source check、terminology check、論文再生成、生成物同期を要求する。\n"""),
):
    text = read(path)
    marker = block.strip().splitlines()[0]
    if marker not in text:
        text += block
    write(path, text)

# ---------------------------------------------------------------------------
# Replace the current R180 verifier with the simpler two-end sequential chain.
# ---------------------------------------------------------------------------
write(
    TOOLS / "verify_r180_m54_receiver.py",
    r'''#!/usr/bin/env python3
from __future__ import annotations

import math
import numpy as np


def projector(axis: np.ndarray, sign: int) -> np.ndarray:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    sigma = axis[0] * sx + axis[1] * sy + axis[2] * sz
    return (np.eye(2) + sign * sigma) / 2


singlet = np.array([0, 1, -1, 0], dtype=complex) / math.sqrt(2)
settings_a = [np.array([0.0, 0.0, 1.0]), np.array([1.0, 0.0, 0.0])]
settings_b = [
    np.array([1.0, 0.0, 1.0]) / math.sqrt(2),
    np.array([-1.0, 0.0, 1.0]) / math.sqrt(2),
]

corr = np.zeros((2, 2))
for ix, a in enumerate(settings_a):
    for iy, b in enumerate(settings_b):
        probs: dict[tuple[int, int], float] = {}
        for r in (-1, 1):
            pa = np.kron(projector(a, r), np.eye(2))
            branch = pa @ singlet
            p_r = float(np.vdot(branch, branch).real)
            assert p_r > 0
            cond_sum = 0.0
            for s in (-1, 1):
                pb = np.kron(np.eye(2), projector(b, s))
                joint_action = float(np.vdot(pb @ branch, pb @ branch).real)
                p_cond = joint_action / p_r
                probs[(r, s)] = p_r * p_cond
                cond_sum += p_cond
            assert abs(cond_sum - 1.0) < 2e-12
        assert abs(sum(probs.values()) - 1.0) < 2e-12
        marg_a = {r: sum(probs[(r, s)] for s in (-1, 1)) for r in (-1, 1)}
        marg_b = {s: sum(probs[(r, s)] for r in (-1, 1)) for s in (-1, 1)}
        assert max(abs(v - 0.5) for v in marg_a.values()) < 2e-12
        assert max(abs(v - 0.5) for v in marg_b.values()) < 2e-12
        corr[ix, iy] = sum(r * s * probs[(r, s)] for r in (-1, 1) for s in (-1, 1))
        assert abs(corr[ix, iy] + float(a @ b)) < 2e-12

chsh = corr[0, 0] + corr[0, 1] + corr[1, 0] - corr[1, 1]
assert abs(abs(chsh) - 2 * math.sqrt(2)) < 2e-12
print("R180 sequential two-end R191 checks passed")
''',
)

# ---------------------------------------------------------------------------
# Remove migration-era wording in docs that would make the old path look live.
# ---------------------------------------------------------------------------
for path in (ROOT / "PROJECT_GUIDE.md", ROOT / "PROJECT_STANCE.md"):
    if path.exists():
        text = read(path)
        text = text.replace("R164/R190/R179/R170", "旧作用殻型測定経路")
        write(path, text)

# Drop temporary transformation source from the final tree. The workflow file
# deletes itself separately after running this script.
print("r191_simplification_applied")
