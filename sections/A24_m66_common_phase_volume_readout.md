@number: X
@chapter: 付録
@title: M66 common thermal-reservoir parentとQ2多結果readout
@status: M66/R205A--R205Fをphase-volume、mean-flow、thermal sampling、passive separationを共通化するthermal-reservoir parentとする。Q2-1/Q2-3/Q2-4の現行terminal multi-outcome readoutはR206A--R206EをM66のQ2特殊化として維持する。M64/M65のdomain modelは置換せず、それぞれのreservoir実現だけをR205C/R205D/R205Eへ埋め込む。Q2-4のR186 additive-noise障害は独立に残す。

M66は、resolved classical degreesと一つのthermal reservoirの間の物理interfaceだけを共通化するopen parent modelである。M64のtracer/Nelson dynamics、M65のbinary selector、R206のQ2 terminal samplerそのものを置換せず、それらが用いるreservoir phase volume、mean flow、thermal sampling、空間分離時の受動decouplingを共通原理として切り出す。

共通入力は正のphase-volume weight $w(Q,t)>0$、reservoir mean-flow port $U(Q,t)$、resolved configurationの通常のenergy landscape $H_{\rm cfg}(Q,t)$ とする。これらはBorn確率表やGibbs確率表を外部controllerが計算して注入するための入力ではなく、各specializationの局所signal、粒子配置、受動幾何から決まる物理量である。reservoir couplingは固定、または粒子間距離・局所配置へ受動的に依存するconstitutive lawとし、確率生成のためだけのbath switchを要求しない。

R205A/R205Cはphase-volume/free-energy sector、R205B/R205Dはfinite-chamber reduction、R205Eはoverdamped thermal sampler、R205Fは空間分離時のgenerator decouplingを与える。Q2-1/Q2-3/Q2-4ではR206A--R206Eへ接続する。Q1/Q2-2の逐次binary instrumentはM65/R181D、Q3のparticle/Nelson主線はM64/R203A--R203Dを維持する。

## X.1 R205A：共通phase-volume identity

signalから得る正の局所scaleを $w>0$ とする。reservoir内部自由度を $(\zeta_\alpha,\Pi_\alpha)$ とし、

```math
H_{\rm res}(w)
=
\sum_{\alpha}
\left[
\frac{\Pi_\alpha^2}{2m_\alpha}
+
\frac{m_\alpha\omega_\alpha^2}{2}
\left(
\lambda_\alpha(w)\zeta_\alpha-d_\alpha R
\right)^2
\right],
```

```math
\lambda_\alpha(w)=w^{-q_\alpha},
\qquad
q_\alpha>0,
\qquad
\sum_\alpha q_\alpha=1
```

とする。

<!-- theorem-start:theorem -->
**定理（R205A：共通phase-volume identity）**

固定 $w>0$ と $R$ に対するcanonical積分は

```math
Z_{\rm res}(w,R)
=
Z_{\rm res}^0\,w
```

を満たす。従って

```math
F_{\rm res}(w)
=
-k_BT\log w+C
```

である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R205A）**

各modeで $Q_\alpha=\lambda_\alpha\zeta_\alpha-d_\alpha R$ と変数変換する。Gaussian積分の $w$ 依存性は

```math
\prod_\alpha\lambda_\alpha^{-1}
=
w^{\sum_\alpha q_\alpha}
=
w
```

だけである。証明終。
<!-- theorem-end:proof -->

R203Bは $w=r_X^\delta/r_*$ の特殊化、R204Bは二結果の局所scaleをcapacity/conductanceへ共通に入れる特殊化として読める。

## X.2 R205B：matched capacity--conductance原理

結果channel $y$ のwell-mixed capacityを $V_y$、hubとのconductanceを $G_y$、hub capacityを $V_H$ とする。固定装置定数 $V_0,G_0,V_H^0>0$ に対し

```math
V_y=V_0s_y,
\qquad
G_y=G_0s_y
```

とする。

<!-- theorem-start:theorem -->
**定理（R205B：matched capacity--conductance原理）**

上の一様scale則では

```math
k_{y\to H}
=
\frac{G_y}{V_y}
=
\frac{G_0}{V_0}
=:\Lambda
```

となり、channelからhubへのrateは $s_y$ と結果数に依存しない。

hubからchannelへのrateは

```math
k_{H\to y}
=
\frac{G_y}{V_H}
```

であり、$V_H$ の一様scaleを選ぶことで局所 $s_y$ をそのまま標本化rateへ写せる。
<!-- theorem-end:theorem -->

この構成では外部制御器が比 $s_y/\sum_zs_z$ を計算する必要はない。

## X.3 R205C--R205F：common thermal-reservoir parentの閉包

### X.3.1 R205C：phase-volume / mean-flow orthogonality

R205Aにmean-flow portを加えて

```math
H_{\rm res}(w,U)
=
\sum_\alpha
\left[
\frac{(\Pi_\alpha-m_\alpha U)^2}{2m_\alpha}
+
\frac{m_\alpha\omega_\alpha^2}{2}
\left(
\lambda_\alpha(w)\zeta_\alpha-d_\alpha R
\right)^2
\right],
```

```math
\lambda_\alpha(w)=w^{-q_\alpha},
\qquad
q_\alpha>0,
\qquad
\sum_\alpha q_\alpha=1
```

とする。

<!-- theorem-start:theorem -->
**定理（R205C：phase-volume / mean-flow orthogonality）**

固定 $w>0$、$U$、$R$ に対して

```math
Z_{\rm res}(w,U,R)=Z_{\rm res}^0w,
```

```math
F_{\rm res}(w)=-k_BT\log w+C,
\qquad
\partial_UF_{\rm res}
=
\partial_RF_{\rm res}
=
0
```

が成立する。$w=w(Q)$ なら

```math
-\nabla_QF_{\rm res}
=
k_BT\nabla_Q\log w.
```

従ってphase-volume weightとmean-flow shiftは同じreservoir内でfree energyに対して直交したportとして共存できる。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R205C）**

$P_\alpha=\Pi_\alpha-m_\alpha U$、$Q_\alpha=\lambda_\alpha(w)\zeta_\alpha-d_\alpha R$ と変数変換する。運動量側は平行移動でJacobian 1、座標側だけが $\prod_\alpha\lambda_\alpha^{-1}=w$ を与える。従ってpartition functionは $U,R$ に依存せず、$Q$ 微分からmean force式を得る。証明終。
<!-- theorem-end:proof -->

M64/R203Bでは $w=r_X^\delta/r_*$ と特殊化する。R205Cが共通化するのはR203Bのpartition/free-energyとflow分離であり、current dictionary、initial preparation、finite-time flow tracking、R203C/R203DはM64固有の責務として残す。

### X.3.2 R205D：M65 fixed-hub chamberの特殊化

<!-- theorem-start:corollary -->
**系（R205D：binary fixed-hub specialization）**

R205Bで $y\in\{+,-\}$、$s_y=a_y$、$V_H=V_H^0$ とすると

```math
k_{y\to H}
=
\frac{G_0}{V_0}
=:\Lambda,
\qquad
k_{H\to y}
=
\frac{G_0}{V_H^0}a_y
=:\kappa a_y
```

となり、R204Bのfixed-hub matched capacity--conductance generatorを回収する。
<!-- theorem-end:corollary -->

<!-- theorem-start:proof -->
**証明（R205D）**

$V_y=V_0a_y$、$G_y=G_0a_y$ をR205Bへ代入すればよい。証明終。
<!-- theorem-end:proof -->

R205DはM65のcanonical open law R204A/R204Dを置換せず、追加物理実現R204Bだけをcommon parentへ埋め込む。

### X.3.3 R205E：common thermal Gibbs sampler

compact connected configuration domain $\mathcal D$ に周期境界または反射境界を課す。$w\in C^2(\mathcal D)$ は正で上下に有界、$H_{\rm cfg}\in C^2(\mathcal D)$、$\mu,T>0$ とし、

```math
H_{\rm eff}
=
H_{\rm cfg}
-k_BT\log w
```

に対するopen SDE

```math
dQ_t
=
-\mu\nabla H_{\rm eff}(Q_t)\,dt
+
\sqrt{2\mu k_BT}\,dW_t
```

を取る。

<!-- theorem-start:theorem -->
**定理（R205E：common thermal Gibbs sampler）**

Fokker--Planck方程式は

```math
\partial_t p
=
\mu k_BT
\nabla\!\cdot
\left[
\pi\,
\nabla
\left(
\frac{p}{\pi}
\right)
\right],
```

```math
\pi(Q)
=
\frac{
w(Q)e^{-\beta H_{\rm cfg}(Q)}
}{
\int_{\mathcal D}
w(q)e^{-\beta H_{\rm cfg}(q)}\,dq
},
\qquad
\beta=(k_BT)^{-1}
```

と書ける。従って $\pi$ はzero-fluxの可逆定常分布である。さらにgeneratorが $L^2(\pi)$ でPoincaré gap $\lambda_{\rm mix}>0$ を持つなら

```math
\left\|
\frac{p_t}{\pi}-1
\right\|_{L^2(\pi)}
\le
e^{-\lambda_{\rm mix}t}
\left\|
\frac{p_0}{\pi}-1
\right\|_{L^2(\pi)},
```

```math
D_{\rm TV}(p_t,\pi)
\le
\frac12
e^{-\lambda_{\rm mix}t}
\left\|
\frac{p_0}{\pi}-1
\right\|_{L^2(\pi)}.
```
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R205E）**

$-\mu\nabla H_{\rm eff}=\mu k_BT\nabla\log\pi$ なのでFokker--Planck作用素を表示のreversible divergence formへ書ける。$p=\pi$ でfluxは零である。Poincaré gap下の $L^2(\pi)$ 収束はDirichlet formのenergy estimateから従い、Cauchy--SchwarzでTV上界を得る。証明終。
<!-- theorem-end:proof -->

M64のstatic initial-preparation windowでは $H_{\rm cfg}=0$、$w=r_0^\delta/r_*$ とすれば $\pi_0^\delta(dX)\propto r_0^\delta(X)dX$ を回収する。time-dependent mean-flow trackingとNelson reductionはR203B/R203Cに残す。

### X.3.4 R205F：passive separation principle

二つのresolved subsystem $Q_A,Q_B$ のlocal generatorを $\mathcal L_A,\mathcal L_B$ とする。距離 $R$ に依存する受動相互作用を

```math
H_{AB}^{(R)}
=
K(R)V_{AB}(Q_A,Q_B)
```

とし、local mobilityを $\mu_A,\mu_B>0$、同一spatial reservoir由来のcross-diffusion blockを $C_{AB}(R)$ とする。local diffusion blockと $C_{AB}(R)$ を合わせた全拡散行列は各 $R$ で正半定値と仮定する。joint generatorを

```math
\mathcal L_R f
=
(\mathcal L_A+\mathcal L_B)f
-
K(R)
\left[
\mu_A\nabla_AV_{AB}\!\cdot\!\nabla_Af
+
\mu_B\nabla_BV_{AB}\!\cdot\!\nabla_Bf
\right]
+
2C_{AB}(R):\nabla_A\nabla_Bf
```

とする。local reservoir coupling、温度、local noise strengthは分離時に切り替えない。

<!-- theorem-start:theorem -->
**定理（R205F：passive separation principle）**

$V_{AB}\in C^1$、$f\in C^2$ なら

```math
\begin{aligned}
\|
(\mathcal L_R-\mathcal L_A-\mathcal L_B)f
\|_\infty
\le{}&
|K(R)|\mu_A
\|\nabla_AV_{AB}\|_\infty
\|\nabla_Af\|_\infty
\\
&+
|K(R)|\mu_B
\|\nabla_BV_{AB}\|_\infty
\|\nabla_Bf\|_\infty
\\
&+
2\|C_{AB}(R)\|
\|\nabla_A\nabla_Bf\|_\infty .
\end{aligned}
```

従って $K(R)\to0$、$C_{AB}(R)\to0$ ならjoint generatorは $\mathcal L_A+\mathcal L_B$ へ収束する。有限range構成で $R\ge R_{\rm sep}$ に対して両者が厳密に零なら

```math
\mathcal L_R
=
\mathcal L_A+\mathcal L_B
```

が厳密に成立する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R205F）**

joint generatorからlocal generatorの和を引き、interaction drift二項とcross-diffusion項に三角不等式を適用すればよい。$K=C_{AB}=0$ なら差の全項が消える。証明終。
<!-- theorem-end:proof -->

R205Fは固定local bath couplingのまま受動的に力学が分離する条件だけを主張する。Bell型共同統計、setting依存準備、measurement independenceへの具体的適用は付録W/R207A--R207DのQ2-2-S candidateで扱う。R205F単独からfinite-speed spatial isolationは主張しない。

### X.3.5 specializationsと責務境界

| specialization | $w$ | $H_{\rm cfg}$ | $U$ | M66が共通化する部分 |
|---|---|---|---|---|
| M64 reservoir sector | $r_X^\delta/r_*$ | tracer側local energy | $v_\delta$とtracking | R203Bのpartition/free-energyとthermal preparation |
| M65 physical lift | $a_\pm$ | fixed chamber geometry | 0 | R204Bのcapacity--conductance |
| R206 terminal sampler | $s_y$ | hub/chamber geometry | 0 | phase-volumeとmatched conductance |
| general thermal preparation | $w(Q)$ | $H_{\rm cfg}(Q)$ | 0 | R205E Gibbs sampler |

M66はreservoir layerだけを共通化し、M64のcurrent dictionary/Nelson縮約、M65のbinary open law/R181D handoff、R206のfinite-$L$ samplerとQ2 resource contractを吸収しない。

## X.4 R206A：有限L結果common-hub sampler

有限結果集合を

```math
\Omega_L=\{1,\ldots,L\}
```

とする。非負作用 $a_y\ge0$ と

```math
a_\Sigma=\sum_{y=1}^La_y>0
```

を取り、

```math
p_y=\frac{a_y}{a_\Sigma}
```

とする。

canonical open samplerを

```math
k_{y\to H}=\Lambda,
\qquad
k_{H\to y}=\kappa a_y
```

で定める。確率を $x_y(t)=P(X_t=y)$、$h(t)=P(X_t=H)$ とすると

```math
\dot x_y
=
-\Lambda x_y+\kappa a_yh,
```

```math
\dot h
=
\Lambda(1-h)-\kappa a_\Sigma h.
```

<!-- theorem-start:theorem -->
**定理（R206A：finite-$L$ common-hub sampler）**

```math
d_y(t)
=
x_y(t)-p_y[1-h(t)]
```

と置けば

```math
\dot d_y=-\Lambda d_y
```

が各 $y$ で厳密に成立する。また

```math
h_\infty
=
\frac{\Lambda}{\Lambda+\kappa a_\Sigma},
```

```math
h(t)
=
h_\infty+
[h(0)-h_\infty]
e^{-(\Lambda+\kappa a_\Sigma)t}.
```

従って有限時間で

```math
x_y(t)
=
p_y[1-h(t)]
+
e^{-\Lambda t}d_y(0).
```

収束率 $\Lambda$ は $L$ と $\min_y p_y$ に依存しない。$a_y=0$ のexact zero-weight channelも許す。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R206A）**

$a_y=p_ya_\Sigma$ をmaster equationへ代入すれば

```math
\dot d_y
=
-\Lambda[x_y-p_y(1-h)]
```

を得る。$h$ は一次線形方程式を直接解けばよい。証明終。
<!-- theorem-end:proof -->

## X.5 R206B：Q2-4用の一様受動channel構成

Q2-4では $L=2^n$ とする。R181C後のterminal signal作用を

```math
J_y
=
\mathcal J_0|Z_y|^2,
\qquad
J_\Sigma=\sum_yJ_y=J_*
```

とする。解析上

```math
p_y=\frac{J_y}{J_*}
```

と書くが、物理装置がこの比を計算して入力することは禁止する。

固定regularization $\delta>0$ を取り、各channelが局所 $J_y$ だけから同一規則

```math
s_y
=
\delta+\frac{LJ_y}{J_*}
```

を使うとする。

capacity/conductanceを

```math
V_y=V_0s_y,
\qquad
G_y=G_0s_y
```

とし、共通hubを

```math
V_H=LV_H^0
```

とする。

<!-- theorem-start:theorem -->
**定理（R206B：一様passive $L$-channel realization）**

上の同型channel族では

```math
k_{y\to H}
=
\Lambda
:=
\frac{G_0}{V_0},
```

```math
k_{H\to y}
=
\kappa
\left(
p_y+\frac{\delta}{L}
\right),
\qquad
\kappa:=\frac{G_0}{V_H^0}.
```

従って総hub escape rateは

```math
\sum_yk_{H\to y}
=
\kappa(1+\delta)
```

であり $L$ に依存しない。

対応する規格化結果重みは

```math
p_y^\delta
=
\frac{p_y+\delta/L}{1+\delta},
```

かつ

```math
D_{\rm TV}(p^\delta,p)
\le
\frac{\delta}{1+\delta}.
```

channelごとに異なるBorn表、振幅表、較正係数表を外部入力する必要はない。
<!-- theorem-end:theorem -->

### X.5.1 bounded local scaling

一つの極端な幾何factorへ $s_y$ を集中させず、各channelに $m=n$ 個の同型phase-volume座標を置き、

```math
q_\alpha=\frac1n,
\qquad
\lambda_{y\alpha}=s_y^{-1/n}
```

とする。R205Aにより積Jacobianは $s_y$ を与える。

```math
\delta\le s_y\le 2^n+\delta
```

なので、固定 $\delta$ または $\delta^{-1}=\operatorname{poly}(n,1/\epsilon)$ の範囲では、各局所scaleに指数精度を直接要求しない。内部自由度総数は $O(n2^n)$ と報告する。

## X.6 R206C：有限時間・製造誤差・完全結果

<!-- theorem-start:theorem -->
**定理（R206C：finite-time / fabrication-error bound）**

R206Aを $p^\delta$ に適用する。任意のpointer初期分布について

```math
\frac12\sum_y|d_y(0)|\le1.
```

decision時刻 $T$ でhub質量を捨てて成功試行だけを再規格化しない。hubを完全結果として保持するか、事前固定した合法的な結果写像へ送る。

そのときsampler誤差は保守的に

```math
\varepsilon_{\rm samp}(T)
\le
2e^{-\Lambda T}
+
\frac{\Lambda}
{\Lambda+\kappa(1+\delta)}
+
\frac{\delta}{1+\delta}
+
T\varepsilon_{\rm gen}
+
\varepsilon_{\rm rec}
```

と置ける。従って

```math
T
=
O\left(
\Lambda^{-1}\log\frac1\epsilon
\right)
```

で有限時間誤差を制御でき、$L$ は明示的に現れない。

実際のlocal scaleが

```math
\widetilde s_y
=
s_y(1+\epsilon_y)+b_y,
```

```math
|\epsilon_y|\le\eta,
\qquad
|b_y|\le b
```

を満たすとする。$s_y\ge\delta$ より

```math
\left|
\frac{\widetilde s_y-s_y}{s_y}
\right|
\le
\xi,
\qquad
\xi:=\eta+\frac{b}{\delta}.
```

$\xi<1$ なら規格化重みの全変動誤差は

```math
D_{\rm TV}(\widetilde p,p^\delta)
\le
\frac{\xi}{1-\xi}
```

で抑えられる。これはchannel数の粗い和を取らないaggregate relative-error boundである。

一方、各signal modeへ状態非依存の独立additive noiseを直接注入する場合はR186の障害が残る。本定理はR186を解消しない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R206C）**

R206Aの厳密解に対して任意初期分布の偏差を $\frac12\sum_y|d_y(0)|\leq1$ で抑え、hub質量を完全結果空間に残す。R206Bのregularization差を三角不等式で加え、generator perturbationにはMarkov半群の縮約性とDuhamel評価を使う。local scale誤差については $(1-\xi)s_y\leq\widetilde s_y\leq(1+\xi)s_y$ を規格化前後で比較すれば表示の全変動距離上界を得る。証明終。
<!-- theorem-end:proof -->


## X.7 R206D：Q2-1、Q2-3、Q2-4 readout bridge

R181C後の実際の一試行terminal signalを $Z_{\rm out}$ とする。理想回路出力を $Z_C^{\rm id}$ とし、状態方向誤差を $\varepsilon_{\rm ray}$ とする。

Q2-1では $L=4$、Q2-3では $L=8$、Q2-4では $L=2^n$ と特殊化する。R206A--R206C samplerへ

```math
J_y=\mathcal J_0|Z_{{\rm out},y}|^2
```

を局所入力する。

<!-- theorem-start:theorem -->
**定理（R206D：Q2 terminal multi-outcome readout）**

terminal signal作用をR206A--R206Cへ同一試行内で物理的に接続し、外部制御器が最終Born表・振幅表・結果別係数表を入力しないとする。すると理想極限で

```math
P(Y=y)
=
\frac{|Z_{{\rm out},y}|^2}
{\sum_z|Z_{{\rm out},z}|^2}.
```

有限実装では

```math
D_{\rm TV}(P_{\rm out},P_C)
\le
\varepsilon_{\rm ray}
+
\varepsilon_{\rm samp}.
```

Q2-4では $Y\in\{0,1\}^n$ を固定配線のconfiguration labelとして読み、外部readoutは $O(n)$ bitとする。全chamberを外部走査して結果を探索する方式は本定理の一様装置条件を満たさない。
<!-- theorem-end:theorem -->

Q2-1/Q2-3/Q2-4ではterminal readout後に非規格化射影成分を次段へ渡さないため、R181D型逐次projector treeと非終端作用回復を要求しない。R181DはQ1/Q2-2のsame-trial post-state handoffへ責務を限定する。

## X.8 R206E：Q2-4 uniform root preparation / refresh

Q2-4の計算開始rootを

```math
Z_\star=z_\star e_{0^n}
```

とする。全signal modeへ同じ減衰率 $\gamma_{\rm p}>0$ を作用させ、固定root portだけへ同じ装置族で一定driveを入れるopen preparation law

```math
\dot Z_y
=
-\gamma_{\rm p} Z_y
+
\gamma_{\rm p} z_\star\,\delta_{y,0^n}
```

を用いる。これは各modeの初期値、Born重み、回路出力表を外部から入力しない。

<!-- theorem-start:theorem -->
**定理（R206E：uniform root preparation / refresh）**

初期誤差が

```math
\|Z(0)-Z_\star\|\leq B_{\rm p}
```

を満たす任意の前試行状態に対し、

```math
Z(t)-Z_\star
=
e^{-\gamma_{\rm p}t}
[Z(0)-Z_\star],
```

従って

```math
\|Z(T_{\rm p})-Z_\star\|
\leq
B_{\rm p}e^{-\gamma_{\rm p}T_{\rm p}}.
```

$B_{\rm p}$、$\gamma_{\rm p}^{-1}$ が $n,d,1/\epsilon$ の多項式で抑えられるなら、

```math
T_{\rm p}
\geq
\gamma_{\rm p}^{-1}
\log\frac{B_{\rm p}}{\epsilon_{\rm p}}
```

でroot preparation時間は多項式である。外部制御はglobal preparation windowと固定root portだけであり、$2^n$ modeの個別reset、個別較正、指数長初期化表を要求しない。

またR206Aはsampler pointerの任意初期分布から同じtarget lawへ指数収束するため、Q2-4の一出力標本生成にpointerの結果別明示resetを要求しない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R206E）**

各成分について一次線形方程式を解けば表示の指数収束を得る。pointer側はR206Aの $d_y(t)=e^{-\Lambda t}d_y(0)$ をそのまま適用する。証明終。
<!-- theorem-end:proof -->

R206EはQ2-4 fixed-goalの準備・refresh資源を閉じるopen lawである。永久record、装置全体の自律clock、全系列を通じたjoint-device renewalはM0へ残す。

## X.9 terminal action保持とbackreaction境界

action-angle表示でsampler couplingが $J_y$ とreservoir座標だけに依存し、$\phi_y$ に依存しないなら

```math
\dot J_y
=
-\frac{\partial H_{\rm int}}{\partial\phi_y}
=
0.
```

従ってgate終了後のterminal readoutではsignal actionをQND型に保持できる。

一方、R181Cのcoherent gate実行中から同じ有限強度couplingを常時作用させても位相coherenceを十分保てることは本付録では証明しない。always-on passive coupling、finite-bandwidth reservoir、full Hamiltonian lift、gate中のphase backreactionはM66 strengtheningとして残す。

## X.10 Q2-4資源境界

$L=2^n$ のとき内部受動資源として次を許容・報告する。

- signal mode数：$2^n$。
- result chamber数：$2^n$。
- phase-volume内部自由度：保守的に $O(n2^n)$。
- hub capacity、総conductance、総bath容量、総熱：指数的でもよいが規模を報告する。

外部運用資源には次を要求する。

- gate program長：$\operatorname{poly}(n,d)$。
- sampler制御：global parameter $\Lambda,\kappa,\delta,T$ と固定一様規則だけ。
- channel別Born表・振幅表・係数表：不要。
- terminal readout：$O(n)$ bit。
- sampling時間：
```math
O\left(
\Lambda^{-1}\log\frac1\epsilon
\right).
```
- $\delta^{-1}$、$\Lambda^{-1}$、$\kappa^{-1}$、必要なlocal relative precision：$\operatorname{poly}(n,d,1/\epsilon)$ 以内。

R186のdirect-amplitude registerに対する独立additive-noise障害は独立に残る。従ってM66/R206追加だけからQ2-4を達成へ昇格しない。

## X.11 fixed-goal status

M66/R205A--R205Fをcommon thermal-reservoir parentとして採用し、R206A--R206EをQ2-1/Q2-3/Q2-4のterminal multi-outcome readout specializationとして維持する。

現行責務は次のように分離する。

- Q1およびQ2-2の逐次binary instrument：M65/R204D--R204F＋R181D。
- Q2-1/Q2-3/Q2-4のterminal joint readout：M66/R206A--R206D。
- Q2-4のuniform root preparation / refresh：R206E。
- Q2-2および全周期renewal側のopen reset：R179。
- Q2-4のdirect-amplitude register additive-noise監査：R186。

Q2-4の旧逐次binary readout、非終端作用安定化、結果別routerはfixed-goal主線から外す。Q2-4の条件付き達成はR186障害が残るため維持する。
