@number: I
@chapter: 付録
@title: W型2モード Hopf共同統計模型
@status: M47の基礎として、実現配置--浴共同統計、R145の開放Hopf有限時間吸引、閉鎖作用角伝播、左右占有振動、条件付き閉包、枝別matching、逆設計存在構成を詳述する。

## I.1 目的と主張範囲

本付録は、対称なW型ポテンシャルの最低2モード sectorだけを扱う。各試行で実在する基本状態は、実現配置 $X$ と浴変数 $\xi$ の組

```math
\Gamma=(X,\xi)
```

である。複素振幅は独立した物理場として追加せず、共同測度 $\mu(dX\,d\xi)$ から得る統計核がrank-oneである場合の因子として定義する。

この模型をM47と呼ぶ。M47はM42の場からrateを作るR113、M46の局所current transducerであるR133、R133を前提とするR134を使わない。Q1はM47へ移行し、第3章と付録Bで傾斜制御測定を扱う。M42と付録FはQ2・Q3の暫定操作模型としてだけ残り、M47の因果的根拠ではない。

M47で区別する導出段階は次の4つである。

| 段階 | 内容 | 状態 |
|---|---|---|
| 閉鎖bath回転 | 2作用角の古典Hamiltonian流と共分散commutator | R135、厳密 |
| W型占有振動 | rank-one統計核の密度、current、左右占有率 | R136、厳密 |
| 統計閉包 | matching多様体が閉鎖流で保存される場合の振幅方程式 | R137、条件付き |
| 共同測度の存在 | 一様ラベルと逆累積分布による決定論的古典実現 | R138、逆設計存在構成 |
| 開放bath準備 | 採用Hopf方程式の目標位相円への有限時間吸引 | R145、採用開放方程式後に厳密 |

Q1への拡張は、R139のBloch縮約、R140の傾斜制御、R141の左右占有周辺固定、R142の左右読出し、R143の局所記録instrument、R144の条件付き周期である。R139--R144の定理文と証明は第3章と付録Bへ置く。R145は、その入力となるbath方向の準備率を本付録で与える。

採用した開放Hopf方程式がbath方向を目標位相円へ吸引することはR145で有限時間評価する。一方、自然な局所Hopf--浴結合からその方程式を導くこと、実現配置周辺と条件付きbath分布を含む完全なmatching多様体を吸引すること、切断後の完全な $X$--bath流がその多様体を保存することは未導出である。この未導出部分をR135--R138、R145の厳密部分へ含めない。

R152は、固定Bell装置に限り、単一試行bath座標 $z$ に条件付けた有限W型配置jump生成子を新しい採用開放法則として置く。R153、R154は切断面と局所記録面のmatchingを有限時間で回復する。この特殊構成は、M47の一般Q1操作中にmatchingが自然保存されること、結果別測定後状態、逐次測定を導かないため、Q1-2、Q1-3の判定を変更しない。

## I.2 古典W型作用素と最低2モード

有限の対称1次元格子または有界区間上で、M37の古典振動子網から得る実対称包絡生成子を

```math
h_W
=
\frac{\mathcal J_0^2}{2m}L_W+V_W
```

とする。$L_W$ は正の離散Laplacian、$V_W$ は左右対称なW型離調である。連続表示を使う箇所では

```math
h_W
=
-\frac{\mathcal J_0^2}{2m}\partial_x^2+V_W(x),
\qquad
V_W(-x)=V_W(x)
```

と読む。この作用素は量子力学から入力するのでなく、M37の古典正常モード問題の有効生成子である。

最低2モードの単純固有対を

```math
h_W\phi_0=E_0\phi_0,
\qquad
h_W\phi_1=E_1\phi_1,
\qquad
E_0<E_1
```

とする。位相規約を選び、$\phi_0$ を実偶関数、$\phi_1$ を実奇関数、両者を規格化直交とする。2モード埋込みを

```math
\Phi c
=
c_0\phi_0+c_1\phi_1,
\qquad
c\in\mathbb C^2
```

と書く。

左井戸射影を $\Pi_L$ とし、対称性から

```math
\langle\phi_0,\Pi_L\phi_0\rangle
=
\langle\phi_1,\Pi_L\phi_1\rangle
=
\frac12
```

となる分割を採用する。井戸間重なりを

```math
B_W
=
\langle\phi_0,\Pi_L\phi_1\rangle
```

と置く。$\phi_1$ の符号を反転すれば $B_W$ の符号も反転するため、物理的内容は初期相対位相との積で決まる。

## I.3 M46から保持する補助結果

M46の三角形current模型は現行因果模型から外すが、R130--R132のうち次の有限次元計算はM47と独立に再利用できる。

### I.3.1 R130：指数capacityの無記憶性

正のcapacity $I$ が

```math
P(I>a)
=
\exp
\left(
-\frac{a}{\mathcal J_0}
\right),
\qquad
a\geq0
```

を満たすなら、$a,b\geq0$ について

```math
P(I>a+b\mid I>a)
=
P(I>b)
```

である。従って非負の消費率 $W(X_t)$ に対し、経路を固定した生存率は

```math
P
\left(
I>
\int_0^tW(X_s)\,ds
\right)
=
\exp
\left[
-\frac1{\mathcal J_0}
\int_0^tW(X_s)\,ds
\right]
```

となる。これは指数分布の補助結果であり、複素振幅、実現配置の時間発展、W型重ね合わせの準備を導かない。

### I.3.2 R131：条件付き線形半減衰

実二quadratureへ同率で作用するphase-preserving線形散逸式

```math
\dot z
=
-\frac{W}{2\mathcal J_0}z
```

を開放方程式として仮定すれば、有限時間因子は

```math
A_t
=
\exp
\left(
-\frac1{2\mathcal J_0}
\int_0^tW_s\,ds
\right)
```

であり、強度因子は $A_t^2$ となる。指数thresholdを二方向で共有するだけではこの平方根関係は出ない。R131は条件付き線形応答補題としてだけ保持し、独立した物理的複素場の存在またはM47の統計振幅を意味しない。

### I.3.3 R132：線形共分散の主モード選択

有限次元の正作用素 $S$ と独立雑音 $\eta_n$ に対し

```math
Y_{n+1}=gSY_n+\eta_n
```

とする。$g\|S\|<1$ なら定常共分散は

```math
C_g
=
\sum_{k=0}^{\infty}
g^{2k}S^kQ(S^\dagger)^k,
\qquad
Q=E[\eta_n\eta_n^\dagger]
```

である。最大固有値が単純で、雑音がその固有方向へ非零成分を持つなら、臨界側から $g\|S\|\uparrow1$ とすることで、trace規格化共分散は最大固有射影へ収束する。

この線形定理は、有限振幅Hopf飽和を持つ非線形定常測度、$X$ の周辺分布、一般複素相対位相、切断後のmatching保存を与えない。M47では準備機構を設計するための補助指針としてだけ使う。

## I.4 実現配置--浴共同統計

浴変数 $\xi$ は少なくとも二つの作用角対

```math
(I_0,\theta_0),
\qquad
(I_1,\theta_1),
\qquad
I_n\geq0
```

を含む。複素表示を

```math
Z_n(\xi)
=
\sqrt{\frac{I_n}{\mathcal J_0}}
e^{-i\theta_n}
```

とする。$Z$ は単一試行の空間波ではなく、浴作用角をまとめる記法である。

共同測度 $\mu$ から、実現配置周辺と規格化bath共分散を

```math
\rho_i[\mu]
=
\mu(X=i),
```

```math
C_{mn}[\mu]
=
\frac{
E_\mu[Z_mZ_n^*]
}{
E_\mu[Z^\dagger Z]
}
```

と定める。分母は正とする。$C$ はHermitian、正半定値、trace 1である。

2モード空間核を

```math
K_W[\mu]
=
\Phi C[\mu]\Phi^\dagger
```

とする。有限格子では

```math
K_{W,ij}[\mu]
=
\sum_{m,n=0}^1
\phi_m(i)C_{mn}[\mu]\phi_n(j)
```

である。

### I.4.1 matching多様体

M47のmatching多様体を

```math
\mathcal M_W
=
\left\{
\mu:
\operatorname{rank}C[\mu]=1,
\quad
\rho_i[\mu]=K_{W,ii}[\mu]
\right\}
```

と定める。$\mu\in\mathcal M_W$ なら、ある規格化 $c\in\mathbb C^2$ が存在して

```math
C[\mu]=cc^\dagger,
\qquad
K_W[\mu]=|\Phi c\rangle\langle\Phi c|
```

となる。このとき

```math
\psi_W^{\rm stat}[\mu]
=
\Phi c
```

を統計的複素振幅と呼ぶ。$c$ と $e^{i\alpha}c$ は同じ $C$ を与えるため、$\psi_W^{\rm stat}$ は共通位相を除いて一意である。

重要なのは、$C$ だけでなく

```math
\rho_i[\mu]
=
|\psi_{W,i}^{\rm stat}[\mu]|^2
```

を同時に要求することである。振幅の大きさは実現配置周辺、相対位相はbath共分散から読み、両者が同じ共同測度の上で一致した場合にだけ複素振幅を定義する。独立場を追加してから $X$ を従わせる定義ではない。

rankが1より大きい場合、$K_W$ は混合統計核であり、単一の $\psi_W^{\rm stat}$ を定義しない。対角だけが一致しても非対角位相相関は決まらず、matchingとは呼ばない。

### I.4.2 枝別matching

測定記録を $R$、安全結果を $s$ とする。結果枝の非規格化共分散を

```math
\widetilde C_s
=
\frac{
E_\mu
\left[
\mathbf1_{R=s}ZZ^\dagger
\right]
}{
E_\mu[Z^\dagger Z]
}
```

とする。$p_s=\operatorname{tr}\widetilde C_s>0$ なら $C_s=\widetilde C_s/p_s$ が条件付き共分散である。射影測定後状態には、大域条件 $C=cc^\dagger$ だけでなく

```math
\widetilde C_s^{\rm out}
\simeq
p_s\Pi_s
```

という枝別条件が必要である。大域階数1条件は、結果で条件付けただけでは異なる2つの $\Pi_s$ を作らない。第3章のR143は、左右実現配置の局所記録と結果別テンプレート交換を明示して、この枝別条件を有限誤差で構成する。ただし、その前提となる分析器終了時のmatchingと、記録中に単一試行の $X$ が安全井戸へ滞在する経路上界は仮定として残る。

## I.5 外部制御された開放Hopf準備

準備段階と伝播段階は外部制御 $\lambda_{\rm prep}(t)$ で切り替える。内部latchまたは反応座標 $s$ を切替器に使わない。

```math
\lambda_{\rm prep}(t)>0
```

では、M47はreservoir、能動供給、散逸、必要なら外部位相基準へ接続された開放系である。

```math
\lambda_{\rm prep}(t)=0
```

では、これらの準備portを切り、二作用角と残存bath自由度を閉鎖Hamiltonian流で発展させる。切替時に外部制御が仕事または相関を交換し得るため、全周期を自律閉鎖系とは呼ばない。

### I.5.1 理想開放方程式

2モード対角行列を

```math
D_W
=
\begin{pmatrix}
E_0&0\\
0&E_1
\end{pmatrix}
```

とする。準備したい規格化係数を $c_*$ とし、閉鎖回転軌道と射影を

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

と置く。理想化したbath包絡 $z\in\mathbb C^2$ の開放方程式を

```math
\dot z
=
-\frac{i}{\mathcal J_0}D_Wz
+
\lambda_{\rm prep}(t)
\left[
g(1-z^\dagger z)z
-
\kappa
\left(
I_2-\Pi_*(t)
\right)z
\right]
+
\lambda_{\rm prep}(t)\eta_t
```

とする。$g>0$ はHopf型動径供給と飽和、$\kappa>0$ は目標2モード方向から外れた成分の散逸、$\eta_t$ は開放portの雑音である。

雑音を零とし、回転座標

```math
\widetilde z(t)
=
\exp
\left[
\frac{iD_W(t-t_*)}{\mathcal J_0}
\right]z(t)
```

へ移ると、$\lambda_{\rm prep}$ が一定の区間では

```math
\dot{\widetilde z}
=
\lambda_{\rm prep}
\left[
g(1-\widetilde z^\dagger\widetilde z)\widetilde z
-
\kappa(I_2-\Pi_*)\widetilde z
\right]
```

となる。$\Pi_*=c_*c_*^\dagger$ である。$g,\kappa>0$ とし、初期値が $c_*$ 方向へ非零成分を持てば、直交成分は減衰し、動径は1へ近づく。$\kappa>g$ は不要である。共通位相方向は中立なので、吸引集合は1点でなく

```math
\left\{
e^{i\alpha}c_*(t):
\alpha\in[0,2\pi)
\right\}
```

という回転軌道である。

この方程式は、開放Hopf準備がどの構造を持てばよいかを示す採用有効式である。M45の局所 $(s,r)$ Langevin方程式または具体的負性抵抗回路から、$\Pi_*(t)$、$g$、$\kappa$、雑音共分散を導いた結果ではない。

### I.5.2 位相基準の必要性

自律Hopf limit cycleだけを各試行で独立に準備すると、共通位相は不要でも、2モード間の相対位相または切断時の位相が試行ごとに散る可能性がある。W型左右占有振動を同じ時刻原点で観測するには、準備中に次のいずれかが必要である。

1. 2モードが共有する外部pump位相。
2. 外部clockに同期した切断時刻。
3. 二作用角間の明示的な位相固定結合。
4. 同じ役割を持つ自律な参照自由度を含む拡大開放系。

M47は外部制御 $\lambda_{\rm prep}(t)$ を許すため、最小構成では1または2を採用する。外部位相基準を使ったことを自律的な相対位相生成とは呼ばない。

### I.5.3 準備の真の目標

$z$ の方向だけを揃えても、共同測度 $\mu$ が $\mathcal M_W$ へ入るとは限らない。必要なのは同時に

```math
\operatorname{rank}C[\mu]
\simeq1,
\qquad
\rho_i[\mu]
\simeq K_{W,ii}[\mu]
```

を満たし、切断後の未来を決める条件付きbath変数も同じmatching fiberへ入ることである。$X$ 周辺、bath共分散、条件付きbath分布を同時に準備する定理は未完成である。

### I.5.4 R145：単一Hopf準備の厳密解

雑音を零とし、有効準備時間を

```math
\tau(t)
=
\int_{t_*}^{t}
\lambda_{\rm prep}(s)\,\mathrm{d}s
```

とする。回転座標の状態を

```math
\widetilde z
=
a c_*+p,
\qquad
c_*^\dagger p
=
0
```

と分解する。開放方程式は

```math
\frac{da}{d\tau}
=
g
\left(
1-\|\widetilde z\|^2
\right)a,
```

```math
\frac{dp}{d\tau}
=
\left[
g
\left(
1-\|\widetilde z\|^2
\right)
-\kappa
\right]p
```

となる。$a_0=a(0)\neq0$ とし、

```math
q_0
=
\frac{\|p_0\|^2}{|a_0|^2},
\qquad
y
=
\frac{1}{|a|^2},
\qquad
y_0
=
\frac{1}{|a_0|^2}
```

と置く。2式の比から

```math
\frac{\|p(\tau)\|}{|a(\tau)|}
=
\frac{\|p_0\|}{|a_0|}
e^{-\kappa\tau}
```

を得る。$y$ は線形方程式を満たし、$\kappa\neq g$ では

```math
y(\tau)
=
1
+
(y_0-1)e^{-2g\tau}
+
\frac{gq_0}{g-\kappa}
\left(
e^{-2\kappa\tau}
-e^{-2g\tau}
\right),
```

$\kappa=g$ では

```math
y(\tau)
=
1
+
(y_0-1)e^{-2g\tau}
+
2gq_0\tau e^{-2g\tau}
```

である。

<!-- theorem-start:theorem -->
**定理（R145：M47単一Hopf準備の吸引位相円と有限時間率）**

$g,\kappa>0$、$a_0\neq0$ とする。雑音零の採用開放方程式では、上の厳密解が成り立ち、

```math
\widetilde z(\tau)
\longrightarrow
e^{i\arg a_0}c_*
```

である。$|a_0|\geq a_*>0$、$\|\widetilde z_0\|\leq R_*<\infty$ を満たす有界seed集合では、ある明示定数 $K_{47}(a_*,R_*,g,\kappa)<\infty$ が存在して

```math
\operatorname{dist}
\left(
\widetilde z(\tau),
\left\{
e^{i\alpha}c_*:
\alpha\in[0,2\pi)
\right\}
\right)
\leq
K_{47}e^{-\gamma_{47}\tau},
```

```math
\gamma_{47}
=
\min\{2g,\kappa\}
```

を得る。同じseed境界を持つ共同測度について、規格化bath共分散を $C_z(\tau)$ とすれば

```math
\left\|
C_z(\tau)-c_*c_*^\dagger
\right\|_1
\leq
K_Ce^{-\gamma_{47}\tau}
```

となる有限定数 $K_C$ を選べる。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**

$a$ と $p$ の方程式を割ると $p/a=(p_0/a_0)e^{-\kappa\tau}$ を得る。従って

```math
\frac{dy}{d\tau}
+
2gy
=
2g
\left(
1+q_0e^{-2\kappa\tau}
\right).
```

積分因子を使えば上の2つの $y$ の式が従う。$y\to1$、$p/a\to0$ なので位相円へ収束する。$\kappa\neq g$ では表示式の各指数を比較する。$\kappa=g$ では $\tau e^{-2g\tau}$ が $e^{-g\tau}$ の定数倍で抑えられる。seed集合上で $q_0$ と $y_0$ は一様有界なので距離上界を得る。$\widetilde z\widetilde z^\dagger$ の一様収束を共同測度で平均し、分母 $\mathbb E[\widetilde z^\dagger\widetilde z]$ が十分大きい $\tau$ で零から離れることを使えば共分散上界が従う。有限初期区間は定数へ吸収できる。証明終。
<!-- theorem-end:proof -->

### I.5.5 seed条件、雑音、準備誤差の境界

$a_0=0$ の直交超平面は不変であり、R145の目標位相円へ入らない。従って非零seed条件は必要である。共同測度がこの超平面へ正の質量を持つ場合、その質量を無反応またはseed失敗誤差として完全結果集合へ残す。

R145は $\eta_t=0$ の決定論的方程式に対する定理である。雑音付き定常測度、位相拡散、盆横断率は導いていない。準備誤差を

```math
\varepsilon_{\rm prep}
=
\varepsilon_{\rm Hopf}
+
\varepsilon_{\rm Xmatch}
+
\varepsilon_{\rm cond}
+
\varepsilon_{\rm cut}
```

と分ける。$\varepsilon_{\rm Hopf}$ のbath方向部分はR145で有限時間評価できる。実現配置周辺、条件付きbath fiber、切断残差は別項であり、R145からは従わない。

## I.6 閉鎖作用角Hamiltonian

切断時刻を $t_0$ とし、$t\geq t_0$ で

```math
\lambda_{\rm prep}(t)=0
```

とする。二作用角sectorの古典Hamiltonianを

```math
H_{\rm rot}
=
\sum_{n=0}^1
\frac{E_n}{\mathcal J_0}I_n
```

とする。正準関係 $\{\theta_n,I_m\}=\delta_{nm}$ から

```math
\dot I_n=0,
\qquad
\dot\theta_n
=
\frac{E_n}{\mathcal J_0}
```

を得る。従って

```math
Z_n(t)
=
e^{-iE_n(t-t_0)/\mathcal J_0}Z_n(t_0)
```

である。これは二つの古典rotorのHamilton方程式であり、Schrödinger方程式を運動方程式として入力していない。

第3章では、この対角生成子を一般のHermitian2モード生成子 $G(t)$ へ拡張し、$H_G=Z^\dagger GZ$ から $i\mathcal J_0\dot C=[G,C]$ を得る。W型へ1次傾斜を加えると、局在基底で $G=-J\sigma_x+\varepsilon(t)\sigma_z/2$ となる。これはM47の統計共分散を操作する古典正準Hamiltonianであり、M42の複素振幅場を追加するものではない。

## I.7 R135：bath共分散の厳密回転

<!-- theorem-start:theorem -->
**定理（R135：古典作用角共分散のcommutator回転）**

$t\geq t_0$ で二作用角が $H_{\rm rot}$ に従い、$E[Z^\dagger Z]>0$ とする。このとき規格化bath共分散は

```math
i\mathcal J_0\dot C
=
[D_W,C]
```

を満たす。trace、正値性、rankは保存される。特に

```math
C(t_0)=c_0c_0^\dagger
```

なら

```math
C(t)=c(t)c(t)^\dagger,
\qquad
c(t)
=
\exp
\left[
-\frac{iD_W(t-t_0)}{\mathcal J_0}
\right]c_0
```

である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**

各試行で $Z(t)=U(t)Z(t_0)$、

```math
U(t)
=
\exp
\left[
-\frac{iD_W(t-t_0)}{\mathcal J_0}
\right]
```

である。$U$ はunitaryであるため分母 $E[Z^\dagger Z]$ は一定で、

```math
C(t)=U(t)C(t_0)U(t)^\dagger
```

となる。微分すればcommutator式を得る。unitary共役はtrace、正値性、rankを保存する。rank-oneの場合は $c(t)=U(t)c_0$ を選べる。証明終。
<!-- theorem-end:proof -->

空間核は

```math
K_W(t)
=
\Phi U(t)C(t_0)U(t)^\dagger\Phi^\dagger
```

と回転する。rank-one因子については

```math
i\mathcal J_0\partial_t\psi_W^{\rm stat}
=
h_W\psi_W^{\rm stat}
```

が2モード sectorで代数的に成り立つ。この式は古典作用角流から導いた統計因子の式であり、$X$ 周辺がその対角へ追随することはR135だけからは従わない。

## I.8 R136：W型左右占有振動

rank-one係数を

```math
c(t_0)
=
\begin{pmatrix}
a_0e^{-i\theta_0(t_0)}\\
a_1e^{-i\theta_1(t_0)}
\end{pmatrix},
\qquad
a_0,a_1\geq0,
\qquad
a_0^2+a_1^2=1
```

とする。相対角を

```math
\delta(t)
=
\theta_1(t)-\theta_0(t)
```

とすれば

```math
\delta(t)
=
\delta(t_0)
+
\frac{E_1-E_0}{\mathcal J_0}(t-t_0)
```

である。

<!-- theorem-start:theorem -->
**定理（R136：W型2モード共同統計の占有振動）**

$\mu_t\in\mathcal M_W$ がR135のrank-one共分散を持つとする。このとき実現配置密度は

```math
\rho(x,t)
=
a_0^2\phi_0(x)^2
+
a_1^2\phi_1(x)^2
+
2a_0a_1\phi_0(x)\phi_1(x)\cos\delta(t)
```

である。左井戸占有率は

```math
P_L(t)
=
\frac12
+
2a_0a_1B_W\cos\delta(t)
```

となる。等重み $a_0=a_1=1/\sqrt2$ では

```math
P_L(t)
=
\frac12
+
B_W
\cos
\left[
\delta(t_0)
+
\frac{E_1-E_0}{\mathcal J_0}(t-t_0)
\right].
```

従って振動角周波数と周期は

```math
\Omega_W
=
\frac{E_1-E_0}{\mathcal J_0},
\qquad
T_W
=
\frac{2\pi\mathcal J_0}{E_1-E_0}
```

である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**

R135のrank-one因子を

```math
\psi_W^{\rm stat}(x,t)
=
a_0\phi_0(x)e^{-i\theta_0(t)}
+
a_1\phi_1(x)e^{-i\theta_1(t)}
```

と選ぶ。$\rho=|\psi_W^{\rm stat}|^2$ を展開すれば密度式を得る。左井戸積分では二つの対角項がそれぞれ $1/2$ を与え、交差項が $2a_0a_1B_W\cos\delta$ を与える。相対角の式を代入すれば周期式を得る。証明終。
<!-- theorem-end:proof -->

### I.8.1 currentと連続方程式

連続表示では

```math
j(x,t)
=
\frac{\mathcal J_0}{m}
\operatorname{Im}
\left[
(\psi_W^{\rm stat})^*
\partial_x\psi_W^{\rm stat}
\right]
```

と置くと

```math
j(x,t)
=
\frac{\mathcal J_0}{m}
a_0a_1
\left[
\phi_1\partial_x\phi_0
-
\phi_0\partial_x\phi_1
\right]
\sin\delta(t)
```

である。固有方程式から

```math
\partial_x
\left[
\phi_1\partial_x\phi_0
-
\phi_0\partial_x\phi_1
\right]
=
\frac{2m(E_1-E_0)}{\mathcal J_0^2}
\phi_0\phi_1
```

を得るため、直接微分して

```math
\partial_t\rho+\partial_xj=0
```

が成り立つ。ここでcurrentは統計核から計算する縮約量であり、局所比較器でrateへ変換しない。

### I.8.2 固有状態との違い

$a_1=0$ または $a_0=0$ なら交差項が消え、密度は定常である。基底状態または第1励起状態だけの準備では、閉鎖伝播の非自明な検査にならない。$a_0a_1B_W\neq0$ の重ね合わせでは相対角が観測可能な左右占有振動へ変換されるため、閉鎖伝播の中心検査になる。

## I.9 R137：条件付き統計閉包

R135はbath共分散を閉じるが、実現配置周辺の未来を単独では決めない。そこで完全な古典流を $F_t$、共同測度の押出しを

```math
\mu_t=(F_t)_\#\mu_{t_0}
```

とする。

<!-- theorem-start:theorem -->
**定理（R137：matching保存を仮定したW型統計閉包）**

次を仮定する。

1. $\mu_{t_0}\in\mathcal M_W$ である。
2. $t\geq t_0$ では $\lambda_{\rm prep}=0$ であり、bath作用角は $H_{\rm rot}$ に従う。
3. 完全な閉鎖古典流が観測時間 $0\leq t-t_0\leq T$ でmatching多様体を保存する。

```math
(F_t)_\#\mathcal M_W
\subseteq
\mathcal M_W
```

4. 2モード外への漏れと切断後の散逸、雑音、記憶項がない。

このとき $\psi_W^{\rm stat}[\mu_t]$ は共通位相規約を選べば

```math
i\mathcal J_0\partial_t\psi_W^{\rm stat}
=
h_W\psi_W^{\rm stat}
```

を満たし、実現配置周辺は

```math
P_{\mu_t}(X=i)
=
|\psi_{W,i}^{\rm stat}(t)|^2
```

を保つ。左右占有率はR136の周期式に従う。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**

仮定2からR135により $C(t)=U(t)C(t_0)U(t)^\dagger$ である。仮定1と3から全時刻でrank-one性と $\rho_i=K_{W,ii}$ が保たれる。rank-one因子を $c(t)=U(t)c(t_0)$ と選べば、$\psi_W^{\rm stat}=\Phi c$ は2モード生成子式を満たす。対角matchingから実現配置周辺がその絶対値二乗に一致し、R136を適用できる。証明終。
<!-- theorem-end:proof -->

この定理の中心仮定は3である。同じ初期 $\rho$ と $C$ を持っても、条件付きbath分布、対称活動度、切断時の残留相関が異なれば未来は異なり得る。M47の自然な局所ミクロ方程式から仮定3を証明することが、統計閉包問題の未解決部分である。

## I.10 誤差付き有限時間形

理想matchingからのずれを

```math
\varepsilon_{\rm rank}(t)
=
\inf_{\operatorname{rank}P=1}
\|C(t)-P\|_1,
```

```math
\varepsilon_{\rm diag}(t)
=
\sum_i
\left|
\rho_i(t)-K_{W,ii}(t)
\right|
```

とする。さらに2モード漏れ、bath記憶、切断残差をそれぞれ

```math
\varepsilon_{\rm leak},
\qquad
\varepsilon_{\rm mem},
\qquad
\varepsilon_{\rm cut}
```

とする。有限時間近似定理の目標形は

```math
\sup_{0\leq t-t_0\leq T}
\left|
i\mathcal J_0\partial_t\psi_W^{\rm stat}
-
h_W\psi_W^{\rm stat}
\right|
\leq
C_T
\left(
\varepsilon_{\rm prep}
+
\varepsilon_{\rm rank}
+
\varepsilon_{\rm diag}
+
\varepsilon_{\rm leak}
+
\varepsilon_{\rm mem}
+
\varepsilon_{\rm cut}
\right)
```

である。本稿では右辺の誤差を同じ局所Hopf--bathパラメータから評価していないため、この不等式をR137の証明済み結論には含めない。

R145により、雑音零の採用開放方程式については $\varepsilon_{\rm Hopf}$ のbath方向成分を $K_Ce^{-\gamma_{47}\tau_{\rm p}}$ で評価できる。ただし

```math
\varepsilon_{\rm prep}
=
\varepsilon_{\rm Hopf}
+
\varepsilon_{\rm Xmatch}
+
\varepsilon_{\rm cond}
+
\varepsilon_{\rm cut}
```

の残り3項は同じ定理で閉じない。従ってR137の中心仮定である完全matching保存は未解決のままである。

## I.11 R138：逆設計による古典共同測度の存在

R137の仮定3が論理的に矛盾しないことは、局所性を要求しない逆設計構成で確認できる。

有限配置集合を順序付け、R135から得る正規化密度を $\rho_i(t)$ とする。一様な古典ラベル

```math
U\in[0,1),
\qquad
P(U<u)=u
```

を導入し、累積境界を

```math
F_k(t)
=
\sum_{i\leq k}\rho_i(t)
```

とする。実現配置を

```math
X_t
=
\min
\left\{
k:
U<F_k(t)
\right\}
```

で定める。

<!-- theorem-start:theorem -->
**定理（R138：逆累積分布による決定論的古典実現）**

$U$ が一様でbath初期状態と所定の共同分布を持ち、bath作用角が $H_{\rm rot}$ に従うとする。このとき上の $X_t$ は各時刻で

```math
P(X_t=i)=\rho_i(t)
```

を満たす。$U$ を角座標、その共役作用を保存量とする自明なHamiltoniansectorへ埋め込めば、全入力変数は古典正準変数として持ち上げられる。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**

$X_t=i$ は

```math
F_{i-1}(t)
\leq U<F_i(t)
```

と同値である。一様性からこの区間の測度は $F_i-F_{i-1}=\rho_i$ である。証明終。
<!-- theorem-end:proof -->

R138は存在証明であって、自然な局所運動則の導出ではない。境界 $F_i(t)$ はR135で先に得た全密度を使うため、これをHopf装置のミクロ説明として採用すると逆設計になる。また、$X_t$ は境界通過時に区分的に変化し、局所慣性軌道、有限伝播速度、bath反作用を自動的に持たない。従ってR138をM47の自然実装またはR137仮定3の物理的証明とは呼ばない。

## I.12 M42およびM46との境界

M42では、物理的複素振幅場 $b$ を先に置き、その辺流から最小rateを定めて $X$ を更新する。M46のR133は別の対称往復流を持つcurrent rateを $b$ から作る。どちらも因果の向きは

```math
b
\longrightarrow
q(b)
\longrightarrow
X
```

である。

M47では

```math
\mu(dX\,d\xi)
\longrightarrow
(\rho,C)
\longrightarrow
K_W
\longrightarrow
\psi_W^{\rm stat}
```

であり、$\psi_W^{\rm stat}$ は共同統計の後に定義される。従ってR113またはR133をM47へ混ぜない。

Q1はM47の傾斜制御と局所記録へ移行した。M42/R113はQ2の共同配置とQ3の固定時刻位置読出しだけに暫定保持する。M42をM47の基礎、W型統計閉包の証拠、transducerなし模型の実装とは扱わない。全面退役には、Q2の共同配置とQ3の位置読出しをM47型共同統計から再導出する必要がある。

## I.13 反証条件と未導出事項

M47の主張は次の条件で縮小または撤回する。

1. 古典作用角HamiltonianからR135のcommutator式が得られない。
2. rank-one共分散またはtraceが閉鎖回転で保存されない。
3. W型偶奇2モードの交差項がR136の密度または左右占有率と一致しない。
4. $\mu\in\mathcal M_W$ としたにもかかわらず $P(X=i)=K_{W,ii}$ が破れる。
5. 切断後に準備散逸、雑音、位相固定、bath記憶が同じ次数で残る。
6. 2モード外への漏れが観測時間内で無視できない。
7. 開放Hopf方程式が目標回転軌道へ吸引せず、相対位相が試行間で拡散する。
8. matching条件を目的密度の直接入力だけで満たし、それを自然な導出と呼ぶ。
9. 大域階数1共分散だけを、結果枝ごとの測定後固有状態と同一視する。
10. 傾斜による離調固定をZeno効果と呼ぶ。

現在の未導出事項は次の通りである。

1. M45または具体的負性抵抗回路からI.5の2モード開放方程式を導くこと。
2. R145のbath方向吸引に加え、$X$ 周辺、条件付きbath分布を同時に $\mathcal M_W$ へ吸引すること。
3. 切断時の外部仕事、残留相関、bath記憶を評価すること。
4. 閉鎖した局所古典流がmatching fiberを有限時間ほぼ保存すること。
5. 逆累積分布によらない局所的な実現配置軌道を作ること。
6. W型最低2モードを越える一般ポテンシャル、多モード、node、連続空間一様極限へ拡張すること。
7. 傾斜切替中の局所実現配置保持と枝別matchingを同じミクロ流から一様に導くこと。
8. R144の周期間matching帰還と開放準備の総エネルギー・エントロピー収支を閉じること。

従って、M47が解析的に確立する中心は、採用開放Hopf方程式がbath方向を有限時間で階数1位相円へ準備すること、古典作用角回転がその統計核の相対位相を回すこと、matching条件下でW型左右占有分布を周期振動させることである。開放準備から実現配置周辺と条件付きbath fiberまで含む完全matchingを自然に作る部分は、次の中心定理として残る。
