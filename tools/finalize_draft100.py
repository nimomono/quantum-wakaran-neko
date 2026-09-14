#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    text = read(path)
    count = text.count(old)
    if count != 1:
        raise AssertionError(f"{path}: expected one occurrence, got {count}: {old[:80]!r}")
    write(path, text.replace(old, new, 1))


def regex_once(path: str, pattern: str, repl: str, flags: int = 0) -> None:
    text = read(path)
    new, count = re.subn(pattern, repl, text, count=1, flags=flags)
    if count != 1:
        raise AssertionError(f"{path}: regex expected one match, got {count}: {pattern!r}")
    write(path, new)


def prepend(path: str, block: str) -> None:
    text = read(path)
    if block.strip() in text:
        raise AssertionError(f"{path}: block already present")
    write(path, block + text)


# ---------------------------------------------------------------------------
# Section 2: R161 now owns finite-state path existence; R162 is optional PRM.
# ---------------------------------------------------------------------------
path = "sections/02_common_canonical_modules.md"
regex_once(
    path,
    r"^@status:.*$",
    "@status: M54をQ1・Q2・Q3の共通有効信号--配置状態構成族として定義する。初期状態方向は準備済み古典入力境界として扱い、R191をQ1/Q2の2結果射影読出し主線、R181B/R181Cを固定入力持上げ・永続ゲート、R181Dを射影結果成分受渡し、R192を一般深さQ2-4の方向不変作用安定化として分離する。R161をQ3位置輸送の共通数学核とし、有限状態のcanonical Markov経路法則とBayes後退率まで含める。M57/R195A・R196A--R196Cを現行ミクロ物理実現、R162をR161経路法則のoptional independent-Poisson realizationとして分離する。Q1型局所信号とQ2型辺結合からR161の $(\\pi,j)$ が得られる構造を明示する。",
    re.MULTILINE,
)
replace_once(
    path,
    "Q1/Q2では2結果射影作用をR191読出しinterfaceへ渡し、Q3ではM57の2作用状態数が開始配置重みを与え、同じ局在tracerをR196C/R161へ渡す。R162は同じ生成子を持つideal stochastic referenceとして使う。",
    "Q1/Q2では2結果射影作用をR191読出しinterfaceへ渡し、Q3ではM57の2作用状態数が開始配置重みを与え、同じ局在tracerをR196C/R161へ渡す。R161自身が有限状態のcanonical Markov経路法則まで定め、R162は同じ経路法則を独立Poisson random measuresで実現するoptional referenceとして使う。",
)
replace_once(
    path,
    "| Q3 | 空間信号＋局在tracer | 準備済み古典空間入力、M37＋M57 dual-ballistic-TL moving-bath tracer | R195A、R196A--R196C、R161、R185（R162はideal reference） |",
    "| Q3 | 空間信号＋局在tracer | 準備済み古典空間入力、M37＋M57 dual-ballistic-TL moving-bath tracer | R195A、R196A--R196C、R161、R185 |",
)
replace_once(
    path,
    "Q3は準備済み空間信号からM37/R86とM57/R195A・R196A--R196Cの経路へ入り、R161/R185へ接続する。R162は比較用ideal open-jump referenceとして残す。",
    "Q3は準備済み空間信号からM37/R86とM57/R195A・R196A--R196Cの経路へ入り、R161のcanonical Markov経路法則を経てR185へ接続する。R162はこの経路法則のoptional independent-Poisson realizationとして比較用途にだけ残す。",
)
replace_once(
    path,
    "## 2.8 R161の共通整合とM57/R162の物理・参照実現",
    "## 2.8 R161の共通整合・Markov経路法則とM57/R162の物理・参照実現",
)
replace_once(
    path,
    "**定理（R161：有限配置の確率流・活動量整合）**",
    "**定理（R161：有限配置の確率流・活動量整合とMarkov経路存在）**",
)
needle = """同じ経路分布のBayes反転は

```math
\\frac{\\pi_jk^+_{j\\to i}}{\\pi_i}
=
k^-_{i\\to j}
```

を満たす。

静的状態構成では $j=0$ とし、"""
insert = """同じ経路分布のBayes反転は

```math
\\frac{\\pi_jk^+_{j\\to i}}{\\pi_i}
=
k^-_{i\\to j}
```

を満たす。

さらに固定有限時間 $0\\leq t\\leq T$ で $k^+_{i\\to j}(t)$ がBorel可測かつ

```math
M_T
=
\\sup_{0\\leq t\\leq T}
\\max_i\\sum_{j\\ne i}k^+_{i\\to j}(t)
<\\infty
```

を満たすなら、この時間依存生成子を持つ非爆発càdlàg有限状態Markov過程は法則の意味で一意に存在する。Q3では許容された古典signal履歴 $Z_{[0,T]}=z_{[0,T]}$ を固定してこの条件付き経路法則を構成し、その後signal履歴の法則で混合して共同法則を得る。従ってR185が必要とする前向き経路法則とBayes後退率はR161自身の結論である。

静的状態構成では $j=0$ とし、"""
replace_once(path, needle, insert)
replace_once(
    path,
    "この生成子同値により、R161より前段のミクロ実現を交換しても、同じ位置経路法則とR185の縮約を共通に扱える。現行主線ではM57を物理実現、R162をideal stochastic referenceとする。",
    "この生成子同値により、R161より前段のミクロ実現を交換しても、同じcanonical位置経路法則とR185の縮約を共通に扱える。現行主線ではM57を物理実現とし、R162はR161経路法則を独立Poisson random measuresでpathwiseに実現するoptional stochastic referenceとする。",
)
replace_once(
    path,
    "**定理（R162：局所有向率の開放Poisson-jump実現）**",
    "**定理（R162：R161経路法則の独立Poisson-jump実現）**",
)
replace_once(
    path,
    "固定有限グラフ、固定有限時間 $T$ 上で、R161が与える有向率 $k_{i\\to j}(t)\\geq0$ が可測かつ",
    "固定有限グラフ、固定有限時間 $T$ 上で、R161の仮定を満たす有向率 $k_{i\\to j}(t)\\geq0$ を取る。R161によりcanonical Markov経路法則は既に一意に存在する。さらに",
)
replace_once(
    path,
    "Poisson reservoirはR161生成子を厳密に実現するideal open-jump referenceである。現行Q3の基礎的ミクロ存在論はM57/R195A・R196A--R196Cが担い、R162は生成子・経路法則の比較とR185の数学的参照に用いる。有限衝突Hamiltonian列への持上げは強化結果として論文外メモへ分離する。R161の静的 $j=0$ 特殊化は数学的比較用に残すが、Q1/Q2の2結果読出し主線ではR191を使う。",
    "Poisson reservoirはR161 canonical経路法則の一つの明示的pathwise realizationである。現行Q3の基礎的ミクロ存在論はM57/R195A・R196A--R196Cが担い、Q3-2とR185の論理依存はR161だけで閉じる。R162は比較、シミュレーション、開放Poisson実装の参照に用いる。有限衝突Hamiltonian列への持上げは強化結果として論文外メモへ分離する。R161の静的 $j=0$ 特殊化は数学的比較用に残すが、Q1/Q2の2結果読出し主線ではR191を使う。",
)
replace_once(
    path,
    "R161は静的・移動の率構成を共通に保つ。現行Q3の物理主線はM57/R195A・R196A--R196Cであり、R162は同じ率を持つideal referenceとして残す。Q1/Q2の2結果測定はR161静的鎖を経由せずR191へ直接接続する。旧有限衝突実装は退役メモに保存する。",
    "R161は静的・移動の率構成に加え、有限状態のcanonical Markov経路法則まで共通に保つ。現行Q3の物理主線はM57/R195A・R196A--R196Cであり、R162は同じ経路法則を持つoptional Poisson realizationとして残す。Q1/Q2の2結果測定はR161静的鎖を経由せずR191へ直接接続する。旧有限衝突実装は退役メモに保存する。",
)

# ---------------------------------------------------------------------------
# Appendix K: prove the path law inside R161, narrow R162 to realization only.
# ---------------------------------------------------------------------------
path = "sections/A11_common_collision_bath_thermodynamics.md"
regex_once(path, r"^@title:.*$", "@title: 共通整合Markov経路と開放jump参照実現", re.MULTILINE)
regex_once(
    path,
    r"^@status:.*$",
    "@status: R161の確率流・活動量整合、有限状態canonical Markov経路存在、Bayes後退率、その活動量--親和力等価表示と生成子同値を証明する。R162は同じR161経路法則の独立Poisson-random-measureによるoptional明示実現として保持し、Q3-2の達成根拠には用いない。静的詳細釣り合いは一般整合定理の特殊化としてのみ残す。",
    re.MULTILINE,
)
replace_once(
    path,
    "本付録はM54の有限配置変数 $X$ を動かす共通整合原理を扱う。R161は目標分布、確率流、活動量から前向き・Bayes後向き率を定め、R162はその有向率を明示的な古典開放Poisson reservoirで実現する。現行因果鎖での用途はQ3の開始配置後の位置輸送と、R185の前進・後退平均微分への受渡しである。",
    "本付録はM54の有限配置変数 $X$ を動かす共通整合原理を扱う。R161は目標分布、確率流、活動量から前向き率を定め、有界総hazardの下で一意な非爆発canonical Markov経路法則とそのBayes後退率まで与える。現行因果鎖ではこのR161経路法則をQ3の開始配置後の位置輸送からR185の前進・後退平均微分へ直接渡す。R162は同じ法則を独立Poisson random measuresで実現するoptional参照構成である。",
)
anchor = "### K.3.1 活動量--親和力表示とR161実現同値"
path_block = r"""### K.3.1 有限状態canonical Markov経路法則の存在と一意性

固定有限時間 $0\leq t\leq T$ で各 $k^+_{i\to j}(t)$ をBorel可測とし、

```math
M_T
=
\sup_{0\leq t\leq T}
\max_i\sum_{j\ne i}k^+_{i\to j}(t)
<\infty
```

を仮定する。時刻 $s$ に $X_s=i$ であるとき、次jump時刻 $\tau$ の生存関数を

```math
P(\tau>u\mid X_s=i)
=
\exp\!\left[
-\int_s^u\lambda_i(r)\,dr
\right],
\qquad
\lambda_i(t)=\sum_{j\ne i}k^+_{i\to j}(t)
```

とし、$\tau=u$ で $\lambda_i(u)>0$ のとき遷移先を

```math
P(X_u=j\mid \tau=u,X_{u-}=i)
=
\frac{k^+_{i\to j}(u)}{\lambda_i(u)}
```

で選ぶ。このhazard constructionを再帰すればcàdlàg純jump過程が得られる。固定有限時間内のjump数は率 $M_T$ のPoisson過程で上から支配できるので非爆発である。有限状態の時間非一様Kolmogorov方程式の一意性と上のhazard指定により、この生成子を持つMarkov経路法則は法則の意味で一意である。

Q3ではsignal履歴 $z_{[0,T]}$ を固定するとR161率は時間の既知関数になるため、まず条件付き法則

```math
\mathbb P^{\rm R161}
\left(dX_{[0,T]}\mid Z_{[0,T]}=z_{[0,T]}\right)
```

を構成し、最後にsignal履歴の法則で混合して $(Z,X)$ の共同法則を得る。従って $X$ 単独を自律Markov過程と仮定する必要はない。

### K.3.2 活動量--親和力表示とR161実現同値"""
replace_once(path, anchor, path_block)
replace_once(path, "### K.3.2 静的 詳細釣り合い特殊化", "### K.3.3 静的 詳細釣り合い特殊化")
replace_once(path, "### K.3.3 節点における静的再平衡化の障害", "### K.3.4 節点における静的再平衡化の障害")
replace_once(
    path,
    "一般整合部分は確率流恒等式と有限状態マスター方程式の一意性、後退 率はBayes反転から従う。",
    "一般整合部分は確率流恒等式と有限状態マスター方程式の一意性から従う。有界総hazardの下では上のhazard constructionが非爆発càdlàg Markov経路法則を与え、有限状態ではその法則は一意である。後退率は同じ経路法則のBayes反転から従う。",
)
replace_once(path, "## K.4 R162の証明：開放Poisson-jump実現", "## K.4 R162の証明：R161経路法則の独立Poisson-jump実現")
replace_once(
    path,
    "有限状態集合上の各有向辺 $(i,j)$ に独立なPoisson random measure $N_{ij}(dt\\,du)$ を強度 $dt\\,du$ で置く。",
    "R161の有界総hazard条件を満たす固定有限時間の率を取る。R161によりcanonical Markov経路法則の存在・一意性・非爆発性は既に確立している。ここではその同じ法則をpathwiseに具体化するため、有限状態集合上の各有向辺 $(i,j)$ に独立なPoisson random measure $N_{ij}(dt\\,du)$ を強度 $dt\\,du$ で置く。",
)
replace_once(
    path,
    "従って生成子は",
    "このPoisson構成の生成子は",
)
replace_once(
    path,
    "であり、Kolmogorov前進方程式はR161のmaster equationに一致する。R161の整合条件から初期分布 $p(0)=\\pi(0)$ なら $p(t)=\\pi(t)$ である。同じ経路法則の2時刻条件付き確率にBayes則を適用すれば後向き率はR161の $k^-$ となる。物理的逆時間浴は追加しない。",
    "であり、R161のcanonical生成子と一致する。経路法則の一意性から、このPoisson構成はR161 lawそのものを実現する。周辺分布整合とBayes後退率はR161から既に従い、物理的逆時間浴は追加しない。",
)
replace_once(
    path,
    "上のPoisson構成の標準的なcompensator計算から生成子式を得る。有限総hazard上界が非爆発性を与え、有限状態のKolmogorov方程式の一意性からR161の周辺分布が従う。後退率は同じ前向き経路法則のBayes反転であり、別の確率源を必要としない。証明終。",
    "上のPoisson構成の標準的なcompensator計算からR161と同一の生成子式を得る。R161で既に示した経路法則の一意性により、この構成の法則はcanonical R161 lawと一致する。証明終。",
)
replace_once(
    path,
    "新R162はQ3の移動過程に対する採用開放ミクロ方程式であり、有限閉鎖Hamiltonian実装を主張しない。",
    "R162はR161 canonical経路法則のoptional independent-Poisson realizationであり、Q3の現行ミクロ物理層でもQ3-2の達成根拠でもない。有限閉鎖Hamiltonian実装を主張しない。",
)

# ---------------------------------------------------------------------------
# Appendix N: R185 depends directly on the R161 law, not R162.
# ---------------------------------------------------------------------------
path = "sections/A14_m54_spatial_moving_matching.md"
regex_once(
    path,
    r"^@status:.*$",
    "@status: R161が定める空間移動参照過程とcanonical Markov経路法則を定義し、Q1型局所正準信号とQ2型辺結合から得る $(\\pi,j)$ をR161へ接続する。現行 $T_{ij}^\\delta$ は許容される対称活動量の1選択として位置づけ、R184のM37開始作用保持機構実装とR185のNelson型前後平均微分・時間対称Newton則を証明する。R162は同じR161 lawのoptional Poisson realizationであり、本付録の論理依存には置かない。",
    re.MULTILINE,
)
replace_once(
    path,
    "$Q_i,P_i$ は実正準信号自由度、$X_t\\in V$ はR161生成子に従う参照位置座標である。R162は同じ局所有向率を実現するideal open-jump referenceとして利用できるが、M57 tracerとは別の実在粒子やQ3の基礎的ミクロ存在論を追加するものではない。",
    "$Q_i,P_i$ は実正準信号自由度、$X_t\\in V$ はR161 canonical Markov経路法則に従う参照位置座標である。R162を用いなくてもこの経路法則はR161自身で存在・一意性・非爆発性まで定まる。",
)
replace_once(
    path,
    "新R162の開放jump過程と終時刻記録を加えた完全結果誤差を",
    "R161 canonical Markov経路法則と終時刻記録を加えた完全結果誤差を",
)
replace_once(
    path,
    "R162の開放jump生成子を適用する。",
    "対応するR161有限状態Markov生成子へDuhamel公式を適用する。",
)
replace_once(
    path,
    "R161が定める前向き経路法則（R162はそのideal open-jump reference）からR185のBayes後退率を作るため、",
    "R161自身が定めるcanonical前向き経路法則からR185のBayes後退率を作るため、",
)

# ---------------------------------------------------------------------------
# Current status and prose: remove R162 from Q3-2 evidence, retain as optional.
# ---------------------------------------------------------------------------
path = "PROJECT_STATUS.md"
prepend(
    path,
    """## draft-100：R161へ有限状態Markov経路法則を吸収

- R161の責務を、確率流・活動量からの有向率と周辺分布整合だけでなく、固定有限時間・有限状態・有界総hazard下の一意な非爆発canonical Markov経路法則とBayes後退率まで拡張する。
- Q3-2の達成根拠からR162を外し、M57/R195A・R196A--R196C → R161 → R185を現行因果鎖とする。
- R162は結果IDを維持するが、R161経路法則を独立Poisson random measuresでpathwiseに実現するoptional referenceへ責務を縮約する。現行Q3ミクロ物理層でもR185の必須依存でもない。
- 固定目標、達成ラベル、M57/R195A・R196A--R196C、R184、R185の内容は変更しない。

""",
)
replace_once(
    path,
    "| R161 | 厳密結果 | 正の対象分布、反対称確率流、対称活動量から前向き整合と共通の確率分布後退率を構成。静的特殊化で平方根型詳細釣り合い・一意定常分布・一様混合上界、空間特殊化で旧R183移動分布の整合を回収 | 採用生成子後。静的/移動の活動量選択を別途指定。$\\delta\\downarrow0$ で資源発散 |",
    "| R161 | 厳密結果 | 正の対象分布、反対称確率流、対称活動量から前向き率を構成し、有界総hazard下で一意な非爆発canonical Markov経路法則とBayes後退率まで与える。静的特殊化で平方根型詳細釣り合い・一意定常分布・一様混合上界、空間特殊化で旧R183移動分布の整合を回収 | 固定有限時間・有限状態。静的/移動の活動量選択を別途指定。$\\delta\\downarrow0$ で資源発散 |",
)
replace_once(
    path,
    "| R162 | ideal open-jump referenceの厳密結果 | R161の任意の有界局所有向率を独立Poisson reservoirで直接実現し、生成子とmaster equationを一致させる。M57の基礎的実体ではなくR195Dの比較対象。Bayes後退率は同じ前向き経路法則から得る | 固定有限時間・有限状態。有限衝突Hamiltonian列への持上げは強化結果として退役メモへ分離 |",
    "| R162 | optional Poisson realizationの厳密結果 | R161 canonical経路法則を独立Poisson random measuresでpathwiseに実現する。経路存在・周辺整合・Bayes後退率はR161側で既に閉じるため、Q3-2達成根拠には含めない | 固定有限時間・有限状態。有限衝突Hamiltonian列への持上げは強化結果として退役メモへ分離 |",
)
replace_once(
    path,
    "R195A、R196A--R196C、R161、R162、R185",
    "R195A、R196A--R196C、R161、R185",
)
replace_once(
    path,
    "R162 Poisson reservoirはideal referenceであり基礎的存在論へ含めない。",
    "R162 Poisson realizationはR161 lawのoptional referenceであり、Q3-2の達成根拠にも基礎的存在論にも含めない。",
)
replace_once(
    path,
    "R161はM57に固有でなく、拡散を担う対称活動量と確率流を受け取る共通数学interfaceである。",
    "R161はM57に固有でなく、拡散を担う対称活動量と確率流を受け取り、有限状態canonical Markov経路法則まで定める共通数学interfaceである。",
)

# Section 1
path = "sections/01_scope_and_cycle.md"
regex_once(
    path,
    r"^@status:.*$",
    "@status: M54をQ1・Q2・Q3の共通有効信号構成族、M37を物理信号実装層、M57をQ3粒子輸送の現行ミクロ物理層として区別する。Q1/Q2のR191射影読出しとQ3のM57/R195A・R196A--R196C--R161位置輸送は結果形成として分離し、R161自身が有限状態canonical Markov経路法則まで与える。R162はそのoptional independent-Poisson realizationとしてのみ扱いつつ、Q1型局所正準信号とQ2型2体系結合からQ3空間信号の $(\\pi,j)$ を作る共通構造を明示する。",
    re.MULTILINE,
)
text = read(path)
text = text.replace("R161/R162/R185", "R161/R185")
write(path, text)

# Section 6: current prose only, historical occurrences left untouched.
path = "sections/06_m37_spatial_envelope.md"
text = read(path)
text = text.replace("R161/R162の数学核", "R161/R185の数学核")
text = text.replace("R162はideal reference", "R162はR161 lawのoptional Poisson realization")
write(path, text)

# Section 8: path-existence failure condition belongs to R161.
path = "sections/08_errors_resources_open_targets.md"
regex_once(
    path,
    r"^@status:.*$",
    "@status: Q1/Q2のR191 2結果読出し、R181D projector router、Q2-2の2端逐次R191、Q3のM57/R195A・R196A--R196C--R161--R185経路、M37信号物理実装層を横断して誤差・資源・反証条件を整理する。R162はR161 lawのoptional Poisson realizationであり中心誤差台帳へ入れない。",
    re.MULTILINE,
)
# Insert a failure row immediately before the M57 row.
needle = "| M57/R195A・R196A--R196C |"
text = read(path)
pos = text.find(needle)
if pos < 0:
    raise AssertionError("sections/08: M57 failure row not found")
line_start = text.rfind("\n", 0, pos) + 1
row = "| R161 path law | 固定有限時間で $M_T=\\sup_{t\\leq T}\\max_i\\sum_{j\\ne i}k^+_{i\\to j}(t)<\\infty$ を満たさず、finite-state canonical Markov経路法則の非爆発性を保証できない |\n"
text = text[:line_start] + row + text[line_start:]
write(path, text)

# README: make dependency unambiguous.
path = "README.md"
replace_once(
    path,
    "Q3では、M37/M54空間信号からM57 dual-ballistic-TL moving-bath tracerへ接続し、R161/R162/R185の共通数学核を通して",
    "Q3では、M37/M54空間信号からM57 dual-ballistic-TL moving-bath tracerへ接続し、R161が定めるcanonical Markov経路法則とR185を通して",
)
replace_once(
    path,
    "R161は共通数学interface、R162はideal stochastic referenceとして残し、M57の基礎的物理実体とは扱いません。",
    "R161は共通数学interfaceであり、有限状態のcanonical Markov経路法則まで自身で定めます。R162はその法則を独立Poisson random measuresで具体化したoptional stochastic referenceとして残し、Q3-2の達成根拠やM57の基礎的物理実体とは扱いません。",
)

# Notes: update current interpretation, not historical records.
path = "notes/r161_q1_q2_q3_realization_equivalence.md"
text = read(path)
text = text.replace("     k±\n      ↓ R162\nideal jump reference", "     k±\n      ↓ R161 canonical path law\nfinite-state Markov path\n      ↘ R162\noptional Poisson realization")
text = text.replace("R162/R185を再導出", "R161 path law/R185を再導出")
write(path, text)

path = "notes/superseded_q3_poisson_microphysics.md"
text = read(path)
marker = "R162「局所有向率の開放Poisson-jump実現」そのものは退役しない。退役するのは、独立Poisson reservoirをQ3粒子輸送の基礎的ミクロ物理そのものと読む旧位置づけである。"
if marker not in text:
    raise AssertionError("superseded_q3_poisson_microphysics marker missing")
text = text.replace(
    marker,
    marker + " draft-100以後、有限状態Markov経路法則の存在・一意性・非爆発性とBayes後退率はR161自身へ吸収し、R162はそのcanonical lawのoptional independent-Poisson realizationとしてのみ保持する。",
    1,
)
write(path, text)

# Changelog / manifest / validation: append a current record without rewriting history.
block = """## draft-100：R161 canonical Markov path law

- R161へ、固定有限時間・有限状態・有界総hazard下の非爆発càdlàg Markov経路法則の存在・一意性を吸収した。
- R185の前向き・Bayes後向き平均微分はR161 lawへ直接依存させ、Q3-2根拠一覧からR162を除外した。
- R162は同じR161 lawの独立Poisson-random-measureによるoptional pathwise realizationへ責務を縮約した。結果IDは維持する。
- 固定目標、達成ラベル、M57/R195A・R196A--R196C、R184、R185の数式内容は変更していない。

"""
prepend("CHANGELOG.md", block)
prepend("MANIFEST.md", block)
prepend(
    "VALIDATION.md",
    """## draft-100：R161 canonical Markov path law検算

- R161の有界総hazard条件、前向きmaster equation、Bayes後退率、有限状態経路法則の責務境界を検算対象へ追加した。
- `tools/verify_r161_path_law.py` で3状態時間依存例の非負率、有限総hazard、連続方程式、Bayes reverse identityを数値確認する。
- `tools/check_source.py` でPROJECT_STATUSのQ3-2根拠行にR162が再混入しないこと、R161にpath-existence markerがあること、R162定理がoptional Poisson realizationとして残ることを回帰検査する。

""",
)

# Source regression checks.
path = "tools/check_source.py"
insert_before = "\ndef check_enhancement_targets() -> None:\n"
new_func = '''\ndef check_r161_path_boundary() -> None:\n    status = (ROOT / "PROJECT_STATUS.md").read_text(encoding="utf-8")\n    q32 = next((line for line in status.splitlines() if line.startswith("| Q3-2 |")), "")\n    if not q32:\n        raise AssertionError("Q3-2 current-position row is missing")\n    cells = [cell.strip() for cell in q32.strip().strip("|").split("|")]\n    if len(cells) < 7:\n        raise AssertionError("Q3-2 current-position row is malformed")\n    evidence = cells[5]\n    if "R162" in evidence:\n        raise AssertionError("R162 must not be a Q3-2 evidence dependency")\n    for token in ("R195A", "R196A--R196C", "R161", "R185"):\n        if token not in evidence:\n            raise AssertionError(f"Q3-2 evidence is missing {token}")\n\n    common = (ROOT / "sections" / "02_common_canonical_modules.md").read_text(encoding="utf-8")\n    required = (\n        "R161：有限配置の確率流・活動量整合とMarkov経路存在",\n        "M_T",\n        "canonical Markov経路法則",\n        "R162：R161経路法則の独立Poisson-jump実現",\n    )\n    missing = [token for token in required if token not in common]\n    if missing:\n        raise AssertionError(f"R161 path-law markers missing: {missing}")\n\n    appendix = (ROOT / "sections" / "A14_m54_spatial_moving_matching.md").read_text(encoding="utf-8")\n    if "R161が定める前向き経路法則（R162" in appendix:\n        raise AssertionError("R185 still declares R162 as a path dependency")\n\n'''
text = read(path)
if insert_before not in text:
    raise AssertionError("check_source insertion point missing")
text = text.replace(insert_before, new_func + insert_before, 1)
text = text.replace(
    "    check_project_status()\n    check_enhancement_targets()",
    "    check_project_status()\n    check_r161_path_boundary()\n    check_enhancement_targets()",
    1,
)
write(path, text)

# Numerical verifier; run_physics_checks.py discovers verify_*.py automatically.
verify = r'''#!/usr/bin/env python3
from __future__ import annotations

import math
import numpy as np


def sample(t: float) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    eps = 0.04
    pi = np.array([
        1.0 / 3.0 + eps * math.sin(t),
        1.0 / 3.0 - eps * math.sin(t),
        1.0 / 3.0,
    ])
    dpi = np.array([eps * math.cos(t), -eps * math.cos(t), 0.0])

    # Convention: dot(pi_i) = sum_j j_{j i}.
    j = np.zeros((3, 3))
    j[1, 0] = eps * math.cos(t)
    j[0, 1] = -j[1, 0]

    activity = np.array([
        [0.0, 0.12, 0.08],
        [0.12, 0.0, 0.07],
        [0.08, 0.07, 0.0],
    ])
    kp = np.zeros((3, 3))
    km = np.zeros((3, 3))
    for i in range(3):
        for k in range(3):
            if i == k:
                continue
            kp[i, k] = (activity[i, k] + j[i, k]) / (2.0 * pi[i])
            km[i, k] = (activity[i, k] - j[i, k]) / (2.0 * pi[i])
    return pi, dpi, j, kp, km


def main() -> None:
    hazard_max = 0.0
    for t in np.linspace(0.0, 4.0, 401):
        pi, dpi, j, kp, km = sample(float(t))
        assert np.min(pi) > 0.0
        assert np.min(kp) >= -1e-14
        assert np.min(km) >= -1e-14

        forward = np.zeros(3)
        for i in range(3):
            forward[i] = sum(pi[k] * kp[k, i] - pi[i] * kp[i, k] for k in range(3) if k != i)
        assert np.max(np.abs(forward - dpi)) < 1e-12

        for i in range(3):
            for k in range(3):
                if i == k:
                    continue
                bayes = pi[k] * kp[k, i] / pi[i]
                assert abs(bayes - km[i, k]) < 1e-12

        hazard_max = max(hazard_max, float(np.max(np.sum(kp, axis=1))))

    assert math.isfinite(hazard_max) and hazard_max < 1.0
    print(f"r161_path_law_ok hazard_max={hazard_max:.6f}")


if __name__ == "__main__":
    main()
'''
write("tools/verify_r161_path_law.py", verify)

print("draft100_source_edits_ok")
