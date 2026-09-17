@number: V
@chapter: 付録
@title: M60 chiral-medium transport reduction とR161有限誤差持上げ
@status: Q3のtransport縮約。M37/M54実正準空間信号から局所chiral作用を厳密に取り出し、M60二成分媒体のballistic lead、moving bath-frame carrier、平衡oscillator bath、局在tracerへ接続してR161生成子へ有限誤差で持ち上げる。独立dual ballistic TLはM60で退役し、R196A以降のmoving-reflector/GLE/FDT縮約は維持する。

## V.1 責務と実在自由度

本付録は独立したM57親模型を定義しない。Q3の共通親模型は付録WのM60であり、本付録はそのtransport sectorだけを縮約する。

単一試行でtransportに関与する実在自由度は、M37/M54の実正準空間信号、M60二成分chiral媒体のballistic lead、局所bath cellのcenter-of-mass座標 $Y_e$、その内部の平衡oscillator bath、1個のtracer座標 $X$、periodic/double-well potentialである。2-action state-count shellとnonlinear reservoir coreは付録WのR198A--R198Dが担当する。複素信号 $Z$ と媒体振幅 $b_{\sigma n}$ は実正準平面の派生表示であり独立実体ではない。

M60のchiral媒体はnonlinear coreとballistic leadを同じ $b_{\pm n}$ 自由度で実現する。R199Aがcore--lead有限時間分離とsignal portからincident energyへの接続を担当する。Brownian noiseとFDTはchiral媒体には課さず、$Y_e$ と共に並進する別の通常の平衡oscillator bathだけに適用する。

## V.2 R195A：chiral作用とsignal current恒等式

有限格子の辺 $e=\{i,j\}$ ごとに

```math
R_i=|Z_i|^2,
\qquad
C_{e,+}=\frac{Z_i-iZ_j}{\sqrt2},
\qquad
C_{e,-}=\frac{Z_i+iZ_j}{\sqrt2},
```

```math
I_{e,\pm}=|C_{e,\pm}|^2
```

と置く。直接計算から

```math
I_{e,+}+I_{e,-}=R_i+R_j,
```

```math
I_{e,+}-I_{e,-}=2\operatorname{Im}(Z_i^*Z_j)
```

が全信号振幅について厳密に成り立つ。nearest-neighbor Schrödinger特殊化で $\mathcal J_0=2m\nu$ とし、辺結合を $h_{ij}=-\mathcal J_0\nu/a^2$ と取る向き規約では

```math
J_{ij}^{\rm sig}=\frac{\nu}{a^2}(I_{e,+}-I_{e,-}).
```

edge chiralityを

```math
r_e=\frac{I_{e,+}-I_{e,-}}{I_{e,+}+I_{e,-}}
```

と定めると、signal edge velocityは

```math
u_{ij}^{\rm sig}
=\frac{2aJ_{ij}^{\rm sig}}{R_i+R_j}
=\frac{2\nu}{a}r_e
```

と厳密に書ける。従って後段の責務は $J/\rho$ を外部で計算することではなく、局所chiral作用として露出しているvelocityを実在bath frameとtracerへ受動的に伝えることである。

<!-- theorem-start:theorem -->
**定理（R195A：M37 chiral作用・signal current恒等式）**

上の定義の下で、chiral作用の和・差、$J_{ij}^{\rm sig}=\nu(I_+-I_-)/a^2$、$u_{ij}^{\rm sig}=2\nu r_e/a$ は厳密恒等式である。2-action state-countとGibbs平均力はM60付録WのR198A--R198D、R197Aが担当する。
<!-- theorem-end:theorem -->

## V.3 M60 ballistic leadからincident energyへ

M37 chiral modeとM60 leadのlocal passive portは付録Wで

```math
H_{37\chi}
=-\epsilon_p\sum_{e,\sigma}
\left[C_{e,\sigma}^*b_{\sigma,n(e)}+{\rm c.c.}\right]
```

と定義する。R199Aの狭帯域・弱非線形lead条件の下で、適切なport観測面のincident energy densityは

```math
e_{e,\sigma}(t)
=\kappa_p I_{e,\sigma}(t-\tau_p)
+\delta e_{e,\sigma}(t),
```

```math
\sup_{t\le T}|\delta e_{e,\sigma}(t)|
\le\varepsilon_{\rm lead}I_*
```

と書ける。$\varepsilon_{\rm lead}$ はband dispersion、core--lead interface、lead nonlinear phase、signal backreactionを含む。M60では独立のdual TLを別途導入しない。

## V.4 R196A：M60 ballistic leadからmoving bath velocityへの有限時間持上げ

二本のchiral leadは、局所bath cellのcenter-of-mass座標

```math
Y_e,
\qquad
U_e=\dot Y_e,
\qquad
M_e>0
```

が作る可動完全反射境界の左右へ入射する。$Y_e$ はservoや測定器ではなく、後段の平衡oscillator bathが共有する物理的bath-frame carrierである。

速度比

```math
\beta=\frac{U_e}{c},
\qquad |\beta|<1
```

とする。左から入射するenergy density $e_+$ と右から入射する $e_-$ に対するmoving boundary forceは

```math
F_{\rm bal}(\beta;e_+,e_-)
=2e_+\frac{1-\beta}{1+\beta}
-2e_-\frac{1+\beta}{1-\beta}.
```

```math
E=e_++e_->0,
\qquad
r=\frac{e_+-e_-}{e_++e_-}
```

と置くと

```math
F_{\rm bal}
=2E\frac{r(1+\beta^2)-2\beta}{1-\beta^2}.
```

$F_{\rm bal}=0$ の $|\beta|<1$ にある唯一の解は

```math
\beta_*(r)
=\frac{\sqrt{e_+}-\sqrt{e_-}}{\sqrt{e_+}+\sqrt{e_-}}
=\frac{r}{1+\sqrt{1-r^2}}.
```

また

```math
\frac{\partial F_{\rm bal}}{\partial U}
=-\frac4c
\left[
\frac{e_+}{(1+\beta)^2}
+\frac{e_-}{(1-\beta)^2}
\right]<0.
```

tracerからbath cellへの反作用を $f_{\rm load}$ として

```math
M_e\dot U_e=F_{\rm bal}(U_e/c;e_+,e_-)+f_{\rm load}(t)
```

とする。$E\ge E_{\min}>0$、$|r(t)|\le r_*<1$ なら、$U_*(t)=c\beta_*(r(t))$ に対し

```math
|U_e(t)-U_*(t)|
\le e^{-\lambda_Yt}|U_e(0)-U_*(0)|
+\frac{cL_*(r_*)}{\lambda_Y}\|\dot r\|_{\infty,[0,T]}
+\frac1{M_e}\int_0^t e^{-\lambda_Y(t-s)}|f_{\rm load}(s)|ds,
```

```math
\lambda_Y=\frac{E_{\min}}{M_ec}.
```

さらに

```math
\beta_*(r)-\frac r2
=\frac{r^3}{2[1+\sqrt{1-r^2}]^2},
```

従ってsmooth sector $r=O(a)$ では

```math
U_*(r)=\frac c2r+O(ca^3).
```

<!-- theorem-start:theorem -->
**定理（R196A：M60 ballistic leadからmoving bath velocityへの有限時間持上げ）**

R199Aのballistic lead条件、$E\ge E_{\min}>0$、$|r|\le r_*<1$ の下で、bath-frame carrierには唯一安定なinstantaneous terminal velocity $U_*=c\beta_*(r)$ が存在し、上の有限時間追従誤差で制御される。M60 coreのthermalizationやFDTを本定理には用いない。
<!-- theorem-end:theorem -->

## V.5 R196B：moving equilibrium bathからtracer GLE・Nelson driftへ

actual tracer $X$ はM60 chiral媒体そのものには熱化させず、$Y_e$ と共に並進する通常のequilibrium oscillator bathへ結合する。bath内部座標を $q_n$ とし、相対座標 $X-Y_e$ へ

```math
H_{\rm eq}
=\sum_n
\left[
\frac{p_n^2}{2m_n}
+\frac{m_n\omega_n^2}{2}
\left(
q_n-\frac{c_n}{m_n\omega_n^2}(X-Y_e)
\right)^2
\right]
```

で結合する。oscillator bathを厳密に消去すると

```math
M_X\ddot X
=-\partial_XV_{\rm eff}(X,Z)
-\int_0^t\Gamma(t-s)[\dot X(s)-\dot Y_e(s)]ds
+\xi(t)+r_{\rm init}(t),
```

```math
\langle\xi(t)\xi(s)\rangle=k_BT\,\Gamma(|t-s|)
```

を得る。FDTを適用しているのはbath cell内部の平衡oscillator bathだけである。

R197AとR198A--R198Dで同じ試行のshell/coreを消去すると、tracerへ作用する平均shell力は

```math
F_{\rm sh}(X,Z)
=k_BT[1-\Delta(x(A))]\partial_X\log R^\delta(X,Z)
```

となる。Ohmic/Markov極とoverdamped極で

```math
dX_t
=U_e(t)dt
+D_0\,\partial_x\log R^\delta(X_t,t)dt
-\mu V_{\rm per}'(X_t)dt
+\sqrt{2D_0}\,dW_t
+r_{\rm GLE}dt,
```

```math
D_0=\mu k_BT=\frac{k_BT}{\gamma_X}.
```

period $a$ の対称potentialに対するLifson--Jackson suppressionを

```math
g_K
=\frac1{\langle e^{\beta V_{\rm per}}\rangle_a
\langle e^{-\beta V_{\rm per}}\rangle_a}
```

とする。中心matchingを

```math
D_0=\frac\nu{g_K},
\qquad
g_Kc=\frac{4\nu}{a}
```

と置けば

```math
D_{\rm eff}=\nu+O(\varepsilon_{\rm hom}),
```

```math
g_KU_*(r)=\frac{2\nu}{a}r+O(a^2),
```

```math
b_{\rm osm}=\nu\partial_x\log R^\delta+O(\varepsilon_{\rm hom}),
```

従って

```math
b_+
=\frac j\rho+\nu\partial_x\log\rho
+O(a^2+\varepsilon_{\rm micro}).
```

<!-- theorem-start:theorem -->
**定理（R196B：moving equilibrium bathからNelson driftへの有限誤差縮約）**

R196Aのmoving bath-frame追従、明示oscillator bathのFDT、有限cutoff Markov極、overdamped極、periodic homogenizationの仮定の下で、tracerのeffective diffusion、current drift、osmotic driftは同じ $D_0=\nu/g_K$ と $g_Kc=4\nu/a$ によりそれぞれ $\nu$、$j/\rho+O(a^2)$、$\nu\partial_x\log\rho$ へ一致する。
<!-- theorem-end:theorem -->

## V.6 R196C：metastable well indexからR161生成子への持上げ

periodic/double-well landscapeのwell indexを有限格子位置として読む。moving bath velocity $U_e$ はoverdamped equationではconstant tilt force $f_e=\gamma_XU_e$ と等価であり、edge affinityは

```math
\mathcal A_e=\beta f_ea=\frac{aU_e}{D_0}.
```

理想trackingと中心matchingでは

```math
\mathcal A_e=4\beta_*(r_e)
=2r_e+\frac12r_e^3+O(r_e^5).
```

state-count free energyによってwell weightが $R_i^\delta$、symmetric saddle weightが

```math
R_b=\frac{R_i^\delta+R_j^\delta}{2}
```

となるsectorを用いる。zero-bias periodic homogenizationで $D_{\rm eff}=\nu$ に較正した同じlandscapeについて、対称well間の基準fluxを

```math
c_K=\frac{\nu R_b}{a^2}
```

と取ると、Eyring--Kramers/metastable reductionは

```math
q_{ij}^+=\frac{\nu R_b}{a^2}\exp(\mathcal A_e/2)[1+O(\varepsilon_{\rm EK})],
```

```math
q_{ij}^-=\frac{\nu R_b}{a^2}\exp(-\mathcal A_e/2)[1+O(\varepsilon_{\rm EK})].
```

従って

```math
k_{i\to j}^{60}
=\frac{q_{ij}^++q_{ij}^-+q_{ij}^+-q_{ij}^-}{2R_i^\delta}
```

はR161形式を持つ。$\delta=0$、$R_b=(R_i+R_j)/2$ ではnative current correctionはrelative $O(r_{ij}^2)=O(a^2)$ である。

有限時間生成子差を $\varepsilon_{60}^{\rm tr}$ とすると、node-free safe sectorで

```math
\varepsilon_{60}^{\rm tr}
\le C_{60}
\left(
\varepsilon_{86}
+\varepsilon_{\rm shell}^{60}
+\varepsilon_{\chi}
+\varepsilon_{\rm track}
+\varepsilon_{\rm load}
+\varepsilon_{\rm GLE}
+\varepsilon_{\rm od}
+\varepsilon_{\rm hom}
+\varepsilon_{\rm EK}
+a^2
\right).
```

<!-- theorem-start:theorem -->
**定理（R196C：M60 transportからR161への有限誤差持上げ）**

R195A、R199A、R196A--R196Bの仮定とmetastable well-index縮約の下で、M60 tracerのcoarse-grained位置生成子はR161形式へ持ち上がり、signal-current理想生成子との差は $\varepsilon_{60}^{\rm tr}$ で有限時間制御される。
<!-- theorem-end:theorem -->

## V.7 parameter windowと責務境界

必要な時間尺度窓は概念的に

```math
\tau_X\ll\tau_p,\lambda_Y^{-1}\ll T_{\rm sig},T_{\rm well},
```

```math
\tau_R\ll\tau_{\rm therm}\ll\tau_A
```

であり、さらにR199Aのlead dispersion、interface反射、lead nonlinearity、core driveが小さいことを要求する。`tools/verify_m57_ballistic_tracer.py` はR195A、R196A--R196Cの既存代数と時間尺度matchingを回帰検査し、M60固有のcore--lead条件は `tools/verify_q3_common_micro_model.py` が担当する。

R161/R162/R185の数学核は変更しない。R162はR161 lawのoptional Poisson realizationであり、M60の基礎的物理実体ではない。