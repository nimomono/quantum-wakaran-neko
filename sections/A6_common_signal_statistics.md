@number: F
@chapter: 付録
@title: 共通信号集団と状態方向平均の証明
@status: 共通R135の正確輸送、有限時間誤差、階数1支持と、一般状態方向平均定理R168を証明する。Q3ではM37包絡誤差をR135へ代入する統計診断として扱い、単一試行の物理結果形成はQ1/Q2のM65またはQ3のM64へ委ねる。

## F.1 共通信号集団と受渡し契約

有限試行空間を $(\mathcal P,\mu)$、M37局所包絡を

```math
Z_t(\omega)=b(t;\omega)\in\mathbb C^L
```

とする。全ての期待値は $\mu$ に関して取る。有限で正の集団作用

```math
S_t=\mathbb E[Z_t^\dagger Z_t]
```

を仮定し、

```math
C_Z(t)
=
\frac{\mathbb E[Z_tZ_t^\dagger]}{S_t}
```

と置く。$C_Z$ は集団の自己共分散であり、M54静的状態構成へ直接入力する物理変数ではない。M54静的状態構成へ渡すのは、入力標本時刻 $t_\star$ に各試行が持つ $Z_{t_\star}(\omega)$ またはその正準コピーである。

ここで自己共分散は非中心化された規格化第2モーメントを指す。$\mathbb E[Z_t]=0$ を追加した場合にだけ、通常の中心化共分散と比例して一致する。以下の支持証明に中心化共分散だけを代入してはならない。

R135とR168は集団統計を評価する定理であり、それ自体は単一試行の排他的結果を生成しない。Q1/Q2の結果形成はM65、Q3の位置過程と終位置読出しはM64/R203が担う。

## F.2 R135の有限時間誤差節の証明

理想有効発展を

```math
U_L(t)=\exp\left(-ih_Lt/\mathcal J_0\right),
\qquad
\widetilde Z_t=U_L(t)\widetilde Z_0
```

とする。$U_L$ はユニタリなので

```math
\widetilde S_0
=
\mathbb E\|\widetilde Z_t\|^2
=
\mathbb E\|\widetilde Z_0\|^2
```

は時間に依存しない。誤差標本を

```math
D_t=Z_t-\widetilde Z_t
```

と書く。R86の一様包絡評価から

```math
d_t
:=
\mathbb E\|D_t\|^2
\leq
\varepsilon_{\rm car}(T)^2\widetilde S_0
```

である。

任意の $x,y\in\mathbb C^L$ について、$d=x-y$ と書けば

```math
xx^\dagger-yy^\dagger
=
xd^\dagger+dx^\dagger-dd^\dagger
```

である。階数1作用素のトレースノルムが

```math
\|uv^\dagger\|_1=\|u\|\|v\|
```

であることから

```math
\|xx^\dagger-yy^\dagger\|_1
\leq
2\|x\|\|d\|+\|d\|^2
```

を得る。$x=Z_t$、$y=\widetilde Z_t$ とし、Cauchy--Schwarz不等式を使うと、非規格化第2モーメント

```math
A_t=\mathbb E[Z_tZ_t^\dagger],
\qquad
B_t=\mathbb E[\widetilde Z_t\widetilde Z_t^\dagger]
```

について

```math
\|A_t-B_t\|_1
\leq
2\sqrt{S_td_t}+d_t
```

である。

正半定値作用素 $A,B$、$a=\operatorname{tr}A>0$、$b=\operatorname{tr}B>0$ について

```math
\frac12
\left\|
\frac{A}{a}-\frac{B}{b}
\right\|_1
\leq
\frac{\|A-B\|_1}{a}
```

が成り立つ。実際、三角不等式と

```math
|a-b|
\leq
\|A-B\|_1
```

を使えばよい。従って

```math
D_{\rm tr}
\left(
C_Z(t),
\frac{B_t}{\widetilde S_0}
\right)
\leq
2\sqrt{\frac{d_t}{S_t}}
+\frac{d_t}{S_t}.
```

$B_t/\widetilde S_0=U_L(t)C_{\widetilde Z}(0)U_L(t)^\dagger$ である。同じ初期集団を使い $C_{\widetilde Z}(0)=C_Z(0)$ とし、

```math
\kappa_T
=
\sup_{0\leq t\leq T}
\frac{\widetilde S_0}{S_t}
```

と置けば

```math
D_{\rm tr}
\left(
C_Z(t),
U_L(t)C_Z(0)U_L(t)^\dagger
\right)
\leq
2\varepsilon_{\rm car}(T)\sqrt{\kappa_T}
+\varepsilon_{\rm car}(T)^2\kappa_T.
```

トレース距離は1以下なので右辺を1で切ってよい。$S_0=\widetilde S_0$ かつ局所--正常モード変換が

```math
\|Z_t\|
\geq
(1-\delta_{\rm loc})\|\widetilde Z_t\|
```

を与えるなら $\kappa_T\leq(1-\delta_{\rm loc})^{-2}$ である。従って

```math
q_T
=
\frac{\varepsilon_{\rm car}(T)}{1-\delta_{\rm loc}},
\qquad
r_T\leq2q_T+q_T^2
```

となる。これでR135の有限時間誤差節を得る。正確なユニタリ輸送は $Z_t=U(t)Z_0$ を第2モーメントへ代入して直ちに従う。

## F.3 R168の階数1節の証明

$C_Z(t_\star)=c_\star c_\star^\dagger$、$\|c_\star\|=1$ とする。直交射影 $P_\star^\perp=I-c_\star c_\star^\dagger$ に対して

```math
\frac{\mathbb E\|P_\star^\perp Z_{t_\star}\|^2}{S_{t_\star}}
=
\operatorname{tr}
\left(P_\star^\perp C_Z(t_\star)\right)
=0
```

である。非負確率変数の期待値が零なので

```math
Z_{t_\star}(\omega)
=
\alpha(\omega)c_\star
```

がほとんど確実に成り立つ。安全試行では $\alpha\neq0$ なので、M54静的状態構成の状態方向重みは

```math
w_i\left(Z_{t_\star}\right)
=
\frac{|(\Psi Z_{t_\star})_i|^2}{Z_{t_\star}^\dagger Z_{t_\star}}
=
|(\Psi c_\star)_i|^2
```

である。従って

```math
\pi_i^\delta\left(Z_{t_\star}\right)
=
\frac{|(\Psi c_\star)_i|^2+\delta q_i}{1+\delta}
```

となる。

近似状態方向を単位ベクトル $\widehat z$、目標状態方向を $c$ とする。純粋状態トレース距離を

```math
s
=
D_{\rm tr}
\left(
\widehat z\widehat z^\dagger,
cc^\dagger
\right)
```

と置く。$M_i=\Psi^\dagger|i\rangle\langle i|\Psi$ は1つの有限結果測定を定めるため、トレース距離の縮約性から

```math
D_{\rm TV}
\left(w(\widehat z),w(c)\right)
\leq s.
```

正則化は両分布へ同じ $q$ を混ぜるので

```math
D_{\rm TV}
\left(
\pi^\delta(\widehat z),
\pi^\delta(c)
\right)
=
\frac{1}{1+\delta}
D_{\rm TV}
\left(w(\widehat z),w(c)\right)
\leq
\frac{s}{1+\delta}.
```

R135のベクトル誤差から直接状態方向誤差を作る場合、目標状態方向を $c$ とし、適切な同位相・同尺度の代表に対して $\|z-c\|\leq q_T<1$ なら

```math
\frac{\|(I-cc^\dagger)z\|}{\|z\|}
\leq
\frac{q_T}{1-q_T}
```

である。左辺は $z$ と $c$ の純粋状態トレース距離なので、$\rho_T=q_T/(1-q_T)$ を使える。同じ $q_T$ をR135のトレース誤差とR168の状態方向誤差の双方へ加算してはならない。これでR168を得る。

## F.4 R168の一般状態方向平均、固定作用節、可変作用反例

安全事象 $G$ を固定し、安全状態方向平均を

```math
R_Z^G
=
\mathbb E
\left[
\mathbf1_G
\frac{ZZ^\dagger}{Z^\dagger Z}
\right]
```

と置く。M54静的状態構成の結果成分平均は線形性から

```math
P(i)
=
\frac{\operatorname{tr}(M_iR_Z^G)+\delta q_iP(G)}{1+\delta},
\qquad
P(\varnothing)=P(G^c)
```

である。次に $P(G)=1$ かつ $S(\omega)=Z_{t_\star}(\omega)^\dagger Z_{t_\star}(\omega)=s_*$ がほとんど確実に成り立つとする。$M_i=\Psi^\dagger|i\rangle\langle i|\Psi$ に対し

```math
\mathbb E[w_i(Z)]
=
\mathbb E
\left[
\frac{Z^\dagger M_iZ}{s_*}
\right]
=
\operatorname{tr}
\left(
M_i
\frac{\mathbb E[ZZ^\dagger]}{s_*}
\right)
=
\operatorname{tr}(M_iC_Z).
```

正則化項を加えると

```math
\mathbb E[\pi_i^\delta(Z)]
=
\frac{\operatorname{tr}(M_iC_Z)+\delta q_i}{1+\delta}.
```

これは固定作用面で $R_Z^G=C_Z$ となること、従って各試行で状態方向規格化してから平均する操作と、集団第2モーメントを規格化してから結果成分射影を取る操作が可換であることを示す。

固定作用を外すと一般には可換しない。2次元で、確率 $1/2$ ずつ

```math
Z=\sqrt3e_1,
\qquad
Z=e_2
```

を取る集団を考える。試行ごとの状態方向平均は

```math
R_Z
=
\mathbb E
\left[
\frac{ZZ^\dagger}{Z^\dagger Z}
\right]
=
\begin{pmatrix}
1/2&0\\
0&1/2
\end{pmatrix},
```

一方、規格化共分散は

```math
C_Z
=
\frac{\mathbb E[ZZ^\dagger]}{\mathbb E[Z^\dagger Z]}
=
\begin{pmatrix}
3/4&0\\
0&1/4
\end{pmatrix}
```

である。従って高階数公式を可変作用集団へ無条件に拡張できない。

一般の正の作用変数 $S=Z^\dagger Z$ と $\overline S=\mathbb E[S]$ について

```math
R_Z-C_Z
=
\mathbb E
\left[
\left(
\frac1S-\frac1{\overline S}
\right)
ZZ^\dagger
\right].
```

$\|ZZ^\dagger\|_1=S$ なので

```math
D_{\rm tr}(R_Z,C_Z)
\leq
\frac12
\mathbb E
\left|
\frac{S}{\overline S}-1
\right|
\leq
\frac12
\frac{\sqrt{\operatorname{Var}S}}{\overline S}.
```

最後はCauchy--Schwarz不等式である。結果成分射影とM54静的状態構成正則化を通した全変動距離は

```math
D_{\rm TV}
\leq
\frac{1}{1+\delta}
D_{\rm tr}(R_Z,C_Z)
```

で抑えられる。これでR168の固定作用節、可変作用反例、半径方向補正を得る。階数1ならF.3により $R_Z^G=P(G)c_\star c_\star^\dagger$ である。

## F.5 制御されたM37の共通位相と階数1診断

M37の局所包絡は共役成分を含む実線形発展である。一般には $b(t;e^{i\alpha}b_0)=e^{i\alpha}b(t;b_0)$ は厳密には成り立たない。従って初期 $Z_0=\alpha c$ の階数1集団に対して、局所包絡の第2モーメントが厳密に階数1を保つとは主張しない。

第6.17節の入力一様な相対誤差をF.2の二乗平均誤差へ代入すれば、有効ユニタリ輸送からの偏差をR135で抑えられる。別の方法として安全作用下で試行ごとの方向誤差をR168へ直接渡してよい。同じ偏差を両経路の和として数えない。局所作用は実際の読出し入口で評価し、射影後の成功試行だけを再規格化しない。M37の共通位相依存は制御精度の検査対象であり、新しい確率源ではない。
