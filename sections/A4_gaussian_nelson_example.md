@number: D
@chapter: 付録
@title: Gauss 型 Nelson 方程式、Schrödinger 表示、OU 補助モデル
@status: 主定理の極限作用が与える物理像を示し、OU 表示を弱開放現行モデルそのものではなく補助モデルとして用いる。

## D.1 連続の式を組み込んだ変分

Nelson 作用を

```math
\mathcal A_{\mathrm{N}}[\rho,v]
=
\int\rho
\left[
\frac m2|v|^2
-\frac{m\nu^2}{2}|\nabla\log\rho|^2
-U
\right]\,\mathrm{d} x\,\mathrm{d} t
```

とする。制約

```math
\partial_t\rho+\nabla\cdot(\rho v)=0
```

を Lagrange 乗数 $S$ で課す。$v$ について変分すると

```math
mv=\nabla S
```

を得る。$\rho$ について変分すると

```math
\partial_tS
+\frac{|\nabla S|^2}{2m}
+U
-2m\nu^2
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=0
```

となる。最後の項は密度勾配エネルギーの変分である。

## D.2 Schrödinger 表示

有効作用定数を

```math
\hbar_{\rm eff}=2m\nu
```

とし、

```math
\psi=\sqrt\rho
\exp\left(\frac{iS}{\hbar_{\rm eff}}\right)
```

と置く。連続の式と前節の Hamilton--Jacobi 型方程式を合わせると

```math
i\hbar_{\rm eff}\partial_t\psi
=
\left[
-\frac{\hbar_{\rm eff}^2}{2m}\Delta+U
\right]\psi
```

を得る [3--6]。

この変換は、$\rho>0$ で $v$ が局所的に勾配場となる領域では厳密である。しかし、多重連結領域の循環量子化、節を横切る位相接続、一般の重ね合わせ状態は追加条件を必要とする [20]。本論文の線形 Gauss 型定理は正の密度領域に限定され、この大域位相問題を解かない。

## D.3 1次元 Gauss 型変分

平均 $q(t)$、標準偏差 $\sigma(t)>0$ の Gauss 型密度を考える。

```math
\rho(x,t)
=
\frac1{\sqrt{2\pi}\sigma}
\exp\left[-\frac{(x-q)^2}{2\sigma^2}\right].
```

連続の式を満たす最小の1次速度場は

```math
v=\dot q+\frac{\dot\sigma}{\sigma}(x-q),
```

浸透速度は

```math
u=-\nu\frac{x-q}{\sigma^2}
```

である。Gauss 平均を取ると

```math
\mathbb{E}[v^2]=\dot q^2+\dot\sigma^2,
\qquad
\mathbb{E}[u^2]=\frac{\nu^2}{\sigma^2}.
```

調和ポテンシャル $U=m\Omega^2x^2/2$ では

```math
\mathbb{E}[U]=\frac{m\Omega^2}{2}(q^2+\sigma^2)
```

なので、第4.7節の有限次元作用を得る。

## D.4 幅方程式の保存量

幅方程式

```math
\ddot\sigma+\Omega^2\sigma-\frac{\nu^2}{\sigma^3}=0
```

には

```math
E_\sigma
=
\frac12\dot\sigma^2
+\frac12\Omega^2\sigma^2
+\frac{\nu^2}{2\sigma^2}
```

という保存量がある。$\sigma\to0$ では最後の項が発散するため、正の初期幅は有限時間で零にならない。定常点 $\sigma_*^2=\nu/\Omega$ の周囲では幅が振動する。

この振る舞いは、通常の熱拡散が平衡へ単調緩和する像とは異なる。Nelson 作用では、確率流の運動項と密度勾配項が実時間の変分原理で釣り合い、可逆な幅運動を作る。

## D.5 2次元 OU 位相補助モデル

計算例として

```math
\,\mathrm{d} Z_t
=
(-\lambda I+\Omega J)Z_t\,\mathrm{d} t
+\sqrt{2D}\,\,\mathrm{d} W_t,
\qquad
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
```

を考える [19]。$\lambda>0$ なら定常共分散は

```math
\operatorname{Cov}(Z)=\frac D\lambda I
```

である。$\Omega=0$ なら定常過程は詳細釣り合いを満たす。$\Omega\neq0$ では縮約された位相平面に定常回転流があり、通常の時間反転だけでは詳細釣り合いを満たさない。

このことは閉鎖 Hamiltonian 補助モデルの可逆性と矛盾しない。$\lambda$ は消去した外部自由度への有効緩和、$\Omega$ は残した調和回転を表す。OU 表示は弱開放な観測部分系の計算用補助モデルであり、現行モデルの外部結合とエネルギー収支をそれ自体で与えるものではない。

OU 近似を現行モデルへ用いるには、外部相関時間 $\tau_{\rm corr}$ と遅い位相時間 $\tau_{\rm slow}$ の比

```math
\varepsilon_{\rm M}
=
\frac{\tau_{\rm corr}}{\tau_{\rm slow}}
\ll1
```

を要求し、記憶核と有色雑音の残差を測る必要がある。本付録はこの縮約を導出せず、$\lambda$、$\Omega$、$D$ を有効係数として置く。

## D.6 Itô と Stratonovich

一般に

```math
\,\mathrm{d} X=b(X,t)\,\mathrm{d} t+\sigma(X,t)\circ\,\mathrm{d} W_t
```

を Itô 表現へ変換すると、$\sigma$ の空間微分に比例する補正が流れへ加わる。本論文では $\sigma=\sqrt{2\nu}I$ が定数なので補正は零である。

従って線形 Gauss 型定理、Schur 補完、Guerra--Morato 作用、Nelson 表示のいずれも、Itô と Stratonovich の記法選択に依存しない。Stratonovich 微分は、乗法的雑音へ拡張するときに初めて本質的になる。

## D.7 Bell 部分との接続

2次元 Gauss 型位相変数は、第6章の実正準伝達ベクトルを具体化する候補になる。しかし、OU 定常分布だけでは左右の等振幅、共通生成時位相、4つの符号領域の対称性は自動的に保証されない。

従って

```math
\mathrm{OU}_{2D}
\quad\not\Rightarrow\quad
\mathrm{Bell\ cosine\ law}.
```

Bell 系論には、位相同期した生成源 `[P]`、対称準備 `[S]`、2モード入口測度 `[M]`、2境界履歴集団 `[R]` が別に必要である。この点を保つことで、Gauss 型 Nelson 部分と Bell 部分の役割が明確になる。
