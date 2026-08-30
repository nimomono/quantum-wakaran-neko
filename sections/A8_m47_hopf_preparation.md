@number: H
@chapter: 付録
@title: M47単一Hopf準備
@status: M47の単一Hopf準備R145を共通M51/R171の2モード特殊化として示す。閉鎖信号集団の第2モーメント輸送と2次元幾何は共通R135、W型占有振動はR140の特殊化として付録Fと本文第3章へ集約する。

## H.1 目的と主張範囲

本付録は、対称なW型ポテンシャルの最低2モードsectorで、単一試行信号bath $Z\in\mathbb C^2$ を準備し、閉鎖正準流で回転させる部分だけを扱う。粒子位置のBorn型分布、有限熱化、局所記録はM50/R170が操作面ごとに構成する。信号bathの統計核から連続粒子位置rateを作る規則は使わない。

| 段階 | 内容 | 結果 |
|---|---|---|
| 開放準備 | M51による目標rayの位相円への有限時間吸引 | R171、R145 |
| 閉鎖伝播 | 2作用角の共分散回転 | R135 |
| W型診断 | 統計核対角の左右占有振動 | R140の零傾斜特殊化 |

本筋から外した計算と旧連続matching線は、論文外の研究メモとGit履歴に保存する。いずれも現行R143またはR170の仮定に使わない。

## H.2 W型作用素と最低2モード

有限の対称1次元格子または有界区間上で、M37の古典振動子網から得る実対称包絡生成子を

```math
h_W
=
\frac{\mathcal J_0^2}{2m}L_W+V_W
```

とする。最低2モードの単純固有対を

```math
h_W\phi_0=E_0\phi_0,
\qquad
h_W\phi_1=E_1\phi_1,
\qquad
E_0<E_1
```

とし、$\phi_0$ を実偶、$\phi_1$ を実奇、両者を規格化直交とする。2モード埋込みは

```math
\Phi c=c_0\phi_0+c_1\phi_1,
\qquad
c\in\mathbb C^2
```

である。左井戸射影を $\Pi_L$ とし、対称分割で

```math
\langle\phi_0,\Pi_L\phi_0\rangle
=
\langle\phi_1,\Pi_L\phi_1\rangle
=
\frac12,
\qquad
B_W=\langle\phi_0,\Pi_L\phi_1\rangle
```

と置く。

## H.3 R145：M51/R171のW型2モード特殊化

2モード対角行列を

```math
D_W
=
\begin{pmatrix}
E_0&0\\
0&E_1
\end{pmatrix}
```

とする。目標規格化係数 $c_*$ の閉鎖回転軌道と射影を

```math
c_*(t)
=
\exp
\left[
-\frac{iD_W(t-t_*)}{\mathcal J_0}
\right]c_*,
\qquad
\Pi_*(t)=c_*(t)c_*(t)^\dagger
```

と置く。共通M51へ $m=2$、$G=D_W$、$c(t)=c_*(t)$ を代入すると、準備portが開いた区間の採用有効方程式は

```math
\dot z
=
-\frac{i}{\mathcal J_0}D_Wz
+
\lambda_{\rm prep}(t)
\left[
g(1-z^\dagger z)z
-
\kappa(I_2-\Pi_*(t))z
\right]
```

である。$g>0$ は動径供給と飽和、$\kappa>0$ は目標rayから外れた成分の散逸である。各試行の実体は2個の実正準担体、template、pump、sink、clockである。$z$ は実担体の派生複素座標、$c_*$ と $c_*c_*^\dagger$ はtemplate設定および試行集団の統計記述であり、追加の物理場ではない。

有効準備時間を

```math
\tau(t)=\int_{t_*}^t\lambda_{\rm prep}(s)\,\mathrm ds
```

とし、回転座標を $\widetilde z=ac_*+p$、$c_*^\dagger p=0$ と分解する。雑音零では

```math
\frac{da}{d\tau}
=
g(1-\|\widetilde z\|^2)a,
\qquad
\frac{dp}{d\tau}
=
\left[g(1-\|\widetilde z\|^2)-\kappa\right]p.
```

$a_0\neq0$、$q_0=\|p_0\|^2/|a_0|^2$、$y=|a|^{-2}$ と置くと

```math
\frac{\|p(\tau)\|}{|a(\tau)|}
=
\frac{\|p_0\|}{|a_0|}e^{-\kappa\tau}
```

であり、$\kappa\neq g$ では

```math
y(\tau)
=
1
+(y_0-1)e^{-2g\tau}
+\frac{gq_0}{g-\kappa}
\left(e^{-2\kappa\tau}-e^{-2g\tau}\right).
```

$\kappa=g$ では最後の項を $2gq_0\tau e^{-2g\tau}$ に置き換える。

<!-- theorem-start:theorem -->
**定理（R145：M51共通開放準備のM47特殊化）**

$g,\kappa>0$、$a_0\neq0$ とする。上の雑音零の採用開放方程式では

```math
\widetilde z(\tau)
\longrightarrow
e^{i\arg a_0}c_*.
```

$|a_0|\geq a_*>0$、$\|\widetilde z_0\|\leq R_*<\infty$ の有界seed集合では有限定数 $K_{47}$ が存在し、

```math
\operatorname{dist}
\left(
\widetilde z(\tau),
\{e^{i\alpha}c_*:\alpha\in[0,2\pi)\}
\right)
\leq
K_{47}e^{-\gamma_{47}\tau},
\qquad
\gamma_{47}=\min\{2g,\kappa\}.
```

同じseed境界を持つ集団の規格化bath第2モーメント $C_z(\tau)$ についても、有限定数 $K_C$ を選び、

```math
\|C_z(\tau)-c_*c_*^\dagger\|_1
\leq
K_Ce^{-\gamma_{47}\tau}
```

とできる。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**

$a$ と $p$ の方程式を割ると $p/a=(p_0/a_0)e^{-\kappa\tau}$ を得る。$y$ の線形方程式を積分すると上の厳密解が従い、$y\to1$、$p/a\to0$ となる。有界seed集合では係数を一様に抑えられる。外積の収束を平均し、分母が十分大きい $\tau$ で零から離れることを使えば第2モーメント上界を得る。証明終。
<!-- theorem-end:proof -->

この証明は付録MのR171証明を $m=2$ へ制限したものである。R145をM51とは別の準備機構として数えず、共通のpump、transverse sink、port切断のW型特殊化として扱う。

$a_0=0$ の直交超平面は不変である。その質量はseed失敗または無反応として残す。R145は雑音付き定常測度、位相拡散、粒子位置周辺、作用殻準備を導かない。

## H.4 共通R135のM47特殊化

準備portを切った後の古典Hamiltonianを

```math
H_{\rm rot}
=
\sum_{n=0}^1\frac{E_n}{\mathcal J_0}I_n
```

とする。正準関係から $\dot I_n=0$、$\dot\theta_n=E_n/\mathcal J_0$ であり、各試行で

```math
Z_n(t)
=
e^{-iE_n(t-t_0)/\mathcal J_0}Z_n(t_0)
```

となる。

**R135の2モード特殊化。**

$\mathbb E[Z^\dagger Z]>0$ とし、非中心化された規格化第2モーメントを

```math
C_Z
=
\frac{\mathbb E[ZZ^\dagger]}{\mathbb E[Z^\dagger Z]}
```

とする。このとき

```math
i\mathcal J_0\dot C_Z=[D_W,C_Z]
```

であり、trace、正値性、rankは保存される。$C_Z(t_0)=c_0c_0^\dagger$ なら

```math
C_Z(t)=c(t)c(t)^\dagger,
\qquad
c(t)
=
\exp
\left[-\frac{iD_W(t-t_0)}{\mathcal J_0}\right]c_0.
```
<!-- theorem-start:proof -->
**証明（R135の2モード特殊化）**

各試行で $Z(t)=U(t)Z(t_0)$ であり、$U$ はユニタリである。従って分母は一定、$C_Z(t)=U(t)C_Z(t_0)U(t)^\dagger$ である。微分すればcommutator式を得る。証明終。
<!-- theorem-end:proof -->

## H.5 R140の零傾斜W型占有振動

rank-one因子を

```math
c(t_0)
=
\begin{pmatrix}
a_0e^{-i\theta_0(t_0)}\\
a_1e^{-i\theta_1(t_0)}
\end{pmatrix},
\qquad
a_0^2+a_1^2=1
```

とし、$\delta(t)=\theta_1(t)-\theta_0(t)$ と置く。

**R140の零傾斜特殊化。**

R135のrank-one因子に対する統計核の対角は

```math
\rho_{\rm stat}(x,t)
=
a_0^2\phi_0(x)^2
+a_1^2\phi_1(x)^2
+2a_0a_1\phi_0(x)\phi_1(x)\cos\delta(t)
```

である。左井戸への積分は

```math
P_L^{\rm stat}(t)
=
\frac12+2a_0a_1B_W\cos\delta(t),
```

```math
\delta(t)
=
\delta(t_0)
+\frac{E_1-E_0}{\mathcal J_0}(t-t_0)
```

となる。従って角周波数と周期は

```math
\Omega_W=\frac{E_1-E_0}{\mathcal J_0},
\qquad
T_W=\frac{2\pi\mathcal J_0}{E_1-E_0}.
```
<!-- theorem-start:proof -->
**証明（R140の零傾斜特殊化）**

$\Phi c(t)$ の絶対値2乗を展開し、対称井戸の対角積分と $B_W$ を代入すれば従う。証明終。
<!-- theorem-end:proof -->

この $\rho_{\rm stat}$ は信号bath第2モーメントの空間核であり、それだけから単一試行粒子位置 $X$ の分布または経路は従わない。R143は各操作面でM50/R170を適用し、実在する粒子位置を別に準備して記録する。

## H.6 現行Q1への接続と限界

現行Q1は次の順序を使う。

1. R145で単一試行信号bathの方向を準備する。
2. R135とR140で有限正準操作を行う。
3. 各操作面でR170を適用し、M50枝状態数から粒子位置を再平衡化して局所記録する。
4. R143でW型有限コントラスト、傾斜固定、結果別テンプレート交換を合成する。

従って全時刻の粒子位置--信号bath matching保存は不要である。本付録からは、採用Hopf方程式の具体的回路導出、作用容量結合、作用殻fiber内平衡化、信号保持反作用、周期総収支、独立同分布型結果列は従わない。
