@number: 3
@chapter: 本文
@title: 相関行列力学、空間グラフ、干渉と節
@status: 共通2次 Hamiltonian 下の相関行列発展、階数1因子の発展、有限グラフ上の干渉、階数欠陥による節の残留強度上界は厳密である。局所結合係数の必然的導出、連続極限、位相量子化、粒子の連続運動は未完成である。

## 3.1 相関行列の閉じた発展

各試行が共通の有限2次 Hamiltonian に従い、

```math
i\mathcal J_0\dot b^\omega
=
h(t)b^\omega
```

を満たすとする。

<!-- theorem-start:theorem -->
**定理（相関行列の交換子発展）**
相関行列

```math
C(t)
=
\mathbb E
\left[
b^\omega(t)
\left(b^\omega(t)\right)^\dagger
\mid
\mathcal P
\right]
```

は厳密に

```math
i\mathcal J_0\dot C
=
\left[h,C\right]
```

を満たす。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
$bb^\dagger$ を微分し、$i\mathcal J_0\dot b=hb$ とその共役転置を代入すると

```math
i\mathcal J_0
\frac{d}{dt}
\left(bb^\dagger\right)
=
hbb^\dagger
-
bb^\dagger h
```

となる。集団平均を取る。
<!-- theorem-end:proof -->

この方程式は、単一の統計振幅 $\chi$ を先に仮定しない。基礎的な集団状態は $C$ である。

## 3.2 保存量

時間発展作用素を

```math
i\mathcal J_0\dot U(t,t_0)
=
h(t)U(t,t_0),
\qquad
U(t_0,t_0)=I
```

とする。$h=h^\dagger$ なら $U$ はユニタリであり、

```math
C(t)
=
U(t,t_0)
C(t_0)
U(t,t_0)^\dagger
```

となる。

<!-- theorem-start:corollary -->
**系（相関スペクトルの保存）**
閉鎖線形発展では、$C$ の跡、全固有値、階数、および

```math
\mathcal P_C
=
\frac{\operatorname{tr}C^2}{\left(\operatorname{tr}C\right)^2}
```

で定める純度が保存される。
<!-- theorem-end:corollary -->

従って、観測窓の理想2次発展は既に準備された相関を回転させるだけである。相関の純化または熱化を説明しない。

## 3.3 階数1因子の Schrödinger 型発展

$C=\Lambda\chi\chi^\dagger$、$\chi^\dagger\chi=1$ とする。$\Lambda=\operatorname{tr}C$ は保存される。

<!-- theorem-start:theorem -->
**定理（階数1統計振幅の発展）**
相関行列が階数1で交換子方程式に従うなら、ある実関数 $\lambda(t)$ が存在して

```math
i\mathcal J_0\dot\chi
=
h\chi
+
\lambda(t)\chi
```

となる。時間依存共通位相を選べば、

```math
i\mathcal J_0\dot\chi
=
h\chi
```

とできる。
<!-- theorem-end:theorem -->

証明は付録Aに置く。$\lambda(t)$ は射影 $\chi\chi^\dagger$ に影響しない共通位相だけを表す。

この定理は Schrödinger 型の有限次元形式を与えるが、$h$ の物理的内容を自動的に決めない。任意の Hermitian 行列を選べること自体は、量子力学的構造の創発ではない。

## 3.4 空間グラフ上の局所 Hamiltonian

有限空間グラフ $G=(V,E)$ を取り、各頂点に1つの位相担体を置く。辺係数 $g_{ij}=g_{ji}\geq0$ は長さの逆2乗の次元を持つとする。グラフ Laplacian を

```math
\left(L_G\chi\right)_i
=
\sum_{j:\{i,j\}\in E}
g_{ij}
\left(
\chi_i-\chi_j
\right)
```

と定める。局所外部ポテンシャルを $V_i(t)$ とし、

```math
h_L(t)
=
\frac{\mathcal J_0^2}{2m}
L_G
+
\operatorname{diag}
\left(
V_1(t),\ldots,V_L(t)
\right)
```

と置く。

対応する古典 Hamiltonian は

```math
H_{\rm ph}
=
\frac{\mathcal J_0^2}{2m}
\sum_{\{i,j\}\in E}
g_{ij}
\left|b_i-b_j\right|^2
+
\sum_i
V_i(t)
\left|b_i\right|^2
```

である。各辺は隣接位相担体だけを結び、各ポテンシャル項は局所モードだけに作用する。$Q$ と $P$ の両直交成分へ同じ結合を置くため、共通内部回転が保たれる。

階数1因子は

```math
i\mathcal J_0\dot\chi
=
\left[
\frac{\mathcal J_0^2}{2m}L_G
+
V_L(t)
\right]
\chi
```

に従う。規則格子で $L_G$ が $-\Delta$ の整合離散化なら、これは離散 Schrödinger 型方程式である。

## 3.5 既知の古典振動子表示との区別

量子状態を古典正準座標または結合振動子へ写し、有限次元 Schrödinger 方程式と同型の運動を得ること自体は既知である [34--37]。従って、本稿は次を新規な導出として主張しない。

1. 複素ベクトルを2倍次元の実ベクトルで表すこと。
2. Hermitian 行列を2次古典 Hamiltonian として表すこと。
3. 古典結合振動子がユニタリ行列と同型の線形発展を持つこと。

本稿が検討する追加構造は、$C$ を客観的集団相関として定義し、共通源による階数1準備、位置入口作用殻、Bell 共通境界測度へ接続することである。

また、係数 $\mathcal J_0^2/(2m)$ と局所ポテンシャル $V_i$ は、本節では古典結合の設計値である。より原始的な粒子・媒質 Hamiltonian からこれらの値が必然的に現れることは未導出であり、Q1の未完成部分に残る。

## 3.6 2経路干渉

入力1モードを等分岐すると

```math
\chi_{\rm arm}
=
\frac1{\sqrt2}
\begin{pmatrix}
1\\
1
\end{pmatrix}
```

となる。経路位相 $\phi_1,\phi_2$ を蓄積し、同じ50対50混合で再結合すると

```math
\chi_+
=
\frac{
e^{i\phi_1}+e^{i\phi_2}
}{2},
\qquad
\chi_-
=
\frac{
e^{i\phi_1}-e^{i\phi_2}
}{2}
```

となる。従って

```math
p_+
=
\cos^2
\left(
\frac{\phi_1-\phi_2}{2}
\right),
\qquad
p_-
=
\sin^2
\left(
\frac{\phi_1-\phi_2}{2}
\right)
```

である。$\phi_1-\phi_2=\pi$ では $p_+=0$ となり、出力統計に完全な節が生じる。

この干渉は正の対角成分の混合だけでは生じない。再結合前の非対角相関

```math
C_{12}
=
\Lambda
\chi_1\chi_2^*
```

が相対位相を保持することが必要である。

## 3.7 階数欠陥と節の深さ

$C=\lambda_1\chi\chi^\dagger+E$、$E\geq0$ とし、ユニタリ再結合 $U$ の出力 $k$ が理想因子に対して節を持つ、すなわち $(U\chi)_k=0$ とする。

<!-- theorem-start:proposition -->
**命題（階数欠陥による節の残留強度上界）**
正規化出力強度

```math
p_k
=
\frac{
\left(UCU^\dagger\right)_{kk}
}{
\operatorname{tr}C
}
```

は

```math
p_k
\leq
\varepsilon_{\rm rank}
```

を満たす。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
節条件により主成分の寄与は零であり、

```math
p_k
=
\frac{
\left(UEU^\dagger\right)_{kk}
}{
\operatorname{tr}C
}
\leq
\frac{\left\|E\right\|_{\rm op}}{\operatorname{tr}C}
\leq
\frac{\operatorname{tr}E}{\operatorname{tr}C}
=
\varepsilon_{\rm rank}
```

である。
<!-- theorem-end:proof -->

従って、節の残留強度は階数1からのずれを直接検査する量になる。

## 3.8 位相雑音と可視度

相対位相ゆらぎを $\delta\phi$ とする。平均干渉項は

```math
\mathbb E
\left[
e^{i\delta\phi}
\right]
```

だけ減衰する。零平均 Gauss ゆらぎで分散が $\sigma_\phi^2$ なら、可視度は

```math
V_{\rm int}
=
e^{-\sigma_\phi^2/2}
```

である。小さい位相雑音では $1-V_{\rm int}=O(\sigma_\phi^2)$ となる。階数欠陥と位相雑音は異なる機構なので、検算では別に測る。

## 3.9 連続補間と離散化誤差

規則格子のセル中心 $x_i$ に $\psi_i=\chi_i/\sqrt{\Delta V}$ を置き、補間作用素を $\mathcal I_L$ とする。滑らかな試験関数に対する整合性を

```math
\left\|
L_G\mathcal R_L f
+
\mathcal R_L\Delta f
\right\|
\leq
c_L\ell^p
\left\|f\right\|_{H^{p+2}}
```

と書く。$\mathcal R_L$ はセル標本化、$\ell$ は格子幅である。

有限時間 $0\leq t\leq T$ で安定性があれば、連続 Schrödinger 型方程式との差は概ね $O(T\ell^p)$ で蓄積する。境界、非一様格子、時間依存ポテンシャルでは別の安定性定数が必要である。本稿は有限グラフの厳密結果を中心とし、一般連続極限の一様定理を主張しない。

## 3.10 固有ベクトルの条件付き包含

時間非依存 $h_L$ の固有ベクトル $\varphi_n$ が

```math
h_L\varphi_n
=
E_n\varphi_n
```

を満たすなら、

```math
\chi_n(t)
=
e^{-iE_nt/\mathcal J_0}
\varphi_n
```

は厳密解である。従って、離散ポテンシャル模型は節を持つ固有ベクトルを解として含む。

これは次を意味しない。

1. $h_L$ のスペクトルが実在粒子のエネルギー測定値になること。
2. 任意初期集団が特定の固有ベクトルへ吸引されること。
3. 基底状態または励起状態が弱開放系で選択されること。
4. 井戸型または調和型ポテンシャルの連続極限が定量的に再現されたこと。

## 3.11 粒子の連続運動を導かない

連続密度表示から形式的な統計流

```math
j_\psi
=
\frac{\mathcal J_0}{m}
\operatorname{Im}
\left(
\psi^*\nabla\psi
\right)
```

を作れる。しかし $C$ と $\psi$ は集団量であり、単一試行の粒子 Hamiltonian に $j_\psi/|\psi|^2$ を直接入れると、求める集団量をミクロ法則へ戻す循環になる。

必要なのは、単一試行の変数だけからなる

```math
\dot X^\omega
=
F_X
\left(
X^\omega,
P_X^\omega,
b^\omega,
Y^\omega
\right)
```

を先に構成し、その集団流束が $j_\psi$ へ縮約されることを示すことである。本稿はこの流束定理を持たない。

従って、主張は再結合後の統計強度と第4章の位置入口頻度までに限定する。2重スリット途中の粒子軌道、節を避ける運動、全時刻での等変性は未解決である。

## 3.12 位相量子化の位置づけ

旧2成分誘導場では、非零の単価な連続場に対する閉路巻数から条件付き循環量子化を記述できた。現行模型は有限グラフ上の位相担体を基礎とし、一般の閉路で位相差が定義できても、連続空間の単価性、節の生成・消滅、閉路変形に対する巻数保存をまだ統合していない。

従って、Wallstrom 問題は未解決へ戻す。将来の課題は、非零位相担体が置かれた空間グラフ、辺位相差、閉路巻数、連続補間、節を通る位相すべりを同じ有限 Hamiltonian で記述することである。
