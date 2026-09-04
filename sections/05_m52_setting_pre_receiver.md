@number: 5
@chapter: 本文
@title: M52駆動setting-pre paired-Hopf receiverとBell前提監査
@status: M52の実際の1試行末端信号をA設定で条件付きblockへ分け、source-driven paired-Hopf流、切断後fresh局所作用殻、2翼M50/R170へ接続する。R180A/Bは代数と採用開放流を閉じ、R180Cは単一装置統合を条件とする。Q2-2の条件付き達成を維持する。

## 5.1 目的と模型の境界

本章は、M52の実際の1試行末端信号を2つの物理的測定端へ渡すsetting-pre receiverを定義する。M52でgate列を終えた信号を

```math
v=Z_{\rm out}(\omega)\in\mathbb C^4,
\qquad
v\neq0
```

とし、R112のcanonical SWAPで同次元hold registerへ物理信号をそのまま

```math
\widetilde V=v
```

と保持する。canonical SWAPは同次元正準座標の交換だけを行い、状態依存除算を行わない。解析上の規格化rayを

```math
r=\|\widetilde V\|,
\qquad
V=\frac{\widetilde V}{r}
```

と定義する。$r\geq r_{\min}>0$ をsafe setに含め、零信号またはこの下限を外れる試行は無反応へ送る。$V$ はcontrollerが生成する物理registerではなく、枝容量比と誤差を記述する解析変数である。$\widetilde V$ は集団共分散、交差moment、理想係数の外部再構成値ではない。同じ試行の実正準座標から得る派生信号である。

M52のanti-register $G_S$ はR176A直後には $\overline{a\otimes b}$ だが、R176Bのgate列は一般に $Z_S$ だけを更新する。従って末端で $G_S=\overline{\widetilde V}$ とは仮定せず、本receiverはholdされた $\widetilde V$ だけを物理入力に使う。未知係数をcontrollerが読み出してtemplate表へ書き込むこと、試行集団momentを単一試行へ再注入することも認めない。

固定有限設定族を $\mathcal X,\mathcal Y$ とする。A設定 $x\in\mathcal X$ は中央receiverへ先行入力され、B設定 $y\in\mathcal Y$ は中央切断後にB局所分析器へだけ入る。設定前のM52 source、設定生成角、fresh cell、局所noise seedの共同測度は設定値に依存しないが、receiver準備後の切断面測度は一般に $x$ に依存する。

R180の物理状態を概念上

```math
\Gamma_{180}
=
\left(
\Gamma_{52}^{\rm hold},x,y,
A_+,A_-,S,
z_A,z_B,X_A,X_B,
\gamma_A,\gamma_B,
\tau,H,R
\right)
```

と書く。$A_\pm$ はbranch容量pointer、$S$ は内部枝、$z_A,z_B$ は2翼receiver信号、$X_A,X_B$ はW型有限位置グラフ上の粒子位置、$\gamma_A,\gamma_B$ はfresh局所作用殻と衝突cell、$H$ は使用済みsourceとclockの履歴、$R$ は外部記録である。$S$ は中央で形成される共通原因であり、この段階では外部結果として記録しない。

R180を三つに分ける。

1. R180AはM52信号のsetting-pre条件付きblock抽出、branch作用、Born共同代数を与える。
2. R180Bは選択blockを物理templateとして2翼carrierへ移すsource-driven paired-Hopf吸引を与える。
3. R180Cは中央切断、2翼M50/R170、局所記録、Bell監査、fresh-cell帰還を条件付きで合成する。

## 5.2 M52の固定singlet sourceと試行順序

Q2-2の固定benchmarkでは、M52の2入力を $|00\rangle$ とし、R176Aのtensor-lift後にR176Bの局所gateとCNOTを

```math
|00\rangle
\xrightarrow{H_A}
\frac{|00\rangle+|10\rangle}{\sqrt2}
\xrightarrow{\operatorname{CX}_{A\to B}}
\frac{|00\rangle+|11\rangle}{\sqrt2}
\xrightarrow{X_B}
\frac{|01\rangle+|10\rangle}{\sqrt2}
\xrightarrow{Z_A}
\frac{|01\rangle-|10\rangle}{\sqrt2}
```

の順に作用させる。従って理想末端信号は

```math
\beta_{\rm s}
=
\frac1{\sqrt2}
\begin{pmatrix}
0&1&-1&0
\end{pmatrix}^{\mathsf T}
```

である。これは設定生成前に作る固定M52信号であり、$x,y$ をgate列へ入力しない。

1周期のclock順序を次とする。

1. M52で $v$ を作り、$\widetilde V=v$ をholdする。
2. 設定生成器から $x,y$ を得る。
3. $x$ を中央basis splitterとbranch latchへ入力する。
4. 選択blockをsource portへ保持し、R180Bを有限時間走らせる。
5. 中央couplerを切り、使用済みM52 sourceとbranch latchを結果形成から隔離する。
6. A、Bの局所分析器を作用させる。$y$ はこの段階でB側だけへ入る。
7. 2翼のR170を走らせ、局所結果または無反応を記録する。
8. 外部記録を残し、能動部をfresh cellへ交換する。

R176Cの直接計算基底instrumentとR180はM52の別々の末端interfaceである。同じ試行で両方を作動させず、Q2-1・Q2-3の判定は変更しない。

## 5.3 R180A：setting-pre条件付きblock抽出

行優先規約で、物理hold信号と解析上の規格化rayを

```math
\widetilde V=\operatorname{vec}_{\rm row}(\widetilde D),
\qquad
V=\operatorname{vec}_{\rm row}(D),
\qquad
D=\frac{\widetilde D}{r},
\qquad
\|V\|=1
```

とする。A設定 $x$ の正規直交固有basisを

```math
U_x
=
\left(
u_{+,x},u_{-,x}
\right)
```

とする。物理hold信号 $\widetilde V$ へ有限4mode unitary $U_x^\dagger\otimes I_2$ を作用させる。枝 $s\in\{+1,-1\}$ の物理的なB側2成分blockと、その解析上の規格化表示は

```math
\widetilde w_{s,x}
=
\widetilde D^{\mathsf T}\overline{u_{s,x}}
=
r w_{s,x}(V),
\qquad
w_{s,x}(V)
=
D^{\mathsf T}\overline{u_{s,x}}
```

となる。直交projectorとbranch作用を

```math
\Pi_s^x
=
|u_{s,x}\rangle\langle u_{s,x}|\otimes I_2,
\qquad
p_{s|x}(V)
=
V^\dagger\Pi_s^xV
=
\|w_{s,x}(V)\|^2
```

と定める。物理容量は $\widetilde w_{s,x}$ からlatchし、確率比だけを規格化ray $V$ で表す。$\Pi_+^x+\Pi_-^x=I_4$ なので

```math
p_{+|x}(V)+p_{-|x}(V)=1.
```

安全枝 $p_{s|x}>0$ ではreceiver方向を

```math
a_{s,x}=u_{s,x},
\qquad
b_{s,x}(V)
=
\frac{w_{s,x}(V)}{\sqrt{p_{s|x}(V)}}
```

と書く。式は方向を表すための解析表示であり、controllerが $w_{s,x}$ を数値読出しして除算する操作ではない。物理receiverでは選択された未規格化block $\widetilde w_{s,x}$ をsource portへ渡し、R180Bのpumpが動径を整える。

<!-- theorem-start:theorem -->
**定理（R180A：M52末端信号のsetting-pre条件付きblock抽出定理）**

零でないM52末端信号をcanonical SWAPで $\widetilde V=v$ とholdし、解析上だけ $V=\widetilde V/\|\widetilde V\|$ とする。A設定 $x$ に応じた $U_x^\dagger\otimes I_2$、R178Bの直交projector作用latch、R164の2枝作用殻、R161/R162の有限再平衡化を順に作用させる。R178Bがlatchする物理branch容量を

```math
J_s(\widetilde V,x)
=
\mathcal J_0
\widetilde V^\dagger\Pi_s^x\widetilde V
=
\mathcal J_0r^2p_{s|x}(V)
```

とする。すると共通radial因子は全容量による規格化で消え、理想内部枝は

```math
P(S=s\mid \widetilde V,x)
=
\frac{J_s}{J_++J_-}
=
p_{s|x}(V)
```

を持つ。安全枝でA方向 $a_{s,x}$、B方向 $b_{s,x}(V)$ を2翼局所instrumentへ渡すと、任意のB設定basis $u_{b,y}$ について

```math
P(S=s,B=b\mid V,x,y)
=
\left|
\left(
u_{s,x}^\dagger\otimes u_{b,y}^\dagger
\right)V
\right|^2.
```

B側の規格化縮約行列は

```math
\rho_B(V)=D^{\mathsf T}\overline D
```

であり、

```math
\sum_s
w_{s,x}(V)w_{s,x}(V)^\dagger
=
\rho_B(V)
```

だからB周辺は $x$ に依存しない。代数部分は厳密である。有限装置ではhold、basis splitter、projector latch、作用殻、混合、衝突、block保持の誤差と無反応を完全結果集合上で加える。
<!-- theorem-end:theorem -->

R180AはR178Bの一般projector latchを特殊化して使い、同じ機構を独立に再証明しない。$S$ はA結果の前駆体だが、外部結果は中央で直接記録せず、切断後のA局所R170が一意な記録を作る。

## 5.4 node切断とsinglet特殊化

一般の $V$ では $p_{s|x}$ が零または小さくなり得る。固定 $0<\tau<1/2$ に対し

```math
G_\tau(V,x,s)
=
\left\{
p_{s|x}(V)\geq\tau
\right\}
```

を安全事象とする。選択された枝が $G_\tau^c$ なら結果を無反応へ送り、成功試行だけを再規格化しない。二枝について切断質量は

```math
\sum_{s:p_{s|x}<\tau}p_{s|x}
\leq2\tau
```

である。$\|w\|\geq\sqrt\tau$ の安全域では $w\mapsto w/\|w\|$ のLipschitz定数を $C_\tau=O(\!\left(\tau^{-1/2}\right))$ で抑えられる。

singletでは係数行列を

```math
D_{\rm s}
=
\frac1{\sqrt2}
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}
=
\frac{\mathsf E}{\sqrt2}
```

と書ける。このとき

```math
w_{s,x}
=
-\frac1{\sqrt2}
\mathsf E\overline{u_{s,x}},
\qquad
p_{s|x}=\frac12,
\qquad
b_{s,x}
=
-\mathsf E\overline{u_{s,x}}.
```

最後のglobal signは局所rayと作用に影響しない。従って旧M48の等重みspin-flip fiberはR180Aのsinglet特殊化として回復される。$\tau<1/2$ ならsinglet枝にnode無反応はない。

## 5.5 2翼の局所matching

各翼のW型2モード埋込みを

```math
\Phi:
\mathbb C^2
\longrightarrow
\mathbb C^{|\Omega_W|},
\qquad
\Phi^\dagger\Phi=I_2
```

とする。単一試行の局所信号 $z\neq0$ に対して

```math
q_i(z)
=
\frac{|(\Phi z)_i|^2}{z^\dagger z},
\qquad
\pi_i^\delta(z)
=
\frac{q_i(z)+\delta r_i}{1+\delta},
\qquad
r_i>0,
\quad
\sum_ir_i=1
```

を置く。R164が作用殻状態数、R161が平方根型詳細釣合い率と有限混合、R162が固定信号に対する有限衝突近似を与える。ここで入力するのは各試行の $z_A,z_B$ であり、$V$ の集団平均ではない。

規格化方向 $c$ の強い局所fiber $\mathcal F_W^\delta(c)$ を

```math
z=e^{i\alpha}c,
\qquad
P(X=i\mid z)=\pi_i^\delta(z)
```

を満たす共同測度の族とする。R180の理想切断面fiberを

```math
\nu_{V,x}^0
=
\sum_{s=\pm1}
p_{s|x}(V)
\mathcal F_W^0(a_{s,x})
\mathbin{\widehat\otimes}
\mathcal F_W^0(b_{s,x}(V))
```

とする。$\widehat\otimes$ は枝 $s$ とpaired位相を共有し、局所粒子位置noiseは条件付き独立であることを表す。

連続bath座標は有限時間に目標rayへ厳密到達しないため、切断面の連続部分を全変動距離で比較しない。動径誤差、2翼の射影方向誤差、paired位相、枝不一致、離散粒子位置不一致を合わせた有界costのWasserstein距離 $d_{\rm fib}$ を使う。結果分布へ移すときだけ、固定有限設定族のcompact安全域上のLipschitz定数 $L_{\rm fib}$ を掛けて全変動誤差へ変換する。

## 5.6 R180B：source-driven paired-Hopf吸引

安全枝のtemplateを $a=a_{s,x}$、$b=b_{s,x}(V)$ と固定する。標準source loadでは、branch pointerで既知のA templateを選び、選択された未規格化M52 blockをB portへそのまま注入して

```math
z_A(0)=a,
\qquad
z_B(0)=w_{s,x}=\sqrt{p_{s|x}}\,b
```

とする。従って $p_A(0)=p_B(0)=0$ かつ

```math
m_0
=
\frac{1+\sqrt{p_{s|x}}}{2}>0,
\qquad
d_0
=
\frac{1-\sqrt{p_{s|x}}}{2}.
```

安全域 $p_{s|x}\geq\tau$ では $m_0\geq(1+\sqrt\tau)/2$ であり、吸引定理の非零条件は自動的に満たされる。この表示はB template係数の外部読出しを要求せず、物理port上のblock方向を解析的に $b$ と呼んでいるだけである。

一般の有限入口偏差も含め、receiver信号を

```math
z_A=c_Aa+p_A,
\qquad
z_B=c_Bb+p_B,
\qquad
a^\dagger p_A=b^\dagger p_B=0
```

と分け、

```math
m=\frac{c_A+\overline{c_B}}2,
\qquad
d=\frac{c_A-\overline{c_B}}2
```

と置く。逆表示は

```math
z_A=(m+d)a+p_A,
\qquad
z_B=(\overline m-\overline d)b+p_B
```

である。準備有効時間 $T_{\rm PH}$ に対し、決定論的開放流を

```math
\dot m
=
g(1-|m|^2)m,
\qquad
\dot d
=
-\kappa_{\rm p}d,
```

```math
\dot p_A
=
-\kappa_\perp p_A,
\qquad
\dot p_B
=
-\kappa_\perp p_B
```

とする。

<!-- theorem-start:theorem -->
**定理（R180B：M52 source-driven paired-Hopf receiver吸引定理）**

$m_0\neq0$、$a,b$ が準備窓中に保持され、初期状態が有界安全集合にあるとする。上の採用開放流では $\alpha=\arg m_0$ が保存され、

```math
|m(T_{\rm PH})|^2
=
\frac1{
1+
\left(
|m_0|^{-2}-1
\right)e^{-2gT_{\rm PH}}
},
```

```math
d(T_{\rm PH})
=
e^{-\kappa_{\rm p}T_{\rm PH}}d_0,
\qquad
p_{A,B}(T_{\rm PH})
=
e^{-\kappa_\perp T_{\rm PH}}p_{A,B}(0).
```

従って有限定数 $K_{180}<\infty$ と

```math
\gamma_{180}
=
\min
\left\{
2g,\kappa_{\rm p},\kappa_\perp
\right\}
```

を選び、

```math
\left\|
z_A-e^{i\alpha}a
\right\|
+
\left\|
z_B-e^{-i\alpha}b
\right\|
\leq
K_{180}e^{-\gamma_{180}T_{\rm PH}}
```

とできる。これは採用した開放方程式後の厳密結果であり、pump、sink、template holdを含む有限閉鎖Hamiltonianへの持ち上げを主張しない。
<!-- theorem-end:theorem -->

作用様量

```math
N_{\rm rec}
=
|m|^2+|d|^2+
\|p_A\|^2+
\|p_B\|^2
```

は

```math
\dot N_{\rm rec}
=
2g(1-|m|^2)|m|^2
-2\kappa_{\rm p}|d|^2
-2\kappa_\perp
\left(
\|p_A\|^2+
\|p_B\|^2
\right)
```

を満たす。第1項はbright pumpと飽和、第2項はpaired phase外成分のsink、第3項はtemplate直交成分のsinkである。選択block source、pump、sink、clockの総仕事・総熱・総エントロピー収支は閉じていない。

## 5.7 中央切断と局所instrument

R180B終了後の完全共通原因を

```math
\Lambda
=
\left(
V,x,S,\alpha,
z_A,z_B,X_A,X_B,H
\right)
```

とする。中央coupler、M52 hold、branch latchを切り離し、切断後生成子を

```math
\mathcal L_{\rm post}^{xy}
=
\mathcal L_A^x
+
\mathcal L_B^y
```

とする。各翼には中央branch作用殻と異なるfresh局所2枝作用殻を置く。完全共通原因に条件付けて

```math
\mu_{\rm sh}^{AB}
\left(
d\gamma_A,d\gamma_B
\mid
\Lambda,x,y
\right)
=
\mu_{{\rm sh},A}^x
\left(
d\gamma_A
\mid
\Lambda
\right)
\otimes
\mu_{{\rm sh},B}^y
\left(
d\gamma_B
\mid
\Lambda
\right)
```

とする。有限偏差を $\varepsilon_{\rm prod}$ として誤差台帳へ残す。

A分析器は $a_{s,x}=u_{s,x}$ を結果 $A=s$ の安全井戸へ写す。B分析器は $b_{s,x}(V)$ をbasis $u_{b,y}$ で分析する。分析器終了後に各局所信号を固定し、R161/R162の局所粒子位置bathとR170の収集、固定、記録を走らせる。切断後のA核は $y$、B核は反対翼の結果形成変数を参照しない。

## 5.8 理想共同分布と非信号性

理想fiberでは $A=s$ であり、

```math
P(B=b\mid S=s,V,x,y)
=
\left|
u_{b,y}^\dagger b_{s,x}(V)
\right|^2.
```

R180Aから

```math
P(A=a,B=b\mid V,x,y)
=
\left|
\left(
u_{a,x}^\dagger
\otimes
u_{b,y}^\dagger
\right)V
\right|^2.
```

A周辺は $y$ に依存せず、B周辺は $\rho_B(V)=D^{\mathsf T}\overline D$ に対する局所Born重みであり $x$ に依存しない。非信号性はsinglet対称性だけでなく、任意の規格化M52純粋信号について成立する。

singletでは

```math
P(A=a,B=b\mid x,y)
=
\frac14
\left(
1-ab\,\boldsymbol n_x\cdot\boldsymbol n_y
\right),
```

```math
E(A\mid x,y)
=
E(B\mid x,y)
=
0,
\qquad
E(AB\mid x,y)
=
-\boldsymbol n_x\cdot\boldsymbol n_y.
```

平面標準設定ではCHSH絶対値は $2\sqrt2$ である。

## 5.9 前向き誤差とR180C

理想規格化末端rayを $V_*$ とし、R176A/B、canonical SWAP、holdの有限誤差を規格化後に一度だけ

```math
\varepsilon_{\rm ray}^{52}
=
\inf_\phi
\left\|
\frac{\widetilde V}{\|\widetilde V\|}
-e^{i\phi}V_*
\right\|_2
```

へまとめる。規格化写像のLipschitz評価は $r\geq r_{\min}$ のsafe set上だけで使い、その外は無反応に含める。1設定対の完全結果分布に対する前向き誤差を

```math
\begin{aligned}
\varepsilon_{180}^{\rm cyc}
\leq{}&
\varepsilon_{\rm ray}^{52}
+\varepsilon_{\rm set}
+\varepsilon_{\rm split}
+\varepsilon_{\rm latch}
+2\tau\\
&+
C_\tau\varepsilon_{\rm block}
+L_{\rm fib}K_{180}
e^{-\gamma_{180}T_{\rm PH}}
+\frac{2\delta}{1+\delta}
+2C_Xe^{-\lambda_X^\delta T_X}\\
&+
\varepsilon_{\rm cut}
+\varepsilon_{\rm prod}
+\varepsilon_{170,{\rm rest}}^{A}
+\varepsilon_{170,{\rm rest}}^{B}
+\varepsilon_{\rm rec}
+\varepsilon_{\rm clk}
\end{aligned}
```

とする。$\varepsilon_{\rm ray}^{52}$ はR176A/Bのlift・gateとSWAP・holdが規格化rayへ与える誤差であり、状態依存除算を物理操作として数えない。radial偏差は $J_++J_-=\mathcal J_0\|\widetilde V\|^2$ を通じて必要な作用殻容量と混合時間を変えるが、枝容量比へは入らない。$\varepsilon_{\rm latch}$ は中央projector容量、作用殻、有限混合、衝突、内部枝固定、$\varepsilon_{\rm block}$ は選択block保持とtemplate portを表す。$\varepsilon_{170,{\rm rest}}^{A,B}$ は局所R170のうち、直前に明示した正則化、有限混合と、後ろに明示する記録・clockを除く作用殻、衝突、収集、固定の残差である。同じ有限段の誤差を二重に数えない。固定singletでは $p_s=1/2$ なので $\tau<1/2$ を選び、$2\tau$ のnode項を零にする。

<!-- theorem-start:theorem -->
**定理（R180C：M52駆動2端receiver合成、有限誤差、局所性監査、帰還）**

R180AのM52 signal hold、projector latch、branch作用殻、選択block port、R180Bのtemplate hold、pump、sink、2翼carrier、中央切断、および2つの局所R170が共通safe setと1つの有限clock schedule上で上式の各誤差以内に実行できるとする。完全結果集合を

```math
\Omega_{AB}
=
\left(
\{+1,-1\}\times\{+1,-1\}
\right)
\sqcup
\{\varnothing\}
```

とする。このとき実際の完全結果分布とR180Aの理想共同Born分布の全変動距離は $\varepsilon_{180}^{\rm cyc}$ 以下である。一側周辺の反対設定による差は高々 $2\varepsilon_{180}^{\rm cyc}$ である。singlet標準設定では

```math
\left|
|S_{180}|-2\sqrt2
\right|
\leq
8\varepsilon_{180}^{\rm cyc}.
```

従って

```math
\varepsilon_{180}^{\rm cyc}
<
\frac{\sqrt2-1}{4}
```

ならCHSH不等式の破れが残る。周期末に $r_{\rm ret}<1$ のfresh-cell交換を行えば、外部記録を保ったまま能動receiverを次周期入口の近傍へ戻せる。
<!-- theorem-end:theorem -->

R180Cは条件付き定理である。特に、M52 holdからprojector latchまでの反作用、branch pointerから未規格化block source portへの物理的routing、template portとpaired-Hopf pump・sinkの両立、中央切断後のfresh局所作用殻の積因子化、全窓を共有する単一clockは未統合である。有限閉鎖Hamiltonian liftはQ2-2の固定条件にしないが、上の開放装置境界を満たしたとはまだ主張しない。

## 5.10 Bell前提監査

| 監査項目 | R180 receiverでの位置 |
|---|---|
| 設定前測度 | M52 source、設定生成角、fresh cell、noise seedの基準測度は $x,y$ に依存しない |
| 設定の中央入力 | A設定 $x$ はR180Aのbasis splitter、projector latch、R180B template選択へ入る |
| 測定開始面 | 一般に $\mu_{\rm cut}(d\Lambda\mid V,x,y)=\mu_{V,x}(d\Lambda)$ であり、$x$ に依存する |
| B設定 | $y$ は中央準備へ入らず、切断後のB局所分析器へだけ入る |
| 切断後局所性 | 完全共通原因 $\Lambda$ に条件付けてA、Bの生成子、作用殻、noise、記録核を因子化する |
| 非信号性 | R180Aのprojector完全性から理想周辺は反対設定に依存しない。有限差は $2\varepsilon_{180}^{\rm cyc}$ 以下 |
| 結果の一意性 | 初期粒子位置と局所jump clock列を完全状態へ含めれば、局所記録は各試行で一意 |
| 無反応 | node、safe set外、overflow、有限混合・固定失敗を $\varnothing$ に残し、成功試行だけを再規格化しない |
| Bell前提 | 成立しない前提は測定設定独立性である。標準的な空間分離・自由設定Bell実験ではない |

共通原因を平均した共同分布から

```math
-\Theta
\log
P(A=a,B=b\mid x,y)
```

を作り、切断後の物理的な大域ポテンシャルとして局所率へ戻してはならない。反対翼設定の再注入となり、R180Cの条件付き局所因子化を壊す。

## 5.11 開放模型の局所帳簿

| 項目 | 明示する内容と限界 |
|---|---|
| M52 source | R176A/Bの有限Hamiltonian liftとgate列、実際の末端信号 $\widetilde V$、同次元holdを使う。canonical SWAPに規格化を含めず、末端anti-registerを共役信号に使わない |
| branch形成 | $U_x^\dagger\otimes I_2$、R178Bのprojector作用容量latch、R164の容量比に対する作用殻状態数、有限再平衡化を使う |
| paired-Hopf | bright pump、paired差mode sink、template直交sinkの採用開放方程式を明示する |
| 局所測定 | 切断後に2つのR170を使い、fresh作用殻、有限衝突bath、固定、局所記録を分離する |
| 仕事と熱 | R180Bの $N_{\rm rec}$ 収支は示すが、source、controller、pump、sink、切断器、記録、fresh交換を含む総収支は閉じない |
| 環境消去 | paired-Hopf driftとMarkov型局所粒子位置bathの有限閉鎖環境からの導出は行わない |
| 試行の数え方 | 無反応を完全結果へ含め、設定対ごとの全試行を分母とする |
| 反証条件 | block Born恒等式、B周辺独立性、paired吸引、切断後因子化、完全結果誤差のいずれかが破れれば対応するR180結果は成立しない |

## 5.12 弱開放帰還

能動receiver状態を $Y_n$、次周期のfresh基準状態を $Y_*$ とする。記録後に使用済みhold、branch latch、pump、sink、局所作用殻、衝突cellをspent側へ移し、fresh cellとの交換核がある距離 $d_{\rm ret}$ について

```math
E
\left[
d_{\rm ret}(Y_{n+1},Y_*)
\mid
Y_n
\right]
\leq
r_{\rm ret}
d_{\rm ret}(Y_n,Y_*),
\qquad
0\leq r_{\rm ret}<1
```

を満たすとする。この交換は使用済みcellを履歴なしに初期化する操作ではない。有限runでは必要数を初期bankへ積み、無期限runではcold inflowとspent outflowを仮定する。帰還誤差は次周期入口へ渡し、既に記録した同じ周期の分布へ遡って加えない。

## 5.13 有限時間と資源

固定2入力、固定有限設定族について必要な能動信号mode数は定数である。外部controllerが扱うのは、M52 lift・gate列、設定値、basis splitter種、branch窓、paired-Hopf窓、切断、2つの局所分析器、記録窓だけであり、$\widetilde V$ の4係数、$r$、または $\widetilde w_s$ の2係数を個別に読み出さない。

精度を上げると、M52 gate時間、hold品質、projector latch精度、作用殻容量、mixing時間、衝突cell数、paired-Hopf時間、W型粒子位置混合時間、fresh bank容量が増える。一般状態で $\tau\downarrow0$ とするとnode質量は減るが $C_\tau$ が発散する。固定singletでは $p_s=1/2$ なので、この交換をQ2-2のCHSH benchmarkへ持ち込む必要はない。

## 5.14 Q2-2判定と非主張

M52、setting-pre paired-Hopf receiver、M50と、R112、R161、R162、R164、R170、R176A--R176B、R178B、R180A--R180Cにより、固定singlet、固定有限設定族、準備先行、非空間分離、プロトコル面matching、無反応込み、採用開放法則、弱開放帰還という範囲で固定目標Q2-2を条件付き達成とする。

Q2-2の固定目標文言と独立判定規則は変更しない。現行の根拠構成がM52を共有するのであって、「Q2-1が達成ならQ2-2も達成」と推論しない。Q2-2はR180固有の条件と完全結果誤差から判定する。

本章は次を主張しない。

1. R180Cの全interfaceを1つの具体的開放装置または有限閉鎖Hamiltonianで統合したこと。
2. 準備終了後にA設定を自由に変更できること。
3. 標準的な空間分離・自由設定Bell実験を再現したこと。
4. 一般混合状態を単一試行信号と同一視したこと。
5. 任意のM52一般状態についてnodeなし・一様資源の完全2端装置を得たこと。
6. M52のanti-registerを末端共役信号として利用できること。
7. 総仕事、総熱、総エントロピー生成、無期限resetを閉じたこと。
8. Q2-3、M53/Q2-4、またはQ1--Q3のM0統合を同時に達成したこと。
