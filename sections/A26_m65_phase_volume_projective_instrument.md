@number: Z
@chapter: 付録
@title: M65 phase-volume型3状態open射影読出し
@status: Q1/Q2二結果射影用の現行canonical open selector model。正本発展則は保持済み二作用を線形rateへ入れる3状態連続時間Markov過程とし、exact endpoint、有限decision後のR112型record/latch、R204Dの有限時間Born誤差、R204Eの共通binary selector contract、R204FのQ1/Q2-4互換性を備える。R204A--R204Cのphase-volume chamber/Hamiltonian構成は追加実現・持上げであり、M65正本の成立条件にしない。R191/R193はretirement-readiness監査のため現行fixed-goal証人として維持する。

## Z.1 目的と責務境界

M65は、二結果直交射影に対して上流が保持した二作用から排他的な古典結果を作る最小open selectorである。複素信号そのものを再読出しせず、capture終了後に固定された二作用だけを入力とする。

本付録ではM65を正本へ昇格するが、Q1/Q2のfixed-goal witnessはまだR191/R193からM65へ切り替えない。従ってA20/A21、R191/R193のrequired検算、Q1/Q2達成ラベルは維持する。R181D、R192、R179、R180A/R180Cだけをselector非依存のinterfaceへ一般化し、次回の実装切替に備える。

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

本draftではfixed-goal witnessをR191からM65へ切り替えない。
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

の弱結合極で追加latencyを任意に小さくできる。この結果は互換性を示すもので、本draftのQ1 fixed-goal witnessをR193/R191から切り替えない。

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

これはR191/R193退役前の互換性確認であり、本draftではR143/R144/R189B/R189Cの現行fixed-goal証人を切り替えない。

## Z.10 正本と強化課題の境界

M65の正本はR204Aのopen generator、R204Dの有限時間Born誤差、endpoint comparator、R204Eのbinary selector contractで閉じる。

R204Bのphase-volume chamber、R204CのHamiltonian--Brownian lift、finite-bandwidth bath、direct Brownian trajectory、具体回路化は追加の物理実現・A2/B系強化課題である。これらをM65の正本性やfixed-goal達成判定の前提にしない。

R191/R193は本draftでは退役しない。A20/A21とrequired verifierを維持し、Q1/Q2の現行fixed-goal witnessもR191/R193のままとする。本付録でexact endpoint、有限record/latch、Q1空操作対照までを閉じ、退役そのものは後続変更へ分離する。
