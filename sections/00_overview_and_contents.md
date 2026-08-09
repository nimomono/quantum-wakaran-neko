@number: 0
@chapter: 概要
@title: 概要

本論文は、有限自由度の古典 Hamiltonian 系を基礎とし、量子力学に特徴的な時間発展と確率構造が、どの仮定と誤差の下で有効理論として現れ得るかを検証する。力学、測定、Bell 統計を1つの完成理論として先取りせず、ミクロ振動子、有効包絡、局所正準測定装置、二側履歴測度を分離する。

第1の主結果は、位置だけで局所結合した有限実古典振動子網からの Schrödinger 型包絡である。ミクロ Hamiltonian を

```math
H_{\rm micro}
=
\frac{1}{2M_{\rm osc}}p^{\mathsf T}p
+
\frac12q^{\mathsf T}
\left(
M_{\rm osc}\omega_0^2I+A
\right)q
```

とする。$A=D_\delta+L_\kappa$ は局所離調とばね Laplacian からなる実対称疎行列である。局所正準振幅を搬送周波数で回して作る包絡 $b$ は、厳密に

```math
i\mathcal J_0\dot b
=
h_Lb
+
h_Le^{2i\omega_0t}\overline b
```

を満たす。第2項は反回転項であり、位置結合だけの模型では厳密に消えない。

一方、行列平方根

```math
\Omega
=
\left(
\omega_0^2I
+
\frac{A}{M_{\rm osc}}
\right)^{1/2}
```

を使う正常モード包絡 $\widetilde b$ は

```math
i\mathcal J_0\dot{\widetilde b}
=
h_{\rm ex}\widetilde b,
\qquad
h_{\rm ex}
=
\mathcal J_0
\left(
\Omega-\omega_0I
\right)
```

に厳密に従い、作用を保存する。ただし $\widetilde b$ は一般に非局所である。

古典係数を調整して

```math
h_L
=
\frac{\mathcal J_0^2}{2m}L_G
+
V_L
```

を目標演算子とし、

```math
\eta
=
\frac{2\left\|h_L\right\|}
{\mathcal J_0\omega_0}
<1
```

とすると、

```math
\left\|
h_{\rm ex}-h_L
\right\|
\leq
\frac{
\left\|h_L\right\|^2
}{
2\mathcal J_0\omega_0
\left(1-\eta\right)^{3/2}
}
```

を得る。自然時間 $T=O(\mathcal J_0/\|h_L\|)$ では、厳密ミクロ局所包絡と目標 Schrödinger 型解の差は $O(\eta)$ である。局所作用の変動も $O(\eta)$ で抑えられる。従ってQ1は、有限個の実振動子、実対称時間非依存演算子、弱結合・弱離調・有限時間という限定で達成と判定する。

第2の主結果は、Q1の包絡誤差を有限基底測定分布へ接続することである。測定時刻の実際の局所包絡を $\widehat b_{\rm mic}$、目標有効状態を $\chi_L$ とし、任意の有限基底変換 $W$ について

```math
p_k^{\rm mic}
=
\left|
\left(W\widehat b_{\rm mic}\right)_k
\right|^2,
\qquad
p_k^L
=
\left|
\left(W\chi_L\right)_k
\right|^2
```

とする。このとき

```math
D_{\rm TV}
\left(
p^{\rm mic},p^L
\right)
\leq
\sqrt{
1-
\left|
\left\langle
\widehat b_{\rm mic},
\chi_L
\right\rangle
\right|^2
}
```

が成立する。これにより、Q1の状態方向誤差はQ2の Born 型分布誤差へ伝播する。

固定された純粋準備 $\chi\in\mathbb C^L$ と有限測定基底 $\{|u_k\rangle\}$ については、任意の基底変換を局所位相回転と隣接 $QQ+PP$ 交換の有限列へ分解する。作用読出し、累積剪断、双曲型増幅、滑らかな比較、隣接テンプレート経路、正準 SWAP、内部記録、逆計算を $3L+4$ 正準対の自律 Hamiltonian 周期として構成する。周期末の選択器角が

```math
\vartheta
\longmapsto
\vartheta+2\pi\alpha
\pmod{2\pi},
\qquad
\alpha\notin\mathbb Q
```

と進むため、Haar 測度は不変かつ一意エルゴード的であり、各結果の長期頻度は

```math
\lim_{N\to\infty}
\frac{N_k(N)}{N}
=
\left|
\langle u_k|\chi\rangle
\right|^2
```

になる。結果集合を $\{1,\ldots,L,\varnothing\}$ とし、比較境界近傍を正式な無反応結果に含める。安全な結果 $k$ では測定後信号が厳密に $|u_k\rangle$ となり、無反応領域でも内部逆計算は厳密である。無反応込みの長期分布と理想 Born 型分布の全変動距離は

```math
D_{\rm TV}
\leq
2(L-1)
\frac{Xe^{-\Lambda}}{I_{\rm ph}}
+
\varepsilon_{\rm cut}
```

で抑えられるため、任意精度へ近づけられる。これによりQ2は、固定純粋準備、固定有限基底、有限次元の範囲で達成と判定する。無理数回転は混合的でないため、独立同分布または二項分布型有限標本揺らぎは得ない。

第3の結果は Bell 型二側履歴模型である。左右担体の反対称な集団交差相関 $\Xi_0$ から、4成分重み

```math
w_{AB}^{xy}
=
\frac14
\left[
1-AB\cos\Delta_{xy}
\right]
```

が代数的に得られる。これは有限 $L=4$ の作用重みと同じ線形代数構造を持つが、$\Xi_0$ は集団量であり、単一試行の正準変数ではない。

左右の局所結果角と共通未来角を独立 Haar 角とし、局所半円分割から4結果の基準密度 $1/4$ を得る。記録済み結果に対応する余弦区間へ未来角が入る事象を $G$ とし、

```math
d\mu_{\rm B}
=
4\mathbf1_G
\,d\nu_{\rm B}^0
```

と定めれば、余弦共同確率、非信号周辺、標準設定での CHSH 値 $2\sqrt2$、設定分布保存を得る。完全ミクロ履歴の分布は設定に依存するので、Bell の前提違反は測定設定独立性にある。

ただし、余弦区間は反対称集団源と設定角から指定する境界プログラムである。単一試行の源変数から同じ区間多重度を生成する有限 Hamiltonian、二側支持 $G$ の物理的必然性、完全境界流束測度の結果非依存因子化は未導出である。Bell 結果はQ1・Q2と同じ完成度の定理ではなく、明示した二側支持条件に依存する条件付き結果である。

相関行列 $C=\mathbb E[dd^\dagger]$ とその交換子発展、階数1条件、高階数作用公式は補助統計理論として付録へ移す。相関行列をミクロ力学の基礎状態とはしない。ミクロ振動子、固定測定周期、Bell 二側履歴で使う測度を区別し、全プログラム共通の統一母測度 $\mu_*$ は将来目標に残す。

本文は7章から成る。第1章で記述層、測度、主結果の確立度を示す。第2章で局所位置結合振動子網、第3章で Schrödinger 型包絡と有限時間誤差、第4章で有限基底 Born 型測定とQ1からQ2への誤差伝播、第5章で Bell 型二側履歴模型、第6章で反復周期、性能、資源、第7章で反証条件と未完成ベンチマークを扱う。正常モード正準変換、相関行列と作用区間、測定装置、Bell 境界模型の詳細は付録へ置く。
