from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def path(name: str) -> Path:
    return ROOT / name


def read(name: str) -> str:
    return path(name).read_text(encoding="utf-8")


def write(name: str, text: str) -> None:
    path(name).write_text(text, encoding="utf-8")


def rep(name: str, old: str, new: str, count: int = 1) -> None:
    text = read(name)
    found = text.count(old)
    if found != count:
        raise SystemExit(f"{name}: expected {count} occurrence(s), found {found}: {old[:120]!r}")
    write(name, text.replace(old, new, count))


def sub(name: str, pattern: str, repl: str, count: int = 1, flags: int = 0) -> None:
    text = read(name)
    out, n = re.subn(pattern, repl, text, count=count, flags=flags)
    if n != count:
        raise SystemExit(f"{name}: expected {count} regex replacement(s), found {n}: {pattern[:120]!r}")
    write(name, out)


def prepend(name: str, block: str) -> None:
    text = read(name)
    if block.strip() in text:
        raise SystemExit(f"{name}: block already present")
    write(name, block.rstrip() + "\n\n" + text)


# ---------------------------------------------------------------------------
# Canonical enhancement-target document.
# ---------------------------------------------------------------------------
write(
    "ENHANCEMENT_TARGETS.md",
    r'''# 固定目標に付随する強化目標

本ファイルは `PROJECT_STATUS.md` に定める固定目標へ付随する強化目標の正本を管理する。固定目標そのものの定義と達成判定は `PROJECT_STATUS.md` を正本とし、本ファイルの強化目標はそれらへ追加の物理実装・数値再現・回路実装を要求する独立の評価軸とする。

強化目標は固定目標そのものとは独立に判定する。強化目標が未達であることを理由として、固定目標の既存の達成・条件付き達成・未達ラベルを変更しない。また、固定目標の達成だけから対応する強化目標の達成を自動的に認定しない。

強化目標の状態は `未監査`、`未達`、`部分達成`、`達成` の4段階で管理する。既存結果が新しい強化基準を満たす可能性があっても、新基準による監査を行うまでは `未監査` とする。

## 強化目標A：具体的古典物理模型と直接数値再現

全ての固定目標 Q1-1--Q3-6 に対し、次の2項目を追加する。

| ID末尾 | 強化目標 | 達成条件 |
|---|---|---|
| A1 | 明示的な古典ミクロ模型 | 対応する固定目標に必要な主要因果鎖を、実在古典自由度、運動方程式またはHamiltonian、相互作用、浴または雑音機構、準備条件、外部制御、読出し量、物理パラメータまで含む1つの具体的物理模型として接続する。Hamiltonian無限浴を用いてよい。また、Langevin方程式、LLG-Langevin方程式その他の古典確率微分方程式を採用開放ミクロ方程式として直接採用してよく、Itô/Stratonovich規約、平均、共分散を明示するなら理想白色雑音も許す。有限閉鎖Hamiltonian全系への持上げは要求しない |
| A2 | ミクロ模型の直接数値再現 | A1で採用したミクロ方程式そのものを数値的に発展または標本化し、固定目標で要求する主要観測量・統計・時間発展を再現する。採用開放SDEならそのSDEを直接標本化する。Hamiltonian無限浴または連続浴なら、有限帯域・有限モード切断を直接計算し、対象時間窓で切断依存性または収束性を示してよい。有効Schrödinger方程式、Born則、目標Markov生成子など導出後の有効模型だけを数値計算することでは代替しない |

A1でいう「ミクロ模型」は、単に目的の確率分布、Born重み、Bell共同確率、Schrödinger生成子、または目標出力分布を遷移率や外部入力として直接与えるものではない。目的の挙動を生じさせる下位の古典自由度とその力学を提示することを要求する。複数の固定目標で同じ物理模型を共有してよいが、各A1ではその固定目標に必要な因果鎖が同じ具体模型内で閉じていることを示す。

採用開放模型では、白色雑音をHamiltonian無限浴から再導出することをA1の必須条件としない。ただし、その方程式をHamiltonian浴から導出したと主張する場合は、浴、結合、縮約条件と誤差を別途示す。理想白色雑音を採用した場合も、物理回路実装Bでは有限帯域の雑音源へ落とす。

A2では、確率模型について十分な標本数による経験分布と理論分布を比較し、決定論的模型について主要観測量の有限時間軌道を比較する。可能な場合は、時間刻み、系サイズ、浴切断、雑音相関時間、結合強度その他の近似パラメータに対する収束性または誤差依存性も報告する。

Q2-4のように任意規模を対象とする固定目標では、全ての $n,d$ を直接数値計算することは要求しない。複数の有限規模で代表的な回路族を直接計算し、外部時間、精度、ノイズ感度、制御量その他の固定目標で要求する資源量について規模依存性を検査する。

## 強化目標B：Q1/Q2アナログ回路実装

Q1-1、Q1-2、Q2-1、Q2-2、Q2-3、Q2-4について、さらに次の3項目を追加する。

LC共振器だけに限定せず、LC/RLC回路、結合共振器、伝送線、非線形回路素子、増幅器、比較器、スイッチ、古典雑音源、制御回路その他の古典アナログ素子を使用してよい。ただし、抽象的な正準変数の対応表だけでなく、実際の回路方程式へ落とせる具体的装置を要求する。

| ID末尾 | 強化目標 | 達成条件 |
|---|---|---|
| B1 | 具体的アナログ回路 | 対応する固定目標を実現する具体的回路構成を提示し、主要素子、接続、状態変数、制御入力、読出し点と、理論模型中の自由度との対応を明示する。必要に応じて回路図、ネットリストまたは同等の回路方程式を与える |
| B2 | 実験可能パラメータ領域 | 固定目標に必要な近似、時間尺度分離、結合、SNR、読出し、リセット等が同時に成立する非空な物理パラメータ領域を示す。代表値1点だけでなく、少なくとも主要パラメータについて許容範囲または設計余裕を示す。A1で理想白色雑音を用いる場合は、有限帯域雑音の相関時間が系の遅い時間尺度より十分短い領域を含める |
| B3 | 回路の直接数値再現 | B1の具体回路をSPICE、回路ODE/SDE、伝送線模型または同等の回路シミュレーションで直接計算し、対応する固定目標の挙動を再現する。有限Q、熱雑音、有限帯域雑音、素子公差、寄生成分などを段階的に導入して成立範囲を評価する。A1の白色雑音近似を使う場合は、必要に応じて雑音帯域を増やした極限との整合も確認する |

B2では、対象回路に応じて少なくとも共振周波数、帯域、Q値、結合係数、電圧・電流または作用尺度、雑音強度、素子公差、制御時間、読出し時間、SNRのうち重要なものを明示する。

Q2-4のB1--B3は単一の巨大回路図を要求するものではなく、任意規模 $n$ に対して一様な有限規則から生成できる回路族を要求する。B3では有限規模の直接回路シミュレーションと規模依存性の監査を組み合わせる。

## 強化目標の適用表

| 固定目標 | A1 ミクロ模型 | A2 ミクロ数値 | B1 回路 | B2 実験領域 | B3 回路数値 | 固有強化 |
|---|---:|---:|---:|---:|---:|---|
| Q1-1 | 対象 | 対象 | 対象 | 対象 | 対象 | — |
| Q1-2 | 対象 | 対象 | 対象 | 対象 | 対象 | — |
| Q2-1 | 対象 | 対象 | 対象 | 対象 | 対象 | — |
| Q2-2 | 対象 | 対象 | 対象 | 対象 | 対象 | Q2-2-S |
| Q2-3 | 対象 | 対象 | 対象 | 対象 | 対象 | — |
| Q2-4 | 対象 | 対象 | 対象 | 対象 | 対象 | — |
| Q3-1 | 対象 | 対象 | — | — | — | — |
| Q3-2 | 対象 | 対象 | — | — | — | — |
| Q3-3A | 対象 | 対象 | — | — | — | — |
| Q3-3B | 対象 | 対象 | — | — | — | — |
| Q3-3C | 対象 | 対象 | — | — | — | — |
| Q3-4A | 対象 | 対象 | — | — | — | — |
| Q3-4B | 対象 | 対象 | — | — | — | — |
| Q3-5 | 対象 | 対象 | — | — | — | — |
| Q3-6 | 対象 | 対象 | — | — | — | — |

各個別目標は、例えば `Q1-2-A1`、`Q1-2-A2`、`Q1-2-B1` のように固定目標IDへ末尾を付けて参照する。

## Q2-2-S：空間隔離強化

Q2-2本体は、Bell型共同統計を古典構成で再現し、その構成についてBell不等式の導出に用いられる前提の成立・不成立を監査することを要求する。どのBell前提を破るかは固定目標側で指定しない。`Q2-2-S` はその上で、A端とB端の空間的・因果的隔離をどこまで強めてもBell型共同統計を維持できるかを独立に調べる。

この強化はBellの定理を回避または否定することを目的としない。各段階で、物理的因果構造と確率因子化を明示し、どの前提が成立し、どの前提が成立しないかを構成から判定する。

| 段階 | 条件 | 検証内容 |
|---|---|---|
| S0 | 現行の非空間分離構成 | A端の結果成分をB端へ物理的に渡す現行逐次装置を基準系とする。現行証人では測定窓中のA→B因果伝播を用いる |
| S1 | 物理的2端化 | A端とB端を実際に異なる場所へ配置し、中央準備部、配線、伝送距離、伝送遅延を明示する。測定窓中の端間通信はまだ許してよい |
| S2 | 測定窓内の因果隔離 | 各端の設定確定から局所結果固定まで、他端から到達可能な信号を利用しない構成を示す。端間距離を $L$、最大伝播速度を $v_{\max}$、設定確定時刻を $t_A^{\rm set},t_B^{\rm set}$、結果固定時刻を $t_A^{\rm out},t_B^{\rm out}$ として、少なくとも $t_A^{\rm out}-t_B^{\rm set}<L/v_{\max}$ および $t_B^{\rm out}-t_A^{\rm set}<L/v_{\max}$ を要求する。同期設定では $v_{\max}T_{\rm meas}<L$ が十分条件となる |
| S3 | 因果隔離下のBell型統計と前提監査 | S2を維持したままBell型共同統計をどこまで再現できるかを構成し、成立した模型についてBell不等式導出に必要な前提を中立的に監査する。特定のloophole、共通原因、設定依存性を先に要求しない |
| S4 | Bell局所CHSH対照系 | Bell局所CHSH境界を導く十分な前提集合を明示的に課した対照系を構成し、$|S|\le2$ へ戻ることを確認する。S4でCHSH破れを維持すること自体は強化目標の達成条件としない |

S3では少なくとも、測定設定独立性、Bell局所因子化

```math
P(a,b\mid x,y,\lambda)
=
P(a\mid x,\lambda)P(b\mid y,\lambda),
```

測定窓中の端間通信、無反応・棄却を含む標本選択、非信号性を監査する。必要に応じてBell局所因子化をparameter independenceとoutcome independenceへ分解してよい。設定と内部状態の依存性が現れる場合は、相互情報量 $I(\Lambda;X,Y)$、全変動距離その他の指標でその大きさを定量化してよいが、測定設定独立性の破れそのものをS3の必須条件にはしない。

Q2-2-Sの主要な到達目標は、Bell型共同統計を維持したままS2またはS3まで物理的隔離を進められるかを判定することである。どの段階で不可能になるか、またはどのBell前提の不成立が避けられないかが判明した場合、その否定的結果自体を有効な成果として記録する。

## 強化目標の現在地表

強化目標の追加時点では、既存結果を新基準へ自動的に読み替えず、以下の形式で独立に監査する。全項目を `未監査` から開始する。

| 固定目標 | A1 | A2 | B1 | B2 | B3 | 固有強化 | 主な既存候補 |
|---|---|---|---|---|---|---|---|
| Q1-1 | 未監査 | 未監査 | 未監査 | 未監査 | 未監査 | — | M37、R140、R187 |
| Q1-2 | 未監査 | 未監査 | 未監査 | 未監査 | 未監査 | — | R189A--R189C、R193、R191、R181D |
| Q2-1 | 未監査 | 未監査 | 未監査 | 未監査 | 未監査 | — | M54、R181B--R181D、R191 |
| Q2-2 | 未監査 | 未監査 | 未監査 | 未監査 | 未監査 | 未監査 | R180A、R180C、R191 |
| Q2-3 | 未監査 | 未監査 | 未監査 | 未監査 | 未監査 | — | M54、R177、R181B--R181D、R191 |
| Q2-4 | 未監査 | 未監査 | 未監査 | 未監査 | 未監査 | — | M54、R179、R181C--R181D、R186、R191、R192 |
| Q3-1 | 未監査 | 未監査 | — | — | — | — | M37、R86 |
| Q3-2 | 未監査 | 未監査 | — | — | — | — | M57、R195A--R195D、R161、R185 |
| Q3-3A | 未監査 | 未監査 | — | — | — | — | M37、R123 |
| Q3-3B | 未監査 | 未監査 | — | — | — | — | M37、R123 |
| Q3-3C | 未監査 | 未監査 | — | — | — | — | M37、R123、R182 |
| Q3-4A | 未監査 | 未監査 | — | — | — | — | M37、M57、R124、R195D |
| Q3-4B | 未監査 | 未監査 | — | — | — | — | M37、M57、R182、R195D |
| Q3-5 | 未監査 | 未監査 | — | — | — | — | M37、M57、R125、R195D |
| Q3-6 | 未監査 | 未監査 | — | — | — | — | 完結候補なし |

ここで「主な既存候補」は強化目標の達成を意味せず、新基準を監査するときの出発点だけを示す。

## 既存の実装強化課題との関係

固定目標そのものの達成条件と、物理実装・数値実験・回路実験へ進む強化目標を区別する。

全固定目標について、具体的古典ミクロ模型 `A1` と、そのミクロ方程式を直接計算する数値再現 `A2` を強化目標とする。Q1/Q2については、具体的アナログ回路 `B1`、実験可能パラメータ領域 `B2`、回路直接シミュレーション `B3` を追加する。Q2-2についてはさらに、2つの測定端の物理的・因果的隔離とBell前提の境界を調べる `Q2-2-S` を置く。

これらは固定目標の既存達成ラベルを変更しない。逆に、既存の解析証明または有効模型の数値検証だけから強化目標を自動的に達成としない。

従来の強化課題であるQ1/Q2の完全周期収支、共通浴統合、M37信号源--M57 tracer--時計--終位置記録の単一反復周期統合、連続空間一様極限、多粒子拡張、有限閉鎖Hamiltonian化は引き続き保持する。これらはA/B/Sの横断的または上位の実装強化課題として管理する。

M0は、複数の固定目標にまたがる部品を1つのミクロ装置と共通反復周期へ統合する、A1より強い統合目標として区別する。各固定目標についてA1を達成することだけではM0達成としない。
'''
)


# ---------------------------------------------------------------------------
# PROJECT_STATUS: policy change, canonical link, and Bell audit interpretation.
# ---------------------------------------------------------------------------
prepend(
    "PROJECT_STATUS.md",
    """## draft-97：強化目標同期、Q2-2 Bell前提一般化、採用開放雑音模型の明確化

- Q2-2の固定目標から特定の「測定設定独立性の破れ」を必須条件として外し、Bell型共同統計を再現した古典構成についてBell不等式導出に用いられる前提の成立・不成立を物理的因果構造と確率因子化に対応させて監査する一般基準へ改める。Q2-2の条件付き達成ラベルは変更しない。
- `ENHANCEMENT_TARGETS.md` を固定目標に付随する強化目標A1/A2、Q1/Q2のB1/B2/B3、Q2-2-Sの正本として正式に接続し、全強化目標は未監査から開始する。
- A1ではHamiltonian無限浴に加え、Langevin型SDEなどの採用開放ミクロ方程式と理想白色雑音を許す。A2は採用したミクロODE/SDEそのものの直接数値再現を要求し、B2/B3では有限帯域雑音へ落として実験可能性を監査する。
- 固定目標のうちQ2-2以外の定義、全ての既存達成ラベル、現行結果IDは変更しない。"""
)

sub(
    "PROJECT_STATUS.md",
    r"^\| Q2-2 \| Bell 型測定統計 \|.*$",
    "| Q2-2 | Bell 型測定統計 | 二体系の共同内部状態を2つの物理的な測定端へ接続し、各端での操作・測定・記録から、余弦共同確率、CHSH 不等式の破れ、Tsirelson 限界、非信号性を整合的に導く。さらに、その古典構成についてBell不等式の導出に用いられる前提のうち、どれが成立し、どれが成立しないかを、物理的因果構造および確率因子化と対応させて明示する。特定のQ2-1実装からの受渡しはQ2-2単独の達成条件にしない。 |",
    flags=re.MULTILINE,
)

rep(
    "PROJECT_STATUS.md",
    "以下の目標ID、名称、意味、達成判定基準は通常の論文更新では変更しない。追加、削除、統合、分割または判定基準の変更は独立した方針変更として扱う。",
    "以下の目標ID、名称、意味、達成判定基準は通常の論文更新では変更しない。追加、削除、統合、分割または判定基準の変更は独立した方針変更として扱う。固定目標に付随するA1/A2、Q1/Q2のB1/B2/B3、Q2-2-Sの定義、適用範囲、現在地は `ENHANCEMENT_TARGETS.md` を正本とし、固定目標の達成状態とは独立に管理する。",
)

sub(
    "PROJECT_STATUS.md",
    r"^- R180CのCHSH不等式の破れは.*$",
    "- 現行R180CのCHSH不等式の破れは、設定前の一重項源を設定非依存に保ったままA端結果成分をB端へ物理的に渡す非空間分離逐次構成で得る。従って現行証人はBell局所因子化を満たす空間分離模型ではない。Q2-2固定目標は特定のBell前提違反を先に指定せず、採用構成ごとに前提の成立・不成立を監査する。",
    flags=re.MULTILINE,
)


# ---------------------------------------------------------------------------
# PROJECT_STANCE: Bell-neutral policy and adopted open noise.
# ---------------------------------------------------------------------------
sub(
    "PROJECT_STANCE.md",
    r"## 5\. Bellの定理に対する立場\n.*?(?=\n## 6\.)",
    r'''## 5. Bellの定理に対する立場

本プロジェクトはBellの定理を否定しない。古典構成からBell型共同統計またはCHSH不等式の破れが得られる場合は、Bell不等式の導出に用いられる前提の少なくとも1つが、その構成では成立していないと考える。

ただし、どの前提を破るかを固定目標の側で先に指定しない。測定設定独立性、Bell局所因子化、parameter independence、outcome independence、標本選択、測定窓中の通信、境界条件その他の因果構造を、採用した模型ごとに監査する。相関式の一致だけでなく、どの確率因子化または因果分離が成立し、どれが成立しないかを物理的な状態変数、設定、結果、記録の流れと対応させる。

現行Q2-2のR180Cは、設定前の一重項源を設定非依存に準備した後、A端で形成した結果成分をB端へ物理的に渡す非空間分離逐次装置である。この現行証人ではBell局所因子化を仮定しない。一方、設定依存準備、共通過去相関、別の境界条件を用いる古典模型も研究対象から排除せず、それぞれ別のBell前提監査を行う。

Q2-2-Sでは、どのBell前提を破るかを先に固定せず、2端の物理的分離と測定窓内の因果隔離を段階的に強めたとき、Bell型共同統計をどこまで維持できるかを調べる。因果隔離下で成立する模型が得られた場合も、Bell前提監査を省略しない。完全なBell局所CHSH前提集合を課した対照系ではCHSH境界へ戻ることを確認する。
''',
    flags=re.DOTALL,
)

rep(
    "PROJECT_STANCE.md",
    "- 開放古典模型では、状態変数、決定論的ドリフト、散逸、雑音の規約と相関、外部駆動または自由エネルギー供給源、エネルギー・エントロピーの流れ、定常化条件を明示する。Hamiltonian無限浴から縮約する場合は、全Hamiltonian、浴の状態、結合、必要なスペクトル密度または相関、縮約の対象を示す。採用ミクロ方程式として置く場合は、その方程式自体をHamiltonian浴から導出したとは呼ばない。",
    "- 開放古典模型では、状態変数、決定論的ドリフト、散逸、雑音の規約と相関、外部駆動または自由エネルギー供給源、エネルギー・エントロピーの流れ、定常化条件を明示する。Hamiltonian無限浴から縮約する場合は、全Hamiltonian、浴の状態、結合、必要なスペクトル密度または相関、縮約の対象を示す。採用ミクロ方程式として置く場合は、その方程式自体をHamiltonian浴から導出したとは呼ばない。Itô/Stratonovich規約と共分散を明示したLangevin型SDEおよび理想白色雑音は採用開放ミクロ方程式として許し、物理回路へ移す場合は有限帯域雑音と時間尺度分離を別途監査する。",
)


# ---------------------------------------------------------------------------
# PROJECT_GUIDE: enhancement governance, file roles, open SDE, Bell audit.
# ---------------------------------------------------------------------------
rep(
    "PROJECT_GUIDE.md",
    "\n### 2.3 検算記録の正本\n",
    r'''
#### 2.2.2 固定目標に付随する強化目標の管理

固定目標に付随する強化目標の定義、適用範囲、現在地は `ENHANCEMENT_TARGETS.md` を正本とする。強化目標は固定目標とは独立に判定し、状態は `未監査`、`未達`、`部分達成`、`達成` の4段階で管理する。

強化目標A1/A2は全固定目標へ適用し、B1/B2/B3はQ1/Q2へ適用する。Q2-2-SはQ2-2固有の空間隔離強化とする。個別項目は `Q1-2-A1`、`Q2-2-B3` のように固定目標IDと強化IDを連結して参照する。新しい固定目標を追加・分割した場合は、同じ方針変更の中で強化目標の適用表も更新する。

強化目標の定義または適用範囲の変更は方針変更として扱う。既存結果を新基準へ照合して現在地だけを更新する場合は通常の論文更新としてよい。固定目標の達成だけから強化目標を自動的に達成とせず、強化目標が未達であることを固定目標の既存達成ラベルへ遡及させない。

A1は各固定目標の主要因果鎖を1つの具体的古典物理模型として閉じることを要求する。複数の固定目標で同じ物理模型を共有してよいが、全系列を同一装置・同一反復周期へ統合するM0はA1より強い横断的統一目標として別に管理する。完全周期収支、有限閉鎖Hamiltonian化、共通浴統合、連続空間一様極限、多粒子化など従来の強化課題もA/B/Sの横断的または上位課題として保持する。

### 2.3 検算記録の正本
''',
)

rep(
    "PROJECT_GUIDE.md",
    "├── PROJECT_STATUS.md\n├── CHANGELOG.md",
    "├── PROJECT_STATUS.md\n├── ENHANCEMENT_TARGETS.md\n├── CHANGELOG.md",
)
rep(
    "PROJECT_GUIDE.md",
    "| `PROJECT_STATUS.md` | 固定長期目標と現在地、モデルの運用状態、導出結果の導出状態と付記情報、物理的解釈、未解決問題の整理 | する |",
    "| `PROJECT_STATUS.md` | 固定長期目標と現在地、モデルの運用状態、導出結果の導出状態と付記情報、物理的解釈、未解決問題の整理 | する |\n| `ENHANCEMENT_TARGETS.md` | 固定目標に付随するA1/A2、Q1/Q2のB1/B2/B3、Q2-2-Sの定義、適用範囲、現在地 | する |",
)
rep(
    "PROJECT_GUIDE.md",
    "既存の問題を未確立の仮説へ移しただけの場合は、解決とは呼ばない。特に、確率重み、境界条件、測定設定独立性、Born則、Tsirelson限界、Wallstrom問題について、2.2節の区分と付記情報を適用する。",
    "既存の問題を未確立の仮説へ移しただけの場合は、解決とは呼ばない。特に、確率重み、境界条件、Bell前提、Born則、Tsirelson限界、Wallstrom問題について、2.2節の区分と付記情報を適用する。",
)
rep(
    "PROJECT_GUIDE.md",
    "開放方程式を置いた後の計算が厳密であっても、その方程式自体を有限閉鎖ハミルトニアン系から導出したことにはならない。ハミルトニアンへの持ち上げを示した場合も、どの極限、初期浴分布、粗視化、誤差評価の下で開放方程式が得られるかを別に示す。逆に、持ち上げが未構成であることだけを理由に、上記の事項を満たす開放古典モデルを不採用とはしない。",
    "開放方程式を置いた後の計算が厳密であっても、その方程式自体を有限閉鎖ハミルトニアン系から導出したことにはならない。ハミルトニアンへの持ち上げを示した場合も、どの極限、初期浴分布、粗視化、誤差評価の下で開放方程式が得られるかを別に示す。逆に、持ち上げが未構成であることだけを理由に、上記の事項を満たす開放古典モデルを不採用とはしない。\n\n強化目標A1では、上記8項目を満たすLangevin型SDEその他の採用開放ミクロ方程式を具体的古典物理模型として認める。理想白色雑音を採用する場合はItô/Stratonovich規約、平均、共分散、白色雑音極限の意味を明示し、その雑音をHamiltonian無限浴から再導出することを必須にしない。A2では採用したSDEそのものを直接標本化する。Hamiltonian無限浴または連続浴をA1として選ぶ場合は、有限帯域・有限モード切断の直接計算と対象時間窓での収束検査をA2としてよい。Q1/Q2のB2/B3では、理想白色雑音を有限帯域の物理雑音源へ置き換え、雑音相関時間と系の遅い時間尺度の分離を監査する。",
)

sub(
    "PROJECT_GUIDE.md",
    r"#### 4\.5\.3 Bellの前提監査\n.*?(?=\n#### 4\.5\.4)",
    r'''#### 4.5.3 Bellの前提監査

Bell型相関を扱う場合は、相関式の再現とは別に、採用した構成についてBell不等式の導出に用いられる前提の成立・不成立を中立的に監査する。特定のloopholeまたは測定設定独立性の破れを成功条件として先に固定しない。

| 監査項目 | 確認する内容 |
|---|---|
| Bell局所因子化 | 隠れた状態または完全履歴 $\lambda$ に条件付けたとき、$P(a,b\mid x,y,\lambda)=P(a\mid x,\lambda)P(b\mid y,\lambda)$ が成立するか。成立しない場合は通信、共通境界、相互作用、結果依存などの物理的原因を示す |
| 測定設定独立性 | $P(\lambda\mid x,y)=P(\lambda)$ が成立するか。成立しない場合は、共通過去、設定依存準備、境界条件、条件付けその他の因果機構を明示し、目的のBell重みを説明なしに外部入力しない |
| parameter / outcome independence | 必要に応じてBell局所因子化を分解し、反対側設定または反対側結果への条件付き依存を区別する |
| 測定窓中の通信 | 設定確定から結果固定までにA→BまたはB→Aの因果伝播を使用するか。使用する場合は伝送経路と時間を示す |
| 結果の一意性 | 各試行で記録される結果が一意に定まるか。確率的応答を用いる場合は、その確率の物理的起源を示す |
| 事後選別・標本選択 | 無反応、棄却、採用試行が設定または結果に依存するか。完全結果集合、除外率、分母の定義を示す |
| 非信号性 | 一側周辺分布が反対側の設定に依存しないか。Bell局所因子化とは別に確認する |
| 試行測度・境界条件 | Bell重みを生む準備、浴、境界条件、試行の数え方を示し、求める重みを未説明の外部表として置いていないか確認する |

近似を採用しても、この監査を省略しない。監査結果は、どの前提が成立し、どの前提が成立しないか、その物理的機構が観測周辺の非信号性とどのように両立するかが分かる形で記録する。

Q2-2-Sで測定窓内因果隔離を主張する場合は、端間距離、最大伝播速度、各端の設定確定時刻と結果固定時刻を明示する。設定確定から結果固定まで他端信号が到達できない時間順序を満たしても、測定設定独立性、共通過去、境界条件、標本選択など他のBell前提が自動的に成立するとは扱わない。逆に、完全なBell局所CHSH前提集合を課したS4対照系ではCHSH境界へ戻ることを確認する。
''',
    flags=re.DOTALL,
)


# ---------------------------------------------------------------------------
# Main paper: Q2-2 interpretation and enhancement-track synchronization.
# ---------------------------------------------------------------------------
rep(
    "sections/05_m54_setting_pre_receiver.md",
    "@title: M54駆動設定先行2端R191受信機構とBell前提監査",
    "@title: M54駆動逐次2端R191受信機構とBell前提監査",
)
rep(
    "sections/05_m54_setting_pre_receiver.md",
    "Q2-2は、固定一重項、固定有限設定族、準備先行、非空間分離の古典装置として、二つの物理的な2値読出し端から量子一重項と同じ共同入出力統計を作ることを目標とする。空間分離Bell局所模型または自由設定loophole-free実験の古典説明は主張しない。",
    "Q2-2の固定目標は、Bell型共同統計を古典構成で再現し、その構成についてBell不等式の導出に用いられる前提の成立・不成立を監査することである。どのBell前提を破るかは固定目標側で指定しない。本節の現行証人は、固定一重項、固定有限設定族、非空間分離の逐次古典装置であり、二つの物理的な2値読出し端から量子一重項と同じ共同入出力統計を作る。現行証人について空間分離Bell局所模型またはloophole-free Bell実験の古典局所説明は主張しない。",
)
rep(
    "sections/05_m54_setting_pre_receiver.md",
    "A端結果結果成分がB端へ物理的に渡るため、切断後局所factorizationやBell局所性は仮定しない。設定前の一重項源は $x,y$ に依存しないが、B端へ到達する内部状態はA設定とA結果に依存する。本結果は測定設定独立性・Bell局所性の前提監査を明示し、空間分離局所模型を主張しない。",
    "A端結果成分がB端へ物理的に渡るため、現行証人ではBell局所因子化を仮定しない。設定前の一重項源は $x,y$ に依存せず、現行証人のCHSH破れを測定設定独立性の破れへ帰属させない。一方、B端へ到達する内部状態はA設定とA結果に依存する。本結果は、この逐次因果伝播、完全結果集合、非信号周辺を同時に示すBell前提監査であり、空間分離局所模型を主張しない。",
)
rep(
    "sections/05_m54_setting_pre_receiver.md",
    "Q2-2で新たに使う確率源はない。A端・B端とも共通R191を用い、共同確率はR191 T.8の逐次Lüders telescopingから得る。固定目標、条件付き達成ラベル、自由設定・空間分離を非主張とする境界は変更しない。",
    "Q2-2で新たに使う確率源はない。A端・B端とも共通R191を用い、共同確率はR191 T.8の逐次Lüders telescopingから得る。Q2-2の条件付き達成ラベルは維持する。現行R180C証人が非空間分離であることと、Q2-2固定目標自体が特定のBell前提違反を指定しないことを区別する。空間隔離をどこまで強められるかは `Q2-2-S` の独立強化課題とする。",
)

rep(
    "sections/00_overview_and_contents.md",
    "Q2-2は固定一重項、固定有限設定族、準備先行、非空間分離の古典装置として扱う。末端4モード信号にA設定を作用し、A端R191で結果 $r$ を形成した後、非規格化結果成分をprojector routerでB端へ渡す。B設定をそこで作用し、B端R191で $s$ を形成する。",
    "Q2-2の現行証人は、固定一重項、固定有限設定族、非空間分離の逐次古典装置である。末端4モード信号にA設定を作用し、A端R191で結果 $r$ を形成した後、非規格化結果成分をprojector routerでB端へ渡す。B設定をそこで作用し、B端R191で $s$ を形成する。Q2-2固定目標は特定のBell前提違反を先に指定せず、採用した古典構成ごとに前提の成立・不成立を監査する。",
)
rep(
    "sections/00_overview_and_contents.md",
    "一重項型信号では余弦共同統計、非信号性、CHSH/Tsirelson値を回収する。A結果成分がB端へ物理的に渡るため、これは空間分離Bell局所模型ではない。自由設定・空間分離・loophole-free Bell実験の古典局所説明を主張しない。",
    "一重項型信号では余弦共同統計、非信号性、CHSH/Tsirelson値を回収する。A結果成分がB端へ物理的に渡るため、現行証人はBell局所因子化を満たす空間分離模型ではない。自由設定・空間分離・loophole-free Bell実験の古典局所説明を現行証人から主張しない。測定窓内の因果隔離をどこまで強められるかはQ2-2-Sで別に監査する。",
)

rep(
    "sections/01_scope_and_cycle.md",
    "固定目標と達成ラベルは `PROJECT_STATUS.md` を正本とする。本再編は固定目標を変更しない。Q1-1、Q1-2、Q3-1--Q3-3Cは現行判定を維持し、Q2-1--Q2-4、Q3-4A、Q3-4B、Q3-5は各文書に明記した単一装置統合条件付き、Q3-6は未達のままとする。Q3-2の達成根拠は、抽象open-Poissonミクロ存在論からM57/R195A--R195Dの明示TL-tracer縮約へ強化する。",
    "固定目標と達成ラベルは `PROJECT_STATUS.md` を正本とする。本改訂ではQ2-2だけを、特定の測定設定独立性違反を必須としない一般のBell前提監査へ広げる。Q2-2を含む既存達成ラベルは維持し、Q1-1、Q1-2、Q3-1--Q3-3Cは達成、Q2-1--Q2-4、Q3-4A、Q3-4B、Q3-5は各文書に明記した条件付き達成、Q3-6は未達のままとする。Q3-2の達成根拠はM57/R195A--R195Dの明示TL-tracer縮約である。\n\n固定目標に付随する強化目標は `ENHANCEMENT_TARGETS.md` を正本とする。全固定目標にA1/A2、Q1/Q2にB1/B2/B3、Q2-2にQ2-2-Sを置き、固定目標の達成状態とは独立に全項目を未監査から開始する。A1では採用開放SDEと理想白色雑音を許し、A2はそのミクロ方程式自体の直接数値再現を要求する。回路強化Bでは有限帯域雑音を含む実験可能領域へ落とす。",
)

# Section 08: Bell falsification row and canonical strengthening section.
sub(
    "sections/08_errors_resources_open_targets.md",
    r"^\| M54/R180A--R180C \|.*$",
    "| M54/R180A--R180C | 実際の末端信号でなく集団モーメントを再注入する、A端R191の結果とrouterが一致しない、B端へ非規格化結果成分を同じ試行のまま渡せない、B端読出しがA/B以外の設定を参照する、R180Cの単一装置境界を満たさない、無反応込みでCHSH誤差上界を満たさない、または現行逐次構成で成立・不成立となるBell前提を因果構造と確率因子化に対応させて監査できない |",
    flags=re.MULTILINE,
)
sub(
    "sections/08_errors_resources_open_targets.md",
    r"## 8\.13 固定目標の残件と実装強化課題\n.*?(?=\n## 8\.14)",
    r'''## 8.13 固定目標の残件と実装強化課題

固定目標上の未完成事項は、Q3-6の位相量子化、Q2-1/Q2-3の末端R191--R181D接続、Q2-4の一様装置族統合である。Q2-4では静的部分系配線、R191 transducerとBrownian macrospin、R181D router、R192方向不変作用安定化、R179開放リセット/供給接続部を1つの装置族へ接続し、R186のノイズ条件を満たす必要がある。Q2-2は特定のBell前提違反を固定条件とせず、現行R180CについてはA結果成分のB端への物理転送によりBell局所因子化を仮定しない構成として監査する。

固定目標に付随する標準強化目標の定義、適用範囲、現在地は `ENHANCEMENT_TARGETS.md` を正本とする。全固定目標に具体的古典ミクロ模型A1と直接数値再現A2、Q1/Q2に具体回路B1、実験可能領域B2、回路直接数値再現B3を置く。Q2-2にはさらに、非空間分離の現行証人から物理的2端化、測定窓内因果隔離、隔離下のBell前提監査へ進むQ2-2-Sを置く。これらの強化状態は固定目標の達成状態と独立であり、導入時点では全て未監査とする。

A1ではHamiltonian無限浴だけでなく、規約と共分散を明示したLangevin型SDEその他の採用開放ミクロ方程式を認め、理想白色雑音を許す。A2では採用したミクロODE/SDEそのものを直接計算する。理想白色雑音を使うQ1/Q2模型を回路へ移す場合、B2/B3では有限帯域雑音源と時間尺度分離を明示する。

従来からのQ1/Q2完全周期収支、R180Cの共通浴統合、M37信号源--M57 tracer--時計--終位置記録の単一反復周期統合、M57の連続空間一様極限、多粒子拡張、有限閉鎖Hamiltonian化は、A/B/Sを横断する上位または系列固有の実装強化課題として保持する。R162を特定Hamiltonian浴から再導出することはM57主線の要件ではない。旧R162有限衝突経路、旧R188、旧R179部分SWAP貯蔵部、旧R178D有限閉鎖リセット境界は撤回せず、有限閉鎖実装を調べる強化結果として論文外メモへ保存する。

Q1-1、Q1-2、Q3-1、Q3-2、Q3-3A、Q3-3B、Q3-3Cは達成、Q2-1、Q2-2、Q2-3、Q2-4、Q3-4A、Q3-4B、Q3-5は条件付き達成、Q3-6は未達である。
''',
    flags=re.DOTALL,
)

# Section 09: neutral Bell audit and expanded open targets.
rep(
    "sections/09_conclusion.md",
    "Q2-2では、固定一重項4モード信号にA設定を作用し、A端R191で $r$ を形成して結果成分 $P_{A,r}^{x}Z$ をB端へ渡し、B設定後のB端R191で $s$ を形成する。共同分布は",
    "Q2-2の現行証人では、固定一重項4モード信号にA設定を作用し、A端R191で $r$ を形成して結果成分 $P_{A,r}^{x}Z$ をB端へ渡し、B設定後のB端R191で $s$ を形成する。Q2-2固定目標は特定のBell前提違反を先に指定せず、採用構成ごとに前提の成立・不成立を監査する。共同分布は",
)
rep(
    "sections/09_conclusion.md",
    "であり、一重項型信号では余弦共同相関、非信号性、CHSH/Tsirelson値を再現する。この装置はA結果成分をB端へ渡す非空間分離装置であり、Bell局所性を主張しない。",
    "であり、一重項型信号では余弦共同相関、非信号性、CHSH/Tsirelson値を再現する。この装置はA結果成分をB端へ渡す非空間分離装置であり、現行証人ではBell局所因子化を仮定しない。設定前の一重項源は設定非依存であり、現行証人のCHSH破れを測定設定独立性の破れへ限定して解釈しない。",
)
rep(
    "sections/09_conclusion.md",
    "残る主要な物理課題は、R191の作用和・作用差transducer、Brownian macrospin、projector router、外部record、R179 resetを同じ具体装置へ統合すること、M37 signal sourceとM57 tracer、clock、終位置recordを単一反復周期へ統合すること、Q2-4の外部多項式資源条件を物理配線・較正・ノイズまで閉じること、Q3のcontinuous-space一様極限・多粒子拡張、Q3-6の位相量子化を閉じることである。",
    "残る主要な物理課題は、各固定目標について具体的古典ミクロ模型A1とその直接数値再現A2を監査すること、Q1/Q2について具体的アナログ回路B1、実験可能パラメータ領域B2、回路直接数値再現B3へ進むこと、Q2-2で測定窓内の空間的・因果的隔離をどこまで強められるかQ2-2-Sで検査することにある。これと並行して、R191の作用和・作用差transducer、Brownian macrospin、projector router、外部記録、R179リセットを同じ具体装置へ統合すること、M37信号源とM57 tracer、時計、終位置記録を単一反復周期へ統合すること、Q2-4の外部多項式資源条件を物理配線・較正・雑音まで閉じること、Q3の連続空間一様極限・多粒子拡張、Q3-6の位相量子化を閉じることを上位または横断的強化課題として残す。A1では採用開放SDEと理想白色雑音を許すが、回路実装Bでは有限帯域雑音へ落とす。",
)


# ---------------------------------------------------------------------------
# README and simulation policy.
# ---------------------------------------------------------------------------
rep(
    "README.md",
    "ただし、A側の結果成分をB側へ物理的に渡す装置なので、空間分離されたBell局所模型ではありません。",
    "ただし、現行証人はA側の結果成分をB側へ物理的に渡す装置なので、Bell局所因子化を満たす空間分離模型ではありません。Q2-2固定目標は特定のBell前提違反を先に指定せず、採用構成ごとに前提の成立・不成立を監査します。測定窓内の因果隔離をどこまで強められるかはQ2-2-Sで別に調べます。",
)
rep(
    "README.md",
    "正式な達成判定、根拠結果、残っている条件は [PROJECT_STATUS.md](PROJECT_STATUS.md) を正本とします。",
    "正式な達成判定、根拠結果、残っている条件は [PROJECT_STATUS.md](PROJECT_STATUS.md) を正本とします。\n\n固定目標とは別に、全Q1--Q3について具体的古典ミクロ模型とその直接数値再現、Q1/Q2についてアナログ回路・実験可能パラメータ領域・回路直接シミュレーション、Q2-2について空間隔離を強める研究軸を [ENHANCEMENT_TARGETS.md](ENHANCEMENT_TARGETS.md) で管理しています。これらは固定目標の達成ラベルと独立で、現在は全項目を未監査から開始しています。理論側では規約を明示した採用開放SDEと理想白色雑音を認め、回路実装では有限帯域雑音へ落とします。",
)
rep(
    "README.md",
    "- [証明状態と理論の境界](PROJECT_STATUS.md)\n- [プロジェクトの長期的方針](PROJECT_STANCE.md)",
    "- [証明状態と理論の境界](PROJECT_STATUS.md)\n- [固定目標に付随する強化目標](ENHANCEMENT_TARGETS.md)\n- [プロジェクトの長期的方針](PROJECT_STANCE.md)",
)

write(
    "simulations/README.md",
    r'''# 現行モデルの数値シミュレーション

このフォルダーには、現行モデルと現行論文の主張を直接検査する数値プログラムを置く。不採用モデルと置換済みモデルのコードは保存せず、Git履歴から参照する。

## 強化目標A2との関係

`ENHANCEMENT_TARGETS.md` のA2は、A1で採用したミクロ方程式そのものの直接数値再現を要求する。採用開放ODE/SDEをA1とする場合は、そのODE/SDEを直接積分または標本化する。理想白色雑音を用いるSDEも、Itô/Stratonovich規約と共分散を固定して直接標本化してよい。

Hamiltonian無限浴、連続伝送線その他の連続浴をA1とする場合は、有限帯域・有限モード切断を直接計算し、対象時間窓で切断依存性または収束性を調べる。有効Schrödinger方程式、Born分布、R161生成子など、導出後の有効模型だけを計算した結果はA2の直接再現とは数えない。

## 強化目標B3との関係

Q1/Q2のB3では、B1で定めた具体回路をSPICE、回路ODE/SDE、伝送線模型などで直接計算する。A1で理想白色雑音を用いる場合も、B3では有限帯域雑音源を用い、有限Q、熱雑音、素子公差、寄生成分とともに成立領域を監査する。必要に応じて雑音帯域を増やしたときのA1白色雑音模型との整合を確認する。

## `tools/` の短い検算との区別

`tools/verify_*.py` は恒等式、有限次元の数値診断、短い回帰検査を担う。これらはA2/B3の補助検算になり得るが、ミクロ方程式または具体回路の直接シミュレーションを行っていない限り、それだけでA2/B3達成とは数えない。

## 収録規約

モデル別または強化目標別フォルダーを追加するときは、完全IDを明示し、少なくとも次を自己完結して保持する。

1. 対象となるA1またはB1模型と運動方程式
2. 数値積分法、確率積分規約、乱数種
3. 基準設定と自動検算用の短縮設定
4. 主要観測量、対照条件、収束検査
5. 集約済み基準結果と再生成命令
6. 数値的一致からは導けない主張の境界

大容量の生軌道や全標本は収録せず、人が差分を読める集約結果を保存する。
'''
)


# ---------------------------------------------------------------------------
# Management records and version metadata.
# ---------------------------------------------------------------------------
prepend(
    "CHANGELOG.md",
    """## draft-97：強化目標体系の全体同期とQ2-2 Bell前提一般化

- Q2-2固定目標から「測定設定独立性の破れ」を特定必須条件として外し、Bell型共同統計を再現した古典構成についてBell不等式導出に用いられる前提の成立・不成立を因果構造と確率因子化に対応させて監査する一般基準へ変更した。現行R180CはA結果成分をBへ渡す非空間分離逐次証人として維持し、Q2-2の条件付き達成ラベルは変更しない。
- `ENHANCEMENT_TARGETS.md` をA1/A2、Q1/Q2のB1/B2/B3、Q2-2-Sの正本としてPROJECT_STATUS、PROJECT_GUIDE、README、第1・8・9章へ正式に接続した。全強化目標は未監査から開始する。
- A1ではHamiltonian無限浴に加え、規約を明示したLangevin型SDEその他の採用開放ミクロ方程式と理想白色雑音を許す。A2は採用ミクロODE/SDEそのものの直接計算を要求する。回路強化B2/B3では有限帯域雑音へ落とす。
- Q2-2-Sを、特定のloopholeまたは共通原因を先に指定しないS0--S4の空間隔離・Bell前提監査へ一般化した。
- `simulations/README.md`、MANIFEST、VALIDATION、構造検査、用語lint、生成物を新しい強化目標体系へ同期した。"""
)

prepend(
    "VALIDATION.md",
    """## draft-97：強化目標体系・Bell前提監査・開放雑音方針の同期検査

```bash
python -m compileall -q tools
python tools/check_source.py
python tools/test_validation_policy.py
python tools/check_terminology.py
python tools/run_physics_checks.py
python tools/build_paper.py
python tools/build_paper.py --output-dir build/ci
python tools/check_generated.py build/ci
python tools/lint_typeset.py build/ci/latex/main.log
git diff --check
```

- PROJECT_STATUSのQ2-2固定目標が特定の測定設定独立性違反を要求せず、Bell前提の成立・不成立を中立的に監査する文言へ一般化されていることを確認する。既存のQ2-2条件付き達成ラベルは維持する。
- `ENHANCEMENT_TARGETS.md` の適用表と現在地表が全固定目標を過不足なく含み、A1/A2は全目標、B1/B2/B3はQ1/Q2だけ、Q2-2-SはQ2-2だけへ適用され、全状態が未監査から始まることを構造検査する。
- A1で採用開放SDEと理想白色雑音を許し、A2でそのミクロ方程式自体を直接標本化し、B2/B3で有限帯域雑音へ落とす責務境界を確認する。
- 現行R180Cについて、設定前一重項源の設定非依存性、A結果成分のB端への物理転送、Bell局所因子化を仮定しないこと、非信号周辺を同時に記述し、特定のBell前提違反へ誤帰属しないことを確認する。
- 過去版CHANGELOG、VALIDATION、退役notesにある旧Q2-2記述は当時の履歴として書き換えない。"""
)

prepend(
    "MANIFEST.md",
    """## draft-97の強化目標・Bell前提・開放雑音方針同期

- `ENHANCEMENT_TARGETS.md` をA1/A2、Q1/Q2のB1/B2/B3、Q2-2-Sの正本として管理文書体系へ正式に追加する。
- Q2-2固定目標を特定のBell前提違反に限定しない一般監査へ改め、現行R180Cを非空間分離逐次証人として維持する。
- 採用開放SDEと理想白色雑音をA1/A2で許し、B2/B3では有限帯域雑音の実験可能領域を監査する。
- README、PROJECT_STANCE、PROJECT_GUIDE、PROJECT_STATUS、第0・1・5・8・9章、simulation規約、構造検査、用語lint、生成物を同期する。"""
)
rep(
    "MANIFEST.md",
    "- `PROJECT_STATUS.md`\n- `CHANGELOG.md`",
    "- `PROJECT_STATUS.md`\n- `ENHANCEMENT_TARGETS.md`\n- `CHANGELOG.md`",
)

rep("CITATION.cff", 'version: "draft-95"', 'version: "draft-97"')


# ---------------------------------------------------------------------------
# Static/source validation for enhancement targets and terminology coverage.
# ---------------------------------------------------------------------------
rep(
    "tools/check_terminology.py",
    '    ROOT / "PROJECT_STANCE.md",\n    *sorted(path for path in SECTIONS.glob("*.md") if path.name != "90_references.md"),',
    '    ROOT / "PROJECT_STANCE.md",\n    ROOT / "ENHANCEMENT_TARGETS.md",\n    *sorted(path for path in SECTIONS.glob("*.md") if path.name != "90_references.md"),',
)

check_source = read("tools/check_source.py")
anchor = "\ndef check_verifier_boundary() -> None:\n"
if anchor not in check_source:
    raise SystemExit("tools/check_source.py: verifier boundary anchor missing")
new_func = r'''

def check_enhancement_targets() -> None:
    status_path = ROOT / "PROJECT_STATUS.md"
    status_text = status_path.read_text(encoding="utf-8")
    fixed_ids = {
        match.group(1)
        for match in re.finditer(r"^\|\s*(Q[123]-\d+[A-Z]?)\s*\|\s*[^|]+\|", status_text, re.MULTILINE)
    }
    # Remove current-position duplicates by set semantics; only actual fixed IDs remain.
    if not fixed_ids:
        raise AssertionError("fixed-goal IDs were not found")

    path = ROOT / "ENHANCEMENT_TARGETS.md"
    text = path.read_text(encoding="utf-8")
    try:
        current = text.split("## 強化目標の現在地表", 1)[1].split("## 既存の実装強化課題との関係", 1)[0]
    except IndexError as exc:
        raise AssertionError("enhancement current-position boundary is missing") from exc

    rows: dict[str, list[str]] = {}
    allowed = {"未監査", "未達", "部分達成", "達成", "—"}
    for line in current.splitlines():
        if not re.match(r"^\|\s*Q[123]-", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 7:
            raise AssertionError(f"malformed enhancement row: {line}")
        qid = cells[0]
        rows[qid] = cells[1:7]
        invalid = set(cells[1:7]) - allowed
        if invalid:
            raise AssertionError(f"unsupported enhancement status for {qid}: {sorted(invalid)}")

    if set(rows) != fixed_ids:
        raise AssertionError(
            f"enhancement target IDs differ from fixed goals: missing={sorted(fixed_ids-set(rows))}, extra={sorted(set(rows)-fixed_ids)}"
        )

    for qid, values in rows.items():
        a1, a2, b1, b2, b3, special = values
        if a1 == "—" or a2 == "—":
            raise AssertionError(f"{qid}: A1/A2 must apply")
        if qid.startswith(("Q1-", "Q2-")):
            if "—" in (b1, b2, b3):
                raise AssertionError(f"{qid}: B1/B2/B3 must apply")
        else:
            if any(value != "—" for value in (b1, b2, b3)):
                raise AssertionError(f"{qid}: B1/B2/B3 must not apply")
        if qid == "Q2-2":
            if special == "—":
                raise AssertionError("Q2-2-S must apply to Q2-2")
        elif special != "—":
            raise AssertionError(f"{qid}: unexpected goal-specific enhancement")

    required = (
        "採用開放ミクロ方程式",
        "理想白色雑音",
        "有限帯域雑音",
        "Q2-2-S",
        "Bell局所因子化",
        "未監査",
    )
    missing = [token for token in required if token not in text]
    if missing:
        raise AssertionError(f"enhancement policy markers missing: {missing}")

    fixed_section = status_text.split("### 固定目標一覧", 1)[1].split("#### Q3-1からQ3-6の達成判定の補足", 1)[0]
    q22 = next((line for line in fixed_section.splitlines() if line.startswith("| Q2-2 |")), "")
    if "測定設定独立性の破れ" in q22:
        raise AssertionError("Q2-2 fixed goal still requires measurement-setting dependence")
    if "Bell不等式の導出に用いられる前提" not in q22:
        raise AssertionError("Q2-2 fixed goal does not require neutral Bell-premise audit")

    stance = (ROOT / "PROJECT_STANCE.md").read_text(encoding="utf-8")
    if "どの前提を破るかを固定目標の側で先に指定しない" not in stance:
        raise AssertionError("Bell-neutral project stance is missing")

    receiver = (ROOT / "sections" / "05_m54_setting_pre_receiver.md").read_text(encoding="utf-8")
    for token in ("設定前の一重項源は $x,y$ に依存せず", "Bell局所因子化を仮定しない", "Q2-2-S"):
        if token not in receiver:
            raise AssertionError(f"Q2-2 receiver policy marker missing: {token}")
'''
check_source = check_source.replace(anchor, new_func + anchor, 1)
main_anchor = "    check_project_status()\n    check_verifier_boundary()"
if main_anchor not in check_source:
    raise SystemExit("tools/check_source.py: main anchor missing")
check_source = check_source.replace(
    main_anchor,
    "    check_project_status()\n    check_enhancement_targets()\n    check_verifier_boundary()",
    1,
)
write("tools/check_source.py", check_source)


# Remove temporary finalizer files before the generated commit.
for temporary in (
    ROOT / "tools" / "finalize_draft97.py",
    ROOT / ".github" / "workflows" / "draft97-finalize.yml",
):
    if temporary.exists():
        temporary.unlink()

print("draft97_policy_sync_ok")
