@number: 4
@chapter: 本文
@title: 位置入口作用殻と Born 型標本化
@status: 一般作用殻容量、2モード殻の線形重み、作用分配次元の剛性は厳密結果である。位置入口頻度には単一試行の局所作用転送と共通流束因子を仮定する。一般 Born 則、排他的な全局所転送、標本化後の完全周期は未完成である。

## 4.1 相関対角成分と規格化セル重み

セル体積を吸収した相関行列 $C$ に対し、

```math
p_i
=
\frac{C_{ii}}{\operatorname{tr}C},
\qquad
\sum_i p_i=1
```

と定める。$p_i$ は相関行列の正規化対角成分であり、この段階では粒子確率と定義しない。

階数1の場合は

```math
C
=
\Lambda\chi\chi^\dagger,
\qquad
\chi^\dagger\chi=1
```

なので、

```math
p_i
=
\left|\chi_i\right|^2
```

である。連続密度表示 $\psi_i=\chi_i/\sqrt{\Delta V}$ を用いる場合だけ、

```math
p_i
=
\left|\psi_i\right|^2
\Delta V
```

と書く。正規化済みの $p_i$ へさらにセル体積を掛けない。

## 4.2 単一試行の局所作用

各試行の局所位相担体作用は

```math
I_i^\omega
=
\mathcal J_0
\left|b_i^\omega\right|^2
```

である。集団平均は

```math
\mathbb E
\left[
I_i^\omega
\mid
\mathcal P
\right]
=
\mathcal J_0C_{ii}
```

となる。

単位作用の共通源準備 $b^\omega=e^{i\beta^\omega}\chi$ では、絶対位相が試行ごとに異なっても

```math
I_i^\omega
=
\mathcal J_0
\left|\chi_i\right|^2
=
\mathcal J_0p_i
```

が各試行で成立する。従って、この理想階数1集団では装置が集団量 $C_{ii}$ を直接読む必要はない。各試行に実在する局所作用を転送すればよい。

## 4.3 単一入口の理想作用交換

入口 $i$ の受け取りモードを $d_i$ とし、初期値を $d_i=0$ とする。局所交換 Hamiltonian を

```math
H_{{\rm tr},i}
=
i\mathcal J_0g_i(t)
\left(
d_i^*b_i-b_i^*d_i
\right)
```

とする。これは実数であり、$b_i$ と $d_i$ の全作用を保存する。交換角

```math
\Theta_i
=
\int g_i(t)\,dt
```

が $\pi/2$ なら、自由発展を無視する理想パルスで

```math
b_i^{\rm out}=0,
\qquad
d_i^{\rm out}=b_i^{\rm in}
```

となる。従って局所作用は破壊的に入口モードへ移る。

この交換は1つの指定入口では明示的である。しかし、全 $i$ の担体を同時に独立な入口殻へ移すと殻の直積が現れ、位置結果の排他的な和にならない。粒子位置、局所反応窓、共有反応座標を含め、1試行につき1つの入口だけを作動させる有限 Hamiltonian は未完成である。本章では、この排他的局所転送を独立の成立条件として明記する。

## 4.4 一般作用殻容量

$n$個の複素正準モードを

```math
a_k
=
\frac{q_k+ip_k}{\sqrt2},
\qquad
J_k
=
\left|a_k\right|^2
```

とする。固定総作用 $\sum_kJ_k=A$ の未規格化 Liouville 殻容量を

```math
\Omega_n(A)
=
\int
\delta
\left(
A-
\sum_{k=1}^nJ_k
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
\left(2\pi\right)^n
}{
\left(n-1\right)!
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

## 4.5 排他的な位置入口

主定理2では、固定振幅の共通源

```math
b^\omega
=
e^{i\beta^\omega}\chi
```

を仮定する。すると全ての試行で

```math
I_i^\omega
=
\mathcal J_0p_i,
\qquad
I_{\rm ph}^\omega
=
\mathcal J_0
```

となる。単一試行の局所作用を、全チャンネルで共通な変換係数によって入口自由度へ移す。変換後の全入口作用を $A_{\rm tot}>0$ とすれば、各試行で

```math
A_i
=
A_{\rm tot}p_i
```

となる。理想単位作用交換では $A_{\rm tot}=\mathcal J_0$ とできる。増幅または単位変換を含む場合は、全チャンネルで共通の係数を $A_{\rm tot}$ へ吸収する。この順序では、単一試行の装置が集団量 $C_{ii}$ または $p_i$ を読み取る必要はない。

入口反応面は排他的な和

```math
\Gamma_\partial
=
\bigsqcup_i
\Gamma_{\partial,i}
```

とする。1つの履歴は1つの入口面だけを結果として通過する。他セルの作用殻を同じ履歴について直積しない。

各入口セクターでは、選択された活性モードの作用を $K_i$、全チャンネルで共有する明反応座標の作用を $I$ とし、

```math
K_i+I
=
A_i
```

を課す。作用を直接分配する方向はこの2モードだけであり、時計、記録、混合角などの残る自由度は付随因子として扱う。

## 4.6 正方向 Liouville 流束

$n=2$ の殻容量は

```math
\Omega_2(A_i)
=
\left(2\pi\right)^2A_i
```

である。正方向入口流束を

```math
\mathscr F_i
=
\int_{\Gamma_{\partial,i}}
\left(\dot s_i\right)_+
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

## 4.7 主定理2

<!-- theorem-start:theorem -->
**定理（2モード作用殻による位置入口標本化）**
次を仮定する。

1. 固定振幅の階数1共通源 $b^\omega=e^{i\beta^\omega}\chi$ が準備される。
2. 入口面が排他的な和である。
3. 各試行の局所位相担体作用が、該当する入口の2モード総作用 $A_i=A_{\rm tot}p_i$ へ転送される。
4. 全チャンネルで $\lambda_i=\lambda>0$ である。
5. 各開始履歴を正方向入口通過として1回だけ数える。
6. 結果または位置に応じて失敗履歴を捨てない。

このとき、

```math
P_i
=
\frac{\mathscr F_i}{\sum_j\mathscr F_j}
=
p_i
=
\frac{C_{ii}}{\operatorname{tr}C}
```

が成立する。階数1の連続密度表示では

```math
P_i
=
\left|\psi_i\right|^2
\Delta V
```

である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
共通 $\lambda$ と $\Omega_2(A_i)=(2\pi)^2A_i$ により、

```math
P_i
=
\frac{A_i}{\sum_jA_j}
```

である。$\sum_jA_j=A_{\rm tot}$ を代入する。
<!-- theorem-end:proof -->

この定理は $C_{ii}$ を確率と定義した結果ではない。固定振幅の共通源が各試行に同じ相対作用分配を準備し、その単一試行作用を入力とする入口反応面を横切る Liouville 流束の相対頻度である。

## 4.8 共通流束条件からのずれ

基準流束因子 $\lambda>0$ に対し、

```math
\frac{\lambda_i}{\lambda}
=
1+\delta_i
```

とする。一般には

```math
P_i
=
\frac{
p_i\left(1+\delta_i\right)
}{
\sum_jp_j\left(1+\delta_j\right)
}
```

である。主要な標本化誤差を

```math
\varepsilon_{\rm sample}
=
\max_i\left|\delta_i\right|
```

とすれば、

```math
P_i
=
p_i
+
O\left(\varepsilon_{\rm sample}\right)
```

となる。位置依存の障壁と法線速度だけでなく、余面積 Jacobian、付随体積、入口分解能、解多重度も共通でなければならない。

局所作用転送誤差を $A_i=A_{\rm tot}(p_i+\eta_i)$、$\sum_i\eta_i=0$ と書けば、確率誤差には $O(\max_i|\eta_i|)$ が加わる。試行ごとの全振幅が変動する場合は、$A_{\rm tot}^\omega$ と入口流束因子の相関も評価しなければならない。階数欠陥、全振幅ゆらぎ、作用転送誤差、流束非対称性を1つの量へ無差別にまとめない。

## 4.9 作用分配次元の剛性

活性モードに加えて、作用を直接受け取る独立な明反応方向が $d_{\rm A}$ 個あるとする。固定総作用殻は $d_{\rm A}+1$ モードなので、

```math
\Omega_{d_{\rm A}+1}(A_i)
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
p_i^{d_{\rm A}}
```

となる。線形則には $d_{\rm A}=1$ が必要である。
<!-- theorem-end:proposition -->

追加自由度が時計、混合角、記録、不要情報だけを担い、総作用を直接分配しないなら、共通の付随因子として線形則を壊さない。

## 4.10 殻内混合とセクター質量

選択された2モードを $a_i$ とすると、総作用は $A_i=a_i^\dagger a_i$ である。$u(2)$ 生成子 $T_\alpha$ を用いた殻接混合

```math
H_{\rm mix}^{(i)}
=
\varepsilon_{\rm mix}
\chi_i(X)
\sum_\alpha
\xi_\alpha
a_i^\dagger T_\alpha a_i
```

は

```math
\left\{A_i,H_{\rm mix}^{(i)}\right\}
=
0
```

を満たす。従って殻内角分布は変えられる。

しかし、正規化された初期集団を Hamiltonian 写像で押し出しても、入口セクターの総確率質量は保存される。殻内混合だけでは、セクター間の質量を $\Omega_2(A_i)$ に比例させられない。主定理2の共通未規格化流束条件は、殻内混合とは独立の仮定である。同じ制限は第5章の Bell 境界殻にも現れる。

## 4.11 一般 Born 則との区別

本章の結果は、次に限定される。

1. 位置入口チャンネルの通過頻度。
2. 1つの直接作用分配方向を持つ2モード殻。
3. チャンネル間で共通な未規格化流束。
4. 単一試行の局所位相担体作用に比例する入口作用。
5. 無条件に数えられる全開始履歴。

任意基底、一般射影測定、連続スペクトルの有限分解能、複合系の一般 Born 則は示していない。また、途中の粒子軌道を与えず、測定入口での結果頻度だけを扱う。
