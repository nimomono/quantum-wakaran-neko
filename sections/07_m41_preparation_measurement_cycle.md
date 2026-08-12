@number: 7
@chapter: 本文
@title: M41の共同実現配置Bell測定周期
@status: M39の4頂点複素振幅場と共同実現配置をsinglet型へ準備し、A分析器で共同配置のA成分を読み、条件付きB場とB配置を局所端へ移し、2端の局所分析器、永久記録、逆計算、弱開放resetを前向き周期へまとめる。操作的接続、準備先行、非空間分離に限定する。

## 7.1 M41と結果変数の一本化

M41は、第6章のM39をBell型測定統計へ接続する初期共通原因型周期である。入力は4頂点複素振幅場

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

## 7.2 鋭い基準配置からのsinglet型準備

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

## 7.3 A分析器と共同配置のA成分

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

<!-- theorem-start:proposition -->
**命題（R107：A分析器後の実現配置読出し）**

固定4頂点場 $c$ とA分析器 $W_x\otimes I_2$ に対し、A分析器出口で共同実現配置のA成分を読むと、理想頻度は $\|c_A^x\|^2$ である。有限装置では正則化、時間離散化、局所更新、検出境界を無反応込みの全変動誤差として任意に小さくできる。A作用選択器が別の結果を生成するとはしない。
<!-- theorem-end:proposition -->

実現配置は全ての測定軸の値を同時に持つ変数ではない。設定 $x$ に対応する分析器を通る間に変化するため、結果は物理的な測定文脈に依存する。

## 7.4 A結果に条件付けた2局所端の準備

安全なA結果 $X_A=A$ に対して、A端の2頂点場を $|A_x\rangle$ へ準備し、A端実現配置を対応する出力へ移す。B端へは規格化条件付き場

```math
\beta_A^x
=
\frac{c_A^x}{\|c_A^x\|}
```

と、中央共同配置に含まれていたB成分 $X_B$ を移す。零作用ブロックは無反応へ送る。singlet型では両ブロック作用が $\mathcal J_0/2$ なので零作用切断は不要である。

条件付き準備は正準SWAP、配置通信路、履歴セルを使う。未選択ブロック、旧端状態、中央配置、選択枝を履歴へ残すため全写像は1対1である。非因子化4頂点場全体を2端へ複製または分配しない。

<!-- theorem-start:proposition -->
**命題（R108：共同実現配置に条件付けた2端準備）**

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
<!-- theorem-end:proposition -->

A枝間のコヒーレンス喪失は、中央A分析器、実現配置読出し、条件付き2端準備で生じる。後段のA局所確認からBへ作用が送られるのではない。

## 7.5 2端の局所分析器と共同分布

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

<!-- theorem-start:proposition -->
**命題（R109：局所分析器後の実現配置共同分布）**

中央でA成分を読み、条件付き2端準備を終えた後、A、B端の局所Hamiltonianだけを作用させる。A端は準備済み結果を確定的に確認し、B端は条件付き場に対する分析器後の実現配置を読む。理想共同分布は $|\langle A_x,B_y|c\rangle|^2$ であり、B結果形成後にAからBへ結果または設定を送らない。
<!-- theorem-end:proposition -->

singlet型では

```math
P(A,B\mid x,y)
=
\frac14
\left[
1-AB\cos(x-y)
\right]
```

となる。共同分布、非信号周辺、CHSH値、Bell前提監査は第8章で分けて扱う。

## 7.6 永久記録、逆計算、reset

A、B端の実現配置検出関数を別々の外部記録セルへ正準剪断でコピーする。理想空セルでは記録窓中の反作用は零である。無反応を含む結果集合を

```math
\{+1,-1,\varnothing\}^2
```

とし、無反応試行を除いて再規格化しない。

記録後は、B分析器、A確認分析器、B端準備SWAP、A端準備、中央A読出し、A分析器、singlet準備、設定生成を逆順で戻す。中央配置と選択履歴を保存しているため、異なる結果履歴を同一点へ押しつぶさない。有限残差は外部空resetセルと交換する。固定有限回は有限閉鎖Hamiltonian系へ埋め込め、無期限反復は記録・resetセル流を持つ弱開放系となる。

## 7.7 測定開始面と初期共通原因

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

## 7.8 誤差、資源、完全周期

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

## 7.9 達成範囲

M41は、M39出力を2つの物理的測定端で同じ共同統計へ接続する操作的接続を構成する。この意味でQ2-2の中心装置を与える。ただし次は含まない。

1. 非因子化4頂点場全体を設定選択前に2つの独立物理部分系へ分配する状態的接続。
2. 2端準備後の自由なA設定変更。
3. 標準的な空間分離Bell実験。
4. 一般非singlet状態の一様な零作用枝処理。
5. 一般測定族を拘束するTsirelson原理。
6. 独立同分布型の有限標本統計。
7. 無期限記録を有限固定容量へ保存すること。

Q2-2の条件付き達成は、接続を操作的接続と読むという意味条件であり、精度パラメータ条件ではない。余弦則、非信号性、CHSH破れ、Tsirelson値、測定設定独立性の監査を第8章で閉じる。
