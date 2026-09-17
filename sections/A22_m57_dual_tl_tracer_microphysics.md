@number: V
@chapter: 付録
@title: M57 dual-ballistic-TL moving-bath tracerミクロ模型とR161有限誤差持上げ
@status: Q3の現行ミクロ物理層。M37/M54実正準空間信号から局所chiral作用を厳密に取り出し、dual ballistic waveguide、moving bath-frame carrier、平衡oscillator bath、局在tracerへ接続してR161生成子へ有限誤差で持ち上げる。旧pinned/anharmonic thermalizing-TL、drifting-Gibbs、TL自身へのFDTは用いない。R161/R162/R185の数学核は変更しない。

## V.1 M57の責務と実在自由度

M57はM58内のQ3粒子位置輸送subsystemである。単一試行で物理的に存在する自由度は、M37/M54の実正準空間信号、辺ごとの二本のballistic wave channel、局所bath cellのcenter-of-mass座標 $Y_e$、その内部の平衡oscillator bath、1個のtracer座標 $X$、2作用状態数sector、periodic/double-well potentialである。複素信号 $Z$ は実正準平面の派生表示であり独立実体ではない。

旧M57で用いた weak pinning、quartic anharmonicity、Drude termination、TL mixing、force-correlation time、drifting-Gibbs近似は現行M57から退役する。dual ballistic TLはcurrent情報を機械的なbath-frame速度へ変換するだけであり、Brownian noiseとFDTは別の通常の平衡oscillator bathが担う。

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

と置く。二本のchannelは同一線路上の運動量符号ではなく独立な物理channelとする。

## V.2 R195A：chiral作用・状態数・signal current velocity

直接計算から

```math
I_{e,+}+I_{e,-}=R_i+R_j,
```

```math
I_{e,+}-I_{e,-}=2\operatorname{Im}(Z_i^*Z_j)
```

が全信号振幅について厳密に成り立つ。nearest-neighbor Schrödinger特殊化で $\mathcal J_0=2m\nu$ とし、辺結合を $h_{ij}=-\mathcal J_0\nu/a^2$ と取る向き規約では

```math
J_{ij}^{\rm sig}
=\frac{\nu}{a^2}(I_{e,+}-I_{e,-}).
```

edge chiralityを

```math
r_e
=\frac{I_{e,+}-I_{e,-}}{I_{e,+}+I_{e,-}}
```

と定めると、signal edge velocityは

```math
\boxed{
u_{ij}^{\rm sig}
=\frac{2aJ_{ij}^{\rm sig}}{R_i+R_j}
=\frac{2\nu}{a}r_e
}
```

と厳密に書ける。従ってR196A以後の責務は $J/\rho$ を外部で計算することではなく、すでに局所chiral作用比として露出しているvelocityを実在bath frameとtracerへ受動的に伝えることである。

tracer位置に付随する2作用sector $(K_1,\theta_1),(K_2,\theta_2)$ に

```math
H_{\rm sh}
=\frac{\kappa_{\rm sh}}2
[K_1+K_2-A^\delta(X,Z)]^2,
```

```math
A_i^\delta
=\alpha\,[R_i+\delta q_iS_{\rm ref}]
```

を置く。strict-shell極では

```math
\int_0^\infty dK_1\int_0^\infty dK_2\,
\delta(A-K_1-K_2)=A
```

なので

```math
\Omega_i^\delta\propto R_i^\delta,
\qquad
R_i^\delta=R_i+\delta q_iS_{\rm ref},
```

```math
\pi_i^\delta
=\frac{R_i^\delta}{\sum_kR_k^\delta}.
```

同じ状態数sectorの容量は $R^\delta$ に比例する。これを実際のpotential of mean forceとして動力学的に実現するthermostatted shellと有限時間averagingは付録WのR197A/Bで与える。

<!-- theorem-start:theorem -->
**定理（R195A：M57 chiral作用・状態数・signal current恒等式）**

上の定義の下で、chiral作用の和・差、$J_{ij}^{\rm sig}=\nu(I_+-I_-)/a^2$、$u_{ij}^{\rm sig}=2\nu r_e/a$ は厳密恒等式である。strict 2-action shellでは条件付きLiouville状態数は $A_i^\delta$ に比例し、規格化位置重みは $\pi_i^\delta$ となる。M59ではR198A--R198Dがこの2-action Gibbs shellを実Duffing＋二保存action reservoirから持ち上げ、有限幅に加えてfinite-$N$、finite-exchange、finite-time mixing誤差を付録A23で管理する。
<!-- theorem-end:theorem -->

## V.3 dual ballistic port

各 $\sigma=\pm$ channelを同じ波速 $c$ を持つ1次元Hamiltonian waveguide

```math
H_{{\rm bal},\sigma}
=\frac12\int dx
\left[
\frac{\Pi_\sigma(x)^2}{\chi}
+\chi c^2(\partial_x\phi_\sigma(x))^2
\right]
```

として表す。固定有限時間では半無限線路、または遠端反射が観測時間内に戻らない有限線路を用いる。一方向進行波ではenergy density $e_\sigma$ とmomentum density $p_\sigma$ は

```math
p_\sigma=\sigma\frac{e_\sigma}{c}
```

を満たす。

signal chiral modeとwaveguideのlocal passive portをbilinear coupling

```math
H_{\rm port}
=\epsilon\sum_{\sigma=\pm}\int dk\,
[g_kC_{e,\sigma}^*b_{\sigma k}+\mathrm{c.c.}]
```

で与える。zero incoming carrier、有限bandwidth、固定有限時間でDuhamel展開を行うと、適切なport観測面におけるincident energy densityは

```math
e_{e,\sigma}(t)
=\kappa_p I_{e,\sigma}(t-\tau_p)
+\delta e_{e,\sigma}(t),
```

```math
\sup_{t\le T}|\delta e_{e,\sigma}(t)|
\le \varepsilon_{\rm port}I_*,
\qquad
\varepsilon_{\rm back}(T)\le C_{\rm back}(T)\epsilon^2
```

と評価する。ここで $\kappa_p=O(\epsilon^2)$、$\tau_p$ は伝播遅延である。有限band dispersionとdirectivityは $\varepsilon_{\rm port}$ に含める。

このport補題はstate-dependent divisionやphase measurementを含まず、左右作用を対応する二本のwaveguideへ線形にtapするだけである。

## V.4 R196A：dual ballistic TLからmoving bath velocityへの有限時間持上げ

二本のwaveguideは、局所bath cellのcenter-of-mass座標

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

とする。左から入射するenergy density $e_+$ の反射Doppler比は $(1-\beta)/(1+\beta)$、右からの $e_-$ では $(1+\beta)/(1-\beta)$ である。moving boundaryへ単位時間に到達するenergyと反射前後のmomentum差から

```math
F_+(\beta)
=2e_+\frac{1-\beta}{1+\beta},
```

```math
F_-(\beta)
=-2e_-\frac{1+\beta}{1-\beta},
```

従って

```math
\boxed{
F_{\rm bal}(\beta;e_+,e_-)
=2e_+\frac{1-\beta}{1+\beta}
-2e_-\frac{1+\beta}{1-\beta}
}
```

を得る。

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
\boxed{
\beta_*(r)
=\frac{\sqrt{e_+}-\sqrt{e_-}}{\sqrt{e_+}+\sqrt{e_-}}
=\frac{r}{1+\sqrt{1-r^2}}
}
```

である。また

```math
\frac{\partial F_{\rm bal}}{\partial U}
=-\frac4c
\left[
\frac{e_+}{(1+\beta)^2}
+\frac{e_-}{(1-\beta)^2}
\right]<0.
```

特に $E\ge E_{\min}>0$ なら

```math
-\partial_UF_{\rm bal}\ge\frac{E_{\min}}c.
```

tracerからbath cellへの反作用を $f_{\rm load}$ として

```math
M_e\dot U_e
=F_{\rm bal}(U_e/c;e_+,e_-)+f_{\rm load}(t)
```

と書く。instantaneous fixed pointを

```math
U_*(t)=c\beta_*(r(t))
```

とし、

```math
\lambda_Y=\frac{E_{\min}}{M_ec},
```

```math
L_*(r_*)
=\frac1{\sqrt{1-r_*^2}\,[1+\sqrt{1-r_*^2}]}
```

と置く。$|r(t)|\le r_*<1$ なら平均値定理とGronwall不等式から

```math
\boxed{
\begin{aligned}
|U_e(t)-U_*(t)|
\le{}&e^{-\lambda_Yt}|U_e(0)-U_*(0)|\\
&+\frac{cL_*(r_*)}{\lambda_Y}\|\dot r\|_{\infty,[0,T]}\\
&+\frac1{M_e}\int_0^t e^{-\lambda_Y(t-s)}|f_{\rm load}(s)|\,ds.
\end{aligned}
}
```

ballistic propagation delayまで含めると $r(t)=r_{\rm sig}(t-\tau_p)+O(\varepsilon_{\rm port})$ なので、必要なfast-sector条件は

```math
\boxed{
\tau_p\ll T_{\rm sig},
\qquad
\lambda_Y^{-1}\ll T_{\rm sig}
}
```

である。

さらに

```math
\beta_*(r)-\frac r2
=\frac{r^3}{2[1+\sqrt{1-r^2}]^2}
```

が厳密に成り立つので、smooth sector $r=O(a)$ では

```math
U_*(r)=\frac c2r+O(ca^3).
```

weak tap scaling

```math
\kappa_p=\epsilon^2\bar\kappa_p,
\qquad
M_e=\epsilon^2\bar M_e
```

を取ると

```math
\lambda_Y
=\frac{\bar\kappa_p S_{\min}}{\bar M_ec}
```

は $\epsilon\to0$ でも有限のまま、signal backreactionは $O(\epsilon^2)$ へ下げられる。これは有限powerを保ったままbackreactionだけを消す主張ではなく、incident energyとcarrier inertiaを同じ比率で縮小してterminal velocityを保つ受動スケーリングである。

<!-- theorem-start:theorem -->
**定理（R196A：dual ballistic TLからmoving bath velocityへの有限時間持上げ）**

上のpassive ballistic-port条件、$E\ge E_{\min}>0$、$|r|\le r_*<1$ の下で、bath-frame carrierには唯一安定なinstantaneous terminal velocity $U_*=c\beta_*(r)$ が存在し、有限時間追従誤差は上式で制御される。weak tapとcarrier massを同時に $O(\epsilon^2)$ へ縮小すれば追従rateを有限に保ったままsignal backreactionを $O(\epsilon^2)$ へ下げられる。TL thermalization、mixing、drifting-Gibbs、Green--Kuboは本定理に用いない。
<!-- theorem-end:theorem -->

## V.5 R196B：moving equilibrium bathからtracer GLE・Nelson driftへ

actual tracer $X$ はTLそのものには熱化させず、$Y_e$ と共に並進する通常のequilibrium oscillator bathへ結合する。bath内部座標を $q_n$ とし、相対座標 $X-Y_e$ へ

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
-\int_0^t\Gamma(t-s)[\dot X(s)-\dot Y_e(s)]\,ds
+\xi(t)+r_{\rm init}(t),
```

```math
\langle\xi(t)\xi(s)\rangle
=k_BT\,\Gamma(|t-s|)
```

を得る。ここでFDTを適用しているのはbath cell内部の平衡oscillator bathだけであり、ballistic TLには適用しない。

R197A/Bで同じ試行のthermostatted shellを消去すると、tracerへ作用する平均shell力は

```math
F_{\rm sh}(X,Z)
=k_BT[1-\Delta(x(A))]\partial_X\log R^\delta(X,Z)
```

となり、finite-width誤差 $\varepsilon_{\rm width}$ とfast--slow averaging誤差 $\varepsilon_{\rm sh,av}$ が明示的に付く。strict-shell/fast-shell極では従来の $-k_BT\log R^\delta$ 表示へ一致する。Ohmic/Markov極とoverdamped極で

```math
dX_t
=U_e(t)\,dt
+D_0\,\partial_x\log R^\delta(X_t,t)\,dt
-\mu V_{\rm per}'(X_t)\,dt
+\sqrt{2D_0}\,dW_t
+r_{\rm GLE}\,dt,
```

```math
D_0=\mu k_BT=\frac{k_BT}{\gamma_X}
```

へ縮約する。有限bath cutoffと慣性消去の誤差をそれぞれ $\varepsilon_{\rm GLE}$、$\varepsilon_{\rm od}$ とする。

period $a$ の対称potential $V_{\rm per}(X+a)=V_{\rm per}(X)$ に対し、zero-biasのLifson--Jackson suppressionを

```math
\boxed{
g_K
=\frac1{
\langle e^{\beta V_{\rm per}}\rangle_a
\langle e^{-\beta V_{\rm per}}\rangle_a
}
}
```

とする。slow spatial modulationとsmall edge affinityのhomogenizationでは

```math
D_{\rm eff}=g_KD_0+O(\varepsilon_{\rm hom}),
```

```math
u_{\rm eff}=g_KU_e+O(\varepsilon_{\rm hom}),
```

```math
b_{\rm osm}=g_KD_0\,\partial_x\log R^\delta
+O(\varepsilon_{\rm hom}).
```

中心matchingを

```math
\boxed{
D_0=\frac\nu{g_K},
\qquad
g_Kc=\frac{4\nu}{a}
}
```

と置けば

```math
D_{\rm eff}=\nu+O(\varepsilon_{\rm hom}),
```

```math
g_KU_*(r)
=\frac{2\nu}{a}r+O(a^2),
```

```math
b_{\rm osm}
=\nu\partial_x\log R^\delta+O(\varepsilon_{\rm hom}).
```

従って

```math
\boxed{
b_+
=\frac j\rho
+\nu\partial_x\log\rho
+O(a^2+\varepsilon_{\rm micro})
}
```

が得られる。

bath-frame loadingを同じ極で制御するため、weak-tap familyに

```math
\gamma_X=\epsilon^4\bar\gamma,
\qquad
k_BT=\gamma_XD_0,
\qquad
M_X=\epsilon^6\bar M_X,
```

```math
V_{\rm per}=k_BT\,\bar V_{\rm per}
```

を加える。すると $D_0$、dimensionless barrier、$g_K$ を固定したまま

```math
\tau_X=\frac{M_X}{\gamma_X}=O(\epsilon^2),
```

tracerから$Y_e$へ返るfriction/noise impulseによるvelocity perturbationは固定有限時間で

```math
\varepsilon_{\rm load}=O(\gamma_X/M_e)=O(\epsilon^2)
```

へ下げられる。

<!-- theorem-start:theorem -->
**定理（R196B：moving equilibrium bathからNelson driftへの有限誤差縮約）**

R196Aのmoving bath-frame追従、明示oscillator bathのFDT、有限cutoff Markov極、overdamped極、periodic homogenizationの仮定の下で、tracerのeffective diffusion、current drift、osmotic driftは同じ $D_0=\nu/g_K$ と $g_Kc=4\nu/a$ によりそれぞれ $\nu$、$j/\rho+O(a^2)$、$\nu\partial_x\log\rho$ へ一致する。weak-tap familyではsignal backreactionとtracer loadingを同時に $O(\epsilon^2)$ へ下げられる。
<!-- theorem-end:theorem -->

## V.6 R196C：metastable well indexからR161生成子への持上げ

periodic/double-well landscapeのwell indexを有限格子位置として読む。moving bath velocity $U_e$ はoverdamped equationではconstant tilt force $f_e=\gamma_XU_e$ と等価であり、edge affinityは

```math
\mathcal A_e
=\beta f_ea
=\frac{aU_e}{D_0}.
```

理想trackingと中心matchingでは

```math
\boxed{
\mathcal A_e
=4\beta_*(r_e)
}
```

であり、small-$r$ 展開は

```math
\mathcal A_e
=2r_e+\frac12r_e^3+O(r_e^5).
```

state-count free energyによってwell weightが $R_i^\delta$、symmetric saddle weightが

```math
R_b=\frac{R_i^\delta+R_j^\delta}{2}
```

となるsectorを用いる。zero-bias periodic homogenizationで $D_{\rm eff}=\nu$ に較正した同じlandscapeについて、対称well間のcoarse-grained基準fluxを

```math
c_K=\frac{\nu R_b}{a^2}
```

と定める。これは独立に挿入する率ではなく、R196Bの $D_{\rm eff}=\nu$ とsymmetric barrier weightをwell-index generatorへ書き直した基準activityである。その上でEyring--Kramers/metastable reductionは

```math
q_{ij}^+
=\frac{\nu R_b}{a^2}
\exp(\mathcal A_e/2)
[1+O(\varepsilon_{\rm EK})],
```

```math
q_{ij}^-
=\frac{\nu R_b}{a^2}
\exp(-\mathcal A_e/2)
[1+O(\varepsilon_{\rm EK})]
```

を与える。理想主項に対し

```math
T_{ij}^{57}=q_{ij}^++q_{ij}^-,
\qquad
J_{ij}^{57}=q_{ij}^+-q_{ij}^-.
```

従って

```math
k_{i\to j}^{57}
=\frac{T_{ij}^{57}+J_{ij}^{57}}{2R_i^\delta}
```

はR161形式を持つ。

$\delta=0$、$R_b=(R_i+R_j)/2$ では

```math
\frac{J_{ij}^{57}}{J_{ij}^{\rm sig}}
=\frac{\sinh[2\beta_*(r_{ij})]}{r_{ij}}
=1+\frac5{12}r_{ij}^2+O(r_{ij}^4).
```

smooth sector $r=O(a)$ ではnative current correctionはrelative $O(a^2)$ である。

有限時間 $0\le t\le T$ の生成子差を

```math
\varepsilon_{57}
=\sup_{t\le T}\max_i\sum_{j\ne i}
|k_{i\to j}^{57}-k_{i\to j}^{161}|
```

とすると、node-free safe sectorで

```math
\boxed{
\varepsilon_{57}
\le C_{57}
\left(
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
\right).
}
```

R161実現同値の有限時間比較から同じ初期位置分布について

```math
\sup_{t\le T}
D_{\rm TV}(p_t^{57},p_t^{161})
\le T\varepsilon_{57}
```

を得る。

<!-- theorem-start:theorem -->
**定理（R196C：ballistic M57からR161への有限誤差持上げ）**

R195A、R196A--R196Bの仮定とmetastable well-index縮約の下で、M57 tracerのcoarse-grained位置生成子はR161形式へ持ち上がり、signal-current理想生成子との差は上の $\varepsilon_{57}$ で有限時間制御される。smooth sectorではmoving-reflectorの非線形性によるnative current correctionはrelative $O(a^2)$ である。
<!-- theorem-end:theorem -->

## V.7 明示parameter witness

旧thermalizing-TL witnessの $N,L,C,L_0,R_b,\Omega_D,\beta_{\rm anh},\Phi_*$ は現行M57では用いない。dimensionless witnessとして

```math
a=1,
\qquad
\nu=2.0\times10^{-3},
\qquad
g_K=5.0\times10^{-4},
\qquad
c=16,
```

```math
D_0=4,
\qquad
\epsilon=2.0\times10^{-2},
\qquad
\bar\kappa_p=1,
\qquad
S_{\min}=1,
\qquad
\bar M_e=0.2,
```

```math
\tau_p=0.25,
\qquad
\bar\gamma=0.1,
\qquad
\bar M_X=0.1
```

を取る。すると

```math
g_Kc=\frac{4\nu}{a}=8.0\times10^{-3},
\qquad
D_0=\frac\nu{g_K}=4,
```

```math
E_{\min}=\epsilon^2\bar\kappa_pS_{\min}=4.0\times10^{-4},
```

```math
M_e=\epsilon^2\bar M_e=8.0\times10^{-5},
```

```math
\lambda_Y
=\frac{E_{\min}}{M_ec}
=0.3125,
\qquad
\tau_Y=3.2.
```

また

```math
\gamma_X=\epsilon^4\bar\gamma=1.6\times10^{-8},
```

```math
k_BT=\gamma_XD_0=6.4\times10^{-8},
```

```math
M_X=\epsilon^6\bar M_X=6.4\times10^{-12},
\qquad
\tau_X=M_X/\gamma_X=4.0\times10^{-4}.
```

$T_{\rm sig}=a^2/\nu=500$ に対して

```math
\tau_X\ll\tau_p\ll\tau_Y\ll T_{\rm sig}
```

である。sinusoidal periodic potentialではLifson--Jackson式から $g_K=5\times10^{-4}$ に対応するdimensionless barrier $\beta\Delta U\simeq11.102572$ を選べる。`tools/verify_m57_ballistic_tracer.py` はこれらの恒等式、fixed point、安定性、scaling、matching、新R161 current correctionを独立に再計算する。

## V.8 成立範囲と非主張

1. exactなのはR195Aのchiral恒等式、moving-reflector forceから得る $\beta_*(r)$ とその安定性、ならびに理想R161 fluxの代数である。
2. ballistic portの有限band/delay、oscillator bathのMarkov/overdamped極、periodic homogenization、Eyring--Kramers projectionは明示誤差付きの縮約であり、有限誤差を0と同一視しない。
3. ballistic TLをthermalizeしたとは主張しない。TLへequilibrium FDTを適用しない。
4. $Y_e$ はsignalを読み取るservoではなくwave pressureで受動的に動くbath cellのCOM自由度である。
5. $\mathcal J_0=2m\nu$ はsignal currentのchiral作用表示とQ3 diffusivityを結ぶNelson matchingであり、moving-reflector力学から別途生成するものではない。
6. finite-grid exact current matchingを非線形servoで作らず、smooth sectorのnative $O(a^2)$ correctionをR185の格子誤差台帳へ渡す。
