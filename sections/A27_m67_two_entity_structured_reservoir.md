@number: AA
@chapter: 付録
@title: M67 二実体finite-Hamiltonian physical parent
@status: M67をQ3-1--Q3-5の共通二実体finite-Hamiltonian physical parentとし、Q1ではM65/R204E binary-selector contractのfinite-Hamiltonian strengtheningをR211A--R211Cで与える。M37はM67 coherent module、M64/R203はM67のcanonical open effective reduction、R123有限環境はR210Bのbounded dephasing liftの有効則として維持する。R208A--R209Cはtracer/Nelson側、R210Aはcoherent-sector/R86 compatibility、R210Bはbounded finite-dephasing embedding、R211A--R211CはQ1 double-well selector liftを担う。Q3-6はM67 coherent sector上の未達課題として残し、Q2/NBL、M0、M54/M65/M66の運用状態は変更しない。

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

本付録の責務はM67をQ3共通physical parentとして固定し、さらにQ1 binary selectorのfinite-Hamiltonian strengtheningを同じ二実体architectureへ特殊化することである。coherent profileはR210Aを介してM37/R86へ、dephasing profileはR210Bを介してR123へ、continuous/finite-graph tracer profileはR208/R209を介してM64/R203A--R203Dへ接続する。Q1 binary-selector profileはR211A--R211Cを介してM65/R204E contractとR181Dへ接続する。R161/R185、R123--R125、R182、R204E、R181Dは既存の下流結果として再利用し、本付録では再証明しない。Q2のM54/R181B--R181C、M66/R205--R207、NBL型registerは本付録の直接主張に含めない。

M67の「二実体」は自由度が二個という意味ではない。一つのstructured reservoir sector $\mathcal R_{\rm str}$ が有限個のcoherent/thermal/reaction-coordinate/dephasing/held-action内部自由度を持ち、marker sector $\mathcal X$ はQ3-2/Q3-4/Q3-5でtracer、Q1 selector profileではbinary decision markerとしてactiveになる。Q3-1およびQ3-3A--Q3-3Cではmarker sectorをdecoupleしたprofileを許す。

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

とする。これはcontinuous/finite-graph tracer profileの全Hamiltonianである。Q3全体では同じ有限Hamiltonian architectureの固定specializationとして次を使う。

| M67 profile | active sector | Q3用途 |
|---|---|---|
| coherent | $H_{\rm coh}$ | Q3-1 |
| dephasing | $H_{\rm coh}+H_{\rm deph,add}^{67}$ | Q3-3A/B/C |
| continuous tracer | $H_{\rm coh}+H_\rho+H_U+H_{\rm drag}+H_X$ | Q3-2 |
| finite-graph tracer | coherent sector＋finite-graph phase-volume/current/marker specialization | Q3-4A/B/5 |
| Q1 binary selector | held-action port＋Q1 phase-volume sector＋finite marker bath＋double-well marker | Q1 M65/R204E strengthening |

profileは試行途中に確率生成のためswitchするものではなく、対象固定目標に対して開始前に固定したHamiltonian specializationである。Q3-3Cのdephasing運転とQ3-4Bのcoherent tunnelling運転は同時にactiveにしない。Q1 binary-selector profileもR189A capture終了後に固定して使い、Q3 tracer profileとの同時運転を主張しない。

coherent sectorにはM37/R86の有限局所振動子網を使う。

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

M37/R86 safe coherent sector、$K_e>M_e$、正の有限harmonic-bath parameterを取り、$r_X^\delta$ と $v_e$ が固定観測窓で有界とする。このときcontinuous/finite-graph tracer profileの全自由度は

```math
\mathcal R_{\rm str}
+
(X,P_X)
```

の二つの主要物理sectorへ分類でき、$H_{67}$ は有限古典Hamiltonianとして構成できる。$Z,\rho,j,U,\xi$ はすべてM67正準自由度から作る派生量であり、新しい独立実体を必要としない。coherent profileはreservoir/marker couplingをdecoupleした特殊化、dephasing profileはR210Bの下方有界な有限canonical sectorを追加した特殊化である。
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

ここで $\varepsilon_U^{64}$ はM64自身のbaseline errorであり、M67からM64へのcompatibility errorへ再加算しない。
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

はGaussian過程であり、kernel covarianceがDrude kernelへ一様積分収束し、increment boundが一様なら、固定 $T<T_{\rm bath\,rec}^{Q1}$ で

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

## AA.13 R209C：M67からM64へのfinite-time process compatibility

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

とする。regularized safe sectorでobservable mapがLipschitzで定数 $L_{\rm sig}$ を持つとする。R210Aのload-only relative boundを $q_{\rm load}(T)=\varepsilon_{\rm load}^{67}(T)$ とすると、$q_{\rm load}<1$ の範囲で

```math
\varepsilon_{\rm sig}(T)
\le
\min\left\{
1,
\frac{2q_{\rm load}(T)}
{1-q_{\rm load}(T)}
\right\}.
```

ここではR86のcarrier-envelope誤差を加えない。M67からM64へのcompatibilityでは両者が同じbare M37 signalを基準にするためであり、R86誤差はQ3-1でSchrödinger目標へ接続するときだけR210Aで合成する。

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


## AA.14 R210A：M67 coherent-sector / R86 finite-time compatibility

R210Aはdephasing sectorをoffにしたcoherent/tracer profileに適用する。full M67のsignal依存loadを

```math
H_R
=
H_\rho+H_U+H_{\rm drag}+H_X
```

とまとめる。$H_{U{\rm bath}},H_{\rm drag},H_X$ はcoherent変数へ直接依存せず、signalへの直接backreactionは $H_\rho+H_U$ からだけ生じる。

M37のlocal rotating envelopeを $b$、bare M37 trajectoryを $b^{37}$、full M67 trajectoryを $b^{67}$ とする。M37のsafe narrow-band parameterを

```math
\eta
=
\frac{2\|h_L\|}
{\mathcal J_0\omega_0}
<1,
\qquad
\kappa_\eta
=
(1-\eta)^{-1/4}
```

とする。R86のBogoliubov normal-envelope変換とその逆の作用素normはともに $\kappa_\eta$ 以下である。

### AA.14.1 signal load bound

regularized density portを

```math
r_X^\delta
=
b^\dagger B_X^\delta b,
\qquad
B_X^\delta\ge\beta_\rho I,
\qquad
\|B_X^\delta\|\le B_\rho
```

と書く。phase-volume sectorについて

```math
\mathcal A_\rho
=
\sum_\alpha
w_\alpha
m_\alpha\omega_\alpha^2
\lambda_\alpha^2\zeta_\alpha^2
```

と置くと、

```math
G_\rho
:=
\frac{\partial H_\rho}{\partial b^*}
=
-\frac{\mathcal A_\rho}{r_X^\delta}
B_X^\delta b,
```

従って

```math
\|G_\rho\|
\le
\frac{C_\rho\mathcal A_\rho}{\|b\|},
\qquad
C_\rho
=
\frac{B_\rho}{\beta_\rho}.
```

edge targetはsafe sectorでdegree-zeroのquadratic ratio

```math
v_e[b]
=
\frac{b^\dagger C_e b}
{b^\dagger B_e b},
\qquad
B_e\ge\beta_eI
```

として表せるものとする。R203Aのregularized local current/density dictionaryはこの形に含まれる。直接微分すると

```math
\frac{\partial v_e}{\partial b^*}
=
\frac{
C_eb\,(b^\dagger B_eb)
-
(b^\dagger C_eb)B_eb
}{
(b^\dagger B_eb)^2
}.
```

従って

```math
\left\|
\frac{\partial v_e}{\partial b^*}
\right\|
\le
\frac{\ell_e}{\|b\|},
\qquad
\ell_e
=
\frac{\|C_e\|}{\beta_e}
+
\frac{\|C_e\|\,\|B_e\|}{\beta_e^2}.
```

と取れる。



```math
L_v
=
\left(\sum_e\ell_e^2\right)^{1/2},
\qquad
\Lambda_U
=
\left[
\sum_eK_e^2|U_e-v_e|^2
\right]^{1/2}
```

とすれば、

```math
\|G_U\|
\le
\frac{L_v\Lambda_U}{\|b\|}.
```

従って

```math
\|G_{67}\|
\le
\frac{\mathcal C_{67}}{\|b\|},
\qquad
\mathcal C_{67}
=
C_\rho\mathcal A_\rho+L_v\Lambda_U.
```

### AA.14.2 保存energy shellからの明示上界

$w_{\max}=\max_\alpha w_\alpha$ とする。phase-volume energyから

```math
\mathcal A_\rho
\le
2w_{\max}H_\rho.
```

flow coreについて $A_e=K_e-M_e>0$ と置くと平方完成により

```math
\frac{P_{Y,e}^2}{2M_e}
+
P_{Y,e}U_e
+
\frac{K_e}{2}(U_e-v_e)^2
=
\frac{(P_{Y,e}+M_eU_e)^2}{2M_e}
+
\frac{A_e}{2}
\left(
U_e-\frac{K_e}{A_e}v_e
\right)^2
-
c_ev_e^2,
```

```math
c_e
=
\frac{K_eM_e}{2(K_e-M_e)}.
```

$|v_e|\le v_{e,*}$ をsafe regularizationから取り、

```math
C_{\rm flow}
=
\sum_ec_ev_{e,*}^2
```

とする。$V_{\rm ext}\ge V_{\min}$ とし、

```math
\mathcal E_R
=
H_\rho
+
H_U
+
H_{\rm drag}
+
H_X
+
C_{\rm flow}
-
V_{\min}
\ge0
```

をreservoir excess energyとする。さらに

```math
\Gamma_K
=
\max_e
\frac{K_e^2}{K_e-M_e},
```

```math
\Gamma_v
=
\left[
\sum_e
\left(
\frac{K_eM_e}{K_e-M_e}
v_{e,*}
\right)^2
\right]^{1/2}
```

なら

```math
\Lambda_U
\le
\sqrt{2\Gamma_K\mathcal E_R}
+
\Gamma_v.
```

よって

```math
\mathcal C_{67}
\le
a\mathcal E_R+b\sqrt{\mathcal E_R}+c,
```

```math
a=2C_\rho w_{\max},
\qquad
b=L_v\sqrt{2\Gamma_K},
\qquad
c=L_v\Gamma_v.
```

M67 loadはglobal carrier phaseに不変で、

```math
H_R[e^{i\theta}b]=H_R[b],
\qquad
\{b^\dagger b,H_R\}=0.
```

従って $O(\omega_0N_0)$ のcommon carrier energyとは直接energy交換せず、M37 slow spatial couplingだけが $\mathcal E_R$ を変化させる。複素正準normの保守的評価として

```math
|\dot{\mathcal E}_R|
\le
\Omega_h
\left(
a\mathcal E_R+b\sqrt{\mathcal E_R}+c
\right),
\qquad
\Omega_h
=
\frac{4\|h_L\|}{\mathcal J_0}.
```

任意の $\epsilon>0$ に対し

```math
A_\epsilon=a+\epsilon,
\qquad
B_\epsilon
=
c+\frac{b^2}{4\epsilon}
```

と置けば、

```math
\mathcal E_R(t)
\le
\mathcal E_{R,*}(T)
:=
\left[
\mathcal E_R(0)
+
\frac{B_\epsilon}{A_\epsilon}
\right]
e^{\Omega_hA_\epsilon T}
-
\frac{B_\epsilon}{A_\epsilon}.
```

したがって

```math
\mathcal C_{67}(t)
\le
C_{210}(T)
:=
a\mathcal E_{R,*}(T)
+
b\sqrt{\mathcal E_{R,*}(T)}
+
c.
```

prepared reservoir shell $\mathcal E_R(0)=O(1)$ を $N_0$ と独立に取れば $C_{210}(T)=O(1)$ である。

<!-- theorem-start:theorem -->
**定理（R210A：M67 coherent-sector / R86 finite-time compatibility）**

上のsafe regularization、$K_e>M_e$、$\eta<1$、有限prepared reservoir shellを仮定し、

```math
N_0=\|b_0\|^2
```

とする。同じ $b_0$ から始めるfull M67とbare M37について、

```math
N_0
\ge
\frac{
4TC_{210}(T)
}{
\mathcal J_0(1-\eta)^{3/2}
}
```

ならbootstrapが閉じ、

```math
q_{\rm load}(T)
:=
\sup_{t\le T}
\frac{\|b^{67}(t)-b^{37}(t)\|}{\sqrt{N_0}}
\le
\varepsilon_{\rm load}^{67}(T),
```

```math
\varepsilon_{\rm load}^{67}(T)
=
\frac{
2TC_{210}(T)
}{
\mathcal J_0N_0(1-\eta)
}.
```

prepared energy shellを固定したfamilyでは $\varepsilon_{\rm load}^{67}=O(N_0^{-1})$ である。

R86のbare M37からSchrödinger目標 $b_L$ への既存有限時間相対誤差を $\varepsilon_{86}(T)$ とすると、

```math
q_{210}(T)
=
\kappa_\eta\varepsilon_{86}(T)
+
\varepsilon_{\rm load}^{67}(T).
```

$q_{210}<1$ なら

```math
d_{\rm ray}
\left(
b^{67}(t),b_L(t)
\right)
\le
\min\left\{
1,
\frac{2q_{210}(T)}
{1-q_{210}(T)}
\right\}.
```

自然時間でR86の $\varepsilon_{86}=O(\eta)$ を用いれば

```math
q_{210}
=
O(\eta)+O(N_0^{-1}).
```
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R210A）**

R86のBogoliubov normal-envelope座標ではbare M37 propagatorはunitaryである。M67 forcingを同座標へ移すとnormは高々 $\kappa_\eta\|G_{67}\|$、局所包絡へ戻すともう一度 $\kappa_\eta$ が掛かる。Duhamel公式と上の $G_{67}$ boundを用い、bare M37の正常作用保存から得る $\|b^{37}\|\ge\kappa_\eta^{-2}\sqrt{N_0}$ の半分をbootstrap下限として使うと表示したload boundを得る。energy-shell節の微分不等式とGronwall評価により $C_{210}(T)$ は初期prepared shellから従い、独立仮定ではない。最後にR86誤差との三角不等式と規格化ベクトルの安定性を用いる。証明終。
<!-- theorem-end:proof -->

## AA.15 R210B：M67 bounded finite-dephasing embedding

現行R123のeffective Hamiltonianに現れる $I_nP_n$ couplingはprepared finite-action sectorでは正しい有限Hamiltonian lawを与える一方、$I_n$ まで全位相空間で無制限に動かすと平方完成で負の $I_n^2$ 項を生じ得る。M67 physical parentでは同じR123 lawを保ちながらglobally boundedなportへ持ち上げる。

M37 exact normal modesの先頭有限 $K$ 個について

```math
I_n
=
\mathcal J_0|c_n|^2,
\qquad
H_{\rm coh}^{(K)}
=
\sum_{n=1}^{K}\omega_nI_n
```

とする。有限環境正準対を $(\theta_n,P_n)$ とし、

```math
f(P)
=
p_*
\sin
\left(
\frac{\pi P}{2p_*}
\right),
\qquad
|f(P)|\le p_*,
\qquad
f(\pm p_*)=\pm p_*
```

を用いる。

```math
H_{\rm deph,add}^{67}
=
\sum_{n=1}^{K}
\left[
\frac{P_n^2}{2M_n}
+
\frac{\lambda}{\mathcal J_0}
I_nf(P_n)
\right],
\qquad
H_{\rm profile}^{\rm deph}
=
H_{\rm coh}
+
H_{\rm deph,add}^{67}.
```

<!-- theorem-start:theorem -->
**定理（R210B：M67 bounded finite-dephasing embedding）**

```math
\omega_{\min}
:=
\min_{1\le n\le K}\omega_n
>
\frac{|\lambda|p_*}{\mathcal J_0}
```

なら $H_{\rm profile}^{\rm deph}$ は全位相空間で下に有界である。さらに $\theta_n$ とmodal angleはHamiltonian中に現れないため

```math
\dot I_n=0,
\qquad
\dot P_n=0.
```

開始面で各 $P_n=\pm p_*$ を独立等重みに調製し環境を読まなければ、$n\ne m$ の縮約相関は厳密に

```math
C_{nm}^{67}(t)
=
C_{nm}(0)
e^{-i(\omega_n-\omega_m)t}
\cos^2
\left(
\frac{\lambda p_*t}{\mathcal J_0}
\right),
```

対角成分は $C_{nn}(t)=C_{nn}(0)$ となる。従って

```math
T_{\rm dec}
=
\frac{\pi\mathcal J_0}{2|\lambda|p_*},
\qquad
T_{\rm rec}
=
2T_{\rm dec}.
```

R123との差はdephasing factorではなく、M37 exact normal-mode差 $\mathcal J_0(\omega_n-\omega_m)$ とSchrödinger低位energy差の既存R86/R182誤差だけである。よってR123有限環境はM67 structured reservoir内部のbounded dephasing profileとして実装でき、新しい第三物理実体を要求しない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R210B）**

$|f(P_n)|\le p_*$ から

```math
\omega_nI_n
+
\frac{\lambda}{\mathcal J_0}I_nf(P_n)
\ge
\left(
\omega_n-
\frac{|\lambda|p_*}{\mathcal J_0}
\right)I_n
\ge0.
```

bath kinetic energyも非負なので下界を得る。$I_n,P_n$ はそれぞれの共役angleがcyclicなため保存される。prepared pointsでは $f(P_n)=\pm p_*$ なので、独立二点分布に対する二つのmodal phase factorの平均は $\cos^2(\lambda p_*t/\mathcal J_0)$ となる。証明終。
<!-- theorem-end:proof -->

## AA.16 数値検証契約と未主張範囲

M67 supporting simulationではHamiltonian drift、M37 ideal signalとの状態方向誤差、$U_X-v_\delta$、phase-volume mean force、finite-bath memory、tracer分布を同じparameter setで監査する。R210A/Bを含むrequired解析検算とfull trajectory simulationを区別し、後者だけからA2を昇格しない。$N_0$、$N_\rho$、$K_U$、$\tau_U$、$\tau_{\rm mem}$、bath mode数、格子幅を独立に振り、一つの改善を複数誤差へ二重計数しない。

M67をQ3 common physical parentへ昇格してもM37、M64、R123の結果を削除しない。M37はactive coherent module、M64/R203はactive open effective reduction、R123はR210Bで物理liftされたactive dephasing lawとして維持する。R211A--R211CはQ1 binary selectorだけを追加specializeし、M65/R204A・R204D--R204Fをcanonical open selectorとして維持する。A1/A2/B1--B3、M0の判定は変更しない。Q2/NBL特殊化は将来候補であり、H/T/CNOTの一般実装、NBL Born sampling、mixing/resource boundを本付録から推論しない。$R_i^\delta=|Z_i|^2+\delta q_iS$ のglobal $S$ を完全局所化する問題もstrict-locality strengtheningとして残す。


## AA.17 Q1 binary-selector profileとsafe branch

R189Aのcapture終了後に保持された二作用を

```math
A_\pm\ge0,
\qquad
A_\Sigma=A_++A_->0,
\qquad
\widehat p_\pm=\frac{A_\pm}{A_\Sigma}
```

とする。R189Aでは保持窓後も $\bar J_L+\bar J_R=J_\Sigma$ が厳密に成り立つので、Q1 selectorでは $A_\Sigma=J_\Sigma$ を固定総作用scaleとして扱う。M65と同じ固定cutoff $0<\tau_{\rm cut}<1/2$ を使い、

```math
\widehat p_\pm\ge\tau_{\rm cut}
```

をQ1 double-well profileのsafe branchとする。cutoff外およびexact endpointはR204D/R204Eで既に用いる固定線形comparatorへ渡し、double-well profileへ $\log0$ を持ち込まない。

固定装置scale $A_*>0$ に対して $a_\pm=A_\pm/A_*$ とする。Hamiltonianを全位相空間でsmoothに定義するため、正のsmooth extension $\bar a_\pm(I_+,I_-)$ を選び、safe branchでは厳密に

```math
\bar a_\pm=a_\pm
```

とする。さらに装置定数 $0<a_{\rm floor}<a_{\rm ceil}<\infty$ を選び、全位相空間で $a_{\rm floor}\le\bar a_\pm\le a_{\rm ceil}$ とする。safe branch外のextensionはHamiltonian regularizationだけを担い、Born重みを計算する外部tableとして使わない。固定 $A_\Sigma=J_\Sigma$ と $\widehat p_\pm\in[\tau_{\rm cut},1-\tau_{\rm cut}]$ によりsafe held-action集合はcompactになる。

Q1 profileではrunning W2 signalはR189A capture終了後にselectorから切り離す。M67 structured reservoir内部にheld-action pair、phase-volume modes、finite marker bathを置き、別sector $\mathcal X=(X,P_X)$ をbinary markerとして使う。

## AA.18 R211A：M67 Q1 double-well finite-Hamiltonian construction

held-action pairをcanonical action-angle変数

```math
(I_+,\theta_+),
\qquad
(I_-,\theta_-),
\qquad
I_\pm=A_\pm
```

として受ける。selector Hamiltonianを $\theta_\pm$ に依存させない。

裸のmarker potential $W_0$ はevenなdouble wellとし、

```math
W_0(-X)=W_0(X)
```

を満たす。数値witnessでは

```math
W_0(X)=16(X^2-1)^2
```

を使うが、定理本体は一般のsmooth even double wellへ適用する。

collar幅 $\ell>0$ とsmooth step $\chi_\ell$ を

```math
\chi_\ell(X)=0
\quad
(X\le-\ell),
```

```math
\chi_\ell(X)=1
\quad
(X\ge\ell)
```

となるよう選び、

```math
\log w_\ell(X)
=
[1-\chi_\ell(X)]\log\bar a_-
+
\chi_\ell(X)\log\bar a_+
```

とする。safe branchでは左右でそれぞれ $w_\ell=a_-$、$w_\ell=a_+$ となり、中央に第三のphase-volume plateauを置かない。

Q1 phase-volume sectorを

```math
H_{\rm pv}^{Q1}
=
\sum_{\alpha=1}^{N_\rho}
\left[
\frac{\Pi_\alpha^2}{2m_\alpha}
+
\frac{m_\alpha\omega_\alpha^2}{2}
w_\ell(X)^{-2q_\alpha}\zeta_\alpha^2
\right],
```

```math
q_\alpha>0,
\qquad
\sum_\alpha q_\alpha=1
```

とする。marker frictionにはR209Bと同型のfinite harmonic bath

```math
H_B^{Q1}
=
\sum_{\mu=1}^{N_B}
\left[
\frac{p_\mu^2}{2m_\mu}
+
\frac{m_\mu\omega_\mu^2}{2}
(q_\mu-c_\mu X)^2
\right]
```

を使う。固定 $X$ でbath座標の平行移動はJacobian 1なので、このbathはstatic Born biasを追加しない。

Q1 selector Hamiltonianでは $H_{\rm hold}(I_+,I_-)$ をsmoothかつ下に有界に選ぶ。全Hamiltonianを

```math
H_{67}^{Q1}
=
H_{\rm hold}(I_+,I_-)
+
\frac{P_X^2}{2M_X}
+
W_0(X)
+
H_{\rm pv}^{Q1}
+
H_B^{Q1}
```

とする。

<!-- theorem-start:theorem -->
**定理（R211A：M67 Q1 double-well finite-Hamiltonian construction）**

safe held-action domainを含み $a_{\rm floor}\le\bar a_\pm\le a_{\rm ceil}$ を満たすsmooth positive extensionを取り、$W_0$、$\chi_\ell$、下に有界な $H_{\rm hold}$、有限phase-volume modes、finite harmonic bathを上のように選ぶ。このとき $H_{67}^{Q1}$ は有限自由度のsmoothかつ下に有界なclassical Hamiltonianとして構成でき、

```math
\dot I_\pm
=
-\frac{\partial H_{67}^{Q1}}{\partial\theta_\pm}
=
0
```

がdecision区間で厳密に成立する。

固定 $X,I_\pm$ のphase-volume canonical積分は

```math
Z_{\rm pv}
=
Z_{\rm pv}^0w_\ell(X)
```

を与え、markerのpotential of mean forceは

```math
F_\ell(X)
=
W_0(X)
-
k_BT\log w_\ell(X)
+
C
```

となる。

safe action-ratio集合全体で $F_\ell$ が左右二つの局所極小と中央collar内の一つの局所極大だけを持つよう $W_0$、$\ell$ を選べる。この場合stable marker basinは $+$ と $-$ の二つだけであり、中央に第三の安定pointer状態を持たない。全自由度はM67の

```math
\mathcal R_{\rm str}
+
\mathcal X_{\rm marker}
```

という二つの主要physical sectorへ分類できる。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R211A）**

$\theta_\pm$ がcyclicなので $I_\pm$ の保存はHamilton方程式から直ちに従う。各phase-volume oscillatorについて $\widetilde\zeta_\alpha=w_\ell^{-q_\alpha}\zeta_\alpha$ と変数変換すればJacobianは $w_\ell^{q_\alpha}$ であり、積を取ると $\sum_\alpha q_\alpha=1$ から全Jacobianが $w_\ell$ になる。従って $Z_{\rm pv}=Z_{\rm pv}^0w_\ell$ とfree-energy式を得る。finite marker bathは座標平行移動なので固定 $X$ partitionへ追加の $X$ 依存factorを生じない。$H_{\rm hold}$、$W_0$、phase-volume quadratic terms、finite marker bathはそれぞれ下限を持ち、$\bar a_\pm$ は正の上下界を持つので全Hamiltonianも下に有界である。固定 $A_\Sigma$ とsafe ratio条件からsafe held-action集合はcompactであり、$\partial_X\log w_\ell$ とその必要微分は有限である。裸のdouble-well curvature/barrierをこれらの有限摂動に対して十分強く選べば、左右二極小と中央一極大だけを一様に維持できる。証明終。
<!-- theorem-end:proof -->

R211AはBorn確率をまだ主張しない。これはfinite-Hamiltonian device constructionとheld-action invarianceだけを閉じる。

## AA.19 R211B：M67 Q1 double-well Born kernelとR204E compatibility

R211Aのpotential of mean forceに対するideal overdamped markerを

```math
dX_t^D
=
-\mu F_\ell'(X_t^D)dt
+
\sqrt{2\mu k_BT}\,dW_t
```

とする。$0<\ell<d<L$ を取り、$\pm L$ を数学上のdeep commitment surface、$\pm d$ を固定decision時刻のterminal readout thresholdとする。

sharp-interface $\ell=0$ では

```math
w_0(X)
=
\begin{cases}
a_-,
&
X<0,
\\
a_+,
&
X>0.
\end{cases}
```

1次元committor $q_+(x)=P_x(\tau_{+L}<\tau_{-L})$ は

```math
q_+(x)
=
\frac{
\displaystyle
\int_{-L}^{x}
e^{\beta F_0(y)}dy
}{
\displaystyle
\int_{-L}^{L}
e^{\beta F_0(y)}dy
}.
```

$W_0$ のeven symmetryから

```math
q_+(0)
=
\frac{a_+}{a_++a_-}
=
\widehat p_+,
\qquad
q_-(0)=\widehat p_-.
```

有限collarについて

```math
G(x)=e^{\beta W_0(x)},
\qquad
I=\int_0^LG(x)dx,
\qquad
I_\ell=\int_0^\ell G(x)dx,
\qquad
r_\ell=\frac{I_\ell}{I},
```

```math
\rho_\tau
=
\frac{1-\tau_{\rm cut}}{\tau_{\rm cut}}
```

と置く。$(\rho_\tau-1)r_\ell<1$ なら、

```math
\varepsilon_{\rm col}
:=
|q_{\ell,+}(0)-\widehat p_+|
\le
\frac{
(\rho_\tau-1)r_\ell
}{
2[
1-(\rho_\tau-1)r_\ell
]
}.
```

初期markerが $|X_0|\le\delta_0$ にある場合、

```math
L_q
=
\sup_{|x|\le\delta_0}
|q_\ell'(x)|
```

として

```math
\varepsilon_{\rm launch}
\le
L_q\delta_0.
```

実装側ではfirst-event memoryを追加せず、固定decision時刻 $T$ に

```math
g_d(X)
=
\begin{cases}
+,
&
X\ge d,
\\
-,
&
X\le-d,
\\
\varnothing,
&
|X|<d
\end{cases}
```

と読む。ideal diffusion kernelを $K_D^T=\mathcal L(g_d(X_T^D))$ とする。

deep commitment未到達を

```math
\varepsilon_{\rm surv}(T)
=
P(\tau_L>T),
\qquad
\tau_L
=
\inf\{t:|X_t^D|\ge L\},
```

一度deep commitmentした後にterminal thresholdまで戻る確率を

```math
r_+(T)
=
P_{+L}(\tau_d\le T),
\qquad
r_-(T)
=
P_{-L}(\tau_{-d}\le T),
```

```math
\varepsilon_{\rm ret}(T)
\le
q_{\ell,+}r_+(T)
+
q_{\ell,-}r_-(T)
```

とする。

finite-Hamiltonian markerを $X_t^{67}$ とし、R209B/Cと同じfinite-bath eliminationとsmall-mass reductionをQ1 profileへ特殊化して、固定時刻で

```math
W_1
\left(
\mathcal L(X_T^{67}),
\mathcal L(X_T^D)
\right)
\le
\varepsilon_X(T)
```

を得る。Q1 profileではflow/current sectorを使わないため、

```math
\varepsilon_X(T)
=
\varepsilon_{\rm bath}^{X}(T)
+
\varepsilon_{\rm od}^{X}(T)
+
\varepsilon_{\rho}^{X}(T)
+
\varepsilon_{\rm init}^{X}
```

と取る。equal phase-volume weightsでは $\varepsilon_\rho^X=O(T/\sqrt{N_\rho})$、small-mass項は

```math
\varepsilon_{\rm od}^{X}(T)
\le
C_T
\left[
\frac{M_X}{\gamma}B_*
+
\sqrt{
\nu\frac{M_X}{\gamma}
}
\right].
```

threshold近傍質量を

```math
\omega_d(\delta,T)
=
P_D
\left(
\bigl||X_T^D|-d\bigr|
\le\delta
\right)
```

とすれば、Wasserstein couplingとMarkov inequalityから

```math
\varepsilon_{\rm cg}(T)
:=
D_{\rm TV}
\left(
\mathcal L(g_d(X_T^{67})),
\mathcal L(g_d(X_T^D))
\right)
\le
\inf_{\delta>0}
\left[
\frac{\varepsilon_X(T)}{\delta}
+
\omega_d(\delta,T)
\right].
```

ideal diffusion densityを $\rho_D(x,T)$ とし、threshold近傍で $\rho_D\le m_d(T)$ なら補助上界

```math
\varepsilon_{\rm cg}(T)
\le
4
\sqrt{
m_d(T)\varepsilon_X(T)
}
```

も得る。

<!-- theorem-start:theorem -->
**定理（R211B：M67 Q1 double-well Born kernel / R204E compatibility）**

R211Aのsafe Q1 profileを取り、$0<\ell<d<L$、有限decision時刻 $T<T_{\rm bath\,rec}^{Q1}$ を選ぶ。finite-Hamiltonian terminal result kernelを

```math
K_{67}^T
=
\mathcal L(g_d(X_T^{67}))
```

とし、保持作用比に対するcomplete Born kernelを

```math
K_{\widehat p}
=
(\widehat p_+,\widehat p_-,0)
```

とする。このとき

```math
D_{\rm TV}
\left(
K_{67}^T,
K_{\widehat p}
\right)
\le
\varepsilon_{211B}(T),
```

```math
\varepsilon_{211B}
=
\varepsilon_{\rm col}
+
\varepsilon_{\rm launch}
+
\varepsilon_{\rm surv}
+
\varepsilon_{\rm ret}
+
\varepsilon_{\rm cg}.
```

各項は上の1次元quadrature、backward equation、one-time Wasserstein boundから有限に評価できる。

さらにsafe action-ratio集合を固定したまま、collar幅、launch幅、finite phase-volume mode数、finite-bath近似、small-mass parameter、recurrence time、well depthとdecision windowを順に選ぶparameter族で

```math
\varepsilon_{211B}
\longrightarrow0
```

とできる。従ってM67 Q1 profileはR204E binary selector contractを任意精度で満たすfinite-Hamiltonian physical liftを与える。

R211BはM65/R204Aの指数Poisson waiting-time lawや $\lambda_\pm=\kappa a_\pm$ を再現するとは主張しない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R211B）**

sharp-interface committor式は1次元reversible diffusionのscale functionから従い、$W_0$ のeven symmetryによって左右積分の共通factorが消え、保持作用比を厳密に得る。finite collarはsharp profileとの差が $|X|<\ell$ にだけ支持を持つため、左右scale integralの摂動評価から $\varepsilon_{\rm col}$ を得る。launch errorはcommittorの平均値定理で抑える。

eventual deep-commitment signと固定時刻basin readoutが異なるpathは、時刻 $T$ までに $\pm L$ へ到達しない場合か、到達後に対応する $\pm d$ まで戻る場合へ含まれるので、自然couplingから $\varepsilon_{\rm surv}+\varepsilon_{\rm ret}$ で抑えられる。

finite-Hamiltonian lawとideal diffusion lawをone-time $W_1$ couplingし、coupling距離が $\delta$ を超える確率をMarkov inequalityで $\varepsilon_X/\delta$ と評価する。両marker位置がthresholdから $\delta$ 以上離れ、coupling距離が $\delta$ 以下なら $g_d$ の結果は一致するため、残る不一致確率は $\omega_d(\delta,T)$ 以下である。$\delta$ について下限を取れば $\varepsilon_{\rm cg}$ を得る。各誤差項を順次小さくできるparameter族を選べば最後の主張が従う。証明終。
<!-- theorem-end:proof -->

### AA.19.1 required numerical witness

dimensionless units $k_BT=\mu=x_0=1$ で、

```math
W_0(X)=16(X^2-1)^2,
\qquad
\tau_{\rm cut}=0.07,
```

```math
\ell=0.01,
\qquad
d=0.40,
\qquad
L=0.78,
\qquad
T=0.22,
\qquad
\delta_0=5\times10^{-4}
```

を取る。tools/verify_m67_q1_first_passage.py はsafe action ratio全域でdouble-well topology、smooth-collar committor、launch bound、finite-time survival、return、terminal threshold mass、Wasserstein-to-result transferを同じparameter setで検算する。

現行deterministic finite-difference witnessでは

```math
\varepsilon_{\rm col}^{\max}
<
4.8\times10^{-3},
```

```math
\varepsilon_{\rm launch}
<
1.7\times10^{-3},
```

```math
\varepsilon_{\rm surv}^{\max}
<
2.0\times10^{-5},
\qquad
\varepsilon_{\rm ret}^{\max}
<
5.0\times10^{-4}.
```

finite-Hamiltonian reduction target $\varepsilon_X(T)\le10^{-4}$ では直接threshold-mass optimizationを使って

```math
\varepsilon_{211B}
<
8.0\times10^{-3}.
```

$\varepsilon_X(T)\le10^{-3}$ というloose targetでも

```math
\varepsilon_{211B}
<
1.3\times10^{-2}
```

を満たす。これはfull finite-Hamiltonian trajectory simulationによるA2判定ではなく、R211Bの同時parameter領域が空でないことを示すrequired numerical regressionである。

## AA.20 R211C：M67 Q1 selector physical-lift composition

R211Bは与えられた保持作用比 $\widehat p$ に対するphysical selector errorだけを扱う。R189Aの作用保持誤差はここで初めて合成する。

safe interior branchでは

```math
\varepsilon_{\rm int}^{67}
\le
\varepsilon_{189A}
+
\varepsilon_{211B}
+
\varepsilon_{\rm rec}.
```

cutoff外ではM65/R204Dと同じ固定線形comparatorを使い、

```math
\varepsilon_{\rm edge}^{67}
\le
\tau_{\rm cut}
+
\varepsilon_{189A}
+
\varepsilon_{\rm cmp}
+
\varepsilon_{\rm rec}.
```

従って

```math
\varepsilon_{\rm sel}^{67}
=
\max
\left\{
\varepsilon_{\rm int}^{67},
\varepsilon_{\rm edge}^{67}
\right\}.
```

safe nonempty resultについて真のprojector weightには

```math
p_r
\ge
\tau_{\rm state}^{67}
:=
\tau_{\rm cut}
-
\varepsilon_{189A}
>0
```

という一様下限を与える。

<!-- theorem-start:theorem -->
**定理（R211C：M67 Q1 selector physical-lift composition）**

R189A、R211A、R211Bの条件を満たし、decision時刻 $T$ のterminal result $Y\in\{+,-,\varnothing\}$ をR112型有限recordへ固定してからR181D routerを開くとする。このときM67 Q1 selectorはR204E binary selector contractを

```math
\varepsilon_{\rm sel}
=
\varepsilon_{\rm sel}^{67},
\qquad
\tau_{\rm state}
=
\tau_{\rm state}^{67}
```

として満たす。

従ってR181Dを変更せず適用でき、既存R189Bのdistribution errorはM67 physical-lift経路では

```math
\varepsilon_{189B,67}^{\rm dist}
\le
\varepsilon_{\rm sel}^{67}
+
\varepsilon_{\rm lat}
```

と評価できる。

selector parameter setと有限decision時間 $T_{211}$、R112 record時間 $T_{\rm record}$、R181D router時間 $T_F$ を先に固定し、その後R187のweak-coupling極を取れば

```math
\Omega_\kappa
\left(
T_{211}
+
T_{\rm record}
+
T_F
\right)
\longrightarrow0
```

とできる。従ってR189Cの有限2回Rabi--Zeno比較へ同じ試行内で接続できる。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R211C）**

interior branchではR211Bのcomplete-result TV errorへR189A作用保持誤差と有限record errorを三角不等式で一度だけ加える。edge branchではR204Dと同じ固定線形comparatorを使うため表示した上界を得る。safe branchの理想重み下限から $\tau_{\rm state}^{67}>0$ が従う。R204Eはselector内部のwaiting-time law、state数、bath実装を要求せず、complete-result TV bound、safe-state lower bound、record-before-router、Born tableを外部入力しないこと、$\varnothing$ を捨てないことだけを要求するため、R211A/B構成はそのままcontractへ入る。R181DとR189B/R189Cの既存証明はselector contractだけに依存するので変更不要である。証明終。
<!-- theorem-end:proof -->

R211A--R211CはM65を置換しない。M65/R204A・R204Dはcanonical open selector、R211A/Bはfinite-Hamiltonian physical lift、R204Eは両者が共有するinterface、R181Dはselector-independent projector routerとして維持する。
