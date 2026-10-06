@number: AA
@chapter: 付録
@title: M67 二実体finite-Hamiltonian physical parent
@status: M67をQ3-1--Q3-5の共通二実体finite-Hamiltonian physical parentとし、continuous Q3-2は付録AC/R214A--R214Bをrequired profileとする。draft-149以後R214A/B本体はgeneric density/flow port theoremで、current M37/M64 specializationだけがR210A coherent-load stabilityとR209A flow compatibilityを使う。R209Bはgeneric finite-bath/FDT補題として再利用する。Q1ではR211A--R211C、Q2 thermal sectorではR212A--R212Cをphysical liftとして与え、付録AB/R213A--R213DはQ2 signal/NBL/register/gate candidateのまま維持する。

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

本付録の責務はM67をQ3共通physical parentとして固定し、さらにQ1 binary selectorのfinite-Hamiltonian strengtheningを同じ二実体architectureへ特殊化することである。coherent profileはgeneric R210Aを介してM37/R86へ、dephasing profileはR210Bを介してR123へ、continuous tracer profileはR214A/R214Bを介してM64/R203A--R203Cへ、finite-graph tracer profileはR208D/R203Dへ接続する。R209A/R209Bは両profileから再利用できるgeneric flow / finite-bath補題として扱う。Q1 binary-selector profileはR211A--R211Cを介してM65/R204E contractとR181Dへ接続する。R161/R185、R123--R125、R182、R204E、R181Dは既存の下流結果として再利用し、本付録では再証明しない。Q2についてはR212A--R212CがM66/R205 thermal layerとR207A/R207Cのthermal physical liftを本付録の直接主張へ加える。M54/R181B--R181Cのsignal/register/gateを置換する候補は付録AB/R213A--R213Dへ分離する。R206 common-hub apparatus全体のfinite-Hamiltonian liftは依然として本付録・付録ABの直接主張に含めない。

M67の「二実体」は自由度が二個という意味ではない。一つのstructured reservoir sector $\mathcal R_{\rm str}$ が有限個のcoherent/thermal/reaction-coordinate/dephasing/held-action内部自由度を持ち、marker sector $\mathcal X$ はQ3-2/Q3-4/Q3-5でtracer、Q1 selector profileではbinary decision markerとしてactiveになる。Q3-1およびQ3-3A--Q3-3Cではmarker sectorをdecoupleしたprofileを許す。

### R214 continuous-tracer required mainline

draft-146ではR214A--R214BをQ3 continuous-tracer profileの唯一のactive finite-Hamiltonian bridgeとして維持し、旧R208B/R208C/R209Cをactive resultから退役した。draft-149以後R214本体はgeneric density/flow port theoremであり、R209Bをgeneric finite-bath/FDT lemmaとして使う。current M37/M64 specializationではR210Aがcoherent-load stability、R209Aがflow compatibilityを供給する。R208Dはcontinuous/finite-graphを振り分けるstructural bridgeとして残し、finite-graph profileへR214を流用しない。

## AA.2 profile別Hamiltonianとcoherent sector

M67は用途ごとに固定したfinite-Hamiltonian profileの族として使う。共通coherent sectorを $H_{\rm coh}$、profile固有の残りを $H_R^{(p)}$ と書き、

```math
H_{67}^{(p)}
=
H_{\rm coh}
+
H_R^{(p)}
```

とする。continuous Q3-2のrequired profileは付録ACの

```math
H_{67}^{\rm db}
=
H_{\rm coh}
+
H_{\rm db}
+
H_{{\rm db},B}
+
H_U
+
H_{\rm drag}
+
H_X
```

である。finite-graph/Q1/Q2のphase-volume構成はR212A、R211、各open/effective interfaceへ責務分離し、旧continuous $H_\rho$ profileはactive Q3 physical parentとして使わない。

| M67 profile | active sector | 用途 |
|---|---|---|
| coherent | $H_{\rm coh}$ | Q3-1 |
| dephasing | $H_{\rm coh}+H_{\rm deph,add}^{67}$ | Q3-3A/B/C |
| continuous tracer | $H_{67}^{\rm db}$（付録AC） | Q3-2 |
| finite-graph tracer | coherent sector＋R212A型phase-volume/current/marker specialization | Q3-4A/B/5 |
| Q1 binary selector | held-action port＋R211 phase-volume sector＋finite marker bath＋double-well marker | Q1 M65/R204E strengthening |
| Q2 thermal | R212A--R212C thermal specializations | Q2 thermal physical parent |

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

## AA.3 phase-volume責務の分離

draft-146以後、Q3 continuous-tracerのosmotic free energyとsignal backreactionは付録AC/R214A--R214Bが担う。旧continuous $H_\rho$ のinverse-designed phase-volume sectorはactive Q3 resultから退役し、数式・証明は退役メモとGit履歴を参照する。

phase-volume原理そのものは退役しない。finite-Hamiltonian phase-volume / mean-flowの一般埋込みはR212A、Q1 binary selector固有のphase-volume collarはR211、M64 open/effective partition identityはR203B、finite-graph位置lawはR203Dがそれぞれ担う。したがってQ3 continuous branchの退役をQ1/Q2/finite-graphへ波及させない。

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
\tau_{\rm fast}^{(p)}
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

M37/R86 safe coherent sectorを共通部とし、各profile固有Hamiltonianが有限自由度・下方有界で、必要なlocal targetとcouplingが固定観測窓で有界とする。このときQ3/Q1/Q2で用いるM67 profileの全自由度は

```math
\mathcal R_{\rm str}
+
(X,P_X)
```

の二つの主要物理sectorへ分類でき、$H_{67}^{(p)}$ は有限古典Hamiltonianとして構成できる。$Z,\rho,j,U,\xi$ はすべてM67正準自由度から作る派生量であり、新しい独立実体を必要としない。continuous profileの具体構成はR214A/B、finite-graphのphase-volume側はR212A/R203D、coherent/dephasing profileはR210A/R210Bへ委譲する。
<!-- theorem-end:theorem -->

## AA.8--AA.9 旧R208B/R208Cの退役境界

draft-146でR208BとR208Cをactive resultから退役する。

- 旧R208Bのcontinuous phase-volume osmotic force / $N_\rho^{-1/2}$ fluctuation / $O(N_0^{-1})$ load責務はR214A/R214Bへ置換する。
- 旧R208Cのfinite harmonic moving-bath / GLE / FDT / Markov責務はgeneric R209Bへ吸収する。
- phase-volume原理一般はR212A、M64 open/effective partition identityはR203Bとして残るため、退役はそれらを反証しない。
- 結果ID R208B/R208Cは再利用しない。最終active主張は退役メモとdraft-145以前のGit履歴を参照する。

## AA.10 R208D：M64へのprofile-dispatch有限時間bridge

<!-- theorem-start:theorem -->
**定理（R208D：M67 profileからM64 Q3 lawへのstructural bridge）**

R208Aの二実体finite-Hamiltonian parentを共通入口とする。continuous Q3-2では付録AC/R214A--R214Bをrequired reductionとし、R209A/R209Bをgeneric flow / finite-bath補題として用いてM64/R203Cへ接続する。finite-graph Q3-4A/Q3-4B/Q3-5ではR214を要求せず、R212A型phase-volume/current/marker specializationからR203Dへ渡す。

continuous branchでは

```math
\mathrm{M67}^{\rm db}
\xrightarrow{R214A,R214B}
\mathrm{M64}/R203C
\xrightarrow{}
R161/R185,
```

finite-graph branchでは

```math
\mathrm{M67}^{\rm graph}
\xrightarrow{R208D}
\mathrm{M64}/R203D
\xrightarrow{}
R161
```

と責務を分ける。R208D自身はR214BまたはR203Dで既に評価されたprocess-law errorを再加算せず、同じsignal/current interfaceを下流へ渡すstructural corollaryである。
<!-- theorem-end:theorem -->

R208B/R208C/R209Cはdraft-146でactive resultから退役した。R208Dは結果IDを維持し、continuous branchではR214A/B、finite-graph branchではR212A/R203Dをdispatchする。

## AA.11 R209A：generic local-flow compatibility

<!-- theorem-start:theorem -->
**定理（R209A：M67 generic local-flow compatibility）**

任意のM67 profileで、同じsignal $b$ から作るedge target $v_e[b]$ を共有するcanonical effective flow

```math
\tau_U\dot U_e^{\rm eff}
=
-U_e^{\rm eff}+v_e[b]
```

と、M67 finite-Hamiltonian flow sectorのfast-bath平均

```math
\tau_U\dot{\bar U}_e^{67}
=
-\bar U_e^{67}
+
v_e[b]
+
R_{U,e},
\qquad
|R_{U,e}|\le\varepsilon_{H,U}
```

を比較する。このとき

```math
|\bar U_e^{67}(t)-U_e^{\rm eff}(t)|
\le
e^{-t/\tau_U}
|\bar U_e^{67}(0)-U_e^{\rm eff}(0)|
+
(1-e^{-t/\tau_U})\varepsilon_{H,U}.
```

same-prepared flowなら
```math
\sup_{t\le T}|\bar U_e^{67}-U_e^{\rm eff}|
\le\varepsilon_{H,U}.
```

moving material frame
```math
\widetilde U_X^{67}
=
\sum_e\chi_e(X)\dot Y_e
```
に対して
```math
|\widetilde U_X^{67}-U_X^{\rm eff}|
\le
\varepsilon_{H,U}+\varepsilon_Y.
```

この定理はtarget $v_e[b]$ の具体的なdensity dictionaryを仮定しない。Q3-2では $U^{\rm eff}=U^{64}$、$v_e[b]$ をR214の $J/\widetilde\rho$ dictionaryへ特殊化し、finite-graphではR203D側のtargetへ特殊化する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R209A）**

差 $E_e=\bar U_e^{67}-U_e^{\rm eff}$ は
```math
\tau_U\dot E_e=-E_e+R_{U,e}
```
を満たすのでvariation of constantsで最初の評価を得る。material-frame boundは $\dot Y_e=U_e+P_{Y,e}/M_e$ とpartition of unityから従う。証明終。
<!-- theorem-end:proof -->

## AA.12 R209B：generic finite harmonic bath / Markov--FDT reduction

resolved coordinate $y$ とprofile変数 $z$ に対し、translated finite harmonic bath

```math
H_B[y;z]
=
\sum_{\mu=1}^{N_B}
\left[
\frac{P_\mu^2}{2m_\mu}
+
\frac{m_\mu\omega_\mu^2}{2}
(\zeta_\mu-c_\mu y(z))^2
\right]
```

を考える。固定 $y$ でのbath partitionはtranslationにより $y$ に依存しない。

<!-- theorem-start:theorem -->
**定理（R209B：generic finite harmonic bath / Markov--FDT reduction）**

上のbathを厳密に消去するとresolved coordinateには

```math
M_y\ddot y
+
\partial_yV
+
\int_0^t
\Gamma_N(t-s)\dot y(s)ds
=
\xi_N(t),
```

```math
\Gamma_N(t)
=
\sum_\mu
m_\mu\omega_\mu^2c_\mu^2
\cos(\omega_\mu t),
qquad
\langle\xi_N(t)\xi_N(s)\rangle
=
k_BT\Gamma_N(t-s)
```

を得る。target Drude kernel
```math
\Gamma_D(t)=\frac{\gamma}{\theta}e^{-t/\theta}
```
に対し
```math
\varepsilon_\Gamma(T)
=
\int_0^T|\Gamma_N(t)-\Gamma_D(t)|dt
```
と置けば、smooth input $f$ について
```math
|\Gamma_D*f-\gamma f|
\le
\gamma
\int_0^\infty
\frac{e^{-r/\theta}}{\theta}
|f(t-r)-f(t)|dr
```
であり、Lipschitz inputでは右辺は $O(\gamma\theta)$ である。kernel covarianceの積分収束と一様increment boundの下で、積分noise過程は固定 $T<T_{\rm rec}$ 上
```math
\int_0^t\xi_N(s)ds
\Longrightarrow
\sqrt{2\gamma k_BT}\,W_t
```
と収束する。finite spectrumのrecurrenceは $T_{\rm rec}\sim2\pi/\Delta\omega$ で管理する。

このgeneric resultには次の三つのspecializationが含まれる。

1. flow coordinate $y=U_e$：R209Aの $\varepsilon_{H,U}$ を与える。
2. tracer drag channel $y=s_c(X)-\eta_c$：tight-frame $\sum_cg_c^2=1$ により一定frictionを得て、
   ```math
   \sum_cg_cg_c'=0
   ```
   なのでwhite-noise極のStratonovich correctionは0である。
3. R214 dumbbell内部座標 $y=r_a$：各Cartesian成分に同じfinite-bath FDT/Drude縮約を適用できる。

従ってR209Bは特定のphase-volume profileに依存しないM67共通finite-bath lemmaである。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R209B）**

harmonic bathの線形方程式をDuhamel表示して $\zeta_\mu$ を消去すればmemory kernelとFDTを得る。Drude convolution差には上のmodulus-of-continuity bound、finite-spectrum差には $L^1$ kernel normを使う。Gaussian noiseの有限次元分布はcovariance収束から、一様tightnessはincrement boundから従う。translated bathのpartition independenceはunit-Jacobian shift、drag specializationのzero correctionはtight-frame identityの微分から従う。証明終。
<!-- theorem-end:proof -->

### R209B finite-window OU/Langevin realization corollary

Ford--Kac--Mazur型のcoupled-oscillator bath [12] およびZwanzig型のharmonic-bath消去 [14] に従い、resolved coordinate $y_a$ にtranslated finite harmonic bath

```math
H_{B,a}
=
\sum_{\mu=1}^{N_{B,a}}
\left[
\frac{p_{a\mu}^2}{2m_{a\mu}}
+
\frac{m_{a\mu}\omega_{a\mu}^2}{2}
(q_{a\mu}-c_{a\mu}y_a)^2
\right]
```

を接続する。有限bathの厳密消去はR209BのGLE/FDTを与える。任意の固定有限時間 $0\le t\le T<T_{\rm rec}$ で、target short-memory kernelとfinite-spectrum covarianceを十分よく近似し、必要ならresolved inertiaを小さく取れば、対応するMarkov Langevinまたは線形OU型open lawの有限時間lawを任意精度で近似できる。

このcorollaryは有限自由度Hamiltonian bathが無限時間にわたり厳密なwhite noiseを生成するとは主張しない。Q1/R211ではphase-volume auxiliary coordinate $y_a=\zeta_\alpha$ とmarker $y_a=X$ にこの有限時間realizationを用い、open OU/Langevin計算とfinite-Hamiltonian liftの責務を分離する。

## AA.13 旧R209C process bridgeの退役境界

draft-146でR209Cをactive resultから退役する。R209Cのsmall-mass synchronous coupling

```math
Y_t=X_t^M+\frac{M_X}{\gamma_X}V_t^M
```

と有限時間 $W_1$ 誤差移送は、dumbbell固有drift・single-dumbbell fluctuationと一体で扱うR214Bへ直接吸収した。finite-bath部分はgeneric R209B、flow部分はgeneric R209Aが担う。結果ID R209Cは再利用しない。

## AA.14 R210A：phase-invariant generic coherent-load compatibility

M67 profile $p$ のfull Hamiltonianを

```math
H^{(p)}
=
H_{\rm coh}
+
H_R^{(p)}
```

と分ける。$z$ をprofile側の全canonical変数とし、次の三条件を仮定する。

```math
H_R^{(p)}[e^{i\theta}b,z]
=
H_R^{(p)}[b,z],
```

```math
\left\|
\frac{\partial H_R^{(p)}}{\partial b^*}
\right\|
\le
\frac{
\Psi_p(\mathcal E_p)
}{\|b\|},
\qquad
\Psi_p(E)=a_pE+b_p\sqrt E+c_p,
```

```math
\mathcal E_p(0)\le E_{p,0}=O(1),
\qquad
\mathcal E_p\ge0.
```

global carrier phase不変性から
```math
\{b^\dagger b,H_R^{(p)}\}=0
```
であり、common carrier actionとは直接energy交換しない。M37 slow spatial couplingだけを用いた保守的評価として

```math
|\dot{\mathcal E}_p|
\le
\Omega_h\Psi_p(\mathcal E_p),
\qquad
\Omega_h=\frac{4\|h_L\|}{\mathcal J_0}
```

を得る。任意の $\epsilon>0$ に対し
```math
A_\epsilon=a_p+\epsilon,
\qquad
B_\epsilon=c_p+\frac{b_p^2}{4\epsilon},
```
と置けば
```math
\mathcal E_p(t)
\le
\mathcal E_{p,*}(T)
=
\left[
E_{p,0}+\frac{B_\epsilon}{A_\epsilon}
\right]
e^{\Omega_hA_\epsilon T}
-
\frac{B_\epsilon}{A_\epsilon}.
```
従って
```math
C_p(T)
=
a_p\mathcal E_{p,*}
+
b_p\sqrt{\mathcal E_{p,*}}
+
c_p
```
は固定prepared shellで $O(1)$ である。

### AA.14.1 R214 dumbbell specialization

R214では
```math
\varrho_X
=
\frac{b^\dagger B_Xb}{N_0},
\qquad
\ell_X^2=\ell_0^2+\alpha\varrho_X,
```
なので
```math
G_{\rm db}
=
-\frac{\alpha k}{2N_0\ell_X}
(\rho_c-\ell_X)B_Xb.
```
bootstrap tube上で
```math
\frac{\|b\|^2}{N_0}
\le
K_\eta^2,
\qquad
K_\eta
=
\kappa_\eta^2
+
\frac12\kappa_\eta^{-2},
```
かつ $\ell_X\ge\ell_0$、$H_{\rm db}\ge k(\rho_c-\ell_X)^2/2$ だから
```math
\|G_{\rm db}\|
\le
D_{\rm db}
\frac{\sqrt{H_{\rm db}}}{\|b\|},
\qquad
D_{\rm db}
=
\frac{
\alpha\|B_X\|K_\eta^2\sqrt{2k}
}{
2\ell_0
}.
```

flow targetについては具体的なquadratic ratioを要求せず、
```math
\left\|
\partial_{b^*}v_e[b]
\right\|
\le
\frac{\ell_e}{\|b\|}
```
を仮定すればよい。$L_v=(\sum_e\ell_e^2)^{1/2}$ とすればR214 profileでは
```math
a_{\rm db}=0,
\qquad
b_{\rm db}
=
D_{\rm db}
+
L_v\sqrt{2\Gamma_K},
\qquad
c_{\rm db}=L_v\Gamma_v.
```

<!-- theorem-start:theorem -->
**定理（R210A：phase-invariant generic coherent-load finite-time compatibility）**

M37 safe narrow-band parameter
```math
\eta
=
\frac{2\|h_L\|}
{\mathcal J_0\omega_0}
<1,
\qquad
\kappa_\eta=(1-\eta)^{-1/4}
```
と上のgeneric profile条件を仮定する。同じ初期 $b_0$ から始めるprofile-$p$ M67 trajectory $b^{(p)}$ とbare M37 trajectory $b^{37}$ について、$N_0=\|b_0\|^2$ が

```math
N_0
\ge
\frac{
4TC_p(T)
}{
\mathcal J_0(1-\eta)^{3/2}
}
```

を満たせばbootstrapが閉じ、

```math
q_{\rm load}^{(p)}(T)
=
\sup_{t\le T}
\frac{
\|b^{(p)}(t)-b^{37}(t)\|
}{
\sqrt{N_0}
}
\le
\frac{
2TC_p(T)
}{
\mathcal J_0N_0(1-\eta)
}
=
O(N_0^{-1}).
```

R86のbare M37からSchrödinger targetへのerror $\varepsilon_{86}$ はQ3-1でのみ
```math
q_{210}^{(p)}
=
\kappa_\eta\varepsilon_{86}
+
q_{\rm load}^{(p)}
```
と合成する。Q3-2のM67からM64へのcompatibilityではcarrier-envelope errorを二重計上せず、load-only $q_{\rm load}^{(p)}$ だけをR214Bへ渡す。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R210A）**

R86のBogoliubov normal-envelope座標ではbare M37 propagatorはunitaryである。profile loadをnormal coordinatesへ移しDuhamel公式を使うと、bootstrap下限 $\|b\|\ge\frac12\kappa_\eta^{-2}\sqrt{N_0}$ とgeneric gradient envelopeから表示した $N_0^{-1}$ boundを得る。energy-shell微分不等式とGronwall評価により $C_p(T)$ は初期prepared shellから従う。R214 dumbbell specializationはAA.14.1の係数を代入すればよい。その他profileではgeneric envelope仮定を個別に確認する。証明終。
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

M67 Q3 supporting simulationではM37 ideal signalとの差、generic flow / finite-bath memory、R214 dumbbell radial law、tracer分布を責務ごとに監査する。旧R208B/R208C/R209C専用full-compatibility witnessはactive evidenceから外す。R210A/B・R214A/Bを含むrequired解析検算とsupporting trajectory simulationを区別し、後者だけからA2を昇格しない。$N_0$、$K_U$、$\tau_U$、$\tau_{\rm mem}$、bath mode数、格子幅を独立に振り、一つの改善を複数誤差へ二重計数しない。

M67をcommon physical parentとして広げてもM37、M64、M66、R123の結果を削除しない。M37はactive coherent module、M64/R203はactive Q3 open effective reduction、M66/R205はactive thermal open/effective interface、R123はR210Bで物理liftされたactive dephasing lawとして維持する。R211A--R211CはQ1 binary selectorを、R212A--R212Cはthermal sectorを追加specializeする。A1/A2/B1--B3、M0の判定は変更しない。Q2 signal/NBL/register/gateの統合、H/T/CNOTの一般実装、NBL Born sampling、R206 common-hub apparatus全体のfinite-Hamiltonian liftは本付録から推論しない。$R_i^\delta=|Z_i|^2+\delta q_iS$ のglobal $S$ を完全局所化する問題もstrict-locality strengtheningとして残す。


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

をQ1 double-well profileのsafe branchとする。この判定自体は $(1-\tau_{\rm cut})A_+-\tau_{\rm cut}A_-$ とその左右反転という二つの固定線形量をR112の有限正準比較節へ渡して行い、状態依存除算を制御器へ入力しない。cutoff外およびexact endpointはR204D/R204Eと同じcomparator経路へ送り、double-well profileへ $\log0$ を持ち込まない。

固定装置scale $A_*>0$ に対して $a_\pm=A_\pm/A_*$ とする。Hamiltonianを全位相空間でsmoothに定義するため、正のsmooth extension $\bar a_\pm(I_+,I_-)$ を選び、safe branchでは厳密に

```math
\bar a_\pm=a_\pm
```

とする。さらに装置定数 $0<a_{\rm floor}<a_{\rm ceil}<\infty$ を選び、全位相空間で $a_{\rm floor}\le\bar a_\pm\le a_{\rm ceil}$ とする。safe branch外のextensionはHamiltonian regularizationだけを担い、Born重みを計算する外部tableとして使わない。固定 $A_\Sigma=J_\Sigma$ と $\widehat p_\pm\in[\tau_{\rm cut},1-\tau_{\rm cut}]$ によりsafe held-action集合はcompactになる。

Q1 profileではrunning W2 signalはR189A capture終了後にselectorから切り離す。M67 structured reservoir内部にheld-action pair、phase-volume modes、finite marker bathを置き、別sector $\mathcal X=(X,P_X)$ をbinary markerとして使う。

## AA.18 R211A：M67 Q1 double-well finite-Hamiltonian construction

R189Aが保持するcanonical pair $(A_\pm,P_\pm^J)$ を、capture終了後に

```math
I_\pm=A_\pm,
\qquad
\theta_\pm=-P_\pm^J
```

と正準relabellingする。$d\theta_\pm\wedge dI_\pm=dA_\pm\wedge dP_\pm^J$ なのでsymplectic formは保たれる。selector Hamiltonianを $\theta_\pm$ に依存させない。

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

を使う。decision開始面では、held actionsとmarker初期値を固定した条件付きcanonical preparationでphase-volume modesとfinite marker bathを準備する。phase-volumeのstatic mean-force identityはR211A自身のJacobian計算で閉じ、marker bathの固定 $X$ partition independenceはunit-Jacobian translationから従う。動的thermalizationだけをR209Bのfinite-window OU/Langevin realization corollaryへ委譲する。

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

R211Aの条件付きcanonical preparation、finite-bath Markov化、phase-volume mean-force縮約を前提として、potential of mean forceに対するideal overdamped markerを

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

R211Bの計算核では、phase-volume auxiliary modesをopen OU型law

```math
d\zeta_\alpha
=
-
\frac{k_\alpha(X_t)}{\gamma_{\rho,\alpha}}
\zeta_\alpha dt
+
\sqrt{
\frac{2k_BT}{\gamma_{\rho,\alpha}}
}
dB_{\alpha,t},
```

```math
k_\alpha(X)
=
m_\alpha\omega_\alpha^2
w_\ell(X)^{-2q_\alpha}
```

で記述する。固定 $X$ では

```math
\mathbb E_X[\zeta_\alpha^2]
=
\frac{k_BT}{k_\alpha(X)}
```

であり、markerへのphase-volume forceは

```math
F_{\rm pv}(t)
=
\partial_X\log w_\ell(X_t)
\sum_\alpha q_\alpha k_\alpha(X_t)\zeta_\alpha(t)^2
=
k_BT\partial_X\log w_\ell(X_t)
+
R_{\rm pv}(t).
```

frozen equilibriumでは

```math
\operatorname{Var}_X(F_{\rm pv})
=
2(k_BT)^2
\left(\sum_\alpha q_\alpha^2\right)
(\partial_X\log w_\ell)^2.
```

従ってequal weights $q_\alpha=1/N_\rho$ ではinstantaneous RMS fluctuationは $O(N_\rho^{-1/2})$ である。fast relaxation timeを

```math
\tau_\rho
=
\sup_{X,\alpha}
\frac{\gamma_{\rho,\alpha}}{2k_\alpha(X)}
```

とし、safe compact regionでmarker time scale $\tau_X$ と分離して

```math
\varepsilon_{\rm pv}(T)
\le
C_T
\left[
\frac{\tau_\rho}{\tau_X}
+
\left(\sum_\alpha q_\alpha^2\right)^{1/2}
\right]
```

というfinite-time averaging boundを用いる。これは旧R208Dへ委譲せず、Q1 open reductionの誤差としてR211B内で管理する。

open markerを

```math
dX_t^{\rm op}=V_t^{\rm op}dt,
```

```math
M_XdV_t^{\rm op}
=
\left[
-W_0'(X_t^{\rm op})
+
F_{\rm pv}(t)
-
\gamma_XV_t^{\rm op}
\right]dt
+
\sqrt{2\gamma_Xk_BT}\,dW_t
```

とする。$\epsilon_M=M_X/\gamma_X$ と

```math
Y_t=X_t^{\rm op}+\epsilon_MV_t^{\rm op}
```

を置くと

```math
dY_t
=
\left[
-\mu W_0'(X_t^{\rm op})
+
\mu F_{\rm pv}(t)
\right]dt
+
\sqrt{2\nu}\,dW_t,
\qquad
\mu=\gamma_X^{-1}.
```

同じBrownian motionでideal diffusion $X_t^D$ を駆動し、safe compact region上のdrift Lipschitz boundとMaxwell preparationを用いれば

```math
W_1\left(\mathcal L(X_T^{\rm op}),\mathcal L(X_T^D)\right)
\le
\varepsilon_{\rm pv}(T)+\varepsilon_{\rm od}(T)+\varepsilon_{\rm init}^{X},
```

```math
\varepsilon_{\rm od}(T)
\le
C_T
\left[
\frac{M_X}{\gamma_X}B_*
+
\sqrt{\nu\frac{M_X}{\gamma_X}}
\right].
```

最後にR209B finite-window realization corollaryをphase-volume modesとmarkerへ適用し、$T<T_{\rm bath\,rec}^{Q1}$ で

```math
\sup_{t\le T}
W_1\left(\mathcal L(X_t^{67}),\mathcal L(X_t^{\rm op})\right)
\le
\varepsilon_{\rm FH}(T)
```

とする。従って

```math
W_1\left(\mathcal L(X_T^{67}),\mathcal L(X_T^D)\right)
\le
\varepsilon_X(T),
```

```math
\varepsilon_X(T)
=
\varepsilon_{\rm FH}(T)
+
\varepsilon_{\rm pv}(T)
+
\varepsilon_{\rm od}(T)
+
\varepsilon_{\rm init}^{X}.
```

threshold近傍質量をthreshold近傍質量を

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

さらにdimensionless marker units $k_BT=\mu=x_0=1$ でsafe action-ratio集合と固定 $0<d<L<1$ を保ち、$B\to\infty$ に対して一例として

```math
W_0^{(B)}(X)
=
B(X^2-1)^2,
\qquad
\ell_B=B^{-1},
\qquad
\delta_{0,B}=B^{-1},
```

```math
T_B
=
C\frac{\log B}{B}
```

を取る。$C>0$ を十分大きく固定すると、1次元scale/speed評価から

```math
\varepsilon_{\rm col}
=
O(B^{-1/2}),
\qquad
\varepsilon_{\rm launch}
=
O(B^{-1/2}),
```

```math
\varepsilon_{\rm surv}(T_B)
\longrightarrow0,
\qquad
\varepsilon_{\rm ret}(T_B)
=
O
\left(
T_Be^{-c_{dL}B}
\right),
```

となる。ここで

```math
c_{dL}
=
(1-d^2)^2-(1-L^2)^2
>
0.
```

各有限 $B$ を先に固定した後、phase-volume relaxation比 $\tau_\rho/\tau_X$、mode数 $N_\rho$、R209B finite-window realization error $\varepsilon_{\rm FH}$、small-mass parameter $M_X/\gamma_X$、初期compatibilityを選び、

```math
\varepsilon_{\rm cg}(T_B)
\le
B^{-1/2},
\qquad
T_B<T_{\rm bath\,rec}^{Q1}
```

とできる。縮約定数が $B$ または $\ell_B$ に一様であることは要求せず、各有限 $B$ に対してreduction parameterを後から選ぶ。このnested finite-parameter familyで

```math
\varepsilon_{211B}
\longrightarrow0.
```

従ってM67 Q1 profileはR204E binary selector contractを任意精度で満たすfinite-Hamiltonian physical liftを与える。

R211BはM65/R204Aの指数Poisson waiting-time lawや $\lambda_\pm=\kappa a_\pm$ を再現するとは主張しない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R211B）**

sharp-interface committor式は1次元reversible diffusionのscale functionから従い、$W_0$ のeven symmetryによって左右積分の共通factorが消え、保持作用比を厳密に得る。finite collarはsharp profileとの差が $|X|<\ell$ にだけ支持を持つため、左右scale integralの摂動評価から $\varepsilon_{\rm col}$ を得る。launch errorはcommittorの平均値定理で抑える。

eventual deep-commitment signと固定時刻basin readoutが異なるpathは、時刻 $T$ までに $\pm L$ へ到達しない場合か、到達後に対応する $\pm d$ まで戻る場合へ含まれるので、自然couplingから $\varepsilon_{\rm surv}+\varepsilon_{\rm ret}$ で抑えられる。

finite-Hamiltonian lawとideal diffusion lawをone-time $W_1$ couplingし、coupling距離が $\delta$ を超える確率をMarkov inequalityで $\varepsilon_X/\delta$ と評価する。両marker位置がthresholdから $\delta$ 以上離れ、coupling距離が $\delta$ 以下なら $g_d$ の結果は一致するため、残る不一致確率は $\omega_d(\delta,T)$ 以下である。$\delta$ について下限を取れば $\varepsilon_{\rm cg}$ を得る。

最後のparameter familyでは、中央barrier近傍のscale densityは幅 $O(B^{-1/2})$ に集中するため $\ell_B=B^{-1}$ のcollar比は $O(B^{-1/2})$ である。committor derivativeは同領域で $O(B^{1/2})$ なので $\delta_{0,B}=B^{-1}$ によりlaunch errorも $O(B^{-1/2})$ になる。中央saddle近傍の不安定drift scaleは $O(B)$ であり、$T_B=C(\log B)/B$ は十分大きい $C$ でfall timeを上回る一方、$L$ から $d$ へ戻るにはfree-energy差 $c_{dL}B+O(1)$ を上るためfinite-window returnは指数的に抑えられる。各有限 $B$ で $\tau_\rho/\tau_X$ を小さくし、$N_\rho$ を大きくし、R209B finite-window realization errorと $M_X/\gamma_X$ をその後に小さく取れば、open phase-volume averaging、finite-Hamiltonian lift、small-mass、coarse-grainingの各誤差を責務別に独立して小さくできる。証明終。
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

cutoff外ではR204Dと同じ固定線形comparatorをR112の有限正準比較・無反応節で実装し、

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


## AA.21 R212 thermal-sector bridge

R212A--R212CはM66/R205を削除せず、M67 structured reservoirの有限Hamiltonian parentからそのopen/effective thermal lawを回収する。責務は

```math
M67
\longrightarrow
R212A
\longrightarrow
\{R212B,R212C\}
\longrightarrow
M66/R205
```

とする。R205B/R205Dはfinite-chamber reduced lawとしてそのまま維持し、R206/R207の用途別specializationも削除しない。

### AA.21.1 R212A：universal phase-volume / mean-flow embedding

resolved canonical variablesをまとめて $S$ とし、smooth positive weight $w(S)$、mean-flow shift $U(S)$、coordinate shift $R(S)$ を取る。safe domainで

```math
0<w_*\le w(S)\le w^*<\infty
```

とする。structured reservoir内部に有限個のcanonical pairs $(\zeta_\alpha,\Pi_\alpha)$ を置き、

```math
H_{\rm th}^{67}
=
\sum_{\alpha=1}^{N_{\rm pv}}
\left[
\frac{(\Pi_\alpha-m_\alpha U(S))^2}{2m_\alpha}
+
\frac{m_\alpha\omega_\alpha^2}{2}
\left(
w(S)^{-q_\alpha}\zeta_\alpha-d_\alpha R(S)
\right)^2
\right],
\qquad
q_\alpha>0,
\quad
\sum_\alpha q_\alpha=1
```

とする。

<!-- theorem-start:theorem -->
**定理（R212A：M67 universal phase-volume / mean-flow embedding）**

固定 $S$ に対するconditional canonical partitionは

```math
Z_{\rm th}^{67}(S)=Z_0 w(S)
```

であり、

```math
F_{\rm th}^{67}(S)
=
-k_BT\log w(S)+C.
```

従って任意のresolved coordinate $s\subset S$ に対して

```math
-\langle\partial_s H_{\rm th}^{67}\rangle
=
k_BT\,\partial_s\log w,
```

一方でmean-flow momentum shiftとcoordinate translationはpartition factorを変えない。pure phase-volume sectorのconditional force fluctuationは

```math
\operatorname{Var}(F_s^{\rm pv})
=
2(k_BT)^2
\left(\sum_\alpha q_\alpha^2\right)
(\partial_s\log w)^2.
```

特に $q_\alpha=1/N_{\rm pv}$ ならRMS fluctuationは $O(N_{\rm pv}^{-1/2})$ である。

R205Aは $U=R=0$、R205Cは一般 $U,R$、R211Aはselector weightへのspecializationとして回収される。旧R208Bで用いていた $w=r_X^\delta/r_*$ のphase-volume数学もR212Aのspecializationとして回収されるが、R208B自体はdraft-146で退役済みであり現行依存には数えない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R212A）**

```math
P_\alpha=\Pi_\alpha-m_\alpha U(S),
\qquad
Q_\alpha=w(S)^{-q_\alpha}\zeta_\alpha-d_\alpha R(S)
```

と変数変換する。momentum shiftとtranslationのJacobianは1で、$d\zeta_\alpha=w^{q_\alpha}dQ_\alpha$ だから全Jacobianは $w^{\sum q_\alpha}=w$。残るGaussian積分は $S$ に依存しない。force identityは $F=-k_BT\log Z$ から従う。各potential energyはcanonical ensembleで平均 $k_BT/2$、分散 $(k_BT)^2/2$ なので表示のvarianceを得る。証明終。
<!-- theorem-end:proof -->

terminal signalをaction-angle $(J_y,\phi_y)$ で表し、$w=w(J)$ がphaseに依存しないspecializationでは

```math
\dot J_y=-\partial_{\phi_y}H=0
```

である。従ってphase-volume couplingはterminal actionをQNDに保持できるが、$\dot\phi_y$ へのthermal phase loadまで消すとは主張しない。

## AA.22 R212B：finite-Hamiltonian thermal sampler / R205E compatibility

### AA.22.1 flat configuration

resolved pair $(Q,P)$ に対し

```math
H_{212B}
=
\frac{|P|^2}{2M}
+
H_{\rm cfg}(Q)
+
H_{\rm pv}(Q)
+
\sum_{\mu=1}^{N_B}
\left[
\frac{|p_\mu|^2}{2m_\mu}
+
\frac{m_\mu\Omega_\mu^2}{2}
|q_\mu-a_\mu Q|^2
\right]
```

とする。R212Aからhidden-variable partitionは $Cw(Q)$、harmonic drag bathはcoordinate translationなので追加weightを作らない。従ってfull canonical $Q$-marginalは厳密に

```math
\pi(Q)
\propto
w(Q)e^{-\beta H_{\rm cfg}(Q)},
\qquad
H_{\rm eff}
=
H_{\rm cfg}-k_BT\log w.
```

finite harmonic bathを厳密消去すると

```math
M\ddot Q_t
=
-\nabla H_{\rm cfg}(Q_t)
+
F_{\rm pv}(t)
-
\int_0^t\Gamma_N(t-s)\dot Q_s\,ds
+
\xi_N(t),
```

```math
\Gamma_N(t)
=
\sum_\mu m_\mu\Omega_\mu^2a_\mu^2\cos(\Omega_\mu t),
\qquad
\langle\xi_N(t)\xi_N(s)^T\rangle
=
k_BT\Gamma_N(t-s)I
```

を得る。phase-volume forceを

```math
F_{\rm pv}(t)
=
k_BT\nabla\log w(Q_t)
+
R_{\rm pv}(t)
```

と分解し、finite-spectrum、short-memory、small-mass誤差を別々に数える。

<!-- theorem-start:theorem -->
**定理（R212B：M67 finite-Hamiltonian thermal sampler / R205E compatibility）**

compact safe domainで $w>0$、$H_{\rm cfg}$ がsmoothとする。固定有限時間 $0\le t\le T<T_{\rm rec}$ に対し

```math
\varepsilon_{212B}^{\rm flat}
=
\varepsilon_{\rm pv}
+
\varepsilon_{\Gamma}
+
\varepsilon_{\rm noise}
+
\varepsilon_{\rm od}
+
\varepsilon_{\rm init}
```

とする。finite harmonic bathをshort-memory kernelへ近似し、$M/\gamma\to0$ を取るparameter familyで

```math
\sup_{t\le T}
W_1
\left(
\mathcal L(Q_t^{67}),
\mathcal L(Q_t^{205E})
\right)
\le
C_T\varepsilon_{212B}^{\rm flat},
```

ここで $Q^{205E}$ は

```math
dQ_t
=
-\mu\nabla
\left[
H_{\rm cfg}(Q_t)-k_BT\log w(Q_t)
\right]dt
+
\sqrt{2\mu k_BT}\,dW_t,
\qquad
\mu=\gamma^{-1}.
```

従ってR205EはM67 thermal sectorのfinite-time open reductionとして回収される。有限Hamiltonianが無限時間Markov semigroupになるとは主張しない。
<!-- theorem-end:theorem -->

### AA.22.2 S2 rigid-rotor corollary

orientationを $\lambda\in S^2$、tangent angular momentumを $L$ とし、

```math
|\lambda|=1,
\qquad
\lambda\cdot L=0,
\qquad
H_{\rm rot}=\frac{|L|^2}{2I},
\qquad
\dot\lambda=\omega\times\lambda,
\quad
\omega=L/I
```

とする。finite isotropic bathを

```math
H_B^{\rm rot}
=
\sum_{\mu=1}^{N_B}
\left[
\frac{|p_\mu|^2}{2m_\mu}
+
\frac{m_\mu\omega_\mu^2}{2}
|q_\mu-a_\mu\lambda|^2
\right]
```

とする。固定 $\lambda$ では $q_\mu\mapsto q_\mu-a_\mu\lambda$ は平行移動なのでbath partitionはorientation-independentである。

bathを厳密消去するとtorqueは

```math
\tau_B(t)
=
\lambda(t)\times\xi_N(t)
-
\lambda(t)\times
\int_0^t
\Gamma_N(t-s)\dot\lambda(s)\,ds.
```

noise torqueはHamiltonian構造だけで接平面へ投影される。short-memory極では $\lambda(t)\times\dot\lambda(s)$ と $\omega(s)$ の差がgeometry residualを与え、十分条件として

```math
\theta_B\ll I/\gamma
```

を取る。

<!-- theorem-start:corollary -->
**系（球面回転子版：M67 finite-Hamiltonian rotor / spherical R205E compatibility）**

R212Aのpositive smooth weight $w(\lambda)$ とsmooth $H_{\rm cfg}(\lambda)$ を持つfinite rotor profileを取る。固定有限時間 $T<T_{\rm rec}$ で

```math
\varepsilon_{212B}^{\rm rot}
=
\varepsilon_{\rm pv}
+
\varepsilon_{\Gamma}
+
\varepsilon_{\rm geom}
+
\varepsilon_{\rm noise}
+
\varepsilon_{\rm od}^{\rm rot}
+
\varepsilon_{\rm init}
```

とする。$\theta_B\ll I/\gamma$、finite-spectrum Markov化、small-inertia極を同時に満たすparameter familyではM67 orientation lawはgenerator

```math
\mathcal L_{S^2}f
=
-\mu\nabla_S H_{\rm eff}\cdot\nabla_S f
+
\mu k_BT\Delta_S f,
\qquad
H_{\rm eff}=H_{\rm cfg}-k_BT\log w
```

を持つspherical diffusionへ有限時間で近づく。

Stratonovich形式は

```math
d\lambda_t
=
-\mu P_{\lambda_t}\nabla H_{\rm eff}\,dt
+
\sqrt{2\mu k_BT}\,
P_{\lambda_t}\circ dW_t,
\qquad
P_\lambda=I-\lambda\lambda^T,
```

Itô形式は

```math
d\lambda_t
=
\left[
-\mu P_{\lambda_t}\nabla H_{\rm eff}
-
2\mu k_BT\lambda_t
\right]dt
+
\sqrt{2\mu k_BT}\,
P_{\lambda_t}dW_t.
```

reversible stationary measureは

```math
\pi(d\lambda)
\propto
w(\lambda)e^{-\beta H_{\rm cfg}(\lambda)}d\Omega.
```
<!-- theorem-end:corollary -->

### AA.22.3 R207A finite-Hamiltonian preparation lift

二rotor $(\lambda_A,L_A),(\lambda_B,L_B)$ と独立local finite rotor bathを取り、

```math
H_{\rm cfg}
=
-K\lambda_A\cdot\lambda_B,
\qquad
k=\beta K,
```

```math
w_\epsilon
=
f_\epsilon(a\cdot\lambda_A)
+
f_\epsilon(b\cdot\lambda_B)
```

とする。$0<\epsilon<1$ なら $2\epsilon\le w_\epsilon\le2$ である。rotor momenta、R212A phase-volume variables、local rotor bathsをcanonicalに積分するとorientation marginalは厳密に

```math
\rho_{\epsilon,k}^{67}
(\lambda_A,\lambda_B\mid a,b)
=
\frac{
e^{k\lambda_A\cdot\lambda_B}
w_\epsilon
}{
Z_{\epsilon,k}
},
```

すなわちR207A densityそのものになる。

<!-- theorem-start:corollary -->
**系（Q2-2二回転子版：R207A finite-Hamiltonian preparation lift）**

任意の $0<\epsilon<1$、有限 $k>0$、held settings $a,b\in S^2$ に対して、有限rigid rotors、R212A phase-volume modes、有限isotropic local bathsからなるsmoothで下に有界なM67 Hamiltonian profileを構成できる。そのcanonical orientation marginalはR207Aの $\rho_{\epsilon,k}$ と厳密に一致する。従ってR207Aのsetting-independent partition、独立setting marginal、source hidden stateのsetting dependenceはM67 canonical ensembleからも回収される。

さらにR212B-rotのfinite-time reduction条件を満たせば、任意のinitial orientation lawからspherical R205Eを経て $\rho_{\epsilon,k}$ へ有限時間で近づけられる。mixingの存在はcompactnessとstrictly positive smooth stationary densityから従い、具体的な $t_{\rm mix}<T_{\rm rec}$ windowはnumerical witnessで別に監査する。
<!-- theorem-end:corollary -->

R207で使う一つのexplicit witnessは

```math
\eta=0.25,
\quad
\epsilon=1/32,
\quad
k=8,
\quad
\theta_B=5\times10^{-4},
\quad
I/\gamma=10^{-2},
```

```math
t_{\rm mix}=12,
\quad
T_{\rm prep}=15,
\quad
T_{\rm rec}=100.
```

従って

```math
5\times10^{-4}
\ll
10^{-2}
<
12
<
15
<
100
```

という有限parameter windowが空でない。Monte Carlo mixing witnessは解析証明ではなくsupporting numerical evidenceとして扱う。

## AA.23 R212C：finite-Hamiltonian passive separation / R205F compatibility

二つのresolved subsystem $Q_A,Q_B$ と距離 $R$ を取り、smooth compact-support profile

```math
s(R)\in[0,1],
\qquad
s(R)=1\quad(R\le R_{\rm prep}),
\qquad
s(R)=0\quad(R\ge R_{\rm sep})
```

を固定constitutive lawとして使う。direct interactionとshared phase-volume couplingを

```math
H_{AB}^{\rm int}
=
K_0s(R)V_{AB},
qquad
F_{\rm pv}^{AB}
=
-k_BT\,s(R)\log w_{\rm sh}
```

とする。

一般shared-bath profileでは二成分bath coupling directionを

```math
u_A=(1,0),
\qquad
u_B(R)=
\left(
c(R),
\sqrt{1-c(R)^2}
\right),
\qquad
c(R)=c_0s(R)
```

と選べる。固定 $R$ でbathを消去するとmemory/friction matrixのcross blockは $O(c(R))$、overdamped local mobility correctionは $O(c(R)^2)$ である。

<!-- theorem-start:theorem -->
**定理（R212C：M67 finite-Hamiltonian passive separation / R205F compatibility）**

M67 shared-reservoir profileを上のcompact-support geometryで構成する。finite-bath Markov reductionとsmall-mass reduction後のgenerator $\mathcal L_R^{67}$ は完全分離generator $\mathcal L_A+\mathcal L_B$ に対して

```math
\|
(\mathcal L_R^{67}
-\mathcal L_A
-\mathcal L_B)f
\|_\infty
\le
C_f
\left[
|K_0|s(R)
+
s(R)
+
|c(R)|
+
c(R)^2
+
\varepsilon_{\rm bath}
+
\varepsilon_{\rm od}
\right].
```

従って $R\to R_{\rm sep}$ とともにgenerator defectを任意に小さくできる。さらに $R\ge R_{\rm sep}$ ではcompact-support couplingsが厳密に零となり、

```math
H_{67}=H_A^{67}+H_B^{67}+H_{\rm spectators},
\qquad
\mathcal L_R^{67}=\mathcal L_A+\mathcal L_B
```

が厳密に成立する。

finite $R$ ではFDTによりcross noiseとcross frictionが同時に生じるため、R205Fの固定local-mobility formを係数ごと完全再現するとは主張しない。R205FはM67 separation lawのopen/effective reductionとして読む。
<!-- theorem-end:theorem -->

R207最小profileではA/Bに独立local rotor bathsを常時接続し、相関はnear-contact lockとshared phase-volume weightだけで作ればよい。このときcross-bath blockを $c(R)=0$ とでき、R212Cは $K(R)$ とshared phase-volume portの受動消去を与える。local thermal contactは切らない。

## AA.24 R212A--R212Cの責務境界

R212A--R212Cにより

```math
R212A\Rightarrow R205A,R205C,
\qquad
R212B\Rightarrow R205E,
\qquad
R212C\Rightarrow R205F
```

というphysical-parent chainを置く。M66/R205はM67 thermal sectorのopen/effective interfaceとして維持する。R205B/R205D、R206A--R206E、R207A--R207Dは用途別reduced/effective resultとして残す。

R212B-Q2-2によりR207A canonical preparationはM67 physical parentへ持ち上がるが、R206 common-hub apparatus全体、Q2 signal/register/gate、NBL register、gate中always-on phase backreaction、M0 joint-device renewalを導出したとは扱わない。fixed-goal達成ラベル、R186、A1/A2/B1--B3の判定も本定理群だけでは変更しない。
