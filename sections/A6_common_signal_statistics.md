@number: F
@chapter: 付録
@title: 共通信号集団とM50 ray平均の証明
@status: 共通R135の正確輸送、有限時間誤差、階数1支持と、一般ray平均定理R168を証明する。Q3ではM37包絡誤差をR135へ代入する統計診断として扱い、R168/R170の固定時刻instrumentをM42連続粒子経路と区別する。

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

と置く。$C_Z$ は集団の自己共分散であり、M50へ直接入力する物理変数ではない。M50へ渡すのは、入力標本時刻 $t_\star$ に各試行が持つ $Z_{t_\star}(\omega)$ またはその正準コピーである。

ここで自己共分散は非中心化された規格化第2モーメントを指す。$\mathbb E[Z_t]=0$ を追加した場合にだけ、通常の中心化共分散と比例して一致する。以下の支持証明に中心化共分散だけを代入してはならない。

R170の完全結果集合は

```math
\mathcal Y=\mathcal I\cup\{\varnothing\}
```

である。$\varnothing$ は零信号、信号閾値未満、比較境界、作用殻準備失敗、衝突数超過、保持失敗、枝固定失敗、記録失敗を含む。無反応を除いて再規格化しない。

入力時刻と出力時刻を

```math
t_\star<t_{\rm out}
```

と固定する。$t_\star$ はM37包絡を採取する時刻、$t_{\rm out}$ はM50熱化、ラッチ、局所記録を終えた時刻である。R170は両者の間に有限の処理時間を必要とする。

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

である。階数1作用素のtrace normが

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

trace距離は1以下なので右辺を1で切ってよい。$S_0=\widetilde S_0$ かつ局所--正常モード変換が

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

となる。これでR135の有限時間誤差節を得る。正確なunitary輸送は $Z_t=U(t)Z_0$ を第2モーメントへ代入して直ちに従う。

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

がほとんど確実に成り立つ。安全試行では $\alpha\neq0$ なので、M50のray重みは

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

近似rayを単位ベクトル $\widehat z$、目標rayを $c$ とする。純粋状態trace距離を

```math
s
=
D_{\rm tr}
\left(
\widehat z\widehat z^\dagger,
cc^\dagger
\right)
```

と置く。$M_i=\Psi^\dagger|i\rangle\langle i|\Psi$ は1つの有限結果測定を定めるため、trace距離の縮約性から

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

R135のベクトル誤差から直接ray誤差を作る場合、目標rayを $c$ とし、適切な同位相・同尺度の代表に対して $\|z-c\|\leq q_T<1$ なら

```math
\frac{\|(I-cc^\dagger)z\|}{\|z\|}
\leq
\frac{q_T}{1-q_T}
```

である。左辺は $z$ と $c$ の純粋状態trace距離なので、$\rho_T=q_T/(1-q_T)$ を使える。同じ $q_T$ をR135のtrace誤差とR168のray誤差の双方へ加算してはならない。これでR168を得る。

## F.4 R168の一般ray平均、固定作用節、可変作用反例

安全事象 $G$ を固定し、安全ray平均を

```math
R_Z^G
=
\mathbb E
\left[
\mathbf1_G
\frac{ZZ^\dagger}{Z^\dagger Z}
\right]
```

と置く。M50の枝平均は線形性から

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

これは固定作用面で $R_Z^G=C_Z$ となること、従って各試行でray規格化してから平均する操作と、集団第2モーメントを規格化してから枝射影を取る操作が可換であることを示す。

固定作用を外すと一般には可換しない。2次元で、確率 $1/2$ ずつ

```math
Z=\sqrt3e_1,
\qquad
Z=e_2
```

を取る集団を考える。試行ごとのray平均は

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

最後はCauchy--Schwarz不等式である。枝射影とM50正則化を通した全変動距離は

```math
D_{\rm TV}
\leq
\frac{1}{1+\delta}
D_{\rm tr}(R_Z,C_Z)
```

で抑えられる。これでR168の固定作用節、可変作用反例、半径方向補正を得る。階数1ならF.3により $R_Z^G=P(G)c_\star c_\star^\dagger$ である。

## F.5 入力標本化、保持、作用殻消去表示

M37信号registerを $Z$、同じ次元の空registerを $V$ とする。対応する全ての実正準対を交換する写像

```math
(Z,V)\longmapsto(V,Z)
```

は正準であり、自己逆である。入力面で $V=0$ なら、交換後は $V=Z_{t_\star}$ を保持し、M37側registerは空になる。交換前の値、時計面、保持controllerの状態を履歴へ残せば、閾値判定と保持失敗を含めても拡大写像は1対1にできる。

保持した $V\neq0$ に対し、付録LのM50容量は

```math
A_i^\delta(V)
=
\mathcal J_0
\left[
|(\Psi V)_i|^2
+\delta q_iV^\dagger V
\right]
```

である。2作用殻のLiouville状態数を1回だけ規格化して $\pi_i^\delta(V)$ を得る。R161/R162へ渡すときは殻を消去し、

```math
E_i^\delta(V)=-\Theta\log\pi_i^\delta(V)
```

だけを使う。同じ分配関数内で $\Omega_i^\delta e^{-\beta E_i^\delta}$ を使わない。

作用容量結合、殻内平衡化、枝対称性、保持controller反作用を一つの有限局所Hamiltonianへ統合した定理はまだない。R170は、これらを指定誤差で実行できるという条件付きinstrument定理である。

## F.6 共通R170のQ3固定時刻診断

有限熱化、衝突近似、辺閉鎖、局所記録、履歴単射性の共通証明は付録K.6のR170へ集約する。Q3信号を任意の固定時刻に診断する代替instrumentでは、F.5のSWAPにより $v=V=Z_{t_\star}(\omega)$ を固定し、集団理想分布をR168で評価する。安全事象外は全て $\varnothing$ へ送り、$t_{\rm out}>t_\star$ を保つ。現行Q3の物理経路はM42を初期化して同じ粒子を輸送するため、終時刻R170と同じ運転へ併用しない。

各段階の全変動誤差を合成すると

```math
\begin{aligned}
\varepsilon_{170}
\leq{}&
\varepsilon_{\rm nr}
+\varepsilon_{37\to50}
+\varepsilon_{\rm reg}
+\varepsilon_{\rm cap}
+\varepsilon_{\rm width}
+\varepsilon_{\rm flux}\\
&+\varepsilon_{\rm mix}
+\varepsilon_{\rm coll}
+\varepsilon_{\rm hold}
+\varepsilon_{\rm lock}
+\varepsilon_{\rm rec}
\end{aligned}
```

を得る。ここで

```math
\varepsilon_{\rm mix}
\leq
C_\delta e^{-\lambda_\delta\tau_X}.
```

$\varepsilon_{37\to50}$ にはR168の階数1ray評価、固定作用等式、半径方向補正の必要なものだけを入れる。同じM37標本偏差を $\varepsilon_{\rm reg}$、$\varepsilon_{\rm cap}$ へ再び入れない。

R168の理想分布は既に $P(\varnothing)=P(G^c)$ を含む。R170固有の実装失敗だけを追加し、上流の無反応質量を再加算しない。これにより成功試行の再規格化なしにQ3特殊化を得る。

## F.7 R124とR125に対する固定時刻代替診断

R124の初期読出し分布を $p_0$、終期読出し分布を $p_1$、障壁反対側の理想増分を

```math
p_1(R)-p_0(R)=\alpha>0
```

とする。各読出しのR170誤差が $\varepsilon_{170}$ 以下なら

```math
p_1^{\rm out}(R)-p_0^{\rm out}(R)
\geq
\alpha-2\varepsilon_{170}.
```

従って $\varepsilon_{170}<\alpha/2$ なら正の増分が残る。

R125の2つの理想分布を $p,q$ とし、理想全変動距離を $\Delta$ とする。各R170読出しが誤差 $\varepsilon_{170}$ 以下なら三角不等式から

```math
D_{\rm TV}
\left(p^{\rm out},q^{\rm out}\right)
\geq
\Delta-2\varepsilon_{170}.
```

コヒーレント入力と非干渉混合では $\Delta=1/2$、2つの相対位相入力では $\Delta=1$ なので、$\varepsilon_{170}<1/4$ で両方の差が正に残る。

これらは固定入力時刻の分布を後刻に読む代替instrument接続である。現行Q3のQ3-4・Q3-5判定は付録NのM42/R174接続を使い、この節のR170を第2の終位置標本器として重ねない。どちらの経路も、障壁散乱の初回到達率、吸収率、幾何学的2開口、連続運転スクリーンを構成しない。

## F.8 物理的限界と反証条件

R135、R168とR170の固定時刻診断だけから次は従わない。第3項の有限グラフ版はM42/R172--R174が別の追加模型として扱う。

1. 集団共分散 $C_Z$ を単一試行制御器が直接読むこと。
2. 可変全作用集団で $\mathbb E[ZZ^\dagger]/\mathbb E[Z^\dagger Z]$ と $\mathbb E[ZZ^\dagger/(Z^\dagger Z)]$ が一致すること。
3. 粒子位置が入力時刻以前からM37作用比を追跡すること。
4. M50熱化中の枝軌道がSchrödinger型確率流または物理空間の連続軌道であること。
5. 粒子位置がM37振動子網の全エネルギー、慣性質量、電荷を運ぶこと。
6. 初回到達、吸収、時間積分流束、多粒子位置、連続空間極限。
7. 固定有限精度の同じ装置で $\delta\downarrow0$ を取れること。
8. 作用殻fiber、衝突bath、信号保持、局所記録、resetの総仕事・総熱収支が閉じること。

固定作用公式が可変作用反例で破れない、入力時刻と出力時刻を同一視しない、作用殻状態数を二重計数しない、無反応を除いて再規格化しない、同じM37誤差を複数回加算しないことが本付録の監査条件である。

## F.9 制御されたM37の共通位相と階数1診断

M37の局所包絡は共役成分を含む実線形発展である。一般には $b(t;e^{i\alpha}b_0)=e^{i\alpha}b(t;b_0)$ は厳密には成り立たない。従って初期 $Z_0=\alpha c$ の階数1集団に対して、局所包絡の第2モーメントが厳密に階数1を保つとは主張しない。

第6.17節の入力一様な相対誤差をF.2の二乗平均誤差へ代入すれば、有効unitary輸送からの偏差をR135で抑えられる。別の方法として安全作用下で試行ごとの方向誤差をR168へ直接渡してよい。同じ偏差を両経路の和として数えない。局所作用は実際の読出し入口で評価し、射影後の成功試行だけを再規格化しない。M37の共通位相依存は制御精度の検査対象であり、新しい確率源ではない。
