@number: 4
@chapter: 本文
@title: 正準作用選択器と有限基底標本化
@status: 条件付き一様な正準角から、各試行で作用比に一致する排他的な1結果を得る式は厳密である。固定全作用と基底に依存しない調製相関の下で、一般の正半定値相関行列に対する有限基底 Born 型則を得る。滑らかな比較器、粒子検出、完全周期は未完成である。

## 4.1 測定基底と出力作用

$L$ 個の位相担体モードを $b\in\mathbb C^L$ とする。測定する有限直交基底をユニタリ行列 $U$ で表し、測定前の正準モード混合を

```math
b'
=
Ub
```

とする。複素ユニタリ変換は実正準変数 $(Q,P)$ 上の直交正準変換に対応する。出力モード $k$ の作用と全位相作用を

```math
I_k
=
\mathcal J_0
\left|b'_k\right|^2,
\qquad
I_{\rm ph}
=
\sum_{k=1}^L I_k
=
\mathcal J_0b^\dagger b
```

とする。$U$ は全作用を保存する。以下、$I_{\rm ph}>0$ がほとんど確実に成立する条件付き集団を扱う。

$I_k$ は各試行に実在する正準作用である。装置は集団量 $C$ を単一試行の Hamiltonian へ代入せず、各試行の $I_k$ だけを読み出す。

## 4.2 固定作用の正準選択器

補助振動子の作用角変数を

```math
\left(
J_{\rm sel},
\vartheta_{\rm sel}
\right),
\qquad
J_{\rm sel}=J_*>0
```

とする。選択器角に必要なのは周辺一様性ではなく、位相担体、測定基底、調製条件の下での条件付き一様性である。具体的に、

```math
\mu_*
\left(
d\vartheta_{\rm sel}
\mid
b,U,\mathcal P,M=\mathsf{basis}
\right)
=
\frac{d\vartheta_{\rm sel}}{2\pi}
```

を仮定する。$\vartheta_{\rm sel}$ の周辺分布だけが一様でも、作用分配と相関していれば以下の区間則は一般に成立しない。

選択変数を

```math
u
=
\frac{\vartheta_{\rm sel}}{2\pi}
I_{\rm ph},
\qquad
0\leq u<I_{\rm ph}
```

とする。角度の切断点 $0=2\pi$ は零測度境界であり、有限幅実装では比較誤差として扱う。

## 4.3 累積作用区間と唯一結果

累積作用を

```math
S_0=0,
\qquad
S_k
=
\sum_{j=1}^k I_j
```

とする。結果 $k$ の事象を

```math
E_k^U
=
\left\{
S_{k-1}\leq u<S_k
\right\}
```

と定める。$S_L=I_{\rm ph}$ なので、境界を除いて事象 $E_k^U$ は互いに素であり、全標本を覆う。従って、各試行はちょうど1つの結果を持つ。

この結果は粒子が入口 $k$ を最初に通過した事象ではない。結果レジスターが位相担体の出力モード $k$ を記録した事象である。旧位置作用殻の共通入口流束、全入口の排他的作用転送、2モード殻容量は本定理の仮定から外れる。

## 4.4 主定理2の一般形

<!-- theorem-start:theorem -->
**定理（正準作用選択器による有限基底標本化）**
次を仮定する。

1. $I_{\rm ph}>0$ がほとんど確実に成立する。
2. 測定前の正準混合 $U$ が全作用を保存する。
3. 選択器角が $(b,U,\mathcal P)$ の下で条件付き一様である。
4. 累積作用区間が排他的に比較され、各試行で1つの結果だけが記録される。
5. 比較失敗、記録失敗、再帰失敗を結果に応じて捨てない。

このとき各試行の条件付き結果確率は

```math
P(k\mid b,U)
=
\frac{I_k}{I_{\rm ph}}
=
\frac{
\left|\left(Ub\right)_k\right|^2
}{
b^\dagger b
}
```

であり、母測度で平均した頻度は

```math
P(k\mid U,\mathcal P)
=
\mathbb E_{\mu_*}
\left[
\frac{I_k}{I_{\rm ph}}
\middle|
U,\mathcal P,M=\mathsf{basis}
\right]
```

である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
$(b,U)$ を固定すると、$u$ は区間 $[0,I_{\rm ph})$ 上で一様である。$E_k^U$ の区間長は $S_k-S_{k-1}=I_k$ なので、条件付き確率は $I_k/I_{\rm ph}$ である。条件付き期待値を取ると第2式を得る。
<!-- theorem-end:proof -->

周期写像が $\mu_*$ に関して不変かつエルゴード的であるという第1章の仮定により、同じ装置を繰り返した結果 $k$ の長期相対頻度は、この母測度確率へ収束する。

## 4.5 固定全作用と Born 型則

測定基底 $U$ の下の相関行列を

```math
C_U
=
\mathbb E_{\mu_*}
\left[
bb^\dagger
\mid
U,\mathcal P,M=\mathsf{basis}
\right]
```

とする。全位相作用が条件付き集団で固定され、

```math
I_{\rm ph}=I_0>0
```

なら、

```math
\operatorname{tr}C_U
=
\frac{I_0}{\mathcal J_0}
```

である。

<!-- theorem-start:corollary -->
**系（固定作用下の有限基底 Born 型則）**
主定理2の条件に加えて $I_{\rm ph}=I_0$ を仮定すると、

```math
P(k\mid U,\mathcal P)
=
\frac{
\left(
UC_UU^\dagger
\right)_{kk}
}{
\operatorname{tr}C_U
}
```

が成立する。
<!-- theorem-end:corollary -->

階数1は仮定していない。従って、純度が1未満の高階数相関行列も同じ選択器で扱える。

## 4.6 全作用変動の共分散補正

一般には比の平均と平均の比は一致しない。正規化作用分配を

```math
r_k
=
\frac{I_k}{I_{\rm ph}}
```

とすると、主定理2は $P_k=\mathbb E[r_k]$ を与える。一方、

```math
\frac{
\mathbb E[I_k]
}{
\mathbb E[I_{\rm ph}]
}
=
\mathbb E[r_k]
+
\frac{
\operatorname{Cov}
\left(
I_{\rm ph},r_k
\right)
}{
\mathbb E[I_{\rm ph}]
}
```

なので、

```math
P_k
-
\frac{
\left(
UC_UU^\dagger
\right)_{kk}
}{
\operatorname{tr}C_U
}
=
-
\frac{
\operatorname{Cov}
\left(
I_{\rm ph},r_k
\right)
}{
\mathbb E[I_{\rm ph}]
}
```

である。従って、Born 型の平均比と一致する十分条件は次のいずれかである。

1. $I_{\rm ph}$ が試行ごとに固定される。
2. $I_{\rm ph}$ と $r_k$ が無相関である。

全作用変動を許すとき、この共分散項を消えたものとして扱わない。

## 4.7 任意有限基底と調製独立性

同じ状態 $C$ を異なる基底 $U$ で測ったと主張するには、単粒子側の調製相関が基底選択に依存しないことが必要である。すなわち、

```math
C_U=C
```

を要求する。固定作用下では

```math
P(k\mid U,\mathcal P)
=
\frac{
\left(
UCU^\dagger
\right)_{kk}
}{
\operatorname{tr}C
}
```

となる。これは有限次元の任意の直交基底に対する Born 型則である。

Bell側では設定条件付き母測度を許すが、その測定設定依存性を単粒子側へ無条件に持ち込まない。$C_U\neq C$ なら、上式は同じ状態の基底変更でなく、基底に応じて異なる条件付き集団を測っている。

## 4.8 空間セル基底

$U=I$ とし、モード $i$ が体積 $\Delta V$ の空間セルに対応するとする。第2章の規格化により、固定作用下では

```math
P_i
=
\frac{C_{ii}}{\operatorname{tr}C}
```

である。階数1なら

```math
C
=
\Lambda\chi\chi^\dagger,
\qquad
\psi_i
=
\frac{\chi_i}{\sqrt{\Delta V}}
```

なので、

```math
P_i
=
\left|\chi_i\right|^2
=
\left|\psi_i\right|^2
\Delta V
```

となる。

ただし、これは位相担体の空間セル基底を標本化する式である。粒子座標 $X$ がセル $i$ の局所検出器を作動させたこと、粒子と選択モードが同期すること、粒子が連続軌道を持つことは別の導出を要する。従って本稿では「粒子位置 Born 則」ではなく「空間セル基底の Born 型標本化」と呼ぶ。

## 4.9 可逆装置の候補

理想装置は次の順序で働く。

1. 正準回路 $U$ が測定基底へモードを混合する。
2. 各 $I_k$ を累積作用レジスターへ可逆に加える。
3. 選択器角から $u$ を計算する。
4. $u-S_k$ の符号変化を滑らかな有限幅比較器で検出する。
5. 最初の1結果だけをラッチへ記録する。
6. 結果を空の外部記録へ可逆にコピーする。
7. 比較、累積加算、基底混合を逆計算する。
8. 消せない結果情報と不要情報を外部自由度へ移す。

正準加算と比較器の候補 Hamiltonian は付録Cに示す。直列走査の相互作用窓は $O(L)$ 個であり、二分木比較では深さを $O(\log L)$ にできるが、追加レジスターが必要である。本稿は構成要素を示すが、全てを1つの滑らかな自律 Hamiltonian と不変母測度へ統合していない。

## 4.10 条件付き一様性と比較幅の誤差

選択器角の条件付き分布と一様分布の全変動距離を

```math
\varepsilon_{\rm sel}
=
\mathbb E
\left[
d_{\rm TV}
\left(
\mu_*
\left(
d\vartheta_{\rm sel}\mid b,U,\mathcal P,M=\mathsf{basis}
\right),
\frac{d\vartheta_{\rm sel}}{2\pi}
\right)
\right]
```

とする。このとき各結果確率の一様選択器からの偏差は $\varepsilon_{\rm sel}$ 以下である。

比較境界の半幅を $w>0$ とし、

```math
\varepsilon_{\rm cmp}(w)
=
\mu_*
\left(
\min_k
\left|u-S_k\right|
\leq w
\middle|
\mathcal P,M=\mathsf{basis}
\right)
```

とする。境界近傍だけで理想結果と有限幅結果が異なる装置なら、比較器による全変動誤差は $\varepsilon_{\rm cmp}(w)$ で抑えられる。理想境界が零測度で、条件付き密度が有界なら $w\to0$ でこの誤差は零へ近づく。

## 4.11 主張の範囲

本章で得たものは次である。

1. 各試行の作用分配から1結果を排他的に選ぶ厳密な区間則。
2. 高階数を含む一般の正半定値相関行列への拡張。
3. 固定作用下の任意有限直交基底 Born 型則。
4. 全作用変動に対する厳密な共分散補正。
5. 条件付き一様性と有限比較幅の誤差指標。

一方、次は示していない。

1. 選択器角の条件付き一様性を具体的な周期写像から導くこと。
2. 累積、比較、ラッチ、記録、逆計算を統合した完成 Hamiltonian。
3. 連続スペクトルと無限次元測定。
4. 位相担体モードの選択と粒子の局所位置検出の同一性。
5. 粒子の連続軌道。
