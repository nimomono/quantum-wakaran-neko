@number: A1
@chapter: 付録
@title: 有限セル正準変換と位相接続縮約の詳細
@status: 第2章と第3章の正準変換、固定作用最小化、時間反転、縮約作用の変分を有限次元表示から補足する。

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

付録Fは、正定値定数係数2次模型について2と3の一部を具体化し、高速法線成分を同型補助系へ移した後の局所縮約残差を $O(\epsilon_{\rm s})$ に抑える。ただし、現行作用に必要な半正定値位相 Hessian、粒子-場混合、時間依存射影、非線形再励起を含む一様誤差定理は与えない。第3章の定理は、制限作用内部の厳密結果として読む。
