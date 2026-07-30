# 測定設定依存度の表現論的比較

> **位置づけ。** draft-10の付録E.1〜E.3を整理した比較メモ。Bell の前提監査は現行本文第7.9節で完結するため、装置事後分布の依存度と、同じ観測分布を再現する抽象表現の最小値との比較を論文生成から外した。

関連文献：A. Fine, “Hidden Variables, Joint Probability, and the Bell Inequalities,” Physical Review Letters 48, 291–295 (1982). <https://doi.org/10.1103/PhysRevLett.48.291>

## 1. Hall尺度

測定設定に依存する未読変数分布に対する $L^1$ 尺度を

```math
M
=
\sup_{a,b,a',b'}
\int
\left|
\rho(\lambda\mid a,b)
-
\rho(\lambda\mid a',b')
\right|
d\lambda
```

とする。通常の最大全変動距離とは

```math
M=2D_{\rm TV}^{\max}
```

の関係にある。

本文の最小2モード事後分布では

```math
D_{\rm TV}(c,c')
=
\frac{V_{\rm eff}}2
|c-c'|
```

なので、

```math
M_{\rm dev}
=
V_{\rm eff}
\sup
\left|
\cos\Delta_{ab}
-
\cos\Delta_{a'b'}
\right|.
```

全角度を許せば $M_{\rm dev}=2V_{\rm eff}$、標準 CHSH の4設定対では

```math
M_{\rm dev}^{(4)}
=
\sqrt2V_{\rm eff}
```

となる。これは本文の具体的な装置事後分布の値であり、全ての局所表現の中で最小化した値ではない。

## 2. 確率表を直接埋め込む表現

未読変数を $\lambda_{\rm tab}=(A_*,B_*)$ とし、

```math
\rho_{\rm tab}(A_*,B_*\mid a,b)
=
\frac14
\left[
1-A_*B_*V_{\rm eff}\cos\Delta_{ab}
\right]
```

と置けば、局所決定論的に目標共同法則を再現できる。この表現は出力確率を未読変数分布へ直接書き込んだものであり、物理的説明ではない。本文の装置事後分布と同じ尺度値を持っても、装置構成の最適性や力学的起源は示さない。

## 3. 標準 CHSH 4設定での下界

$V_{\rm eff}\leq1/\sqrt2$ では全 CHSH 不等式が満たされ、測定設定と独立な共同未読変数分布を選べるため、

```math
M_{\min}^{(4)}
=
0.
```

$V_{\rm eff}>1/\sqrt2$ では、緩和された CHSH 上界から

```math
M_{\min}^{(4)}(V_{\rm eff})
\geq
\frac{
2\sqrt2V_{\rm eff}-2
}{3}
```

を得る。既知の表現を混合すると、この4設定問題では

```math
M_{\min}^{(4)}(V_{\rm eff})
=
\max
\left\{
0,
\frac{
2\sqrt2V_{\rm eff}-2
}{3}
\right\}
```

を達成できる。

$V_{\rm eff}=1$ では

```math
M_{\min}^{(4)}
=
\frac{2(\sqrt2-1)}3,
\qquad
M_{\rm dev}^{(4)}
=
\sqrt2.
```

したがって明示装置の事後分布は、この表現論的尺度について最小ではない。

## 4. 現行理論への意味

この比較は、測定設定依存性の量がモデル表現に依存することを示す。有限 Hamiltonian 装置が表現論的最小値を実現できること、全角度の余弦族で同じ最小値が成り立つこと、`[R]` の物理的生成は含意しない。

## 5. 再検討条件

有限 Hamiltonian 装置の自由度、局所応答、準備対称性、終端関数を固定したうえで、測定設定依存度の下界または最適化定理が得られた場合に、本文へ戻す価値がある。
