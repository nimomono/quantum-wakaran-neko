@number: R
@chapter: 付録
@title: M54一様受動fabricのprojective頑健性とadditive-noise障害
@status: R186のprojective製造誤差、独立phase noise、projector latch相対誤差、extensive additive-noise障害を証明し、Q2-4のblack-box資源規約へ接続する。

## R.1 設定

$N=2^n$、$Z\in\mathbb C^N$、$S=Z^\dagger Z>0$、$P_Z=ZZ^\dagger/S$ とする。global phaseはprojective stateとBorn分布を変えないため、Hermitian摂動 $V$ のprojective seminormを

```math
\|V\|_{\rm proj}=\inf_{c\in\mathbb R}\|V-cI\|
```

とする。

## R.2 静的製造誤差

<!-- theorem-start:proof -->
**証明（R186）**

理想propagatorを $U(t)$、摂動propagatorを $\widetilde U(t)$ とする。任意の実関数 $c(t)$ について $c(t)I$ はglobal phaseだけを与えるので、interaction pictureとDuhamel公式から

```math
\|\widetilde U(T)-e^{-i\phi(T)}U(T)\|
\leq
\frac1{\mathcal J_0}
\int_0^T\|V(t)-c(t)I\|\,dt
```

を得る。$c(t)$ で下限を取れば本文R186第1項の評価となる。純粋状態trace distanceは位相を最適化したstate-vector距離以下なので同じ右辺で抑えられる。

局所coupler摂動行列の各rowに高々 $\Delta$ 個の非零項があり、各絶対値が $\mu$ 以下なら、行和normと列和normから

```math
\|V\|
\leq
\sqrt{\|V\|_1\|V\|_\infty}
\leq
\Delta\mu
```

である。対角の共通ずれを $cI$ へ吸収する場合も同様で、本文では規約差を吸収する定数 $C$ を許した。

## R.3 独立phase noise

各modeについて

```math
dZ_x=-i\sigma Z_x\circ dW_x
```

ならStratonovich解は

```math
Z_x(T)=Z_x(0)e^{-i\sigma W_x(T)}.
```

$p_x=|Z_x(0)|^2/S$ とすれば規格化overlapは

```math
\langle\psi(0)|\psi(T)\rangle
=
\sum_xp_xe^{-i\sigma W_x(T)}.
```

独立Brownian運動について $x\ne y$ なら

```math
\mathbb E e^{-i\sigma(W_x-W_y)}=e^{-\sigma^2T}.
```

従って

```math
\mathbb E F(T)
=
e^{-\sigma^2T}
+
\left(1-e^{-\sigma^2T}\right)\sum_xp_x^2.
```

よって $1-\mathbb EF(T)\leq1-e^{-\sigma^2T}\leq\sigma^2T$ であり、$N$ は現れない。

## R.4 Projector latchの係数誤差

枝集合 $B$ に対し $J_B=\sum_{x\in B}|Z_x|^2$、実装値を

```math
\widetilde J_B=\sum_{x\in B}(1+\delta_x)|Z_x|^2
```

とする。$|\delta_x|\leq\mu$ なら三角不等式から

```math
|\widetilde J_B-J_B|\leq\mu J_B.
```

従って指数個のsectorを含むprojectorでも相対係数誤差を加算しない。

## R.5 Extensive additive noise

additive incrementを $B\,dW$、$Q_{\rm add}=BB^\dagger$ とする。rayに平行な成分は一次の方向誤差を作らないので、有害な平均二乗作用注入率は

```math
\operatorname{tr}[(I-P_Z)Q_{\rm add}].
```

$Q_{\rm add}\succeq\sigma^2I_N$ なら

```math
\operatorname{tr}[(I-P_Z)Q_{\rm add}]
\geq
\sigma^2\operatorname{tr}(I-P_Z)
=
(N-1)\sigma^2.
```

$H=0$、$B$ 一定のhold窓ではItô isometryから

```math
\mathbb E\|\eta_\perp(T)\|^2
=
T\operatorname{tr}[(I-P_Z)Q_{\rm add}]
\geq
(N-1)\sigma^2T.
```

signal作用 $S$ に対するRMS横方向比を $r$ 以下にする必要があれば

```math
\sigma\leq r\sqrt{\frac{S}{(N-1)T}}.
```

$N=2^n$ で $S,T,r^{-1}$ が多項式なら、右辺は $2^{-n/2}$ と多項式因子の積になる。これは現在のdirect-amplitude M54が一定のisotropic additive noise floorを許せないことを示す障害条件であり、別の符号化またはfault-tolerant古典装置一般を排除しない。

以上でR186を証明した。
<!-- theorem-end:proof -->

## R.6 Sub-Gaussian製造ばらつきの系

独立な局所係数偏差 $X_j$ が

```math
P(|X_j|>t)\leq2e^{-t^2/(2s^2)}
```

を満たし、部品数 $M\leq2^n p(n,d)$ ならunion boundにより、確率 $1-\alpha$ 以上で

```math
\max_j|X_j|
\leq
s\sqrt{2\log\frac{2M}{\alpha}}
=
O\!\left(s\sqrt{n+\log p+\log\alpha^{-1}}\right).
```

従って連続的な小さい製造ばらつきは、指数部品数だけを理由に指数精度を要求しない。一方、各部品が一定確率でhard defectになる模型では、全block正常を要求するだけならyieldが指数的に低下する。R186はそのfault toleranceを構成しない。

## R.7 Compute--uncompute診断と資源境界

additive noiseの診断には、$|0^n\rangle$ を一様重ね合わせへ移し、hold窓の後に逆演算するcompute--uncompute列を使える。unitary逆演算は横方向noise normを消さないので、R.5の作用注入が末端ray誤差へ残る。radial-only repumpも $Z\mapsto\alpha Z$ とray全体を保存するため、理想成分だけを選んで増幅しない。

この付録は装置体積、部品総数、総熱を多項式へ削減しない。主張するのは、内部の指数自由度数と外部精度を自動的に同一視しないこと、および現在のM54 direct-modeでどの種類のnoiseが外部指数精度へ露出するかを区別することである。
