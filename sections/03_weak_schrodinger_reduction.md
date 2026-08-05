@number: 3
@chapter: 本文
@title: 有限時間弱 Schrödinger 型縮約、節、励起状態
@status: コヒーレント縮約集合上の Madelung 作用と、その変分は厳密結果である。各標本の弱縮約残差を仮定した有限時間安定性と弱密度同期は近似結果である。現行ミクロ模型から節近傍を含む残差上界を導く部分は未完成である。

## 3.1 有効複素場の位相向き

ミクロ複素場 $\zeta^\omega=\Phi_1^\omega+i\Phi_2^\omega$ と、その射影的代表場 $\bar\zeta$ を第2章で定めた。位相接続の縮約作用では

```math
S
=
-
\mathcal J_\phi
\theta
```

となるため、Schrödinger 表示の位相向きは保存作用の符号に依存する。そこで、有効場を

```math
\psi
=
\operatorname{Re}
\bar\zeta
-
i
\operatorname{sgn}
\left(
\mathcal J_\phi
\right)
\operatorname{Im}
\bar\zeta
```

と定める。$\mathcal J_\phi>0$ なら $\psi=\bar\zeta^*$、$\mathcal J_\phi<0$ なら $\psi=\bar\zeta$ である。従って

```math
q
=
\left|
\psi
\right|^2
=
\left|
\bar\zeta
\right|^2
```

である。

有効作用定数を

```math
\hbar_{\rm eff}
=
\left|
\mathcal J_\phi
\right|
```

とする。$\bar\zeta$ と $\psi$ を同じ記号にせず、ミクロ場、代表場、有効場の役割を分ける。

## 3.2 コヒーレント縮約集合上の作用

節外の局所座標で、局所作用整合、密度同期、単流束化、動径低速化、接続極限を理想的に課す。場の正準項と粒子の接続項は

```math
-\int
\rho
\left(
\partial_tS
+
\boldsymbol v
\cdot
\nabla S
\right)
\,dx
```

を作る。固定作用セクターで定数となる回転基底エネルギーを除くと、制限作用は

```math
\mathcal A_{\rm red}
\left[
\rho,
\boldsymbol v,
S
\right]
=
\int
\left[
\frac m2
\rho
\left|
\boldsymbol v
\right|^2
-
\rho V
-
\rho
\left(
\partial_tS
+
\boldsymbol v
\cdot
\nabla S
\right)
-
\kappa
\left|
\nabla\sqrt\rho
\right|^2
\right]
\,dx\,dt
```

となる。

<!-- theorem-start:theorem -->
**定理（縮約集合上の Madelung 作用）**
理想縮約条件と係数整合

```math
\kappa
=
\frac{
\mathcal J_\phi^2
}{
2m
}
```

の下で、$\mathcal A_{\rm red}$ は作用定数 $\hbar_{\rm eff}$ を持つ Madelung 作用に一致する。
<!-- theorem-end:theorem -->

この定理は、縮約集合へ制限した後の作用の代数的一致である。ミクロ流がその集合へ吸引されること、または制限作用の特定の停留経路を選ぶことは含まない。

$S$、$\boldsymbol v$、$\rho$ を独立に変分すると、

```math
\partial_t\rho
+
\nabla
\cdot
\left(
\rho\boldsymbol v
\right)
=
0,
\qquad
m\boldsymbol v
=
\nabla S
```

および

```math
\partial_tS
+
\frac{
\left|
\nabla S
\right|^2
}{
2m
}
+
V
-
\frac{
\mathcal J_\phi^2
}{
2m
}
\frac{
\Delta\sqrt\rho
}{
\sqrt\rho
}
=
0
```

を得る。後2式を節外で複素表示へまとめると理想 Schrödinger 型方程式になる。

## 3.3 弱縮約残差

一般の実外部位置ポテンシャルに対し、

```math
H_V(t)
=
-
\frac{
\hbar_{\rm eff}^2
}{
2m
}
\Delta
+
V(x,t)
```

とする。共通2次形式領域を $\mathcal Q$、その双対を $\mathcal Q^*$ とする。

標本ごとの位相向きを整えた有効場を $\psi^\omega$ とする。第2章の連続位相整合を行った後、ミクロ時間発展が

```math
i\hbar_{\rm eff}
\partial_t
\psi^\omega
=
H_V(t)
\psi^\omega
+
R^\omega
```

を $\mathcal Q^*$ で満たすと仮定する。共通位相項がある場合は、標本ごとの連続位相変換へ吸収する。弱方程式を制御する残差を

```math
\varepsilon_{\rm mic}^{\rm wk}(T)
=
\int_0^T
\left(
\mathbb E_\omega
\left\|
R^\omega(t)
\right\|_{\mathcal Q^*}^2
\right)^{1/2}
\,dt
```

と定める。エネルギーノルムでのコヒーレント安定性には、これより強い

```math
\varepsilon_{\rm mic}^{\mathcal E}(T)
=
\int_0^T
\left(
\mathbb E_\omega
\left\|
R^\omega(t)
\right\|_{\mathcal E_V}^2
\right)^{1/2}
\,dt
```

も仮定する。$\mathcal E_V$ は連続埋め込みにより $\mathcal Q^*$ の残差としても読める。双対残差だけからエネルギーノルム集中は導かない。

$R^\omega$ は1つの物理誤差ではなく、次をまとめた監査量である。

1. 有限セルと連続極限の差。
2. 局所作用欠陥と動径欠陥。
3. 正定値2次模型から外れる半正定値方向。
4. 時間依存する低速・高速射影。
5. 非線形高速再励起。
6. 係数不一致。
7. 節近傍の正則化接続と密度差の重み付き積。

現行ミクロ模型から1から7を一様に評価する定理はない。粒子・場流束差は $R^\omega$ へ含めず、第3.6節の独立な同期誤差として扱う。付録Fの局所2次残差は3から5を除いた限定模型での部分結果である。

## 3.4 主定理1

<!-- theorem-start:theorem -->
**定理（準備済み集団の条件付き有限時間弱縮約）**
有限観測時間 $T>0$ を固定する。次を仮定する。

1. $H_V(t)$ が共通形式領域 $\mathcal Q$ 上で有限時間安定な発展作用素を生成する。
2. $\|\psi^\omega(t)\|_{\mathcal E_V}$ が $\omega$ と $0\leq t\leq T$ について一様に有界である。
3. 初期コヒーレント分散 $\varepsilon_{\rm coh}(0)$ が小さい。
4. 連続位相整合後の残差が $\varepsilon_{\rm mic}^{\rm wk}(T)$ と $\varepsilon_{\rm mic}^{\mathcal E}(T)$ の上界を満たす。
5. 位相整合平均が零にならず、代表場の連続位相規約を選べる。

このとき、規格化した代表有効場 $\psi$ と実数値関数 $\lambda(t)$ が存在し、

```math
i\hbar_{\rm eff}
\partial_t\psi
=
H_V(t)\psi
+
\lambda(t)\psi
+
R_{\rm red}
```

が $\mathcal Q^*$ で成立する。さらに、

```math
\left\|
R_{\rm red}
\right\|_{
L^1
\left(
0,T;
\mathcal Q^*
\right)
}
\leq
C_T
\varepsilon_{\rm mic}^{\rm wk}(T)
```

および

```math
\sup_{
0\leq t\leq T
}
\varepsilon_{\rm coh}(t)
\leq
C_T
\left[
\varepsilon_{\rm coh}(0)
+
\varepsilon_{\rm mic}^{\mathcal E}(T)
\right]
```

を得る。時間依存の共通位相変換により $\lambda(t)$ を除去できる。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
標本ごとの共通位相を初期代表場から連続に選び、位相整合した場を作る。共通線形発展を差し引くと、2標本の差は初期差と残差差の Duhamel 積分で表される。エネルギーノルムでの有限時間安定性と Minkowski 不等式により、$\varepsilon_{\rm mic}^{\mathcal E}$ を用いたコヒーレント分散の上界を得る。位相整合平均を規格化すると、平均残差と規格化微分の組合せが代表場の接空間に入る。その位相方向成分を実数の $\lambda(t)$ とし、残りを $R_{\rm red}$ とする。平均ノルムの正の下限により、両者は $\varepsilon_{\rm mic}^{\rm wk}$ で評価できる。詳細は付録Aに置く。
<!-- theorem-end:proof -->

この定理は、双対残差とエネルギー残差がともに小さいなら、コヒーレント集中が有限時間保たれ、代表場も小さい残差の弱方程式を満たすという安定性結果である。仮定4を現行 M0 から導くことは定理の外にある。従って「有限古典 Hamiltonian 系から節を含む Schrödinger 方程式を無条件に導出した」とは読まない。

## 3.5 場強度・場流束の集中

位相整合した標本場と代表場の差を $\delta\psi^\omega=\psi^\omega-\psi$ とする。$L^2$ と勾配の一様上界があれば、

```math
\left\|
\left|
\psi^\omega
\right|^2
-
\left|
\psi
\right|^2
\right\|_{L^1}
\leq
\left(
\left\|
\psi^\omega
\right\|_{L^2}
+
\left\|
\psi
\right\|_{L^2}
\right)
\left\|
\delta\psi^\omega
\right\|_{L^2}
```

である。また、

```math
\begin{aligned}
&
\left\|
\operatorname{Im}
\left[
\left(
\psi^\omega
\right)^*
\nabla\psi^\omega
-
\psi^*
\nabla\psi
\right]
\right\|_{L^1}
\\
&\qquad
\leq
\left\|
\delta\psi^\omega
\right\|_{L^2}
\left\|
\nabla\psi^\omega
\right\|_{L^2}
+
\left\|
\psi
\right\|_{L^2}
\left\|
\nabla\delta\psi^\omega
\right\|_{L^2}.
\end{aligned}
```

従ってエネルギーノルムでのコヒーレント集中は、標本場の強度と場流束の代表場への集中を与える。粒子密度・流束との同期はこの積評価からは従わない。

## 3.6 粒子密度との弱同期

粒子側と場側の連続の式の差を

```math
\partial_t
\left(
\rho-q
\right)
+
\nabla
\cdot
\left(
\boldsymbol J_{\rm p}
-
\boldsymbol j_\psi
\right)
=
R_{\rm cont}
```

とする。ここで

```math
\boldsymbol j_\psi
=
\frac{
\hbar_{\rm eff}
}{
m
}
\operatorname{Im}
\left(
\psi^*
\nabla\psi
\right)
```

である。

<!-- theorem-start:proposition -->
**命題（弱密度同期評価）**
適切な境界条件の下で、

```math
\begin{aligned}
\left\|
\rho(t)-q(t)
\right\|_{H^{-1}}
\leq{}&
\left\|
\rho(0)-q(0)
\right\|_{H^{-1}}
\\
&
+
\int_0^t
\left\|
\boldsymbol J_{\rm p}
-
\boldsymbol j_\psi
\right\|_{L^2}
\,ds
+
\int_0^t
\left\|
R_{\rm cont}
\right\|_{H^{-1}}
\,ds.
\end{aligned}
```
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
差の連続の式を時間積分し、発散作用素が $L^2$ から $H^{-1}$ へ有界であることを使う。
<!-- theorem-end:proof -->

この命題は密度同期の有限時間評価である。連続の式だけから流束同期の保存は導けない。粒子速度分散、接続追従、古典圧力を含む流束差の時間積分は独立の仮定である。

## 3.7 節を含む大域弱形式

時間依存の共通位相を除いた後、主定理1の式は

```math
i\hbar_{\rm eff}
\partial_t\psi
=
H_V(t)\psi
+
R_{\rm red}
```

となる。これは $\psi=0$ の点でも定義できる。試験関数 $\eta\in C_c^\infty$ に対し、

```math
\begin{aligned}
&
\int_0^T
\left[
-
i\hbar_{\rm eff}
\left\langle
\psi,
\partial_t\eta
\right\rangle
+
\frac{
\hbar_{\rm eff}^2
}{
2m
}
\left\langle
\nabla\psi,
\nabla\eta
\right\rangle
+
\left\langle
V\psi,
\eta
\right\rangle
\right]
\,dt
\\
&\qquad
=
\int_0^T
\left\langle
R_{\rm red},
\eta
\right\rangle
\,dt
\end{aligned}
```

と書ける。端点項は試験関数の支持または初期値形式に応じて加える。

節集合を

```math
\mathcal Z_t
=
\left\{
x
\mid
\psi(x,t)=0
\right\}
```

とする。大域弱形式は $\mathcal Z_t$ を除外しない。一方、

```math
\psi
=
\sqrt q
\exp
\left(
\frac{
iS
}{
\hbar_{\rm eff}
}
\right)
```

という Madelung 表示は、$\mathcal Z_t$ を除いた各連結節領域 $\Omega_k(t)$ だけで用いる。量子ポテンシャルを節上で点ごとに評価しない。

複素弱形式を採用したことは、ミクロ位相接続から節をまたぐ導出が完成したことを意味しない。正則化接続

```math
\boldsymbol a_\varepsilon
=
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

と密度誤差の積を制御するには、節近傍の粒子質量上界、重み付き同期、正則化極限と有限セル極限の順序が必要である。これは $\varepsilon_{\rm mic}^{\rm wk}$ と $\varepsilon_{\rm mic}^{\mathcal E}$ の未導出成分である。

## 3.8 節外の Madelung 表示と循環量子化

$q>0$ の各節領域で、理想残差を零とすれば弱方程式は連続の式と Hamilton--Jacobi 型方程式へ分解できる。非零残差は両式の弱い源項へ分かれる。

2成分場が閉曲線 $\gamma$ 上で非零かつ単価なら、位相巻数 $n\in\mathbb Z$ により

```math
\oint_\gamma
\nabla\theta
\cdot
d\ell
=
2\pi n
```

である。従って

```math
\oint_\gamma
\nabla S
\cdot
d\ell
=
2\pi
\hbar_{\rm eff}
N,
\qquad
N\in\mathbb Z
```

を得る。

これは単価な基礎場と非零経路を仮定した条件付き循環量子化である。節の生成・消滅時の巻数変化、全ての物理的初期流れを単価場から準備すること、節近傍の接続極限は未完成である。従って Wallstrom 問題への全面的回答ではない [19]。

## 3.9 対称性セクターと励起状態

時間非依存の $H_V$ が離散固有値を持つとする。保存対称性で不変な閉部分空間 $\mathcal H_\sigma$ を取り、

```math
H_V
\varphi_n
=
E_n
\varphi_n,
\qquad
\varphi_n
\in
\mathcal H_\sigma
```

とする。

<!-- theorem-start:corollary -->
**系（対称性で保護された固有状態の条件付き包含）**
主定理1の残差が零で、初期代表場が $\varphi_n$ なら、

```math
\psi_n(t)
=
\exp
\left(
-
\frac{
iE_nt
}{
\hbar_{\rm eff}
}
\right)
\varphi_n
```

は大域弱方程式の定常解である。$\mathcal H_\sigma$ が発展で不変なら、その対称性が強制する節は保存される。
<!-- theorem-end:corollary -->

例えば奇パリティ部分空間の最低固有状態は、全空間では励起状態になり得る。この系は有効方程式が節を持つ固有状態を許容することを示すが、準備浴がその状態を選ぶことは示さない。

次は未解決である。

1. 任意初期状態からの励起状態選択。
2. 低速部分空間内のエネルギー緩和。
3. 一般の非対称ポテンシャルでの節固定。
4. 節の生成、消滅、再結合。
5. $H^1$ 型集中だけから節集合の形と個数を保存すること。

## 3.10 Nelson 表示との関係

節外で

```math
\boldsymbol v
=
\frac{
\nabla S
}{
m
},
\qquad
\boldsymbol u
=
\frac{
\hbar_{\rm eff}
}{
2m
}
\nabla
\log\rho
```

と置けば、縮約作用は Nelson の現在速度・浸透速度表示と同じ係数構造を持つ [3--6,30]。これは有効作用の別表示であり、実在する前進・後退 Markov 過程の導出ではない。配置拡散から同じ構造を得る補助経路は付録Dに置く。

## 3.11 力学的到達点

本章で得たものは次である。

1. 制限作用上の Madelung 構造。
2. 双対残差とエネルギー残差を仮定した代表複素場とコヒーレント分散の有限時間評価。
3. 流束差上界を仮定した弱密度同期評価。
4. 節を含む大域複素弱形式と、節外の Madelung 表示・条件付き循環量子化。
5. 対称性で保護された固有状態の条件付き包含。
