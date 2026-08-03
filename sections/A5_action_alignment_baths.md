@number: A5
@chapter: 付録
@title: 局所作用整合と動径低速化の有限準備浴
@status: 有限調和浴の Hamiltonian、共通位相回転対称性、全位相作用の保存、対称な余弦・正弦結合による位相固定項の消去は厳密結果である。記憶摩擦、欠陥減衰、有限温度床、有限時間準備は明記した短記憶・固定振幅近似の下での結果である。一般初期値に対する一様収束と長期反復は未完成である。

## E.1 目的と時間窓

第2.6節の有限特異 Hamiltonian は、局所作用整合と動径低速化を低速枝として与えるが、一般初期値からその枝を準備しない。本付録では、対象場から高速欠陥エネルギーを有限浴へ移す Hamiltonian を明示する。

準備に使う浴は観測中の位相運動を変え得るため、内部時計の準備窓だけ作動させる。時計正準対を $(\vartheta,J_\vartheta)$ とし、作動帯で滑らかな窓関数

```math
0
\leq
g_{\rm prep}(\vartheta)
\leq
1
```

を用いる。準備平坦部で $g_{\rm prep}=1$、観測窓で $g_{\rm prep}=0$ とする。時計を含む全 Hamiltonian は自律的である。

## E.2 振幅座標の有限浴

セル $i$ の振幅座標 $R_i$ に有限個の調和振動子を結合する。浴正準対を $(Q_{i\alpha},\mathcal P_{i\alpha})$ とし、

```math
H_{R{\rm B}}
=
\sum_{i,\alpha}
\left[
\frac{
\mathcal P_{i\alpha}^2
}{
2m_\alpha
}
+
\frac{
m_\alpha\omega_\alpha^2
}{
2
}
\left(
Q_{i\alpha}
-
\frac{
c_\alpha g_{\rm prep}(\vartheta)R_i
}{
m_\alpha\omega_\alpha^2
}
\right)^2
\right]
```

とする。準備平坦部で浴を正確に消去すると、$P_i$ の式に

```math
-\int_0^t
K_R(t-s)
\dot R_i(s)
\,ds
+
\xi_i(t)
```

が加わる。記憶核は

```math
K_R(t)
=
\sum_\alpha
\frac{
c_\alpha^2
}{
m_\alpha\omega_\alpha^2
}
\cos
\left(
\omega_\alpha t
\right).
```

有限浴では $K_R$ は余弦関数の有限和であり、厳密な局所摩擦ではない。再帰前の短記憶領域で

```math
\int_0^t
K_R(t-s)
\dot R_i(s)
\,ds
\simeq
\eta_R\dot R_i
```

と近似できるとき、

```math
\dot P_i
\simeq
-
\frac{
\partial H_{\epsilon_{\rm s}}
}{
\partial R_i
}
-
\frac{
\eta_R
}{
\epsilon_{\rm s}M
}
P_i
+
\xi_i.
```

従って振幅浴は $P_i$ の高速成分を抑える。ただし、低速枝では $R_i$ 自体が動くため、目標は $P_i=0$ の永久固定ではなく、観測開始時に $P_i=O(\epsilon_{\rm s})$ となる準備である。

## E.3 全作用を保存する作用交換浴

セルを結ぶ連結グラフを取り、辺 $e=(i,k)$ の向き付き接続ベクトルを $b_e=e_i-e_k$ とする。位相差と2つの周期関数を

```math
\phi_e
=
b_e^{\mathsf T}\boldsymbol\theta,
\qquad
F_{e,c}
=
\cos\phi_e,
\qquad
F_{e,s}
=
\sin\phi_e
```

と定める。作用交換浴の正準対を $(X_{e\sigma\alpha},\Pi_{e\sigma\alpha})$ とし、

```math
\begin{aligned}
H_{J{\rm B}}
=
\sum_{e,\sigma,\alpha}
\Bigg[
&
\frac{
\Pi_{e\sigma\alpha}^2
}{
2\mu_\alpha
}
\\
&+
\frac{
\mu_\alpha\Omega_\alpha^2
}{
2
}
\left(
X_{e\sigma\alpha}
-
\frac{
d_\alpha g_{\rm prep}(\vartheta)F_{e,\sigma}
}{
\mu_\alpha\Omega_\alpha^2
}
\right)^2
\Bigg],
\end{aligned}
```

```math
\sigma
\in
\{c,s\}
```

とする。同じ辺の余弦系列と正弦系列には同じ $(\mu_\alpha,\Omega_\alpha,d_\alpha)$ を用いる。

<!-- theorem-start:proposition -->
**命題（有限作用交換浴の全位相作用保存）**
$H_{J{\rm B}}$ は共通位相回転 $\theta_i\mapsto\theta_i+\beta$ に不変である。従って、

```math
\left\{
\mathcal J_\phi,
H_{\epsilon_{\rm s}}
+
H_{R{\rm B}}
+
H_{J{\rm B}}
+
H_{\rm clk}
\right\}
=
0.
```

時計窓の立ち上がりと立ち下がりを含め、$\mathcal J_\phi=\sum_iJ_i$ は厳密に保存される。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
$H_{J{\rm B}}$ の位相依存性は全て $\theta_i-\theta_k$ を通じる。$H_{R{\rm B}}$ と $H_{\rm clk}$ は共通位相に依存しない。従って全 Hamiltonian は共通回転不変であり、その生成子 $\mathcal J_\phi$ との Poisson 括弧は零である。
<!-- theorem-end:proof -->

各辺の2系列から生じる逆項は

```math
\frac{
d_\alpha^2g_{\rm prep}^2
}{
2\mu_\alpha\Omega_\alpha^2
}
\left(
\cos^2\phi_e
+
\sin^2\phi_e
\right)
```

であり、位相差に依存しない。従って、浴は不要な位相固定ポテンシャルを作らない。2系列のスペクトルが一致しない場合は、この相殺が崩れるため誤差として管理する。

## E.4 正確な記憶核と短記憶近似

準備平坦部で作用交換浴を消去すると、辺方向のトルクは

```math
\begin{aligned}
\tau_e(t)
=
{}&-
\int_0^t
K_J(t-s)
\cos
\left[
\phi_e(t)
-
\phi_e(s)
\right]
\dot\phi_e(s)
\,ds
\\
&+
\xi_e(t),
\end{aligned}
```

```math
K_J(t)
=
\sum_\alpha
\frac{
d_\alpha^2
}{
\mu_\alpha\Omega_\alpha^2
}
\cos
\left(
\Omega_\alpha t
\right)
```

となる。余弦因子は、2系列の積の和

```math
\sin\phi_e(t)
\sin\phi_e(s)
+
\cos\phi_e(t)
\cos\phi_e(s)
=
\cos
\left[
\phi_e(t)-\phi_e(s)
\right]
```

から生じる。

浴相関時間中の位相差変化が小さく、記憶核を局所化できるとき、接続行列を $B=(b_e)$、グラフ Laplacian を

```math
L_G
=
BB^{\mathsf T}
```

として、作用方程式の浴寄与は

```math
\dot{\boldsymbol J}
\simeq
-
\eta_JL_G
\dot{\boldsymbol\theta}
+
B\boldsymbol\xi.
```

これは絶対位相速度ではなく、辺に沿う相対位相速度だけへ作用する。しかし、観測中の物理的な相対位相運動も区別しないため、準備終了後には切り離す必要がある。

## E.5 固定振幅準備近似での欠陥減衰

短い準備窓で $q_i=R_i^2$ を固定し、$D_q=\operatorname{diag}(q_i)$ とする。$H_0$ の位相力と浴雑音を無視した高速部分では、全体位相速度を除いて

```math
\dot{\boldsymbol\theta}
-
\bar\omega\boldsymbol 1
=
\frac{1}{\epsilon_{\rm s}I}
D_q^{-1}
\boldsymbol{\delta J}.
```

従って、

```math
\dot{\boldsymbol{\delta J}}
=
-
\frac{
\eta_J
}{
\epsilon_{\rm s}I
}
L_GD_q^{-1}
\boldsymbol{\delta J}.
```

欠陥エネルギーを

```math
E_{\delta J}
=
\frac{1}{2\epsilon_{\rm s}I}
\boldsymbol{\delta J}^{\mathsf T}
D_q^{-1}
\boldsymbol{\delta J}
```

とすると、

```math
\frac{
dE_{\delta J}
}{
dt
}
=
-
\frac{
\eta_J
}{
\epsilon_{\rm s}^2I^2
}
\left(
D_q^{-1}
\boldsymbol{\delta J}
\right)^{\mathsf T}
L_G
\left(
D_q^{-1}
\boldsymbol{\delta J}
\right)
\leq
0.
```

グラフが連結なら $L_G$ の零空間は $\boldsymbol 1$ が張る。等号なら $D_q^{-1}\boldsymbol{\delta J}=c\boldsymbol 1$ であるが、$\sum_i\delta J_i=0$ と $\sum_iq_i=1$ から $c=0$ となる。従って、この近似の範囲では $\boldsymbol{\delta J}=0$ だけが零減衰状態である。

一般の準備運動では、

```math
\dot{\boldsymbol{\delta J}}
=
\dot{\boldsymbol J}
-
\mathcal J_\phi
\dot{\boldsymbol q}
```

であり、$H_0$ の位相力、振幅運動、有限温度雑音、記憶残差が強制項になる。従って上の単調減衰は、固定振幅・短記憶・低温の準備近似に限定される。

## E.6 有限浴、温度、切断の限界

有限 Hamiltonian 浴では永久的な不可逆減衰は起こらない。必要な観測窓は

```math
\tau_{\rm corr}
\ll
T_{\rm prep}
\ll
T_{\rm rec}.
```

$T_{\rm rec}$ より長い時間では、再位相整合とエネルギー再流入が起こり得る。反復運転では、試行後に浴を外部流路へ接続し、欠陥エネルギーを排出して浴を再初期化する必要がある。

有限温度では $\xi_i$ と $\xi_e$ が残り、欠陥は零ではなく温度依存の揺らぎ床を持つ。観測開始時の誤差には少なくとも、

```math
\varepsilon_{\rm prep}
=
\varepsilon_{\rm mem}
+
\varepsilon_T
+
\varepsilon_q
+
\varepsilon_{cs}
+
\varepsilon_{\rm cut}
+
\varepsilon_{\rm rec}
```

を含める。各項は、短記憶化、有限温度、準備中の振幅変化、余弦・正弦浴の不一致、時計窓の切断、有限浴再帰からの誤差である。

本付録は、局所作用欠陥と動径欠陥の準備を部分的に具体化する。coherent集中、$r^2=\rho$ の密度同期、単流束化、節、入口標本化後の活性場再埋め込み、観測時間に一様な欠陥上界は導かない。
