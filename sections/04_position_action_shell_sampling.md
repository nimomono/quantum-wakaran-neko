@number: 4
@chapter: 本文
@title: 位置入口作用殻と Born 型標本化
@status: 一般作用殻容量、2モード殻の線形重み、作用分配次元の剛性は厳密結果である。位置入口頻度には共通流束因子を仮定する。一般 Born 則、初期流束同期、標本化後の再埋め込みは未完成である。

## 4.1 一般作用殻容量

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
\left|
a_k
\right|^2
```

とする。固定総作用 $\sum_kJ_k=A$ の未規格化 Liouville 殻容量を

```math
\Omega_n(A)
=
\int
\delta
\left(
A-\sum_{k=1}^nJ_k
\right)
\prod_{k=1}^n
dJ_k
\,d\theta_k
```

と定める。

<!-- theorem-start:theorem -->
**定理（一般作用殻容量）**
$A>0$ に対し、

```math
\Omega_n(A)
=
\frac{
\left(
2\pi
\right)^n
}{
\left(
n-1
\right)!
}
A^{n-1}
```

が成立する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
角変数の積分が $(2\pi)^n$ を与える。残る作用変数は、$J_k\geq0$ と $\sum_kJ_k=A$ が作る $(n-1)$ 次元単体のデルタ測度であり、$A^{n-1}/(n-1)!$ である。
<!-- theorem-end:proof -->

位置入口と Bell 比較殻で線形重みを得るには $n=2$ が重要である。

## 4.2 排他的な位置入口

有限セルで代表場強度を

```math
q_i
=
\left|
\bar\zeta_i
\right|^2,
\qquad
\sum_i
q_i
\Delta V
=
1
```

とする。全入口作用 $A_{\rm tot}>0$ を

```math
A_i
=
A_{\rm tot}
q_i
\Delta V
```

とセルへ割り当てる。

入口反応面は排他的な和

```math
\Gamma_\partial
=
\bigsqcup_i
\Gamma_{\partial,i}
```

とする。1つの履歴は1つの入口面だけを通過する。他セルの作用殻を同じ履歴について直積しない。

各入口セクターでは、選択された活性モードの作用を $K_i$、全チャンネルで共有する明反応座標の作用を $I$ とし、

```math
K_i+I
=
A_i
```

を課す。作用を直接分配する方向はこの2モードだけであり、残る自由度は付随因子として扱う。

## 4.3 正方向 Liouville 流束

$n=2$ の殻容量は

```math
\Omega_2(A_i)
=
\left(
2\pi
\right)^2
A_i
```

である。正方向入口流束を

```math
\mathscr F_i
=
\int_{
\Gamma_{\partial,i}
}
\left(
\dot s_i
\right)_+
d\mu_i
```

とする。$s_i$ は入口面の法線座標である。作用殻の線形容量以外を流束因子 $\lambda_i$ へまとめ、

```math
\mathscr F_i
=
\lambda_i
\Omega_2(A_i)
```

と書く。$\lambda_i$ は、法線速度、障壁透過、入口面の向き、余面積 Jacobian、付随自由度の体積、有限入口窓、解多重度を含む。

## 4.4 主定理2

<!-- theorem-start:theorem -->
**定理（2モード作用殻による位置入口標本化）**
次を仮定する。

1. 入口面が排他的な和である。
2. 各入口セクターで2モード総作用が $A_i=A_{\rm tot}q_i\Delta V$ である。
3. 全チャンネルで $\lambda_i=\lambda>0$ である。
4. 各開始履歴を正方向入口通過として1回だけ数える。
5. 結果または位置に応じて失敗履歴を捨てない。

このとき、

```math
P_i
=
\frac{
\mathscr F_i
}{
\sum_j
\mathscr F_j
}
=
q_i
\Delta V
=
\left|
\bar\zeta_i
\right|^2
\Delta V
```

が成立する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
共通 $\lambda$ と $\Omega_2(A_i)=(2\pi)^2A_i$ により、

```math
P_i
=
\frac{
A_i
}{
\sum_jA_j
}
```

である。$\sum_jA_j=A_{\rm tot}$ を代入する。
<!-- theorem-end:proof -->

この定理は場強度を確率と定義した結果ではない。入口反応面を横切る Liouville 流束の相対頻度である。

## 4.5 共通流束条件からのずれ

基準流束因子 $\lambda>0$ に対し、

```math
\frac{
\lambda_i
}{
\lambda
}
=
1+\delta_i
```

とする。一般には

```math
P_i
=
\frac{
q_i
\Delta V
\left(
1+\delta_i
\right)
}{
\sum_j
q_j
\Delta V
\left(
1+\delta_j
\right)
}
```

である。主要な標本化誤差を

```math
\varepsilon_{\rm sample}
=
\max_i
\left|
\delta_i
\right|
```

とすれば、

```math
P_i
=
q_i
\Delta V
+
O
\left(
\varepsilon_{\rm sample}
\right)
```

となる。位置依存の障壁と法線速度だけでなく、余面積 Jacobian、付随体積、入口分解能、解多重度も共通でなければならない。

## 4.6 作用分配次元の剛性

活性モードに加えて、作用を直接受け取る独立な明反応方向が $d_{\rm A}$ 個あるとする。固定総作用殻は $d_{\rm A}+1$ モードなので、

```math
\Omega_{
d_{\rm A}+1
}
(A_i)
\propto
A_i^{d_{\rm A}}
```

である。

<!-- theorem-start:proposition -->
**命題（直接作用分配次元の剛性）**
共通流束因子の下で、

```math
P_i
\propto
\left(
q_i
\Delta V
\right)^{d_{\rm A}}
```

となる。線形則には $d_{\rm A}=1$ が必要である。
<!-- theorem-end:proposition -->

追加自由度が時計、混合角、記録、不要情報だけを担い、総作用を直接分配しないなら、共通の付随因子として線形則を壊さない。

## 4.7 殻内混合とセクター質量

選択された2モードを $a_i$ とすると、総作用は $A_i=a_i^\dagger a_i$ である。$u(2)$ 生成子 $T_\alpha$ を用いた殻接混合

```math
H_{\rm mix}^{(i)}
=
\varepsilon_{\rm mix}
\chi_i(X)
\sum_\alpha
\xi_\alpha
a_i^\dagger
T_\alpha
a_i
```

は

```math
\left\{
A_i,
H_{\rm mix}^{(i)}
\right\}
=
0
```

を満たす。従って殻内角分布は変えられる。

しかし、正規化された初期集団を Hamiltonian 写像で押し出しても、入口セクターの総確率質量は保存される。殻内混合だけでは、セクター間の質量を $\Omega_2(A_i)$ に比例させられない。主定理2の共通未規格化流束条件は、殻内混合とは独立の仮定である。同じ制限は第5章の Bell 境界殻にも現れる。

## 4.8 初期密度同期との関係

主定理2は、入口直後の粒子位置頻度を $q_i\Delta V$ にできる。この意味で、第3章の初期密度同期

```math
\rho(0)
\approx
\left|
\psi(0)
\right|^2
```

の分布部分を供給する候補である。

ただし、次は供給しない。

1. 粒子流束と場流束の同期。
2. 粒子速度分散の小ささ。
3. 位相接続に沿う単流束化。
4. 標本化後の活性場を同じコヒーレント部分空間へ戻す写像。
5. 共有明反応座標と準備浴の反復可能な再初期化。

従って、主定理2が主定理1の全初期条件を準備するとは書かない。

## 4.9 一般 Born 則との区別

本章の結果は、次に限定される。

1. 位置入口チャンネルの通過頻度。
2. 1つの直接作用分配方向を持つ2モード殻。
3. チャンネル間で共通な未規格化流束。
4. 場強度に比例する入口前の作用分配。
5. 無条件に数えられる全開始履歴。

任意基底、一般射影測定、連続スペクトルの有限分解能、複合系の一般 Born 則は示していない。位置入口標本化は Born 則の部分達成であり、一般測定理論ではない。
