@number: 0
@chapter: 概要
@title: 概要

本論文は、有限自由度の古典 Hamiltonian 系を基礎とし、対象部分を外部との微小なエネルギー交換を伴う弱開放系として扱う。目的は、量子力学を構成の入力に置かず、量子力学に特徴的な力学と確率構造が縮約された有効理論として現れ得るかを検証することである。

現行構成は、有限2成分誘導場を共有する3つの縮約経路からなる。

1. 位相接続経路は、粒子と2成分場を接続で結合し、coherent縮約多様体上で Nelson--Madelung 作用と局所 Schrödinger 型方程式を与える。
2. 運動量結合経路は、有限誘導場の速度揺らぎから配置拡散と実在的な前後 Markov 過程へ進む候補を与える。
3. 境界作用殻経路は、位置入口の Born 型重みと Bell 型共同統計を、Liouville 流束と作用殻体積から与える。

3経路は同じ完成 Hamiltonian から同時に導出済みではない。位相活性場、配置拡散浴、測定器を固定された別部分空間へ置き、交差作用を誤差として管理する構造化誘導場アーキテクチャとして整理する。

有限セル $i$ の活性場を

```math
\boldsymbol\Phi_i
=
r_i
\begin{pmatrix}
\cos\theta_i\\
\sin\theta_i
\end{pmatrix},
\qquad
j_i
=
\Phi_{1,i}\Pi_{2,i}
-
\Phi_{2,i}\Pi_{1,i}
```

とする。正準1形式は有限次元で厳密に

```math
\sum_i
\boldsymbol\Pi_i\cdot d\boldsymbol\Phi_i
=
\sum_i
\left(
p_{r,i}\,dr_i+j_i\,d\theta_i
\right)
```

となる。規格化

```math
\sum_i r_i^2\Delta V=1
```

と固定全位相作用

```math
\mathcal J_\phi
=
\sum_i j_i\Delta V
```

の下で、回転エネルギーは

```math
E_{\rm rot}
=
\frac{\mathcal J_\phi^2}{2I}
+
\sum_i
\frac{
\left(
j_i-\mathcal J_\phi r_i^2
\right)^2
}{
2Ir_i^2
}
\Delta V
```

と分解できる。従ってエネルギー最小配置は

```math
j_i
=
\mathcal J_\phi r_i^2
```

である。これは固定作用sector内の厳密な最小化結果であり、閉鎖 Hamiltonian 流がこの配置へ吸引されることを意味しない。

連続表示で正則化した位相接続を

```math
\mathbf a_\varepsilon
=
\frac{
\Phi_1\nabla\Phi_2
-
\Phi_2\nabla\Phi_1
}{
|\boldsymbol\Phi|^2+\varepsilon^2
}
```

とし、粒子 Hamiltonian を

```math
H_{\rm p}
=
\frac{
\left|
P-\mathcal J_\phi\mathbf a_\varepsilon(X)
\right|^2
}{
2m
}
+
V(X)
```

とする。coherent集中、局所作用分配、密度同期、単流束化、動径断熱化、節から離れた極限の下で、場の正準項と粒子の接続項は

```math
\mathcal J_\phi
\int
\rho
\left(
\partial_t\theta
+
v\cdot\nabla\theta
\right)
\,dx
```

を与える。位相を

```math
S=-\mathcal J_\phi\theta
```

と定めると、縮約作用は

```math
\mathcal A_{\rm red}
=
\int
\left[
\frac m2\rho|v|^2
-
\rho V
-
\rho
\left(
\partial_tS+v\cdot\nabla S
\right)
-
\kappa
\left|
\nabla\sqrt\rho
\right|^2
\right]
\,dx\,dt.
```

係数整合

```math
\kappa
=
\frac{\mathcal J_\phi^2}{2m}
```

の下で、これは Nelson--Madelung 作用に一致する。変分により

```math
\partial_t\rho
+
\nabla\cdot(\rho v)
=
0,
\qquad
mv=\nabla S,
```

```math
\partial_tS
+
\frac{|\nabla S|^2}{2m}
+
V
-
\frac{\mathcal J_\phi^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=
0
```

を得る。従って

```math
\hbar_{\rm eff}
=
|\mathcal J_\phi|,
\qquad
\psi
=
\sqrt\rho
\exp
\left(
\frac{iS}{\hbar_{\rm eff}}
\right)
```

は節を避ける局所領域で Schrödinger 型方程式を満たす。

単価な2成分場では、

```math
\oint
\nabla\theta\cdot d\ell
=
2\pi n
```

であるため、

```math
\oint
\nabla S\cdot d\ell
=
-2\pi\mathcal J_\phi n
```

を得る。これは条件付き循環量子化である。節の生成・消滅、正則化極限、全ての物理的流れが単価な場から生じることは未解決であり、Wallstrom 問題を全面的に解いたとは主張しない。

密度同期の入口重みは2モード作用殻から得る。局所作用を

```math
A_i
=
A_{\rm tot}r_i^2\Delta V
```

とし、選択された活性モードと1つの共有明反応座標が

```math
K_i+I=A_i
```

を分配すると、2モード殻容量は

```math
\Omega_2(A_i)
=
(2\pi)^2A_i
```

である。排他的な入口チャンネルの法線速度、障壁、coarea Jacobian、spectator因子が共通なら、正方向 Liouville 流束は $A_i$ に比例し、

```math
P_i
=
r_i^2\Delta V,
\qquad
\rho_{{\rm in},i}
=
r_i^2
```

を得る。これは位置入口分布に限定された Born 型結果であり、任意基底の一般測定則ではない。

位相変分から

```math
\partial_tj
+
\mathcal J_\phi
\nabla\cdot(\rho v)
=
0
```

を得る。coherent最小作用多様体で $j=\mathcal J_\phi r^2$ なら、

```math
\partial_t
\left(
r^2-\rho
\right)
=
0
```

となる。入口で作られた同期差は理想多様体上で保存されるが、ずれた状態を同期多様体へ戻す吸引は示していない。

運動量結合経路では、有限誘導場を正確に消去し、自由速度揺らぎと反作用記憶を分ける。配置 Markov 拡散が得られた有効モデル内部では

```math
u
=
\frac{b_+-b_-}{2}
=
\nu\nabla\log\rho
```

と Fisher 項が厳密に従う。位相接続経路と同じ有効理論を表すためには

```math
\nu_{\rm bath}
=
\frac{|\mathcal J_\phi|}{2m}
```

が必要である。この係数一致と、両経路の同時実現は未解決である。

Bell 側では、3モード共通作用殻の残余ファイバー体積から

```math
P(A,B\mid a,b)
=
\frac14
\left[
1
-
V_{\rm eff}
AB\cos\Delta_{ab}
\right]
```

を得る。Bell の前提違反は、設定依存の境界適合による測定設定独立性の破れにある。対称準備では一側周辺は $1/2$ である。

本改訂の中心的な前進は、Schrödinger 型動力学、位置の Born 型入口密度、循環量子化候補を同じ2成分場と作用殻幾何の中へ具体化したことである。最大の未解決問題は、2モード作用殻を偏りなく準備し、標本化後に活性場を coherent 部分空間へ再埋め込み、明反応座標、記録、garbage自由度を事後選別なしで次試行へ復元する有限 Hamiltonian 周期の構成である。
