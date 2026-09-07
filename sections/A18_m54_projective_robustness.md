@number: R
@chapter: 付録
@title: M54一様受動構造の射影型頑健性と加法-ノイズ障害
@status: R186の射影型製造誤差、独立位相ノイズ、射影結果の固定機構相対誤差、全自由度に加わる加法ノイズ障害を証明し、Q2-4のブラックボックス資源規約へ接続する。

## R.1 設定

$N=2^n$、$Z\in\mathbb C^N$、$S=Z^\dagger Z>0$、$P_Z=ZZ^\dagger/S$ とする。大域位相は射影型状態とBorn分布を変えないため、エルミート摂動 $V$ の射影型 半ノルムを

```math
\|V\|_{\rm proj}=\inf_{c\in\mathbb R}\|V-cI\|
```

とする。

## R.2 静的製造誤差

<!-- theorem-start:proof -->
**証明（R186）**

理想時間発展作用素を $U(t)$、摂動時間発展作用素を $\widetilde U(t)$ とする。任意の実関数 $c(t)$ について $c(t)I$ は大域位相だけを与えるので、相互作用表示とDuhamel公式から

```math
\|\widetilde U(T)-e^{-i\phi(T)}U(T)\|
\leq
\frac1{\mathcal J_0}
\int_0^T\|V(t)-c(t)I\|\,dt
```

を得る。$c(t)$ で下限を取れば本文R186第1項の評価となる。純粋状態トレース距離は位相を最適化した状態-vector距離以下なので同じ右辺で抑えられる。

局所結合器摂動行列の各行に高々 $\Delta$ 個の非零項があり、各絶対値が $\mu$ 以下なら、行和ノルムと列和ノルムから

```math
\|V\|
\leq
\sqrt{\|V\|_1\|V\|_\infty}
\leq
\Delta\mu
```

である。対角の共通ずれを $cI$ へ吸収する場合も同様で、本文では規約差を吸収する定数 $C$ を許した。

**独立位相ノイズ。**

各モードについて

```math
dZ_x=-i\sigma Z_x\circ dW_x
```

ならStratonovich解は

```math
Z_x(T)=Z_x(0)e^{-i\sigma W_x(T)}.
```

$p_x=|Z_x(0)|^2/S$ とすれば規格化重なりは

```math
\langle\psi(0)|\psi(T)\rangle
=
\sum_xp_xe^{-i\sigma W_x(T)}.
```

独立Brown 運動について $x\ne y$ なら

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

**射影結果の固定機構の係数誤差。**

枝集合 $B$ に対し $J_B=\sum_{x\in B}|Z_x|^2$、実装値を

```math
\widetilde J_B=\sum_{x\in B}(1+\delta_x)|Z_x|^2
```

とする。$|\delta_x|\leq\mu$ なら三角不等式から

```math
|\widetilde J_B-J_B|\leq\mu J_B.
```

従って指数個の部分系を含む射影子でも相対係数誤差を加算しない。

**全自由度に加わる加法ノイズ。**

加法増分を $B\,dW$、$Q_{\rm add}=BB^\dagger$ とする。状態方向に平行な成分は一次の方向誤差を作らないので、有害な平均二乗作用注入率は

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

$H=0$、$B$ 一定の保持窓ではItô 等長性から

```math
\mathbb E\|\eta_\perp(T)\|^2
=
T\operatorname{tr}[(I-P_Z)Q_{\rm add}]
\geq
(N-1)\sigma^2T.
```

信号作用 $S$ に対するRMS横方向比を $r$ 以下にする必要があれば

```math
\sigma\leq r\sqrt{\frac{S}{(N-1)T}}.
```

$N=2^n$ で $S,T,r^{-1}$ が多項式なら、右辺は $2^{-n/2}$ と多項式因子の積になる。これは現在の直接-振幅 M54が一定の等方加法ノイズ 下限を許せないことを示す障害条件であり、別の符号化または耐故障古典装置一般を排除しない。

以上でR186を証明した。
<!-- theorem-end:proof -->

## R.6 サブガウス型製造ばらつきの系

独立な局所係数偏差 $X_j$ が

```math
P(|X_j|>t)\leq2e^{-t^2/(2s^2)}
```

を満たし、部品数 $M\leq2^n p(n,d)$ なら和集合上界により、確率 $1-\alpha$ 以上で

```math
\max_j|X_j|
\leq
s\sqrt{2\log\frac{2M}{\alpha}}
=
O\!\left(s\sqrt{n+\log p+\log\alpha^{-1}}\right).
```

従って連続的な小さい製造ばらつきは、指数部品数だけを理由に指数精度を要求しない。一方、各部品が一定確率で致命的欠陥になる模型では、全ブロック正常を要求するだけなら歩留まりが指数的に低下する。R186はその耐故障性を構成しない。

## R.7 計算・逆計算診断と資源境界

加法ノイズの診断には、$|0^n\rangle$ を一様重ね合わせへ移し、保持窓の後に逆演算する計算・逆計算列を使える。ユニタリ逆演算は横方向ノイズ ノルムを消さないので、R.5の作用注入が末端状態方向誤差へ残る。方向を変えない振幅再調整も $Z\mapsto\alpha Z$ と状態方向全体を保存するため、理想成分だけを選んで増幅しない。

この付録は装置体積、部品総数、総熱を多項式へ削減しない。主張するのは、内部の指数自由度数と外部精度を自動的に同一視しないこと、および現在のM54 直接-モードでどの種類のノイズが外部指数精度へ露出するかを区別することである。
