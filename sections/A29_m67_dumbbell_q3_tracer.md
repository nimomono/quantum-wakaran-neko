@number: AC
@chapter: 付録
@title: M67 伸縮Brownian dumbbell Q3 continuous-tracer profile
@status: R214A--R214BをM67 continuous-tracer profileのrequired主線とする。R214本体はgeneric density/flow port theoremとしてR209B finite-bath/FDTを使い、current M37/M64 specializationでのみR210A coherent-load stabilityとR209A flow compatibilityを合成する。旧R208B/R208C/R209Cはdraft-146でactive resultから退役し、finite-graph Q3-4A/Q3-4B/Q3-5にはR214を流用しない。

## AC.1 目的と責務境界

draft-145以後のM67 continuous-tracer profileは、本付録の三次元伸縮Brownian dumbbellをrequired主線とする。draft-149ではR214A--R214BをM37固有の局所強度から切り離し、resolved source state $z$ から読み出す正のscalar port $\varrho(X;z)$ とflow port $U(X;z)$ を入力とするgeneric transducer theoremへ一般化する。

主要物理sectorは従来どおり「structured reservoir + marker/tracer」の二分類である。dumbbellの内部相対座標はmarker/tracer内部自由度であり、新しい第三物理実体とは数えない。$\varrho$ と $U$ はsource sectorから構成されるportであり、独立の統計実体を単一試行へ書き戻すものではない。

current M67 specializationではM37/R210Aが局所強度portとcoherent load stabilityを、R209A/M64がflow port compatibilityを供給する。R214本体はそれらのsource-specific構成を仮定せず、port値とその安定性誤差だけを受け取る。finite harmonic bath/FDTはgeneric R209Bを再利用する。

本付録はcontinuous Q3-2だけを対象にする。finite-graph Q3-4A/Q3-4B/Q3-5はR208D/R203D profileを維持し、本付録のdumbbellを要求しない。

## AC.2 generic density/flow portとdumbbell Hamiltonian

resolved source stateを $z$ とし、tracer位置 $X$ で読み出すsmooth scalar portとflow portを

```math
\varrho_X
=
\mathcal R(X;z)
\ge0,
\qquad
U_X
=
\mathcal U(X;z)
```

と書く。R214Aの静的計算では $\varrho_X$ が $C^1$ であればよく、R214Bでは後で定めるtarget driftがboundedかつ空間Lipschitzであることを要求する。$\varrho$ は規格化確率密度である必要はなく、source sectorから物理的に読み出される非負scalar portであればよい。

dumbbellの重心を $(X,P_X)$、内部相対座標を $(\mathbf r,\mathbf p)\in\mathbb R^3\times\mathbb R^3$ とする。有限自然長を

```math
\ell_X^2
=
\ell_0^2+\alpha\varrho_X,
\qquad
\ell_0>0,
\qquad
\alpha>0
```

と置く。smooth collision coreを

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

と置く。$\ell_0>0$ と $a_c>0$ により、port nodeと二質点重なりの両方で全Hamiltonianはsmoothで下に有界である。

熱幅を

```math
\sigma_T^2=\frac{k_BT}{k}
```

とし、

```math
\varrho_T
=
\frac{\ell_0^2+\sigma_T^2}{\alpha},
\qquad
\widetilde\varrho
=
\varrho+\varrho_T
```

と定める。$\varrho_T>0$ なので $\widetilde\varrho\ge\varrho_T$ がglobal node-safe lower boundを与える。

## AC.3 R214A：generic port phase-volume / reciprocal mean force

まずcoreless $a_c=0$ を考える。固定したsource stateとtracer位置における内部canonical位置積分は

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
\frac{a\phi(a)}{1+a^2},
\qquad
G'(a)
=
\frac{2\phi(a)}{(1+a^2)^2}.
```

$\ell^2+\sigma_T^2=\alpha(\varrho+\varrho_T)$ なので

```math
Z_{\rm db}^{(0)}
=
C_T
(\varrho+\varrho_T)
G(a),
```

```math
F_{\rm db}^{(0)}
=
-k_BT\log(\varrho+\varrho_T)
-k_BT\log G(a)
+C_T'.
```

<!-- theorem-start:theorem -->
**定理（R214A：三次元伸縮dumbbellのgeneric port phase-volume / reciprocal mean force）**

$k,T,\ell_0,\alpha$ を固定し、scalar parameter $\lambda$ への依存が $\varrho(\lambda)$ を通じてのみ入るとする。coreless dumbbellでは

```math
\left\langle
F_\lambda^{\rm db}
\right\rangle
:=
\left\langle
-\partial_\lambda H_{\rm db}
\right\rangle
=
-\partial_\lambda F_{\rm db}^{(0)}
```

かつ

```math
\left\langle
F_\lambda^{\rm db}
\right\rangle
=
\left[
1+\varepsilon_F(a)
\right]
k_BT
\partial_\lambda
\log(\varrho+\varrho_T),
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

が厳密に成立する。vector parameterについては各成分へ同じ式を適用する。$a\ge a_0:=\ell_0/\sigma_T>0$ なので

```math
0
\le
\varepsilon_F(a)
\le
\varepsilon_F(a_0)
```

という一様safe-sector評価を持つ。

$\lambda=X$ とすればtracerへのosmotic mean force、$\lambda=z_A$ とすればsource coordinateへのreciprocal mean forceを同じ式から得る。

smooth core $a_c>0$ については $a_c/\ell_0\ll1$ の固定safe sectorで

```math
F_{\rm db}
=
F_{\rm db}^{(0)}
+
R_{\rm core}(\ell),
```

```math
|\partial_\lambda R_{\rm core}|
\le
C_{\rm core}(a_0)
\frac{a_c^2}{\ell_0^2+\sigma_T^2}
\left|
k_BT
\partial_\lambda
\log(\varrho+\varrho_T)
\right|
+
R_{{\rm tail},\lambda}
```

と評価でき、$R_{{\rm tail},\lambda}$ は $r\lesssim a_c$ のGaussian tailとして $a_0$ 増大とともに指数的に小さくなる。

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

$z=(r-\ell)/\sigma_T$ と置き、Gaussianの0次、1次、2次不完全momentを積分すると表示した $I(\ell)$ を得る。$\ell^2+\sigma_T^2=\alpha(\varrho+\varrho_T)$ を代入してfree energyを分離する。

$2\ell\,\partial_\lambda\ell=\alpha\partial_\lambda\varrho$ と $\alpha(\varrho+\varrho_T)=\sigma_T^2(1+a^2)$ を使うと

```math
\frac{
(G'(a)/G(a))\partial_\lambda a
}{
\partial_\lambda\log(\varrho+\varrho_T)
}
=
\frac{1+a^2}{2a}
\frac{G'(a)}{G(a)}
=
\varepsilon_F(a).
```

$\partial_\lambda\varrho=0$ の場合は両辺が0なので同じ式が成り立つ。canonical measureの積分領域は $\lambda$ に依存しないため $\partial_\lambda F=\langle\partial_\lambda H\rangle$ であり、mean-force identityが従う。$a>0$ で $\varepsilon_F$ は単調減少する。

smooth coreは積分を $r<a_c$ と $r\ge a_c$ に分け、後者で $\sqrt{r^2+a_c^2}=r+O(a_c^2/r)$ を使ってまず $dR_{\rm core}/d\ell$ を評価し、$\partial_\lambda\ell=(\alpha/2\ell)\partial_\lambda\varrho$ で任意parameterへ移す。前者は $\ell\ge\ell_0$ によりGaussian tailへ吸収できる。証明終。
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

## AC.5 3次元Brownian dumbbell、Stratonovich規約とR214A定常測度

一次的な有限Hamiltonianではbath相関時間は有限であり、確率微分規則の選択はない。本稿では有限相関GLEからwhite-noise Markov lawを取る物理的極限をStratonovich表示で記述し、Itô表示はFokker--Planck、Bayes条件付き率、非線形座標変換の計算に必要な場合だけ使う。

short-memoryとsmall internal massの極ではCartesian内部座標について

```math
d\mathbf r_t
=
-\frac1{\gamma_r}
\nabla_{\mathbf r}V_{\rm db}\,dt
+
\sqrt{\frac{2k_BT}{\gamma_r}}
\circ d\mathbf W_t
+
R_r(t).
```

noise amplitudeは定数なのでCartesian座標ではStratonovichとItôが一致する。corelessで $r_t=|\mathbf r_t|$ とし、半径過程をItô表示へ変換すると

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

$2D_r/r$ はCartesianな有限相関極限を半径座標へ写した3次元幾何学driftであり、Itôを物理的基本規約に選んだために追加した項ではない。従って固定 $X$ の定常半径密度は

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

## AC.7 generic reciprocal loadとport stability

source coordinateを $z$ とする。$z$ 依存が $\varrho(X;z)$ を通じてのみ入るとき、dumbbellからsourceへ戻る瞬間的Hamiltonian loadは

```math
F_z^{\rm db}
=
-\nabla_zH_{\rm db}
=
k(\rho_c-\ell)
\nabla_z\ell,
```

```math
\nabla_z\ell
=
\frac{\alpha}{2\ell}
\nabla_z\varrho.
```

prepared energy shell $H_{\rm db}\le E_*$ と $\ell\ge\ell_0$ から

```math
|\rho_c-\ell|
\le
\sqrt{\frac{2E_*}{k}}
```

なので、pointwiseに

```math
\|F_z^{\rm db}\|
\le
\frac{
\alpha\sqrt{2kE_*}
}{
2\ell_0
}
\|\nabla_z\varrho\|
```

を得る。従ってR214がsourceに要求するbackreaction情報は、source固有のport susceptibility $\|\nabla_z\varrho\|$ へ分離できる。

### AC.7.1 current M37 load specialization

current M67 coherent profileでは

```math
\varrho_X
=
\frac{b^\dagger B_Xb}{N_0},
\qquad
\frac{\partial\varrho_X}{\partial b^*}
=
\frac{B_Xb}{N_0}.
```

$\|b\|=O(\sqrt{N_0})$ のprepared tubeではgeneric load boundから

```math
\|G_{\rm db}\|
=
O(N_0^{-1/2})
```

を回収する。さらに

```math
H_{\rm db}[e^{i\theta}b]
=
H_{\rm db}[b]
```

なのでcommon carrier phase/actionを直接吸収しない。fixed finite-time trajectory-level

```math
q_{\rm load}^{\rm db}(T)
=
O(N_0^{-1})
```

はR214本体の一般仮定ではなく、R210AのDuhamel/bootstrap theoremをこのloadへ特殊化して得る。

### AC.7.2 port-stabilityからscore/drift-stability

二つのnonnegative scalar ports $\varrho,\varrho^\circ$ に対し

```math
\widetilde\varrho
=
\varrho+\varrho_T,
\qquad
\widetilde\varrho^\circ
=
\varrho^\circ+\varrho_T
\ge
\varrho_T>0
```

とする。$\delta\varrho=\varrho-\varrho^\circ$ と置けば厳密に

```math
\nabla\log\widetilde\varrho
-
\nabla\log\widetilde\varrho^\circ
=
\frac{\nabla\delta\varrho}{\widetilde\varrho}
-
\frac{
\delta\varrho\,\nabla\varrho^\circ
}{
\widetilde\varrho
\widetilde\varrho^\circ
}.
```

従って

```math
\left\|
\nabla\log\widetilde\varrho
-
\nabla\log\widetilde\varrho^\circ
\right\|_\infty
\le
\frac1{\varrho_T}
\|\nabla\delta\varrho\|_\infty
+
\frac{
\|\nabla\varrho^\circ\|_\infty
}{
\varrho_T^2
}
\|\delta\varrho\|_\infty.
```

generic target driftを

```math
b[\varrho,U]
=
U
+
\nu\nabla\log(\varrho+\varrho_T),
\qquad
\nu=\frac{k_BT}{\gamma_X}
```

とすれば、

```math
\|b[\varrho,U]-b[\varrho^\circ,U^\circ]\|_\infty
\le
\|U-U^\circ\|_\infty
+
\nu C_{\rm score}
\|\varrho-\varrho^\circ\|_{C^1},
```

```math
C_{\rm score}
=
\frac1{\varrho_T}
+
\frac{
\|\nabla\varrho^\circ\|_\infty
}{
\varrho_T^2
}.
```

この補題によりsource-specificなtrajectory stabilityは $\|\varrho-\varrho^\circ\|_{C^1}$ と $\|U-U^\circ\|_\infty$ の評価だけをR214へ渡せばよい。

## AC.8 R214B：finite-bath dumbbellのgeneric density/flow-port縮約

generic target ports $\varrho(x,t)\ge0$、$U(x,t)$ に対し

```math
\widetilde\varrho
=
\varrho+\varrho_T,
```

```math
b_{\rm port}(x,t)
=
U(x,t)
+
\nu\partial_x\log\widetilde\varrho(x,t),
\qquad
\nu=\frac{k_BT}{\gamma_X}
```

と定める。$b_{\rm port}$ は固定有限時間上で一様bound $B_*$ と空間Lipschitz定数 $L_b$ を持つとする。

finite bathとfast dumbbellをMarkov化した後の重心を $(X_t^M,V_t^M)$ とし、有限相関GLEからのwhite-noise極限をStratonovich表示で

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
b_{\rm port}(X_t^M,t)
-
e_{214}(X_t^M,t)
\right]dt
+
\sqrt{2\gamma_Xk_BT}\circ dW_t
+
\delta F_t^{\rm db}dt
```

と書く。$\gamma_X$ はrequired leading sectorでは定数なので、ここでのStratonovich--Itô補正は0である。

$e_{214}$ はflow-port residual、R214Aのshell/core mean-force residual、fast-dumbbell tracking residual、AC.7.2から渡るsource-port stability residualを一度ずつ含む決定論的drift mismatchとし、

```math
\Delta_{214}^{\rm drift}
:=
\|e_{214}\|_\infty.
```

source-specific port contributionは

```math
\Delta_{\rm port}
\le
\varepsilon_U
+
\nu C_{\rm score}\varepsilon_\varrho,
```

```math
\varepsilon_\varrho
=
\sup_{t\le T}
\|\varrho_t-\varrho_t^\circ\|_{C^1},
\qquad
\varepsilon_U
=
\sup_{t\le T}
\|U_t-U_t^\circ\|_\infty
```

として分離する。$\delta F_t^{\rm db}$ はAC.6の中心化内部forceである。

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
b_{\rm port}(X_t^M,t)
+
e_{214}(X_t^M,t)
\right]dt
+
\sqrt{2\nu}\circ dW_t.
```

同じBrownian motionでreference port diffusion

```math
dX_t^{\rm port}
=
b_{\rm port}(X_t^{\rm port},t)dt
+
\sqrt{2\nu}\circ dW_t
```

を駆動する。noiseは加法的なので以下のcoupling評価はItô表示へ移しても同一である。velocityをMaxwell preparationすれば、

```math
\sup_{t\le T}
W_1
\left(
\mathcal L(X_t^M),
\mathcal L(X_t^{\rm port})
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
R_{\rm db}^{W_1}(T).
```

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
**定理（R214B：finite-bath dumbbellのgeneric density/flow-port動的osmotic縮約）**

R214Aのsafe sector、AC.7.2のport-stability条件、R209Bのgeneric finite harmonic bath / Markov--FDT条件を仮定する。さらに

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

を満たすとする。このときfinite-bath dumbbell tracerとreference port diffusionについて

```math
\sup_{t\le T}
W_1
\left(
\mathcal L(X_t^{\rm db}),
\mathcal L(X_t^{\rm port})
\right)
\le
\varepsilon_{214}^{\rm port}(T),
```

```math
\varepsilon_{214}^{\rm port}(T)
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

を得る。$\Delta_{214}^{\rm drift}$ にはshell/core、flow-port、tracking、source-port stabilityの各偏差を一度だけ含める。source-specific model自身のbaseline errorは含めない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R214B）**

R209Bをdumbbell内部座標へ特殊化してfinite translated harmonic bathを消去し、short-memoryとsmall internal massでAC.5の三次元Brownian dumbbellを得る。有限相関極限はCartesian Stratonovich lawで取り、noise amplitudeが一定なのでItô表示へ変換してもdrift補正はない。半径表示では幾何学drift $2D_r/r$ が生じ、R214Aの $r^2$ canonical measureを回収する。AC.6の一方向contractivityによりmoving $\ell_t$ へのtracking residualを $\Delta_{214}^{\rm drift}$ へ入れる。

重心small-mass極では $Y=X+\epsilon_MV$ を使うと上のSDEが厳密に得られる。同じBrownian motionでreference port過程を駆動し、$X=Y-\epsilon_MV$、drift Lipschitz性、Maxwell preparationの
$\epsilon_M\sup_{t\le T}\mathbb E|V_t|
=
O(\epsilon_MB_*)+O(\sqrt{\nu\epsilon_M})$
を使ってGronwall評価する。中心化dumbbell forceの積分はAC.6のabsolute covariance積分で二乗平均評価し、追加Green--Kubo dragは $\varepsilon_{\rm fr}$ で別に抑える。source-specific port差はAC.7.2のscore/drift stability boundだけを通じて合成する。R209Cは用いない。証明終。
<!-- theorem-end:proof -->

### AC.8.1 current M37/M64 specialization

current Q3-2では

```math
\varrho_X
=
\frac1{N_0}
\sum_i\chi_i(X)
\frac{Q_i^2+P_i^2}{2\mathcal J_0},
\qquad
U=U_X^{64}
```

を選ぶ。R210AがM37 coherent sourceのload-only trajectory stabilityを、R209AがM67 flowとcanonical M64 flowのcompatibilityを供給するので、AC.7.2の $\varepsilon_\varrho,\varepsilon_U$ をcurrent profile固有誤差で抑えられる。この特殊化では

```math
b_{\rm port}
=
U_X^{64}
+
\nu\partial_X
\log(\varrho+\varrho_T)
=
b_{64}^{\rm db}
```

となり、

```math
\varepsilon_{214}^{\rm port}
\longrightarrow
\varepsilon_{214\to64}.
```

従って従来のrequired bridge

```math
W_1
\left(
\mathcal L(X_t^{67,{\rm db}}),
\widetilde\rho(t)
\right)
\le
\varepsilon_{214\to64}(T)
+
\varepsilon_{\rm red}^{64}(T)
```

をR203Cとの三角不等式で回収する。$\partial_t\widetilde\rho+\partial_XJ=0$ なので、R161/R185の既存regularized lawへそのまま接続する。

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

draft-145でR214A--R214Bをcontinuous Q3-2のrequired主線へ昇格し、draft-146で旧continuous phase-volume bridgeを退役した。draft-149では結果IDとrequired状態を維持したまま、R214A/B本体をgeneric density/flow port theoremへ一般化する。

- R214Aはsource固有の密度辞書を仮定せず、nonnegative scalar portからphase-volume free energy、osmotic mean force、reciprocal mean forceを回収する。
- R214Bはgeneric $b_{\rm port}=U+\nu\nabla\log(\varrho+\varrho_T)$ に対するfinite-bath / fast-dumbbell / small-mass $W_1$ bridgeを閉じる。
- source固有のstabilityは $\varepsilon_\varrho,\varepsilon_U$ としてinterfaceへ渡し、R214本体ではその起源を仮定しない。
- current M37/M64 specializationではR210Aがcoherent load stability、R209Aがflow compatibilityを供給し、従来の $\varepsilon_{214\to64}$ を回収する。
- R209Bはgeneric finite-bath/FDT補題としてR214B内部から使う。
- 旧R208B/R208C/R209Cはactive resultから退役したままとし、結果IDを再利用しない。
- R208Dはprofile-dispatch bridgeとしてactive維持する。
- finite-graph Q3-4A/Q3-4B/Q3-5へR214を流用しない。
- Q3-2 fixed-goal、Q3-2-A1/A2、M37/R86、M64/R203、R161/R185の運用状態を変更しない。
- R215、Fisher information/free energy、M68、Schrödinger再導出は本draftに含めない。
