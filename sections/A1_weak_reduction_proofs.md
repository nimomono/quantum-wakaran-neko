@number: A1
@chapter: 付録
@title: 有限セル正準変換と弱縮約評価の詳細
@status: 第2章と第3章の正準変換、固定作用最小化、縮約作用の変分、射影的代表場、有限時間安定性、弱密度同期を補足する。

## A.1 極座標正準変換

各セルで

```math
\boldsymbol\Phi
=
r e_r,
\qquad
e_r
=
\begin{pmatrix}
\cos\theta\\
\sin\theta
\end{pmatrix},
\qquad
e_\theta
=
\begin{pmatrix}
-\sin\theta\\
\cos\theta
\end{pmatrix}.
```

運動量を

```math
\boldsymbol\Pi
=
p_r e_r
+
\frac jr e_\theta
```

と分解する。すると

```math
d\boldsymbol\Phi
=
e_r\,dr
+
r e_\theta\,d\theta
```

なので、

```math
\boldsymbol\Pi\cdot d\boldsymbol\Phi
=
p_r\,dr
+
j\,d\theta.
```

従ってシンプレクティック2形式も

```math
d\boldsymbol\Pi\wedge d\boldsymbol\Phi
=
dp_r\wedge dr
+
dj\wedge d\theta
```

となる。$r=0$ では極座標が特異であるため、この変換を使う領域は $r>0$ に限定する。

## A.2 固定作用最小化の Lagrange 乗数表示

固定振幅 $(r_i)$ の下で

```math
E_{\rm rot}
=
\sum_i
\frac{j_i^2}{2Ir_i^2}
\Delta V
```

を、制約

```math
\sum_i j_i\Delta V
=
\mathcal J_\phi
```

の下で最小化する。Lagrange 乗数を $\Lambda$ とすると、

```math
\frac{\partial}{\partial j_i}
\left[
E_{\rm rot}
-
\Lambda
\sum_kj_k\Delta V
\right]
=
\left(
\frac{j_i}{Ir_i^2}
-
\Lambda
\right)
\Delta V
=
0.
```

従って

```math
j_i
=
I\Lambda r_i^2.
```

規格化 $\sum_i r_i^2\Delta V=1$ と全作用制約から

```math
I\Lambda
=
\mathcal J_\phi.
```

よって $j_i=\mathcal J_\phi r_i^2$ を得る。Hessian は対角で

```math
\frac{\partial^2E_{\rm rot}}{\partial j_i\partial j_k}
=
\frac{\Delta V}{Ir_i^2}
\delta_{ik}
```

であり、$I>0$ と $r_i>0$ の下で正定値である。

## A.3 連続極限と節正則化

連続表示の回転エネルギーは

```math
E_{\rm rot}
=
\int
\frac{j^2}{2Ir^2}
\,dx.
```

$r=0$ では特異なので、有限正則化では

```math
E_{\rm rot}^{(\varepsilon)}
=
\int
\frac{j^2}{2I(r^2+\varepsilon^2)}
\,dx
```

を使える。しかし、この正則化では最小配置が厳密な $j=\mathcal J_\phi r^2$ からずれる。接続だけを正則化して回転エネルギーの特異性を放置してはならない。

節から離れた領域

```math
r^2
\geq
c_{\rm node}
>
0
```

では、

```math
\left|
\frac{r^2}{r^2+\varepsilon^2}
-
1
\right|
\leq
\frac{\varepsilon^2}{c_{\rm node}}
```

なので、接続誤差は一様に制御できる。節を含む極限は別問題である。

## A.4 位相接続の内部回転不変性

共通内部回転

```math
\boldsymbol\Phi
\mapsto
R(\alpha)\boldsymbol\Phi
```

の下で、行列式型の分子

```math
\Phi_1\nabla\Phi_2
-
\Phi_2\nabla\Phi_1
```

と分母 $|\boldsymbol\Phi|^2+\varepsilon^2$ は不変である。従って $\mathbf a_\varepsilon$ も不変である。

$\mathcal J_\phi$ はこの回転の生成子なので、全 Hamiltonian が共通回転不変なら Noether 量として保存される。固定 $\mathcal J_\phi$ sectorへの制限は、保存量の値を選ぶことであり、Hamiltonianへ外部パラメータを追加することではない。

## A.5 粒子 Legendre 変換

```math
H_{\rm p}
=
\frac{
|P-\mathcal J_\phi\mathbf a|^2
}{
2m
}
+
V
```

から

```math
\dot X
=
\frac{
P-\mathcal J_\phi\mathbf a
}{
m
}
```

を得る。従って $P=m\dot X+\mathcal J_\phi\mathbf a$ であり、

```math
P\cdot\dot X
-
H_{\rm p}
=
\frac m2|\dot X|^2
+
\mathcal J_\phi\mathbf a\cdot\dot X
-
V.
```

接続項の符号は正である。$S=-\mathcal J_\phi\theta$ と定めることで、縮約作用の位相項は $-\rho(\partial_tS+v\cdot\nabla S)$ となる。

## A.6 縮約作用の変分

作用密度を

```math
\mathcal L
=
\frac m2\rho|v|^2
-
\rho V
-
\rho\partial_tS
-
\rho v\cdot\nabla S
-
\kappa
\left|
\nabla\sqrt\rho
\right|^2
```

とする。

$S$ 変分では、

```math
\delta_S\mathcal A
=
\int
\left[
-\rho\partial_t\delta S
-
\rho v\cdot\nabla\delta S
\right]
\,dx\,dt
```

を部分積分し、

```math
\partial_t\rho
+
\nabla\cdot(\rho v)
=
0
```

を得る。

$v$ 変分では、

```math
\delta_v\mathcal A
=
\int
\rho
\left(
mv-\nabla S
\right)
\cdot\delta v
\,dx\,dt,
```

従って $mv=\nabla S$ である。

$q=\sqrt\rho$ と置くと、

```math
\delta
\left[
-
\kappa
\int
|\nabla q|^2
\,dx
\right]
=
2\kappa
\int
\delta q\,\Delta q
\,dx.
```

$\delta\rho=2q\delta q$ から、$\rho$ に関する汎関数微分は

```math
\kappa
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
```

この符号を使うと Hamilton--Jacobi 式の量子ポテンシャルは

```math
-\kappa
\frac{\Delta\sqrt\rho}{\sqrt\rho}
```

となる。

## A.7 同期差保存の仮定

位相変分から

```math
\partial_tj
+
\mathcal J_\phi
\nabla\cdot(\rho v)
=
0
```

を得るため、残余場 Hamiltonian $H_{\rm residual}$ に必要な条件は

```math
\frac{
\delta H_{\rm residual}
}{
\delta\theta
}
=
0
```

である。共通位相の定数回転に対する不変性だけではこの条件に足りない。$r^2|\nabla\theta|^2$ の独立な場エネルギーを残すと、位相流束が追加される。

従って第3章の理想同期差保存は、位相勾配エネルギーを粒子流速の運動エネルギーへ吸収し、残差を $\varepsilon_{\rm cross}$ または $\varepsilon_{\rm press}$ へ含めた縮約に限定される。この非重複条件では、付録Fの位相 Hessian $B$ が半正定値または零になり得るため、正定値2帯定理を直接適用できない。

## A.8 変分縮約の限界

ミクロ作用を多様体へ制限してから変分する操作と、ミクロ方程式を解いてから粗視化する操作は一般に交換しない。必要なのは、少なくとも次のいずれかである。

1. 縮約多様体が近似不変であり、法線方向残差が小さい。
2. 高速法線モードを断熱消去し、有効作用の誤差を評価できる。
3. 弱開放縮約が法線方向だけを安定化し、接方向の Hamiltonian 構造を保つ。

付録Fは、正定値定数係数2次模型について2と3の一部を具体化し、高速法線成分を同型補助系へ移した後の局所縮約残差を $O(\epsilon_{\rm s})$ に抑える。ただし、現行作用に必要な半正定値位相 Hessian、粒子-場混合、時間依存射影、非線形再励起を含む一様誤差定理は与えない。

## A.9 射影的代表場

複素 Hilbert 空間 $\mathcal Q$ の単位球面上で、共通位相を同一視した距離を

```math
d_{\rm pr}
\left(
u,v
\right)
=
\inf_{
\alpha\in
\left[
0,2\pi
\right)
}
\left\|
u-e^{i\alpha}v
\right\|_{\mathcal E_V}
```

とする。基準場 $v_0$ と各標本の重なりが零でなければ、

```math
\left\langle
v_0,
e^{-i\alpha_\omega}u^\omega
\right\rangle
>
0
```

となる位相 $\alpha_\omega$ を局所的かつ連続に選べる。位相整合平均を

```math
m
=
\mathbb E_\omega
\left[
e^{-i\alpha_\omega}
u^\omega
\right]
```

とする。$\|m\|_{L^2}>0$ なら、

```math
\bar u
=
\frac{
m
}{
\left\|
m
\right\|_{L^2}
}
```

を代表場にできる。分散が十分小さい範囲では、基準場の取り方を小さく変えても代表射影点の差は分散と同じ次数である。

各時刻で無関係に $\alpha_\omega$ を選ぶと時間微分が定まらない。初期位相から連続に追跡し、

```math
\left\langle
\bar u,
\partial_t\bar u
\right\rangle
\in
i\mathbb R
```

を許す。この純虚成分が第3章の実数共通位相項 $\lambda(t)$ に対応する。

## A.10 共通線形発展に対する有限時間安定性

$U(t,s)$ を $H_V(t)$ が生成する発展作用素とし、

```math
\left\|
U(t,s)
\right\|_{
\mathcal E_V
\to
\mathcal E_V
}
\leq
C_T
```

を $0\leq s\leq t\leq T$ で仮定する。位相整合した2標本 $u^\omega$、$u^{\omega'}$ が

```math
i\hbar_{\rm eff}
\partial_tu^\omega
=
H_V(t)u^\omega
+
R^\omega
```

を満たすなら、Duhamel 公式から

```math
\begin{aligned}
u^\omega(t)-u^{\omega'}(t)
={}&
U(t,0)
\left[
u^\omega(0)-u^{\omega'}(0)
\right]
\\
&
-
\frac i{
\hbar_{\rm eff}
}
\int_0^t
U(t,s)
\left[
R^\omega(s)-R^{\omega'}(s)
\right]
\,ds.
\end{aligned}
```

従って

```math
\begin{aligned}
&
\left\|
u^\omega(t)-u^{\omega'}(t)
\right\|_{\mathcal E_V}
\\
&\qquad
\leq
C_T
\left\|
u^\omega(0)-u^{\omega'}(0)
\right\|_{\mathcal E_V}
+
\frac{
C_T
}{
\hbar_{\rm eff}
}
\int_0^t
\left[
\left\|
R^\omega(s)
\right\|_{\mathcal E_V}
+
\left\|
R^{\omega'}(s)
\right\|_{\mathcal E_V}
\right]
\,ds.
\end{aligned}
```

標本対について2乗平均を取り、Minkowski 不等式を使えば、第3章のコヒーレント分散評価を得る。ここでは残差のエネルギーノルム上界が必要であり、$\mathcal Q^*$ 上界だけでは足りない。

代表場の弱方程式は位相整合平均 $m$ を微分して得る。$\|m(t)\|_{L^2}\geq c_m>0$ を仮定すると、$\bar u=m/\|m\|_{L^2}$ の微分に現れる規格化項も平均残差の $\mathcal Q^*$ ノルムで評価できる。規格化後の全強制項は単位球面の接空間に入り、その $i\bar u$ 方向を実数共通位相項 $\lambda(t)\bar u$、残りを $R_{\rm red}$ と分ける。従って双対残差の上界は定数 $C_T$ に $c_m^{-1}$ を含む。規格化項だけを実数位相項と同一視しない。

この評価が使えるのは、各標本に対する共通線形主部と残差表示が既に得られた後である。ミクロ Hamiltonian から $R^\omega$ を小さくする部分を置き換えない。

## A.11 強度と場流束の積評価

$u,v\in H^1$ とする。点ごとの恒等式

```math
\left|
u
\right|^2
-
\left|
v
\right|^2
=
\left(
u-v
\right)^*u
+
v^*
\left(
u-v
\right)
```

から、

```math
\left\|
\left|
u
\right|^2
-
\left|
v
\right|^2
\right\|_{L^1}
\leq
\left(
\left\|
u
\right\|_{L^2}
+
\left\|
v
\right\|_{L^2}
\right)
\left\|
u-v
\right\|_{L^2}
```

を得る。

場流束の差は

```math
u^*\nabla u
-
v^*\nabla v
=
\left(
u-v
\right)^*
\nabla u
+
v^*
\nabla
\left(
u-v
\right)
```

なので、

```math
\begin{aligned}
\left\|
\operatorname{Im}
\left(
u^*\nabla u
-
v^*\nabla v
\right)
\right\|_{L^1}
\leq{}&
\left\|
u-v
\right\|_{L^2}
\left\|
\nabla u
\right\|_{L^2}
\\
&
+
\left\|
v
\right\|_{L^2}
\left\|
\nabla
\left(
u-v
\right)
\right\|_{L^2}.
\end{aligned}
```

一様 $H^1$ 上界の下で、エネルギーノルム集中は強度と場流束の $L^1$ 集中を与える。

## A.12 弱密度差評価

差の連続の式を

```math
\partial_t
\delta\rho
+
\nabla
\cdot
\delta\boldsymbol J
=
R_{\rm cont}
```

とする。時間積分すると、

```math
\delta\rho(t)
=
\delta\rho(0)
-
\int_0^t
\nabla
\cdot
\delta\boldsymbol J(s)
\,ds
+
\int_0^t
R_{\rm cont}(s)
\,ds.
```

発散作用素の有界性

```math
\left\|
\nabla
\cdot
\boldsymbol F
\right\|_{H^{-1}}
\leq
\left\|
\boldsymbol F
\right\|_{L^2}
```

を用いれば、

```math
\left\|
\delta\rho(t)
\right\|_{H^{-1}}
\leq
\left\|
\delta\rho(0)
\right\|_{H^{-1}}
+
\int_0^t
\left\|
\delta\boldsymbol J(s)
\right\|_{L^2}
\,ds
+
\int_0^t
\left\|
R_{\rm cont}(s)
\right\|_{H^{-1}}
\,ds.
```

これは流束差を入力とした密度差評価であり、流束差自体の発展方程式ではない。

## A.13 節を含む弱形式と接続極限

$\psi\in L^2(0,T;\mathcal Q)$、$\partial_t\psi\in L^1(0,T;\mathcal Q^*)$ なら、Schrödinger 型方程式は節集合を除外せず弱形式で定義できる。運動エネルギーは

```math
\frac{
\hbar_{\rm eff}^2
}{
2m
}
\int
\left|
\nabla\psi
\right|^2
\,dx
```

として有限であり、$\Delta\sqrt q/\sqrt q$ を節上で点ごとに評価する必要はない。

一方、ミクロ接続項には

```math
\rho
\frac{
\operatorname{Im}
\left(
\zeta^*
\nabla\zeta
\right)
}{
\left|
\zeta
\right|^2
+
\varepsilon^2
}
```

が現れる。$\rho=|\zeta|^2$ が厳密なら分母との相殺を使えるが、$\rho-|\zeta|^2$ が $H^{-1}$ または $L^1$ で小さいだけでは、節近傍の積を一様に抑えられない。必要なのは、例えば

```math
\int_0^T
\int
\frac{
\left|
\rho
-
\left|
\zeta
\right|^2
\right|
}{
\left|
\zeta
\right|^2
+
\varepsilon^2
}
\left|
\operatorname{Im}
\left(
\zeta^*
\nabla\zeta
\right)
\right|
\,dx\,dt
\longrightarrow
0
```

のような重み付き評価である。本稿はこの極限を仮定した弱残差へ含め、現行 M0 からの導出済み結果とはしない。
