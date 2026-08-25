@number: 5
@chapter: 本文
@title: M48の2端Bell測定周期と前提監査
@status: 固定singlet型・固定有限設定族について、M39からの破壊的受渡し、2翼matching、切断後局所分析、記録、弱開放帰還を閉じる。Q2-2は操作的接続の範囲で条件付き達成とする。

## 5.1 目的と模型の境界

本章は、付録JのM48 paired-Hopf準備を、M39の固定singlet型出力から2つの物理的測定端、局所記録、次周期入口まで接続する。M48の各試行で実在する信号変数は、2翼のbath作用角表示 $z_A,z_B$、W型有限配置グラフ上の実現配置 $X_A,X_B$、設定、時計、局所雑音seed、記録・履歴・resetセルである。交差共分散射影は集団統計であり、単一試行の結果変数ではない。

draft-45Aで未完成だった5項目を次の順序で閉じる。

1. M39の4モード場と共同実現配置をM48中央portへ破壊的に渡す。
2. paired-Hopf流の各安全枝について、bath対と2翼実現配置を強いmatching fiberへ準備する。
3. 中央結合を切った後は、A端とB端の生成子を因子化する。
4. 各局所分析器の終了後にmatchingを局所的に回復し、傾斜固定した実現配置だけを記録する。
5. 外部記録を残したまま、能動部をfresh cell交換で次周期入口へ戻す。

全時刻でmatching多様体が厳密不変であるとは主張しない。切断面、局所分析器終了面、記録面というプロトコル面ごとにmatching誤差を評価する。これでBell結果頻度に必要な橋は閉じるが、M47の一般Q1測定で残る自然なmatching保存問題は解消しない。

M48は採用開放古典模型である。paired-Hopf pump、設定controller、配置交換bath、傾斜固定、記録cell、fresh cell流を明示するが、全系を有限閉鎖Hamiltonianへ持ち上げたとは呼ばない。

## 5.2 設定前開始面とM39出力

固定した有限A設定族を $\mathcal X$、有限B設定族を $\mathcal Y$ とする。設定前開始面では、M39の鋭い基準入力、設定生成角、M48の空controller、共通seed、2翼の空W型配置、局所雑音seed、記録・履歴・resetセルを設定非依存測度 $\nu_0$ に置く。

M39の固定回路は

```math
c_{\rm s}
=
\frac{1}{\sqrt2}
\begin{pmatrix}
0&1&-1&0
\end{pmatrix}^{\mathsf T}
```

と、共同実現配置

```math
X^{39}
\in
\{01,10\}
```

を準備する。理想頻度は各 $1/2$ であり、この準備は $x,y$ に依存しない。有限M39準備の全変動誤差と場方向誤差をまとめて $\varepsilon_{39}$ とする。

M39の4モード場を2つの2モード場へ複製しない。中央に1つだけ置く4成分受渡しregisterへ正準SWAPし、元のM39信号slotを空にする。共同配置は履歴を保存した可逆な有限routingで枝seed registerへ渡す。

## 5.3 固定singlet型の破壊的受渡しport

4モード係数 $c$ を行優先で $2\times2$ 行列 $B(c)$ へ並べ、反対称成分を

```math
\mathcal P_-(B)
=
\frac12
\left(
B-B^{\mathsf T}
\right)
```

とする。$\|\mathcal P_-(B)\|_{\rm F}\geq b_*>0$ の安全領域で、pairing controllerを

```math
\mathsf J(c)
=
\sqrt2
\frac{
\mathcal P_-(B(c))
}{
\|\mathcal P_-(B(c))\|_{\rm F}
}
```

と定める。$c=c_{\rm s}$ では $\mathsf J(c)=\mathsf E$ である。全体位相が残っても、ベクトル化した交差共分散射影は同じsinglet射影になる。

$X^{39}=01$ を $s_0=+1$、$X^{39}=10$ を $s_0=-1$ と符号化する。これは測定結果ではなく、設定生成前に存在する等重み共通原因seedである。A設定 $x$ の生成後、有限controllerはbright seed $m$ を

```math
s_0h_x(m)
\geq
h_*,
\qquad
h_x(m)
=
\frac{m^\dagger\Sigma_xm}{m^\dagger m}
```

となる安全盆へ有限時間で送る。有限設定族なので、各 $(s_0,x)$ に1つずつ安全seedと有限routingを用意できる。目的の測定開始分布を開始面へ直接置くのではなく、設定生成後の前向き開放写像として実行する。

<!-- theorem-start:theorem -->
**定理（R151：M39からM48への固定singlet型破壊的受渡し）**

固定singlet型M39回路、有限設定族 $\mathcal X$、$b_*,h_*>0$ を固定する。M39の4モード場を単一中央controllerへSWAPし、その反対称成分から $\mathsf J(c)$ を作り、共同実現配置から等重み枝seedを作る有限正準routingと開放seed整列を構成できる。理想M39出力では $\mathsf J=\mathsf E$、$P(s_0=\pm1)=1/2$ であり、各設定について $s_0h_x(m)\geq h_*$ となる。有限装置では失敗質量を無反応へ送り、controller、枝重み、安全盆の総誤差を $\varepsilon_{\rm link}$ で抑えられる。受渡しは元の4モード場を保存した2翼分配ではなく、固定singlet型に限定した破壊的操作接続である。
<!-- theorem-end:theorem -->

## 5.4 単一試行bath座標からの局所matching流

各翼のW型2モード埋込みを

```math
\Phi:
\mathbb C^2
\longrightarrow
\mathbb C^{|\Omega_W|}
```

とし、$\Phi^\dagger\Phi=I_2$ とする。$\Omega_W$ は有限連結配置グラフである。正の基準分布 $q_i>0$、$\sum_iq_i=1$ と、正則化 $\delta>0$ を固定する。

単一試行のbath座標 $z\neq0$ に対して

```math
w_i(z)
=
\frac{
|\left(\Phi z\right)_i|^2
}{
z^\dagger z
},
```

```math
\pi_i^\delta(z)
=
\frac{
w_i(z)+\delta q_i
}{
1+\delta
}
```

と置く。$w_i$ は集団共分散または統計振幅を入力にせず、その試行に存在する2作用角と固定W型mode係数から作る局所controller信号である。

無向辺 $i\sim j$ に対し $a_{ij}=a_{ji}>0$ とし、配置jump率を

```math
k_{i\to j}^\delta(z)
=
\kappa_Xa_{ij}
\sqrt{
\frac{
\pi_j^\delta(z)
}{
\pi_i^\delta(z)
}
}
```

とする。生成子は

```math
\left(
\mathcal L_X^zf
\right)(i)
=
\sum_{j\sim i}
k_{i\to j}^\delta(z)
\left[
f(j)-f(i)
\right]
```

である。これはM48で新たに採用する開放配置応答則であり、M42/R113の複素振幅場からcurrent rateを作る規則ではない。具体的な回路または衝突浴から導出したとも扱わない。

<!-- theorem-start:theorem -->
**定理（R152：有限W型配置グラフの局所matching生成子）**

$z\neq0$ を固定する。上のjump率は有限かつ非負で、隣接辺ごとに

```math
\pi_i^\delta(z)
k_{i\to j}^\delta(z)
=
\pi_j^\delta(z)
k_{j\to i}^\delta(z)
```

を満たす。従って $\pi^\delta(z)$ は一意定常分布である。$\lambda_X^\delta(z)>0$ を可逆生成子の第1非零固有値とすれば、固定有限seed集合上で有限定数 $C_X$ と一様下界 $\lambda_X^\delta>0$ を選べ、

```math
D_{\rm TV}
\left(
\operatorname{Law}(X_T\mid z),
\pi^\delta(z)
\right)
\leq
C_Xe^{-\lambda_X^\delta T}
```

となる。$\pi^\delta(e^{i\alpha}z)=\pi^\delta(z)$ であり、理想Born型対角 $w(z)$ との差は全変動距離で高々 $\delta/(1+\delta)$ である。
<!-- theorem-end:theorem -->

## 5.5 強いmatching fiber

規格化 $c\in\mathbb C^2$ に対し、強い正則化matching fiber $\mathcal F_W^\delta(c)$ を、次を満たす共同測度の族とする。

```math
z=e^{i\alpha}c,
\qquad
P(X=i\mid z)
=
\pi_i^\delta(z).
```

共通位相 $\alpha$ の分布は任意でよい。このfiberではbath共分散は $cc^\dagger$ であり、実現配置周辺は $|\Phi c|^2$ から高々 $\delta/(1+\delta)$ だけずれる。M47のmatching条件より強く、単一試行bath座標に条件付けた配置分布まで指定する。

$\delta=0$ の理想fiberを $\mathcal F_W^0(c)$ と書く。連続bath座標の有限時間近接を全変動距離で測ると、異なるrayに支持された測度間の距離が1になり得るため、切断面には次のprojective fiber距離を使う。規格化した目標対 $(u,v)$ に対して

```math
\begin{aligned}
d_{\rm pair}
\left(
(z_A,z_B),(u,v)
\right)
={}&
\left|\|z_A\|-1\right|
+
\left|\|z_B\|-1\right|\\
&+
\inf_{\alpha\in\mathbb R}
\left[
\left\|
\frac{z_A}{\|z_A\|}-e^{i\alpha}u
\right\|
+
\left\|
\frac{z_B}{\|z_B\|}-e^{-i\alpha}v
\right\|
\right].
\end{aligned}
```

枝符号の不一致、$X_A$、$X_B$ の不一致、および $d_{\rm pair}$ の和を1で切ったcostを $d_\Omega$ とする。切断面測度と理想fiber混合の間の $d_\Omega$-Wasserstein距離を $d_{\rm fib}$ と書く。離散配置部分では最適couplingの不一致確率が全変動距離に等しく、連続bath部分ではpaired位相を保った方向誤差を測る。この距離を完全状態の全変動距離と呼ばない。

paired-Hopf準備終了後、controllerを保持して $z_A,z_B$ を固定し、A、Bの配置jumpを独立に有限時間走らせる。安全枝 $s$ の理想目標を

```math
u_{s,x},
\qquad
v_{s,x}
=
\mathsf E\overline{u_{s,x}}
```

とする。

<!-- theorem-start:theorem -->
**定理（R153：M48中央切断面の2翼強matching準備）**

R147の有界seed条件、R151の安全受渡し、R152の有限配置グラフを仮定する。paired-Hopf時間を $T_{\rm PH}$、配置混合時間を $T_X$ とする。理想切断面fiber混合を

```math
\nu_x^0
=
\frac12
\sum_{s=\pm1}
\mathcal F_W^0(u_{s,x})
\mathbin{\widehat\otimes}
\mathcal F_W^0(v_{s,x})
```

とする。中央切断面の完全状態測度 $\mu_{\rm cut}^x$ は、無反応部分を含めてprojective fiber距離

```math
\begin{aligned}
d_{\rm fib}
\left(
\mu_{\rm cut}^x,\nu_x^0
\right)
\leq
\varepsilon_{\rm fib}
\leq{}&
\varepsilon_{39}
+
\varepsilon_{\rm link}
+
K_{48}e^{-\gamma_{48}T_{\rm PH}}\\
&+
\frac{2\delta}{1+\delta}
+
2C_Xe^{-\lambda_X^\delta T_X}
+
\varepsilon_{\rm cut}
\end{aligned}
```

以内にある。$\widehat\otimes$ は枝符号とpaired位相を共有し、配置jump noiseは条件付き独立であることを表す。この測度の交差共分散射影はR148のsinglet射影に有限時間誤差で一致し、同時に各翼の実現配置周辺と条件付きbath分布がmatchingされる。
<!-- theorem-end:theorem -->

## 5.6 中央切断と局所分析器

切断後の状態を

```math
\Lambda
=
(\Lambda_A,\Lambda_B,s,\alpha,\mathcal H)
```

と書く。$\mathcal H$ は中央の使用済みsourceと受渡し履歴であり、局所結果形成には入らない。切断後の生成子を

```math
\mathcal L_{\rm post}^{xy}
=
\mathcal L_A^x
+
\mathcal L_B^y
```

とする。A、Bの局所雑音seedは $s,\alpha$ に条件付けて独立である。A設定 $x$ は中央準備ですでに使われている。B設定 $y$ は中央切断後にB局所controllerへだけ入る。

A端はR140の分析器 $A_x$ で $u_{s,x}$ を左右局在方向へ写す。B端は $A_y$ で $v_{s,x}$ をB測定基底へ写す。局所2モード操作中に配置matchingが一時的に崩れることを許すが、操作終了後にbath方向を固定し、R152の局所配置流を時間 $T_{X,\rm meas}$ だけ走らせる。

その後、配置jump prefactorを零へ切り替え、R141の傾斜固定を保ったまま記録する。従って記録窓中の経路滞在失敗は、rate切断残差と傾斜保持誤差へ明示的に分けられる。

## 5.7 局所記録と結果の一意性

各翼の左右安全領域に局所検出関数 $\chi_{w,+}(X_w)$、$\chi_{w,-}(X_w)$ を置く。分離面近傍は無反応とする。外部記録cellへの生成子を

```math
G_{\rm rec}
=
P_A^R
\left(
\chi_{A,+}-\chi_{A,-}
\right)
+
P_B^R
\left(
\chi_{B,+}-\chi_{B,-}
\right)
```

とする。理想空cellでは記録中の能動部への反作用は零である。結果集合は

```math
\{+1,-1,\varnothing\}^2
```

であり、無反応試行を除外して再規格化しない。

Markov jumpの局所noise seedを完全状態へ含めれば、記録時刻の $X_A,X_B$ と記録結果は各試行で一意に決まる。確率応答は外から結果重みとして与えるのでなく、R152の開放配置bathと設定前noise seedから生じる。

<!-- theorem-start:theorem -->
**定理（R154：切断後の局所分析、再matching、固定、記録）**

R153の切断面から開始し、固定有限設定族について局所2モード制御誤差、2モード外漏れ、W型左右コントラスト、配置再matching、rate切断、傾斜固定、境界無反応、記録誤差を有限とする。guardから離れたcompact安全域上の局所応答核は、$d_\Omega$ に関して一様Lipschitzとする。切断後にA、Bの直接結合を使わず、各翼のbath座標、実現配置、設定、局所noiseだけから一意な局所記録を作れる。安全枝 $s$ についてA結果は $s$ から有限誤差内にあり、B条件付き結果は

```math
P(B=b\mid s,x,y)
=
\frac12
\left(
1-sb\,\boldsymbol n_x\cdot\boldsymbol n_y
\right)
```

から局所instrument誤差内にある。切断後の応答核は完全状態に条件付けてA、Bに因子化する。
<!-- theorem-end:theorem -->

本定理はBell結果形成だけを扱う。結果別2モードテンプレート交換、逐次測定後状態、Q1の一般射影instrumentは主張しない。

## 5.8 余弦共同分布、非信号性、CHSH値

枝seedは等重みであり、A記録は理想的に $a=s$ である。従ってR154の条件付き分布から

```math
P(a,b\mid x,y)
=
\frac14
\left(
1-ab\,\boldsymbol n_x\cdot\boldsymbol n_y
\right)
```

を得る。平面角では $\boldsymbol n_x\cdot\boldsymbol n_y=\cos(x-y)$ である。両周辺は

```math
P(A=a\mid x,y)
=
P(B=b\mid x,y)
=
\frac12
```

であり、相関は $E(x,y)=-\cos(x-y)$ となる。標準CHSH設定では $|S|=2\sqrt2$ である。これは固定singlet型平面2出力族の値であり、一般測定族を拘束するTsirelson原理の導出ではない。

## 5.9 前向き有限誤差

M48完全周期の前向き誤差を

```math
\begin{aligned}
\varepsilon_{45B}
\leq{}&
\delta_{\rm set}
+\varepsilon_{39}
+\varepsilon_{\rm link}
+\varepsilon_{\rm PH}
+L_{\rm fib}\varepsilon_{\rm fib}\\
&+
\varepsilon_{\rm an}^A
+\varepsilon_{\rm an}^B
+\varepsilon_{\rm X,meas}^A
+\varepsilon_{\rm X,meas}^B\\
&+
\varepsilon_{\rm lock}^A
+\varepsilon_{\rm lock}^B
+\eta_W^A
+\eta_W^B\\
&+
\varepsilon_{\rm guard}
+\varepsilon_{\rm rec}^A
+\varepsilon_{\rm rec}^B
+\varepsilon_{\rm clk}
\end{aligned}
```

とする。$L_{\rm fib}<\infty$ は固定有限設定族の安全域上で局所応答核を結果全変動距離へ移す一様Lipschitz定数である。R153の展開を使う場合、$\varepsilon_{\rm PH}$ と $\varepsilon_{\rm fib}$ の中の同じpaired-Hopf項を二重に数えない。

<!-- theorem-start:theorem -->
**定理（R155：M48完全周期の有限誤差Bell統計と前提監査）**

各設定対について、無反応を含む完全結果分布と理想singlet分布の全変動距離は $\varepsilon_{45B}$ 以下である。従って一側周辺の反対設定による差は $2\varepsilon_{45B}$ 以下、CHSH値の理想値からのずれは $8\varepsilon_{45B}$ 以下である。

```math
\varepsilon_{45B}
<
\frac{\sqrt2-1}{4}
```

ならCHSH不等式の破れが残る。設定前測度 $\nu_0$ は設定に依存しないが、R151とR147の前向き準備後の切断面測度 $\mu_{\rm cut}^x$ はA設定に依存する。切断後の応答は局所因子化し、理想周辺は非信号的である。従ってBellの定理を否定せず、成立しない前提は測定設定独立性である。
<!-- theorem-end:theorem -->

R149とR150は、完全matchingを抽象的に仮定した条件付き結果として残る。R153とR154は、固定Bell装置についてその仮定を有限誤差で充足し、R155を与える。

## 5.10 Bell前提監査

| 監査項目 | M48完全周期での位置 |
|---|---|
| 局所性 | 切断後の生成子は $\mathcal L_A^x+\mathcal L_B^y$。反対翼の設定、結果、noiseを入力にしない |
| 測定設定独立性 | 設定前は共通測度。A設定生成後のseed routingとpaired-Hopf準備により $\mu_{\rm cut}^x$ が $x$ に依存するため成立しない |
| 結果の一意性 | noise seedを含む完全状態と記録時刻を固定すれば、各翼の実現配置と記録は一意 |
| 事後選別 | 分離面、受渡し失敗、盆失敗、時計境界を $\varnothing$ として分母へ残す |
| 非信号性 | 理想singlet対称性から両周辺は $1/2$。有限装置では反対設定差を $2\varepsilon_{45B}$ で抑える |
| 試行測度 | 枝重みはM39共同配置、配置頻度はR152の有限時間開放流から作り、測定開始面へ目的分布を直接置かない |

$x$ と $x'$ が同じ非順序軸を表さない場合、理想切断面の2枝支持

```math
\left\{
u_{+,x},u_{-,x}
\right\}
```

と

```math
\left\{
u_{+,x'},u_{-,x'}
\right\}
```

は異なる。従って交差共分散射影が両設定で同じでも、完全切断面測度は同じではない。設定依存性を2次交差共分散だけで監査してはならない。

## 5.11 弱開放帰還

paired-Hopf準備と配置混合は散逸を含むため、前向き流を逆実行して開始点へ戻すとはしない。外部記録を保持した後、各翼の使用済みbath、配置seed、controller残差を流出cellへ交換し、設定非依存のfresh cellを次周期入口へ入れる。

能動部偏差 $\Delta_n$ の1周期写像を

```math
\Delta_{n+1}
=
R_{\rm ret}\Delta_n
+
\eta_n
```

とし、$\|R_{\rm ret}\|\leq r_{\rm ret}<1$、$\|\eta_n\|\leq\sigma_{\rm ret}$ とする。この交換は外部記録と使用済み状態を同一点へ戻さない。固定有限周期では有限個の外部cell、無期限運転ではcell流を持つ弱開放系として扱う。

<!-- theorem-start:theorem -->
**定理（R156：M48の固定有限弱開放帰還）**

R151--R155の固定有限設定周期について、$r_{\rm ret}<1$ のfresh cell交換を各周期末に行うと、

```math
\limsup_{n\to\infty}
\|\Delta_n\|
\leq
\frac{
\sigma_{\rm ret}
}{
1-r_{\rm ret}
}
```

である。有限時間のcontroller減衰を明示する場合は

```math
\varepsilon_{\rm ret}
\leq
C_{\rm ret}e^{-\lambda_{\rm ret}T_{\rm ret}}
+
\varepsilon_{\rm swap}
+
\varepsilon_{\rm seed}
```

とできる。$\varepsilon_{\rm ret}$ は同じ周期の記録分布へ遡って加えず、次周期の $\varepsilon_{39}+\varepsilon_{\rm link}$ へ渡す。固定有限周期数について、永久記録、使用済み状態、fresh cellを含む有限装置を選べる。
<!-- theorem-end:theorem -->

## 5.12 開放模型の局所帳簿

| 段階 | 外部作用 | 散逸先・情報流 |
|---|---|---|
| M39受渡し | 中央SWAP、反対称filter、seed routingの仕事 | 元のM39 slotと不採用成分を履歴・流出portへ渡す |
| paired-Hopf準備 | bright pump、設定controller | dark sinkと振幅飽和bathへ熱・位相情報を渡す |
| 配置matching | $z$ 依存局所有効ポテンシャルの制御仕事 | 各翼の配置交換bathへjump熱を渡す |
| 中央切断 | pairing、共通clock、中央配置bathとの結合を停止する仕事 | 切断残差を $\varepsilon_{\rm cut}$ へ入れる |
| 局所分析 | A、B別々の2モード制御仕事 | 各局所controllerと配置bathだけを使う |
| 固定・記録 | rate切断、傾斜、空記録cell | 記録情報を外部cellへ移す |
| 帰還 | fresh cell供給と使用済みcell排出 | 使用済みbath、配置seed、controller情報を外部へ流す |

配置jumpについて

```math
U_i^\delta(z)
=
-\Theta
\log
\pi_i^\delta(z)
```

と置けば、rate比は

```math
\frac{
k_{i\to j}^\delta
}{
k_{j\to i}^\delta
}
=
\exp
\left[
-\frac{
U_j^\delta-U_i^\delta
}{
\Theta
}
\right]
```

となる。固定 $z$ でのjump熱は局所有効ポテンシャル差、$z$ またはsettingを変える間のポテンシャル変化はcontroller仕事である。総仕事、総熱、総エントロピー生成を具体的回路定数で閉じてはいない。

## 5.13 有限時間と精度--資源交換

目標誤差を正に固定すれば、少なくとも

```math
T_{\rm PH}
\geq
\frac1{\gamma_{48}}
\log
\frac{K_{48}}{\epsilon_{\rm PH}},
```

```math
T_X
\geq
\frac1{\lambda_X^\delta}
\log
\frac{C_X}{\epsilon_X},
```

```math
T_{\rm ret}
\geq
\frac1{\lambda_{\rm ret}}
\log
\frac{C_{\rm ret}}{\epsilon_{\rm ret}}
```

と選べる。$\delta\to0$ では率比と混合時間が悪化し得る。深いW型で $\eta_W\to0$ とするとR140の操作時間が増え得る。設定族は固定有限とし、設定数、論理量子ビット数、回路深さに対する規模依存性はQ2-3へ送るが、本改訂では解析しない。

## 5.14 Q2-2判定と非主張

R151--R156により、固定singlet型、固定有限設定族、破壊的操作受渡し、準備先行、非空間分離、プロトコル面matching、無反応込み、弱開放帰還という解釈では、Q2-2の固定条件を同じM39--M48周期で満たす。この意味でQ2-2を条件付き達成とする。

M41のR107--R111、R121は数学的に撤回せず、置換済み模型内の補助結果として研究メモへ移す。M42/R113はQ2-1、Q2-3、Q3の暫定根拠に残るが、M39出力からM48結果形成までの因果鎖には使わない。

ただし、R151へ渡すQ2-1の共同実現配置 $X_{39}$ の生成根拠はR120/M42に依存する。従ってQ2-1出力の生成からM48記録までを含む全接続をM42非依存とは呼ばない。

本章は次を主張しない。

1. 任意のM39二論理状態を2翼へ状態保存的に分配すること。
2. M39の非因子化4モード場を2つの独立物理場へ複製すること。
3. 標準的な空間分離Bell実験または準備後の自由設定変更。
4. 一般測定族に対するTsirelson原理。
5. 独立同分布型有限標本揺らぎ。
6. R152の配置応答則を具体的回路または有限閉鎖Hamiltonianから導出したこと。
7. 連続時間の全区間で強いmatching fiberが不変であること。
8. M47の一般Q1 matching準備、測定後状態、逐次測定を解いたこと。
9. 全系の総エネルギー・総エントロピー収支を閉じたこと。
10. Q2-3の多量子ビット資源問題を進めたこと。
