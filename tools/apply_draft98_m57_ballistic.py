#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

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


def replace_regex_once(path: str, pattern: str, repl: str, flags: int = 0) -> None:
    text = read(path)
    new, count = re.subn(pattern, repl, text, count=1, flags=flags)
    if count != 1:
        raise AssertionError(f"{path}: regex occurrence count={count}: {pattern[:100]!r}")
    write(path, new)


def replace_between(path: str, start: str, end: str, body: str) -> None:
    text = read(path)
    i = text.find(start)
    if i < 0:
        raise AssertionError(f"{path}: start marker missing: {start!r}")
    j = text.find(end, i + len(start))
    if j < 0:
        raise AssertionError(f"{path}: end marker missing: {end!r}")
    write(path, text[:i] + body.rstrip() + "\n\n" + text[j:])


def prepend(path: str, block: str) -> None:
    text = read(path)
    if block.strip().splitlines()[0] in text:
        raise AssertionError(f"{path}: draft-98 block already present")
    write(path, block.rstrip() + "\n\n" + text)


# ---------------------------------------------------------------------------
# A22: preserve R195A; allocate fresh IDs R196A-C for the new ballistic chain.
# ---------------------------------------------------------------------------
path = "sections/A22_m57_dual_tl_tracer_microphysics.md"
text = read(path)
for old, new in (
    ("R195B以後の責務", "R196A以後の責務"),
    ("## V.4 R195B：", "## V.4 R196A："),
    ("**定理（R195B：", "**定理（R196A："),
    ("## V.5 R195C：", "## V.5 R196B："),
    ("**定理（R195C：", "**定理（R196B："),
    ("R195Bのmoving bath-frame追従", "R196Aのmoving bath-frame追従"),
    ("## V.6 R195D：", "## V.6 R196C："),
    ("**定理（R195D：", "**定理（R196C："),
    ("R195A--R195Cの仮定", "R195A、R196A--R196Bの仮定"),
    ("\\nu_{\\rm eff}=g_KU_e", "u_{\\rm eff}=g_KU_e"),
):
    if old not in text:
        raise AssertionError(f"A22 missing replacement token: {old}")
    text = text.replace(old, new)
# Make zero-bias activity calibration explicit before Eyring--Kramers flux.
old = "state-count free energyによってwell weightが $R_i^\\delta$、symmetric saddle weightが\n\n```math\nR_b=\\frac{R_i^\\delta+R_j^\\delta}{2}\n```\n\nとなるsectorで、Eyring--Kramers/metastable reductionは"
new = "state-count free energyによってwell weightが $R_i^\\delta$、symmetric saddle weightが\n\n```math\nR_b=\\frac{R_i^\\delta+R_j^\\delta}{2}\n```\n\nとなるsectorを用いる。zero-bias periodic homogenizationで $D_{\\rm eff}=\\nu$ に較正した同じlandscapeについて、対称well間のcoarse-grained基準fluxを\n\n```math\nc_K=\\frac{\\nu R_b}{a^2}\n```\n\nと定める。これは独立に挿入する率ではなく、R196Bの $D_{\\rm eff}=\\nu$ とsymmetric barrier weightをwell-index generatorへ書き直した基準activityである。その上でEyring--Kramers/metastable reductionは"
if old not in text:
    raise AssertionError("A22 zero-bias calibration insertion point missing")
text = text.replace(old, new, 1)
write(path, text)

# Verifier labels follow the fresh result IDs.
path = "tools/verify_m57_ballistic_tracer.py"
text = read(path).replace("# R195B:", "# R196A:").replace("# R195C", "# R196B").replace("# R195D", "# R196C")
write(path, text)

# ---------------------------------------------------------------------------
# README: replace the Q3 mechanism sections, not historical Q1/Q2 material.
# ---------------------------------------------------------------------------
replace_once(
    "README.md",
    "Q3の実在粒子輸送については、局在tracer、2作用状態数、左右独立open transmission lineを使うM57を現行ミクロ模型とします。",
    "Q3の実在粒子輸送については、局在tracer、2作用状態数、左右独立のballistic transmission line、moving bath-frame carrier、平衡oscillator bathを使うM57を現行ミクロ模型とします。",
)
readme_q3 = r'''### 3. 空間を動く粒子

Q3の信号部分系はQ1/Q2と無関係な別の数理を導入するものではありません。Q1で使うものと同じ局所実正準モードを空間の各点へ並べ、Q2で用いるのと同型の2体系エルミート結合を隣接点の間へ入れると、グラフLaplacian型のSchrödinger伝播と局所確率流が生じます。

各edge $e=\{i,j\}$ で

```math
C_{e,+}=\frac{Z_i-iZ_j}{\sqrt2},
\qquad
C_{e,-}=\frac{Z_i+iZ_j}{\sqrt2},
\qquad
I_{e,\pm}=|C_{e,\pm}|^2
```

と置くと、

```math
I_{e,+}+I_{e,-}=|Z_i|^2+|Z_j|^2,
\qquad
I_{e,+}-I_{e,-}=2\operatorname{Im}(Z_i^*Z_j)
```

が厳密に成り立ちます。Nelson関係 $\mathcal J_0=2m\nu$ の下では

```math
J_{ij}^{\rm sig}=\frac{\nu}{a^2}(I_+-I_-),
\qquad
u_{ij}^{\rm sig}=\frac{2\nu}{a}\frac{I_+-I_-}{I_++I_-}
```

となるため、signal currentを位相測定や外部除算で計算する必要はありません。

M57では $I_+$ と $I_-$ を二本の受動ballistic waveguideへtapし、局所bath cellの可動COM $Y_e$ の左右から入射させます。wave pressureの釣合いは

```math
\frac{U_e}{c}
=\beta_*(r)
=\frac{r}{1+\sqrt{1-r^2}},
\qquad
r=\frac{I_+-I_-}{I_++I_-}
```

という唯一安定なbath-frame速度を作ります。TL自体を熱化せず、drifting-Gibbsや非平衡FDTは使いません。

実在tracer $X$ は、この $Y_e$ と共に並進する通常の平衡oscillator bathへ結合します。Brownian noiseとFDTはこの平衡bathだけが担い、2作用状態数の自由エネルギーがosmotic driftを与えます。periodic potentialのhomogenizationに

```math
D_0=\frac{\nu}{g_K},
\qquad
g_Kc=\frac{4\nu}{a}
```

を課すと、coarse-grained diffusionは $\nu$、current driftは $j/\rho+O(a^2)$、osmotic driftは $\nu\partial_x\log\rho$ となります。

構造としては

```text
M37/M54の空間信号 Z
        ↓ R195A（currentはここで厳密）
   R, chiral I±
        ↓ R196A
 dual ballistic TL → moving bath frame U
        ↓ R196B
 equilibrium Brownian bath → tracer X_t
        ↓ R196C / R161
 ideal Q3位置生成子
        ↓ R185
Nelson / time-symmetric Newton
```

となります。R161は共通数学interface、R162はideal stochastic referenceとして残し、M57の基礎的物理実体とは扱いません。'''
replace_between("README.md", "### 3. 空間を動く粒子", "### 4. Q3のミクロ物理正本と代替研究線", readme_q3)
readme_q3canon = r'''### 4. Q3のミクロ物理正本と代替研究線

Q3の現行ミクロ物理正本はM57 dual-ballistic-TL moving-bath tracerです。R195Aがchiral作用から局所密度・signal current・2作用状態数を与え、R196Aがballistic wave pressureからmoving bath-frame velocityを有限時間で作ります。R196Bは平衡oscillator bathのGLE、FDT、periodic homogenizationからdiffusion・current drift・osmotic driftを同時に整合させ、R196Cがmetastable well-index processをR161生成子へ有限誤差で接続します。

旧draft-95のpinned/anharmonic TL、TL mixing、force-correlation time、drifting-Gibbs、TL自身へのFDTは現行M57から退役しました。M56 Brownian-spin模型はspin-onlyの別実現を探る代替研究線としてnotesに残します。'''
replace_between("README.md", "### 4. Q3のミクロ物理正本と代替研究線", "## 現在どこまでできているか", readme_q3canon)
replace_once(
    "README.md",
    "Q3では、M37/M54空間信号からM57 dual-TL tracerへ接続し、R161/R162/R185の共通数学核を通してSchrödinger型有効力学、Nelson型の時間対称Newton則、井戸型・調和型・W型の束縛状態、トンネル効果、2経路干渉まで進んでいます。位相量子化は未達です。",
    "Q3では、M37/M54空間信号からM57 dual-ballistic-TL moving-bath tracerへ接続し、R161/R162/R185の共通数学核を通してSchrödinger型有効力学、Nelson型の時間対称Newton則、井戸型・調和型・W型の束縛状態、トンネル効果、2経路干渉まで進んでいます。位相量子化は未達です。",
)

# ---------------------------------------------------------------------------
# Overview and scope causal chains.
# ---------------------------------------------------------------------------
overview_q3 = r'''Q3の信号部分系はQ1/Q2と別の代数ではない。Q1で使うものと同じ局所実正準モードを有限配置グラフの頂点へ置き、Q2で用いるのと同型の2体系エルミート結合を辺へ反復すると、グラフLaplacian型の空間伝播と反対称確率流が生じる。R195Aは各辺の信号をchiral作用 $I_\pm$ へ局所変換し、その和から局所密度、差からsignal currentとedge velocityを厳密に得る。2作用状態数は $\pi_i\propto|Z_i|^2$ とosmotic free energyを与える。

Q3の粒子位置形成・輸送はQ1/Q2の測定結果形成とは別の因果鎖である。

```math
Z
\xrightarrow{\mathrm{R195A}}
(R,I_+,I_-)
\xrightarrow{\mathrm{R196A}}
(R,U_{\rm bath})
\xrightarrow{\mathrm{R196B}}
X_t
\xrightarrow{\mathrm{R196C/R161}}
L_{\rm R161}
\xrightarrow{\mathrm{R185}}
\text{Nelson / time-symmetric Newton}.
```

R196Aではdual ballistic TLのwave pressureだけでmoving bath frameを作り、TL thermalizationやdrifting-Gibbsを仮定しない。R196Bでは別の平衡oscillator bathだけにFDTを適用し、periodic homogenizationを経て $D=\nu$、$j/\rho+O(a^2)$、$\nu\partial_x\log\rho$ を得る。R196Cはwell-index generatorをR161へ有限誤差で接続する。'''
replace_between("sections/00_overview_and_contents.md", "Q3の信号部分系はQ1/Q2と別の代数ではない。", "R162のopen Poisson-jump過程は", overview_q3)
replace_once(
    "sections/00_overview_and_contents.md",
    "Q3ではM57 dual-TL tracerを粒子輸送の現行ミクロ物理層とする。",
    "Q3ではM57 dual-ballistic-TL moving-bath tracerを粒子輸送の現行ミクロ物理層とする。",
)

scope_q3 = r'''M57は、この空間信号を一個の局在tracerへ接続する現行ミクロ物理層である。辺 $e=\{i,j\}$ ごとに

```math
C_{e,+}=\frac{Z_i-iZ_j}{\sqrt2},
\qquad
C_{e,-}=\frac{Z_i+iZ_j}{\sqrt2},
\qquad
I_{e,\pm}=|C_{e,\pm}|^2
```

を作る。R195Aにより局所密度、signal current、edge velocityはこのchiral作用から厳密に決まる。R196Aは二本のballistic TLをbath-cell COMへ入射して唯一安定なmoving frame $U_{\rm bath}$ を作り、R196Bはそのframeで通常の平衡oscillator bathへ結合したtracerをGLE/FDTとperiodic homogenizationで縮約する。R196Cはmetastable well-index processをR161へ持ち上げる。

```math
Z
\xrightarrow{\mathrm{R195A}}
(R,I_+,I_-)
\xrightarrow{\mathrm{R196A}}
(R,U_{\rm bath})
\xrightarrow{\mathrm{R196B}}
X_t
\xrightarrow{\mathrm{R196C/R161}}
L_{\rm R161}
\xrightarrow{\mathrm{R185}}
\text{Nelson / time-symmetric Newton}.
```
'''
replace_between("sections/01_scope_and_cycle.md", "M57は、この空間信号を一個の局在tracerへ接続する現行ミクロ物理層である。", "R162のopen Poisson-jump過程は", scope_q3)
replace_regex_once(
    "sections/01_scope_and_cycle.md",
    r"^\| M57 \| Q3粒子輸送ミクロ物理層 \|.*$",
    "| M57 | Q3粒子輸送ミクロ物理層 | 2作用状態数、dual ballistic TL、moving bath-frame carrier、平衡oscillator bath、局在tracer、periodic/double-well potentialからR195A・R196A--R196Cを介してR161生成子へ有限誤差で接続する |",
    re.MULTILINE,
)
replace_regex_once(
    "sections/01_scope_and_cycle.md",
    r"^\| Q3 \| M37/M54空間信号、M57 .*? \| R161/R162 ideal reference、R185時間対称Newton、R112終位置record \|$",
    "| Q3 | M37/M54空間信号、M57 dual-ballistic-TL moving-bath tracer、R195A・R196A--R196C | R161/R162 ideal reference、R185時間対称Newton、R112終位置record |",
    re.MULTILINE,
)
replace_once(
    "sections/01_scope_and_cycle.md",
    "Q3-2の達成根拠はM57/R195A--R195Dの明示TL-tracer縮約である。",
    "Q3-2の達成根拠はM57/R195A・R196A--R196Cの明示ballistic-TL/moving-bath/tracer縮約である。",
)

# Common-module and M37 tables.
replace_once(
    "sections/02_common_canonical_modules.md",
    "| Q3 | 空間信号＋局在tracer | 準備済み古典空間入力、M37＋M57 dual-TL tracer | R195A--R195D、R161、R185（R162はideal reference） |",
    "| Q3 | 空間信号＋局在tracer | 準備済み古典空間入力、M37＋M57 dual-ballistic-TL moving-bath tracer | R195A、R196A--R196C、R161、R185（R162はideal reference） |",
)
replace_once(
    "sections/06_m37_spatial_envelope.md",
    "| M54＋M57空間状態構成 | 実正準信号、局在tracer $X_t$、2作用sector、dual open TL | $Z$、$C_Z$、階数1状態方向、位置分布 | R195A--R195DによるR161実現、R185時間反転・Newton則 |",
    "| M54＋M57空間状態構成 | 実正準信号、局在tracer $X_t$、2作用sector、dual ballistic TL、moving bath-frame carrier、平衡oscillator bath | $Z$、$C_Z$、階数1状態方向、位置分布 | R195A・R196A--R196CによるR161実現、R185時間反転・Newton則 |",
)
replace_once(
    "sections/06_m37_spatial_envelope.md",
    "Q3-4A・Q3-4B・Q3-5では開始面から同じM57 tracer $X_t$ をR195D/R161で運ぶ。",
    "Q3-4A・Q3-4B・Q3-5では開始面から同じM57 tracer $X_t$ をR196C/R161で運ぶ。",
)

# ---------------------------------------------------------------------------
# Q3 chapter: update the operational M57 mechanism and finite conditions.
# ---------------------------------------------------------------------------
path = "sections/07_q3_finite_graph_phenomena.md"
text = read(path)
text = text.replace("M57/R195A--R195D", "M57/R195A・R196A--R196C")
text = text.replace("M57 dual-TL tracer", "M57 dual-ballistic-TL moving-bath tracer")
write(path, text)
q3_operational = r'''**運用状態。** Q3-2は達成である。M37/R86が古典実振動子からM54空間信号 $Z$ を有限時間で与える。R195Aはそのedge chiral作用から局所密度、signal current、signal edge velocityを厳密に取り出し、2作用状態数から位置重みとosmotic free energyを与える。R196Aは二本のballistic TLのwave pressureから局所bath-frame carrierの唯一安定な速度を有限時間で生成し、R196Bはそのmoving frameで平衡oscillator bathへ結合した同じtracerをGLE/FDTとperiodic homogenizationで縮約する。R196Cはcoarse-grained well-index generatorをideal R161 generatorへ有限誤差 $\varepsilon_{57}$ で持ち上げる。R162はideal R161率を実現する参照open-jump過程であり、Q3の基礎的ミクロ存在論とは扱わない。

R195Aのexact identityは

```math
I_++I_-=R_i+R_j,
\qquad
I_+-I_-=2\operatorname{Im}(Z_i^*Z_j),
```

```math
J_{ij}^{\rm sig}=\frac{\nu}{a^2}(I_+-I_-),
\qquad
u_{ij}^{\rm sig}=\frac{2\nu}{a}\frac{I_+-I_-}{I_++I_-}
```

である。R196Aのmoving-reflector fixed pointは

```math
\frac{U_*}{c}
=\beta_*(r)
=\frac{r}{1+\sqrt{1-r^2}},
\qquad
r=\frac{I_+-I_-}{I_++I_-},
```

で唯一安定である。R196BではTL自体をthermalizeせず、別の平衡oscillator bathだけにFDTを適用する。periodic homogenizationに

```math
D_0=\frac\nu{g_K},
\qquad
g_Kc=\frac{4\nu}{a}
```

を課すと、effective diffusionは $\nu$、current driftは $j/\rho+O(a^2)$、osmotic driftは $\nu\partial_x\log\rho$ となる。R196Cのaffinityは $\mathcal A_e=4\beta_*(r_e)$ で、metastable fluxからR161形式を得る。smooth sectorでsignal currentとの差はrelative $O(a^2)$ である。'''
replace_between(path, "**運用状態。** Q3-2は達成である。", "R161移動特殊化の条件付き分布を", q3_operational)
q3_close = r'''従って固定有限時間、1次元有限格子、node-free滑らかな部分系で、ballistic propagation、bath-frame tracking、equilibrium GLE、overdamped reduction、periodic homogenization、metastable well-index縮約の各有限誤差とR185の正則化・格子条件を順に制御すれば任意有限誤差へ閉じる。必要な時間尺度は代表的に

```math
\tau_X,\tau_p,\lambda_Y^{-1}\ll T_{\rm sig},T_{\rm well}
```

である。`tools/verify_m57_ballistic_tracer.py` はchiral恒等式、moving-reflector fixed pointと安定性、有限時間追従、weak-tap/loading scaling、$D_0=\nu/g_K$、$g_Kc=4\nu/a$、Lifson--Jackson suppression、新R161 current correctionの同時parameter windowが非空であることを検算する。'''
replace_between(path, "従って固定有限時間、1次元有限格子、node-free滑らかな部分系で、", "**非主張。**", q3_close)

# ---------------------------------------------------------------------------
# Error ledger: replace obsolete mixing/FDT-on-TL accounting.
# ---------------------------------------------------------------------------
replace_once(
    "sections/08_errors_resources_open_targets.md",
    "7. M57では同じM37/R86 carrier偏差を $\\varepsilon_{86}$ とport誤差へ二重に入れず、同じTL mixing偏差を $\\varepsilon_{\\rm mix}$、$\\varepsilon_{\\rm corr}$、$\\varepsilon_{\\rm FDT}$ へ重複加算しない。",
    "7. M57では同じM37/R86 carrier偏差を $\\varepsilon_{86}$ とballistic-port誤差へ二重に入れず、同じmoving-frame追従偏差を $\\varepsilon_{\\rm prop}$、$\\varepsilon_{\\rm track}$、$\\varepsilon_{\\rm load}$ へ重複加算しない。平衡bathのGLE/FDT誤差とperiodic homogenization誤差も導出箇所ごとに一度だけ数える。",
)
new_87 = r'''## 8.7 Q3のM57--R161--R185誤差

Q3の現行ミクロ物理層はballistic版M57である。R195Aでsignal currentまでをexactに取り出し、R196Aがmoving bath frame、R196Bが平衡Brownian tracer、R196Cがwell-index generatorからideal R161への有限時間matchingを担う。固定有限時間 $0\le t\le T$ で

```math
\varepsilon_{57}
=\sup_{t\le T}
\max_i\sum_{j\ne i}
|k_{i\to j}^{57}(t)-k_{i\to j}^{161}(t)|
```

とし、node-free safe sectorで

```math
\boxed{
\varepsilon_{57}
\le C_{57}\left[
\varepsilon_{86}
+\varepsilon_{\rm shell}
+\varepsilon_{\rm port}
+\varepsilon_{\rm prop}
+\varepsilon_{\rm track}
+\varepsilon_{\rm load}
+\varepsilon_{\rm GLE}
+\varepsilon_{\rm od}
+\varepsilon_{\rm hom}
+\varepsilon_{\rm EK}
+\varepsilon_{\rm back}
+a^2
\right].
}
```

ここで $\varepsilon_{86}$ はM37/M54 signal carrier、$\varepsilon_{\rm shell}$ は有限2作用殻、$\varepsilon_{\rm port}$ はchiral modeからballistic wave energyへの有限band coupling、$\varepsilon_{\rm prop}$ は伝播遅延・dispersion、$\varepsilon_{\rm track}$ はbath-frame carrierの有限追従、$\varepsilon_{\rm load}$ はtracerからcarrierへの反作用、$\varepsilon_{\rm GLE}$ は平衡oscillator bathからMarkov GLEへの縮約、$\varepsilon_{\rm od}$ は慣性消去、$\varepsilon_{\rm hom}$ はperiodic homogenization、$\varepsilon_{\rm EK}$ はmetastable well-index近似、$\varepsilon_{\rm back}$ はsignalへのpassive tap反作用である。最後の $a^2$ は $\mathcal A=4\beta_*(r)$ によるnative smooth-grid current correctionであり、finite-grid exact matchingを外部servoで作らない。

R161実現同値から

```math
\sup_{t\le T}
D_{\rm TV}(p_t^{57},p_t^{161})
\le T\varepsilon_{57}.
```

R185のnode-free 1次元有限格子評価へ渡すと

```math
\varepsilon_{Q3-2}
\leq
T\varepsilon_{57}
+
m\|R_\delta\|_\infty
+
mC_{185,a}a^2.
```

同じ $a^2$ がR196Cの物理generator matchingとR185有限差分に別の起源で現れるため係数を同一視せず、各導出箇所で一度だけ数える。R188の有限サンプリング加速度誤差は必要な場合だけ追加する。

現行M57の代表的fast-sector条件は

```math
\tau_p\ll T_{\rm sig},
\qquad
\lambda_Y^{-1}\ll T_{\rm sig},
\qquad
\tau_X=\frac{M_X}{\gamma_X}\ll T_{\rm sig},T_{\rm well},
```

である。中心matchingは

```math
D_0=\frac\nu{g_K},
\qquad
g_Kc=\frac{4\nu}{a}.
```

weak family

```math
\kappa_p,M_e=O(\epsilon^2),
\qquad
\gamma_X,k_BT=O(\epsilon^4),
\qquad
M_X=O(\epsilon^6)
```

ではtracking rateと $D_0$、$g_K$ を固定したままsignal backreactionとtracer loadingを $O(\epsilon^2)$ へ下げられる。条件を満たすwitnessを `tools/verify_m57_ballistic_tracer.py` で検査する。

旧draft-95の $\varepsilon_{\rm mix}$、$\varepsilon_{\rm corr}$、TLへの $\varepsilon_{\rm FDT}$ は現行M57の誤差台帳から削除する。旧R184の $\varepsilon_{184}$ は撤回しないがM57主線では使わない。R162はideal R161 jump referenceでありM57の基礎的bath誤差として数えない。'''
replace_between("sections/08_errors_resources_open_targets.md", "## 8.7 Q3のM57--R161--R185誤差", "## 8.8 静的分布の整合の正則化資源発散", new_87)
# Replace falsification-table row if present.
replace_regex_once(
    "sections/08_errors_resources_open_targets.md",
    r"^\| M57/R195A--R195D \|.*$",
    "| M57/R195A・R196A--R196C | chiral作用/current恒等式を満たさない、passive ballistic portの有限誤差境界が閉じない、moving-reflector fixed pointが一意安定でない、$\\tau_p$ または $\\lambda_Y^{-1}$ をsignal時間から分離できない、平衡bath GLE/overdamped/homogenizationが制御できない、weak-loading familyが空、またはR196Cのmetastable generatorがR161へ有限誤差で接続しない |",
    re.MULTILINE,
)

# ---------------------------------------------------------------------------
# Conclusion Q3 mechanism.
# ---------------------------------------------------------------------------
conclusion_q3 = r'''Q3の粒子位置はQ1/Q2の測定結果とは別の因果鎖を持つ一方、その信号数学は共通である。Q1型の局所正準モードを空間頂点へ配置し、Q2型の2体系結合を辺へ反復すると、局所作用から $\pi$、連続方程式から反対称流 $j$ が得られる。R195Aはさらにchiral作用の和・差からsignal currentとedge velocityを厳密に露出させる。

M57はこのsignalをdual ballistic TLへ弱くtapし、wave pressureで局所bath-cell COM $Y_e$ を受動的に動かす。R196Aの唯一安定fixed pointは

```math
\frac{U_*}{c}
=\frac{r}{1+\sqrt{1-r^2}},
\qquad
r=\frac{I_+-I_-}{I_++I_-}.
```

TL自体を熱化せず、drifting-Gibbsや非平衡FDTは仮定しない。actual tracer $X$ は $Y_e$ と共に並進する通常の平衡oscillator bathへ結合し、R196BでGLE/FDT、overdamped reduction、periodic homogenizationを行う。

```math
D_0=\frac\nu{g_K},
\qquad
g_Kc=\frac{4\nu}{a}
```

によりcoarse-grained diffusionは $\nu$、current driftは $j/\rho+O(a^2)$、2作用状態数由来のosmotic driftは $\nu\partial_x\log\rho$ へ一致する。R196Cはaffinity $\mathcal A=4\beta_*(r)$ を持つmetastable well-index generatorをR161形式へ写し、signal-current理想生成子との差を有限誤差 $\varepsilon_{57}$ で制御する。

従ってQ3の現行因果鎖は

```math
Z
\xrightarrow{\mathrm{R195A}}
(R,I_+,I_-)
\xrightarrow{\mathrm{R196A}}
(R,U_{\rm bath})
\xrightarrow{\mathrm{R196B}}
X_t
\xrightarrow{\mathrm{R196C/R161}}
L_{\rm R161}
\xrightarrow{\mathrm{R185}}
\text{Nelson / time-symmetric Newton}
```

である。'''
replace_between("sections/09_conclusion.md", "Q3の粒子位置はQ1/Q2の測定結果とは別の因果鎖を持つ一方、", "R162のopen Poisson-jump過程は", conclusion_q3)

# ---------------------------------------------------------------------------
# PROJECT_STATUS: new draft, active result IDs, Q3 row.
# ---------------------------------------------------------------------------
draft98_status = r'''## draft-98：M57をdual ballistic TL＋moving equilibrium bathへ置換

- draft-95のpinned/weakly-anharmonic TL、TL mixing、force-correlation、drifting-Gibbs、TL自身へのFDTをQ3正本から退役し、M57をdual ballistic waveguide、moving bath-frame carrier $Y_e$、平衡oscillator bath、局在tracer $X$ の構造へ置換する。
- R195Aはchiral作用和・差に加えて $J_{ij}^{\rm sig}=\nu(I_+-I_-)/a^2$ と $u_{ij}^{\rm sig}=2\nu r/a$ の厳密恒等式まで強化する。旧R195B--R195Dは結果IDを再利用せず退役し、新系列R196A--R196Cを採用する。
- R196Aはmoving-reflectorのexact ballistic force、唯一安定fixed point $U_*=c\beta_*(r)$、有限時間tracking、weak-tap/backreaction scalingを与える。R196Bはmoving equilibrium oscillator bathからGLE/FDT、overdamped reduction、periodic homogenization、weak-loading scalingを与える。R196Cは $\mathcal A=4\beta_*(r)$ のmetastable well-index generatorをR161へ有限誤差で持ち上げる。
- 中心matchingは $D_0=\nu/g_K$ と $g_Kc=4\nu/a$。TLをthermalizeせず、current drift、osmotic drift、diffusionをそれぞれballistic mechanics、state-count free energy、equilibrium bathへ責務分離する。
- `tools/verify_m57_ballistic_tracer.py` でchiral恒等式、moving-reflector fixed point・安定性・tracking、weak-tap/loading scaling、Lifson--Jackson suppression、新R161 current correctionと時間尺度windowを検算する。
- R161/R162/R185の数学核、Q1/Q2、固定目標の定義と既存達成ラベルは変更しない。Q3-2の達成根拠だけを新M57/R195A/R196A--R196Cへ差し替える。'''
prepend("PROJECT_STATUS.md", draft98_status)
old_rows = """| R195A | 厳密恒等式・条件付き状態数結果 | M57 edge signalのchiral作用和・差を局所密度とsignal currentへ対応させ、2作用shellから $\\Omega_i^\\delta\\propto R_i^\\delta$ を得る |
| R195B | 条件付き・明示誤差付き結果 | finite pinned dual open TLのport slaving、Lyapunov mixing rate、force-correlation time。closed momentum-conserving 1D FPUT鎖は対象外 |
| R195C | 条件付き・明示誤差付き結果 | Green--Kubo/FDTとperiodic-tracer縮約。$g_Kc=4\\nu/a$ で長時間diffusionとcurrent drift係数を同時matching |
| R195D | 条件付き・明示誤差付き結果 | M57 coarse-grained well-index processをR161形式へ写し、signal-current理想生成子との差を $\\varepsilon_{57}$ で有限時間制御。native current差はsmooth sectorで $O(a^2)$ |"""
new_rows = """| R195A | 厳密恒等式・条件付き状態数結果 | M57 edge signalのchiral作用和・差を局所密度とsignal currentへ対応させ、$J_{ij}^{\\rm sig}=\\nu(I_+-I_-)/a^2$、$u_{ij}^{\\rm sig}=2\\nu r/a$ を厳密に得る。2作用shellから $\\Omega_i^\\delta\\propto R_i^\\delta$ を得る |
| R196A | 厳密ballistic力学＋明示誤差付き結果 | passive dual ballistic port、moving-reflector force、唯一安定な $U_*=c\\beta_*(r)$、有限時間tracking、weak-tap/backreaction scaling |
| R196B | 条件付き・明示誤差付き結果 | moving equilibrium oscillator bathのGLE/FDT、overdamped reduction、periodic homogenization、$D_0=\\nu/g_K$ と $g_Kc=4\\nu/a$、weak-loading scaling |
| R196C | 条件付き・明示誤差付き結果 | affinity $\\mathcal A=4\\beta_*(r)$ のmetastable well-index processをR161へ有限誤差で持ち上げ、native signal-current差をsmooth sectorでrelative $O(a^2)$ に制御 |"""
replace_once("PROJECT_STATUS.md", old_rows, new_rows)
replace_regex_once(
    "PROJECT_STATUS.md",
    r"^\| Q3-2 \| 達成 \|.*$",
    "| Q3-2 | 達成 | M54空間信号＋M57粒子輸送 | M37実正準空間信号＋M57 dual-ballistic-TL moving-bath tracer | R195A exact current／R196A moving bath frame／R196B equilibrium GLE・homogenization／R196C R161 matching／Nelson縮約 | R195A、R196A--R196C、R161、R162、R185 | 固定有限時間・1次元有限格子・node-free滑らかな部分系で、M57生成子誤差 $\\varepsilon_{57}$ とR185の $O(\\delta)+C_{185,a}a^2$ を分離して時間対称Newton則へ接続。M37からclock/recordまでの全周期統合、連続空間一様極限、多粒子は強化課題 |",
    re.MULTILINE,
)
# Current-position Q3-4/5 result references use the new well-index lift.
text = read("PROJECT_STATUS.md")
lines = []
for line in text.splitlines():
    if line.startswith(("| Q3-4A |", "| Q3-4B |", "| Q3-5 |")) and "条件付き達成" in line:
        line = line.replace("R195D", "R196C")
    lines.append(line)
write("PROJECT_STATUS.md", "\n".join(lines) + ("\n" if text.endswith("\n") else ""))

# Enhancement target references are current, not historical.
path = "ENHANCEMENT_TARGETS.md"
text = read(path)
for qid in ("Q3-4A", "Q3-4B", "Q3-5"):
    pattern = rf"^(\| {re.escape(qid)} \|.*)R195D(.*)$"
    text, n = re.subn(pattern, r"\1R196C\2", text, count=1, flags=re.MULTILINE)
    if n != 1:
        raise AssertionError(f"{path}: failed to update {qid} R195D reference")
write(path, text)

# ---------------------------------------------------------------------------
# Manifest, validation, changelog.
# ---------------------------------------------------------------------------
draft98_manifest = r'''## draft-98のM57 ballistic moving-bath正本化

- draft-95のthermalizing dual-TL M57を置換し、dual ballistic TL、moving bath-frame carrier、平衡oscillator bath、局在tracerを現行Q3ミクロ物理層とする。
- R195Aをchiral current恒等式まで強化し、新結果R196A--R196Cを追加する。旧R195B--R195DはGit履歴・退役索引へ保存する。
- `sections/A22_m57_dual_tl_tracer_microphysics.md` を全面更新し、`tools/verify_m57_tl_tracer.py` を `tools/verify_m57_ballistic_tracer.py` へ置換する。
- README、PROJECT_STATUS、第0・1・2・6--9章、研究メモ、参考文献、生成物を新M57へ同期する。'''
prepend("MANIFEST.md", draft98_manifest)
# In the live package file list, replace the deleted verifier name. Historical draft-95 paragraph stays untouched.
replace_once("MANIFEST.md", "- `tools/verify_m57_tl_tracer.py`\n- `figures/README.md`", "- `tools/verify_m57_ballistic_tracer.py`\n- `figures/README.md`")

draft98_change = r'''## draft-98：M57をballistic TL＋moving equilibrium bathへ置換

- Q3のM57からpinned/anharmonic TL、TL mixing・force-correlation、drifting-Gibbs、TL自身へのFDTを退役し、dual ballistic waveguide＋moving bath-frame carrier＋平衡oscillator bathへ置換した。
- R195Aをsignal current velocity恒等式まで強化し、旧R195B--R195Dを退役。新R196Aでmoving-reflector fixed pointと有限tracking、新R196Bでequilibrium GLE/FDT・periodic homogenization・weak loading、新R196Cでmetastable well-indexからR161への有限誤差持上げを追加した。
- matchingを $D_0=\nu/g_K$ と $g_Kc=4\nu/a$ に整理し、current drift・osmotic drift・diffusionをballistic mechanics・state-count free energy・equilibrium bathへ分離した。
- `tools/verify_m57_ballistic_tracer.py` へ検算器を置換し、旧thermalizing-M57 verifierを削除した。固定目標と既存達成ラベル、R161/R162/R185数学核は変更しない。'''
prepend("CHANGELOG.md", draft98_change)

draft98_validation = r'''## draft-98：M57 ballistic moving-bath検算

- R195Aのchiral作用和・差、signal current、edge velocity恒等式を検査する。
- R196Aのmoving-reflector forceについて $\beta_*(r)$ fixed point、square-root表示、strict stability、force-slope下限、$\beta_*-r/2=O(r^3)$、時間依存chiralityへのGronwall追従を検査する。
- weak tapで $\kappa_p,M_e\propto\epsilon^2$ としたときtracking rateが消えないこと、R196Bの $\gamma_X,k_BT\propto\epsilon^4$、$M_X\propto\epsilon^6$ でoverdamped timeとloadingが小さくなることを検査する。
- $D_0=\nu/g_K$、$g_Kc=4\nu/a$、Lifson--Jackson barrier、$\tau_X\ll\tau_p\ll\tau_Y\ll T_{\rm sig}$、R196Cの $\mathcal A=4\beta_*(r)$、R161 traffic positivity、native current補正の $O(r^2)$ を `tools/verify_m57_ballistic_tracer.py` で再計算する。
- 通常の `tools/run_physics_checks.py`、原稿構造検査、論文再生成・同期検査を最終PR headで通す。'''
prepend("VALIDATION.md", draft98_validation)

# ---------------------------------------------------------------------------
# Notes: realization comparison and superseded M57 internals.
# ---------------------------------------------------------------------------
path = "notes/r161_q1_q2_q3_realization_equivalence.md"
text = read(path)
old = "- M57 dual-TL tracer：Q3で採用する現行ミクロ物理実現。2作用状態数が $\\pi$、左右TLとKramers activityが $(j,t)$ を供給する。"
new = "- M57 dual-ballistic-TL moving-bath tracer：Q3で採用する現行ミクロ物理実現。R195Aが局所密度とsignal currentをexactに与え、R196Aのballistic wave pressureがmoving bath velocity、R196Bの平衡bathとperiodic homogenizationがdiffusion・osmotic drift、R196Cのmetastable reductionがR161 activityを供給する。"
if old not in text:
    raise AssertionError("R161 realization note M57 bullet missing")
write(path, text.replace(old, new, 1))

superseded_replace = r'''## 2. 現行置換

draft-95でQ3の実在粒子輸送をopen-Poisson存在論からM57 dual-TL tracerへ移した。その最初のM57はpinned weakly-anharmonic open TLをthermalizeし、mixing、force correlation、drifting-Gibbs/FDTからtracer driftを作る構成だった。

draft-98ではこのthermalizing-TL内部機構も退役し、M57をdual ballistic TL＋moving bath-frame carrier＋平衡oscillator bathへ置換する。R195Aがchiral作用から局所密度・signal current・edge velocityを厳密に与え、R196Aがwave pressureからmoving bath frame、R196Bが平衡bathのGLE/FDTとperiodic homogenizationからtracer diffusion・drift、R196Cがmetastable well-index processからR161 generatorを与える。

R162は

```text
M57 microscopic tracer
        ↓ R196C finite-error matching
R161 ideal generator
        ↓ R162
ideal open-jump reference path
        ↓ R185/R188
Nelson / time-symmetric Newton
```

という比較用の数学的・確率過程的参照実現へ責務を下げたまま維持する。'''
replace_between("notes/superseded_q3_poisson_microphysics.md", "## 2. 現行置換", "## 3. 保持する結果", superseded_replace)
# Update retirement rationale paragraph to avoid describing old M57 as current.
replace_once(
    "notes/superseded_q3_poisson_microphysics.md",
    "旧open-Poisson模型は有効jump過程として数学的に明瞭だったが、粒子・bathのミクロ自由度、signal currentからdriftが生じる物理機構、diffusion係数の起源が抽象的だった。M57は局在tracer、2作用状態数、左右独立open TL、FDT/Kramers縮約を明示し、同じR161核へ有限誤差で接続するため、Q3固定目標が要求する「明示的な古典ミクロモデル」の物理層をこちらへ移す。",
    "旧open-Poisson模型は有効jump過程として数学的に明瞭だったが、粒子・bathのミクロ自由度、signal currentからdriftが生じる物理機構、diffusion係数の起源が抽象的だった。現行M57は局在tracer、2作用状態数、dual ballistic TL、moving bath-frame carrier、平衡oscillator bathを明示し、同じR161核へ有限誤差で接続するため、Q3固定目標が要求する『明示的な古典ミクロモデル』の物理層をこちらへ移す。",
)

# Add a dedicated superseded-formulation subsection without reusing result IDs.
path = "notes/superseded_result_index.md"
text = read(path)
marker = "退役は反証を意味しない。現在の固定目標と混同せず、必要な場合だけ独立研究線として再開する。\n"
if marker not in text:
    raise AssertionError("superseded index insertion marker missing")
block = r'''

### draft-95 M57 thermalizing-TL定式化

| 結果 | 旧用途 | 現行の扱い | 参照先 |
|---|---|---|---|
| R195B | pinned weakly-anharmonic dual open TLのslaving・mixing・force correlation | draft-98で退役。ballistic moving-reflector定理R196Aへ置換 | draft-95 Git履歴、付録V |
| R195C | drifting-Gibbs、TLへのGreen--Kubo/FDT、Kramers/Lifson--Jackson matching | draft-98で退役。moving equilibrium bath・GLE・homogenizationのR196Bへ置換 | draft-95 Git履歴、付録V |
| R195D | $A=2r$ のKramers fluxからR161へ持上げ | draft-98で退役。$A=4\beta_*(r)$ のmetastable lift R196Cへ置換 | draft-95 Git履歴、付録V |

R195Aのchiral作用・状態数恒等式は保持し、signal current velocityまで強化する。結果番号は再利用しない。
'''
write(path, text.replace(marker, marker + block, 1))

# ---------------------------------------------------------------------------
# References: add the new physical literature. Keep old refs as historical/useful background.
# ---------------------------------------------------------------------------
path = "sections/90_references.md"
text = read(path)
if "Interaction between a moving mirror and radiation pressure" not in text:
    text = text.rstrip() + "\n- [63] C. K. Law, ``Interaction between a Moving Mirror and Radiation Pressure: A Hamiltonian Formulation,'' Physical Review A 51, 2537--2541 (1995). <https://doi.org/10.1103/PhysRevA.51.2537>\n- [64] A. O. Caldeira and A. J. Leggett, ``Path Integral Approach to Quantum Brownian Motion,'' Physica A 121, 587--616 (1983). <https://doi.org/10.1016/0378-4371(83)90013-4>\n- [65] A. Bovier, M. Eckhoff, V. Gayrard, and M. Klein, ``Metastability in Reversible Diffusion Processes I: Sharp Asymptotics for Capacities and Exit Times,'' Journal of the European Mathematical Society 6, 399--424 (2004). <https://doi.org/10.4171/JEMS/14>\n- [66] P. Reimann, C. Van den Broeck, H. Linke, P. Hänggi, J. M. Rubí, and A. Pérez-Madrid, ``Diffusion in Tilted Periodic Potentials: Enhancement, Universality, and Scaling,'' Physical Review E 65, 031104 (2002). <https://doi.org/10.1103/PhysRevE.65.031104>\n"
write(path, text)

print("draft98_m57_ballistic_sync_ok")
