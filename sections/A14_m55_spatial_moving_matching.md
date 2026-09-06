@number: N
@chapter: 付録
@title: M55粒子--signal bath共同測度とmoving matching
@status: M42/R172--R174を退役し、Q1・Q2と同じ単一試行signal、R135のrank-one支持、R164の条件付き作用容量をQ3の全時刻moving matchingへ拡張する。R183の不変性、R184のM37・finite collision実装、R185の同一母測度時間反転と時間対称Newton則を証明する。

## N.1 M55の状態と因果規約

有限グラフ $G=(V,E)$ 上で1試行の状態を

```math
\Gamma_t
=
(Q(t),P(t),X_t,C_t,H_t,\tau_t,S_{\rm ref})
```

とする。$Q_i,P_i$ は実正準signal自由度、$X_t\in V$ は1個の実在粒子位置、$C_t$ はfinite collision cell、$H_t$ は履歴、$\tau_t$ はclockである。

```math
Z_i
=
\frac{Q_i+iP_i}{\sqrt{2\mathcal J_0}}
```

は派生複素表示であり、独立した複素場ではない。試行集団は $\mu_t(dX\,dZ)$ で記述し、

```math
C_Z(t)
=
\frac{\mathbb E[Z_tZ_t^\dagger]}
{\mathbb E[Z_t^\dagger Z_t]}
```

は集団統計に留める。$C_Z=cc^\dagger$ ならR135により $Z=\alpha c$ がほとんど確実に成り立つが、controllerは $c$、$C_Z$、全位置分布を入力しない。

## N.2 厳密signal sectorとR164型moving target

Hermitian $h=A+iB$、$A^{\mathsf T}=A$、$B^{\mathsf T}=-B$ に対する

```math
H_{\rm sig}
=
\frac{Q^{\mathsf T}AQ+P^{\mathsf T}AP}{2\mathcal J_0}
+
\frac{P^{\mathsf T}BQ}{\mathcal J_0}
```

は厳密に

```math
i\mathcal J_0\dot Z=hZ
```

を与え、$S=Z^\dagger Z$ を保存する。

$q_i>0$、$\sum_iq_i=1$、$\delta>0$ とし、

```math
R_i^\delta
=
|Z_i|^2+\delta q_iS,
\qquad
\pi_i^\delta
=
\frac{R_i^\delta}{(1+\delta)S}
```

とする。これはR164の $A_i^\delta/\mathcal J_0$ と同じ条件付き容量である。局所辺流と対称trafficを

```math
J_{i\to j}
=
\frac{2}{\mathcal J_0}
\operatorname{Im}
\left(
Z_j^*h_{ji}Z_i
\right),
```

```math
T_{ij}^\delta
=
\frac{|h_{ij}|}{\mathcal J_0}
(R_i^\delta+R_j^\delta)
```

と定める。$2|Z_i||Z_j|\leq|Z_i|^2+|Z_j|^2$ から

```math
|J_{i\to j}|
\leq
T_{ij}^\delta
```

である。

## N.3 R183の完全証明

前向きrateを

```math
k^+_{i\to j}
=
\frac{T_{ij}^\delta+J_{i\to j}}{2R_i^\delta}
```

とする。

<!-- theorem-start:theorem -->
**定理（R183：粒子--signal bath共同測度のmoving matching不変性）**

有限グラフ、時間連続な有界Hermitian生成子、$\delta>0$、上のM55 rateを仮定する。初期共同測度が

```math
\mu_0(X=i\mid Z=z)=\pi_i^\delta(z)
```

を満たせば、全有限時刻で

```math
\mu_t(X=i\mid Z=z)=\pi_i^\delta(z)
```

が成り立つ。rank-one signal集団 $C_Z(t)=\psi_t\psi_t^\dagger$ では

```math
P(X_t=i)
=
\frac{|\psi_i(t)|^2+\delta q_i}{1+\delta},
```

```math
D_{\rm TV}
\left(
P(X_t\in\cdot),|\psi_t|^2
\right)
\leq
\frac{\delta}{1+\delta}.
```

matching不変性自体にはrank-one仮定を要しない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R183）**

$R_i^\delta\geq\delta q_{\min}S>0$ と $T_{ij}^\delta\geq|J_{i\to j}|$ からrateは有限かつ非負である。$S$ は保存され、

```math
\frac{d}{dt}|Z_i|^2
=
\sum_jJ_{j\to i}
```

なので

```math
\dot\pi_i^\delta
=
\frac{1}{(1+\delta)S}
\sum_jJ_{j\to i}.
```

一方、

```math
\pi_i^\delta k^+_{i\to j}
-
\pi_j^\delta k^+_{j\to i}
=
\frac{J_{i\to j}}{(1+\delta)S}.
```

従って $\pi^\delta$ は位置master方程式を満たし、有限状態方程式の一意性により全時刻matchingが従う。

rank oneならR135の支持節から $Z=\alpha\psi$ がほとんど確実である。$\pi^\delta(\alpha\psi)=\pi^\delta(\psi)$ を周辺化すれば表示式を得る。証明終。
<!-- theorem-end:proof -->

## N.4 finite collision実装

$\delta>0$ では固定有限グラフ上のrateは有界である。時間を有限窓へ分けてrateを凍結し、辺と窓ごとに正逆rate以上の試行率を選ぶ。方向タグを持つcellの物理閾値 $u_n\in(0,1)$ が

```math
u_n
<
\frac{k^+_{i\to j}}{\nu_{e,m}}
```

なら通過、それ以外は反射させる。source、target、窓、cell番号、未消去の閾値を履歴へ保持し、エネルギー差はwork registerへ移す。有限有理分割と滑らかなHamiltonian shearで固定有限時間の駆動Hamiltonian散乱列へ任意精度近似できる。overflowと各有限近似失敗は無反応へ残す。

旧R173の一般有向rate用collision構成を再利用するが、旧 $(\rho,\sigma)$ node正則化は使わない。R164と共通の $\delta$ が $R_i^\delta\geq\delta q_iS$ を与える。

## N.5 R184の完全評価

M37局所包絡を $b(t)$、理想M55信号を $b_L(t)$ とし、開始面で $S_{\rm ref}=\|b(0)\|^2$ をlatchする。$\Delta=\delta_{\rm loc}(\eta)<1$ とする。規格化信号 $x=b/\sqrt{S_{\rm ref}}$、$y=b_L/\sqrt{S_{\rm ref}}$ は

```math
\|x-y\|
\leq
\frac{\varepsilon_{\rm car}(T)}{1-\Delta},
\qquad
\|x\|
\leq
\frac{1+\Delta}{1-\Delta},
\qquad
\|y\|=1.
```

$r_i(x)=|x_i|^2+\delta q_i$ と置けば

```math
|r_i(x)-r_i(y)|
\leq
(R_\eta+1)|x_i-y_i|,
\qquad
R_\eta=\frac{1+\Delta}{1-\Delta}.
```

traffic差とcurrent差は

```math
|t_{ij}(x)-t_{ij}(y)|
\leq
\frac{|h_{ij}|}{\mathcal J_0}
\sqrt2(R_\eta+1)\|x-y\|,
```

```math
|j_{ij}(x)-j_{ij}(y)|
\leq
\frac{2|h_{ij}|}{\mathcal J_0}
\sqrt{R_\eta^2+1}\|x-y\|.
```

$r_i\geq\delta q_{\min}$ を商へ使うと

```math
\max_i\sum_{j\ne i}
|k^+_{i\to j}(x)-k^+_{i\to j}(y)|
\leq
L_\delta(\eta)\varepsilon_{\rm car}(T)
```

で、

```math
L_\delta(\eta)
=
\frac{h_1}
{\mathcal J_0(1-\Delta)^2}
\left[
\frac{\sqrt2(1+\sqrt{1+\Delta^2})}{\delta q_{\min}}
+
\frac{2(1+\delta)}{\delta^2q_{\min}^2}
\right].
```

<!-- theorem-start:theorem -->
**定理（R184：M55 moving matchingのM37・finite collision実装）**

R86の仮定に加えて $\Delta<1$、$\delta>0$ とする。同じ初期位置分布から開始した理想M55過程とM37 rate過程は

```math
\sup_{0\leq t\leq T}
D_{\rm TV}
\left(
P(X_t^{37}\in\cdot),
P(X_t^L\in\cdot)
\right)
\leq
T L_\delta(\eta)\varepsilon_{\rm car}(T)
```

を満たす。finite collision、時間凍結、overflow、clock、記録を加えた完全結果誤差を

```math
\varepsilon_{184}
=
\varepsilon_{\rm init}
+
T L_\delta\varepsilon_{\rm car}
+
\varepsilon_{\rm step}
+
\varepsilon_{\rm coll}
+
\varepsilon_{\rm over}
+
\varepsilon_{\rm clk}
+
\varepsilon_{\rm rec}
```

とできる。厳密な $|\psi|^2$ と比較するときだけ $\delta/(1+\delta)$ を別項として加える。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R184）**

上のrate差評価を各時刻に適用する。有限Markov生成子のDuhamel公式と全変動距離の収縮性から、位置分布差はrate行差の時間積分以下である。finite collision近似の各失敗を完全結果集合の無反応成分へ残し、三角不等式で加える。証明終。
<!-- theorem-end:proof -->

## N.6 同一母測度の時間反転

R183の共同path measureを固定する。$p_i(t)=P(X_t=i\mid Z_t)$ は $\delta>0$ で正である。同じpath measureのBayes反転から

```math
k^-_{i\to j}
=
\frac{p_jk^+_{j\to i}}{p_i}
=
\frac{T_{ij}^\delta-J_{i\to j}}{2R_i^\delta}
```

を得る。別の未来bath、後向きcontroller、未来境界条件を物理入力として追加しない。

```math
D_+f_i
=
\partial_tf_i
+
\sum_jk^+_{i\to j}(f_j-f_i),
```

```math
D_-f_i
=
\partial_tf_i
+
\sum_jk^-_{i\to j}(f_i-f_j)
```

と定める。

## N.7 有限格子の前後速度

1次元最近接格子 $x_i=ia$ と

```math
h_{i,i+1}
=
-\frac{\mathcal J_0\nu}{a^2},
\qquad
\mathcal J_0=2m\nu
```

を考える。規格化辺流 $j_{i+1/2}=J_{i\to i+1}/[(1+\delta)S]$ に対し

```math
v_i^{(a,\delta)}
=
\frac{a}{2p_i}
(j_{i+1/2}+j_{i-1/2}),
```

```math
u_i^{(a,\delta)}
=
\frac{\nu}{2ap_i}
(p_{i+1}-p_{i-1})
```

と置くと有限格子上で厳密に

```math
D_+X=v^{(a,\delta)}+u^{(a,\delta)},
\qquad
D_-X=v^{(a,\delta)}-u^{(a,\delta)}
```

である。

Q3のR185では一様背景 $q_i=1/N$ を採用する。$\psi=\sqrt\rho e^{iS/\mathcal J_0}$、

```math
v=\frac{\partial_xS}{m},
\qquad
u=\nu\partial_x\log\rho
```

とし、

```math
A=\frac{\rho}{\rho+\delta q_0},
\qquad
\epsilon=1-A
```

と置くと

```math
v_\delta=Av,
\qquad
u_\delta=Au
```

であり、十分滑らかなnode-free領域で $v^{(a,\delta)}=v_\delta+O(a^2)$、$u^{(a,\delta)}=u_\delta+O(a^2)$ である。

## N.8 R185の時間対称Newton則

```math
a_{N,\delta}
=
\frac12(D_+D_-+D_-D_+)X
```

とする。理想M55の実正準signal Hamiltonianが

```math
i\mathcal J_0\partial_t\psi
=
\left[
-\frac{\mathcal J_0^2}{2m}\partial_x^2+V
\right]\psi
```

の複素表示を持つとする。これは独立な量子公理ではなくN.2の実Hamiltonianの表示である。Madelung分解から

```math
\partial_tv+v\partial_xv-u\partial_xu-\nu\partial_x^2u
=
-\frac{\partial_xV}{m}
```

が従う。従って

```math
a_{N,\delta}
=
-\frac{\partial_xV}{m}
+
R_\delta
+
O(a^2),
```

```math
R_\delta
=
\epsilon
\left[
\frac{\partial_xV}{m}
-
2A(v\partial_xv+u\partial_xu)
-
\frac{A\epsilon}{\nu}u(v^2+u^2)
\right].
```

<!-- theorem-start:theorem -->
**定理（R185：moving matching過程の同一母測度時間反転と時間対称Newton則）**

R183を1次元一様格子へ特殊化し、$q_i=1/N$、$\delta>0$、$\mathcal J_0=2m\nu$ とする。固定有限時間のnode-free smooth sectorで $\rho\geq\rho_*>0$ を仮定する。同じ共同path measureから定まる $D_\pm$ は上の有限格子速度分解を厳密に満たし、

```math
m a_{N,\delta}
=
-\partial_xV
+
mR_\delta
+
O(ma^2).
```

$F_0=\|\partial_xV/m\|_\infty$、$V_0=\|v\|_\infty$、$V_1=\|\partial_xv\|_\infty$、$U_0=\|u\|_\infty$、$U_1=\|\partial_xu\|_\infty$、

```math
\epsilon_*
=
\frac{\delta q_0}{\rho_*+\delta q_0}
```

とすれば

```math
\|R_\delta\|_\infty
\leq
\epsilon_*
\left[
F_0
+
2(V_0V_1+U_0U_1)
+
\frac{\epsilon_*}{\nu}U_0(V_0^2+U_0^2)
\right].
```

従って正則化残差は $O(\delta)$、格子残差は $O(a^2)$ である。
<!-- theorem-end:theorem -->

R185は理想M55 signal sectorの結果である。R184の $L_\delta\varepsilon_{\rm car}$ はrateと位置分布を制御するが、$D_+D_-X$ に現れるrateの時間微分までR86の状態ノルム誤差だけから制御しない。生M37の $2\omega_0$ micromotionからNewton加速度まで直接持ち上げるにはcarrier-period粗視化または時間微分付き縮約定理が別に必要である。

## N.9 達成境界と反証条件

R183/R185によりM55の同じ共同測度から前後生成子、current速度、osmotic速度、時間対称Newton則を導いた。一方、finite collision bath近似から合成加速度までの明示誤差を閉じていないためQ3-2は部分達成とする。

反証条件は、集団統計の書戻しが不可避になること、finite collision前後生成子が有限誤差で近似できないこと、node-free sectorで $a^2$ または $\delta$ 残差が表示次数で減らないこと、Q3-4A・Q3-4B・Q3-5の正の余裕をR184誤差が上回ることである。連続空間の一様極限、多粒子、Q3-6の位相量子化は本付録の主張に含めない。