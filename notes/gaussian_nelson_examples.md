# Gauss 型 Nelson 表示と OU 補助例

> **位置づけ。** M3「OU 位相表示」と、主定理の理解を助ける補助計算。draft-10の第2.6節と付録Dを整理した。現行論文の主定理、Bell 型共同法則、弱開放ミクロモデルからの縮約を実質的に支えないため、論文生成から外した。

関連文献：G. E. Uhlenbeck and L. S. Ornstein, “On the Theory of the Brownian Motion,” Physical Review 36, 823–841 (1930). <https://doi.org/10.1103/PhysRev.36.823>

## 1. Nelson 作用の局所的な Schrödinger 表示

Nelson 作用を

```math
\mathcal A_{\rm N}[\rho,v]
=
\int\rho
\left[
\frac m2|v|^2
-
\frac{m\nu^2}{2}|\nabla\log\rho|^2
-
U
\right]
\,\mathrm{d}x\,\mathrm{d}t
```

とする。連続の式を Lagrange 乗数 $S$ で課すと、

```math
mv=\nabla S
```

と

```math
\partial_tS
+
\frac{|\nabla S|^2}{2m}
+
U
-
2m\nu^2
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=
0
```

を得る。$\hbar_{\rm eff}=2m\nu$ と

```math
\psi
=
\sqrt\rho
\exp\left(\frac{iS}{\hbar_{\rm eff}}\right)
```

を用いると、正の密度を持つ局所領域で Schrödinger 型方程式へ書き換えられる。この表示変換の要点は本文第4.5節へ残した。

## 2. 1次元 Gauss 型変分

平均 $q(t)$、標準偏差 $\sigma(t)>0$ の Gauss 型密度と、連続の式を満たす速度場

```math
v
=
\dot q
+
\frac{\dot\sigma}{\sigma}(x-q)
```

を考える。浸透速度は

```math
u
=
-\nu\frac{x-q}{\sigma^2}
```

である。調和ポテンシャル $U=m\Omega^2x^2/2$ では

```math
\mathcal A_G[q,\sigma]
=
\frac m2
\int
\left[
\dot q^2+\dot\sigma^2
-
\frac{\nu^2}{\sigma^2}
-
\Omega^2(q^2+\sigma^2)
\right]
\,\mathrm{d}t
```

となり、

```math
\ddot q+\Omega^2q=0,
```

```math
\ddot\sigma+\Omega^2\sigma-\frac{\nu^2}{\sigma^3}=0
```

を得る。幅方程式の保存量は

```math
E_\sigma
=
\frac12\dot\sigma^2
+
\frac12\Omega^2\sigma^2
+
\frac{\nu^2}{2\sigma^2}.
```

この例は Nelson 作用の密度勾配項が可逆な幅運動を作ることを示すが、弱開放系の緩和や停留点選択を導かない。

## 3. 2次元 OU 位相表示

計算例として

```math
\,\mathrm{d}Z_t
=
(-\lambda I+\Omega J)Z_t\,\mathrm{d}t
+
\sqrt{2D}\,\,\mathrm{d}W_t
```

を考える。$\lambda>0$ なら定常共分散は

```math
\operatorname{Cov}(Z)
=
\frac D\lambda I.
```

$\lambda$ は消去した外部自由度への有効緩和、$\Omega$ は残した調和回転を表す。これは弱開放部分系の計算用補助モデルであり、外部結合とエネルギー収支をそれ自体で与えない。

OU 近似を現行モデルへ接続するには

```math
\varepsilon_{\rm M}
=
\frac{\tau_{\rm corr}}{\tau_{\rm slow}}
\ll1
```

を要求し、記憶核と有色雑音の残差を評価する必要がある。

## 4. Itô 表現と Stratonovich 表現

加法雑音では雑音係数の空間微分が零なので、Itô 表現と Stratonovich 表現の変換補正は零である。乗法的雑音へ拡張しない限り、記法の選択は線形 Gauss 型定理、Schur 補完、Nelson 表示を変えない。

## 5. 再検討条件

明示した有限 Hamiltonian 部分と外部結合から $\lambda$、$\Omega$、$D$ を導き、有限観測時間における Markov 近似誤差を評価できた場合に、OU 表示を現行論文へ戻す価値が生じる。
