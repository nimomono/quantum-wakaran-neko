@number: 5
@chapter: 本文
@title: M48の2端Bell測定周期と前提監査
@status: 固定singlet型・固定有限設定族について、M48内部またはM49由来の等重みseed routing、2翼matching、切断後局所分析、記録、弱開放帰還を閉じる。M48単独周期とM49接続周期を条件付き達成とする。

## 5.1 目的と模型の境界

本章は、付録JのM48 paired-Hopf準備を、setting-freeな等重みseedから2つの物理的測定端、局所記録、次周期入口まで閉じる。M48の各試行で実在する信号変数は、2翼のbath作用角表示 $z_A,z_B$、W型有限配置グラフ上の実現配置 $X_A,X_B$、設定、時計、局所雑音seed、記録・履歴・resetセルである。交差共分散射影は集団統計であり、単一試行のcontrollerまたは結果変数ではない。

M48単独周期は次の5項目を順に閉じる。

1. 設定前の等重みseedを履歴から独立に保持し、A設定生成後に安全盆へ送る。
2. paired-Hopf流の各安全枝について、bath対と2翼実現配置を強いmatching fiberへ準備する。
3. 中央結合を切った後は、A端とB端の生成子を因子化する。
4. 各局所分析器の終了後にmatchingを局所的に回復し、傾斜固定した実現配置だけを記録する。
5. 外部記録を残したまま、能動部をfresh cell交換で次周期入口へ戻す。

全時刻でmatching多様体が厳密不変であるとは主張しない。切断面、局所分析器終了面、記録面というプロトコル面ごとにmatching誤差を評価する。M48内部のBell結果頻度に必要な橋はR151--R156、Q2-1から同じ試行registerを渡す橋はM49/R160が閉じる。M47の一般Q1測定で残る自然なmatching保存問題は解消しない。

M48は採用開放古典模型である。paired-Hopf pump、設定controller、配置交換bath、傾斜固定、記録cell、fresh cell流を明示するが、全系を有限閉鎖Hamiltonianへ持ち上げたとは呼ばない。

## 5.2 設定前開始面と等重みseed

固定した有限A設定族を $\mathcal X$、有限B設定族を $\mathcal Y$ とする。設定前開始面では、設定生成角、固定pairing tensor $\mathsf E$、等重み枝seed $S_0\in\{+1,-1\}$、2翼の空W型配置、局所雑音seed、記録・履歴・resetセルを設定非依存測度 $\nu_0$ に置く。

```math
P(S_0=+1)=P(S_0=-1)=\frac12,
\qquad
\operatorname{Law}(S_0\mid x,y)=\operatorname{Law}(S_0).
```

$S_0$ は測定結果ではなく、設定生成前に存在する共通原因seedである。M48単独運転では内部等重みcellを使い、M49接続運転ではR160が渡した同じ実現配置から $S_0=(-1)^{X_A}$ と読む。後者はM49のbath対、配置対を恒等搬送した後のbranch-carrying成分であり、state-carrying性は受渡し面のcross projector感度で別に検査する。履歴識別子 $H_{\rm prov}$ は設定と結果形成へ入力しない。

## 5.3 setting-pre seedの履歴付き安全盆routing

A設定 $x$ の生成後、有限controllerはbright seed $m$ を

```math
S_0h_x(m)
\geq
h_*,
\qquad
h_x(m)
=
\frac{m^\dagger\Sigma_xm}{m^\dagger m}
```

となる安全盆へ有限時間で送る。有限設定族なので、各 $(S_0,x)$ に1つずつ安全seedと有限routingを用意できる。目的の測定開始分布を開始面へ直接置くのではなく、設定生成後の前向き開放写像として実行する。

<!-- theorem-start:theorem -->
**定理（R151：setting-pre等重みseedの履歴付き安全盆routing）**

有限設定族 $\mathcal X$ と $h_*>0$ を固定する。設定前の等重みseed $S_0\in\{+1,-1\}$ と固定tensor $\mathsf E$ から開始し、各 $(S_0,x)$ について $S_0h_x(m)\geq h_*$ となるbright seedへ送る有限前向きroutingを構成できる。$S_0$ はM48内部cellまたはM49/R160の $X_A$ から供給してよく、いずれも設定生成前に存在する。接続運転では受渡された同じ $z_A,z_B$ registerをbright/dark portとして使い、ensembleから新しいbath対を再標本化しない。有限装置ではseed bias誤差を $\varepsilon_{\rm seed}$、盆外・routing失敗質量を $\varepsilon_{\rm route}$ として無反応へ送る。任意の許された履歴値 $h$ について

```math
\operatorname{Law}(A,B\mid x,y,H_{\rm prov}=h)
=
\operatorname{Law}(A,B\mid x,y)
```

とし、履歴はprovenance監査にだけ残す。M49接続では枝biasは保存され、bath・配置registerのstate-carrying受渡しはR160で評価する。R151自体は設定生成後の安全盆routingであり、一般状態Bell測定を主張しない。
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

R147の有界seed条件、R151の安全盆routing、R152の有限配置グラフを仮定する。paired-Hopf時間を $T_{\rm PH}$、配置混合時間を $T_X$ とする。理想切断面fiber混合を

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
\varepsilon_{\rm seed}
+
\varepsilon_{\rm route}
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
\varepsilon_{\rm Bell}^{48,{\rm cyc}}
\leq{}&
\delta_{\rm set}
+\varepsilon_{\rm seed}
+\varepsilon_{\rm route}
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
**定理（R155：M48単独完全周期の有限誤差Bell統計と前提監査）**

各設定対について、M48の無反応を含む完全結果分布 $P_{\rm Bell}^{48,{\rm cyc}}$ と理想singlet分布の全変動距離は $\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ 以下である。従って一側周辺の反対設定による差は $2\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ 以下、CHSH値の理想値からのずれは $8\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ 以下である。

```math
\varepsilon_{\rm Bell}^{48,{\rm cyc}}
<
\frac{\sqrt2-1}{4}
```

ならCHSH不等式の破れが残る。設定前測度 $\nu_0$ は設定に依存しないが、R151とR147の前向き準備後の切断面測度 $\mu_{\rm cut}^x$ はA設定に依存する。切断後の応答は局所因子化し、理想周辺は非信号的である。従ってBellの定理を否定せず、成立しない前提は測定設定独立性である。本定理はM48のreceiver側を閉じるが、付録Kの $T_{\rm link}$ を構成しない。
<!-- theorem-end:theorem -->

R149とR150は、完全matchingを抽象的に仮定した条件付き結果として残る。R153とR154は、固定Bell装置についてその仮定を有限誤差で充足し、R155を与える。

## 5.10 Bell前提監査

| 監査項目 | M48完全周期での位置 |
|---|---|
| 局所性 | 切断後の生成子は $\mathcal L_A^x+\mathcal L_B^y$。反対翼の設定、結果、noiseを入力にしない |
| 測定設定独立性 | 設定前は共通測度。A設定生成後のseed routingとpaired-Hopf準備により $\mu_{\rm cut}^x$ が $x$ に依存するため成立しない |
| 結果の一意性 | noise seedを含む完全状態と記録時刻を固定すれば、各翼の実現配置と記録は一意 |
| 事後選別 | seed失敗、盆失敗、時計境界を $\varnothing$ として分母へ残す |
| 非信号性 | 理想singlet対称性から両周辺は $1/2$。有限装置では反対設定差を $2\varepsilon_{\rm Bell}^{48,{\rm cyc}}$ で抑える |
| 試行測度 | 枝重みはsetting-pre等重みseed、配置頻度はR152の有限時間開放流から作り、測定開始面へ目的分布を直接置かない |
| provenance | 履歴は監査にだけ使い、許された履歴値で条件付けても結果法則を変えない |

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

とできる。$\varepsilon_{\rm ret}$ は同じ周期の記録分布へ遡って加えず、次周期の $\varepsilon_{\rm seed}+\varepsilon_{\rm route}$ へ渡す。固定有限周期数について、永久記録、使用済み状態、fresh cellを含む有限装置を選べる。
<!-- theorem-end:theorem -->

## 5.12 開放模型の局所帳簿

| 段階 | 外部作用 | 散逸先・情報流 |
|---|---|---|
| seed routing | setting-pre seedの読出しと安全盆routingの仕事 | seed履歴を使用済みcellへ移し、結果形成へ再注入しない |
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

R151--R156によりM48単独Bell周期を閉じ、M49/R160によりQ2-1の固定singlet出力を同じbath・配置registerのままsetting-free面から接続する。従って固定singlet型、固定有限設定族、準備先行、非空間分離、プロトコル面matching、無反応込み、採用開放法則、弱開放帰還という解釈では、固定目標Q2-2全体を条件付き達成とする。

M41のR107--R111、R121は数学的に撤回せず、置換済み模型内の補助結果として研究メモへ置く。M39単独模型とM42/R113のQ2-1適用も現行因果鎖から外す。M42はQ2-3とQ3だけに残り、M48単独周期またはM49接続周期の結果形成には使わない。

本章は次を主張しない。

1. 任意のQ2-1出力を一般状態Bell測定へ渡すこと。
2. 標準的な空間分離Bell実験または準備後の自由設定変更。
3. 一般測定族に対するTsirelson原理。
4. 独立同分布型有限標本揺らぎ。
5. R151、R152の応答則を具体的回路または有限閉鎖Hamiltonianから導出したこと。
6. 連続時間の全区間で強いmatching fiberが不変であること。
7. M47の一般Q1 matching準備、測定後状態、逐次測定を解いたこと。
8. 全系の総エネルギー・総エントロピー収支を閉じたこと。
9. Q2-3の多量子ビット資源問題を進めたこと。
