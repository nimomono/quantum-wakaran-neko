@number: Y
@chapter: 付録
@title: M63 topological reservoir一成分Hamiltonian lattice Q3統合候補
@status: active single-field strengthening candidate。一組の実格子正準変数からkink、Schrödinger型signal、topological reservoir、T対称weak-scattering current frameを構成する。R202Cのpartition identity、R202E1のcurrent dictionary、frozen-coefficient harmonic bathのR202E3 GLE/FDTは解析核として閉じる。R202Bのfull envelope、R202Dのmicroscopic backreaction、R202E2のreal-space scatteringからtrackerへの有限誤差、slow coefficient補正、R202FのPN hopping--R161合成は未閉鎖とする。M61/M60の現行固定達成主線は置換しない。

## Y.1 M63の責務と存在論

M63は一格子点あたり一組の実正準変数

```math
(\phi_n,\pi_n),
\qquad
n\in\mathbb Z
```

だけを基本自由度とする時間非依存古典Hamiltonian latticeである。複素signal、kink中心、current-frame coordinate、reservoir modeは独立した実体ではなく、同じ $(\phi_n,\pi_n)$ の固定線形またはcollective representationである。

M63の目標は、同じ一成分場から

```math
\rho,
\qquad
j,
\qquad
X
```

を得て、

```math
\rho
\longrightarrow
-k_BT\log\rho
\longrightarrow
\nu\partial_X\log\rho
```

と

```math
\frac j\rho
\longrightarrow
\text{T対称weak scattering}
\longrightarrow
\text{current frame}
```

を同じHamiltonian内で合成することである。2-action shell、weighted-shell normal form、shell chemical potential、shell--reservoir exchangeは用いない。

## Y.2 2-site local canonical filter bank

隣接2サイトを一つのcellとして

```math
u_m
=
\frac{\phi_{2m}+\phi_{2m+1}}{\sqrt2},
\qquad
v_m
=
\frac{\phi_{2m}-\phi_{2m+1}}{\sqrt2},
```

```math
p_m
=
\frac{\pi_{2m}+\pi_{2m+1}}{\sqrt2},
\qquad
q_m
=
\frac{\pi_{2m}-\pi_{2m+1}}{\sqrt2}.
```

これは固定線形正準変換で、

```math
\{u_m,p_n\}=\delta_{mn},
\qquad
\{v_m,q_n\}=\delta_{mn},
```

かつ

```math
\frac12(p_m^2+q_m^2)
=
\frac12(\pi_{2m}^2+\pi_{2m+1}^2)
```

を満たす。$u$-branchをkinkとsignalに用いる。

$v$-branchには固定直交正準変換をさらに施し、

```math
(v,q)
\longmapsto
(Y,P_Y)
\oplus
\{(\zeta_\alpha,\Pi_\alpha)\}_{\alpha=1}^{M_R}
```

と分ける。例えば正規化profile $h_m$ に対して

```math
Y
=
\ell_Y\sum_mh_mv_m,
\qquad
P_Y
=
\ell_Y^{-1}\sum_mh_mq_m,
\qquad
\sum_mh_m^2=1
```

と取り、残りをその直交補空間の正準座標とする。$Y$ は新しい粒子ではなく、current-frameを表す同じ場のsoft reaction coordinateである。

<!-- theorem-start:theorem -->
**定理（R202A：一成分local filter-bankによるkink・signal・frame・reservoir構成）**

適切な正のparameterと固定filterを選び、同一の一成分実格子上にstable kink sector、$u$-branch continuum内の狭帯域signal sector、soft frame coordinate $(Y,P_Y)$、残余harmonic reservoir sectorを同時に構成する。signalのkink low-passへの漏れを $\varepsilon_{KS}$、signal/reservoir branch混成を $\varepsilon_{SR}$、frame/reservoir分離誤差を $\varepsilon_{YR}$ とし、固定有限時間safe sectorで所定値以下にできるparameter familyをR202Aの目標とする。
<!-- theorem-end:theorem -->

## Y.3 kink・signal branch

最小候補として

```math
H_A
=
\sum_m
\left[
\frac{p_m^2}{2}
+
U_K(u_m)
\right]
+
\frac{\kappa_A}{2}
\sum_m
(u_{m+1}-u_m)^2,
```

```math
U_K(u)
=
\frac{\Omega_K^2}{8u_0^2}
(u^2-u_0^2)^2
```

を取る。真空 $u=\pm u_0$ を結ぶ離散kink $u_m^K(X)$ のcollective centerを粒子位置 $X$ とする。

真空まわりの線形branchは

```math
\omega_A^2(k)
=
\Omega_K^2
+
4\kappa_A\sin^2\frac{k}{2}
```

を持つ。このcontinuumの狭帯域packetをsignalに用いる。kink抽出用low-passを $\bar u=F_Ku$、signal carrier抽出用band-passを

```math
Q^s=F_su,
\qquad
P^s=F_sp
```

とする。存在証人では有限range FIR filterを許し、一サイト並進対称性を求める強化版では格子作用素の滑らかな関数または有限次数多項式近似を用いる。

## Y.4 same-field signal envelope・density/current

carrier波数 $k_s$ の周囲で

```math
\omega_A(k)
=
\omega_s
+
v_g(k-k_s)
+
\frac12\omega_s''(k-k_s)^2
+
\cdots
```

と展開し、carrier phaseとgroup translationを除いたslow envelopeを $Z$ とする。

局所signal actionを

```math
\rho_m^s
=
\frac{
(P_m^s)^2+\omega_s^2(Q_m^s)^2
}{
2\omega_s
}
```

とする。準備境界から固定physical action scale $N_0>0$ を受け取り、平滑kernel $K_r$ と正則化背景 $\delta\varpi_m>0$ により

```math
r_m^\delta
=
\delta\varpi_m
+
\frac1{N_0}
\sum_\ell
K_r(m-\ell)\rho_\ell^s
```

とする。safe sectorで

```math
0<r_{\min}
\le
r_m^\delta
\le
r_{\max}<\infty
```

を要求する。

<!-- theorem-start:theorem -->
**定理（R202B：same-field Schrödinger signal envelope・density/current）**

R202Aの狭帯域signal sectorについて、固定有限時間で

```math
i\mathcal J_0\partial_tZ
=
-\frac{\mathcal J_0^2}{2m_{\rm eff}}
\partial_x^2Z
+
V_{\rm eff}Z
+
R_{\rm env}
```

へ縮約し、

```math
\|Z_{\rm micro}(t)-Z_{\rm Sch}(t)\|
\le
\varepsilon_{\rm env}(T)
```

を得る。同じsignalから密度 $\rho$ とcurrent $j$ を導き、

```math
\partial_t\rho+\partial_xj
=
O(\varepsilon_{\rm env})
```

を満たす。prepared actionについて

```math
\left|
\frac{N_s(t)}{N_0}-1
\right|
\le
\varepsilon_N
```

を有限時間で要求する。Nelson matchingは $\mathcal J_0=2m_{\rm eff}\nu$ とする。
<!-- theorem-end:theorem -->

## Y.5 topological kink weightとkink-local density

左真空で0、右真空で1となる滑らかな単調関数 $s$ を固定し、

```math
s(-u_0)=0,
\qquad
s(u_0)=1
```

とする。kink weightを

```math
\boxed{
\gamma_m
=
s(\bar u_{m+1})
-
s(\bar u_m)
}
```

と定める。topological sectorではtelescopingにより

```math
\boxed{
\sum_m\gamma_m=1
}
```

が成り立つ。理想単調kinkでは $\gamma_m\ge0$ でkink coreに局在する。

reservoirへ渡すscalar densityをweighted geometric mean

```math
\boxed{
r_K^\delta
=
r_*
\exp
\left[
\sum_m
\gamma_m
\log\frac{r_m^\delta}{r_*}
\right]
}
```

とする。signalがkink幅より滑らかなら

```math
\log r_K^\delta
=
\log r^\delta(X)
+
O(\varepsilon_{\rm width}).
```

## Y.6 topological harmonic reservoir

残余reservoir modeに固定weight $w_\alpha>0$ を割り当て、

```math
\sum_{\alpha=1}^{M_R}w_\alpha=1
```

とする。density scalingを

```math
\boxed{
\lambda_\alpha
=
\left(
\frac{r_K^\delta}{r_*}
\right)^{-w_\alpha}
}
```

とする。

kink--frame relative coordinateを

```math
R
=
X_\gamma-\alpha_YY
```

とし、reservoir Hamiltonianを

```math
\boxed{
H_R
=
\sum_\alpha
\left[
\frac{\Pi_\alpha^2}{2m_\alpha}
+
\frac{m_\alpha\omega_\alpha^2}{2}
\left(
\lambda_\alpha\zeta_\alpha
-
\frac{g_\alpha}{m_\alpha\omega_\alpha^2}R
\right)^2
\right].
}
```

とする。これは正のsquareの和で下に有界である。$X_\gamma$、$Y$、$\lambda_\alpha$ はすべて元の $(\phi,\pi)$ の派生量なので、新しい独立実体を導入しない。

## Y.7 R202C：topological reservoir partition identity

固定signal/kink/frame configurationに対して

```math
Z_R[r_K,R]
=
\int
e^{-\beta H_R}
\prod_\alpha
d\zeta_\alpha d\Pi_\alpha
```

を考える。各modeで

```math
c_\alpha
=
\lambda_\alpha\zeta_\alpha
-
\frac{g_\alpha}{m_\alpha\omega_\alpha^2}R
```

と変数変換すると

```math
d\zeta_\alpha
=
\lambda_\alpha^{-1}dc_\alpha.
```

従ってrelative-coordinate shiftはpartition functionへ寄与せず、density scalingのJacobianだけが残る。

<!-- theorem-start:theorem -->
**定理（R202C：topological reservoir phase-volume identity）**

R202Aのsafe kink sectorで $\sum_m\gamma_m=1$、$\sum_\alpha w_\alpha=1$ とする。このとき

```math
\boxed{
Z_R[r_K,R]
=
Z_R^0
\frac{r_K^\delta}{r_*}
}
```

が厳密に成立し、

```math
\boxed{
F_R
=
-k_BT\log r_K^\delta
+
C_R
}
```

となる。自由エネルギーはrelative coordinate $R=X_\gamma-\alpha_YY$ に依存しない。
<!-- theorem-end:theorem -->

従って等価なPN minima間、またはbaseline pinningを分離した条件付き位置重みについて

```math
P_i
\propto
e^{-\beta F_R(x_i)}
\propto
r_K^\delta(x_i)
```

を得る。smooth・正則化極では $r_K^\delta\to\rho/N_0$ なので、これはBorn型位置重み $P_i\propto\rho(x_i)$ を与える。

## Y.8 R202D：osmotic forceとsmall backreaction

R202Cより

```math
F_R
=
-k_BT
\sum_m
\gamma_m\log r_m^\delta
+
C_R.
```

kink幅を $\sigma_K$ とすると

```math
\sum_m\gamma_m\log r_m^\delta
=
\log r^\delta(X_\gamma)
+
\frac{\sigma_K^2}{2}
\partial_x^2\log r^\delta(X_\gamma)
+
\cdots.
```

<!-- theorem-start:theorem -->
**定理（R202D：topological osmotic force・small-backreaction）**

R202A--R202Cのsafe sectorでsignal densityがkink幅より滑らかなら

```math
\boxed{
F_X^{\rm osm}
=
k_BT\partial_X\log r^\delta
+
O(
\varepsilon_{\rm width}
+
\varepsilon_{\rm filt}
+
\varepsilon_{\rm top}
)
}
```

を得る。

$r^\delta$ がprepared physical action $N_0$ で規格化されるため、density portからsignalへ返る相対shape変形は固定有限時間で $O(N_0^{-1})$ に抑えるparameter familyを要求する。
<!-- theorem-end:theorem -->

physical signal振幅を $O(\sqrt{N_0})$、bare lattice nonlinear scaleを $v_0$ とすると $\sqrt{N_0}/v_0\ll1$ を要求する。例えば $v_0=N_0^{3/4}$ とすればdensity-port backreactionとbare signal非線形性を同時に小さくできる。

## Y.9 R202E1：same-field current dictionary

edge $e=(i,j)$ のsignalについて

```math
C_{e,+}
=
\frac{Z_i-iZ_j}{\sqrt2},
\qquad
C_{e,-}
=
\frac{Z_i+iZ_j}{\sqrt2}
```

とし、

```math
I_{e,\pm}=|C_{e,\pm}|^2
```

と置く。このとき厳密に

```math
I_{e,+}+I_{e,-}
=
|Z_i|^2+|Z_j|^2,
```

```math
I_{e,+}-I_{e,-}
=
2\operatorname{Im}(Z_i^*Z_j).
```

kink-localな和・差を$\gamma$で平均し、

```math
E_K
=
\sum_e\gamma_e
(I_{e,+}+I_{e,-}),
```

```math
r_{\rm ch}
=
\frac{
\sum_e\gamma_e(I_{e,+}-I_{e,-})
}{
E_K+\delta I_0
}
```

とする。

<!-- theorem-start:lemma -->
**補題（R202E1：current dictionary）**

R202Bのsmooth narrow-band sectorでは既知の係数 $c_J$ に対して

```math
\boxed{
\frac j\rho(X)
=
c_Jr_{\rm ch}
+
O(
a^2
+
\delta
+
\varepsilon_{\rm env}
+
\varepsilon_{\rm width}
)
}
```

となる。$r_{\rm ch}$ はsignal全体の振幅scaleに依存しない。
<!-- theorem-end:lemma -->

## Y.10 R202E2：T対称weak-scattering current frame

frame free Hamiltonianを

```math
H_Y
=
\frac{P_Y^2}{2M_Y}
```

とする。kink近傍へ局在したT対称なreal-space current portとして

```math
\boxed{
H_{\rm sc}
=
\frac{\varepsilon_s}{2}
\sum_m
\gamma_m
W(2k_sx_m-2k_sY)
(Q_m^s)^2
}
```

を取る。$W$ は実の有界周期関数である。bare signal stiffnessとの和が正に保たれるよう $|\varepsilon_s|$ を小さく取る。$H_{\rm sc}$ は座標だけに依存するため時間反転で不変であり、複素signal記法を用いても実正準Hamiltonianの略記にすぎない。

narrow-band weak-reflection normal formでは

```math
H_{\rm sc}^{\rm NF}
=
J_s
\left[
e^{2ik_sY}C_-^*C_+
+
e^{-2ik_sY}C_+^*C_-
\right]
+
R_{\rm sc}^{\rm NF}.
```

local incoming actionsを $I_\pm$、frame速度を $U=\dot Y$、$\beta=U/c_s$ とする。弱反射・outgoing-wave windowでradiation forceが

```math
F_{\rm sc}
=
A_{\rm sc}E_K
\left[
r_{\rm ch}(1+\beta^2)
-
2\beta
\right]
+
R_{\rm sc},
\qquad
A_{\rm sc}>0
```

へ縮約すると仮定する。

理想固定点は

```math
\boxed{
\beta_*(r)
=
\frac{r}{1+\sqrt{1-r^2}}
}
```

で、

```math
\beta_*(r)
=
\frac r2
+
O(r^3),
```

かつ $\partial_\beta F_{\rm sc}|_{\beta_*}<0$ である。

<!-- theorem-start:lemma -->
**補題（R202E2：weak-scattering frame tracker）**

real-space $H_{\rm sc}$ から上のforce lawへの有限誤差を $\varepsilon_{\rm sc}$ とし、working sectorでforce-slope下限 $\lambda_Y>0$ を持つとする。relative bathからframeへ返る力を $F_{\rm load}$ とすれば

```math
\begin{aligned}
|U(t)-c_s\beta_*(r_{\rm ch}(t))|
\le{}&
e^{-\lambda_Yt}
|U(0)-c_s\beta_*(r_{\rm ch}(0))|
\\
&+
\frac{L_\beta}{\lambda_Y}
\|\dot r_{\rm ch}\|_{\infty,[0,T]}
\\
&+
\frac1{M_Y}
\int_0^t
e^{-\lambda_Y(t-s)}
|F_{\rm load}(s)|ds
+
C\varepsilon_{\rm sc}.
\end{aligned}
```

scale $\alpha_Y$ を

```math
\frac{\alpha_Yc_s}{2}
=
c_J
```

と較正すれば

```math
\boxed{
\alpha_Y\dot Y
=
\frac j\rho
+
O(
a^2+
\delta+
r_{\rm ch}^3+
\varepsilon_{\rm env}+
\varepsilon_{\rm width}+
\varepsilon_{\rm sc}+
\varepsilon_{\rm track}
)
}.
```
<!-- theorem-end:lemma -->

signal physical actionを $N_0$ とし、reflection probabilityを $\mathcal R=O(N_0^{-1})$ と取れば、radiation-force slopeを $O(1)$ に保ちながらsignalのfractional reflection/depletionを $O(N_0^{-1})$ にするlarge-action scalingを狙える。

## Y.11 R202E3：relative harmonic-bath GLE/FDT

R202E2のframeとkinkのrelative coordinate

```math
R
=
X_\gamma-\alpha_YY
```

をY.6のharmonic reservoirへ結合する。

固定された $r_K^\delta$、従って固定 $\lambda_\alpha$ の時間窓では各reservoir modeは

```math
H_\alpha
=
\frac{\Pi_\alpha^2}{2m_\alpha}
+
\frac{m_\alpha(\lambda_\alpha\omega_\alpha)^2}{2}
\left[
\zeta_\alpha
-
\frac{g_\alpha}{m_\alpha\omega_\alpha^2\lambda_\alpha}R
\right]^2
```

という標準completed-square oscillatorである。したがってreservoirを厳密消去できる。

<!-- theorem-start:lemma -->
**補題（R202E3：frozen-coefficient relative GLE/FDT）**

初期reservoirを固定初期 $R(0)$ に条件づけたcanonical Gibbs分布から準備する。固定 $\lambda_\alpha$ の時間窓ではkinkへのreservoir力は

```math
\boxed{
F_R^{\rm dyn}(t)
=
-
\int_0^t
\Gamma_\lambda(t-s)
[
\dot X_\gamma(s)
-
\alpha_Y\dot Y(s)
]ds
+
\xi(t)
}
```

となる。memory kernelは

```math
\boxed{
\Gamma_\lambda(t)
=
\sum_\alpha
\frac{g_\alpha^2}{
m_\alpha\omega_\alpha^2
}
\cos(
\lambda_\alpha\omega_\alpha t
)
}
```

であり、

```math
\langle\xi(t)\rangle=0,
\qquad
\boxed{
\langle\xi(t)\xi(s)\rangle
=
k_BT\Gamma_\lambda(|t-s|)
}
```

が厳密に成立する。
<!-- theorem-end:lemma -->

$\lambda_\alpha(t)$、$\gamma_m(t)$ がmemory時間上でslowに変化するfull M63では、frozen-coefficient式との差を $\varepsilon_{\rm ad}$ として管理する。

effective spectral densityがsafe $\lambda$ 区間で一様に

```math
J_\lambda(\omega)
=
\gamma_X\omega
+
O(\omega^3/\omega_c^2)
```

を満たすようreservoir spectrumを設計すると、

```math
\int_0^t
\Gamma_\lambda(t-s)\dot R(s)ds
=
\gamma_X\dot R(t)
+
O(\varepsilon_{\rm Ohm}+\varepsilon_{\rm mem})
```

というMarkov極を狙える。

## Y.12 R202E：current transport・osmotic force・GLEの合成

<!-- theorem-start:theorem -->
**定理（R202E：same-field current transport・relative GLE/FDT）**

R202A--R202D、R202E1--R202E3を同じparameter familyで満たすとする。このとき

```math
\begin{aligned}
M_X\ddot X
={}&
-\partial_XU_{\rm PN}
+
k_BT\partial_X\log r^\delta
\\
&-
\int_0^t
\Gamma(t-s)
\left[
\dot X(s)-\frac j\rho(s)
\right]ds
+
\xi(t)
+
R_{202E},
\end{aligned}
```

を有限時間で得ることをR202Eの目標とする。$R_{202E}$ はcurrent dictionary、real-space scattering、tracking、slow coefficient、finite-memory、filter/backreaction誤差をまとめる。

Markov/overdamped極で

```math
\nu
=
\frac{k_BT}{\gamma_X}
```

と較正すれば

```math
\boxed{
dX_t
=
\left[
\frac j\rho
+
\nu\partial_X\log\rho
\right]dt
+
\sqrt{2\nu}\,dW_t
+
O(\varepsilon_{202E})
}
```

へ縮約する。
<!-- theorem-end:theorem -->

R202E1とfrozen-coefficient R202E3は解析核として閉じる。R202E2のreal-space Hamiltonianからweak-scattering force lawへの有限誤差、loadを含む同時tracking window、slow $\lambda$ 補正、full-trajectory signal backreactionは未閉鎖である。

## Y.13 R202F：PN hoppingからR161/R185への合成

離散kink中心はPeierls--Nabarro周期ポテンシャル $U_{\rm PN}(X)$ を持つ。そのminimaを $x_i$ とし、intra-well relaxationがescapeより速いregimeでwell-index過程へ粗視化する。

<!-- theorem-start:theorem -->
**定理（R202F：M63からR161位置経路・R185への有限時間合成）**

R202A--R202Eを同じparameter familyで満たし、

```math
\tau_Y,
\tau_{\rm mem},
\tau_{\rm well}
\ll
\tau_r,
\tau_{\rm hop},
\qquad
T_{\rm obs}
<
\min(T_{\rm env},T_{\rm return})
```

となる非空の観測時間窓を取れるとする。PN well-index過程のgenerator $k_{i\to j}^{63}$ について

```math
\sup_{t\le T}
\max_i
\sum_{j\ne i}
\left|
k_{i\to j}^{63}(t)
-
k_{i\to j}^{161}(t)
\right|
\le
\varepsilon_{\rm tr}^{63}
```

を満たすparameter familyを構成することをR202Fの目標とする。この接続が閉じれば、同じ前向き経路法則のBayes反転から後退率、$D_\pm$、時間対称Newton則を得る既存R185を再利用する。
<!-- theorem-end:theorem -->

## Y.14 誤差責務と現行主線との境界

M63候補の誤差は

```math
\begin{aligned}
\varepsilon_{\rm tr}^{63}
\le C_{63}(&
\varepsilon_{\rm env}
+\varepsilon_{KS}
+\varepsilon_{SR}
+\varepsilon_{YR}
+\varepsilon_{\rm filt}
+\varepsilon_N
+\varepsilon_{\rm top}
+\varepsilon_{\rm width}
\\
&
+\varepsilon_{\rm back}
+\varepsilon_{\rm ch}
+\varepsilon_{\rm sc}
+\varepsilon_{\rm track}
+\varepsilon_{\rm ad}
+\varepsilon_{\rm Ohm}
+\varepsilon_{\rm mem}
\\
&
+\varepsilon_{\rm od}
+\varepsilon_{\rm PN}
+\varepsilon_{\rm EK}
+a_X^2)
\end{aligned}
```

と整理する。同じ上流偏差を複数項へ重複加算しない。

M63の主要時間尺度は

```math
\tau_Y,
\qquad
\tau_{\rm mem},
\qquad
\tau_{\rm well},
\qquad
\tau_{\rm hop},
\qquad
\tau_r,
\qquad
T_{\rm env},
\qquad
T_{\rm return}
```

であり、基本階層を

```math
\tau_Y,
\tau_{\rm mem},
\tau_{\rm well}
\ll
\tau_r,
\tau_{\rm hop}
```

とする。

M63/R202はactive single-field candidateであるが、M61/R200--M60/R198/R199/R196の現行固定達成主線はまだ置換しない。固定Q3-1/Q3-2の達成ラベル、Q3-1-A1/Q3-2-A1の部分達成、Q3-1-A2/Q3-2-A2の未監査は変更しない。

M63を現行Q3ミクロ主線へ昇格させるには、少なくともR202A/R202Bの同一parameter branch witness、R202Dのfull-trajectory osmotic forceと $N_0^{-1}$ backreaction、R202E2のreal-space weak-scattering tracking、R202E3のslow-coefficient/Ohmic finite-time closure、R202FのPN hopping--R161有限誤差接続、およびそれらを同時に満たす共通時間窓を閉じる必要がある。
