@number: U
@chapter: 付録
@title: R193 Q1作用保持座標からブラウン巨視的スピンへの直接decision接続
@status: R189Aが保持したQ1 W2の2作用を、R191の一般transducer契約を経由する抽象箱として残さず、ブラウン巨視的スピンのdecision energyへ直接Hamiltonian結合するQ1専用特殊化を与える。R191のQ1/Q2共通一般定理とQ2の一般transducer契約は変更しない。

## U.1 目的と責務境界

Q1 W型2モード手順では、R189Aが走行中W2の左右射影作用を2個の正準指針変数へ保持する。R191は一般の2結果信号について作用和・作用差の近似値を受け取り、ブラウン巨視的スピンの吸引域境界を作る。本付録では、この2つの間をQ1に限って直接接続する。

R193が担うのは次の範囲だけである。

1. R189Aの保持座標をR191 decision energyの係数へ直接結合する。
2. decision中に保持座標が変化せず、R193自身からW2へ直接反作用しないことを示す。
3. R189Aの作用比誤差をR191の吸引域境界誤差へ一度だけ伝播する。
4. 端点dispatcherを状態依存除算なしの固定線形比較へ書き換える。
5. decision後に保持対の共役運動量へ残る履歴を次回captureから隔離する条件を明示する。

R193はブラウン巨視的スピンの混合、有限温度stochastic LLG、捕獲、無反応、吸収記録を新しく導出しない。それらはR191をそのまま使う。またR181Dの射影結果成分振り分けも変更しない。Q2系列はR193へ依存せず、R191の一般transducer契約を引き続き使う。

## U.2 R189A保持座標

R189Aのcapture終了直後を考える。左右結果を $b\in\{L,R\}$ とし、保持用正準対を

```math
(A_b,P_b^J)
```

とする。capture窓では

```math
H_{\rm cap}(t)
=
\chi_\ell(t-t_\ell)
\sum_{b=L,R}
P_b^J J_b(Z)
```

を使い、理想未使用条件 $P_L^J=P_R^J=0$ から開始する。capture終了時の保持増分を

```math
A_L=\bar J_L,
\qquad
A_R=\bar J_R
```

と書く。初期オフセットを使う場合は既知の固定オフセットを差し引いた保持増分を以下の $A_b$ とする。

和と差を

```math
A_\Sigma=A_L+A_R,
\qquad
A_\Delta=A_L-A_R
```

と定める。R189Aの理想窓では

```math
A_\Sigma=J_\Sigma
```

が成り立ち、差だけが有限窓平均を受ける。中心時刻 $t_\ell$ の理想作用比を

```math
p_L
=
\frac{J_L(t_\ell)}{J_\Sigma},
\qquad
p_R=1-p_L
```

とし、保持作用比を

```math
q_L
=
\frac{A_L}{A_\Sigma},
\qquad
q_R=1-q_L
```

とする。以下では $A_\Sigma>0$ を仮定する。

## U.3 直接decision Hamiltonian

R191の固定長ブラウン巨視的スピンを $\boldsymbol m\in S^2$ とし、読出し軸成分を

```math
U=m_z\in[-1,1]
```

とする。R189Aのcaptureを閉じて $H_{\rm cap}=0$ とした後、decision窓だけ滑らかな固定gate $\lambda_{\rm dec}(t)$ を開き、

```math
H_{193}(t)
=
-\lambda_{\rm dec}(t)
\frac{\chi}{2}
\left[
A_\Sigma U^2
+2A_\Delta U
\right],
\qquad
\chi>0
```

を作用させる。decision plateauでは $\lambda_{\rm dec}=1$ とする。立上げ・立下げの有限誤差は後の $\varepsilon_{193}^{u}$ または時計誤差へ含める。

この結合はR191のdecision potential

```math
V_{\rm dec}(u)
=-\frac{\chi}{2}
\left(
\widehat S u^2+2\widehat D u
\right)
```

を

```math
\widehat S=A_\Sigma,
\qquad
\widehat D=A_\Delta
```

として直接実装する。従って理想接続での吸引域境界は

```math
u_A
=-\frac{A_\Delta}{A_\Sigma}
=1-2q_L.
```

外部制御器が $A_\Delta/A_\Sigma$ を計算してmacrospinへ書き戻す操作は使わない。比は二つの物理係数が同じenergyに入ることで吸引域境界として現れる。

<!-- theorem-start:theorem -->
**定理（R193：R189A作用保持座標からR191ブラウン巨視的スピンへの直接decision接続）**

R189Aのcapture終了後に $H_{\rm cap}=0$ とし、保持座標 $A_L,A_R$ と固定長macrospin $\boldsymbol m$ を上の $H_{193}$ で有限decision窓だけ結合する。decision plateau上では次が成り立つ。

1. 保持座標は厳密に固定される。

```math
\dot A_L=\dot A_R=0.
```

2. $H_{193}$ はW2信号座標 $Z$ を含まないため、R193自身から走行中W2への直接Hamiltonian反作用は零である。W2は同じ区間に存在するRabi Hamiltonianだけで発展する。

3. macrospin側のdecision energyはR191の一般形と一致し、

```math
\widehat S=A_\Sigma,
\qquad
\widehat D=A_\Delta
```

を与える。

4. R189Aの保持済み二値作用比が中心時刻の理想比に対して

```math
|q_L-p_L|
\leq
\varepsilon_{189A}
```

を満たすなら、理想R191境界

```math
u_*
=-\frac{J_L-J_R}{J_L+J_R}
=1-2p_L
```

に対して

```math
|u_A-u_*|
\leq
2\varepsilon_{189A}
```

である。直接結合、有限gate、較正、時計から生じる追加境界誤差を

```math
|\widetilde u_*-u_A|
\leq
\varepsilon_{193}^{u}
```

とまとめれば、

```math
|\widetilde u_*-u_*|
\leq
2\varepsilon_{189A}
+
\varepsilon_{193}^{u}.
```

5. 安全集合上で

```math
A_\Sigma
\geq
S_{\min}^{A}>0
```

なら、R191の有限温度評価は

```math
\Delta_{\min}^{193}
=
\frac{\chi S_{\min}^{A}}
{2k_{\rm B}T_{\rm dec}}
```

を下限としてそのまま適用できる。

6. decision中、保持対の共役運動量は一般に固定されず、

```math
\dot P_L^J
=
\lambda_{\rm dec}(t)
\frac{\chi}{2}
\left(U^2+2U\right),
```

```math
\dot P_R^J
=
\lambda_{\rm dec}(t)
\frac{\chi}{2}
\left(U^2-2U\right)
```

となる。従って $0\leq\lambda_{\rm dec}\leq1$ とdecision窓長 $T_{\rm dec}$ に対して

```math
|\Delta P_b^J|
\leq
\frac{3\chi}{2}T_{\rm dec},
\qquad
b=L,R.
```

この使用済み保持対を、共役運動量を除去せず次回の $H_{\rm cap}$ へ再接続してはならない。次回capture前に未使用保持対との正準SWAPを行うか、R179のopen resetへ切り離して未使用保持対を供給する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明（R193）**

$H_{193}$ は $P_L^J,P_R^J$ を含まないので、正準方程式から $\dot A_b=\partial H_{193}/\partial P_b^J=0$ である。またcapture終了後は $H_{\rm cap}=0$ であり、$H_{193}$ は $Z$ を含まないため、R193から $Z$ への追加Hamiltonianベクトル場は零である。

$H_{193}$ のmacrospin依存部分はR191の $V_{\rm dec}$ に $\widehat S=A_\Sigma$、$\widehat D=A_\Delta$ を代入した式と一致する。さらに

```math
u_A=1-2q_L,
\qquad
u_*=1-2p_L
```

なので

```math
|u_A-u_*|
=2|q_L-p_L|
\leq2\varepsilon_{189A}.
```

追加接続誤差には三角不等式を使う。$A_\Sigma$ の正下限からR191の障壁下限が直ちに従う。

最後に $\dot P_b^J=-\partial H_{193}/\partial A_b$ を計算すると表示式を得る。$|U|\leq1$ だから $|U^2\pm2U|\leq3$ であり、有限decision窓を積分して共役運動量の上界を得る。次回captureでは $H_{\rm cap}$ が $P_b^J J_b(Z)$ を含むため、使用済み $P_b^J$ を残した再接続は一般にW2へ反作用する。従って未使用保持対条件が必要である。証明終。
<!-- theorem-end:proof -->

## U.4 endpoint dispatcherの除算除去

R191の解析上の推定重みをR193特殊化すると

```math
\widehat p_L
=
\frac{A_L}{A_L+A_R},
\qquad
\widehat p_R
=
\frac{A_R}{A_L+A_R}.
```

固定 $0<\tau_{\rm cut}<1/2$ に対して

```math
\widehat p_L<\tau_{\rm cut}
```

は

```math
(1-\tau_{\rm cut})A_L
-\tau_{\rm cut}A_R
<0
```

と同値である。右側も $L,R$ を交換すればよい。従ってQ1/R193のendpoint dispatcherはR112型の固定線形比較器で実装でき、物理制御器が状態依存除算を実行する必要はない。比較器の有限保護帯はR191の正式な無反応または $\varepsilon_{193}^{u}$ に含める。

## U.5 誤差を一度だけ数える規約

R193はR189Aの作用比誤差をR191へ伝播する特殊化であり、同じ偏差を二重に数えない。Q1ではR191内部誤差を、R189Aから既に計上した境界ずれを除いて

```math
\varepsilon_{191|193}^{\rm int}
=
\varepsilon_{\rm mix}
+g
+\frac{\varepsilon_{193}^{u}}{2}
+q_{\rm ret}
+q_{\rm time}
+\varepsilon_{\rm cap}
```

と整理できる。端点側も

```math
\varepsilon_{191|193}^{\rm edge}
=
\tau_{\rm cut}
+\frac{\varepsilon_{193}^{u}}{2}
+\varepsilon_{\rm cap}
```

とし、

```math
\varepsilon_{191|193}
=
\max
\left\{
\varepsilon_{191|193}^{\rm int},
\varepsilon_{191|193}^{\rm edge}
\right\}
```

とする。従ってR189BのQ1特殊化は

```math
\varepsilon_{189B}^{\rm dist}
\leq
\varepsilon_{189A}
+\varepsilon_{191|193}
+\varepsilon_{\rm lat}
```

と書ける。一般R191のtransducer誤差式はQ2とR193を使わない実装のために残す。

## U.6 mixing、decision、未使用保持対の時計順序

R191の等方mixingは $A_L,A_R$ を必要としないので、Q1ではW2発展およびR189A capture以前から並行して実行できる。必要条件はdecision gateを開く時刻までに所定の $\varepsilon_{\rm mix}$ を達成していることである。

1回のQ1測定周期は例えば次の有限時計順序でよい。

```
macrospin mixing ----+------------------------------
W2 Rabi -------------+-- R189A capture --+----------
                                             |
                                             +-- R193/R191 decision
                                                  |
                                                  +-- R181D router
                                                       |
                                                       +-- used pointer SWAP/reset
```

R189Bのlatencyへmixing時間全体を必ず加える必要はない。capture中心時刻からR181D完了までの実際の時間差だけを $\varepsilon_{\rm lat}$ へ入れる。

## U.7 主張しないこと

R193の追加後も次は未導出である。

1. R191のstochastic LLGを含むmacrospin浴、吸収記録、R181D router、R179 resetをM37の元の局所ばね座標だけから導くこと。
2. Q1の全周期について仕事、熱、エントロピー収支を一つの具体的装置で閉じること。
3. Q2の4、8、一般 $2^n$ モード信号からR191へ入る一般transducerをR189A/R193で置き換えること。
4. Q1、Q2、Q3を同じ製造済み装置、同じパラメータ、単一周期へ統合するM0全体。

従ってR193はQ1の「W2作用保持からmacrospin decision energyまで」の抽象接続を閉じる強化結果であり、M0達成を意味しない。