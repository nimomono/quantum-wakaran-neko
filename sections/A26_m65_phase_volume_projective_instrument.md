@number: Z
@chapter: 付録
@title: M65 phase-volume型3状態open射影読出し
@status: Q1/Q2二結果射影用の現行fixed-goal canonical open selector model。正本発展則は保持済み二作用を線形rateへ入れる3状態連続時間Markov過程とし、exact endpoint、有限decision後のR112型record/latch、R204Dの有限時間Born誤差、R204Eの共通binary selector contract、R204FのQ1/Q2-4接続と資源条件を備える。R204A--R204Cのphase-volume chamber/Hamiltonian構成は追加実現・持上げであり、M65正本の成立条件にしない。 Z.11にM66/R205--R206のmulti-outcome common-reservoir readoutをactive replacement candidateとして併置するが、現行M65/R181D/R192/R179主線は変更しない。

## Z.1 目的と責務境界

M65は、二結果直交射影に対して上流が保持した二作用から排他的な古典結果を作る最小open selectorである。複素信号そのものを再読出しせず、capture終了後に固定された二作用だけを入力とする。

M65/R204D--R204FをQ1/Q2のfixed-goal witnessへ採用する。R181D、R192、R179、R180A/R180Cはselector非依存のinterfaceを通してM65へ接続する。旧R191/R193はM65へ責務を吸収した退役研究線としてnotes/Git履歴へ保存する。

M65の正本は開放3状態Markov過程そのものである。固定chamber、phase-volume oscillator、調和bath、Fick--Jacobs縮約は正本の定義ではなく、R204B/R204Cに置く追加の物理実現・Hamiltonian liftである。

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

を通常経路とする。この条件の下では両作用は自動的に正である。$A_+=0$ または $A_-=0$ を含む通常経路外はZ.7のendpoint comparatorへ送り、3状態decision lawを通す必要はない。

## Z.3 R204A：canonical 3状態open selector

pointer状態を

```math
X_t\in\{+,H,-\}
```

とする。$H$ は中央の未決定状態であり、decision終了時には正式な無反応 $\varnothing$ へ写す。固定装置定数 $\Lambda>0,\kappa>0,A_*>0$ を取り、通常経路では連続時間Markov rateを

```math
k_{+\to H}=k_{-\to H}=\Lambda,
\qquad
k_{H\to +}=\kappa a_+,
\qquad
k_{H\to -}=\kappa a_-,
```

それ以外を零と直接定める。

確率を

```math
x_+(t)=P(X_t=+),
\qquad
x_-(t)=P(X_t=-),
\qquad
h(t)=P(X_t=H)
```

とすると、

```math
\dot x_r
=
-\Lambda x_r+\kappa a_r h,
\qquad
r\in\{+,-\},
```

```math
\dot h
=
\Lambda(x_++x_-)-\kappa a_\Sigma h.
```

<!-- theorem-start:theorem -->
**定理（R204A：M65 canonical open selector）**

上の発展則は確率単体を保存する古典連続時間Markov過程を定める。装置へ入力される状態依存量は $a_+,a_-$ の二つだけであり、各入力はrateへ線形に入る。物理制御器は $a_r/a_\Sigma$、Born確率表、振幅表を入力として必要としない。

また $A_\pm$ はdecision区間で固定入力なので、M65自身は走行信号 $Z$ を変更せず、結果形成とprojector routerの責務を分離する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R204A）**

全rateは非負であり、generatorの各行和は零である。上のmaster equationを加えると

```math
\frac{d}{dt}(x_++x_-+h)=0
```

だから確率単体を保存する。rate式には $a_+,a_-$ と固定係数しか現れず、$a_\Sigma$ による除算はない。証明終。
<!-- theorem-end:proof -->

## Z.4 R204B：fixed-hub phase-volume実現候補

R204Aはopen lawそのものを正本とする。この節は同じlawを受動phase-volume構造から作る追加実現候補であり、M65の定義には使わない。

固定された左右chamber $C_\pm$、neck $N_\pm$、hub $H$ を取り、局所phase-volume factorを概念的に

```math
\Phi_A(Q)
=
\begin{cases}
a_+\phi_C(Q),&Q\in C_+,\\
a_+\phi_N(Q),&Q\in N_+,\\
\phi_H(Q),&Q\in H,\\
a_-\phi_N(Q),&Q\in N_-,\\
a_-\phi_C(Q),&Q\in C_-,
\end{cases}
```

とする。hubのphase volumeは作用に依存させない。

R203Bと同じ調和自由度のcanonical積分を使えば、局所Gibbs容量はphase-volume factorへ比例する。左右共通の基準量 $V_C^0,G_0,V_H^0>0$ に対して

```math
V_r=a_rV_C^0,
\qquad
G_r=a_rG_0,
\qquad
V_H=V_H^0
```

を得る場合、

```math
\frac{G_r}{V_r}
=
\frac{G_0}{V_C^0}
=:\Lambda,
\qquad
\frac{G_r}{V_H}
=
\frac{G_0}{V_H^0}a_r
=:\kappa a_r.
```

<!-- theorem-start:theorem -->
**定理（R204B：fixed-hub matched capacity--conductance realization）**

上記capacity/conductance relationsを満たすwell-mixed chamber reductionでは、左右chamberとhubのcoarse generatorはR204Aのcanonical open generatorと一致する。従ってphase-volume構造は、Born比を外部計算せずR204Aを実装する一つの物理候補を与える。
<!-- theorem-end:theorem -->

R204BはM65正本の必須依存ではない。

## Z.5 R204C：Hamiltonian--Brownian lift strengthening

R204Bの固定幾何を明示Hamiltonian、有限帯域bath、Brownian/Smoluchowski過程から導く場合だけこの結果を使う。対象時間窓 $0\leq t\leq T$ で、

```math
\varepsilon_{\rm bath},
\quad
\varepsilon_{\rm od},
\quad
\varepsilon_{\rm pv},
\quad
\varepsilon_{\rm tube},
\quad
\varepsilon_{\rm lump},
\quad
\varepsilon_{\rm cal}
```

を、それぞれbath、overdamped、phase-volume tracking、tube reduction、well-mixed lumping、capacity/conductance較正の誤差とする。

```math
\varepsilon_{\rm gen}
=
\varepsilon_{\rm bath}
+\varepsilon_{\rm od}
+\varepsilon_{\rm pv}
+\varepsilon_{\rm tube}
+\varepsilon_{\rm lump}
+\varepsilon_{\rm cal}.
```

<!-- theorem-start:theorem -->
**定理（R204C：Hamiltonian--Brownian liftの有限時間誤差）**

具体実装のcoarse lawを $\widetilde\nu_t$、R204Aのcanonical lawを $\nu_t$ とする。初期lumping誤差を $\varepsilon_{\rm init}$ とし、対象時間窓でgenerator差の全変動作用normが一様に $\varepsilon_{\rm gen}$ 以下なら、

```math
\sup_{0\leq t\leq T}
D_{\rm TV}
(
\widetilde\nu_t,\nu_t
)
\leq
\varepsilon_{\rm init}
+
T\varepsilon_{\rm gen}
=:
\varepsilon_{204C}(T).
```

これはR204AのHamiltonian/Brownian実現を評価する強化結果であり、R204A/R204D/R204E/R204Fの成立条件ではない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R204C）**

Markov半群の全変動縮約性とDuhamel展開を使い、generator差を時間積分する。証明終。
<!-- theorem-end:proof -->

## Z.6 R204D：有限時間Born readout

通常経路で

```math
h(0)=0,
\qquad
x_+(0)+x_-(0)=1
```

とする。

<!-- theorem-start:theorem -->
**定理（R204D：M65有限時間Born readout）**

R204Aのcanonical open lawでは

```math
h(t)
=
\frac{\Lambda}
{\Lambda+\kappa a_\Sigma}
\left[
1-e^{-(\Lambda+\kappa a_\Sigma)t}
\right].
```

さらに

```math
d_r(t)
:=
x_r(t)-\widehat p_r[1-h(t)]
```

と置くと

```math
\dot d_r=-\Lambda d_r,
```

従って

```math
x_r(t)
-
\widehat p_r[1-h(t)]
=
e^{-\Lambda t}
[x_r(0)-\widehat p_r].
```

decision時刻 $T$ で

```math
+\mapsto +,
\qquad
-\mapsto -,
\qquad
H\mapsto\varnothing
```

と完全結果へ写すと、canonical M65結果分布 $P_{65}^0(T)$ は

```math
D_{\rm TV}
\left(
P_{65}^0(T),
(\widehat p_+,\widehat p_-,0)
\right)
\leq
e^{-\Lambda T}
D_{\rm TV}(x_0,\widehat p)
+
\frac{\Lambda}
{\Lambda+\kappa a_\Sigma}.
```

上流作用保持誤差 $\varepsilon_A$、具体rate実装を選んだ場合のgenerator誤差 $\varepsilon_{\rm rate}$、record誤差 $\varepsilon_{\rm rec}$ を加えると、

```math
D_{\rm TV}
(
P_{65}(T),
P_{\rm Born}
)
\leq
\varepsilon_A
+
e^{-\Lambda T}
D_{\rm TV}(x_0,\widehat p)
+
\frac{\Lambda}
{\Lambda+\kappa a_\Sigma}
+
T\varepsilon_{\rm rate}
+
\varepsilon_{\rm rec}.
```

canonical open lawそのものでは $\varepsilon_{\rm rate}=0$ とする。無反応を捨てて成功結果だけを再規格化しない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R204D）**

$x_++x_-=1-h$ より

```math
\dot h
=
\Lambda-(\Lambda+\kappa a_\Sigma)h
```

だから $h(t)$ の表示を得る。また $a_r=\widehat p_r a_\Sigma$ を使えば、R204Aのmaster equationから $\dot d_r=-\Lambda d_r$ が従う。完全結果分布との差に三角不等式を使い、

```math
h(T)
\leq
\frac{\Lambda}{\Lambda+\kappa a_\Sigma}
```

で抑える。具体実装誤差はMarkov半群の縮約性とDuhamel評価で $T\varepsilon_{\rm rate}$ を一度だけ加える。証明終。
<!-- theorem-end:proof -->

特に $\widehat p_-$ が極端に小さくても、結果比へ近づくモードのrateは $\Lambda$ のままである。小Born重みそれ自体は指数decision時間を生まない。


### Z.6.1 decision終了時の有限record/latch

decision窓 $[0,T]$ の終了時にM65 generatorを閉じ、それ以後のselector jump rateを零にする。時刻 $T$ のpointer状態を

```math
X_T=+
\mapsto
Y=+,
\qquad
X_T=-
\mapsto
Y=-,
\qquad
X_T=H
\mapsto
Y=\varnothing
```

とR112型の有限局所recordへ写す。理想recordではこの写像は結果分布を変えない。有限record、clock、gate-closureの完全結果誤差をまとめて $\varepsilon_{\rm rec}$ とする。

record後の $Y$ はR181D routerを開く前に固定される。$Y=\varnothing$ ならどちらのrouterも開かない。selector pointer、record作業領域、使用済み保持対を反復使用する場合はR179のopen resetへ渡す。

このlatchは新しいBorn確率源ではなく、R204Dが時刻 $T$ に持つ古典pointer状態を有限記録へコピーして以後のdecision dynamicsから切り離すだけである。

## Z.7 endpoint comparator、安全下限、使用済み保持対

通常経路外では大きい側へ決定論的endpointを開く。exact endpoint $A_+=0<A_-$ では結果 $-$、$A_-=0<A_+$ では結果 $+$ を直接固定する。一般のcutoff領域では例えば

```math
\widehat p_+<\tau_{\rm cut}
```

は

```math
(1-\tau_{\rm cut})A_+
-
\tau_{\rm cut}A_-<0
```

と同値なので、状態依存除算ではなく固定係数の線形比較器で判定できる。逆側も同様である。

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
e^{-\Lambda T}
+
\frac{\Lambda}{\Lambda+\kappa a_{\min}}
+
T\varepsilon_{\rm rate}
+
\varepsilon_{\rm rec},
```

ここで安全運用域で $a_\Sigma\geq a_{\min}>0$ とする。

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

## Z.8 R204E：binary selector contract

R181Dが上流selectorに要求する共通契約を、完全結果集合 $\{0,1,\varnothing\}$ 上で次のように書く。

1. 理想作用比は $p_b=A_b/(A_0+A_1)$。
2. 実selector核と理想Born核の全変動距離が $\varepsilon_{\rm sel}$ 以下。
3. 非空安全結果 $Y=b$ では $p_b\geq\tau_{\rm state}>0$。
4. decision終了時にgeneratorを閉じ、$Y$ をR112型有限recordへ写してからprojector routerを開く。
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

fixed-goal witnessにはM65を使う。
<!-- theorem-end:corollary -->

## Z.9 R204F：Q1互換性とQ2-4読出し資源

<!-- theorem-start:theorem -->
**定理（R204F：Q1互換性とQ2-4 polynomial readout-time条件）**

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

M65 decision時間を $T_{65}$ とすると、固定有限回Zeno証人では

```math
\Omega_\kappa T_{65}\longrightarrow0
```

の弱結合極で追加latencyを任意に小さくできる。この結果をQ1 fixed-goal witnessのM65接続として採用する。

Q2-4では二結果node数を $m$、全読出し誤差予算を $\epsilon$ とする。各nodeのmixing項へ $O(\epsilon/m)$ を割り当てる十分条件は

```math
T_{\rm node}
\geq
\frac1\Lambda
\log\frac{Cm}{\epsilon}.
```

さらに

```math
\frac{\Lambda}{\kappa a_{\min}}
=
O\left(\frac{\epsilon}{m}\right),
\qquad
\varepsilon_A,
\varepsilon_{\rm cmp},
\varepsilon_{\rm rec},
T_{\rm node}\varepsilon_{\rm rate}
=
O\left(\frac{\epsilon}{m}\right)
```

を一様に満たすとする。$m,\Lambda^{-1},\kappa^{-1},a_{\min}^{-1}$ と必要な固定装置precisionが $n,d,1/\epsilon$ の多項式で抑えられるなら、

```math
T_{\rm read,total}
=
O\left(
\frac{m}{\Lambda}
\log\frac{m}{\epsilon}
\right)
```

は多項式である。

この結論はM65 readout自身から指数時間が生じないことを示すが、R186の指数個signal modeに対する加法noise/precision障害を解決しない。一般深さで $a_\Sigma$ の絶対下限が必要ならR192作用安定化を使える。
<!-- theorem-end:theorem -->


### Z.9.1 Q1 retirement-readiness合成

R189Aのcapture終了後は $H_{\rm cap}=0$ であり、保持済み $A_L,A_R$ は走行中W2信号から切り離されている。M65はこの二作用だけを入力としてdecisionを行い、Z.6.1のrecordで $Y\in\{L,R,\varnothing\}$ を固定した後にR181Dへ渡せる。

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

## Z.10 正本と強化課題の境界

M65の正本はR204Aのopen generator、R204Dの有限時間Born誤差、endpoint comparator、R204Eのbinary selector contractで閉じる。

R204Bのphase-volume chamber、R204CのHamiltonian--Brownian lift、finite-bandwidth bath、direct Brownian trajectory、具体回路化は追加の物理実現・A2/B系強化課題である。これらをM65の正本性やfixed-goal達成判定の前提にしない。

旧R191/R193はM65へ責務を吸収したため現行主線から退役する。exact endpoint、有限record/latch、Q1空操作対照を含むfixed-goal主線は本付録で閉じる。

## Z.11 M66共通phase-volume reservoirとQ2多結果readout候補

M66は、古典coherent signalの局所作用を一つのthermal reservoirのphase volumeへ受動的に写し、排他的な古典configurationを標本化する共通open模型候補である。

本付録で扱う実体は次の三種類だけとする。

1. classical coherent signal $Z=(Z_y)_{y\in\Omega_L}$。
2. classical resolved configuration $X\in\Omega_L\cup\{H\}$。
3. one thermal reservoir。各結果channelへ同じ局所規則で接続され、channelごとのBorn表、振幅表、較正係数表を外部入力として受け取らない。

ここで $H$ は未決定hubである。複素信号、局所作用、phase-volume scale、Markov rateは派生量であり、独立の量子実体ではない。

本付録はQ2末端readoutの候補を与える。Q1逐次測定、Q2-2現行A端--B端逐次interface、M65/R181D/R192/R179の現行fixed-goal責務は本変更では置換しない。

### Z.11.1 R205A：共通phase-volume identity

signalから得る正の局所scaleを $w>0$ とする。reservoir内部自由度を $(\zeta_\alpha,\Pi_\alpha)$ とし、

```math
H_{\rm res}(w)
=
\sum_{\alpha}
\left[
\frac{\Pi_\alpha^2}{2m_\alpha}
+
\frac{m_\alpha\omega_\alpha^2}{2}
\left(
\lambda_\alpha(w)\zeta_\alpha-d_\alpha R
\right)^2
\right],
```

```math
\lambda_\alpha(w)=w^{-q_\alpha},
\qquad
q_\alpha>0,
\qquad
\sum_\alpha q_\alpha=1
```

とする。

<!-- theorem-start:theorem -->
**定理（R205A：共通phase-volume identity）**

固定 $w>0$ と $R$ に対するcanonical積分は

```math
Z_{\rm res}(w,R)
=
Z_{\rm res}^0\,w
```

を満たす。従って

```math
F_{\rm res}(w)
=
-k_BT\log w+C
```

である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R205A）**

各modeで $Q_\alpha=\lambda_\alpha\zeta_\alpha-d_\alpha R$ と変数変換する。Gaussian積分の $w$ 依存性は

```math
\prod_\alpha\lambda_\alpha^{-1}
=
w^{\sum_\alpha q_\alpha}
=
w
```

だけである。証明終。
<!-- theorem-end:proof -->

R203Bは $w=r_X^\delta/r_*$ の特殊化、R204Bは二結果の局所scaleをcapacity/conductanceへ共通に入れる特殊化として読める。

### Z.11.2 R205B：matched capacity--conductance原理

結果channel $y$ のwell-mixed capacityを $V_y$、hubとのconductanceを $G_y$、hub capacityを $V_H$ とする。固定装置定数 $V_0,G_0,V_H^0>0$ に対し

```math
V_y=V_0s_y,
\qquad
G_y=G_0s_y
```

とする。

<!-- theorem-start:theorem -->
**定理（R205B：matched capacity--conductance原理）**

上の一様scale則では

```math
k_{y\to H}
=
\frac{G_y}{V_y}
=
\frac{G_0}{V_0}
=:\Lambda
```

となり、channelからhubへのrateは $s_y$ と結果数に依存しない。

hubからchannelへのrateは

```math
k_{H\to y}
=
\frac{G_y}{V_H}
```

であり、$V_H$ の一様scaleを選ぶことで局所 $s_y$ をそのまま標本化rateへ写せる。
<!-- theorem-end:theorem -->

この構成では外部制御器が比 $s_y/\sum_zs_z$ を計算する必要はない。

### Z.11.3 R205C--R205D：M64/M65との共通原理

R205Aの $w$ をM64 continuous profileの $r_X^\delta/r_*$ と同定すればR203Bの

```math
F_{\rm res}
=
-k_BT\log r_X^\delta+C
```

を回収する。これをR205Cと呼ぶ。

二結果 $y\in\{+,-\}$ で $s_y=a_y$、$V_H=V_H^0$ とすれば

```math
k_{H\to y}
=
\frac{G_0}{V_H^0}a_y
```

となり、R204Bのmatched capacity--conductance構造を回収する。これをR205Dと呼ぶ。

R205C/R205Dは既存M64/M65の定理を置換せず、共通phase-volume原理への埋込みだけを主張する。

### Z.11.4 R206A：有限L結果common-hub sampler

有限結果集合を

```math
\Omega_L=\{1,\ldots,L\}
```

とする。非負作用 $a_y\ge0$ と

```math
a_\Sigma=\sum_{y=1}^La_y>0
```

を取り、

```math
p_y=\frac{a_y}{a_\Sigma}
```

とする。

canonical open samplerを

```math
k_{y\to H}=\Lambda,
\qquad
k_{H\to y}=\kappa a_y
```

で定める。確率を $x_y(t)=P(X_t=y)$、$h(t)=P(X_t=H)$ とすると

```math
\dot x_y
=
-\Lambda x_y+\kappa a_yh,
```

```math
\dot h
=
\Lambda(1-h)-\kappa a_\Sigma h.
```

<!-- theorem-start:theorem -->
**定理（R206A：finite-$L$ common-hub sampler）**

```math
d_y(t)
=
x_y(t)-p_y[1-h(t)]
```

と置けば

```math
\dot d_y=-\Lambda d_y
```

が各 $y$ で厳密に成立する。また

```math
h_\infty
=
\frac{\Lambda}{\Lambda+\kappa a_\Sigma},
```

```math
h(t)
=
h_\infty+
[h(0)-h_\infty]
e^{-(\Lambda+\kappa a_\Sigma)t}.
```

従って有限時間で

```math
x_y(t)
=
p_y[1-h(t)]
+
e^{-\Lambda t}d_y(0).
```

収束率 $\Lambda$ は $L$ と $\min_y p_y$ に依存しない。$a_y=0$ のexact zero-weight channelも許す。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R206A）**

$a_y=p_ya_\Sigma$ をmaster equationへ代入すれば

```math
\dot d_y
=
-\Lambda[x_y-p_y(1-h)]
```

を得る。$h$ は一次線形方程式を直接解けばよい。証明終。
<!-- theorem-end:proof -->

### Z.11.5 R206B：Q2-4用の一様受動channel構成

Q2-4では $L=2^n$ とする。R181C後のterminal signal作用を

```math
J_y
=
\mathcal J_0|Z_y|^2,
\qquad
J_\Sigma=\sum_yJ_y=J_*
```

とする。解析上

```math
p_y=\frac{J_y}{J_*}
```

と書くが、物理装置がこの比を計算して入力することは禁止する。

固定regularization $\delta>0$ を取り、各channelが局所 $J_y$ だけから同一規則

```math
s_y
=
\delta+\frac{LJ_y}{J_*}
```

を使うとする。

capacity/conductanceを

```math
V_y=V_0s_y,
\qquad
G_y=G_0s_y
```

とし、共通hubを

```math
V_H=LV_H^0
```

とする。

<!-- theorem-start:theorem -->
**定理（R206B：一様passive $L$-channel realization）**

上の同型channel族では

```math
k_{y\to H}
=
\Lambda
:=
\frac{G_0}{V_0},
```

```math
k_{H\to y}
=
\kappa
\left(
p_y+\frac{\delta}{L}
\right),
\qquad
\kappa:=\frac{G_0}{V_H^0}.
```

従って総hub escape rateは

```math
\sum_yk_{H\to y}
=
\kappa(1+\delta)
```

であり $L$ に依存しない。

対応する規格化結果重みは

```math
p_y^\delta
=
\frac{p_y+\delta/L}{1+\delta},
```

かつ

```math
D_{\rm TV}(p^\delta,p)
\le
\frac{\delta}{1+\delta}.
```

channelごとに異なるBorn表、振幅表、較正係数表を外部入力する必要はない。
<!-- theorem-end:theorem -->

#### Z.11.5.1 bounded local scaling

一つの極端な幾何factorへ $s_y$ を集中させず、各channelに $m=n$ 個の同型phase-volume座標を置き、

```math
q_\alpha=\frac1n,
\qquad
\lambda_{y\alpha}=s_y^{-1/n}
```

とする。R205Aにより積Jacobianは $s_y$ を与える。

```math
\delta\le s_y\le 2^n+\delta
```

なので、固定 $\delta$ または $\delta^{-1}=\operatorname{poly}(n,1/\epsilon)$ の範囲では、各局所scaleに指数精度を直接要求しない。内部自由度総数は $O(n2^n)$ と報告する。

### Z.11.6 R206C：有限時間・製造誤差・完全結果

R206Aを $p^\delta$ に適用する。任意のpointer初期分布について

```math
\frac12\sum_y|d_y(0)|\le1.
```

decision時刻 $T$ でhub質量を捨てて成功試行だけを再規格化しない。hubを完全結果として保持するか、事前固定した合法的な結果写像へ送る。

そのときsampler誤差は保守的に

```math
\varepsilon_{\rm samp}(T)
\le
2e^{-\Lambda T}
+
\frac{\Lambda}
{\Lambda+\kappa(1+\delta)}
+
\frac{\delta}{1+\delta}
+
T\varepsilon_{\rm gen}
+
\varepsilon_{\rm rec}
```

と置ける。従って

```math
T
=
O\left(
\Lambda^{-1}\log\frac1\epsilon
\right)
```

で有限時間誤差を制御でき、$L$ は明示的に現れない。

実際のlocal scaleが

```math
\widetilde s_y
=
s_y(1+\epsilon_y)+b_y,
```

```math
|\epsilon_y|\le\eta,
\qquad
|b_y|\le b
```

を満たすとする。$s_y\ge\delta$ より

```math
\left|
\frac{\widetilde s_y-s_y}{s_y}
\right|
\le
\xi,
\qquad
\xi:=\eta+\frac{b}{\delta}.
```

$\xi<1$ なら規格化重みの全変動誤差は

```math
D_{\rm TV}(\widetilde p,p^\delta)
\le
\frac{\xi}{1-\xi}
```

で抑えられる。これはchannel数の粗い和を取らないaggregate relative-error boundである。

一方、各signal modeへ状態非依存の独立additive noiseを直接注入する場合はR186の障害が残る。本定理はR186を解消しない。

### Z.11.7 R206D：Q2-1、Q2-3、Q2-4 readout bridge

R181C後の実際の一試行terminal signalを $Z_{\rm out}$ とする。理想回路出力を $Z_C^{\rm id}$ とし、状態方向誤差を $\varepsilon_{\rm ray}$ とする。

Q2-1では $L=4$、Q2-3では $L=8$、Q2-4では $L=2^n$ と特殊化する。R206A--R206C samplerへ

```math
J_y=\mathcal J_0|Z_{{\rm out},y}|^2
```

を局所入力する。

<!-- theorem-start:theorem -->
**定理（R206D：Q2 terminal multi-outcome readout candidate）**

terminal signal作用をR206A--R206Cへ同一試行内で物理的に接続し、外部制御器が最終Born表・振幅表・結果別係数表を入力しないとする。すると理想極限で

```math
P(Y=y)
=
\frac{|Z_{{\rm out},y}|^2}
{\sum_z|Z_{{\rm out},z}|^2}.
```

有限実装では

```math
D_{\rm TV}(P_{\rm out},P_C)
\le
\varepsilon_{\rm ray}
+
\varepsilon_{\rm samp}.
```

Q2-4では $Y\in\{0,1\}^n$ を固定配線のconfiguration labelとして読み、外部readoutは $O(n)$ bitとする。全chamberを外部走査して結果を探索する方式は本定理の一様装置条件を満たさない。
<!-- theorem-end:theorem -->

本候補ではterminal readout後に非規格化射影成分を次段へ渡さないため、R181D型逐次projector treeとR192型非終端作用回復をreadout内部には要求しない。ただし本PRでは現行fixed-goal依存からR181D/R192を外さない。

### Z.11.8 terminal action保持とbackreaction境界

action-angle表示でsampler couplingが $J_y$ とreservoir座標だけに依存し、$\phi_y$ に依存しないなら

```math
\dot J_y
=
-\frac{\partial H_{\rm int}}{\partial\phi_y}
=
0.
```

従ってgate終了後のterminal readoutではsignal actionをQND型に保持できる。

一方、R181Cのcoherent gate実行中から同じ有限強度couplingを常時作用させても位相coherenceを十分保てることは本付録では証明しない。always-on passive coupling、finite-bandwidth reservoir、full Hamiltonian lift、gate中のphase backreactionはM66 strengtheningとして残す。

### Z.11.9 Q2-4資源境界

$L=2^n$ のとき内部受動資源として次を許容・報告する。

- signal mode数：$2^n$。
- result chamber数：$2^n$。
- phase-volume内部自由度：保守的に $O(n2^n)$。
- hub capacity、総conductance、総bath容量、総熱：指数的でもよいが規模を報告する。

外部運用資源には次を要求する。

- gate program長：$\operatorname{poly}(n,d)$。
- sampler制御：global parameter $\Lambda,\kappa,\delta,T$ と固定一様規則だけ。
- channel別Born表・振幅表・係数表：不要。
- terminal readout：$O(n)$ bit。
- sampling時間：
```math
O\left(
\Lambda^{-1}\log\frac1\epsilon
\right).
```
- $\delta^{-1}$、$\Lambda^{-1}$、$\kappa^{-1}$、必要なlocal relative precision：$\operatorname{poly}(n,d,1/\epsilon)$ 以内。

R186のdirect-amplitude registerに対する独立additive-noise障害は独立に残る。従ってM66/R206追加だけからQ2-4を達成へ昇格しない。

### Z.11.10 candidate status

M66/R205A--R205D/R206A--R206Dは、Q2共通readoutを単一multi-outcome reservoir samplerへ縮約するactive replacement candidateである。

この段階では次を変更しない。

- M65/R204A--R204Fの現行2結果selector責務。
- R181Dのprojector-router責務。
- R192のQ2-4非終端作用安定化責務。
- R179の現行open reset/supply責務。
- Q2-1/Q2-2/Q2-3/Q2-4の達成ラベルと直接依存。
- Q2-2の現行非空間分離A端--B端逐次interface。
- R186のadditive-noise障害。

後続promotionでは、Q2-1/Q2-3/Q2-4のterminal readoutをR206Dへ切り替えられるかを、required verifierと全依存グラフを含めて別PRで判定する。
