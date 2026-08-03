@number: 4
@chapter: 本文
@title: 境界作用殻による Born 型入口標本化
@status: 一般作用殻体積、2モード殻の線形重み、共通流束因子の下での位置入口密度、直接作用分配次元の剛性は厳密結果である。等方準備と標本化後の再埋め込みは未完成である。

## 4.1 一般作用殻体積

$n$個の複素正準モードを

```math
a_k
=
\frac{
q_k+ip_k
}{
\sqrt2
},
\qquad
J_k
=
|a_k|^2
```

とする。作用角変数では

```math
dq_k\,dp_k
=
dJ_k\,d\theta_k.
```

固定総作用

```math
\sum_{k=1}^nJ_k=A,
\qquad
J_k\geq0
```

の未規格化 Liouville 殻容量を

```math
\Omega_n(A)
=
\int
\delta
\left(
A-\sum_{k=1}^nJ_k
\right)
\prod_{k=1}^n
dJ_k\,d\theta_k
```

と定める。

<!-- theorem-start:theorem -->
**定理（一般作用殻容量）**
$A>0$ に対し、

```math
\Omega_n(A)
=
\frac{
(2\pi)^n
}{
(n-1)!
}
A^{n-1}.
```
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
角変数の積分が $(2\pi)^n$ を与える。残る作用変数の積分は、$J_k\geq0$ と $\sum_kJ_k=A$ が作る $(n-1)$ 次元単体のデルタ測度であり、$A^{n-1}/(n-1)!$ である。
<!-- theorem-end:proof -->

このべき指数が Born 型重みと Bell 型重みを決める。

## 4.2 局所作用と排他的入口チャンネル

第3章の活性場強度をセル表示へ戻し、

```math
\sum_i r_i^2\Delta V
=
1
```

とする。全入口作用 $A_{\rm tot}>0$ をセルへ

```math
A_i
=
A_{\rm tot}r_i^2\Delta V
```

と割り当てる。

入口反応面は

```math
\Gamma_\partial
=
\bigsqcup_i
\Gamma_{\partial,i}
```

という排他的な和とする。1つの履歴が通過するのは1つの $\Gamma_{\partial,i}$ だけである。他セルの入口殻を同時に積分しない。

比較器または反応座標は全チャンネルで共有する。粒子位置窓 $\chi_i(X)$ が、セル $i$ の活性モードと共有明反応座標を選択的に結合する。各排他的sectorで、活性側に残る作用を $K_i$、共有反応座標の作用を $I$ とし、

```math
K_i+I=A_i
```

を課す。

## 4.3 2モード殻の線形容量

$n=2$ の一般定理から、

```math
\Omega_2(A_i)
=
(2\pi)^2A_i.
```

正方向入口流束を

```math
\mathscr F_i
=
\int_{\Gamma_{\partial,i}}
\left(
\dot s_i
\right)_+
d\mu_i
```

とする。$s_i$ は反応面の法線座標、$d\mu_i$ は作用殻、spectator自由度、coarea因子を含む誘導測度である。

作用殻の線形容量以外を流束因子 $\lambda_i$ へまとめ、

```math
\mathscr F_i
=
\lambda_i\Omega_2(A_i)
```

と書く。$\lambda_i$ は、法線速度、障壁透過、反応面の向き、coarea Jacobian、spectatorモードの体積、有限入口窓を含む。

<!-- theorem-start:theorem -->
**定理（2モード入口殻からの Born 型位置重み）**
全チャンネルで

```math
\lambda_i=\lambda>0
```

が成立し、各開始履歴を正方向入口通過として1回ずつ数えるなら、

```math
P_i
=
\frac{
\mathscr F_i
}{
\sum_j\mathscr F_j
}
=
r_i^2\Delta V.
```

従ってセル平均の入口密度は

```math
\rho_{{\rm in},i}
=
r_i^2.
```
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
共通 $\lambda$ と $\Omega_2(A_i)=(2\pi)^2A_i$ により、

```math
P_i
=
\frac{A_i}{\sum_jA_j}.
```

$\sum_jA_j=A_{\rm tot}$ と $A_i=A_{\rm tot}r_i^2\Delta V$ を代入する。
<!-- theorem-end:proof -->

これは場強度を確率と定義した結果ではない。入口反応面を横切る Liouville 流束の相対頻度として得た結果である。

## 4.4 共通流束条件と誤差

一般には、基準流束因子 $\lambda>0$ に対する相対偏差を

```math
\frac{\lambda_i}{\lambda}
=
1+\delta_i
\qquad
\sum_i
r_i^2\Delta V\,\delta_i
=
0
```

と定義する。すると

```math
P_i
=
\frac{
r_i^2\Delta V
\left(
1+\delta_i
\right)
}{
\sum_j
r_j^2\Delta V
\left(
1+\delta_j
\right)
}.
```

従って

```math
\varepsilon_{\rm flux}
=
\max_i|\delta_i|
```

が Born 型重みからの主要な1次誤差になる。位置依存の障壁、セル体積、窓関数、法線速度を同じにしただけでは十分でなく、coarea Jacobian と解多重度も共通でなければならない。

## 4.5 作用分配次元の剛性

活性モードに加えて、作用を直接受け取る独立な明反応方向が $q$ 個あるとする。固定総作用殻は $q+1$ モードなので、

```math
\Omega_{q+1}(A_i)
\propto
A_i^q.
```

<!-- theorem-start:proposition -->
**命題（直接作用分配次元の剛性）**
共通流束因子の下で、入口重みは

```math
P_i
\propto
\left(
r_i^2\Delta V
\right)^q.
```

Born 型の線形則を得るには $q=1$ が必要である。
<!-- theorem-end:proposition -->

この結果は、任意に多数の比較器または明反応座標を追加できないことを示す否定的結果である。追加自由度が作用を直接分配せず、共通 spectator因子としてだけ現れるなら線形則を壊さない。

## 4.6 2モード殻の等方混合と境界密度

排他的チャンネル $i$ で、選択された活性モードと共有明反応座標を

```math
a_i
=
\begin{pmatrix}
a_{{\rm A},i}\\
a_{\rm R}
\end{pmatrix}
```

とする。2モード総作用は

```math
A_i
=
a_i^\dagger a_i.
```

暗モード $z_{\rm D}$ が殻接方向だけを混ぜる候補 Hamiltonian を

```math
H_{\rm mix}^{(i)}
=
\varepsilon_{\rm mix}
\chi_i(X)
\sum_\alpha
\xi_\alpha(z_{\rm D})
a_i^\dagger T_\alpha a_i
```

とする。$T_\alpha$ は $u(2)$ の Hermitian 生成子である。

```math
\left\{
A_i,
H_{\rm mix}^{(i)}
\right\}
=
0
```

なので、暗モードが混合を駆動しても2モード総作用は保存される。暗モードへ作用を直接移す座標結合は、$K_i+I=A_i$ を壊すため採用しない。

Born 側で必要なのは、各排他的sectorの2モード殻全体に対する $U(2)$ 等方性である。第6章の Bell 比較殻も2モード全殻を使うため、両者の容量は同じ線形則に従う。

ただし、等方混合とsector間の頻度を区別しなければならない。正規化された初期集団を Hamiltonian 写像で押し出しても、排他的sector $i$ の総確率質量は保存される。$U(2)$ 混合は殻上の角分布を変えるが、

```math
\mu_i
\longmapsto
\left(
\mathcal U_i
\right)_*\mu_i
```

によって $\mu_i(\Gamma_{\partial,i})$ を $\Omega_2(A_i)$ 倍にはしない。従って、Born 型頻度には、全sectorへ共通の未規格化境界密度または共通流束を置く条件が別に必要である。第4.3節の $\lambda_i=\lambda$ はこの条件を表す。

この区別は Bell 側でも同じである。2モード殻容量の線形性は厳密だが、容量に比例する境界測度を実験周期が準備することは未解決である。

## 4.7 一般 Born 則との区別

本章の結果は次に限定される。

1. 位置入口チャンネルの標本頻度である。
2. 2モード作用殻と1つの直接作用分配方向を使う。
3. チャンネル間で流束因子が共通である。
4. 入口前に $A_i=A_{\rm tot}r_i^2\Delta V$ が準備されている。
5. 入口履歴を事後的に捨てない。

任意基底、一般の射影測定、連続スペクトルの有限分解能、複合系の一般 Born 則は示していない。それでも、確率重みを場強度の定義として置かず、作用殻の次元と Liouville 流束から位置重みを出した点で部分達成である。

## 4.8 標本化後の再埋め込み問題

2モード殻を混合すると、活性側に残る作用 $K_i$ は一般に標本化前の値と異なる。そのままでは、入口重みを与えた $r_{\rm in}$ と、その後の位相接続力学を担う $r$ が一致しない。

完全周期には、

1. 結果情報を暗モードまたは記録器へ可逆に転送する。
2. 活性場を同じ coherent部分空間へ再埋め込みする。
3. 共有明反応座標を基準状態へ戻す。
4. 全位相作用 $\mathcal J_\phi$ と規格化を保つ。
5. 結果別に履歴を捨てず、次試行を同じ準備分布から始める。

ことが必要である。再埋め込み誤差を

```math
\varepsilon_{\rm reset}
```

とする。本章は $\varepsilon_{\rm reset}$ を有限 Hamiltonian 周期から小さくする構成を与えない。第6章の比較器では、結果を外部記録へコピーした後の理想的な逆計算を構成するが、入口側の活性場再埋め込みまで自動的に解決しない。
