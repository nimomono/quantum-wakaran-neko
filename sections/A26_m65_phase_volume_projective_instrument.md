@number: Z
@chapter: 付録
@title: M65 phase-volume matched-hub 二結果射影読出し候補
@status: R191/R193をまだ置換しないpromotion-ready replacement candidate。R203Bと共通のphase-volume Jacobianを二結果射影作用へ接続し、固定chamber--neck--hub、Brownian pointer、有限時間Born読出し、R181D受渡し、Q1接続、Q2-4読出し時間資源をR204A--R204Fで整理する。現行Q1/Q2主線、達成ラベル、required verifier、R186判定は変更しない。

## Z.1 目的と責務境界

M65はQ1/Q2の二結果射影読出しについて、現行R191ブラウン巨視的スピンとQ1専用R193 decision接続を将来置換するための候補模型である。本付録では置換そのものは実行しない。現行主線は引き続きR191/R193であり、R181D、R192、R179の定理文と責務も変更しない。

M65が再利用するのはM64のQ3粒子そのものではなく、R203Bで用いたphase-volume Jacobianという統計力学的機構である。Q3ではその局所重みが空間tracerの位置重みを与える。M65では同じ機構を、二結果射影作用を受け取るclassical pointerのchamber容量とneck conductanceへ使う。従ってQ3 tracerとQ1/Q2 pointerを同一物体とはみなさない。

M65の能動自由度は、上流の作用保持機構が固定した二つの正準座標 $A_+,A_->0$、固定chamber--neck--hub領域内を動く一つのclassical pointer $Q$、局所phase volumeを担う高速調和正準対 $(\zeta,\Pi)$、pointerとphase-volume modeへ接続する平衡thermal bath、およびdecision終了時の排他的chamber位置を固定する吸収recordである。

複素信号 $Z$ はM65内部で再読出ししない。capture終了後は信号と保持済み作用を切り離し、M65は $A_\pm$ だけを入力とする。

## Z.2 二結果射影作用入力と安全領域

二結果直交射影 $P_++P_-=I$ に対する理想作用を

```math
J_\pm
=
\mathcal J_0 Z^\dagger P_\pm Z,
\qquad
S=J_++J_->0
```

とし、

```math
p_\pm=\frac{J_\pm}{S}
```

を理想Born重みとする。上流の作用保持終了後の値を $A_\pm$ とし、

```math
A_\Sigma=A_++A_-,
\qquad
\widehat p_\pm=\frac{A_\pm}{A_\Sigma}
```

と置く。作用保持誤差は

```math
D_{\rm TV}(\widehat p,p)\leq\varepsilon_A
```

だけで受ける。M65内部で同じ偏差を再計上しない。

固定cutoff $0<\tau_{\rm cut}<1/2$ に対し、

```math
\min\{\widehat p_+,\widehat p_-\}\geq\tau_{\rm cut}
```

を通常経路とする。それ以外はZ.8のendpoint dispatcherへ送る。

## Z.3 固定chamber--neck--hub Hamiltonian

pointerの配置領域を

```math
\Omega
=
C_+\cup N_+\cup H\cup N_-\cup C_-
```

とする。$C_\pm$ は左右対称なwell-mixed chamber、$N_\pm$ は左右対称な細いneck、$H$ は中央hubである。幾何そのものは試行ごとに変形させない。

固定作用scale $A_*>0$ を用いて

```math
a_\pm=\frac{A_\pm}{A_*},
\qquad
a_\Sigma=\frac{A_\Sigma}{A_*}
```

とする。滑らかな正関数 $\Phi_A(Q)$ を、各領域のplateauで

```math
\Phi_A(Q)
=
\begin{cases}
a_+\phi_C(Q),&Q\in C_+,\\
a_+\phi_N(Q),&Q\in N_+,\\
a_\Sigma\phi_H(Q),&Q\in H,\\
a_-\phi_N(Q),&Q\in N_-,\\
a_-\phi_C(Q),&Q\in C_-,
\end{cases}
```

とする。$\phi_C,\phi_N,\phi_H$ は左右作用に依存しない固定形状因子であり、接続部だけ滑らかに補間する。

phase-volume modeを

```math
H_{\rm pv}
=
\frac{\Pi^2}{2m}
+
\frac{m\omega^2}{2}
\left(
\frac{\zeta}{\Phi_A(Q)}
\right)^2
```

とする。pointer本体は

```math
H_{\rm ptr}
=
\frac{P_Q^2}{2M}
+
U_\Omega(Q)
+
H_{\rm pv}.
```

$U_\Omega$ は固定chamber--neck--hubを作る左右対称なconfining potentialである。pointer座標およびphase-volume modeへ、Ford--Kac--Mazur/Mori--Zwanzig型の調和bath [12--14] を接続する。代表的にはsystem coordinate $X_\ell$ ごとに

```math
H_{{\rm bath},\ell}
=
\sum_n
\left[
\frac{p_{\ell n}^2}{2m_{\ell n}}
+
\frac{m_{\ell n}\omega_{\ell n}^2}{2}
\left(
q_{\ell n}
-
\frac{c_{\ell n}X_\ell}{m_{\ell n}\omega_{\ell n}^2}
\right)^2
\right].
```

decision Hamiltonianを

```math
H_{65}
=
H_{\rm hold}
+
H_{\rm ptr}
+
\sum_\ell H_{{\rm bath},\ell}
```

とする。capture終了後はcapture couplingを切り、$H_{65}$ は元の信号 $Z$ を含まない。$H_{\rm hold}$ は保持座標 $A_\pm$ を含んでよいが、その共役運動量 $P_\pm^A$ を含まない。

## Z.4 R204A：phase-volume projective Hamiltonian identity

<!-- theorem-start:theorem -->
**定理（R204A：二結果射影作用のphase-volume Hamiltonian identity）**

固定 $Q,A_\pm$ の下で $(\zeta,\Pi)$ をcanonicalに積分すると、

```math
Z_{\rm pv}(Q|A)
=
Z_{\rm pv}^0\Phi_A(Q)
```

が厳密に成立する。従ってpointerの平均力ポテンシャルは

```math
F_A(Q)
=
U_\Omega(Q)
-k_BT\log\Phi_A(Q)
+C
```

である。

さらにdecision Hamiltonianが $P_\pm^A$ を含まないので、

```math
\dot A_+=\dot A_-=0.
```

capture終了後に $Z$ との直接結合を切れば、M65自身から走行中signalへの直接Hamiltonian反作用は零である。共通scale変換 $(A_+,A_-)\mapsto(cA_+,cA_-)$ は後で得るchamber分岐比 $\widehat p_\pm$ を変えない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R204A）**

$y=\zeta/\Phi_A(Q)$ と変数変換すると $d\zeta=\Phi_A(Q)\,dy$ であり、Gaussian積分の $Q,A_\pm$ 依存性はJacobian $\Phi_A(Q)$ だけである。従って $F_A=-k_BT\log Z_{\rm pv}+U_\Omega$ から表示式を得る。また正準方程式から $\dot A_r=\partial H_{65}/\partial P_r^A=0$ である。capture終了後の $H_{65}$ が $Z$ を含まないことから、M65のdecision項はsignal方程式へ直接項を加えない。証明終。
<!-- theorem-end:proof -->

R204AはR193が担っていた「保持値をdecision中に変えない」「decision backendを走行信号から切り離す」という責務の候補代替を与える。ただし本draftではR193の現行主線statusを変更しない。

## Z.5 R204B：matched capacity--conductance theorem

左右chamberの基準Gibbs容量を

```math
V_C^0
=
\int_{C_\pm}
e^{-\beta U_\Omega(Q)}
\phi_C(Q)\,dQ
```

とする。hubについて

```math
V_H^0
=
\int_H
e^{-\beta U_\Omega(Q)}
\phi_H(Q)\,dQ
```

とする。

neck軸座標を $s\in[0,\ell]$ とし、reduced Smoluchowski lawで固定基準resistanceを

```math
R_N^0
=
\int_0^\ell
\frac{
e^{\beta U_N(s)}
}{
D\,\phi_N(s)
}
\,ds,
\qquad
G_0=(R_N^0)^{-1}
```

と置く。

<!-- theorem-start:theorem -->
**定理（R204B：matched phase-volume capacity--conductance）**

R204Aの局所phase-volume factorを使うと、左右chamber容量とneck conductanceは

```math
V_\pm
=
a_\pm V_C^0,
\qquad
G_\pm
=
a_\pm G_0
```

を満たす。従って

```math
\frac{G_\pm}{V_\pm}
=
\Lambda
:=
\frac{G_0}{V_C^0}
```

は結果作用に依存しない。

hub容量は

```math
V_H
=
a_\Sigma V_H^0.
```

したがって

```math
\frac{G_\pm}{V_H}
=
\mu\widehat p_\pm,
\qquad
\mu:=\frac{G_0}{V_H^0}.
```

特に小さいBorn重みを持つ結果が存在しても、chamberからの総escape scale $\Lambda$ は小さくならない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R204B）**

chamberではcanonical densityにR204Aの $\Phi_A=a_\pm\phi_C$ が掛かるので容量は $a_\pm V_C^0$ である。neckでは定常Smoluchowski抵抗のintegrandが局所phase volumeの逆数に比例するため $R_\pm=R_N^0/a_\pm$、従って $G_\pm=a_\pm G_0$ である。hubについても同じcanonical積分から $V_H=a_\Sigma V_H^0$。比を取れば表示式を得る。証明終。
<!-- theorem-end:proof -->

R204Bのconductance部分はreduced Brownian/Smoluchowski記述上の厳密恒等式であり、full Hamiltonianからそのreduced lawへ至る誤差は次のR204Cへ分離する。

## Z.6 R204C：Hamiltonian--Brownian--lumped-network reduction contract

対象時間窓 $0\le t\le T$ で、有限帯域bathからMarkov Langevin、underdampedからoverdamped、高速phase-volume modeのconditional canonical tracking、多次元neckからreduced tube law、chamber内非一様性からwell-mixed lumping、左右capacity/conductance較正の誤差をそれぞれ

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

とし、

```math
\varepsilon_{\rm gen}
=
\varepsilon_{\rm bath}
+\varepsilon_{\rm od}
+\varepsilon_{\rm pv}
+\varepsilon_{\rm tube}
+\varepsilon_{\rm lump}
+\varepsilon_{\rm cal}
```

とする。理想coarse lawを

```math
\dot x_+
=
-\Lambda x_+
+\mu\widehat p_+h,
\qquad
\dot x_-
=
-\Lambda x_-
+\mu\widehat p_-h,
```

```math
\dot h
=
\Lambda(x_++x_-)-\mu h
```

とする。

<!-- theorem-start:theorem -->
**定理（R204C：matched-hub Brownian reduction contract）**

full M65 pointerのcompartment lawを $\widetilde\nu_t$、上の理想three-state lawを $\nu_t$ とする。初期lumping誤差を $\varepsilon_{\rm init}$ とし、対象時間窓で実coarse generatorと理想generatorのrow-sum差が一様に $\varepsilon_{\rm gen}$ 以下なら、

```math
\sup_{0\le t\le T}
D_{\rm TV}
(
\widetilde\nu_t,\nu_t
)
\le
\varepsilon_{\rm init}
+
T\varepsilon_{\rm gen}
=:
\varepsilon_{204C}(T).
```

従ってR204A--R204BのHamiltonian/phase-volume構成から、上記各縮約誤差を同時に十分小さくする非空parameter windowが得られれば、M65のphysical pointer lawは有限時間でmatched-hub three-state lawへ収束する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R204C）**

Markov半群の全変動縮約性とDuhamel展開を使う。generator差のrow-sum normを時間積分すると $T\varepsilon_{\rm gen}$、初期差を加えて表示式を得る。証明終。
<!-- theorem-end:proof -->

R204Cは本draftのpromotion gateである。本付録はharmonic bathからGLEへ至る標準構造 [12--14] を採用するが、$\varepsilon_{\rm bath}$ から $\varepsilon_{\rm lump}$ までを特定幾何について完全な定数付きHamiltonian縮約として閉じたとは主張しない。

## Z.7 R204D：有限時間Born readout

理想three-state lawで $h(0)=0$、$x_+(0)+x_-(0)=1$ とする。

<!-- theorem-start:theorem -->
**定理（R204D：matched-hub有限時間Born projective readout）**

理想three-state generatorの固有値は

```math
0,
\qquad
-\Lambda,
\qquad
-(\Lambda+\mu)
```

である。hub occupancyは

```math
h(t)
=
\frac{\Lambda}{\Lambda+\mu}
\left[
1-e^{-(\Lambda+\mu)t}
\right].
```

さらに各 $r\in\{+,-\}$ について

```math
x_r(t)
-
\widehat p_r[1-h(t)]
=
e^{-\Lambda t}
[x_r(0)-\widehat p_r].
```

decision時刻 $T$ で $C_+\mapsto+$、$C_-\mapsto-$、$H\mapsto\varnothing$ と完全結果へ記録する。hub比を

```math
\chi
=
\frac{V_H^0}{V_C^0}
=
\frac{\Lambda}{\mu}
```

とすると、

```math
D_{\rm TV}
(
P_{65}^{0}(T),
\widehat p
)
\le
e^{-\Lambda T}
D_{\rm TV}
(
x_0,\widehat p
)
+
\frac{\chi}{1+\chi}.
```

R204C、上流作用保持、有限record誤差を合成すると、

```math
D_{\rm TV}
(
P_{65}(T),
P_{\rm Born}
)
\le
\varepsilon_A
+
\varepsilon_{204C}(T)
+
e^{-\Lambda T}
D_{\rm TV}
(
x_0,\widehat p
)
+
\frac{\chi}{1+\chi}
+
\varepsilon_{\rm rec}.
```

成功結果だけを再規格化しない。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R204D）**

$1-h=x_++x_-$ を使うと $\dot h=\Lambda-(\Lambda+\mu)h$。また $d_r=x_r-\widehat p_r(1-h)$ と置けば $\dot d_r=-\Lambda d_r$。完全結果分布と $(\widehat p_+,\widehat p_-,0)$ の差を三角不等式で評価し、$h(T)\le\Lambda/(\Lambda+\mu)=\chi/(1+\chi)$ を使う。R204C、$\varepsilon_A$、record誤差は各一度だけ加える。証明終。
<!-- theorem-end:proof -->

## Z.8 endpoint dispatcherと安全作用下限

通常経路外では大きい側へ決定論的dispatcherを開く。小さい側を $s$ とすれば $p_s\le\tau_{\rm cut}+\varepsilon_A$ なので、

```math
\varepsilon_{65}^{\rm edge}
\le
\tau_{\rm cut}
+
\varepsilon_A
+
\varepsilon_{\rm edge}.
```

通常経路では

```math
\varepsilon_{65}^{\rm int}
=
\varepsilon_A
+
\varepsilon_{204C}(T)
+
e^{-\Lambda T}
+
\frac{\chi}{1+\chi}
+
\varepsilon_{\rm rec},
```

```math
\varepsilon_{65}
=
\max
\left\{
\varepsilon_{65}^{\rm int},
\varepsilon_{65}^{\rm edge}
\right\}.
```

安全結果について

```math
p_r
\ge
\tau_{\rm state}^{65}
:=
\tau_{\rm cut}-\varepsilon_A
>0
```

を得る。

## Z.9 R204E：R181D projector-router受渡し候補

<!-- theorem-start:theorem -->
**定理（R204E：M65結果からR181Dへの安全受渡しと逐次合成）**

R204Dが非空結果 $r$ を固定し、$\tau_{\rm state}^{65}>0$ とする。既存R181Dと同じprojector routerを使い、理想選択成分を $v=P_rZ$ とする。このとき

```math
\|v\|
\ge
\sqrt{\tau_{\rm state}^{65}}\|Z\|.
```

router実装誤差が

```math
\|\widetilde v-v\|
\le
\eta_F\|Z\|,
\qquad
\eta_F<\sqrt{\tau_{\rm state}^{65}}
```

を満たせば、

```math
\left\|
\frac{\widetilde v}{\|\widetilde v\|}
-
\frac{v}{\|v\|}
\right\|
\le
\frac{
2\eta_F
}{
\sqrt{\tau_{\rm state}^{65}}-\eta_F
}.
```

深さ $m$ の逐次射影で各節点の完全結果kernel誤差を $\bar\varepsilon_k$ とすれば、

```math
D_{\rm TV}
(
P_{\rm phys}^{(m)},
P_{\rm ideal}^{(m)}
)
\le
\sum_{k=1}^{m}\bar\varepsilon_k.
```

理想極限では非規格化成分 $P_rZ$ を次段へ渡すだけで条件付き作用比が望遠鏡積をなし、既存R181Dと同じLüders型逐次分布を得る。
<!-- theorem-end:theorem -->

R204EはR181Dの置換ではない。本draftではR181D本文のR191依存を変更しない。

## Z.10 R204F：Q1接続とQ2-4読出し資源

<!-- theorem-start:theorem -->
**定理（R204F：Q1 moving-measurement bridgeとQ2-4 polynomial readout-time条件）**

Q1ではR189Aの保持済み作用 $A_L,A_R$ をR193へ渡さずR204Aへ直接接続できる。R189A作用比誤差を $\varepsilon_{189A}$、中間M65完全結果誤差を $\varepsilon_{65}^{\rm mid}$、保持中心時刻からR181D完了までのRabi重み変化を $\varepsilon_{\rm lat}$ とすれば、

```math
\varepsilon_{189B,65}^{\rm dist}
\le
\varepsilon_{189A}
+
\varepsilon_{65}^{\rm mid}
+
\varepsilon_{\rm lat}.
```

M65 decision時間を $T_{65}$ とすると、固定有限回Zeno証人では弱結合条件 $\Omega_\kappa T_{65}\to0$ の下で追加latencyを任意に小さくできる。

Q2-4では二結果node数を $m$、全読出し誤差予算を $\epsilon$ とする。各nodeのmixing項へ $O(\epsilon/m)$ を配る十分条件は

```math
T_{\rm node}
\ge
\frac1{\Lambda}
\log\frac{Cm}{\epsilon}.
```

さらに

```math
\chi
=
O\left(\frac{\epsilon}{m}\right),
\qquad
\varepsilon_{204C},
\varepsilon_A,
\varepsilon_{\rm rec}
=
O\left(\frac{\epsilon}{m}\right)
```

を各nodeで一様に満たすとする。$m$ と $\Lambda^{-1}$ およびR204Cに現れる実装時間尺度比が $n,d,1/\epsilon$ の多項式で抑えられるなら、

```math
T_{\rm read,total}
=
O\left(
\frac{m}{\Lambda}
\log\frac{m}{\epsilon}
\right)
```

は多項式である。

この結論は小さいBorn重みそのものから指数decision時間が生じないことを示すが、R186の指数個modeに対する加法noise/precision障害を解決しない。またabsolute-action版 $\Phi_A$ のmicroscopic rangeを一般深さで一様に保つため、必要ならR192作用安定化を残す。
<!-- theorem-end:theorem -->

## Z.11 promotion条件と現行主線との関係

M65をR191/R193の現行主線へ昇格させる前に、少なくとも次を満たすことをpromotion gateとする。

1. R204Aのpartition identity、保持不変性、signal切離しが解析的に閉じる。
2. R204Bのcapacity/conductance matchingが同一の固定幾何とphase-volume factorから得られる。
3. R204Cについて、各縮約誤差を同時に小さくする非空parameter windowまたは直接数値witnessが得られる。
4. R204DのBorn、hub無反応、endpoint、record誤差を同じparameter familyで所定精度へ落とせる。
5. R204EがR181Dの安全下限と逐次telescopingを壊さない。
6. R204FがQ1有限Zenoのlatency marginを壊さない。
7. Q2-4のM65固有readout timeとprecisionが多項式である。
8. M65がR186とは別の指数precision障害を新しく導入しない。
9. M65 candidate科学検算が全件通る。
10. reduced Brownian chamberの直接trajectory simulationでR204C/R204Dの収束witnessを得る。

本draftではこれらをpromotion条件として記録するだけで、R191、R193、A20、A21、required verifier、Q1/Q2達成ラベルを変更しない。
