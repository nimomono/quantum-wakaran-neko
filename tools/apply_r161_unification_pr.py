#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    text = read(path)
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected one occurrence, got {count}: {old[:80]!r}")
    write(path, text.replace(old, new, 1))


def regex_once(path: str, pattern: str, replacement: str, *, flags: int = 0) -> None:
    text = read(path)
    new, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{path}: regex expected one occurrence, got {count}: {pattern!r}")
    write(path, new)


# ---------------------------------------------------------------------------
# 0. Overview: separate measurement causality from the shared signal algebra.
# ---------------------------------------------------------------------------
replace_once(
    "sections/00_overview_and_contents.md",
    "@status: M54をQ1・Q2・Q3の共通有効状態構成族、M37を物理実装層として区別し、Q1/Q2のR191射影読出しとQ3のR164--R161/R162位置輸送を二つの現行因果鎖として整理する。Q1ではR189A保持座標からR193を通じてR191 decision energyへ直接接続する。",
    "@status: M54をQ1・Q2・Q3の共通有効状態構成族、M37を物理実装層として区別する。Q1/Q2のR191射影読出しとQ3のR164--R161/R162位置輸送は結果形成の因果鎖として分ける一方、Q1型局所正準信号を空間配置しQ2型2体系結合を辺へ反復するとQ3の空間信号とR161入力 $(\\pi,j)$ が得られる共通構造を明示する。",
)
replace_once(
    "sections/00_overview_and_contents.md",
    "Q3の位置主線は別である。\n",
    "Q3の信号部分系はQ1/Q2と別の代数ではない。Q1で使うものと同じ局所実正準モードを有限配置グラフの頂点へ置き、Q2で用いるのと同型の2体系エルミート結合を辺へ反復すると、グラフLaplacian型の空間伝播と反対称確率流が生じる。局所作用から $\\pi_i\\propto|Z_i|^2$、辺流から $j_{ij}$ を作り、別途与える対称活動量 $t_{ij}$ とともにR161へ渡す。独立なQ1型モードを並べるだけでは辺流がなくQ3にはならない。\n\nQ3の粒子位置形成・輸送はQ1/Q2の測定結果形成とは別の因果鎖である。\n",
)

# ---------------------------------------------------------------------------
# 1. Scope: Q1 local structure + Q2 pair interaction -> Q3 signal input.
# ---------------------------------------------------------------------------
regex_once(
    "sections/01_scope_and_cycle.md",
    r"^@status:.*$",
    "@status: M54をQ1・Q2・Q3の共通有効状態構成族、M37を物理実装層として区別する。Q1/Q2のR191射影読出しとQ3のR164--R161/R162位置輸送は結果形成として分離しつつ、Q1型局所正準信号とQ2型2体系結合からQ3空間信号の $(\\pi,j)$ を作る共通構造を明示する。Q1ではR189A保持座標からR193を通じてR191 decision energyへ直接接続する。",
    flags=re.MULTILINE,
)
replace_once(
    "sections/01_scope_and_cycle.md",
    "Q3では実在粒子位置を別の因果鎖で扱う。\n",
    "Q3の信号数学はQ1/Q2から切り離された別構造ではない。各頂点へQ1型の局所実正準モードを配置し、辺へQ2で用いるのと同じ有限2体系エルミート生成子の結合族を反復すると、$i\\mathcal J_0\\dot Z=hZ$ の空間信号を得る。辺結合を持たない独立Q1列では $j_{ij}=0$ で空間伝播しないが、差モード型結合 $\\sum_{\\{i,j\\}}g_{ij}|Z_i-Z_j|^2$ を加えるとグラフLaplacianと局所連続方程式が生じる。局所作用を規格化した $\\pi_i$ と辺の反対称確率流 $j_{ij}$ がR161への共通入力となる。対称活動量 $t_{ij}$ はこの代数だけから一意には決まらず、位置輸送の物理実現が別途供給する。\n\nこの意味で「Q1型局所構造＋Q2型相互作用」はQ3の空間信号と $(\\pi,j)$ を与えるが、Q1/Q2の測定装置そのものをQ3粒子へ流用するとは主張しない。Q3では実在粒子位置を測定結果形成とは別の因果鎖で扱う。\n",
)
replace_once(
    "sections/01_scope_and_cycle.md",
    "| M54 | 共通有効信号--配置状態構成族 | 有限実正準信号、準備済み入力境界、永続記憶部、作業領域、時計、記録の共通型。Q1/Q2はR191、Q3はR164--R161/R162へ接続する |",
    "| M54 | 共通有効信号--配置状態構成族 | 有限実正準信号、準備済み入力境界、永続記憶部、作業領域、時計、記録の共通型。Q1型局所信号とQ2型2体系結合の空間特殊化がQ3の $(\\pi,j)$ を与え、Q1/Q2測定はR191、Q3粒子位置はR164--R161/R162へ接続する |",
)
replace_once(
    "sections/01_scope_and_cycle.md",
    "| Q3 | M54空間状態構成、M37、R184 | R164開始配置、R161/R162輸送、R185 |",
    "| Q3 | M54空間状態構成（Q1型局所信号＋Q2型辺結合）、M37、R184 | R164開始配置、R161/R162輸送、R185 |",
)

# ---------------------------------------------------------------------------
# 2. Common modules: expose the Q1/Q2 -> spatial input and R161 equivalence.
# ---------------------------------------------------------------------------
regex_once(
    "sections/02_common_canonical_modules.md",
    r"^@status:.*$",
    "@status: M54をQ1・Q2・Q3の共通有効信号--配置状態構成族として定義する。初期状態方向は準備済み古典入力境界として扱い、R191をQ1/Q2の2結果射影読出し主線、R181B/R181Cを固定入力持上げ・永続ゲート、R181Dを射影結果成分受渡し、R192を一般深さQ2-4の方向不変作用安定化として分離する。R164はQ3開始配置の状態数起源、R161をQ3位置輸送の共通数学核、R162をその開放jump実現とし、Q1型局所信号とQ2型辺結合からR161の $(\\pi,j)$ が得られる構造を明示する。",
    flags=re.MULTILINE,
)
q1q2_to_q3 = r'''### 2.7.1 Q1/Q2局所構造からQ3空間信号への持ち上げ

R161へ渡す位置重みと確率流は、Q1/Q2と無関係な追加代数を仮定しなくても、同じ有限実正準信号の空間特殊化から得られる。有限配置グラフ $G_X=(\mathcal I,E_X)$ の各頂点 $i$ にQ1型の局所実正準モードを置き、

```math
Z_i
=\frac{Q_i+iP_i}{\sqrt{2\mathcal J_0}},
\qquad
R_i=|Z_i|^2,
\qquad
S=\sum_iR_i
```

とする。$S>0$ なら、正則化を省いた基本位置重みは

```math
\pi_i=\frac{R_i}{S}
```

である。R164の正則化を使う場合は $R_i$ を $R_i^\delta$ へ置き換える。

頂点間に結合がなければ全ハミルトニアンは局所項の和であり、異なる頂点間の作用輸送はない。従って独立なQ1型モードを空間に並べるだけでは $j_{ij}=0$ であり、Q3の空間伝播にはならない。

ここへQ2で用いるのと同じ有限2体系エルミート二次生成子の結合族を辺ごとに加える。代表的な差モード型結合は

```math
H_{\rm edge}
=\sum_{\{i,j\}\in E_X}g_{ij}|Z_i-Z_j|^2
```

であり、局所項を含めれば

```math
i\mathcal J_0\dot Z=hZ,
\qquad
h=gL_G+V
```

というグラフLaplacian型の空間信号を与える。一般のエルミート辺結合では、辺の作用流を

```math
J_{i\to j}
=\frac{2}{\mathcal J_0}
\operatorname{Im}
\left(Z_j^*h_{ji}Z_i\right),
\qquad
J_{i\to j}=-J_{j\to i}
```

とすると

```math
\dot R_i=\sum_jJ_{j\to i}.
```

従って $S$ が保存される区間では

```math
j_{ij}=\frac{J_{i\to j}}{S}
```

として

```math
\dot\pi_i=\sum_jj_{ji}
```

を得る。すなわち、Q1型局所作用が $\pi$、Q2型2体系結合が空間伝播と反対称流 $j$ を供給する。

ただし、この構造だけではR161の対称活動量 $t_{ij}=t_{ji}\geq|j_{ij}|$ は一意に決まらない。$t$ は位置輸送の物理実現が供給する独立の入力である。従って本稿でいうQ1/Q2からQ3への構造的接続は

```math
\text{Q1型局所信号}
+\text{Q2型辺結合}
\longrightarrow
(\pi,j),
\qquad
(\pi,j,t)
\xrightarrow{\mathrm{R161}}
X_t
```

を意味する。Q1/Q2のR191測定pointerを空間粒子へ同一視する主張ではない。

'''
replace_once(
    "sections/02_common_canonical_modules.md",
    "## 2.8 R161の共通整合とR162の開放jump実現\n",
    q1q2_to_q3 + "## 2.8 R161の共通整合とR162の開放jump実現\n",
)

activity_affinity = r'''### R161の活動量--親和力表示と実現同値

R161の各辺について $t_{ij}>|j_{ij}|$ とし、前向き・逆向きの確率流を

```math
q_{ij}^{+}
=\pi_i k^+_{i\to j}
=\frac{t_{ij}+j_{ij}}{2},
\qquad
q_{ij}^{-}
=\pi_j k^+_{j\to i}
=\frac{t_{ij}-j_{ij}}{2}
```

と置く。対称基準活動度と無次元親和力を

```math
c_{ij}
=\frac12\sqrt{t_{ij}^2-j_{ij}^2},
\qquad
\mathcal A_{ij}
=\log\frac{t_{ij}+j_{ij}}{t_{ij}-j_{ij}}
=2\operatorname{artanh}\frac{j_{ij}}{t_{ij}}
```

と定めると、厳密に

```math
q_{ij}^{\pm}
=c_{ij}e^{\pm\mathcal A_{ij}/2},
```

```math
t_{ij}
=2c_{ij}\cosh\frac{\mathcal A_{ij}}2,
\qquad
j_{ij}
=2c_{ij}\sinh\frac{\mathcal A_{ij}}2
```

である。従ってR161は、対称な遷移活動度 $c$ と反対称な非平衡親和力 $\mathcal A$ の表示へ等価に書き換えられる。境界 $t_{ij}=|j_{ij}|$ では $c\to0$、$|\mathcal A|\to\infty$ の極限表示となるため、有限量としては元の $(t,j)$ 表示を正本とする。

本稿では、同じ信号履歴と同じ初期粒子位置分布に対して2つのミクロ模型が同じ $\pi_i(t)$ と同じ有向率 $k_{i\to j}(t)$ を与えるとき、それらを **R161実現として厳密同値** と呼ぶ。物理自由度や存在論が同じことは要求しない。固定有限時間 $T$ 上で

```math
\varepsilon_{\rm gen}
=\sup_{0\leq t\leq T}
\max_i
\sum_{j\ne i}
\left|k^A_{i\to j}(t)-k^B_{i\to j}(t)\right|
```

なら、同じ初期分布から始めた周辺分布は

```math
\sup_{0\leq t\leq T}
D_{\rm TV}
\left(p_t^A,p_t^B\right)
\leq
T\varepsilon_{\rm gen}
```

を満たす。この生成子同値により、R161より前段のミクロ実現を交換しても、R162以降の位置過程とR185の縮約を共通に扱える。

'''
replace_once(
    "sections/02_common_canonical_modules.md",
    "<!-- theorem-start:theorem -->\n**定理（R162：局所有向率の開放Poisson-jump実現）**",
    activity_affinity + "<!-- theorem-start:theorem -->\n**定理（R162：局所有向率の開放Poisson-jump実現）**",
)

# ---------------------------------------------------------------------------
# K appendix: prove the equivalent representation and finite-time equivalence.
# ---------------------------------------------------------------------------
regex_once(
    "sections/A11_common_collision_bath_thermodynamics.md",
    r"^@status:.*$",
    "@status: R161の確率流・活動量整合、その活動量--親和力等価表示と生成子同値、R162の有界有向率に対する開放Poisson-jump実現を証明し、Q3位置輸送とR185の時間反転率へ接続する。静的詳細釣り合いは一般整合定理の特殊化としてのみ残す。",
    flags=re.MULTILINE,
)
k31 = r'''### K.3.1 活動量--親和力表示とR161実現同値

$t_{ij}>|j_{ij}|$ の辺を固定する。第2章の

```math
c_{ij}
=\frac12\sqrt{t_{ij}^2-j_{ij}^2},
\qquad
\mathcal A_{ij}
=\log\frac{t_{ij}+j_{ij}}{t_{ij}-j_{ij}}
```

から

```math
e^{\mathcal A_{ij}/2}
=\sqrt{\frac{t_{ij}+j_{ij}}{t_{ij}-j_{ij}}}
```

なので

```math
c_{ij}e^{\mathcal A_{ij}/2}
=\frac{t_{ij}+j_{ij}}2,
\qquad
c_{ij}e^{-\mathcal A_{ij}/2}
=\frac{t_{ij}-j_{ij}}2.
```

和と差を取れば

```math
t_{ij}
=2c_{ij}\cosh\frac{\mathcal A_{ij}}2,
\qquad
j_{ij}
=2c_{ij}\sinh\frac{\mathcal A_{ij}}2
```

を得る。従って $(t,j)$ と $(c,\mathcal A)$ は内部領域 $t>|j|$ で1対1であり、$t=|j|$ は一方向流の極限として回収される。

次に2つの時間依存生成子 $L_t^A,L_t^B$ が同じ有限配置集合上で

```math
\sup_{0\leq t\leq T}
\max_i\sum_{j\ne i}
|k^A_{i\to j}(t)-k^B_{i\to j}(t)|
\leq\varepsilon_{\rm gen}
```

を満たすとする。対角成分は各行の流出率の負なので、生成子差の各行の $\ell^1$ ノルムは $2\varepsilon_{\rm gen}$ 以下である。Duhamel公式とMarkov半群の全変動縮約性から、同じ初期分布に対して

```math
D_{\rm TV}(p_t^A,p_t^B)
\leq
\int_0^t\varepsilon_{\rm gen}\,ds
\leq
T\varepsilon_{\rm gen}.
```

特に有向率が一致すれば有限次元Markov経路法則も一致する。これはミクロ自由度の同一性ではなく、R161より下流で観測する位置過程の生成子同値である。

'''
replace_once(
    "sections/A11_common_collision_bath_thermodynamics.md",
    "### K.3.1 静的 詳細釣り合い特殊化\n",
    k31 + "### K.3.2 静的 詳細釣り合い特殊化\n",
)
replace_once(
    "sections/A11_common_collision_bath_thermodynamics.md",
    "### K.3.2 節点における静的再平衡化の障害\n",
    "### K.3.3 節点における静的再平衡化の障害\n",
)

# ---------------------------------------------------------------------------
# N appendix: make clear which pieces are fixed by signal dynamics and which
# are a choice of R161 activity.
# ---------------------------------------------------------------------------
regex_once(
    "sections/A14_m54_spatial_moving_matching.md",
    r"^@status:.*$",
    "@status: M54共通親模型の空間移動状態構成を定義し、Q1型局所正準信号とQ2型辺結合から得る $(\\pi,j)$ をR161へ接続する。現行 $T_{ij}^\\delta$ は許容される対称活動量の1選択として位置づけ、R184のM37開始作用保持機構実装とR185のNelson型前後平均微分・時間対称Newton則を証明する。局所有向率の開放jump実現は共通R162へ置く。",
    flags=re.MULTILINE,
)
replace_once(
    "sections/A14_m54_spatial_moving_matching.md",
    "有限グラフ $G=(V,E)$ 上でM54を $\\Lambda=\\mathcal I=V$、$\\Psi=I$ へ特殊化する。Q3で直接使う1試行状態断面を\n",
    "有限グラフ $G=(V,E)$ 上でM54を $\\Lambda=\\mathcal I=V$、$\\Psi=I$ へ特殊化する。この空間信号はQ1/Q2と別の正準代数ではなく、Q1型の局所実正準モードを頂点へ配置し、Q2で用いるのと同じ有限2体系エルミート結合族を辺へ反復した特殊化として読める。辺結合を切れば独立な局所モード列に戻り、空間確率流は消える。\n\nQ3で直接使う1試行状態断面を\n",
)
replace_once(
    "sections/A14_m54_spatial_moving_matching.md",
    "である。\n\n## N.3 R161移動特殊化\n",
    "である。ここで $J_{i\\to j}$ は信号Hamiltonianと局所連続方程式から固定されるが、$T_{ij}^\\delta$ はR161が許す対称活動量の1選択であり、連続方程式だけから一意には定まらない。規格化した $t_{ij}=T_{ij}^\\delta/[(1+\\delta)S]$ を別のミクロ模型が同じ有向率まで再現する場合、その模型は第2章の意味で同じR161実現となる。異なる許容活動量を採る場合もR161の一般定理自体は変わらない。\n\n## N.3 R161移動特殊化\n",
)

# ---------------------------------------------------------------------------
# M37 remains a backend, not the common mathematical core.
# ---------------------------------------------------------------------------
replace_once(
    "sections/06_m37_spatial_envelope.md",
    "M37はM54と並ぶ別の粒子親模型ではない。Q3ではM54空間信号部分系を局所位置ばねだけで有限時間近似する信号系実現模型であり、Q1ではR187の弱結合W型族に限って最低2正常モードをM54のW2静的状態構成の物理信号部分系として使う。役割を次のように分ける。\n",
    "M37はM54と並ぶ別の粒子親模型ではない。Q3ではM54空間信号部分系を局所位置ばねだけで有限時間近似する信号系実現模型であり、Q1ではR187の弱結合W型族に限って最低2正常モードをM54のW2静的状態構成の物理信号部分系として使う。従ってM37は、Q1型局所信号＋Q2型辺結合からR161入力 $(\\pi,j)$ へ進む共通構造の1つの空間担体実装であり、R161そのものの定義や活動量の一意性を担わない。役割を次のように分ける。\n",
)

# ---------------------------------------------------------------------------
# Conclusion: same separation of signal algebra and measurement causality.
# ---------------------------------------------------------------------------
regex_once(
    "sections/09_conclusion.md",
    r"^@status:.*$",
    "@status: M54/M37の現行階層、Q1型局所信号＋Q2型辺結合からQ3空間 $(\\pi,j)$ への接続、Q1/Q2のR191 2結果読出し、Q2-2の2端逐次R191、Q3のR164--R161/R162位置経路、R184--R185を総括する。",
    flags=re.MULTILINE,
)
replace_once(
    "sections/09_conclusion.md",
    "Q3は別の位置因果鎖を持つ。R164が開始面の実在粒子配置を準備し、R161が信号確率流と活動量から有向率を作り、R162が開放Poisson-jump過程として同じ粒子を輸送する。R185は同じ前向き経路法則のBayes反転から前進・後退平均微分と時間対称Newton則へ接続する。Q3の位置問題をQ1/Q2の測定pointerへ混ぜない。",
    "Q3の粒子位置はQ1/Q2の測定結果とは別の因果鎖を持つ一方、その信号数学は共通である。Q1型の局所正準モードを空間頂点へ配置し、Q2型の2体系結合を辺へ反復すると、局所作用から $\\pi$、連続方程式から反対称流 $j$ が得られる。対称活動量 $t$ を加えた $(\\pi,j,t)$ をR161の共通数学核へ渡し、R164が開始面の実在粒子位置を準備し、R162が開放Poisson-jump過程として同じ粒子を輸送する。R185は同じ前向き経路法則のBayes反転から前進・後退平均微分と時間対称Newton則へ接続する。Q1/Q2の測定pointerをQ3粒子へ同一視しない。",
)

# ---------------------------------------------------------------------------
# README: explain the structural unification without promoting a new micro model.
# ---------------------------------------------------------------------------
readme_q3 = r'''### 3. 空間を動く粒子

Q3の信号部分系はQ1/Q2と無関係な別の数理を導入するものではありません。Q1で使うものと同じ局所実正準モードを空間の各点へ並べるだけでは点同士の作用移送がないため、まだQ3にはなりません。そこへQ2で用いるのと同型の2体系エルミート結合を隣接点の間へ入れると、グラフLaplacian型のSchrödinger伝播と局所確率流が生じます。

各点の局所作用を

```math
R_i=|Z_i|^2,
\qquad
\pi_i=\frac{R_i}{\sum_kR_k}
```

とし、辺の信号流を

```math
J_{i\to j}
=\frac{2}{\mathcal J_0}
\operatorname{Im}(Z_j^*h_{ji}Z_i),
\qquad
j_{ij}=\frac{J_{i\to j}}{\sum_kR_k}
```

とすると、$\dot\pi_i=\sum_jj_{ji}$ です。したがって構造としては

```text
Q1型の局所正準信号
+ Q2型の隣接相互作用
        ↓
    (π, j)
+ 対称活動量 t
        ↓
      R161
        ↓
  1個の粒子位置 X_t
```

と整理できます。R161は $(\pi,j,t)$ から前向き・後向き遷移率を作り、R162が開放Poisson跳躍過程として同じ粒子を時間発展させます。開始位置の状態数起源はR164、同じ経路法則からの前進・後退平均微分と時間対称Newton則はR185が担います。

```math
Z_{t_0}
\xrightarrow{\mathrm{R164}}
X_{t_0}
\xrightarrow{\mathrm{R161/R162}}
X_T.
```

ここで対称活動量 $t$ はQ1/Q2の信号代数だけから一意には決まりません。その物理的起源はQ3のミクロ実現側の課題です。また、この整理はQ1/Q2のR191測定器を空間に並べた装置を自然界の実体として採用する主張ではありません。そのような空間化Q1模型は、同じR161生成子を作れることを見通す数学的な参照実現として扱います。

### 4. Q3のミクロ物理実現候補

現行Q3の正本はM54空間状態構成とR161/R162/R185です。これと同じR161生成子を、より具体的で自然な古典物理系から導く模型は別の研究課題として比較します。異なる内部自由度を持つ模型でも、同じ信号履歴に対して同じ $\pi$ と有向率を与えるなら、Q3の位置過程としては同じR161実現とみなせます。

M56はその候補の1つで、Q1のBrownian spinとQ3の粒子運動を同じ古典spin物理へ接続できるかを調べています。Q3粒子をbiaxial磁性体のdomain-wall中心 $X$ とし、理想的には

```math
dX_t
=\left[
\frac{\partial_xS}{m}
+\nu\partial_x\log\rho
\right]dt
+\sqrt{2\nu}\,dW_t
```

というNelson型拡散へ接続することを狙います。

現段階では必要な有限誤差bridgeが未証明なので、M56はR161/R162/R185を置換しません。模型、導出済み部分、未解決条件は [Brownian-spin Q3ミクロ実現候補](notes/brownian_spin_q1_q3_unification.md) に分けて記録しています。

'''
regex_once(
    "README.md",
    r"### 3\. 空間を動く粒子\n.*?(?=## 現在どこまでできているか)",
    readme_q3,
    flags=re.DOTALL,
)

# ---------------------------------------------------------------------------
# Status/changelog: no fixed-goal or achievement-label changes.
# ---------------------------------------------------------------------------
status_block = r'''## draft-94：R161共通数学核とQ1--Q3空間構造整理

- R161をQ3位置輸送の共通数学核として明示し、Q1型局所実正準信号を空間頂点へ配置し、Q2型2体系エルミート結合を辺へ反復するとQ3空間信号の $(\pi,j)$ が得られる構造を正本化する。
- 独立なQ1型モード列だけでは辺流がなくQ3にならないこと、対称活動量 $t$ は信号連続方程式から一意には決まらず位置輸送の物理実現が別途供給することを境界として明示する。
- R161の $(t,j)$ を対称基準活動度 $c$ と非平衡親和力 $\mathcal A$ へ厳密に書き換える等価表示と、同じ有向率を与えるミクロ模型をR161実現として同値とみなす規約を追加する。
- 空間化Q1＋Q2相互作用は数学的参照実現として扱い、M56などの具体模型は同じR161核のミクロ物理実現候補へ位置づける。新しいミクロHamiltonianは本改訂では採用しない。
- Q1--Q3の固定目標、達成ラベル、R161/R162/R184/R185の既存定理内容は変更しない。

'''
replace_once(
    "PROJECT_STATUS.md",
    "# 固定長期目標、現行モデル、現行結果\n\n",
    "# 固定長期目標、現行モデル、現行結果\n\n" + status_block,
)
changelog_block = r'''## draft-94：R161共通数学核とQ1--Q3空間構造整理

- Q1型局所正準モードを空間配置し、Q2型2体系結合を辺へ反復すると、Q3のSchrödinger型空間信号とR161入力 $(\pi,j)$ が得られる構造を第1・2・6章、概要、結論へ明示した。
- R161へ活動量--親和力等価表示を追加し、同じ有向率を与える異なるミクロ模型をR161実現として同値とみなす規約と、固定有限時間の生成子差から全変動距離への上界を付録Kへ追加した。
- 現行Q3の $T_{ij}^\delta$ はR161が許す対称活動量の1選択であり、$j$ と違って信号連続方程式だけから一意には決まらないことを付録Nへ明記した。
- 空間化Q1模型を数学的参照実現、M56をR161のミクロ物理実現候補として整理し直した。伝送線bath等の新しいミクロHamiltonian候補は正本へ入れていない。
- 固定目標、達成ラベル、R161/R162/R184/R185の既存主張は変更せず、README、状態表、研究メモ、検算、生成物を同期する。

'''
write("CHANGELOG.md", changelog_block + read("CHANGELOG.md"))

# ---------------------------------------------------------------------------
# Research note: keep micro-realization comparisons outside the paper.
# ---------------------------------------------------------------------------
note = r'''# R161を介したQ1--Q3実現同値の整理

## 1. 位置づけ

このメモは、Q1型局所自由度を空間に並べQ2型2体系相互作用を加える参照模型と、Q3の具体的な粒子・浴模型を、どの意味で「同じ」とみなすかを整理する。論文正本へ採用する新しいミクロHamiltonianはここでは固定しない。

現行Q3の数学的正本は

```text
signal dynamics
      ↓
   (π, j, t)
      ↓ R161
     k±
      ↓ R162
     X_t
      ↓ R185
Nelson / time-symmetric Newton
```

である。R161より前段だけをミクロ実現依存とし、R161以降は共通に保つ。

## 2. Q1/Q2から得る空間入力

各空間頂点にQ1型の局所実正準モードを置き、$R_i=|Z_i|^2$ とする。独立な局所モード列だけでは辺流がなく、空間伝播は生じない。

隣接頂点へQ2で用いるのと同じ有限2体系エルミート結合族を反復すると

```math
i\mathcal J_0\dot Z=hZ
```

となり、辺流

```math
J_{i\to j}
=\frac{2}{\mathcal J_0}
\operatorname{Im}(Z_j^*h_{ji}Z_i)
```

を得る。$S=\sum_iR_i$ が保存される区間では

```math
\pi_i=\frac{R_i}{S},
\qquad
j_{ij}=\frac{J_{i\to j}}{S},
\qquad
\dot\pi_i=\sum_jj_{ji}.
```

従ってQ1型局所作用が $\pi$、Q2型相互作用が空間伝播と反対称流 $j$ を供給する。ただし対称活動量 $t$ はこの代数だけから一意に決まらない。

## 3. 空間化Q1模型の役割

Q1のBorn型選択機構を各辺へ置き、Q2型の反対称流を局所的に重ねる模型は、適切な $(\pi,j,t)$ を作ればR161と同じ位置生成子を与える。これはQ1/Q2からQ3数学へ接続できることを露出した **参照実現** として有用である。

一方、この模型のpointer列やone-hot tokenを自然界の基礎的実体として採用する必要はない。数学的に同じR161生成子を、より通常の局在粒子と浴から作る模型を別に探索してよい。

## 4. R161実現同値

同じ信号履歴と同じ初期粒子位置分布に対し、2つの模型 $M_A,M_B$ が同じ $\pi_i(t)$ と同じ有向率 $k_{i\to j}(t)$ を与えるなら、R161実現として厳密同値とする。内部自由度、bath、pointer、粒子の具体的な担体が同じであることは要求しない。

固定有限時間 $T$ で

```math
\varepsilon_{\rm gen}
=\sup_{0\leq t\leq T}
\max_i\sum_{j\ne i}
|k^A_{i\to j}-k^B_{i\to j}|
```

なら

```math
\sup_{0\leq t\leq T}
D_{\rm TV}(p_t^A,p_t^B)
\leq T\varepsilon_{\rm gen}.
```

従って近似ミクロ模型も、生成子誤差を制御すれば同じR161/R162/R185下流へ接続できる。

## 5. 物理実現候補の比較規約

- 現行M54/R162開放jump模型：論文で採用する有効位置輸送実現。
- 空間化Q1＋Q2相互作用：Q1/Q2からR161へ到達できることを示す数学的参照実現。
- M56：spin系から同じQ3有効位置過程を得ることを狙うミクロ物理実現候補。
- その他の粒子・浴模型：同じ $(\pi,j,t)$ または同じ有向率を導けるかで比較する。

今後のミクロ模型では、Nelson縮約全体を毎回導き直すのでなく、まず

```text
micro model -> (π, j, t) -> R161
```

を証明する。ここが閉じればR162/R185は共通結果を再利用する。

## 6. 非主張

- Q1型モードを空間に並べるだけでQ3が自動的に得られるとは主張しない。Q2型の辺結合が必要である。
- Q1/Q2のR191測定pointerをQ3粒子と同一視しない。
- $(\pi,j)$ だけから対称活動量 $t$ が一意に決まるとは主張しない。
- 異なるミクロ模型が同じ生成子を持つことから、それらの存在論や熱力学的資源まで同じとは結論しない。
- M56やその他の候補を現行Q3-2の達成根拠へ昇格させない。
'''
write("notes/r161_q1_q2_q3_realization_equivalence.md", note)
replace_once(
    "notes/README.md",
    "| `brownian_spin_q1_q3_unification.md` |",
    "| `r161_q1_q2_q3_realization_equivalence.md` | draft-94のR161再整理 | Q1型局所信号＋Q2型辺結合からQ3の $(\\pi,j)$ を作り、異なるミクロ模型を同じR161生成子で比較する参照メモ | 数学的同値と物理的存在論を分離し、ミクロ模型を変更するたびにR162/R185を再導出しないため |\n| `brownian_spin_q1_q3_unification.md` |",
)
replace_once(
    "notes/README.md",
    "M56/R194A--R194E/R194H/R194Iの現役統合候補。active phase normalizer、2-action entropy shell、Brownian domain wallからNelson diffusionを狙う。relative-velocity magnon-dragは主線へ戻さない",
    "M56/R194A--R194E/R194H/R194IのR161ミクロ物理実現候補。spin signal、phase normalizer、2-action entropy shell、Brownian domain wallからNelson diffusionを狙う。relative-velocity magnon-dragは主線へ戻さない",
)
replace_once(
    "notes/brownian_spin_q1_q3_unification.md",
    "# M56 Brownian-spin Q1/Q3統合候補",
    "# M56 Brownian-spin Q3ミクロ実現候補",
)
replace_once(
    "notes/brownian_spin_q1_q3_unification.md",
    "M56は、Q1のR191ブラウン巨視的スピン読出しとQ3の空間粒子・Nelson型力学を、同じ古典spin物理で統合できるかを調べる現役研究候補である。現段階では論文正本へ昇格させず、`notes/` 内でR194A--R194E、R194H、R194Iを検討する。\n\n現行Q3-2の達成根拠はM54空間状態構成、R161、R162、R185のままとし、R162を退役しない。M37とR191の責務も変更しない。本メモの更新は固定目標、達成判定、`sections/`、`paper.md`、`main.tex`、`paper.pdf` を変更しない。",
    "M56は、Q1で実績のあるBrownian spin物理を手掛かりに、Q3の空間粒子・Nelson型力学を具体的な古典spin系から実現できるかを調べる研究候補である。draft-94以後、Q1--Q3の数学的統一そのものはR161の共通核とQ1型局所信号＋Q2型辺結合の空間構造で整理し、M56はその同じ有効位置生成子を担うミクロ物理実現候補として位置づける。現段階では論文正本へ昇格させず、`notes/` 内でR194A--R194E、R194H、R194Iを検討する。\n\n現行Q3-2の達成根拠はM54空間状態構成、R161、R162、R185のままとし、R162を退役しない。M37とR191の責務も変更しない。M56がR161実現同値まで閉じることは未証明であり、本メモの模型を現行Q3の存在論へ採用しない。",
)

# ---------------------------------------------------------------------------
# Verification: extend the existing spatial matching regression.
# ---------------------------------------------------------------------------
verify_anchor = '    check(np.max(np.abs(master - pdot)) < TOL, "R161 spatial moving matching")\n'
verify_insert = r'''    check(np.max(np.abs(master - pdot)) < TOL, "R161 spatial moving matching")

    # Q1-type local modes without off-diagonal pair coupling have no edge current.
    h_local = np.diag(np.linspace(-0.2, 0.2, n)).astype(complex)
    j_local = current(z, h_local)
    check(np.max(np.abs(j_local)) < TOL, "uncoupled Q1-type local modes carry no edge current")

    # R161 activity--affinity representation is algebraically identical on live edges.
    live = t > 1.0e-14
    c = np.zeros_like(t)
    affinity = np.zeros_like(t)
    c[live] = 0.5 * np.sqrt(t[live] ** 2 - j[live] ** 2)
    affinity[live] = np.log((t[live] + j[live]) / (t[live] - j[live]))
    qplus = 0.5 * (t + j)
    qminus = 0.5 * (t - j)
    rec_plus = np.zeros_like(t)
    rec_minus = np.zeros_like(t)
    rec_plus[live] = c[live] * np.exp(0.5 * affinity[live])
    rec_minus[live] = c[live] * np.exp(-0.5 * affinity[live])
    check(np.max(np.abs(rec_plus[live] - qplus[live])) < TOL, "R161 activity-affinity forward flux")
    check(np.max(np.abs(rec_minus[live] - qminus[live])) < TOL, "R161 activity-affinity reverse flux")
    check(
        np.max(np.abs(2.0 * c[live] * np.cosh(0.5 * affinity[live]) - t[live])) < TOL,
        "R161 activity reconstruction",
    )
    check(
        np.max(np.abs(2.0 * c[live] * np.sinh(0.5 * affinity[live]) - j[live])) < TOL,
        "R161 current reconstruction",
    )
'''
replace_once("tools/verify_m54_spatial_matching.py", verify_anchor, verify_insert)

# ---------------------------------------------------------------------------
# Manifest and validation record.
# ---------------------------------------------------------------------------
manifest_block = r'''## draft-94のR161共通数学核整理

- Q1型局所正準信号＋Q2型辺結合からQ3の $(\pi,j)$ へ接続する構造を第1・2・6章、付録K・N、概要、結論へ明示する。
- R161の活動量--親和力等価表示、生成子同値、固定有限時間の全変動距離上界を追加する。
- `notes/r161_q1_q2_q3_realization_equivalence.md` を追加し、空間化Q1模型、現行M54/R162、M56等を同じR161核の実現として比較する規約を保存する。
- `tools/verify_m54_spatial_matching.py` に無結合局所モードの零辺流と活動量--親和力恒等式の検算を追加する。
- `paper.md`、`main.tex`、`paper.pdf` は章別正本から再生成する。

'''
replace_once(
    "MANIFEST.md",
    "# 現行パッケージ一覧\n\n",
    "# 現行パッケージ一覧\n\n" + manifest_block,
)
replace_once(
    "MANIFEST.md",
    "- `notes/README.md`\n",
    "- `notes/README.md`\n- `notes/r161_q1_q2_q3_realization_equivalence.md`\n",
)
validation_block = r'''## draft-94：R161共通数学核とQ1--Q3空間構造整理

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

- `tools/verify_m54_spatial_matching.py` で、Q1型局所モードだけでは辺流が零であること、R161の $(t,j)$ と $(c,\mathcal A)$ が同じ前後確率流を与えること、活動量と確率流の逆変換を検査した。
- Q1型局所信号＋Q2型辺結合から $(\pi,j)$ を作る構造と、対称活動量 $t$ をミクロ実現側へ残す責務境界を本文・付録・README・研究メモで横断確認した。
- 固定目標と達成ラベルは変更していない。M56はQ1--Q3の数学的統一そのものではなく、R161のミクロ物理実現候補へ位置づけ直した。
- Actions run `__RUN_ID__` で上記検算と生成物同期を実行した。生成PDFはA4、__PDF_PAGES__ページである。

'''
write("VALIDATION.md", validation_block + read("VALIDATION.md"))

# Temporary bootstrap files remove themselves from the final branch.
for temporary in (
    ROOT / ".github/workflows/apply-r161-unification.yml",
    ROOT / "tools/apply_r161_unification_pr.py",
):
    if temporary.exists():
        temporary.unlink()

print("draft-94 R161/Q1-Q3 reorganization applied")
