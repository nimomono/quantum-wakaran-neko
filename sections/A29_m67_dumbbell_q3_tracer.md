@number: AC
@chapter: 付録
@title: M67 伸縮Brownian dumbbell Q3 continuous-tracer profile
@status: R214A--R214BをM67 continuous-tracer profileのrequired主線とする。R209A/R209Bをgeneric flow / finite-bath補題として使い、R214B自身がsmall-mass W1 bridgeを閉じる。R208B/R208C/R209Cはdraft-145では退役させずactive regressionとして残し、finite-graph Q3-4A/Q3-4B/Q3-5にはR214を流用しない。

## AC.1 目的と責務境界

draft-145以後のM67 continuous-tracer profileは、本付録の三次元伸縮Brownian dumbbellをrequired主線とする。旧AA.3/R208Bのinverse-designed phase-volume implementationはPR1ではactive regressionとして残すが、Q3-2のfixed-goal直接主線から外す。

主要物理sectorは従来どおり「structured reservoir + marker/tracer」の二分類である。dumbbellの内部相対座標はmarker/tracer内部自由度であり、新しい第三物理実体とは数えない。structured reservoir側のM37 coherent sector、R209 flow/drag sector、R210A coherent compatibilityは再利用する。

本付録はcontinuous Q3-2だけを対象にする。finite-graph Q3-4A/Q3-4B/Q3-5はR208D/R203D profileを維持し、本付録のdumbbellを要求しない。

## AC.2 M37局所強度とdumbbell Hamiltonian

M37の実正準座標を

```math
Q_i=\sqrt{M_{\rm osc}\omega_0}\,q_i,
\qquad
P_i=\frac{p_i}{\sqrt{M_{\rm osc}\omega_0}}
```

とし、固定smooth partition of unity $\chi_i(X)$ を用いて局所強度

```math
\varrho_X
=
\frac1{N_0}
\sum_i\chi_i(X)
\frac{Q_i^2+P_i^2}{2\mathcal J_0}
\ge0
```

を定める。$N_0>0$ はprepared coherent-action scaleである。複素包絡 $Z$ や $|Z|$ を独立canonical variableとしてHamiltonianへ戻さない。

dumbbellの重心を $(X,P_X)$、内部相対座標を $(\mathbf r,\mathbf p)\in\mathbb R^3\times\mathbb R^3$ とする。有限自然長

```math
\ell_X^2
=
\ell_0^2+\alpha\varrho_X,
\qquad
\ell_0>0,
\qquad
\alpha>0
```

を採用する。smooth collision coreを

```math
\rho_c(\mathbf r)
=
\sqrt{|\mathbf r|^2+a_c^2},
\qquad
a_c>0
```

とし、

```math
H_{\rm db}
=
\frac{|\mathbf p|^2}{2\mu}
+
\frac{k}{2}
\left[
\rho_c(\mathbf r)-\ell_X
\right]^2
```

と置く。$\ell_0>0$ と $a_c>0$ により、signal nodeと二質点重なりの両方で全Hamiltonianはsmoothで下に有界である。

熱幅を

```math
\sigma_T^2=\frac{k_BT}{k}
```

と書く。

## AC.3 R214A：一バネdumbbell phase-volume / osmotic force

まずcoreless $a_c=0$ を考える。固定したsignalとtracer位置における内部canonical位置積分は

```math
I(\ell)
=
\int_0^\infty
r^2
\exp\left[
-\frac{(r-\ell)^2}{2\sigma_T^2}
\right]dr.
```

$a=\ell/\sigma_T$、標準正規密度と累積分布を $\phi,\Phi$ とすると厳密に

```math
I(\ell)
=
\sigma_T\sqrt{2\pi}
(\ell^2+\sigma_T^2)
G(a),
```

```math
G(a)
=
\Phi(a)
+
\frac{a\phi(a)}{1+a^2}.
```

また

```math
G'(a)
=
\frac{2\phi(a)}{(1+a^2)^2}.
```

したがって

```math
\varrho_T
=
\frac{\ell_0^2+\sigma_T^2}{\alpha}
```

と置けば

```math
Z_{\rm db}^{(0)}
=
C_T
(\varrho_X+\varrho_T)
G(a_X),
\qquad
a_X=\frac{\ell_X}{\sigma_T},
```

であり、

```math
F_{\rm db}^{(0)}
=
-k_BT\log(\varrho_X+\varrho_T)
-k_BT\log G(a_X)
+C_T'.
```

<!-- theorem-start:theorem -->
**定理（R214A：三次元伸縮dumbbellのphase-volume osmotic force）**

上のcoreless dumbbellについて

```math
\left\langle F_X^{\rm db}\right\rangle
=
\left[
1+\varepsilon_F(a_X)
\right]
k_BT
\partial_X\log(\varrho_X+\varrho_T),
```

```math
\varepsilon_F(a)
=
\frac{
\phi(a)
}{
a(1+a^2)G(a)
}
```

が厳密に成立する。$a_X\ge a_0:=\ell_0/\sigma_T>0$ なので

```math
0
\le
\varepsilon_F(a_X)
\le
\varepsilon_F(a_0)
```

という一様safe-sector評価を持つ。

smooth core $a_c>0$ については $a_c/\ell_0\ll1$ の固定safe sectorで

```math
F_{\rm db}
=
F_{\rm db}^{(0)}
+
R_{\rm core},
```

```math
|\partial_XR_{\rm core}|
\le
C_{\rm core}(a_0)
\frac{a_c^2}{\ell_0^2+\sigma_T^2}
\left|
k_BT\partial_X\log(\varrho_X+\varrho_T)
\right|
+
R_{\rm tail}
```

と評価でき、$R_{\rm tail}$ は $r\lesssim a_c$ のGaussian tailとして $a_0$ 増大とともに指数的に小さくなる。

特に $\ell_0=2.5\sigma_T$ ではcoreless force correctionは

```math
\varepsilon_F(2.5)
<
9.7\times10^{-4},
```

$\ell_0=3\sigma_T$ では

```math
\varepsilon_F(3)
<
1.5\times10^{-4}.
```
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R214A）**

$z=(r-\ell)/\sigma_T$ と置き、Gaussianの0次、1次、2次不完全momentを積分すると表示した $I(\ell)$ を得る。$\ell_X^2+\sigma_T^2=\alpha(\varrho_X+\varrho_T)$ を代入してfree energyを分離する。$G'(a)=2\phi(a)/(1+a^2)^2$ を直接微分で得て、$2\ell_X\partial_X\ell_X=\alpha\partial_X\varrho_X$ を用いれば $\varepsilon_F$ の式が従う。$a>0$ で $\varepsilon_F$ は単調減少する。

smooth coreは積分を $r<a_c$ と $r\ge a_c$ に分け、後者で $\sqrt{r^2+a_c^2}=r+O(a_c^2/r)$ を用いる。前者は $\ell_X\ge\ell_0$ によりGaussian tailへ吸収できる。証明終。
<!-- theorem-end:proof -->

### AC.3.1 $\ell_0=0$ を採らない理由

$\ell_0=0$ では $\ell=\sqrt{\alpha\varrho}$ となり、

```math
G(a)
=
\frac12
+
\sqrt{\frac2\pi}a
+
O(a^2)
```

なので

```math
Z_{\rm db}
=
Z_0
+
C_1\sqrt{\varrho}
+
O(\varrho).
```

従ってnodeで $\partial_\varrho\log Z_{\rm db}$ が非解析になる。一本バネの物理像を維持しnode-safe Hamiltonianを得るため、required continuous profileでは有限自然長 $\ell_0>0$ を採用する。

## AC.4 finite harmonic bath

同じstructured mediumのthermal modeをdumbbell内部相対座標へ並進型に結合する。

```math
H_{{\rm db},B}
=
\sum_{a=1}^3
\sum_{\mu=1}^{N_B}
\left[
\frac{\Pi_{a\mu}^2}{2m_\mu}
+
\frac{m_\mu\omega_\mu^2}{2}
(\zeta_{a\mu}-c_\mu r_a)^2
\right].
```

固定 $\mathbf r$ で $\zeta_{a\mu}\mapsto\zeta_{a\mu}-c_\mu r_a$ と平行移動できるので、このbathはR214Aのcanonical位置weightを変更しない。

bathを厳密消去すると

```math
\mu\ddot r_a
=
-\partial_{r_a}V_{\rm db}
-
\int_0^t
\Gamma_N(t-s)\dot r_a(s)ds
+
\xi_{a,N}(t),
```

```math
\Gamma_N(t)
=
\sum_\mu
m_\mu\omega_\mu^2c_\mu^2
\cos(\omega_\mu t),
```

```math
\left\langle
\xi_{a,N}(t)
\xi_{b,N}(s)
\right\rangle
=
\delta_{ab}k_BT\Gamma_N(t-s)
```

を得る。finite-spectrumからDrude kernelへの固定有限時間近似はR209Bと同じ補題を再利用する。

## AC.5 3次元Brownian dumbbellとR214A定常測度

short-memoryとsmall internal massの極では

```math
d\mathbf r_t
=
-\frac1{\gamma_r}
\nabla_{\mathbf r}V_{\rm db}\,dt
+
\sqrt{\frac{2k_BT}{\gamma_r}}d\mathbf W_t
+
R_r(t).
```

corelessで $r_t=|\mathbf r_t|$ とするとItô公式から

```math
dr_t
=
\left[
-\frac{k}{\gamma_r}(r_t-\ell_X)
+
\frac{2k_BT}{\gamma_rr_t}
\right]dt
+
\sqrt{\frac{2k_BT}{\gamma_r}}dW_t.
```

従って固定 $X$ の定常半径密度は

```math
p_{\rm eq}(r\mid X)
\propto
r^2
\exp\left[
-\frac{k(r-\ell_X)^2}{2k_BT}
\right],
```

であり、R214Aの位相体積measureと一致する。別のauxiliary rotorやRMS読出し座標を必要としない。

## AC.6 fast内部緩和とsingle-dumbbell force fluctuation

coreless radial driftを

```math
b_\ell(r)
=
-\frac{k}{\gamma_r}(r-\ell)
+
\frac{2k_BT}{\gamma_rr}
```

とすると

```math
\partial_rb_\ell(r)
=
-\frac{k}{\gamma_r}
-
\frac{2k_BT}{\gamma_rr^2}
\le
-\frac1{\tau_r},
\qquad
\tau_r=\frac{\gamma_r}{k}.
```

したがって同一noise couplingで固定$\ell$ dynamicsは少なくとも $e^{-t/\tau_r}$ でcontractする。slow target $\ell_t$ に対するtracking errorはsafe sectorで

```math
W_1(\mathcal L(r_t),\pi_{\ell_t})
\le
e^{-t/\tau_r}d_0
+
C_\pi(a_0)\tau_r
\sup_{s\le t}|\dot\ell_s|
+
R_r(t)
```

と評価する。

single dumbbellでは旧phase-volume mode群の $N_\rho^{-1/2}$ 自己平均化を使わない。内部力揺らぎを

```math
\delta F_X^{\rm db}
=
F_X^{\rm db}
-
\langle F_X^{\rm db}\rangle
```

とし、Green--Kubo摩擦

```math
\zeta_{\rm db}(X)
=
\beta
\int_0^\infty
\langle
\delta F_X^{\rm db}(t)
\delta F_X^{\rm db}(0)
\rangle_{\rm eq}
dt
```

process-law誤差には符号相殺を使わないabsolute correlation integralも分離する。

```math
\zeta_{\rm db}^{\rm abs}(X)
=
\beta
\int_0^\infty
\left|
\operatorname{Cov}_{\rm eq}
\left(
\delta F_X^{\rm db}(t),
\delta F_X^{\rm db}(0)
\right)
\right|dt.
```

を定める。半径effective potential

```math
U_{\rm eff}(r)
=
\frac{k}{2}(r-\ell)^2
-
2k_BT\log r
```

は

```math
U_{\rm eff}''(r)
=
k+\frac{2k_BT}{r^2}
\ge k
```

なのでspectral-gap boundから

```math
\zeta_{\rm db}^{\rm abs}(X)
\le
C_{\rm mix}(a_0)
\gamma_r
(\partial_X\ell_X)^2,
\qquad
|\zeta_{\rm db}(X)|
\le
\zeta_{\rm db}^{\rm abs}(X).
```

strong convexityからradial Markov semigroupは指数相関減衰を持つため、このabsolute boundを取れる。同時にFDTにより対応する追加noiseが生じる。主重心摩擦 $\gamma_X$ に対し

```math
\varepsilon_{\rm fr}
=
\sup_X
\frac{|\zeta_{\rm db}(X)|}{\gamma_X},
\qquad
\varepsilon_{\rm fr}^{\rm abs}
=
\sup_X
\frac{\zeta_{\rm db}^{\rm abs}(X)}{\gamma_X}
\ll1.
```

を要求する。

## AC.7 M37へのbackreaction

局所強度を

```math
\varrho_X
=
\frac{b^\dagger B_Xb}{N_0}
```

と書くと

```math
\frac{\partial\ell_X}{\partial b^*}
=
\frac{\alpha}{2N_0\ell_X}
B_Xb.
```

したがってprepared dumbbell energy shell $H_{\rm db}\le E_*$、$\ell_X\ge\ell_0$、$\|b\|=O(\sqrt{N_0})$ ではsignalへの絶対loadは

```math
\|G_{\rm db}\|
=
O(N_0^{-1/2}),
```

bare signalとの相対固定有限時間loadは

```math
q_{\rm load}^{\rm db}(T)
=
O(N_0^{-1}).
```

また

```math
H_{\rm db}[e^{i\theta}b]
=
H_{\rm db}[b]
```

なのでcommon carrier phase/actionを直接吸収しない。R210AのDuhamel/bootstrap評価を同じ形で再利用できる。

## AC.8 R214B：finite-bath dynamic lift / Q3-2 compatibility

R214Aのregularized densityを

```math
\widetilde\rho
=
\varrho+\varrho_T
```

とし、canonical M64 target driftを

```math
b_{64}^{\rm db}(x,t)
=
U_X^{64}(x,t)
+
\nu\partial_x\log\widetilde\rho(x,t),
\qquad
\nu=\frac{k_BT}{\gamma_X}
```

と定める。$\varrho_T$ は空間・時間に依らないので、規格化後も $J/\widetilde\rho$ と $\partial_x\log\widetilde\rho$ は不変である。

finite bathとfast dumbbellをMarkov化した後の重心を $(X_t^M,V_t^M)$ とし、

```math
dX_t^M=V_t^Mdt,
```

```math
M_XdV_t^M
=
-\gamma_X
\left[
V_t^M
-
b_{64}^{\rm db}(X_t^M,t)
-
e_{214}(X_t^M,t)
\right]dt
+
\sqrt{2\gamma_Xk_BT}\,dW_t
+
\delta F_t^{\rm db}dt
```

と書く。$e_{214}$ はR209Aのflow residual、R214Aのshell/core mean-force residual、fast-dumbbell tracking、R210Aから渡るsignal-load residualを一度ずつ含む決定論的drift mismatchで、

```math
\Delta_{214}^{\rm drift}
:=
\|e_{214}\|_\infty
```

と置く。$\delta F_t^{\rm db}$ はAC.6の中心化内部forceである。

small-mass parameterを

```math
\epsilon_M=\frac{M_X}{\gamma_X}
```

とし、

```math
Y_t=X_t^M+\epsilon_MV_t^M
```

と置けば、追加dumbbell fluctuationを除く部分について厳密に

```math
dY_t
=
\left[
b_{64}^{\rm db}(X_t^M,t)
+
e_{214}(X_t^M,t)
\right]dt
+
\sqrt{2\nu}\,dW_t
```

となる。したがって同じBrownian motionで

```math
dX_t^{64}
=
b_{64}^{\rm db}(X_t^{64},t)dt
+
\sqrt{2\nu}\,dW_t
```

を駆動し、$b_{64}^{\rm db}$ が空間Lipschitz定数 $L_b$、一様bound $B_*$ を持ち、velocityをMaxwell preparationすれば、

```math
\sup_{t\le T}
W_1
\left(
\mathcal L(X_t^M),
\mathcal L(X_t^{64})
\right)
\le
e^{L_bT}
\left[
\varepsilon_{\rm init}
+
T\Delta_{214}^{\rm drift}
\right]
+
C_{\rm sm}(L_b,T)
\left[
\epsilon_M
(B_*+\Delta_{214}^{\rm drift})
+
\sqrt{\nu\epsilon_M}
\right]
+
R_{\rm db}^{W_1}(T),
```

と評価できる。ここで $C_{\rm sm}(L_b,T)$ は固定有限時間で有限な定数である。

single-dumbbellの中心化forceについて

```math
A_t
=
\frac1{\gamma_X}
\int_0^t
\delta F_s^{\rm db}ds
```

とするとAC.6から

```math
\mathbb E|A_t|
\le
\sqrt{
2\nu t
\varepsilon_{\rm fr}^{\rm abs}
}.
```

またfast-variable消去で生じる追加Green--Kubo dragは

```math
|R_{\rm lag-fr}^{W_1}(T)|
\le
C_TT\varepsilon_{\rm fr}
\left[
B_*+\Delta_{214}^{\rm drift}
+
\sqrt{\frac{\nu}{\epsilon_M}}
\right].
```

したがって

```math
R_{\rm db}^{W_1}(T)
\le
\varepsilon_{\rm bath}^{X}(T)
+
C_TT\varepsilon_{\rm fr}
\left[
B_*+\Delta_{214}^{\rm drift}
+
\sqrt{\frac{\nu}{\epsilon_M}}
\right]
+
C_T
\sqrt{
2\nu T
\varepsilon_{\rm fr}^{\rm abs}
}.
```

<!-- theorem-start:theorem -->
**定理（R214B：finite-bath dumbbellの動的osmotic縮約とQ3-2 compatibility）**

R214Aのsafe sector、R209Aのgeneric flow compatibility、R209Bのgeneric finite harmonic bath / Markov--FDT条件を仮定する。さらに

```math
\tau_{\rm mem}^{(r)}
\ll
\frac{\mu}{\gamma_r}
\ll
\tau_r=\frac{\gamma_r}{k}
\ll
\tau_{\rm slow}
\ll
T_{\rm rec}^{(r)},
```

```math
\epsilon_M=\frac{M_X}{\gamma_X}\ll1,
\qquad
\varepsilon_{\rm fr}=o(\sqrt{\epsilon_M}),
\qquad
\varepsilon_{\rm fr}^{\rm abs}\to0
```

を満たすとする。このときM67 dumbbell tracerとcanonical M64 tracerについて

```math
\sup_{t\le T}
W_1
\left(
\mathcal L(X_t^{67,{\rm db}}),
\mathcal L(X_t^{64})
\right)
\le
\varepsilon_{214\to64}(T),
```

```math
\varepsilon_{214\to64}(T)
=
\varepsilon_{\rm bath}^{X}
+
e^{L_bT}
\left[
\varepsilon_{\rm init}
+
T\Delta_{214}^{\rm drift}
\right]
+
C_{\rm sm}
\left[
\epsilon_M(B_*+\Delta_{214}^{\rm drift})
+
\sqrt{\nu\epsilon_M}
\right]
+
C_TT\varepsilon_{\rm fr}
\left[
B_*+\Delta_{214}^{\rm drift}
+
\sqrt{\frac{\nu}{\epsilon_M}}
\right]
+
C_T
\sqrt{
2\nu T\varepsilon_{\rm fr}^{\rm abs}
}
```

を得る。ここで $\Delta_{214}^{\rm drift}$ にはshell/core、flow/material-frame、tracking、signal-loadの各偏差を一度だけ含め、M64自身のR203C baseline errorは含めない。

従ってR203Cとの三角不等式から

```math
W_1
\left(
\mathcal L(X_t^{67,{\rm db}}),
\widetilde\rho(t)
\right)
\le
\varepsilon_{214\to64}(T)
+
\varepsilon_{\rm red}^{64}(T).
```

$\partial_t\widetilde\rho+\partial_XJ=0$ なので、R161/R185の既存regularized lawへそのまま接続する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R214B）**

R209Bをdumbbell内部座標へ特殊化してfinite translated harmonic bathを消去し、short-memoryとsmall internal massでAC.5の三次元Brownian dumbbellを得る。Itô公式から半径の幾何学drift $2D_r/r$ が生じ、R214Aの $r^2$ canonical measureを回収する。AC.6の一方向contractivityによりmoving $\ell_t$ へのtracking residualを $\Delta_{214}^{\rm drift}$ へ入れる。

重心small-mass極では $Y=X+\epsilon_MV$ を使うと上のSDEが厳密に得られる。同じBrownian motionでM64過程を駆動し、$X=Y-\epsilon_MV$、drift Lipschitz性、Maxwell preparationの
$\epsilon_M\sup_{t\le T}\mathbb E|V_t|
=
O(\epsilon_MB_*)+O(\sqrt{\nu\epsilon_M})$
を使ってGronwall評価する。中心化dumbbell forceの積分はAC.6のabsolute covariance積分で二乗平均評価し、追加Green--Kubo dragは $\varepsilon_{\rm fr}$ で別に抑える。R209Aのflow residualとR210Aのload-only signal errorを合成すれば表示した $W_1$ boundを得る。R209Cは用いない。最後の式はR203Cとの三角不等式である。証明終。
<!-- theorem-end:proof -->

## AC.9 明示parameter witness

静的幾何について

```math
\ell_0=2.5\sigma_T,
\qquad
a_c=0.02\sigma_T
```

を取るとcoreless force correctionは $<9.7\times10^{-4}$ である。動的時間尺度のdimensionless witnessとして

```math
\tau_{\rm mem}^{(r)}=10^{-7},
\qquad
\mu/\gamma_r=10^{-6},
\qquad
\tau_r=10^{-3},
\qquad
\tau_{\rm slow}=1,
\qquad
T_{\rm rec}^{(r)}=100
```

を取れる。さらに

```math
\gamma_r/\gamma_X=10^{-3},
\qquad
\sup_X|\partial_X\ell_X|\le0.1
```

なら $C_{\rm mix}=O(1)$ の範囲で追加摩擦比は $O(10^{-5})$ である。さらに小parameter $\lambda\to0$ に対し

```math
\epsilon_M=\lambda^2,
\qquad
\varepsilon_{\rm fr},
\varepsilon_{\rm fr}^{\rm abs}
=
O(\lambda^3),
\qquad
\tau_r=O(\lambda^3),
\qquad
\mu/\gamma_r=O(\lambda^4)
```

と取れば、small-mass、追加drag/noise、fast-internal条件を同時に0へ送れる。これは必要parameter windowが空でないことのwitnessであり、唯一の物理較正ではない。

## AC.10 required主線と責務境界

draft-145でR214A--R214Bをcontinuous Q3-2のrequired主線へ昇格する。

- R209A/R209Bはgeneric flow / finite-bath補題としてR214B内部から使う。
- R214BはR209Cを参照せずsmall-mass $W_1$ bridgeを自身で閉じる。
- R210Aはgeneric coherent-load theoremとしてdumbbell loadを受ける。
- R208B/R208C/R209CはPR1ではactive regressionとして残し、退役は後続PRへ分離する。
- R208Dはprofile-dispatch bridgeとしてactive維持する。
- finite-graph Q3-4A/Q3-4B/Q3-5へR214を流用しない。
- Q3-2-A1/A2を変更しない。supporting reduced witnessだけからA2を昇格しない。
