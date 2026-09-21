@number: Y
@chapter: 付録
@title: M64 三実体・最小古典開放系Q3共通模型
@status: M60/M61をまだ置換しないpromotion-ready replacement candidate。古典coherent signal、classical tracer、signal-driven thermal reservoirの三実体だけを正本候補とし、R203A--R203Dでregularized density/current辞書、phase-volume free energy、初期準備、有限時間mean-flow tracking、canonical overdamped tracer、R161の1次元・有限graph接続、R185/R125受渡しを整理する。固定Q3-1/Q3-2達成判定とrequired主線は本更新だけでは切り替えない。

## Y.1 責務、三実体、二つのconfiguration profile

M64はQ3の位置過程を次の三つの古典的実体から構成する最小open model候補である。

1. classical coherent signal：M37型の実正準oscillator network。
2. classical tracer：一つの古典configuration variable。
3. signal-driven thermal reservoir：signal densityに応じて内部phase volumeが変わり、signal currentに応じたlocal mean flowを持ち、tracerへ摩擦・熱揺らぎまたは局所jump activityを与える一つの古典環境。

複素包絡 $Z$、density $\rho$、current $j$、reservoir mean flow $U$、density scaling $\lambda_\alpha$ は三実体から作る派生量またはcollective variableであり、独立した実体とはしない。

tracer configurationには二つの特殊化を許す。

- **continuous profile**：1次元位置 $X$ をcanonical overdamped Langevin SDEで発展させ、Q3-2、Q3-4Bの連続位置過程へ使う。
- **finite-graph profile**：有限配置graphの頂点 $X\in V$ をlocal reservoir jump lawで発展させ、Q3-4A、Q3-5の有限graph位置過程へ使う。

両profileは別の粒子実体を導入せず、同じsignal density/currentから同じphase-volume/current-reservoir責務を読むM64模型族の特殊化である。M64本体ではkink、domain wall、Duffing shell、PN well、Eyring--Kramers hoppingをtracerの定義に要求しない。

M64は採用open SDEまたはfinite-state jump lawを正本候補としてよい。single-field Hamiltonian化、finite-bath化、current transducerの完全Hamiltonian散乱導出、underdamped lift、metric-graph連続極は独立strengtheningとする。

## Y.2 regularized signal density/currentと局所補間

signal sectorはM37/R86を再利用する。固定有限時間で規格化signal density $\rho(x,t)$、current $j(x,t)$ が

```math
\partial_t\rho+\partial_xj=0,
\qquad
\rho\ge\rho_*>0
```

を満たすnode-free smooth sectorを取る。正の規格化背景 $q_0(x)$ と $\delta>0$ に対し

```math
\rho_\delta
=
\frac{\rho+\delta q_0}{1+\delta},
\qquad
J_\delta
=
\frac{j}{1+\delta},
```

```math
v_\delta
=
\frac{J_\delta}{\rho_\delta},
\qquad
u_\delta
=
\nu\partial_x\log\rho_\delta
```

と置く。従って

```math
\partial_t\rho_\delta+\partial_xJ_\delta=0.
```

離散signalでは各頂点の派生複素包絡を $Z_i$、全signal作用を

```math
S=\sum_i|Z_i|^2
```

とする。finite-graph profileでは固定 $q_i>0$、$\sum_iq_i=1$ に対し

```math
R_i^\delta
=
|Z_i|^2+\delta q_iS,
\qquad
\pi_i^\delta
=
\frac{R_i^\delta}{(1+\delta)S}
```

を正本のregularized位置重みとする。

continuous profileではtracer近傍を読む固定partition of unityを

```math
\chi_i(X)\ge0,
\qquad
\sum_i\chi_i(X)=1,
\qquad
\sum_i x_i\chi_i(X)=X
```

とし、各 $\chi_i$ の支持を $|x_i-X|\le C_\chi a$ に取る。nodal regularized density $r_i^\delta>0$ から

```math
r_X^\delta
=
r_*
\exp\left[
\sum_i
\chi_i(X)
\log\frac{r_i^\delta}{r_*}
\right]
```

を定める。

$g_\delta=\log\rho_\delta$ が $C^2$ で、$r_i^\delta$ が $\rho_\delta(x_i,t)$ と共通規格化まで一致するなら、一次再現性から

```math
\left|
\log r_X^\delta-\log\rho_\delta(X,t)-C(t)
\right|
\le
\frac12C_\chi^2a^2
\|\partial_x^2g_\delta\|_\infty
```

を得る。従って固定safe sectorで

```math
\left|
\partial_X\log r_X^\delta
-
\partial_X\log\rho_\delta
\right|
\le
\varepsilon_{\rho,1},
```

```math
D_{\rm TV}
\left(
\frac{r_X^\delta\,dX}{\int r_x^\delta dx},
\rho_\delta(X,t)\,dX
\right)
\le
\varepsilon_{\rho,0},
```

と書け、smooth linear-reproducing interpolationでは代表的に $\varepsilon_{\rho,0},\varepsilon_{\rho,1}=O(a^2)$ である。以下ではこの二つをdensity interpolation errorとして一度だけ数える。

## Y.3 R203A：regularized signal density/current dictionary

edge $e=(i,j)$ ごとに

```math
C_{e,+}
=
\frac{Z_i-iZ_j}{\sqrt2},
\qquad
C_{e,-}
=
\frac{Z_i+iZ_j}{\sqrt2},
```

```math
I_{e,\pm}=|C_{e,\pm}|^2
```

と置く。

<!-- theorem-start:theorem -->
**定理（R203A：M64 regularized signal density/current dictionary）**

上のedge変換について厳密に

```math
I_{e,+}+I_{e,-}
=
|Z_i|^2+|Z_j|^2,
```

```math
I_{e,+}-I_{e,-}
=
2\operatorname{Im}(Z_i^*Z_j)
```

が成立する。局所chiralityを

```math
r_e
=
\frac{
I_{e,+}-I_{e,-}
}{
I_{e,+}+I_{e,-}+\delta I_{0,e}
}
```

とする。regularization背景 $I_{0,e}$ をY.2の $\rho_\delta$ と同じ背景へ較正し、M37/R86のsafe narrow-band sectorを取ると、固定係数 $c_J$ に対して

```math
c_Jr_e
=
v_{\delta,e}
+
\Delta_{A,e},
```

```math
|\Delta_{A,e}|
\le
C_A
\left(
a^2+\varepsilon_{\rm env}
\right)
=
\varepsilon_A.
```

nearest-neighbor Schrödinger特殊化では $c_J=2\nu/a$ とできる。smooth sectorでは $r_e=O(a)$ なので $c_Jr_e=O(1)$ であり、$a\to0$ でmean-flow targetは発散しない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R203A）**

和・差恒等式は $C_{e,\pm}$ の定義を直接展開すれば得られる。nearest-neighbor smooth signalでは分子は中心差分currentに比例して $O(a)$、分母はregularized local densityに比例する。背景項をY.2の $\rho_\delta$ と同じ正則化へ較正すると、有限 $\delta$ の効果はtarget $v_\delta=J_\delta/\rho_\delta$ 自体へ吸収され、残る辞書誤差は中心差分とM37 envelope誤差である。証明終。
<!-- theorem-end:proof -->

一般finite graphではchirality近似を必須にせず、Hermitian signal generator $h$ の各辺で厳密なlocal current

```math
J_{i\to j}
=
\frac{2}{\mathcal J_0}
\operatorname{Im}
\left(
Z_j^*h_{ji}Z_i
\right),
\qquad
J_{i\to j}=-J_{j\to i}
```

をcurrent portとして使う。

## Y.4 R203B：phase-volume reservoir、initial preparation、finite-time flow tracking

reservoirの条件付き内部自由度を $(\zeta_\alpha,\Pi_\alpha)$ とし、固定signal、tracer位置、reservoir mean flowに対する内部Hamiltonianを

```math
H_{\rm res}
=
\sum_\alpha
\left[
\frac{
(\Pi_\alpha-m_\alpha U)^2
}{
2m_\alpha
}
+
\frac{
m_\alpha\omega_\alpha^2
}{2}
\left(
\lambda_\alpha\zeta_\alpha-d_\alpha R
\right)^2
\right]
```

とする。density scalingを

```math
\lambda_\alpha
=
\left(
\frac{r_X^\delta}{r_*}
\right)^{-w_\alpha},
\qquad
w_\alpha>0,
\qquad
\sum_\alpha w_\alpha=1
```

とする。

<!-- theorem-start:theorem -->
**定理（R203B：moving phase-volume reservoirのfree energyとflow分離）**

固定 $r_X^\delta>0$、$U$、$R$ に対して上のreservoirをcanonicalに積分すると、

```math
Z_{\rm res}(r_X^\delta,U,R)
=
Z_{\rm res}^0
\frac{r_X^\delta}{r_*}
```

が厳密に成立する。従って

```math
F_{\rm res}
=
-k_BT\log r_X^\delta+C_{\rm res},
```

```math
\partial_UF_{\rm res}
=
\partial_RF_{\rm res}
=
0,
```

```math
F_X^{\rm osm}
=
k_BT\,\partial_X\log r_X^\delta.
```

mean flow $U$ は運動量分布の平行移動としてphase-volume Jacobianを変えず、density scalingだけが座標積分のJacobianを変える。従ってdensity preparationとflow preparationは同じreservoir内で競合しない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R203B）**

各modeで $P_\alpha=\Pi_\alpha-m_\alpha U$、$Q_\alpha=\lambda_\alpha\zeta_\alpha-d_\alpha R$ と変数変換する。運動量側は平行移動、座標側は $d\zeta_\alpha=\lambda_\alpha^{-1}dQ_\alpha$ なので、Gaussian積分の依存性は

```math
\prod_\alpha\lambda_\alpha^{-1}
=
\frac{r_X^\delta}{r_*}
```

だけである。free energyとmean forceは $-k_BT\log Z_{\rm res}$ を微分して得る。証明終。
<!-- theorem-end:proof -->

### Y.4.1 initial tracer preparation

準備窓 $-T_{\rm prep}\le s\le0$ ではsignal densityを初期値へ固定し、reservoir flowのtracer輸送作用だけを切る。canonical overdamped preparation lawを

```math
dX_s
=
\nu
\partial_X\log r_0^\delta(X_s)\,ds
+
\sqrt{2\nu}\,dW_s
```

とする。そのFokker--Planck方程式は

```math
\partial_sp
=
\nu\partial_X
\left[
r_0^\delta
\partial_X
\left(
\frac{p}{r_0^\delta}
\right)
\right]
```

であり、周期境界または反射境界のcompact connected domainでは

```math
\pi_0^\delta(dX)
=
\frac{
r_0^\delta(X)\,dX
}{
\int r_0^\delta(x)\,dx
}
```

が可逆定常分布である。

weighted generatorのspectral gapを $\lambda_{\rm prep}>0$ とし、

```math
C_{\rm init}
=
\left\|
\frac{p_{-T_{\rm prep}}}{\pi_0^\delta}
-1
\right\|_{L^2(\pi_0^\delta)}
```

と置けば

```math
D_{\rm TV}
\left(
p_0,\pi_0^\delta
\right)
\le
\frac12
C_{\rm init}
e^{-\lambda_{\rm prep}T_{\rm prep}}.
```

Y.2の0階補間誤差と合成して

```math
D_{\rm TV}
\left(
p_0,\rho_{\delta,0}
\right)
\le
\varepsilon_{\rm prep}
:=
\frac12
C_{\rm init}
e^{-\lambda_{\rm prep}T_{\rm prep}}
+
\varepsilon_{\rho,0}.
```

従って初期Born型位置重みを外から標本化する必要はなく、R203Bのphase volumeと同じtracer dynamicsから有限時間で準備できる。

準備中、flow collective variable自体は下のtracking lawで初期値へ緩和させてよい。$\partial_UF_{\rm res}=0$ なのでflow momentum preparationは上のdensity weightを変えない。$t=0$ でsignal evolutionとflow-to-tracer couplingを同時にreleaseする。

### Y.4.2 finite-time mean-flow tracking

canonical M64のmean-flow lawを

```math
\tau_U\dot U_e
=
-U_e+c_Jr_e
```

とする。非零residual $R_{U,e}$ はfinite-bandwidth実装またはHamiltonian liftのstrengtheningで扱い、本体には入れない。

targetを $q_e=v_{\delta,e}$、errorを $E_e=U_e-q_e$ とするとR203Aから

```math
\tau_U\dot E_e
=
-E_e
+
\Delta_{A,e}
-
\tau_U\dot q_e.
```

従ってvariation of constantsにより

```math
|E_e(t)|
\le
e^{-t/\tau_U}|E_e(0)|
+
(1-e^{-t/\tau_U})
\left[
\varepsilon_A
+
\tau_UM_q
\right],
```

```math
M_q
=
\sup_{e,0\le s\le T}
|\partial_tv_{\delta,e}(s)|.
```

特にwell-prepared flow

```math
U_e(0)=c_Jr_e(0)
```

なら

```math
\sup_{0\le t\le T}
|U_e-v_{\delta,e}|
\le
\varepsilon_A+\tau_UM_q
=
\varepsilon_{\rm track}.
```

$c_J=O(a^{-1})$ でもsmooth sectorでは $r_e=O(a)$ なので、必要条件は $\tau_UM_q\ll1$ であり $\tau_U=o(a)$ ではない。

tracer位置のflow interpolationを

```math
U_X(X,t)
=
\sum_e
\chi_e^U(X)U_e(t)
```

とし、$\sum_e\chi_e^U=1$、$\sum_ex_e\chi_e^U=X$ を課すと、

```math
\left|
U_X-v_\delta(X,t)
\right|
\le
\varepsilon_{\rm track}
+
C_{\rm int}a^2
\|\partial_x^2v_\delta\|_\infty
=
\varepsilon_U.
```

## Y.5 R203C：canonical overdamped tracerとideal diffusionへの有限時間縮約

M64 continuous profileの正本は、constant $T$、constant frictionに対応するoverdamped open SDE

```math
dX_t
=
\left[
U_X(X_t,t)
+
\nu\partial_X\log r_{X_t}^\delta
\right]dt
+
\sqrt{2\nu}\,dW_t,
```

```math
\nu=\frac{k_BT}{\gamma_X}
```

とする。Itô規約を採用する。underdamped Langevin方程式とsmall-mass極はstrengtheningであり、固定主線の誤差項に入れない。

ideal regularized diffusionを

```math
d\bar X_t
=
\left[
v_\delta(\bar X_t,t)
+
u_\delta(\bar X_t,t)
\right]dt
+
\sqrt{2\nu}\,dW_t
```

とする。

<!-- theorem-start:theorem -->
**定理（R203C：M64 tracerのregularized diffusion縮約）**

固定有限時間で $\rho_\delta\ge\rho_{\delta,*}>0$ とし、

```math
b_\delta
=
v_\delta+u_\delta
```

が空間Lipschitzで定数 $L_b$ を持つとする。M64 drift errorを

```math
e_{64}
=
U_X-v_\delta
+
\nu
\left(
\partial_X\log r_X^\delta
-
\partial_X\log\rho_\delta
\right)
```

とすると

```math
\|e_{64}\|_\infty
\le
\varepsilon_U
+
\nu\varepsilon_{\rho,1}
=
\varepsilon_{\rm drift}^{64}.
```

ideal diffusionのFokker--Planck方程式には $p=\rho_\delta$ が厳密解として入り、同じBrownian motionを使うsynchronous couplingにより

```math
W_1
\left(
{\cal L}(X_t),
\rho_\delta(t)
\right)
\le
e^{L_bt}
W_1
\left(
{\cal L}(X_0),
\rho_{\delta,0}
\right)
+
\frac{
e^{L_bt}-1
}{
L_b
}
\varepsilon_{\rm drift}^{64}
```

が成立する。$L_b=0$ の場合は第2項を $t\varepsilon_{\rm drift}^{64}$ と読む。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R203C）**

ideal Fokker--Planck方程式で

```math
b_\delta\rho_\delta
-
\nu\partial_x\rho_\delta
=
v_\delta\rho_\delta
=
J_\delta
```

だから、$\partial_t\rho_\delta+\partial_xJ_\delta=0$ と一致する。

実過程とideal過程へ同じBrownian motionを入れ、$\Delta_t=X_t-\bar X_t$ とすると

```math
\frac{d}{dt}
\mathbb E|\Delta_t|
\le
L_b
\mathbb E|\Delta_t|
+
\varepsilon_{\rm drift}^{64}.
```

Gronwall評価と初期couplingの下限を取れば表示した $W_1$ boundを得る。証明終。
<!-- theorem-end:proof -->

①の準備を使えば初期項は $\varepsilon_{\rm prep}$ から制御できる。有限 $\tau_U$ の実M64 tracer自身について時間対称加速度まで直接比較する高階parabolic stabilityはstrengtheningとし、固定Q3-2では次節のcanonical R161 processへ受け渡す。

## Y.6 R203D：一般finite-graph R161 interface、1D finite volume、R185/R125接続

### Y.6.1 一般finite graph

有限signal graph $G=(V,E)$ で

```math
i\mathcal J_0\dot Z=hZ
```

とし、$h=h^\dagger$ とする。Y.2の $R_i^\delta$、$\pi_i^\delta$ とR203Aのexact edge current $J_{i\to j}$ を使う。各辺の対称activity numeratorを

```math
T_{ij}^\delta
=
\frac{|h_{ij}|}{\mathcal J_0}
\left(
R_i^\delta+R_j^\delta
\right)
```

と定める。

<!-- theorem-start:theorem -->
**定理（R203D：M64 finite-graph R161 interfaceと1D特殊化）**

任意の辺 $\{i,j\}$ で

```math
|J_{i\to j}|
\le
T_{ij}^\delta
```

が成立する。従ってlocal jump rates

```math
k_{i\to j}^{64,G}
=
\frac{
T_{ij}^\delta+J_{i\to j}
}{
2R_i^\delta
}
```

は非負であり、

```math
R_i^\delta k_{i\to j}^{64,G}
-
R_j^\delta k_{j\to i}^{64,G}
=
J_{i\to j}.
```

よって初期分布が $\pi^\delta(0)$ ならR161により全有限時刻で

```math
P(X_t=i)=\pi_i^\delta(t)
```

が厳密に成立する。rateは辺のlocal quantities $R_i^\delta,R_j^\delta,J_{ij}$ だけで書け、全位置分布をcontrollerへ入力しない。

1次元nearest-neighborで

```math
|h_{i,i+1}|
=
\frac{\mathcal J_0\nu}{a^2}
```

なら、正規化activityは

```math
t_{i+1/2}
=
\frac{\nu}{a^2}
\left(
\pi_i^\delta+\pi_{i+1}^\delta
\right),
```

となり、R185が用いるR161 activityと同一である。cell average表現を使えば前後平均速度とgeneratorはsmooth sectorでcontinuum regularized diffusionへ $O(a^2)$ で収束する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R203D）**

Cauchy--Schwarzと $2|Z_i||Z_j|\le|Z_i|^2+|Z_j|^2$ から

```math
|J_{i\to j}|
\le
\frac{|h_{ij}|}{\mathcal J_0}
\left(
|Z_i|^2+|Z_j|^2
\right)
\le
T_{ij}^\delta.
```

rate positivityとcurrent identityは定義を直接代入すれば得る。signal continuityにより $\dot R_i^\delta=\sum_jJ_{j\to i}$ なので、規格化後はR161 master equationそのものである。

1次元特殊化は $T^\delta$ を $(1+\delta)S$ で割れば表示したactivityになる。centered cell averageとedge currentのTaylor展開から、R203Dの従来の $v^{(a)},u^{(a)}$、generatorの $O(a^2)$ 収束が従う。証明終。
<!-- theorem-end:proof -->

### Y.6.2 R185への受渡し

1次元canonical discrete M64はR185と同じ

```math
\left(
\pi^\delta,
j^\delta,
t^\delta
\right)
```

を使う。従ってeffective R161 processではR185をそのまま適用し、

```math
\left\|
m
\frac12
\left(
D_+D_-+D_-D_+
\right)X
+
\partial_xV
\right\|_\infty
\le
m\|R_\delta\|_\infty
+
mC_{185,a}a^2
```

を得る。

ここでR203Cのmicro-to-effective reduction errorとR185のforce residualを単純加算しない。前者は

```math
\varepsilon_{\rm red}^{64}(T)
```

としてprocess-law metricで管理し、後者は

```math
\varepsilon_{\rm Newt}^{185}
=
m\|R_\delta\|_\infty
+
mC_{185,a}a^2
```

として力の誤差で管理する。有限 $\tau_U$ の実tracer自身の加速度誤差を直接評価するには位置密度の高階parabolic stabilityが必要であり、これはstrengtheningとする。

### Y.6.3 R125の2頂点再結合器

R125の2頂点graphで

```math
h_{\rm int}
=
\kappa
\left(
|L\rangle\langle R|
+
|R\rangle\langle L|
\right),
\qquad
q_L=q_R=\frac12
```

とする。R125のideal分布 $p_\phi$ に対してM64 regularized position lawは

```math
p_\phi^\delta
=
\frac{
p_\phi+\delta(1/2,1/2)
}{
1+\delta
}.
```

従って厳密に

```math
D_{\rm TV}
\left(
p_{\pi/2}^\delta,
p_{\rm mix}^\delta
\right)
=
\frac{1}{2(1+\delta)},
```

```math
D_{\rm TV}
\left(
p_{\pi/2}^\delta,
p_{-\pi/2}^\delta
\right)
=
\frac{1}{1+\delta}.
```

M64 graph transportと終位置readoutの各run誤差が $\varepsilon_{64,G}$ 以下なら、観測分布間距離はそれぞれ

```math
\frac{1}{2(1+\delta)}
-
2\varepsilon_{64,G},
```

```math
\frac{1}{1+\delta}
-
2\varepsilon_{64,G}
```

以上である。従って

```math
\varepsilon_{64,G}
<
\frac{1}{4(1+\delta)}
```

ならQ3-5のcoherent/mixed差と相対位相差はともに正に残る。

Q3-5固定目標はこの2頂点再結合器であり、metric graph、幾何学的2開口、junction PDE、多画素screenは本接続に要求しない。

## Y.7 誤差責務

M64では異なる次元・意味の誤差を一つの総和へ潰さない。

**準備誤差**

```math
\varepsilon_{\rm prep}
=
\frac12
C_{\rm init}
e^{-\lambda_{\rm prep}T_{\rm prep}}
+
\varepsilon_{\rho,0}.
```

**flow tracking**

```math
\varepsilon_{\rm track}
=
\varepsilon_A
+
\tau_UM_q,
```

```math
\varepsilon_U
=
\varepsilon_{\rm track}
+
C_{\rm int}a^2
\|\partial_x^2v_\delta\|_\infty.
```

**continuous micro-to-effective drift**

```math
\varepsilon_{\rm drift}^{64}
=
\varepsilon_U
+
\nu\varepsilon_{\rho,1}.
```

**finite-time process reduction**

```math
\varepsilon_{\rm red}^{64}(T)
=
e^{L_bT}
\varepsilon_{\rm prep}^{W_1}
+
\frac{
e^{L_bT}-1
}{
L_b
}
\varepsilon_{\rm drift}^{64}.
```

**R185 Newton residual**

```math
\varepsilon_{\rm Newt}^{185}
=
m\|R_\delta\|_\infty
+
mC_{185,a}a^2.
```

**finite-graph/readout error** $\varepsilon_{64,G}$ はgraph jump-law実装、初期分布、終位置recordの全変動誤差として別管理する。

$\delta$ はR203Aの辞書誤差として再加算せず、R185のregularizationとfinite-graph position lawに一度だけ入れる。Hamiltonian lift、finite bath、finite-bandwidth $R_U$、underdamped small-mass極はstrengthening用誤差として本台帳から分ける。

## Y.8 現行主線との責務境界

R203A--R203Dにより、M64のpromotion前に必要だった次の四つのbridgeを解析的に閉じる。

1. phase-volume reservoirからの有限時間initial tracer preparation。
2. $U\to v_\delta$ のfinite-time tracking bound。
3. canonical overdamped M64からR161/R185へのprocess reductionと二段誤差台帳。
4. R161 finite graphを介するR125/Q3-5の2頂点接続。

これによりM64は固定目標用のpromotion-ready replacement candidateとする。ただし本更新だけでは現行主線を切り替えず、

- M61/R200--M60/R198/R199/R196を現行Q3固定達成主線として維持する。
- Q3-1/Q3-2の固定達成ラベルを変更しない。
- M61/M60 required verifierを削除・降格しない。
- M60/M61の退役とM64 required昇格は独立promotion PRで行う。

A2 direct simulationは強化目標であり、固定目標用M64 promotionの必要条件とはしない。A1/A2の判定変更もpromotion auditで独立に行う。

direct A2ではM37 signal、preparation stage、mean-flow relaxation、canonical overdamped tracerを同一parameter setで直接積分・標本化し、$U-v_\delta$、osmotic mean force、経験位置密度、finite-volume/finite-graph R161 connectionを検査する。