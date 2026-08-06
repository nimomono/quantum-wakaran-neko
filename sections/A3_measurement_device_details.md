@number: A3
@chapter: 付録
@title: 対モード、境界比較器、完全周期の Hamiltonian 詳細
@status: 固定された左右位相担体モード、反対称交差相関の階数2分解、局所回転、理想比較読み出し、2モード作用保存、殻容量、逆計算を有限正準変数で明示する。境界集団の準備と一般結果形成は未導出である。

## C.1 拡大全系とエネルギー収支

1試行を担う有限部分を

```math
\begin{aligned}
H_{\rm fin}
={}&
H_{\rm particles}
+
H_{\rm ph}
+
H_{\rm prep}
+
H_{\rm source}
+
H_{\rm analyzer}
+
H_{\rm pointer}\\
&
+
H_{\rm return}
+
H_{\rm read}
+
H_{\rm mix}
+
H_{\rm memory}
+
H_{\rm reset}
+
H_{\rm clk}
\end{aligned}
```

とする。外部自由度と仕事源を含め、

```math
H_{\rm all}
=
H_{\rm fin}
+
H_{\rm ext}
+
\varepsilon_{\rm ext}H_{\rm link}
+
H_{\rm work}
```

とする。$H_{\rm all}$ は自律 Hamiltonian であり、有限部分だけのエネルギーは

```math
\dot E_{\rm fin}
=
J_{\rm in}
-
J_{\rm out}
+
P_{\rm ctrl}
```

と変化し得る。

比較窓では $\varepsilon_{\rm ext}$ の効果を小さくし、有限閉鎖系の正準写像として計算する。$H_{\rm prep}$ は共通源の相対振幅・相対位相準備を担う。試行間では、外部記録、不要情報の移送、源と比較器の再初期化に弱開放流路を用い得る。

## C.2 固定モード射影の正準性

有限位相担体と装置の座標を $q\in\mathbb R^N$、運動量を $\pi\in\mathbb R^N$ とする。固定直交行列 $O$ で

```math
q'
=
Oq,
\qquad
\pi'
=
O\pi
```

と変換すると、

```math
\pi^{\mathsf T}dq
=
\left(
\pi'
\right)^{\mathsf T}
dq'.
```

従って変換は正準である。

$O$ の行を、位相活性、A側対モード、B側対モード、比較モード、暗モードの基底に選ぶ。射影は装置の設定、測定結果、目標密度に依存させない。

各2成分正準対 $(Q_{\mu r}^X,P_{\mu r}^X)$ から

```math
z_{\mu r}^X
=
\frac{
Q_{\mu r}^X+iP_{\mu r}^X
}{
\sqrt2
},
\qquad
X\in\{A,B\}
```

と定める。Poisson 括弧は

```math
\left\{
z_{\mu r}^X,
\left(
z_{\nu s}^Y
\right)^*
\right\}
=
-i
\delta_{XY}
\delta_{\mu\nu}
\delta_{rs}.
```

## C.3 反対称源のランク2分解

基底ベクトルを

```math
e_+
=
\begin{pmatrix}
1\\
0
\end{pmatrix},
\qquad
e_-
=
\begin{pmatrix}
0\\
1
\end{pmatrix}
```

とする。理想反対称源は

```math
\Xi_0
=
\sqrt{\frac{\mathcal K}{2}}
\left[
e_+e_-^{\mathsf T}
-
e_-e_+^{\mathsf T}
\right].
```

2つの直交源チャンネルを

```math
z^{A,(1)}
=
a_0e_+,
\qquad
z^{B,(1)}
=
b_0e_-,
```

```math
z^{A,(2)}
=
a_0e_-,
\qquad
z^{B,(2)}
=
-b_0e_+
```

と準備し、$\eta_r$ を

```math
\eta_1a_0b_0^*
=
\eta_2a_0b_0^*
=
\sqrt{\frac{\mathcal K}{2}}
```

に選べば、

```math
\Xi
=
\sum_{r=1}^{2}
\eta_r
z^{A,(r)}
\left(
z^{B,(r)}
\right)^\dagger
=
\Xi_0.
```

$a_0,b_0$ を実数に取る必要はない。共通位相は共役積で消え、相対位相だけが $\Xi_0$ の符号と可視度を決める。

有限 Hamiltonian 源の候補は、時計窓で作動する2モード生成子の組合せとして書けるが、一般の初期集団から上の固定相対位相を偏りなく準備する収束定理はない。

## C.4 局所分析器の生成子

A側の2出力モードに対し、

```math
G_A
=
\sum_r
\left(
Q^A_{+r}P^A_{-r}
-
Q^A_{-r}P^A_{+r}
\right).
```

Poisson 括弧から

```math
\dot z^{A,(r)}
=
\dot\alpha_a
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
z^{A,(r)}
```

を得るため、パルス積分後は

```math
z^{A,(r)}_{\rm out}
=
R(\alpha_a)
z^{A,(r)}_{\rm in}.
```

B側も同様である。$G_A$ と $G_B$ は空間的に離れた位相担体モードへ作用し、

```math
\left\{
G_A,G_B
\right\}
=
0.
```

局所分析器は共通内部位相の生成子と可換である。出力モード添字を実回転するだけだからである。

## C.5 戻り伝達核

局所出力から共通未来比較領域までの線形伝播を

```math
z_{{\rm ret},\mu r}^{X}(t)
=
\sum_{\nu,s}
\int
G_{\mu r,\nu s}^{X}(t-t')
z_{{\rm out},\nu s}^{X}(t')
\,dt'
```

と書く。局所有限伝播には

```math
G^{X}(t)
=
0
\qquad
t<\tau_X
```

が必要である。理想核は比較時刻で

```math
G^{X}
=
e^{i\varphi_X}I
```

となる。共通位相 $e^{i\varphi_X}$ は $\Xi$ の全体位相または較正へ吸収できるが、源チャンネル依存位相は干渉可視度を低下させる。

交差応答の指標を

```math
\varepsilon_{\rm ret}
=
\left\|
G^X
-
e^{i\varphi_X}I
\right\|
```

とする。

## C.6 相関選択関数

局所結果座標の滑らかな窓を $\chi_A(s_A)$、$\chi_B(s_B)$ とし、

```math
\Xi(s_A,s_B)
=
\sum_{A,B}
\chi_A(s_A)
\chi_B(s_B)
\sum_r
\eta_r
z^A_{Ar}
\left(
z^B_{Br}
\right)^*
```

とする。理想的な排他的セクターでは

```math
\chi_A\chi_{A'}
=
0
\qquad
A\neq A',
```

```math
\sum_A\chi_A=1,
\qquad
\sum_B\chi_B=1
```

が結果領域で成立する。

窓の遷移域では複数セクターが重なり得る。遷移域の境界測度を零または制御された有限幅とする条件が必要である。一般的な唯一結果形成は、この窓の定義だけからは従わない。

## C.7 比較 Hamiltonian の Poisson 計算

比較正準対に対し、

```math
H_{\rm read}
=
g_{\rm read}(\vartheta)
\left[
P_{\rm R}\operatorname{Re}\Xi
+
P_{\rm I}\operatorname{Im}\Xi
\right].
```

直接計算すると、

```math
\left\{
Q_{\rm R},
H_{\rm read}
\right\}
=
g_{\rm read}\operatorname{Re}\Xi,
```

```math
\left\{
Q_{\rm I},
H_{\rm read}
\right\}
=
g_{\rm read}\operatorname{Im}\Xi,
```

```math
\left\{
P_{\rm R},
H_{\rm read}
\right\}
=
\left\{
P_{\rm I},
H_{\rm read}
\right\}
=
0.
```

入力モード $z$ について、

```math
\left\{
z,H_{\rm read}
\right\}
=
g_{\rm read}
\left[
P_{\rm R}
\left\{
z,\operatorname{Re}\Xi
\right\}
+
P_{\rm I}
\left\{
z,\operatorname{Im}\Xi
\right\}
\right].
```

従って $P_{\rm R}=P_{\rm I}=0$ なら反作用は厳密に零である。比較中の他の Hamiltonian が $P_\nu$ を生成しないことが必要である。

## C.8 比較作用と内部対称性

比較作用を

```math
A_\partial
=
\frac12
\left(
Q_{\rm R}^2
+
P_{\rm R}^2
+
Q_{\rm I}^2
+
P_{\rm I}^2
\right)
```

とする。理想読み出し後は

```math
A_\partial^{AB}
=
\frac{\Gamma^2}{2}
|\Xi_{AB}|^2.
```

左右位相担体の共通回転生成子を $I_{\rm pair}$ とする。$\Xi$ は共通回転不変で、比較正準対を中性に取るため、

```math
\left\{
I_{\rm pair},
H_{\rm read}
\right\}
=
0.
```

局所分析器、時計、記録、再初期化各項も共通内部回転に不変に設計すれば、

```math
\left\{
I_{\rm pair},
H_{\rm cycle}
\right\}
=
0.
```

この条件は、Bell 源の共通位相方向を比較器が不要に消費しないために必要である。単粒子側の固定作用尺度 $\mathcal J_0$ と同一の保存量である必要はない。

## C.9 作用保存型の比較混合

比較複素ベクトル

```math
c_\partial
=
\frac1{\sqrt2}
\begin{pmatrix}
Q_{\rm R}+iP_{\rm R}\\
Q_{\rm I}+iP_{\rm I}
\end{pmatrix}
```

に対し、

```math
A_\partial
=
c_\partial^\dagger c_\partial.
```

Hermitian 生成子 $T_\alpha$ を用い、

```math
H_{\rm mix}
=
g_{\rm mix}(\vartheta)
\sum_\alpha
\xi_\alpha(z_{\rm D})
c_\partial^\dagger T_\alpha c_\partial
```

とする。複素 Poisson 括弧から

```math
\dot c_\partial
=
-i
g_{\rm mix}
\sum_\alpha
\xi_\alpha
T_\alpha
c_\partial
```

であり、

```math
\frac{dA_\partial}{dt}
=
0.
```

従って暗モードは比較作用を直接受け取らず、$U(2)$ 回転の係数だけを供給する。

## C.10 2モード殻積分

作用角座標で

```math
J_{\rm R}
=
|c_{\rm R}|^2,
\qquad
J_{\rm I}
=
|c_{\rm I}|^2
```

とする。固定比較作用 $A>0$ の未規格化殻容量は

```math
\begin{aligned}
\Omega_2(A)
&=
\int
\delta
\left(
A-J_{\rm R}-J_{\rm I}
\right)
dJ_{\rm R}\,d\theta_{\rm R}\,
dJ_{\rm I}\,d\theta_{\rm I}\\
&=
(2\pi)^2
\int_0^A
dJ_{\rm R}\\
&=
(2\pi)^2A.
\end{aligned}
```

従って $A=A_\partial^{AB}$ なら、

```math
\Omega_2^{AB}
=
(2\pi)^2
\frac{\Gamma^2}{2}
K_{AB}.
```

追加の比較作用モードを直接殻へ入れると、容量のべきが変わる。付随自由度は、結果と設定に共通な因子としてだけ積分する。

## C.11 共通境界流束と余面積公式

全境界位相空間上で作用制約を

```math
F_1(z)
=
A_\partial^{AB}
-
J_{\rm R}
-
J_{\rm I}
```

とし、時計面を

```math
F_2(z)
=
\vartheta-\vartheta_\partial
```

とする。結果セクターの正方向流束は

```math
\mathscr F_{AB}
=
w_{AB}
\int
\rho_\partial(z)
\delta(F_1)
\delta(F_2)
\left(
\dot\vartheta
\right)_+
d\Gamma.
```

余面積公式により、

```math
\mathscr F_{AB}
=
w_{AB}
\int_{F^{-1}(0)}
\frac{
\rho_\partial(z)
\left(
\dot\vartheta
\right)_+
}{
J_F(z)
}
d\Sigma(z),
```

```math
J_F
=
\sqrt{
\det
\left[
DF
\left(
DF
\right)^{\mathsf T}
\right]
}.
```

共通境界条件は、$\rho_\partial$、$\dot\vartheta$、$J_F^{-1}$、付随体積、解多重度の積分後の因子が4結果で等しいことを要求する。殻容量以外の因子が結果依存なら、Bell 共同法則は修正される。

## C.12 正規化された押し出しでは足りない

各結果セクターに規格化された初期測度 $\mu_{AB}$ を置き、読み出しと混合の正準写像を $\mathcal U_{AB}$ とする。すると、

```math
\left(
\mathcal U_{AB}
\right)_*
\mu_{AB}
\left(
\Gamma^{AB}
\right)
=
\mu_{AB}
\left(
\Gamma^{AB}
\right)
=
1.
```

従って、正規化された4集団を別々に比較しても $K_{AB}$ 重みは出ない。$K_{AB}$ 重みは、全セクターへ共通密度を置いた未規格化境界積分が、異なる殻容量を数えるときだけ現れる。

この事実は数値検算でも、セクター質量保存と殻容量の線形性を別項目として確認する。

## C.13 時計、記録、逆計算

時計項を

```math
H_{\rm clk}
=
\Omega I_\vartheta
```

とし、各相互作用を互いに分離した窓 $g_k(\vartheta)$ で作動させる。理想順序は、源準備、局所分析、局所記録、戻り伝播、比較、殻内混合、境界通過である。この順序に対応する Hamiltonian 窓として実装する。

境界通過後、結果を外部記録セルへ可逆にコピーし、

```math
\mathcal U_{\rm cycle}^{-1}
=
\mathcal U_{\rm source}^{-1}
\mathcal U_{\rm analyzer}^{-1}
\mathcal U_{\rm return}^{-1}
\mathcal U_{\rm read}^{-1}
\mathcal U_{\rm mix}^{-1}
```

を実際の逆順に適用する。記号上の積は作用順序に合わせて読む。比較読み出しの逆は同じ入力 $\Xi_{AB}$ に対する $-H_{\rm read}$ である。

外部記録を含む全状態を同じ基準点へ戻すことはできない。異なる結果情報は外部記録、不要情報モード、仕事源、環境のどこかへ残る必要がある。

## C.14 有限幅誤差

有限パルス中の全 Hamiltonian を

```math
H
=
H_{\rm read}
+
H_0
```

とする。相互作用表示の Magnus 展開では、理想読み出しからの先頭補正は概略

```math
\delta\mathcal U
=
O
\left(
\tau_{\rm read}
\|H_0\|
\right)
+
O
\left(
\tau_{\rm read}^2
\left\|
[H_{\rm read},H_0]
\right\|
\right).
```

古典系では交換子を対応する Poisson 作用素の交換子として読む。初期比較運動量が $P_\nu^{\rm in}\neq0$ なら、入力モードへの反作用は1次で生じる。従って、

```math
\varepsilon_{\rm pulse}
\sim
\tau_{\rm read}\omega_{\rm free}
+
\frac{
|P_{\rm R}^{\rm in}|
+
|P_{\rm I}^{\rm in}|
}{
\Gamma|\Xi_{AB}|+\epsilon_0
}
+
\varepsilon_{\rm ret}
```

を代表的な無次元誤差とできる。$\epsilon_0>0$ は作用零セクターでの規格化発散を避ける解析用定数である。

## C.15 未導出事項

本付録の有限正準計算からは、次は導かれない。

1. 一般初期集団から反対称源 $\Xi_0$ を準備すること。
2. 2源チャンネルの相対位相を全試行で保つこと。
3. 連続した局所状態から唯一結果セクターを形成すること。
4. 暗モード集団が比較殻上の Haar 分布を準備すること。
5. 異なる結果殻へ共通の未規格化境界密度を置くこと。
6. 設定生成器を含む境界測度を事後選別なしで実験的に実現すること。
7. 外部記録を保持し、源、比較器、不要情報モードを再初期化する長期反復周期。
8. 単粒子位相担体、Bell 対、比較部分空間の交差誤差を長時間一様に小さくすること。
9. 平面内2出力を超える一般測定器。
10. 一般的な Tsirelson 原理。

これらは補助模型内部の代数的厳密性とは別の、現行モデル M0 の準備、縮約、測定、反復の課題である。
