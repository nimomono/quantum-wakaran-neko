@number: D
@chapter: 付録
@title: M41共同実現配置周期の証明
@status: R107--R111、R121の準備、条件付き2端構成、共同統計、誤差合成を証明する。

## D.1 開始面と設定生成

設定生成角を $(\xi_A,J_A)$、$(\xi_B,J_B)$、複素振幅場と共同実現配置の有限更新角列を $\boldsymbol\vartheta$ とする。開始面で

```math
c=e_{00},
\qquad
X=(0,0)
```

とし、テンプレート、読出し、履歴、記録、resetセルをそれぞれの空入口へ置く。基準測度は

```math
d\mu_0
=
\frac{d\xi_A\,d\xi_B}{(2\pi)^2}
\otimes
d\mu_{\boldsymbol\vartheta}
\otimes
\delta_*.
```

設定窓は $\xi_A,\xi_B$ から有限集合の設定レジスター $x,y$ を作る。比較接続域は無反応へ送る。設定生成後にM39の固定準備回路を作用させるので、場準備回路自体は $x,y$ に依存しない。

## D.2 singlet型場と共同実現配置の準備

固定M39回路 $U_{\rm s}$ を

```math
U_{\rm s}e_{00}
=
c_{\rm s}
=
\frac{|01\rangle-|10\rangle}{\sqrt2}
```

となるように選ぶ。実現配置は同じ時間依存グラフプログラムに従う。開始時は

```math
P(X=00)=1=|\langle00|e_{00}\rangle|^2
```

なのでR113により、準備終了時に

```math
P(X=ab)
=
\left|
\langle ab|c_{\rm s}\rangle
\right|^2
```

を得る。これはR118の4頂点特殊化である。singlet共同分布を開始面へ直接置いていない。

## D.3 A分析器とA成分読出し

A分析器後の場を

```math
c^x
=
(W_x\otimes I_2)c
=
\sum_A
|A\rangle\otimes c_A^x
```

と書く。同じ分析器プログラムで共同実現配置を発展させると、

```math
P(X_A=A\mid x)
=
\sum_B
\left|
\langle A,B|c^x\rangle
\right|^2
=
\|c_A^x\|^2.
```

有限装置では付録Fの正則化、時間離散化、局所更新、1辺輸送、検出を用いる。安全なA出力領域で $X_A=A$ を読み、辺輸送中、比較接続域、時計境界は無反応へ送る。この構成によりR107が従う。

## D.4 条件付き2端準備の正準性

$\|c_A^x\|>0$ の安全枝で

```math
\beta_A^x
=
\frac{c_A^x}{\|c_A^x\|}
```

とする。A端の空2頂点場へ $|A_x\rangle$ を準備し、B端の空2頂点場へ $\beta_A^x$ を正準SWAPする。実現配置については、中央のA成分をA端の対応領域へ、B成分をB端の対応領域へ1辺通信路の有限列で移す。

異なる枝が同じ端状態を作る場合でも、中央の旧場、旧配置、枝ラベル、通信路履歴を別の履歴セルへ残す。従って全写像は単射であり、逆窓は履歴を読んで元の中央状態へ戻せる。零作用ブロックは無反応へ送る。singlet型では

```math
\|c_+^x\|^2
=
\|c_-^x\|^2
=
\frac12
```

なので零作用分岐はない。

## D.5 非選択B状態

A結果を読まずにB場の相関行列を求めると

```math
\begin{aligned}
\sum_A
c_A^x
(c_A^x)^\dagger
&=
\sum_A
(\langle A|W_x\otimes I)c c^\dagger
(W_x^\dagger|A\rangle\otimes I)\\
&=
\operatorname{Tr}_A(cc^\dagger).
\end{aligned}
```

完全性 $\sum_AW_x^\dagger|A\rangle\langle A|W_x=I_2$ を使った。従って非選択B状態は $x$ に依存しない。singlet型では $I_2/2$ である。

共同実現配置についても

```math
P(X_B=B\mid x)
=
\sum_A
|\langle A,B|c^x\rangle|^2
```

であり、同じ完全性から $x$ に依存しない。A枝間コヒーレンスの喪失は、A分析器後の実現配置読出しと条件付き準備で生じる。

## D.6 2端局所分析器と共同分布

2端準備後、中央結合を停止する。A端では $W_x|A_x\rangle=e_A$ なので同じ結果を確定的に確認する。B端では $W_y$ を $\beta_A^x$ とB実現配置へ作用させる。R113から

```math
P(B\mid A,x,y)
=
|\langle B_y|\beta_A^x\rangle|^2.
```

従って

```math
\begin{aligned}
P(A,B\mid x,y)
&=
\|c_A^x\|^2
|\langle B_y|\beta_A^x\rangle|^2\\
&=
|\langle A_x,B_y|c\rangle|^2.
\end{aligned}
```

これはR109である。A、B端の局所Hamiltonianは別の正準変数だけに作用するのでPoisson可換であり、B結果形成後にAから情報を送る必要はない。

singlet型について、平面角の固有ベクトルを標準的に選べば

```math
|\langle A_x,B_y|c_{\rm s}\rangle|^2
=
\frac14
\left[
1-AB\cos(x-y)
\right].
```

和を取れば両周辺は $1/2$、符号積を取れば $E(x,y)=-\cos(x-y)$ となる。第5章のCHSH設定を代入すれば $2\sqrt2$ である。

## D.7 外部記録と逆実行順序

A、B端の配置領域へ支持を持つ滑らかな検出関数を $d_A,d_B$ とする。外部記録セルへの生成子を

```math
G_{\rm rec}
=
P_A^R d_A
+
P_B^R d_B
```

とする。理想空入口 $P_A^R=P_B^R=0$ では能動部への反作用は零である。検出接続域は無反応へ記録する。

前向き写像を、設定生成 $S$、singlet準備 $U_{\rm s}$、A分析器 $U_A^x$、A読出し・2端準備 $C_A$、局所分析器 $M_A^x,M_B^y$、記録 $R$ と書く。記録後は

```math
\begin{aligned}
M_B^{-1}
&\longrightarrow
M_A^{-1}
\longrightarrow
C_A^{-1}\\
&\longrightarrow
(U_A^x)^{-1}
\longrightarrow
U_{\rm s}^{-1}
\longrightarrow
S^{-1}
\end{aligned}
```

の時間順序で内部写像を戻す。記録剪断 $R$ は逆実行しない。履歴セルが全分岐を保存するので、無反応を含む全入力で逆写像が定義される。

## D.8 測定開始面とBell前提

設定生成から2端準備までの写像を $T_{xy}$ とする。測定開始面では

```math
\mu_{\rm meas}^{xy}
=
(T_{xy})_\#
\mu_0(\cdot\mid x,y).
```

$T_{xy}$ は $x$ をA分析器へ使うので、共同実現配置のA成分、条件付きB場、履歴を含む完全状態分布は $x$ に依存する。従って測定設定独立性は成立しない。

一方、2端準備後の局所応答は別々の局所状態に条件付けて因子化する。非信号性はD.5節とsinglet対称性から従う。Bellの定理の結論と矛盾せず、前提違反の位置が中央準備段にある。

## D.9 有限誤差の合成

第5章の前向き誤差項を、それぞれ対応する有限写像の全変動距離または状態距離から出力分布距離へ換算する。逐次核 $K_1,\ldots,K_m$ と理想核 $K_1^0,\ldots,K_m^0$ が各段で一様に $\epsilon_j$ 以下なら、逐次結合から

```math
D_{\rm TV}
\left(
\mu K_1\cdots K_m,
\mu K_1^0\cdots K_m^0
\right)
\leq
\sum_{j=1}^m\epsilon_j.
```

従って

```math
\begin{aligned}
\epsilon_{\rm fwd}
\leq{}&
\delta_{\rm set}
+\varepsilon_{\rm prep}
+\varepsilon_{\rm reg}
+\varepsilon_{\rm disc}
+\varepsilon_{\rm sel}\\
&+
\varepsilon_{\rm move}
+\varepsilon_{\rm cond}
+\varepsilon_{\rm win}
+\varepsilon_{\rm det}
+\varepsilon_{\rm rec}
+\varepsilon_{\rm clk}^{\rm fwd}.
\end{aligned}
```

固定した有限時間と更新数について、R115、R116の順に有限パラメータを選べば各項を任意に小さくできる。逆計算とresetの誤差は $\varepsilon_{\rm ret}$ として次周期へ渡す。

## D.10 R121の証明と限界

<!-- theorem-start:proof -->
**証明（R121）**

D.1、D.2節が設定前開始面と鋭い基準配置からのsinglet型準備、D.3節がA分析器後の共同配置読出し、D.4節が可逆な条件付き2端準備、D.5節が非選択B状態、D.6節が局所共同分布、D.7節が永久記録と逆計算、D.9節が有限誤差合成を与える。固定有限プログラムを互いに重ならない時計窓へ置けば有限自律Hamiltonianへ埋め込める。従ってR121が従う。
<!-- theorem-end:proof -->

本付録は、操作的接続、固定singlet型、準備先行、非空間分離、固定有限設定、無反応込みの任意精度に限定される。非因子化4頂点場全体の状態的分配、準備後の自由設定、空間分離、一般Tsirelson原理、独立同分布型標本統計、無期限記録を固定容量へ蓄積することは証明していない。
