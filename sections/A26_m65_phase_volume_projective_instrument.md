@number: Z
@chapter: 付録
@title: M65 binary selector
@status: M65/R204はQ1のtwo-result first-passage binary instrument正本とする。未決定は第三の物理pointer状態ではなく、まだどちらのfirst eventも起きていないsurvival conditionとして扱う。Q2-2は付録WのM66/R205--R207、Q2 terminal multi-outcome readoutは付録XのM66/R206を用いる。

## Z.1 目的と責務境界

M65は、二結果直交射影に対して上流が保持した二作用から排他的な古典結果を作る最小open selectorである。複素信号そのものを再読出しせず、capture終了後に固定された二作用だけを入力とする。

M65/R204A・R204D--R204FをQ1のfixed-goal binary witnessへ採用する。R181Dは結果固定後のpost-state routerとしてQ1でM65へ接続し、R179は全周期reset/renewal側の一般部品として残す。Q2-2には付録WのM66/R205--R207を採用する。Q2-1/Q2-3/Q2-4のterminal readoutには付録XのM66/R206を採用する。旧R191/R193はM65へ責務を吸収した退役研究線としてnotes/Git履歴へ保存する。

M65の正本は、二つの結果channelの競合first-passage open lawである。結果状態は $+$ と $-$ の二つだけであり、decision開始後まだどちらのfirst eventも起きていない事象をsurvival conditionとして数える。有限decision時刻まで未決定なら完全結果 $\varnothing$ へ写す。指数Poisson raceはこのopen lawの最小witnessであり、将来のfinite-Hamiltonian physical parentにwaiting-time分布までの一致は要求しない。下流が要求する正本interfaceはR204Eのcomplete-result binary selector contractである。

旧R204B/R204Cのfixed-hub chamber / Hamiltonian--Brownian liftはこの正本から外し、旧M65 physical-lift strengtheningとしてnotes/Git履歴へ保存する。R205Dのfixed-hub capacity--conductance恒等式はM66側の数学的結果として残すが、現行M65のphysical liftとは扱わない。

## Z.2 入力作用、保持規約、安全領域

二結果直交射影 $P_++P_-=I$ に対する理想作用を

```math
J_\pm
=
\mathcal J_0 Z^\dagger P_\pm Z,
\qquad
S=J_++J_->0
```

とし、理想Born重みを

```math
p_\pm=\frac{J_\pm}{S}
```

とする。上流の作用保持終了後の値は

```math
A_\pm\geq0,
\qquad
A_\Sigma=A_++A_->0
```

を許す。exact射影固有状態では一方の作用が零でもよい。

```math
a_\pm=\frac{A_\pm}{A_*},
\qquad
a_\Sigma=a_++a_-,
\qquad
\widehat p_\pm=\frac{A_\pm}{A_\Sigma}
=\frac{a_\pm}{a_\Sigma}
```

と置く。作用保持誤差は

```math
D_{\rm TV}(\widehat p,p)\leq\varepsilon_A
```

だけで受け、M65内部で重複計上しない。

decision区間では

```math
\dot A_+=\dot A_-=0
```

をM65の入力契約とする。上流が保持値を正準対 $(A_r,P_r^A)$ で実装する場合、decisionに使った保持対は次のcaptureへそのまま戻さない。固定有限深さでは未使用保持対へ正準SWAPし、反復運転では使用済み保持対とその履歴をR179の流出経路へ渡す。

固定cutoff $0<\tau_{\rm cut}<1/2$ に対し、

```math
\min\{\widehat p_+,\widehat p_-\}\geq\tau_{\rm cut}
```

を通常経路とする。このcutoffはBorn結果を作るためではなく、R181Dへ渡す非空branchのnormを一様に下から抑えるために使う。exact endpointを含む通常経路外はZ.5の固定線形comparatorへ送る。

## Z.3 R204A：canonical two-result first-passage open selector

固定装置定数 $\kappa>0,A_*>0$ を取る。結果がまだ成立していないsurvival事象から、二つの結果channelへ

```math
\lambda_+
=
\kappa a_+,
\qquad
\lambda_-
=
\kappa a_-
```

という線形hazardを与える。

時刻 $t$ までどちらのfirst eventも起きていない確率を $s(t)$、時刻 $t$ までに結果 $r$ が最初に成立した確率を $x_r(t)$ とする。canonical open lawを

```math
\dot s
=
-\kappa a_\Sigma s,
\qquad
s(0)=1,
```

```math
\dot x_r
=
\kappa a_r s,
\qquad
x_r(0)=0,
\qquad
r\in\{+,-\}
```

と直接定める。

ここで $s$ は第三のpointer stateの占有確率ではない。「まだどちらのfirst eventも起きていない」というsurvival probabilityである。一度 $+$ または $-$ が成立した後に、未決定へ戻って再混合するrateは置かない。

<!-- theorem-start:theorem -->
**定理（R204A：M65 canonical two-result first-passage selector）**

上の発展則は

```math
s(t)
=
e^{-\kappa a_\Sigma t},
```

```math
x_r(t)
=
\frac{a_r}{a_\Sigma}
\left(
1-e^{-\kappa a_\Sigma t}
\right)
```

を与え、

```math
x_+(t)+x_-(t)+s(t)=1
```

を保存する。

装置へ入力される状態依存量は $a_+,a_-$ の二つだけであり、各入力は対応するlocal hazardへ線形に入る。物理制御器は $a_r/a_\Sigma$、Born確率表、振幅表を入力として必要としない。

また $A_\pm$ はdecision区間で固定入力なので、M65自身は走行信号 $Z$ を変更せず、結果形成とprojector routerの責務を分離する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R204A）**

survival equationを積分すれば $s(t)=e^{-\kappa a_\Sigma t}$ を得る。これを $\dot x_r=\kappa a_rs$ へ代入して $x_r(0)=0$ から積分すると表示式を得る。三式を加えれば確率保存が従う。hazardには $a_+,a_-$ と固定係数 $\kappa$ しか現れず、装置入力として $a_\Sigma$ による除算を必要としない。証明終。
<!-- theorem-end:proof -->

この指数Poisson raceはM65 open lawの一つの明示的pathwise witnessである。後続のphysical parentがR204Eのcomplete-result kernelを同じ精度で満たす場合、first-passage waiting-time lawそのものを指数分布へ一致させることは要求しない。

## Z.4 R204D：有限時間Born readout

<!-- theorem-start:theorem -->
**定理（R204D：M65有限時間Born readout）**

decision時刻 $T>0$ で、時刻 $T$ までにfirst eventが成立したwinnerを $+$ または $-$ へ、まだfirst eventがないsurvival事象を $\varnothing$ へ写す。canonical M65結果分布 $P_{65}^0(T)$ は

```math
P_{65}^0(T;r)
=
\widehat p_r
\left(
1-e^{-\kappa a_\Sigma T}
\right),
\qquad
r\in\{+,-\},
```

```math
P_{65}^0(T;\varnothing)
=
e^{-\kappa a_\Sigma T}
```

を満たす。

従って保持作用比から作る完全理想結果分布

```math
K_{\widehat p}
=
(\widehat p_+,\widehat p_-,0)
```

に対し、

```math
D_{\rm TV}
\left(
P_{65}^0(T),
K_{\widehat p}
\right)
=
e^{-\kappa a_\Sigma T}.
```

安全運用域

```math
a_\Sigma\geq a_{\min}>0
```

では

```math
D_{\rm TV}
\left(
P_{65}^0(T),
K_{\widehat p}
\right)
\leq
e^{-\kappa a_{\min}T}.
```

上流作用保持誤差 $\varepsilon_A$、具体hazard実装を選んだ場合のfinite-time law誤差を保守的に $T\varepsilon_{\rm rate}$、record/clock/closure誤差を $\varepsilon_{\rm rec}$ とすると、

```math
D_{\rm TV}
(
P_{65}(T),
P_{\rm Born}
)
\leq
\varepsilon_A
+
e^{-\kappa a_{\min}T}
+
T\varepsilon_{\rm rate}
+
\varepsilon_{\rm rec}.
```

canonical open lawそのものでは $\varepsilon_{\rm rate}=0$ とする。無反応を捨てて成功結果だけを再規格化しない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R204D）**

R204Aの閉形式を $t=T$ で評価すればcomplete-result lawを得る。理想分布との差は、左右の欠損質量の総和と $\varnothing$ 質量がいずれも同じsurvival massから生じるため、全変動距離はちょうど $e^{-\kappa a_\Sigma T}$ である。安全運用域では $a_\Sigma\geq a_{\min}$ を代入する。上流保持誤差、具体実装誤差、record誤差は三角不等式で一度だけ加える。証明終。
<!-- theorem-end:proof -->

特に $\widehat p_-$ が極端に小さくても、total decision hazardは

```math
\lambda_++\lambda_-
=
\kappa a_\Sigma
```

であり、最小Born重みには依存しない。指定 $\varepsilon_{\rm dec}>0$ に対し、

```math
T_{65}
\geq
\frac{1}{\kappa a_{\min}}
\log
\frac{1}{\varepsilon_{\rm dec}}
```

と選べばsurvival errorを $\varepsilon_{\rm dec}$ 以下にできる。

### Z.4.1 decision終了時の有限record/latch

二つのfirst-passage時刻を $\tau_+,\tau_-$ とし、

```math
\tau
=
\min\{\tau_+,\tau_-\}
```

とする。

```math
\tau_+<\tau_-,
\quad
\tau_+\leq T
\quad\Longrightarrow\quad
Y=+,
```

```math
\tau_-<\tau_+,
\quad
\tau_-\leq T
\quad\Longrightarrow\quad
Y=-,
```

```math
\tau>T
\quad\Longrightarrow\quad
Y=\varnothing.
```

first eventが $T$ より前に成立した場合、そのwinnerを内部latchで保持し、正式なR112型有限局所recordへのコピーとR181D routerの開放は固定decision時刻 $T$ の後に行う。理想recordではこの写像は結果分布を変えない。有限record、clock、decision closureの完全結果誤差をまとめて $\varepsilon_{\rm rec}$ とする。

record後の $Y$ はR181D routerを開く前に固定される。$Y=\varnothing$ ならどちらのrouterも開かない。winner latch、record作業領域、使用済み保持対を反復使用する場合はR179のopen resetへ渡す。

このlatchは新しいBorn確率源ではない。R204Aのfirst-passage winnerまたは有限時間survival事象を有限記録へ固定し、以後のdecision dynamicsから切り離すだけである。

## Z.5 endpoint comparator、安全下限、使用済み保持対

exact endpoint $A_+=0<A_-$ では $\lambda_+=0$、$A_-=0<A_+$ では $\lambda_-=0$ なので、canonical first-passage law自体が誤ったbranchを生成しない。

一方、R181Dの測定後状態方向誤差を一様に制御するため、一般のcutoff領域では小さいbranchをsafe routerへ渡さない。例えば

```math
\widehat p_+<\tau_{\rm cut}
```

は

```math
(1-\tau_{\rm cut})A_+
-
\tau_{\rm cut}A_-<0
```

と同値なので、状態依存除算ではなく固定係数の線形比較器で判定できる。逆側も同様である。cutoff領域では大きい側へ決定論的に固定する。

比較器とrecordの完全結果誤差を $\varepsilon_{\rm cmp},\varepsilon_{\rm rec}$ とすると、

```math
\varepsilon_{65}^{\rm edge}
\leq
\tau_{\rm cut}
+
\varepsilon_A
+
\varepsilon_{\rm cmp}
+
\varepsilon_{\rm rec}.
```

通常経路の一様上界は

```math
\varepsilon_{65}^{\rm int}
=
\varepsilon_A
+
e^{-\kappa a_{\min}T}
+
T\varepsilon_{\rm rate}
+
\varepsilon_{\rm rec}.
```

従って

```math
\varepsilon_{65}
=
\max
\{
\varepsilon_{65}^{\rm int},
\varepsilon_{65}^{\rm edge}
\}.
```

非空結果の理想作用重みには

```math
p_r
\geq
\tau_{\rm state}^{65}
:=
\tau_{\rm cut}-\varepsilon_A
>0
```

という安全下限を与える。

使用済み保持対はdecision履歴を持ち得るため再captureへ直結しない。固定有限深さでは未使用保持対へSWAPし、反復運転ではR179へ排出する。

## Z.6 R204E：binary selector contract

R181Dが上流selectorに要求する共通契約を、完全結果集合 $\{0,1,\varnothing\}$ 上で次のように書く。

1. 理想作用比は $p_b=A_b/(A_0+A_1)$。
2. 実selector核と理想Born核の全変動距離が $\varepsilon_{\rm sel}$ 以下。
3. 非空安全結果 $Y=b$ では $p_b\geq\tau_{\rm state}>0$。
4. decision終了時に $Y$ をR112型有限recordへ固定してからprojector routerを開く。
5. $\varnothing$ を捨てて再規格化しない。

<!-- theorem-start:corollary -->
**系（R204E：M65はbinary selector contractを満たす）**

M65では

```math
\varepsilon_{\rm sel}=\varepsilon_{65},
\qquad
\tau_{\rm state}=\tau_{\rm state}^{65}
```

と取れば上のbinary selector contractを満たす。従ってR181Dをselector非依存の形で適用できる。

R204Eが要求するのはcomplete-result kernelと結果固定interfaceであり、selector内部のwaiting-time lawや物理実装には依存しない。従って後続physical parentはM65の指数Poisson waiting-time分布そのものではなく、このcontractを有限誤差で回収すればよい。

Q1 fixed-goal witnessにはM65を使う。
<!-- theorem-end:corollary -->

## Z.7 R204F：Q1互換性と有限latency

<!-- theorem-start:theorem -->
**定理（R204F：Q1 M65 interfaceと有限latency条件）**

Q1ではR189Aの保持済み作用 $A_L,A_R$ をM65へ入力できる。R189A作用比誤差を $\varepsilon_{189A}$、M65 selector誤差を $\varepsilon_{65}^{\rm mid}$、保持中心時刻からR181D完了までのRabi重み変化を $\varepsilon_{\rm lat}$ とすれば、

```math
\varepsilon_{189B,65}^{\rm dist}
\leq
\varepsilon_{189A}
+
\varepsilon_{65}^{\rm mid}
+
\varepsilon_{\rm lat}.
```

安全運用域 $a_\Sigma\geq a_{\min}>0$ では、指定decision error $\varepsilon_{\rm dec}$ に対して

```math
T_{65}
\geq
\frac{1}{\kappa a_{\min}}
\log
\frac{1}{\varepsilon_{\rm dec}}
```

と有限に選べる。固定有限回Zeno証人では、この $T_{65}$ を先に固定した後、

```math
\Omega_\kappa T_{65}\longrightarrow0
```

の弱結合極で追加latencyを任意に小さくできる。この結果をQ1 fixed-goal witnessのM65接続として採用する。

Q2-1/Q2-3/Q2-4のterminal readout資源はR206C--R206Eへ移し、R204Fから一般回路の逐次node数、作用下限、polynomial readout-time責務を外す。
<!-- theorem-end:theorem -->

### Z.7.1 Q1 retirement-readiness合成

R189Aのcapture終了後は $H_{\rm cap}=0$ であり、保持済み $A_L,A_R$ は走行中W2信号から切り離されている。M65はこの二作用だけを入力としてdecisionを行い、Z.4.1のrecordで $Y\in\{L,R,\varnothing\}$ を固定した後にR181Dへ渡せる。

従ってQ1の中間測定候補を

```math
\mathrm{R189A}
\longrightarrow
\mathrm{M65/R204D}
\longrightarrow
\mathrm{R112\ record}
\longrightarrow
\mathrm{R181D}
```

と合成できる。保持中心時刻からrouter完了までの有限latencyを従来どおり $\varepsilon_{\rm lat}$ に入れれば、

```math
\varepsilon_{189B,65}^{\rm dist}
\leq
\varepsilon_{189A}
+
\varepsilon_{65}^{\rm mid}
+
\varepsilon_{\rm lat}
```

を使える。

空操作対照ではR189A、M65 decision、record、clock、待ち時間を測定運転と同じにし、R181D routerだけを開かない。M65はcapture終了後のW2信号 $Z$ を状態変数として読まないので、理想保持条件ではこの空操作のW2信号は自由零傾斜Rabi信号を継続する。固定精度で $T_{65}$ を有限に選び、R187の弱結合極限で

```math
\Omega_\kappa T_{65}\to0
```

とすれば、従来R189Cの有限2回Zeno比較へ必要なlatencyを任意に小さくできる。

この合成をR143/R144/R189B/R189Cの現行fixed-goal証人へ採用する。

## Z.8 正本と強化課題の境界

M65の正本はR204Aのtwo-result first-passage open law、R204Dの有限時間Born誤差、cutoff comparator、R204Eのbinary selector contract、R204FのQ1 interfaceで閉じる。

旧R204Bのfixed-hub phase-volume chamberとR204CのHamiltonian--Brownian liftは旧3状態M65の追加physical-lift strengtheningとして退役し、notes/Git履歴へ保存する。結果ID R204B/R204Cは再利用しない。現行M65のfinite-Hamiltonian physical liftはこのPRでは定めず、後続M67/R211で扱う。

旧R191/R193はM65へ責務を吸収したため現行主線から退役する。exact endpoint、有限record/latch、Q1空操作対照を含むfixed-goal主線は本付録で閉じる。
