@number: 5
@chapter: 本文
@title: M41 Bell測定周期と前提監査
@status: M41の前向き周期、余弦共同統計、非信号性、CHSH値、測定設定独立性の破れを1章で扱う。

## 5.1 M41と結果変数の一本化

M41は、第4章のM39をBell型測定統計へ接続する初期共通原因型周期である。入力は4頂点複素振幅場

```math
c
\in
\mathbb C^4
```

と共同実現配置

```math
X
=
(X_A,X_B)
\in
\{+1,-1\}^2
```

である。M35型作用選択器が $A$、$B$ を別々に新しく生成する構成は主線から外す。A結果はA分析器出口の $X_A$、B結果はB分析器出口の $X_B$ である。作用区間、更新角、滑らかな比較器は、実現配置過程と条件付き場準備を有限Hamiltonian化する補助変数として使う。

M41の前向き順序は次である。

1. 設定前の連続角から設定 $x,y$ を生成する。
2. 鋭い基準場 $c=e_{00}$ と基準配置 $X=(0,0)$ を置く。
3. 設定と独立なM39準備回路でsinglet型場と共同実現配置を準備する。
4. 中央でA分析器 $W_x\otimes I_2$ を場と実現配置へ作用させる。
5. A成分 $X_A=A$ を読み、A局所場と条件付きB場を準備し、B成分 $X_B$ をB端へ移す。
6. 中央結合を停止する。
7. A端で準備済み結果を確認し、B端で分析器 $W_y$ を場と実現配置へ作用させて $X_B=B$ を読む。
8. 2結果を別々の外部セルへ永久記録する。
9. 履歴を保存したまま前向き写像を逆実行し、有限残差を外部resetセルへ交換する。

設定、singlet型場、結果ラベルを開始面で同時に設定依存標本化しない。設定依存性は、設定生成後にA分析器を中央共同配置へ作用させる前向き過程から生じる。

## 5.2 鋭い基準配置からのsinglet型準備

理想singlet型場を

```math
c_{\rm s}
=
\frac{1}{\sqrt2}
\begin{pmatrix}
0&1&-1&0
\end{pmatrix}^{\mathsf T}
```

とする。M39の局所操作とCNOTプログラムを使えば、$e_{00}$ から $c_{\rm s}$ を有限回路で準備できる。R118により、同じ回路で発展した共同実現配置は準備終了時に

```math
P(X=(a,b))
=
\left|
(c_{\rm s})_{ab}
\right|^2
```

を持つ。従って開始面へsinglet共同分布を別に書き込まない。

設定生成角を $\xi_A,\xi_B$、実現配置更新角列を $\boldsymbol\vartheta$ とし、設定前基準測度を

```math
d\mu_0
=
\frac{d\xi_A\,d\xi_B}{(2\pi)^2}
\otimes
d\mu_{\boldsymbol\vartheta}
\otimes
\delta_*
```

とする。$\delta_*$ は鋭い基準場、基準配置、空レジスター、時計入口を表す。更新角の有限次元Haar測度は、求めるBell共同分布を直接含まない。

## 5.3 A分析器と共同配置のA成分

A設定の分析器を $W_x$ とし、中央4頂点場へ

```math
c^x
=
\left(
W_x\otimes I_2
\right)c
=
\begin{pmatrix}
c_+^x\\
c_-^x
\end{pmatrix}
```

と作用させる。$c_A^x\in\mathbb C^2$ はA分析器出口 $A$ に対応するBブロックである。共同実現配置も同じ4頂点グラフプログラムで発展するため、R113から

```math
P(X_A=A\mid x)
=
\left\|c_A^x\right\|^2
```

を得る。singlet型では両値が $1/2$ である。

**構成段階（R107：A分析器後の実現配置読出し）**

固定4頂点場 $c$ とA分析器 $W_x\otimes I_2$ に対し、A分析器出口で共同実現配置のA成分を読むと、理想頻度は $\|c_A^x\|^2$ である。有限装置では正則化、時間離散化、局所更新、検出境界を無反応込みの全変動誤差として任意に小さくできる。A作用選択器が別の結果を生成するとはしない。
実現配置は全ての測定軸の値を同時に持つ変数ではない。設定 $x$ に対応する分析器を通る間に変化するため、結果は物理的な測定文脈に依存する。

## 5.4 A結果に条件付けた2局所端の準備

安全なA結果 $X_A=A$ に対して、A端の2頂点場を $|A_x\rangle$ へ準備し、A端実現配置を対応する出力へ移す。B端へは規格化条件付き場

```math
\beta_A^x
=
\frac{c_A^x}{\|c_A^x\|}
```

と、中央共同配置に含まれていたB成分 $X_B$ を移す。零作用ブロックは無反応へ送る。singlet型では両ブロック作用が $\mathcal J_0/2$ なので零作用切断は不要である。

条件付き準備は正準SWAP、配置通信路、履歴セルを使う。未選択ブロック、旧端状態、中央配置、選択枝を履歴へ残すため全写像は1対1である。非因子化4頂点場全体を2端へ複製または分配しない。

**構成段階（R108：共同実現配置に条件付けた2端準備）**

A結果 $X_A=A$ の安全枝で、A端を $|A_x\rangle$ と対応配置へ準備し、B端を $\beta_A^x$ と中央配置のB成分へ準備する有限正準写像を構成できる。枝を読まないB場の相関行列は

```math
\sum_A
c_A^x
\left(c_A^x\right)^\dagger
=
\operatorname{Tr}_A
\left(cc^\dagger\right)
```

となり、A設定に依存しない。
A枝間のコヒーレンス喪失は、中央A分析器、実現配置読出し、条件付き2端準備で生じる。後段のA局所確認からBへ作用が送られるのではない。

## 5.5 2端の局所分析器と共同分布

2端準備後に中央結合を停止し、

```math
H_{\rm meas}
=
H_A+H_B,
\qquad
\{H_A,H_B\}=0
```

とする。A端では $W_x|A_x\rangle=e_A$ なので、A実現配置を再び読めば同じ $A$ が確定的に得られる。B端では $W_y$ をB場とB実現配置へ作用させ、出口配置 $X_B=B$ を読む。条件付き分布は

```math
P(B\mid A,x,y)
=
\left|
\langle B_y|\beta_A^x\rangle
\right|^2
```

である。従って

```math
\begin{aligned}
P(A,B\mid x,y)
&=
\left\|c_A^x\right\|^2
\left|
\langle B_y|\beta_A^x\rangle
\right|^2\\
&=
\left|
\langle A_x,B_y|c\rangle
\right|^2.
\end{aligned}
```

**構成段階（R109：局所分析器後の実現配置共同分布）**

中央でA成分を読み、条件付き2端準備を終えた後、A、B端の局所Hamiltonianだけを作用させる。A端は準備済み結果を確定的に確認し、B端は条件付き場に対する分析器後の実現配置を読む。理想共同分布は $|\langle A_x,B_y|c\rangle|^2$ であり、B結果形成後にAからBへ結果または設定を送らない。
singlet型では

```math
P(A,B\mid x,y)
=
\frac14
\left[
1-AB\cos(x-y)
\right]
```

となる。共同分布、非信号周辺、CHSH値、Bell前提監査は第5章で分けて扱う。

## 5.6 永久記録、逆計算、reset

A、B端の実現配置検出関数を別々の外部記録セルへ正準剪断でコピーする。理想空セルでは記録窓中の反作用は零である。無反応を含む結果集合を

```math
\{+1,-1,\varnothing\}^2
```

とし、無反応試行を除いて再規格化しない。

記録後は、B分析器、A確認分析器、B端準備SWAP、A端準備、中央A読出し、A分析器、singlet準備、設定生成を逆順で戻す。中央配置と選択履歴を保存しているため、異なる結果履歴を同一点へ押しつぶさない。有限残差は外部空resetセルと交換する。固定有限回は有限閉鎖Hamiltonian系へ埋め込め、無期限反復は記録・resetセル流を持つ弱開放系となる。

## 5.7 測定開始面と初期共通原因

設定生成から2端準備までの前向き写像を $T_{xy}$ とする。測定開始面の設定条件付き測度は

```math
\mu_{\rm meas}^{xy}
=
\left(T_{xy}\right)_\#
\mu_0
\left(\cdot\mid x,y\right)
```

である。$T_{xy}$ はA設定 $x$ を中央A分析器と条件付き2端準備に使うため、測定開始時の完全状態分布は $x$ に依存する。Bellの測定設定独立性は成立しない。

一方、2端準備後の局所応答は

```math
P(A,B\mid x,y,\Lambda)
=
P_A(A\mid x,\Lambda_A)
P_B(B\mid y,\Lambda_B)
```

と因子化でき、局所Hamiltonianは可換である。ここで完全状態 $\Lambda$ は複素振幅場、実現配置、更新角、履歴、設定レジスターを含む。Bellの定理を否定せず、成立しない前提とその前向き機構を明示する。

## 5.8 誤差、資源、完全周期

前向き共同分布誤差を

```math
\begin{aligned}
\epsilon_{\rm fwd}
\leq{}&
\delta_{\rm set}
+
\varepsilon_{\rm prep}
+
\varepsilon_{\rm reg}
+
\varepsilon_{\rm disc}\\
&+
\varepsilon_{\rm sel}
+
\varepsilon_{\rm move}
+
\varepsilon_{\rm cond}
+
\varepsilon_{\rm win}\\
&+
\varepsilon_{\rm det}
+
\varepsilon_{\rm rec}
+
\varepsilon_{\rm clk}^{\rm fwd}
\end{aligned}
```

と分ける。$\varepsilon_{\rm prep}$ は基準配置からsinglet型場・配置を作る誤差、$\varepsilon_{\rm cond}$ はA結果に条件付けた2端準備、$\varepsilon_{\rm move}$ は実現配置通信路の誤差である。帰還誤差 $\varepsilon_{\rm ret}$ は観測済み共同分布へ遡って加えず、次周期の準備誤差へ渡す。

資源は、4頂点複素振幅場、実現配置更新・通信路・履歴、2端場、分析器、記録、reset、時計に分ける。各記録端は1周期当たり1セルを使う。固定有限設定・固定有限更新数では有限正準対であるが、最小資源数、空間輸送距離、固定帯域下の最短時間は評価していない。

<!-- theorem-start:theorem -->
**定理（R121：共同実現配置によるM41 Bell測定周期）**

固定有限設定、固定singlet型準備、任意の $\epsilon>0$ に対し、鋭い基準配置からM39準備、中央A分析器、共同実現配置のA成分読出し、条件付き2端準備、2端局所分析器、永久記録、逆計算、弱開放resetまでを有限Hamiltonian周期へまとめられる。無反応を含む共同結果分布は理想singlet型分布から全変動距離 $\epsilon$ 未満、周期末能動部偏差は $\epsilon$ 未満にできる。
<!-- theorem-end:theorem -->

## 5.9 達成範囲

M41は、M39出力を2つの物理的測定端で同じ共同統計へ接続する操作的接続を構成する。この意味でQ2-2の中心装置を与える。ただし次は含まない。

1. 非因子化4頂点場全体を設定選択前に2つの独立物理部分系へ分配する状態的接続。
2. 2端準備後の自由なA設定変更。
3. 標準的な空間分離Bell実験。
4. 一般非singlet状態の一様な零作用枝処理。
5. 一般測定族を拘束するTsirelson原理。
6. 独立同分布型の有限標本統計。
7. 無期限記録を有限固定容量へ保存すること。

Q2-2の条件付き達成は、接続を操作的接続と読むという意味条件であり、精度パラメータ条件ではない。余弦則、非信号性、CHSH破れ、Tsirelson値、測定設定独立性の監査を第5章で閉じる。

## 5.10 Born型共同分布

理想層でA分析器後の共同実現配置読出しとB局所分析器を合成すると、

```math
\begin{aligned}
P_{\rm id}
\left(
A,B\mid x,y
\right)
&=
\left\|c_A^x\right\|^2
\left|
\langle B_y|\beta_A^x\rangle
\right|^2\\
&=
\left|
\langle A_x,B_y|c\rangle
\right|^2
\end{aligned}
```

となる。$\|c_A^x\|=0$ の項は0と定める。最初の因子はA分析器出口の実現配置分布、2番目は条件付きB場をB分析器へ通した実現配置分布である。目的の共同重みを初期測度へ直接置いていない。

A局所確認測定は、安全枝で中央A分析器後に読んだ実現配置 $A$ を確定的に確認するため、外部に記録されるA結果を使っても同じ共同分布になる。各有限更新段は別の更新セルを使い、同じ角を複数段へ再利用しない。

この式は一般M39入力にも成立するが、零作用ブロックを持つ一般状態では条件付き場準備の無反応誤差が加わる。singlet型では両ブロック作用が固定なので、その誤差を必要としない。

## 5.11 singlet余弦則と非信号性

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

なので、反対側の設定に依存しない。より一般には、第5.5節の非選択B相関行列から

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

## 5.12 CHSH値と平面内上界

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

<!-- theorem-start:corollary -->
**系（R111：singlet余弦統計とBell前提監査）**

R121の理想singlet型周期は、余弦共同確率、設定に依存しない一側周辺、標準CHSH値 $2\sqrt2$、平面内2出力族の上界 $2\sqrt2$ を与える。測定段階の局所Hamiltonianは可換だが、測定開始面の完全状態分布はA設定に依存するため、Bellの測定設定独立性は成立しない。
<!-- theorem-end:corollary -->

singlet特殊化と周辺分布の計算は付録D.6に示す。

## 5.13 有限誤差下の非信号性とCHSH破れ

観測開始から外部記録までの共同分布誤差は、

```math
\begin{aligned}
\epsilon_{\rm fwd}
\leq{}&
\delta_{\rm set}
+
\varepsilon_{\rm prep}
+
\varepsilon_{\rm reg}
+
\varepsilon_{\rm disc}\\
&+
\varepsilon_{\rm sel}
+
\varepsilon_{\rm move}
+
\varepsilon_{\rm cond}
+
\varepsilon_{\rm win}\\
&+
\varepsilon_{\rm det}
+
\varepsilon_{\rm rec}
+
\varepsilon_{\rm clk}^{\rm fwd}
\end{aligned}
```

で抑える。$\varepsilon_{\rm prep}$ は基準配置からのsinglet型準備、$\varepsilon_{\rm cond}$ はA結果に条件付けた2端準備、$\varepsilon_{\rm move}$ は実現配置通信路に対応する。観測後の逆計算とresetは別の帰還誤差 $\varepsilon_{\rm ret}$ として次周期の準備誤差へ渡し、既に記録された同じ周期の分布へ遡って加えない。各項の換算と逆写像別の分解は付録D.9、付録Fに示す。

理想分布が非信号的で、各設定対の実分布が理想分布から全変動距離 $\epsilon_{\rm fwd}$ 以下なら、一側周辺の設定差は $2\epsilon_{\rm fwd}$ 以下である。無反応を数値0として相関を計算したCHSH値は

```math
\left|
S_{\rm obs}-S_{\rm id}
\right|
\leq
8\epsilon_{\rm fwd}
```

を満たす。従って $\epsilon_{\rm fwd}<({\sqrt2-1})/4$ なら有限誤差下でもCHSH不等式の破れが残る。

## 5.14 測定設定独立性と局所因子化

測定開始面の完全変数 $\Lambda$ には、複素振幅場、実現配置、2端状態、中央履歴、設定レジスター、局所更新角を含める。B端の条件付き場は

```math
\beta_A^x
=
\frac{c_A^x}{\|c_A^x\|}
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

が一般に成立する。singlet型でも非選択B相関行列は $x$ に依存しないが、共同実現配置のA成分と条件付きB方向を含む完全な古典分解は $x$ に依存する。

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

## 5.15 操作的接続、状態的接続、Q2-2の判定

固定目標Q2-2の「2つの測定端への接続」には、次の2つの読み方を区別する。

| 接続の意味 | 要求 | M41の判定 |
|---|---|---|
| 操作的接続 | Q2-1を構成するM39の4頂点複素振幅場と共同実現配置を利用し、2つの物理的測定端で局所測定・記録を行って目標共同統計を得る | 達成 |
| 状態的接続 | Q2-1の非因子化4頂点場全体を保存したまま、設定選択前に2つの独立物理部分系へ分配する | 未達・主張しない |

M41の「条件付き達成」の条件は、Q2-2を前者の操作的接続として読むことである。有限幅や誤差を小さくするパラメータ条件ではない。この解釈の下で、M41のsinglet型固定プログラムは合格条件を次の範囲で満たす。

| 合格条件 | 根拠 |
|---|---|
| M39の4頂点場と共同実現配置を利用した2つの物理的測定端 | R107、R108、R121 |
| A分析器後の実現配置読出しを非選択操作として見たときA枝間コヒーレンスを失う | R108 |
| 測定中のA--B直接結合なし | R109、R121 |
| A局所確認測定、B局所測定、各側の永久外部記録 | R109、R121 |
| Born型共同分布とsinglet余弦則 | R109、R111、R121 |
| CHSH不等式の破れ | R111 |
| 平面内2出力族のTsirelson上界 | R111 |
| 非信号性 | R111 |
| 測定設定独立性の破れ | R111、R121 |
| 有限幅、無反応、帰還 | R107--R109、R121 |

従ってQ2-2は、操作的接続の意味で、固定有限設定、準備先行、非空間分離、singlet型、無反応込み、制御された任意精度の範囲で条件付き達成と判定する。次は達成範囲に含めない。

1. M39の非因子化4頂点場全体の、設定非依存な2物理部分系への状態的分配。
2. 2担体準備後に自由に変更されるA設定またはB設定。
3. 空間的に隔たった設定選択、長距離空間分離、有限伝播速度を持つ時計配線。
4. 一般非singlet状態での作用側チャネルの不存在。
5. 有限資源で無反応なしの厳密2値測定。
6. 一般測定族を拘束するTsirelson原理。
7. 更新角列の独立同分布性と二項分布型有限標本揺らぎ。
8. 永久記録を含む有限閉鎖系全体の同一点帰還。
9. 多量子ビットへ多項式資源で拡張すること。
10. 標準的な空間分離Bell実験またはBell局所性の実験検証。

M41はBellの定理を否定しない。設定が共通過去の準備過程へ入るためBellの測定設定独立性を満たさない、前向き有限Hamiltonianモデルである。
