@number: W
@chapter: 付録
@title: R207 Q2-2-S共通準備・受動分離候補
@status: R207A--R207DをQ2-2-Sのspatial-preparation candidateとして追加する。Q2-2 fixed-goalの現行R180C--M65/R181D証人、Q2-2達成ラベル、Q2-2-S未監査状態は変更しない。R207はM66/R205Eのthermal preparationとR205Fのpassive separationを使う候補であり、finite-speed spatial reservoir、direct SDE trajectory、loophole-free Bell実験の古典局所説明は主張しない。

## W.1 目的と因果境界

Q2-2-Sでは、現行R180Cの測定窓中AからBへの結果成分伝播とは別に、

common stochastic preparation、passive spatial separation、local setting latch、local outcomesの順

という候補経路を調べる。本付録ではBellの定理を回避または否定せず、候補模型においてどのBell前提が成立し、どの前提が成立しないかを明示する。

準備、分離、局所記録の順序は

```math
t_{\rm prep}
<
t_{\rm sep}
<
t_A^{\rm latch},t_B^{\rm latch}
<
t_A^{\rm out},t_B^{\rm out}
```

とする。ただしsetting precursor自体は準備窓に存在するため、後のlatchが測定設定独立性を回復するとは主張しない。

particle--reservoir couplingは準備時と分離後で切り替えない。A/B間相互作用と共通reservoirのcross-correlationだけが距離によって受動的に減衰する。

## W.2 continuous selectorとnear-contact Gibbs preparation

角度自由度を

```math
\theta_A,\theta_B\in\mathbb T
```

とし、setting precursorとして反射境界を持つ対称区間

```math
q_A,q_B\in[-q_{\max},q_{\max}]
```

上の双安定座標を置く。

```math
U_A(q_A)=a_A(q_A^2-q_0^2)^2,
\qquad
U_B(q_B)=a_B(q_B^2-q_0^2)^2,
```

```math
s(q)=\tanh(q/q_c).
```

粒子間距離を $R$ とし、

```math
H_{\rm prep}^{(R)}
=
U_A(q_A)+U_B(q_B)
-
K(R)\cos(\theta_A-\theta_B)
-
g\,s(q_A)\cos2\theta_A
-
g\,s(q_B)\sin2\theta_B
```

とする。$K(R)$ は固定constitutive lawであり、near-contactでは大きく、分離時には小さくなる。

M66/R205Eを

```math
w=1,
\qquad
H_{\rm cfg}=H_{\rm prep}^{(R)}
```

へ特殊化すれば、準備窓のreversible densityは

```math
p_{\rm prep}^{(R)}
=
\frac{
e^{-\beta H_{\rm prep}^{(R)}}
}{
Z_R
}
```

である。

setting sectorは

```math
\sigma_A=\operatorname{sgn}q_A,
\qquad
\sigma_B=\operatorname{sgn}q_B
```

とし、零集合 $q_Aq_B=0$ は無視する。記録bitは

```math
x=\frac{1-\sigma_A}{2},
\qquad
y=\frac{1-\sigma_B}{2}
```

とする。

### W.2.1 R207A：near-contact joint preparation

<!-- theorem-start:proposition -->
**命題（R207A：対称thermal joint preparationと公平setting sector）**

$U_A,U_B$ が偶関数、$s$ が奇関数であるとする。上のGibbs preparationでは4つのsetting sectorのpartition weightは等しく、

```math
P(\sigma_A,\sigma_B)
=
\frac14
```

である。従って

```math
P(x)=P(y)=\frac12,
\qquad
P(x,y)=P(x)P(y)=\frac14.
```

この結論はparticle--reservoir couplingのswitchを必要としない。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明（R207A）**

変換

```math
T_B:
(\theta_A,\theta_B,q_A,q_B)
\mapsto
(-\theta_A,-\theta_B,q_A,-q_B)
```

はmeasureを保存し、$H_{\rm prep}^{(R)}$ を不変に保ったまま $(\sigma_A,\sigma_B)$ を $(\sigma_A,-\sigma_B)$ へ写す。また

```math
T_{AB}:
(\theta_A,\theta_B,q_A,q_B)
\mapsto
\left(
\theta_A+\frac\pi2,
\theta_B+\frac\pi2,
-q_A,-q_B
\right)
```

もmeasureとHamiltonianを保存し、$(\sigma_A,\sigma_B)$ を $(-\sigma_A,-\sigma_B)$ へ写す。この二変換が4 sectorへ推移的に作用するため、sector partition weightは等しい。証明終。
<!-- theorem-end:proof -->

$g\neq0$ ではsource anglesとsetting precursorは一般に独立ではない。R207Bのdeep-well reductionはこのsource--setting dependenceを明示的に評価する。

準備後はdouble-well barrierにより

```math
T_{\rm sep}+T_{\rm meas}
\ll
\tau_{\rm flip}
```

を要求し、分離から局所setting recordまでsectorを保持する。これはbath couplingを切る操作ではなくmetastability条件である。

## W.3 deep-well / strong-lock CHSH witness

deep-well極で

```math
s(q_A)\simeq\sigma_A,
\qquad
s(q_B)\simeq\sigma_B
```

とし、さらにnear-contact strong-lock極

```math
\beta K\gg1
```

で

```math
\theta_A\simeq\theta_B\simeq\theta
```

とする。このとき

```math
p_\kappa(\theta\mid x,y)
\propto
\exp\!\left[
\kappa
\left(
\sigma_A(x)\cos2\theta
+
\sigma_B(y)\sin2\theta
\right)
\right],
\qquad
\kappa=\beta g,
```

```math
\sigma_A(0)=\sigma_B(0)=+1,
\qquad
\sigma_A(1)=\sigma_B(1)=-1.
```

標準4設定を

```math
\alpha_0=0,
\qquad
\alpha_1=\frac\pi2,
\qquad
\beta_0=\frac\pi4,
\qquad
\beta_1=-\frac\pi4
```

とし、局所応答を

```math
r
=
\operatorname{sgn}\cos(\theta_A-\alpha_x),
\qquad
s
=
-\operatorname{sgn}\cos(\theta_B-\beta_y)
```

とする。

### W.3.1 R207B：4-setting CHSH witness

<!-- theorem-start:proposition -->
**命題（R207B：strong-lock CHSH witnessの存在）**

strong-lock reductionでは対称性により

```math
E_{00}(\kappa)
=
E_{01}(\kappa)
=
E_{10}(\kappa)
=
-C(\kappa),
\qquad
E_{11}(\kappa)=C(\kappa),
```

従って

```math
|S(\kappa)|=4C(\kappa).
```

$C(\kappa)$ は連続で、

```math
C(0)=\frac12,
\qquad
\lim_{\kappa\to\infty}C(\kappa)=1.
```

従って少なくとも一つの有限 $\kappa_*>0$ が存在して

```math
|S(\kappa_*)|
=
2\sqrt2
```

を満たす。

さらに各 $(x,y)$ で

```math
P(r=\pm1\mid x,y)
=
P(s=\pm1\mid x,y)
=
\frac12
```

であり、4-setting observational marginalは非信号である。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明（R207B）**

4 conditional densityは角度の反転と $\pi/2$ 回転で互いに写り、指定したlocal responseも同じ変換で写るため4相関は表示の符号関係を持つ。$\kappa=0$ では一様角度積分から $C=1/2$。$\kappa\to\infty$ では各conditional densityが対応する二fold anisotropyの合成極小近傍へ集中し、指定したresponse productはほとんど確実に所定符号となるので $C\to1$。連続性と中間値の定理から $C=1/\sqrt2$ を与える有限 $\kappa_*$ が存在する。周辺については $\theta\mapsto\theta+\pi$ がdensityを保ち、各単独outcomeの符号を反転するため平均は零である。証明終。
<!-- theorem-end:proof -->

candidate quadratureでは

```math
\kappa_*
\simeq
0.368435
```

が得られる。これは解析命題の必要入力ではなく数値witnessである。

finite-lock deep-well reduction

```math
p(\theta_A,\theta_B\mid x,y)
\propto
\exp\!\left[
k\cos(\theta_A-\theta_B)
+
\gamma
\left(
\sigma_A\cos2\theta_A
+
\sigma_B\sin2\theta_B
\right)
\right]
```

でもcandidate quadratureにより、例えば

```math
k=5,
\qquad
\gamma\simeq0.562
```

の有限lockで $|S|=2\sqrt2$ のwitnessが得られる。continuous $q_A,q_B$ を含むfull SDE trajectoryの直接再現は本結果に含めない。

## W.4 passive separationとBell前提監査

準備後に $R$ を増やし、R205Fの条件

```math
K(R)\to0,
\qquad
C_{AB}(R)\to0
```

へ入るとする。local bath coupling、温度、local noise strengthは変更しない。

分離面でsource側hidden stateを

```math
\lambda_S
=
(\theta_A,\theta_B,\ldots)
```

とする。setting precursor $q_A,q_B$ は $x,y$ を生む局所自由度として分けて記述する。

### W.4.1 R207C：local response / measurement-dependence candidate

<!-- theorem-start:proposition -->
**命題（R207C：passive separation後のlocal responseとBell前提監査）**

R205Fのexact separation条件

```math
K(R)=0,
\qquad
C_{AB}(R)=0
```

が成立する分離面以後では、joint generatorは

```math
\mathcal L
=
\mathcal L_A+\mathcal L_B
```

へ分解する。local outcome lawを上の $r,s$ とすれば

```math
P(r,s\mid\lambda_S,x,y)
=
P_A(r\mid\lambda_A,x)
P_B(s\mid\lambda_B,y)
```

が成立する。

一方、R207Bの $\kappa>0$ witnessでは

```math
\rho(\lambda_S\mid x,y)
\neq
\rho(\lambda_S)
```

である。従って観測共同分布は

```math
P(r,s\mid x,y)
=
\int d\lambda_S\,
\rho(\lambda_S\mid x,y)
P_A(r\mid\lambda_A,x)
P_B(s\mid\lambda_B,y)
```

となり、Bell局所response factorizationと測定設定独立性を区別できる。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明（R207C）**

generator分解はR205Fのspecializationである。outcomeは分離後の各翼の角度と局所settingだけの関数なのでconditional responseは積分解する。$\kappa>0$ ではR207Bのconditional angle densityが $(x,y)$ に依存するため、source hidden-state distributionはsetting-independentではない。証明終。
<!-- theorem-end:proof -->

これは測定窓中のAからBへの通信を用いるR180Cとは異なる候補である。ただしR205Fはgenerator-level decouplingであり、有限最大伝播速度を持つ具体spatial reservoirをまだ与えない。従ってS2を主張するには別途

```math
t_A^{\rm out}-t_B^{\rm latch}
<
\frac{L}{v_{\max}},
\qquad
t_B^{\rm out}-t_A^{\rm latch}
<
\frac{L}{v_{\max}}
```

を満たすphysical implementationが必要である。本付録ではこのfinite-speed条件を未監査とする。

## W.5 Bell-local control

### W.5.1 R207D：measurement-independent local control

<!-- theorem-start:theorem -->
**定理（R207D：Bell-local CHSH control）**

同じlocal response lawについて、

```math
\rho(\lambda_S\mid x,y)
=
\rho(\lambda_S)
```

と

```math
P(r,s\mid\lambda_S,x,y)
=
P_A(r\mid\lambda_A,x)
P_B(s\mid\lambda_B,y)
```

を同時に課すなら、標準CHSH量は

```math
|S|\le2
```

を満たす。strong-lock reductionで $\kappa=0$ とするとsettingとsourceの相関が消え、同じ4 local responseに対して $|S|=2$ を回収する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R207D）**

固定 $\lambda_S$ に対する二値local responseのCHSH integrandは絶対値2以下である。setting-independentな同じ $\rho(\lambda_S)$ で平均すれば $|S|\le2$。$\kappa=0$ の一様角度分布では直接積分して $E_{00}=E_{01}=E_{10}=-1/2$、$E_{11}=1/2$ となり $|S|=2$。証明終。
<!-- theorem-end:proof -->

R207DはR207B/CでCHSH破れを支える前提差を対照化するcontrolであり、Q2-2 fixed-goalの新しい達成根拠ではない。

## W.6 Q2-2-S段階との対応と未完成点

| Q2-2-S段階 | R207候補の対応 | 本draftの状態 |
|---|---|---|
| S0 | 現行R180Cを基準系として維持 | 既存 |
| S1 | R207Aの二端joint preparationと分離protocol | candidate |
| S2 | R205F + R207Cのpost-separation local generator | finite-speed spatial microphysics未監査 |
| S3 | R207B/CのCHSH witnessとBell前提監査 | candidate。measurement dependenceを明示 |
| S4 | R207D | 解析controlあり |

従って本付録だけからQ2-2-Sを達成または部分達成へ更新しない。特に次は未完成である。

1. continuous $q_A,q_B$ を含むfull Langevin trajectoryでのdirect numerical reproduction。
2. 有限伝播速度を持つ具体spatial reservoirから $C_{AB}(R)$ を導くこと。
3. 分離・setting latch・local result固定を同じphysical timing modelで閉じること。
4. 実験装置、実験可能parameter、direct apparatus simulation。

S0--S4の定義と公式状態は `ENHANCEMENT_TARGETS.md` を正本とし、本文第5章5.7はその現在地を要約する。本付録のcandidate表現は独立の状態正本を作らない。
