@number: D
@chapter: 付録
@title: Gaussian Nelson 方程式、Schrödinger 表示、OU 例
@status: 主定理の極限作用が与える物理像と、その適用範囲を具体例で示す。

## D.1 連続の式を組み込んだ変分

Nelson 作用を

$$
\mathcal A_{\Nel}[\rho,v]
=
\int\rho
\left[
\frac m2|v|^2
-\frac{m\nu^2}{2}|\nabla\log\rho|^2
-U
\right]\dd x\dd t
$$

とする。制約

$$
\partial_t\rho+\nabla\cdot(\rho v)=0
$$

を Lagrange 乗数 $S$ で課す。$v$ について変分すると

$$
mv=\nabla S
$$

を得る。$\rho$ について変分すると

$$
\partial_tS
+\frac{|\nabla S|^2}{2m}
+U
-2m\nu^2
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=0
$$

となる。最後の項は密度勾配エネルギーの変分である。

## D.2 Schrödinger 表示

有効作用定数を

$$
\hbar_{\rm eff}=2m\nu
$$

とし、

$$
\psi=\sqrt\rho
\exp\left(\frac{iS}{\hbar_{\rm eff}}\right)
$$

と置く。連続の式と前節の Hamilton--Jacobi 型方程式を合わせると

$$
i\hbar_{\rm eff}\partial_t\psi
=
\left[
-\frac{\hbar_{\rm eff}^2}{2m}\Delta+U
\right]\psi
$$

を得る [3--6]。

この変換は、$\rho>0$ で $v$ が局所的に勾配場となる領域では厳密である。しかし、多重連結領域の循環量子化、節を横切る位相接続、一般の重ね合わせ状態は追加条件を必要とする [20]。本論文の線形 Gaussian 定理は正の密度領域に限定され、この大域位相問題を解かない。

## D.3 1次元 Gaussian 変分

平均 $q(t)$、標準偏差 $\sigma(t)>0$ の Gaussian 密度を考える。

$$
\rho(x,t)
=
\frac1{\sqrt{2\pi}\sigma}
\exp\left[-\frac{(x-q)^2}{2\sigma^2}\right].
$$

連続の式を満たす最小の1次速度場は

$$
v=\dot q+\frac{\dot\sigma}{\sigma}(x-q),
$$

浸透速度は

$$
u=-\nu\frac{x-q}{\sigma^2}
$$

である。Gaussian 平均を取ると

$$
\E[v^2]=\dot q^2+\dot\sigma^2,
\qquad
\E[u^2]=\frac{\nu^2}{\sigma^2}.
$$

調和ポテンシャル $U=m\Omega^2x^2/2$ では

$$
\E[U]=\frac{m\Omega^2}{2}(q^2+\sigma^2)
$$

なので、第4.7節の有限次元作用を得る。

## D.4 幅方程式の保存量

幅方程式

$$
\ddot\sigma+\Omega^2\sigma-\frac{\nu^2}{\sigma^3}=0
$$

には

$$
E_\sigma
=
\frac12\dot\sigma^2
+\frac12\Omega^2\sigma^2
+\frac{\nu^2}{2\sigma^2}
$$

という保存量がある。$\sigma\to0$ では最後の項が発散するため、正の初期幅は有限時間で零にならない。定常点 $\sigma_*^2=\nu/\Omega$ の周囲では幅が振動する。

この振る舞いは、通常の熱拡散が平衡へ単調緩和する像とは異なる。Nelson 作用では、確率流の運動項と密度勾配項が実時間の変分原理で釣り合い、可逆な幅運動を作る。

## D.5 2次元 OU 位相模型

計算例として

$$
\dd Z_t
=
(-\lambda I+\Omega J)Z_t\dd t
+\sqrt{2D}\,\dd W_t,
\qquad
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
$$

を考える [19]。$\lambda>0$ なら定常共分散は

$$
\operatorname{Cov}(Z)=\frac D\lambda I
$$

である。$\Omega=0$ なら定常過程は詳細釣り合いを満たす。$\Omega\neq0$ では縮約された位相平面に定常回転流があり、通常の時間反転だけでは詳細釣り合いを満たさない。

このことは微視的 Hamiltonian 中核の可逆性と矛盾しない。$\lambda$ は消去した浴への有効緩和、$\Omega$ は残した調和回転を表す。OU 模型は観測部分系の計算表示であり、閉じた全系そのものではない。

## D.6 Itô と Stratonovich

一般に

$$
\dd X=b(X,t)\dd t+\sigma(X,t)\circ\dd W_t
$$

を Itô 表現へ変換すると、$\sigma$ の空間微分に比例する補正が流れへ加わる。本論文では $\sigma=\sqrt{2\nu}I$ が定数なので補正は零である。

従って線形 Gaussian 定理、Schur 補完、Guerra--Morato 作用、Nelson 表示のいずれも、Itô と Stratonovich の記法選択に依存しない。Stratonovich 微分は、乗法的雑音へ拡張するときに初めて本質的になる。

## D.7 Bell 部分との接続

2次元 Gaussian 位相変数は、第6章の実正準伝達ベクトルを具体化する候補になる。しかし、OU 定常分布だけでは左右の等振幅、共通生成時位相、4つの符号領域の対称性は自動的に保証されない。

従って

$$
\mathrm{OU}_{2D}
\quad\not\Rightarrow\quad
\mathrm{Bell\ cosine\ law}.
$$

Bell 系論には、位相同期した生成源 `[P]`、対称準備 `[S]`、2モード入口測度 `[M]`、2境界履歴集団 `[R]` が別に必要である。この点を保つことで、Gaussian Nelson 部分と Bell 部分の役割が明確になる。
