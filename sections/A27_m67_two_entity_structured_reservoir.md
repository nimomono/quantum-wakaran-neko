@number: AA
@chapter: 付録
@title: M67 二実体・構造化熱浴Hamiltonian統合候補
@status: M67/R208A--R208Dは、構造化熱浴と古典マーカーの二つの物理sectorだけからM64型Q3有効力学を回収する有限Hamiltonian candidateである。R209A--R209Cはlocal flow、finite bath、finite-time process metricを定量化し、M67->M64 compatibilityを明示誤差付きで強化する。現行Q3正本M37/R86 -> M64/R203A--R203D -> R161/R185は変更せず、M67はその上位parent候補として扱う。Q1/Q2/NBLへの拡張、M64/M66の退役、M0達成は本付録では主張しない。

## AA.1 目的、二実体、責務境界

M67は、M64で別実体としていたclassical coherent signalとsignal-driven thermal reservoirを一つの構造化熱浴へまとめる。単一試行の主要物理sectorは

```math
\mathcal R_{\rm str}
+
\mathcal X,
\qquad
\mathcal X=(X,P_X)
```

だけとする。$\mathcal R_{\rm str}$ は有限個の古典正準自由度からなる一つのHamiltonian媒体であり、内部にcoherent、phase-volume、flow、dragの各sectorを持つ。これらは別々の物理実体ではなく、同じ媒体の正準部分系またはreaction coordinateである。Q3では $\mathcal X$ をclassical tracerとして読む。

本付録の責務はM67からM64/R203A--R203Dのcontinuous Q3 lawへ有限時間で接続することである。R161/R185は既存の下流数学結果として再利用し、本付録では再証明しない。Q1のM65/R181D、Q2のM54/R181B--R181C、M66/R205--R207、NBL型registerは本付録の直接主張に含めない。

## AA.2 全Hamiltonianとcoherent sector

M67の有限Hamiltonianを

```math
H_{67}
=
H_{\rm coh}
+
H_{\rho}
+
H_U
+
H_{\rm drag}
+
H_X,
\qquad
H_X
=
\frac{P_X^2}{2M_X}
+
V_{\rm ext}(X)
```

とする。coherent sectorにはM37/R86の有限局所振動子網を使う。

```math
H_{\rm coh}
=
\sum_i
\left[
\frac{p_i^2}{2M_{\rm osc}}
+
\frac{M_{\rm osc}\omega_0^2q_i^2}{2}
+
\frac{\delta_iq_i^2}{2}
\right]
+
\frac12
\sum_{\{i,j\}}
\kappa_{ij}(q_i-q_j)^2.
```

回転包絡 $Z_i$ は $(q_i,p_i)$ の派生表示であり、safe narrow-band sectorでは

```math
i\mathcal J_0\dot Z
=
hZ
+
R_{\rm env},
\qquad
\|R_{\rm env}\|
\le
\varepsilon_{\rm env}.
```

regularized density/currentはR203Aと同じ

```math
R_i^\delta
=
|Z_i|^2+\delta q_iS,
\qquad
S=\sum_i|Z_i|^2,
```

```math
J_{i\to j}
=
\frac{2}{\mathcal J_0}
\operatorname{Im}
\left(
Z_j^*h_{ji}Z_i
\right)
```

を使う。

## AA.3 phase-volume sectorとsignal backreaction

M64/Y.2と同じcompact interpolationから正のlocal scale $r_X^\delta$ を作る。

```math
H_\rho
=
\sum_{\alpha=1}^{N_\rho}
\left[
\frac{\Pi_\alpha^2}{2m_\alpha}
+
\frac{m_\alpha\omega_\alpha^2}{2}
\lambda_\alpha(Z,X)^2\zeta_\alpha^2
\right],
```

```math
\lambda_\alpha
=
\left(
\frac{r_X^\delta}{r_*}
\right)^{-w_\alpha},
\qquad
w_\alpha>0,
\qquad
\sum_\alpha w_\alpha=1.
```

固定 $Z,X$ のcanonical積分は

```math
Z_\rho(Z,X)
=
Z_\rho^0
\frac{r_X^\delta}{r_*},
\qquad
F_\rho
=
-k_BT\log r_X^\delta+C_\rho
```

を与え、

```math
\left\langle
-\partial_XH_\rho
\right\rangle
=
k_BT\partial_X\log r_X^\delta.
```

equal weights $w_\alpha=1/N_\rho$ ならphase-volume force fluctuationは $O(N_\rho^{-1/2})$ で自己平均化する。

完全Hamiltonianではsignalへの反作用を消せない。$Z_i=\sqrt{N_0}z_i$ とすると、$r_X^\delta$ が $Z$ の二次量であることから

```math
\frac{\partial\log r_X^\delta}{\partial Z_i^*}
=
O(N_0^{-1/2}),
```

一方 $hZ=O(N_0^{1/2})$ なので、固定有限時間のrelative state-direction backreactionは

```math
\varepsilon_{\rm back}^{\rho}
=
O(N_0^{-1})
```

となる。

## AA.4 local flow reaction coordinate

各edge $e$ にR203Aのlocal current/densityからtarget velocity

```math
v_e[Z]
:=
c_Jr_e
=
v_{\delta,e}
+
\Delta_{A,e},
\qquad
|\Delta_{A,e}|
\le
\varepsilon_A
```

ここで $r_e$ と $c_J$ はR203Aと同じlocal current/density dictionaryであり、M67とM64は同じedge target $c_Jr_e$ を使う。

を定め、flow reaction coordinate $(U_e,P_{U,e})$ とmoving material-frame coordinate $(Y_e,P_{Y,e})$ を置く。

```math
H_U
=
\sum_e
\left[
\frac{P_{U,e}^2}{2I_e}
+
\frac{K_e}{2}
(U_e-v_e[Z])^2
+
\frac{P_{Y,e}^2}{2M_e}
+
P_{Y,e}U_e
\right]
+
H_{U{\rm bath}}.
```

$K_e>M_e$ とbounded $v_e$ のsafe sectorでは、平方完成によりquadratic sectorを下に有界に取れる。Hamilton方程式から

```math
\dot Y_e
=
U_e+\frac{P_{Y,e}}{M_e}.
```

finite harmonic flow bathを消去し、短memory・small-inertia極を取ると

```math
\tau_U\dot U_e
=
-U_e+v_e+R_{U,e}
```

となる。

## AA.5 local tight-frame moving bath

$U(X)$ をHamiltonianへ直接momentum shiftとして書かず、tracerとlocal material frameの相対座標だけを結合する。compact-supportのpartition

```math
\chi_e(X)\ge0,
\qquad
\sum_e\chi_e(X)=1,
\qquad
\sum_e x_e\chi_e(X)=X
```

continuous profileではさらにsecond momentを

```math
\sum_e
\chi_e(X)(x_e-X)^2
\le
C_\chi a^2
```

と仮定する。通常の局所linear hat partitionはこの条件を満たし、smooth $v_\delta$ の補間誤差を $O(a^2)$ にする。

を取り、advective channel $g_e=\chi_e$ と、重なるpair $e<f$ のstationary compensator

```math
g_{ef}
=
\sqrt{2\chi_e\chi_f}
```

を置く。すると

```math
\sum_e g_e^2+\sum_{e<f}g_{ef}^2=1.
```

各channel $c$ に $s_c'(X)=g_c(X)$ を取り、advective channelでは $\eta_e=Y_e$、compensatorでは $\eta_{ef}=0$ とする。

```math
H_{\rm drag}
=
\sum_{c,\mu}
\left[
\frac{p_{c\mu}^2}{2m_{c\mu}}
+
\frac{m_{c\mu}\omega_{c\mu}^2}{2}
\left[
q_{c\mu}
-
a_{c\mu}
\left(
s_c(X)-\eta_c
\right)
\right]^2
\right].
```

finite harmonic variablesを厳密に消去すると

```math
F_{\rm drag}^{(N)}(t)
=
\sum_cg_c(X_t)\xi_c^{(N)}(t)
-
\sum_cg_c(X_t)
\int_0^t
\Gamma_{c,N}(t-s)
\left[
g_c(X_s)V_s-\dot\eta_c(s)
\right]ds
+
R_{\rm slip}
```

を得る。条件付きcanonical preparationでは

```math
\left\langle
\xi_c^{(N)}(t)\xi_d^{(N)}(s)
\right\rangle
=
\delta_{cd}k_BT\Gamma_{c,N}(t-s).
```

short-memory、flow tracking、small recoilの極では

```math
F_{\rm drag}
=
-\gamma(V-U_X)+\xi_X+R_C,
\qquad
U_X=\sum_e\chi_eU_e,
```

となる。局所2-subchannel realizationとして、各edgeに

```math
g_{e,1}=\chi_e,
\qquad
g_{e,2}=\sqrt{\chi_e(1-\chi_e)}
```

を置き、第2channelをstationary compensatorとすることもできる。このとき

```math
\sum_{e,r}g_{e,r}^2=1
```

が厳密に成立し、同時にmean-flow項は $\sum_e\chi_eU_e$ のまま保たれる。

```math
\left\langle
\xi_X(t)\xi_X(t')
\right\rangle
=
2\gamma k_BT\delta(t-t')
```

となる。

## AA.6 finite-time window

finite bathの代表memory timeを $\tau_{\rm mem}$、recurrence timeを $T_{\rm rec}$ とする。M67の基本動作窓は

```math
\max
\left(
\tau_{\rm mem},
\tau_U,
M_X/\gamma,
\tau_{\rho,\rm mix}
\right)
\ll
T_{\rm obs}
\ll
\min
\left(
T_{\rm rec},
T_{\rm back}
\right).
```

永久不可逆性は要求せず、固定有限観測時間のprethermal Hamiltonian windowを使う。

## AA.7 R208A：二実体finite-Hamiltonian parent

<!-- theorem-start:theorem -->
**定理（R208A：M67二実体finite-Hamiltonian parent）**

M37/R86 safe coherent sector、$K_e>M_e$、正の有限harmonic-bath parameterを取り、$r_X^\delta$ と $v_e$ が固定観測窓で有界とする。このときM67の全自由度は

```math
\mathcal R_{\rm str}
+
(X,P_X)
```

の二つの主要物理sectorへ分類でき、$H_{67}$ は有限古典Hamiltonianとして構成できる。$Z,\rho,j,U,\xi$ はすべてM67正準自由度から作る派生量であり、新しい独立実体を必要としない。
<!-- theorem-end:theorem -->

## AA.8 R208B：osmotic forceと有限backreaction

<!-- theorem-start:theorem -->
**定理（R208B：phase-volume osmotic forceと有限backreaction）**

M67 phase-volume sectorについて

```math
Z_\rho
=
Z_\rho^0
\frac{r_X^\delta}{r_*},
\qquad
F_\rho
=
-k_BT\log r_X^\delta+C_\rho,
```

従って

```math
\left\langle F_X^\rho\right\rangle
=
k_BT\partial_X\log r_X^\delta.
```

equal weightsではphase-volume force fluctuationは $O(N_\rho^{-1/2})$、coherent action $Z=\sqrt{N_0}z$ に対する固定有限時間のrelative state-direction backreactionは $O(N_0^{-1})$ である。
<!-- theorem-end:theorem -->

## AA.9 R208C：local moving finite bath

<!-- theorem-start:theorem -->
**定理（R208C：local finite bathのrelative Langevin縮約）**

AA.5のlocal tight frameと条件付きcanonical finite bath preparationを用いると、finite harmonic variablesの消去からmemory forceとfinite-bath FDTを厳密に得る。short-memory、flow tracking、small moving-frame recoilの極では

```math
F_{\rm drag}
=
-\gamma(V-U_X)+\xi_X+R_C,
```

```math
\left\langle
\xi_X(t)\xi_X(t')
\right\rangle
=
2\gamma k_BT\delta(t-t')
```

となる。smooth sectorでは

```math
U_X
=
v_\delta(X,t)
+
O(
\varepsilon_A+
\varepsilon_U+
\varepsilon_{\rm int}+
\varepsilon_Y
).
```

finite-memory error、finite-spectrum error、recurrenceはAA.6の時間窓で別々に管理する。
<!-- theorem-end:theorem -->

## AA.10 R208D：M64への有限時間縮約

<!-- theorem-start:theorem -->
**定理（R208D：M67からM64 Q3 lawへの有限時間縮約）**

R208A--R208Cの条件に加え、$\rho_\delta\ge\rho_{\delta,*}>0$、必要な微分の有界性、AA.6の時間尺度分離を仮定する。M67 tracerをfast reservoir sectorについて縮約し、$M_X/\gamma\to0$ のoverdamped極を取ると、

```math
dX_t
=
\left[
\frac{J_\delta}{\rho_\delta}
+
\nu\partial_X\log\rho_\delta
\right]dt
+
\sqrt{2\nu}\,dW_t
+
R_{208}(t),
\qquad
\nu=\frac{k_BT}{\gamma}
```

を得る。総残差はcoherent envelope、density interpolation、$O(N_\rho^{-1/2})$ force fluctuation、flow tracking、moving-frame recoil、finite-memory、finite-spectrum、overdamped、$O(N_0^{-1})$ signal backreactionを別々に管理する。

ideal limitではM64/R203Cを回収し、同じ $\rho_\delta,J_\delta$ をR203Dへ渡せるため、R161/R185およびR124/R182/R125接続は既存結果を再利用できる。
<!-- theorem-end:theorem -->

R208DはM67からM64 lawへのstructural bridgeを与える。以下のR209A--R209Cは、同じ縮約をlocal-flow error、finite-bath error、process-law metricへ分解して定量化する。

## AA.11 R209A：local-flow / M64 mean-flow compatibility

<!-- theorem-start:theorem -->
**定理（R209A：M67 local-flow / M64 mean-flow compatibility）**

同じsignal $Z$ と同じedge target $v_e[Z]=c_Jr_e$ から作るcanonical M64 flow $U_e^{64}$ を

```math
\tau_U\dot U_e^{64}
=
-U_e^{64}+v_e[Z]
```

とする。M67 finite-Hamiltonian flow sectorのfast-bath平均を

```math
\tau_U\dot{\bar U}_e^{67}
=
-\bar U_e^{67}
+
v_e[Z]
+
R_{U,e}
```

とし、固定観測窓で $|R_{U,e}|\le\varepsilon_{H,U}$ とする。このとき

```math
\left|
\bar U_e^{67}(t)-U_e^{64}(t)
\right|
\le
e^{-t/\tau_U}
\left|
\bar U_e^{67}(0)-U_e^{64}(0)
\right|
+
(1-e^{-t/\tau_U})
\varepsilon_{H,U}.
```

特にsame-prepared flowでは

```math
\sup_{0\le t\le T}
\left|
\bar U_e^{67}-U_e^{64}
\right|
\le
\varepsilon_{H,U}.
```

moving material-frame velocityを

```math
\widetilde U_X^{67}
=
\sum_e\chi_e(X)\dot Y_e
```

とし、

```math
\varepsilon_Y
=
\sup_{X,t}
\left|
\sum_e
\chi_e(X)
\frac{P_{Y,e}}{M_e}
\right|
```

と置けば

```math
\left|
\widetilde U_X^{67}-U_X^{64}
\right|
\le
\varepsilon_{H,U}
+
\varepsilon_Y.
```

さらにR203A/R203Bの既存評価を使うと

```math
\left|
\widetilde U_X^{67}
-
v_\delta(X,t)
\right|
\le
\varepsilon_U^{64}
+
\varepsilon_{H,U}
+
\varepsilon_Y,
```

```math
\varepsilon_U^{64}
=
\varepsilon_A
+
\tau_UM_q
+
C_{\rm int}a^2
\|\partial_x^2v_\delta\|_\infty.
```

ここで $\varepsilon_U^{64}$ はM64自身のbaseline errorであり、M67->M64 compatibility errorへ再加算しない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R209A）**

$E_e=\bar U_e^{67}-U_e^{64}$ と置くと

```math
\tau_U\dot E_e=-E_e+R_{U,e}
```

なのでvariation of constantsで最初の評価を得る。$\dot Y_e=U_e+P_{Y,e}/M_e$ とpartition of unityからmaterial-frame boundが従う。最後の表示はR203Bのmean-flow trackingと一次再現partitionの $O(a^2)$ 補間評価との三角不等式である。証明終。
<!-- theorem-end:proof -->

## AA.12 R209B：finite harmonic bathの定量的Markov/FDT縮約

flow bathを各edgeで

```math
H_{U{\rm bath},e}
=
\sum_{\mu=1}^{N_U}
\left[
\frac{p_{e\mu}^2}{2m_{e\mu}}
+
\frac{m_{e\mu}\omega_{e\mu}^2}{2}
\left(
q_{e\mu}-a_{e\mu}U_e
\right)^2
\right]
```

と具体化する。条件付きcanonical preparationではinitial slipを消すことができる。

<!-- theorem-start:theorem -->
**定理（R209B：finite harmonic bathの定量的Markov/FDT縮約）**

上のflow bathを厳密に消去すると

```math
I_e\ddot U_e
+
K_e(U_e-v_e)
+
P_{Y,e}
+
\int_0^t
\Gamma^U_{e,N}(t-s)\dot U_e(s)\,ds
=
\xi^U_{e,N}(t),
```

```math
\Gamma^U_{e,N}(t)
=
\sum_\mu
m_{e\mu}\omega_{e\mu}^2a_{e\mu}^2
\cos(\omega_{e\mu}t),
```

```math
\left\langle
\xi^U_{e,N}(t)
\xi^U_{f,N}(s)
\right\rangle
=
\delta_{ef}k_BT
\Gamma^U_{e,N}(t-s)
```

を得る。target Drude kernelを

```math
\Gamma_D^U(t)
=
\frac{\gamma_U}{\theta_U}
e^{-t/\theta_U},
\qquad
\tau_U=\frac{\gamma_U}{K_e}
```

とし、

```math
\varepsilon_{\Gamma,U}(T)
=
\int_0^T
\left|
\Gamma^U_{e,N}(t)-\Gamma_D^U(t)
\right|dt
```

と置く。$A_U=\sup|\ddot U_e|$、$V_U=\sup|\dot U_e|$ とすれば、fast-bath mean equationのdeterministic residualは

```math
\varepsilon_{H,U}^{\rm det}
\le
\frac{I_e}{K_e}A_U
+
\frac{P_{Y,*}}{K_e}
+
\tau_U\theta_UA_U
+
\frac{\varepsilon_{\Gamma,U}(T)}{K_e}V_U.
```

thermal widthは

```math
\varepsilon_{U,{\rm th}}
=
\sup_{e,t}
\left(
\mathbb E
|U_e-\bar U_e|^2
\right)^{1/2}
```

として別に管理する。

drag channelについて $h_c=g_c(X)V-\dot\eta_c$ と置き、target Drude kernel $\Gamma_D^X(t)=\gamma\theta_X^{-1}e^{-t/\theta_X}$ を使う。$\omega_h(r)$ を $h_c$ の共通modulus of continuity、$H_*=\sup|h_c|$、

```math
\varepsilon_{\Gamma,X}(T)
=
\max_c
\int_0^T
|\Gamma_{c,N}(t)-\Gamma_D^X(t)|dt
```

とするとdeterministic drag residualは

```math
|R_C^{\rm det}|
\le
C_g\gamma
\int_0^\infty
\frac{e^{-r/\theta_X}}{\theta_X}
\omega_h(r)\,dr
+
C_gH_*
\varepsilon_{\Gamma,X}(T)
+
\gamma\varepsilon_Y.
```

特に $h_c$ がLipschitzで定数 $L_h$ を持てば第1項は $C_g\gamma\theta_XL_h$ 以下である。

finite-bath noiseを積分した

```math
B_N(t)
=
\int_0^t\xi_N(s)\,ds
```

はGaussian過程であり、kernel covarianceがDrude kernelへ一様積分収束し、increment boundが一様なら、固定 $T<T_{\rm rec}$ で

```math
\mathcal L(B_N)
\Longrightarrow
\mathcal L
\left(
\sqrt{2\gamma k_BT}\,W
\right)
\quad
\text{on }C[0,T].
```

さらにtight-frame identity $\sum_cg_c^2=1$ から

```math
\sum_cg_cg_c'
=
\frac12\partial_X\sum_cg_c^2
=
0,
```

したがってcolored-noiseのwhite-noise極で生じるStratonovich correctionは0であり、M64のItô noiseへ余分なdriftなしで接続する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R209B）**

harmonic bathの線形方程式をDuhamel表示して $q_{e\mu}$ を消去すればmemory kernelとFDTを得る。Drude convolutionについて

```math
\left|
(\Gamma_D*f)(t)-\gamma f(t)
\right|
\le
\gamma
\int_0^\infty
\frac{e^{-r/\theta}}{\theta}
|f(t-r)-f(t)|dr
```

を用い、finite-spectrum差には $L^1$ kernel normを使えば表示したresidual boundが従う。Gaussian noiseの有限次元分布はcovariance収束から従い、一様increment boundからtightnessを得る。最後のStratonovich correctionはtight-frame identityの微分で消える。証明終。
<!-- theorem-end:proof -->

Drude kernelは

```math
\Gamma_D(t)
=
\frac{2\gamma}{\pi}
\int_0^\infty
\frac{\cos(\omega t)}
{1+(\omega\theta)^2}
d\omega
```

と書けるため、有限harmonic bathで固定有限時間上任意精度に離散近似できる。周波数刻み $\Delta\omega$ に対するrecurrence timeは $T_{\rm rec}\sim2\pi/\Delta\omega$ であり、PR2では $T_{\rm obs}<T_{\rm rec}$ を明示的に要求する。

## AA.13 R209C：M67->M64 finite-time process compatibility

<!-- theorem-start:theorem -->
**定理（R209C：M67からM64への有限時間process compatibility）**

固定 $0\le t\le T$ で $\rho_\delta\ge\rho_{\delta,*}>0$、必要なsignal/flow微分が有界で、canonical M64 driftが空間Lipschitzとする。R209A/R209Bの条件を満たし、同じ初期signalから作るM67 tracer $X^{67}$ とcanonical M64 tracer $X^{64}$ を比較する。

finite-bath Markov化誤差を $\varepsilon_{\rm bath}(T)$、初期compatibility errorを $\varepsilon_{\rm init}^{67\to64}$、signal state-direction errorを

```math
\varepsilon_{\rm sig}(T)
=
\sup_{t\le T}
d_{\rm ray}
\left(
Z^{67}(t),Z^{37}(t)
\right)
```

とする。regularized safe sectorでobservable mapがLipschitzで定数 $L_{\rm sig}$ を持つとする。

Markov化後のunderdamped tracerについて

```math
dX_t^M=V_t^Mdt,
```

```math
M_XdV_t^M
=
-\gamma
\left[
V_t^M-b_{64}(X_t^M,t)
\right]dt
+
\sqrt{2\gamma k_BT}\,dW_t
```

とし、$\epsilon_M=M_X/\gamma$ とする。$|b_{64}|\le B_*$ かつMaxwell-prepared velocityなら、synchronous couplingで

```math
\varepsilon_{\rm od}(T)
\le
C_T
\left[
\epsilon_MB_*
+
\sqrt{\nu\epsilon_M}
\right]
```

となる有限定数 $C_T$ が存在する。従ってM67固有のprocess compatibility errorを

```math
\varepsilon_{67\to64}(T)
=
\varepsilon_{\rm bath}(T)
+
\varepsilon_{\rm od}(T)
+
\varepsilon_{H,U}^{\rm det}
+
\varepsilon_Y
+
\varepsilon_{U,{\rm th}}
+
\varepsilon_{\rho,{\rm fluc}}(T)
+
L_{\rm sig}
\varepsilon_{\rm sig}(T)
+
\varepsilon_{\rm init}^{67\to64}
```

とすれば、固定有限時間で

```math
\sup_{0\le t\le T}
W_1
\left(
\mathcal L(X_t^{67}),
\mathcal L(X_t^{64})
\right)
\le
C_T'
\varepsilon_{67\to64}(T)
```

となる有限定数 $C_T'$ が存在する。

ここで $\varepsilon_A$、$\tau_UM_q$、$a^2$ flow interpolation、$\nu\varepsilon_{\rho,1}$ はM64自身のR203C baseline errorなので $\varepsilon_{67\to64}$ へ再加算しない。

さらに既存R203Cを用いれば

```math
W_1
\left(
\mathcal L(X_t^{67}),
\rho_\delta(t)
\right)
\le
C_T'
\varepsilon_{67\to64}(T)
+
\varepsilon_{\rm red}^{64}(T),
```

```math
\varepsilon_{\rm red}^{64}(T)
=
e^{L_bT}
\varepsilon_{\rm prep}^{W_1}
+
\frac{e^{L_bT}-1}{L_b}
\varepsilon_{\rm drift}^{64},
```

を得る。$L_b=0$ では第2項を $T\varepsilon_{\rm drift}^{64}$ と読む。

固定 $T$ でfinite-bath、small-mass、signal-backreaction、phase-volume fluctuation、material-frame recoilを同時に0へ送れ、$T<T_{\rm rec},T_{\rm back}$ を保てるparameter族では

```math
\sup_{t\le T}
W_1
\left(
\mathcal L(X_t^{67}),
\mathcal L(X_t^{64})
\right)
\longrightarrow0.
```
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R209C）**

R209Bでfinite Hamiltonian bathをMarkov underdamped過程へ縮約する。$Y_t=X_t^M+\epsilon_MV_t^M$ と置くと厳密に

```math
dY_t
=
b_{64}(X_t^M,t)dt
+
\sqrt{2\nu}\,dW_t.
```

同じBrownian motionでcanonical M64過程を駆動し、driftのLipschitz性と $X_t^M=Y_t-\epsilon_MV_t^M$ を使ってGronwall評価を行うとsmall-mass boundを得る。Maxwell preparationでは $\epsilon_M\sup_t\mathbb E|V_t|=O(\epsilon_MB_*)+O(\sqrt{\nu\epsilon_M})$ である。R209Aのflow compatibility、R208Bのphase-volume mean force/backreaction、regularized observable mapのLipschitz性を三角不等式で合成すれば最初の $W_1$ boundを得る。最後の式はR203Cとの三角不等式である。証明終。
<!-- theorem-end:proof -->

## AA.14 数値検証契約と未主張範囲

M67 candidateではHamiltonian drift、M37 ideal signalとの状態方向誤差、$U_X-v_\delta$、phase-volume mean force、finite-bath memory、tracer分布を同じparameter setで監査する。$N_0$、$N_\rho$、$K_U$、$\tau_U$、$\tau_{\rm mem}$、bath mode数、格子幅を独立に振り、一つの改善を複数誤差へ二重計数しない。

M67/R208/R209を追加・強化してもM64、M65、M66、M54を退役させない。R209A--R209CはM67->M64 compatibilityを定量化するcandidate結果であり、Q3 fixed-goalの直接依存へ追加しない。A1/A2/B1--B3、M0の判定も変更しない。Q1/Q2/NBL特殊化は将来候補であり、H/T/CNOTの一般実装、NBL Born sampling、mixing/resource boundを本付録から推論しない。
