@number: 8
@chapter: 本文
@title: Bell型統計と前提監査
@status: 第7章のM41周期についてBorn型共同分布、singlet余弦則、非信号性、CHSH値、平面内2出力族のTsirelson上界、有限誤差、測定設定独立性の破れ、局所因子化、Q2-2の条件付き達成範囲を監査する。

## 8.1 Born型共同分布

理想零幅で源枝とB局所測定を合成すると、

```math
\begin{aligned}
P_{\rm id}
\left(
A,B\mid x,y
\right)
&=
\frac{I_A^x}{\mathcal J_0}
\frac{K_B^{Axy}}{I_A^x}\\
&=
\left|
\langle A_x,B_y|c\rangle
\right|^2
\end{aligned}
```

となる。$I_A^x=0$ の項は0と定める。最初の因子は源選択器の作用区間、2番目はB局所選択器の作用区間から生じる。目的の共同重みを初期測度へ直接置いていない。

A局所確認測定は安全枝でA中央枝選択の結果 $A$ を確定的に確認するため、外部に記録されるA結果を使っても同じ共同分布になる。A、B、源の選択器角は開始面で独立であり、同じ角を複数段へ再利用しない。

この式は一般M39入力にも成立するが、一般状態の測定後テンプレートには第7.7節の作用切断誤差が加わる。singlet型では全枝作用が固定なので、その誤差を必要としない。

## 8.2 singlet余弦則と非信号性

singlet型では

```math
P_{\rm id}
\left(
A,B\mid x,y
\right)
=
\frac14
\left[
1
-
AB\cos(x-y)
\right]
```

となる。従って相関は

```math
E(x,y)
=
\sum_{A,B}
AB
P_{\rm id}
\left(
A,B\mid x,y
\right)
=
-\cos(x-y)
```

である。

一側周辺は

```math
\sum_A
P_{\rm id}
\left(
A,B\mid x,y
\right)
=
\frac12,
\qquad
\sum_B
P_{\rm id}
\left(
A,B\mid x,y
\right)
=
\frac12
```

なので、反対側の設定に依存しない。より一般には、第7.5節の非選択B相関行列から

```math
\sum_A
P_{\rm id}
\left(
A,B\mid x,y
\right)
=
\langle B_y|
\operatorname{Tr}_A
\left(
cc^\dagger
\right)
|B_y\rangle
```

が従う。

## 8.3 CHSH値と平面内上界

CHSH設定を

```math
x_0=0,
\qquad
x_1=\frac{\pi}{2},
\qquad
y_0=\frac{\pi}{4},
\qquad
y_1=-\frac{\pi}{4}
```

とすると、

```math
\left|
E_{00}
+
E_{01}
+
E_{10}
-
E_{11}
\right|
=
2\sqrt2
```

を得る。

平面内の任意の4設定では、単位ベクトルを $\boldsymbol a_i,\boldsymbol b_j$ として

```math
|S|
\leq
\left\|
\boldsymbol b_0+\boldsymbol b_1
\right\|
+
\left\|
\boldsymbol b_0-\boldsymbol b_1
\right\|
\leq
2\sqrt2
```

である。これはM41が実装したsinglet型、平面内2出力相関族の上界であり、一般測定族を拘束するTsirelson原理の導出ではない。

<!-- theorem-start:proposition -->
**命題（R111：singlet余弦統計とBell前提監査）**

R110の理想singlet型周期は、余弦共同確率、設定に依存しない一側周辺、標準CHSH値 $2\sqrt2$、平面内2出力族の上界 $2\sqrt2$ を与える。測定段階の局所Hamiltonianは可換だが、測定開始面の完全状態分布はA設定に依存するため、Bellの測定設定独立性は成立しない。
<!-- theorem-end:proposition -->

singlet特殊化と周辺分布の計算は付録F.11に示す。

## 8.4 有限誤差下の非信号性とCHSH破れ

観測開始から外部記録までの共同分布誤差は、

```math
\begin{aligned}
\epsilon_{\rm fwd}
\leq{}&
\delta_{\rm set}
+
\delta_{\rm s}
+
\delta_A^{\rm loc}
+
\delta_B^{\rm loc}\\
&+
\varepsilon_{\rm prep,A}
+
\varepsilon_{\rm sw,B}
+
\varepsilon_{\rm act}
+
\varepsilon_{\rm rec}
+
\varepsilon_{\rm clk}^{\rm fwd}
\end{aligned}
```

で抑える。$\varepsilon_{\rm prep,A}$ はA担体の局所状態準備、$\varepsilon_{\rm sw,B}$ は選択済みBブロックの正準SWAPに対応する。singlet型では作用切断誤差 $\varepsilon_{\rm act}=0$ とできる。観測後の逆計算とresetは別の帰還誤差 $\varepsilon_{\rm ret}$ として次周期の準備誤差へ渡し、既に記録された同じ周期の分布へ遡って加えない。各項の換算と逆写像別の分解は付録F.12に示す。

理想分布が非信号的で、各設定対の実分布が理想分布から全変動距離 $\epsilon_{\rm fwd}$ 以下なら、一側周辺の設定差は $2\epsilon_{\rm fwd}$ 以下である。無反応を数値0として相関を計算したCHSH値は

```math
\left|
S_{\rm obs}-S_{\rm id}
\right|
\leq
8\epsilon_{\rm fwd}
```

を満たす。従って $\epsilon_{\rm fwd}<({\sqrt2-1})/4$ なら有限誤差下でもCHSH不等式の破れが残る。

## 8.5 測定設定独立性と局所因子化

測定開始面の完全変数 $\Lambda$ には、2担体状態、源枝レジスター、中央作業領域、局所選択器角を含める。B担体は

```math
d^B
=
-c_A^x
```

なので、

```math
\mu_{\rm meas}
\left(
d\Lambda\mid x,y
\right)
\neq
\mu_{\rm meas}
\left(
d\Lambda
\right)
```

が一般に成立する。singlet型でも非選択B相関行列は $x$ に依存しないが、枝ラベルと条件付きB方向を含む完全な古典分解は $x$ に依存する。

一方、中央結合を停止した後の応答は

```math
P
\left(
A,B
\mid
\Lambda,x,y
\right)
=
P_A
\left(
A
\mid
\Lambda_A,x
\right)
P_B
\left(
B
\mid
\Lambda_B,y
\right)
```

と因子化できる。反対側の設定または結果を局所Hamilton方程式へ入れない。Bell不等式の破れは、この測定段階の局所因子化を破るのではなく、$\Lambda$ と設定の独立性を満たさないことで可能になる [1,2,9,23]。

観測周辺の非信号性は、測定設定独立性とは別の性質である。M41ではsinglet対称性により前者を保つが、準備後に設定レジスターだけを外部から変更した場合の統計は保証しない。設定は2担体準備より前に決まり、同じ準備周期へ入る必要がある。

## 8.6 操作的接続、状態的接続、Q2-2の判定

固定目標Q2-2の「2つの測定端への接続」には、次の2つの読み方を区別する。

| 接続の意味 | 要求 | M41の判定 |
|---|---|---|
| 操作的接続 | Q2-1を構成するM39の読出し前4モード出力状態 $c$ を利用し、2つの物理的測定端で局所測定・記録を行って目標共同統計を得る | 達成 |
| 状態的接続 | Q2-1の非因子化4モード状態全体を保存したまま、設定選択前に2つの独立物理部分系へ分配する | 未達・主張しない |

M41の「条件付き達成」の条件は、Q2-2を前者の操作的接続として読むことである。有限幅や誤差を小さくするパラメータ条件ではない。この解釈の下で、M41のsinglet型固定プログラムは合格条件を次の範囲で満たす。

| 合格条件 | 根拠 |
|---|---|
| M39の読出し前4モード出力状態 $c$ を利用した2つの物理的測定端 | R107、R108 |
| A中央枝選択を非選択操作として見たときB枝間コヒーレンスを失う | R108 |
| 測定中のA--B直接結合なし | R110 |
| A局所確認測定、B局所測定、各側の永久外部記録 | R110 |
| Born型共同分布とsinglet余弦則 | R110、R111 |
| CHSH不等式の破れ | R111 |
| 平面内2出力族のTsirelson上界 | R111 |
| 非信号性 | R111 |
| 測定設定独立性の破れ | R110、R111 |
| 有限幅、無反応、帰還 | R107、R109、R110 |

従ってQ2-2は、操作的接続の意味で、固定有限設定、準備先行、非空間分離、singlet型、無反応込み、制御された任意精度の範囲で条件付き達成と判定する。次は達成範囲に含めない。

1. M39の非因子化4モード状態全体の、設定非依存な2物理部分系への状態的分配。
2. 2担体準備後に自由に変更されるA設定またはB設定。
3. 空間的に隔たった設定選択、長距離空間分離、有限伝播速度を持つ時計配線。
4. 一般非singlet状態での作用側チャネルの不存在。
5. 有限資源で無反応なしの厳密2値測定。
6. 一般測定族を拘束するTsirelson原理。
7. 選択器列の独立同分布性と二項分布型有限標本揺らぎ。
8. 永久記録を含む有限閉鎖系全体の同一点帰還。
9. 多量子ビットへ多項式資源で拡張すること。
10. 標準的な空間分離Bell実験またはBell局所性の実験検証。

M41はBellの定理を否定しない。設定が共通過去の準備過程へ入るためBellの測定設定独立性を満たさない、前向き有限Hamiltonianモデルである。
