@number: A6
@chapter: 付録
@title: 単体局所正準形、低速・高速分離、高速モード交換
@status: 厳密規格化・固定全位相作用の局所chart Hamiltonian、2つの慣性行列の逆恒等式、正定値2次模型の2帯分離、同型有限補助系への高速成分交換は、明記した条件の下で厳密結果である。半正定値位相 Hessian、有限規格化ペナルティ、時間依存基準経路、粒子-場を含む全 Hessian、非線形高速再励起は未完成である。

## F.1 厳密制約模型と有限ペナルティ模型

第2.6節の規格化量を

```math
N
=
\sum_{i=1}^{L}R_i^2
```

とする。共通内部回転の生成子

```math
\mathcal J_\phi
=
\sum_{i=1}^{L}J_i
```

は対称性から保存される。従って、固定 $\mathcal J_\phi$ は Hamiltonian 流の不変sectorである。

一方、有限ペナルティ

```math
\frac{\Lambda_N}{2}
\left(
N-1
\right)^2
```

だけでは $N$ は一般に保存されない。本付録の厳密な局所縮約では、

```math
N=1
```

をホロノミック制約として課し、正の規格化単体

```math
\Sigma_{L-1}^{\circ}
=
\left\{
q\in\mathbb R^L:
q_i>0,
\quad
\boldsymbol 1^{\mathsf T}q=1
\right\}
```

の余接束を用いる。有限 $\Lambda_N$ の模型は別の Hamiltonian 系であり、規格化方向を追加モードとして含む。両者を同じ「固定規格化sector」と呼ばない。

固定 $\mathcal J_\phi$ を課した後、共通位相を商で除く。以下の局所chartは、節 $q_i=0$ から離れた単体内点だけを覆う。

## F.2 単体と相対位相の局所座標

$n=L-1$ とし、

```math
E^{\mathsf T}E
=
I_n,
\qquad
E^{\mathsf T}\boldsymbol 1
=
0
```

を満たす $L\times n$ 行列 $E$ を固定する。単体内点 $q^*$ の近傍で、振幅偏差 $\xi\in\mathbb R^n$ と相対位相 $\varphi\in\mathbb R^n$ を

```math
q
=
q^*
+
E\xi,
qquad
\boldsymbol\theta
=
\Theta\boldsymbol 1
+
E\varphi
```

により定める。$\Theta$ は共通位相である。

位相正準項は

```math
\begin{aligned}
\mathcal J_\phi
q^{\mathsf T}
d\boldsymbol\theta
={}&
\mathcal J_\phi d\Theta
+
\mathcal J_\phi
\left(
E^{\mathsf T}q^*
+
\xi
\right)^{\mathsf T}
d\varphi.
\end{aligned}
```

$\mathcal J_\phi(E^{\mathsf T}q^*)^{\mathsf T}d\varphi$ は完全微分なので、局所運動方程式を変えずに除ける。固定 $\mathcal J_\phi$ と共通位相の商を取った後に残る磁気型1形式は

```math
\mathcal J_\phi
\xi^{\mathsf T}d\varphi
```

である。この項が、以下の最小結合型運動量シフトを作る。

## F.3 正確な局所chart Hamiltonian

```math
D_q
=
\operatorname{diag}
\left(
q_1,\ldots,q_L
\right)
```

とし、2つの正定値行列を

```math
G_q(q)
=
E^{\mathsf T}
D_q^{-1}
E,
```

```math
G_\varphi(q)
=
E^{\mathsf T}
\left(
D_q
-
qq^{\mathsf T}
\right)
E
```

と定める。第2.6節の有限 $\epsilon_{\rm s}$ Lagrangian は、このchartで正確に

```math
\begin{aligned}
L_{\epsilon_{\rm s}}^{\rm chart}
={}&
\mathcal J_\phi
\xi^{\mathsf T}\dot\varphi
-
H_0(\xi,\varphi)
\\
&+
\frac{
\epsilon_{\rm s}M
}{
8
}
\dot\xi^{\mathsf T}
G_q(q)
\dot\xi
+
\frac{
\epsilon_{\rm s}I
}{
2
}
\dot\varphi^{\mathsf T}
G_\varphi(q)
\dot\varphi
\end{aligned}
```

となる。共役運動量は

```math
p_\xi
=
\frac{
\epsilon_{\rm s}M
}{
4
}
G_q(q)
\dot\xi,
```

```math
p_\varphi
=
\mathcal J_\phi\xi
+
\epsilon_{\rm s}I
G_\varphi(q)
\dot\varphi.
```

従って、局所chart Hamiltonian は

```math
\begin{aligned}
H_{\epsilon_{\rm s}}^{\rm chart}
={}&
H_0(\xi,\varphi)
+
\frac{
2
}{
\epsilon_{\rm s}M
}
p_\xi^{\mathsf T}
G_q(q)^{-1}
p_\xi
\\
&+
\frac{
1
}{
2\epsilon_{\rm s}I
}
\left(
p_\varphi
-
\mathcal J_\phi\xi
\right)^{\mathsf T}
G_\varphi(q)^{-1}
\left(
p_\varphi
-
\mathcal J_\phi\xi
\right).
\end{aligned}
```

<!-- theorem-start:proposition -->
**命題（厳密制約下の局所chart Hamiltonian）**
$q_i>0$、$N=1$、固定 $\mathcal J_\phi$ の下で、上の Hamiltonian は第2.6節の有限特異 Hamiltonian の局所正準表示である。$\epsilon_{\rm s}\to0$ を取らず、2次化も用いていない。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
$\dot q=E\dot\xi$ を第2.6節の振幅慣性項へ代入すると $G_q$ を得る。相対位相速度から重み付き平均を除いた2次形式は

```math
\sum_i
q_i
\left(
\dot\theta_i
-
\sum_jq_j\dot\theta_j
\right)^2
=
\dot\varphi^{\mathsf T}
G_\varphi
\dot\varphi.
```

正準項から完全微分を除き、2つの運動量を Legendre 変換すればよい。
<!-- theorem-end:proof -->

## F.4 振幅・位相慣性行列の逆恒等式

<!-- theorem-start:theorem -->
**定理（単体慣性行列の逆恒等式）**
$q\in\Sigma_{L-1}^{\circ}$ では、

```math
G_q(q)^{-1}
=
G_\varphi(q)
```

が厳密に成立する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
任意の $x\in\mathbb R^n$ に対し、$v=Ex$ と置く。$\boldsymbol1^{\mathsf T}v=0$ である。さらに

```math
w
=
\left(
D_q
-
qq^{\mathsf T}
\right)
v
```

と置くと、

```math
\boldsymbol1^{\mathsf T}w
=
q^{\mathsf T}v
-
\left(
\boldsymbol1^{\mathsf T}q
\right)
q^{\mathsf T}v
=
0.
```

従って $w=Ey$ を満たす一意な $y$ があり、

```math
y
=
E^{\mathsf T}w
=
G_\varphi x.
```

一方、

```math
D_q^{-1}w
=
v
-
\boldsymbol1
\left(
q^{\mathsf T}v
\right)
```

なので、

```math
G_qy
=
E^{\mathsf T}
D_q^{-1}
Ey
=
E^{\mathsf T}v
=
x.
```

従って $G_qG_\varphi=I_n$ である。
<!-- theorem-end:proof -->

この恒等式は、振幅方向の Fisher 型計量と、相対位相方向の重み付き共分散計量が同じ単体幾何の互いに逆な表示であることを示す。ただし、密度同期または Schrödinger 型力学を単独で導く結果ではない。

## F.5 内点臨界点まわりの2次正準標準形

$H_0$ の内点臨界点を局所原点へ移し、

```math
\nabla H_0
\left(
0,0
\right)
=
0
```

とする。Hessianを

```math
K_{\xi\xi}
=
\partial_\xi^2H_0,
\qquad
K_{\xi\varphi}
=
\partial_\xi\partial_\varphi H_0,
\qquad
K_{\varphi\varphi}
=
\partial_\varphi^2H_0
```

とする。全て臨界点で評価する。

```math
G_*
=
G_\varphi(q^*)
```

を用い、線形正準変換を

```math
x
=
\frac{\sqrt M}{2}
G_*^{-1/2}
\xi,
\qquad
p_x
=
\frac{2}{\sqrt M}
G_*^{1/2}
p_\xi,
```

```math
y
=
\sqrt I
G_*^{1/2}
\varphi,
\qquad
p_y
=
\frac{1}{\sqrt I}
G_*^{-1/2}
p_\varphi
```

と定める。また、

```math
g_\phi
=
\frac{
2\mathcal J_\phi
}{
\sqrt{MI}
}
```

と置く。2次 Hamiltonian は

```math
\begin{aligned}
H_{\epsilon_{\rm s}}^{(2)}
={}&
\frac{1}{2\epsilon_{\rm s}}
\left[
p_x^{\mathsf T}p_x
+
\left(
p_y-g_\phi x
\right)^{\mathsf T}
\left(
p_y-g_\phi x
\right)
\right]
\\
&+
\frac12x^{\mathsf T}A x
+
x^{\mathsf T}C y
+
\frac12y^{\mathsf T}B y
\end{aligned}
```

となる。$A$、$B$ は実対称行列で、$C$ は一般には零でない。これらは元の Hessian を上の線形変換で移した行列である。

<!-- theorem-start:proposition -->
**命題（内点臨界点まわりの2次標準形）**
節から離れた内点臨界点の近傍で、正確なchart Hamiltonianの2次部分は上の最小結合型標準形へ正準変換できる。$G_\varphi(q)$ の位置依存性は、原点で運動量が零なら3次以上の項へ入る。
<!-- theorem-end:proposition -->

位相反転対称性

```math
H_0(\xi,\varphi)
=
H_0(\xi,-\varphi)
```

が臨界点近傍で成立し、臨界位相を $\varphi=0$ に取れるなら、

```math
C=0.
```

この対称性を仮定せずに混合 Hessian を捨ててはならない。

## F.6 正定値2次模型の2帯分離

以下では、

```math
g_\phi\neq0,
\qquad
C=0,
\qquad
A>0,
\qquad
B>0
```

を仮定する。Hamilton方程式は

```math
\epsilon_{\rm s}\ddot x
-
g_\phi\dot y
+
Ax
=
0,
```

```math
\epsilon_{\rm s}\ddot y
+
g_\phi\dot x
+
By
=
0.
```

<!-- theorem-start:theorem -->
**定理（正定値2次模型の低速・高速分離）**
上の条件の下で、十分小さい $\epsilon_{\rm s}>0$ に対し、正の固有振動数は $n$ 個の低速帯と $n$ 個の高速帯へ分かれる。低速帯は $O(1)$ で、その2乗は重複度込みで

```math
\operatorname{spec}
\left[
\frac{
A^{1/2}BA^{1/2}
}{
g_\phi^2
}
\right]
```

へ収束する。高速帯は

```math
\omega_{{\rm f},k}
=
\frac{
|g_\phi|
}{
\epsilon_{\rm s}
}
+
O(1).
```

2帯の間には $\epsilon_{\rm s}\to0$ で発散するスペクトル間隙がある。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
$e^{i\omega t}$ 型の解に対する固有値問題は

```math
\begin{pmatrix}
A-\epsilon_{\rm s}\omega^2I_n
&
-i g_\phi\omega I_n
\\
i g_\phi\omega I_n
&
B-\epsilon_{\rm s}\omega^2I_n
\end{pmatrix}
\begin{pmatrix}
x\\
y
\end{pmatrix}
=
0.
```

$A>0$ と $B>0$ により2次 Hamiltonian は正定値であるため、線形 Hamiltonian 行列の非零固有値は半単純な純虚数対になる。$\omega=O(1)$ として $\epsilon_{\rm s}=0$ を代入し、$x$ を消去すると、

```math
B y
=
g_\phi^2\omega^2
A^{-1}y.
```

これは $A^{1/2}BA^{1/2}/g_\phi^2$ の正の固有値問題であり、$n$ 個の低速極限を与える。

残る $n$ 個について $\zeta=\epsilon_{\rm s}\omega$ を固定すると、最高次の行列束は $\zeta^2=g_\phi^2$ を与える。固有値の連続性と正定値 Hamiltonian 束の慣性指数を用いると、低速根と合わせて正の根は合計 $2n$ 個であり、残りの $n$ 個は $\zeta\to|g_\phi|$ となる。従って2帯の個数と漸近式を得る。
<!-- theorem-end:proof -->

この定理は正定値2次部分模型の結果である。現行の Madelung 縮約へ無条件に適用しない。

## F.7 低速部分空間上の縮約残差

$\mathcal E_{\rm s}^{\epsilon}$ を前節の低速固有モードが張る実不変部分空間とする。正定値2次模型では、その上の解は全時間で有界であり、各時間微分も初期エネルギーにより一様に抑えられる。

形式的な1階縮約方程式は

```math
Ax
-
g_\phi\dot y
=
0,
```

```math
By
+
g_\phi\dot x
=
0.
```

完全2次方程式との差は

```math
\mathcal R_{\rm s}
=
\begin{pmatrix}
-\epsilon_{\rm s}\ddot x\\
-\epsilon_{\rm s}\ddot y
\end{pmatrix}.
```

<!-- theorem-start:proposition -->
**命題（低速部分空間上の全時間残差）**
初期状態を $\mathcal E_{\rm s}^{\epsilon}$ に置き、初期2次エネルギーを一定に抑えると、十分小さい $\epsilon_{\rm s}$ に対し、

```math
\sup_{t\in\mathbb R}
\left\|
\mathcal R_{\rm s}(t)
\right\|
\leq
C\epsilon_{\rm s}
```

となる。$C$ はそのエネルギー上界には依存するが、時刻と $\epsilon_{\rm s}$ には依存しない。
<!-- theorem-end:proposition -->

これは各時刻の方程式残差である。低速固有振動数の $O(\epsilon_{\rm s})$ 補正により、縮約軌道との位相差は一般に $O(\epsilon_{\rm s}t)$ と蓄積し得る。従って、軌道差が全時間で $O(\epsilon_{\rm s})$ とは結論しない。

また、この残差は局所2次化された場chartの1階方程式に対するものである。粒子密度、粒子流速、密度同期を含む完全な Madelung 作用の変分残差ではない。

## F.8 高速Riesz射影

2次 Hamiltonian の線形生成子を $\mathscr L_{\epsilon}$ とする。十分小さい $\epsilon_{\rm s}$ では、低速固有値と高速固有値は分離している。高速固有値だけを囲む複素輪郭 $\gamma_{\rm f}$ を取り、

```math
\Pi_{\rm f}^{\epsilon}
=
\frac{1}{2\pi i}
\oint_{\gamma_{\rm f}}
\left(
z-\mathscr L_{\epsilon}
\right)^{-1}
\,dz
```

と定める。実高速部分空間は、共役な正負固有値の射影を合わせて得る。

<!-- theorem-start:proposition -->
**命題（高速スペクトル射影）**
正定値2次模型では、$\Pi_{\rm f}^{\epsilon}$ と

```math
\Pi_{\rm s}^{\epsilon}
=
I-\Pi_{\rm f}^{\epsilon}
```

は2次流と交換する。対応する実部分空間は不変かつsymplecticであり、2次 Hamiltonian は低速部分と高速部分の直和へ分かれる。
<!-- theorem-end:proposition -->

この射影は一般に全セルへ広がる。従って、固定グラフ辺だけへ結合する付録Eの局所作用交換浴と同じ局所機構ではない。

## F.9 同型有限補助系による高速成分交換

高速部分空間を Williamson 正準座標で

```math
H_{\rm f}
=
\frac12
\sum_{k=1}^{n}
\omega_{{\rm f},k}
\left(
Q_k^2+P_k^2
\right)
```

と書く。同じ振動数を持つ補助正準対 $(\widetilde Q_k,\widetilde P_k)$ と

```math
\widetilde H_{\rm f}
=
\frac12
\sum_{k=1}^{n}
\omega_{{\rm f},k}
\left(
\widetilde Q_k^2
+
\widetilde P_k^2
\right)
```

を置く。交換生成子を

```math
H_{\rm ex}
=
\sum_{k=1}^{n}
\left(
Q_k\widetilde P_k
-
P_k\widetilde Q_k
\right)
```

とし、内部時計で制御された結合係数を $\chi_{\rm ex}(t)$ とする。

```math
\Theta_{\rm ex}
=
\int
\chi_{\rm ex}(t)
\,dt
```

を交換角と呼ぶ。$H_{\rm ex}$ は $H_{\rm f}+\widetilde H_{\rm f}$ と Poisson 可換なので、自由回転と交換回転を分離できる。

<!-- theorem-start:theorem -->
**定理（同型高速モードの完全交換）**
補助系が対象高速部分と同型で、交換窓の間に他の結合を無視できるとする。共通自由回転を除いた座標は

```math
\begin{pmatrix}
z_{\rm f}^{\rm out}\\
\widetilde z_{\rm f}^{\rm out}
\end{pmatrix}
=
\begin{pmatrix}
\cos\Theta_{\rm ex} & -\sin\Theta_{\rm ex}\\
\sin\Theta_{\rm ex} & \cos\Theta_{\rm ex}
\end{pmatrix}
\begin{pmatrix}
z_{\rm f}^{\rm in}\\
\widetilde z_{\rm f}^{\rm in}
\end{pmatrix}.
```

$\widetilde z_{\rm f}^{\rm in}=0$ と $\Theta_{\rm ex}=\pi/2$ の下で、

```math
z_{\rm f}^{\rm out}
=
0
```

となり、対象系の高速成分は補助系へ完全に移る。
<!-- theorem-end:theorem -->

この操作は散逸でなく、有限正準系間の可逆な状態交換である。交換後も全情報と高速エネルギーは補助系に残る。次試行までに補助系を零状態へ戻すには、外部記録または排熱を含む別の再初期化過程が必要である。

定理は厳密制約後の局所2次chart内部で成立する。交換結合を元の全場変数へ大域的に持ち上げ、節を越えて規格化と $\mathcal J_\phi$ を保存する構成は未完成である。

## F.10 交換角と補助初期状態の誤差

高速2次エネルギーが定めるノルムを $\|\cdot\|_{H_{\rm f}}$ とする。前節の正確な同型模型では、

```math
\left\|
z_{\rm f}^{\rm out}
\right\|_{H_{\rm f}}
\leq
\left|
\cos\Theta_{\rm ex}
\right|
\left\|
z_{\rm f}^{\rm in}
\right\|_{H_{\rm f}}
+
\left|
\sin\Theta_{\rm ex}
\right|
\left\|
\widetilde z_{\rm f}^{\rm in}
\right\|_{H_{\rm f}}.
```

$\Theta_{\rm ex}=\pi/2+\delta\Theta$ なら、

```math
\left\|
z_{\rm f}^{\rm out}
\right\|_{H_{\rm f}}
\leq
\left|
\delta\Theta
\right|
\left\|
z_{\rm f}^{\rm in}
\right\|_{H_{\rm f}}
+
\left\|
\widetilde z_{\rm f}^{\rm in}
\right\|_{H_{\rm f}}
+
O
\left(
|\delta\Theta|^2
\right).
```

従って、交換角誤差は振幅に1次、残留エネルギーに2次で入り、補助系の非零初期エネルギーはそのまま対象へ戻り得る。

補助 Hamiltonian の複製誤差、Riesz射影の実装誤差、交換窓中の非線形項は Duhamel 型積分として加わる。これらの一様な定数と連続極限での規模依存性は未評価である。

## F.11 半正定値位相Hessianと零モード

現行の Madelung 縮約では、位相勾配エネルギーを粒子流速側へ整理し、場側で二重計数しない。この分割では $B$ は半正定値、極端には零になり得る。

1自由度で

```math
A>0,
\qquad
B=0,
\qquad
C=0
```

とすると、特性式は

```math
\omega^2
\left[
\epsilon_{\rm s}^2\omega^2
-
\epsilon_{\rm s}A
-
g_\phi^2
\right]
=
0.
```

高速振動数は

```math
\omega_{\rm f}
=
\frac{
\sqrt{
g_\phi^2
+
\epsilon_{\rm s}A
}
}{
\epsilon_{\rm s}
}
```

として残る。一方、低速側は正の振動数でなく零モードになる。一般初期値では零固有値の一般化固有空間に沿う線形成長が生じ得る。

この例は、高速帯の存在に $B>0$ が必須でないことを示す。しかし、一般の $B\geq0$、混合 Hessian、零固有値のJordan構造を含めて、

1. 高速帯だけを一様に分離すること。
2. 高速Riesz射影の正準性を保つこと。
3. 低速一般化部分空間の多項式成長を評価すること。
4. 高速交換後の残差を観測時間に一様に抑えること。

は未証明である。正定値定理を現行 M0 へ適用するために場側へ人工的な位相剛性を戻してはならない。

## F.12 有限規格化ペナルティの中間帯

厳密制約を使わず、有限 $\Lambda_N$ で規格化方向を残すと、その局所偏差を $\eta_N=N-1$ として概略

```math
H_N^{(2)}
=
\frac{
p_N^2
}{
2\epsilon_{\rm s}M_N
}
+
\frac{
\Lambda_N
}{
2
}
\eta_N^2
```

が現れる。$\Lambda_N=O(1)$ なら、

```math
\omega_N
=
O
\left(
\epsilon_{\rm s}^{-1/2}
\right).
```

これは $O(1)$ の低速帯と $O(\epsilon_{\rm s}^{-1})$ の高速帯の間にある中間帯である。実際の係数と混合は $H_0$、規格化方向、相対位相方向の全 Hessian に依存する。

従って、厳密制約模型の2帯定理を有限 $\Lambda_N$ 模型へ直接移せない。有限ペナルティ模型には、少なくとも3帯を許す別のスペクトル解析が必要である。

## F.13 非線形、時間依存、全M0への限界

本付録の厳密交換定理は、固定内点の定数係数2次模型に対する結果である。完全な局所 Hamiltonian では、

```math
G_q
=
G_q(q),
\qquad
G_\varphi
=
G_\varphi(q)
```

であり、$H_0$ は3次以上の項を持つ。これらは低速運動から高速成分を再生成し得る。適用には、初期振幅、観測時間、$\epsilon_{\rm s}$、スペクトル間隙に依存する再励起率の評価が必要である。

基準となる停留経路が時間依存なら、HessianとRiesz射影も時間に依存する。

```math
\dot\Pi_{\rm f}^{\epsilon}
\neq
0
```

であるため、射影の回転自体が低速成分と高速成分を混合する。断熱条件と幾何学的接続項を含む別の定理が必要になる。

さらに、現行 M0 には粒子座標、粒子運動量、密度、位相接続、装置、準備浴が含まれる。全系を2次化すると粒子-場混合 Hessian が現れる。本付録は場chart内部の高速法線成分を扱うが、M0全体の停留経路または特定の Schrödinger 解を選ばない。

従って、本付録が示すのは、

1. 厳密制約下の局所正準形。
2. 正定値2次模型での低速・高速分離。
3. 理想同型補助系への高速成分の可逆な完全交換。
4. 交換後の局所2次縮約方程式に対する $O(\epsilon_{\rm s})$ 残差。

までである。coherent集中、密度同期、単流束化、節、半正定値位相 Hessian、一般の時間依存停留経路は解決していない。
