@number: 0
@chapter: 概要
@title: 概要

本論文は、有限自由度の古典Hamiltonian 系を基礎とし、量子力学に特徴的な可逆力学、測定操作、空間包絡、Bell 型統計が、どの仮定と誤差の下で現れ得るかを検証する。単一量子ビット型装置、空間振動子網、一般有限基底装置、Bell 二側履歴を別模型として明示し、未完成の統一模型を先取りしない。

第1の主結果は、2モード正準担体M38によるQ1-1からQ1-4の構成である。信号を

```math
b_j
=
\frac{Q_j+iP_j}{\sqrt{2\mathcal J_0}},
\qquad
I_{\rm ph}
=
\mathcal J_0b^\dagger b
=
\mathcal J_0
```

とする。共通位相 $b\mapsto e^{i\gamma}b$ に不変な操作・測定代数へ縮約すると、

```math
S^3/U(1)
\simeq
\mathbb{CP}^1
\simeq
S^2
```

を得る。Bloch ベクトル $\boldsymbol r=b^\dagger\boldsymbol\sigma b$ は

```math
\{r_i,r_j\}
=
\frac{2}{\mathcal J_0}
\epsilon_{ijk}r_k
```

を満たす。局所位相回転と $QQ+PP$ 交換の有限列は同じ2モード担体上で任意の $SU(2)$ を厳密に生成する。

駆動作用・角変数を加えた時間非依存Hamiltonian は、回転座標で

```math
i\dot c
=
\frac12
\left(
\Delta\sigma_z+\Omega\sigma_x
\right)c
```

となる。従って

```math
P_{1\to2}(t)
=
\frac{\Omega^2}{\Omega^2+\Delta^2}
\sin^2
\left(
\frac{\sqrt{\Omega^2+\Delta^2}}{2}t
\right)
```

が厳密に得られる。Q1-1は、Bloch 球、共通位相不変性、任意の $SU(2)$、Rabi 振動について達成と判定する。

Q1-2では、任意の Bloch 軸 $\boldsymbol n$ の2結果作用比

```math
p_s(\boldsymbol n)
=
\frac{1+s\boldsymbol n\cdot\boldsymbol r}{2}
```

をM35型の滑らかな作用選択器へ渡す。安全結果 $s$ では測定後信号が厳密に固有状態 $|\boldsymbol n,s\rangle$ となる。滑らかな有限時間Hamiltonian 流は連結入力領域全体を相異なる2固有状態だけへ写せないため、比較境界近傍を正式な無反応結果とする。無反応率は有限増幅で任意に小さくできる。

2つの独立選択器角を用い、周期末に2次元トーラス上の無理数平行移動を行う。同軸再測定では反対符号の安全結果が生じず、異軸 $\boldsymbol n,\boldsymbol m$ の理想共同分布は

```math
P(s,t)
=
\frac{1+s\boldsymbol n\cdot\boldsymbol r}{2}
\frac{1+st\boldsymbol n\cdot\boldsymbol m}{2}
```

となる。有限幅分布との全変動距離は2段の無反応率の和以下である。Q1-2は、無反応を除外せず、制御された任意精度で達成と判定する。

Q1-3では、滑らかな比較ポインターを外部記録セルへ正準剪断でコピーした後、第2測定、第1測定の順で内部逆計算する。装置は準備点へ戻り、記録は外部セルに残る。装置偏差と外部空モードの交換角を $\phi$ とすると、

```math
\delta a^+
=
\cos\phi\,\delta a^-
+
\sin\phi\,\eta
```

である。完全交換または部分収縮により、旧装置状態は使用済み外部セルへ移る。有限個の能動自由度、永久記録セル流、reset セル流、局所作用・角時計を合わせ、次周期の準備集合へ任意精度で戻る弱開放完全周期を構成する。有限 $K$ 周期は有限閉鎖Hamiltonian 系へ埋め込めるが、無期限運転は外部セル供給を要する。Q1-3も制御された任意精度で達成と判定する。

Q1-4では、1個の測定コアと有限長の循環メモリー／reset セル列を使い、継続するRabi 駆動下で $N_{\rm Z}$ 回の $z$ 測定を行う。各区間の反転作用比を $q_j$ とすると、全履歴分布、一度も反転しない確率、最終正占有率は

```math
\pi_{N_{\rm Z}}
=
\prod_{j=1}^{N_{\rm Z}}
\left[
(1-q_j)\mathbf1_{s_j=s_{j-1}}
+
q_j\mathbf1_{s_j=-s_{j-1}}
\right],
```

```math
S_{N_{\rm Z}}
=
\prod_{j=1}^{N_{\rm Z}}(1-q_j),
\qquad
F_{N_{\rm Z}}
=
\frac12
\left[
1+
\prod_{j=1}^{N_{\rm Z}}(1-2q_j)
\right]
```

となる。等間隔 $\tau$ の有効反転率は

```math
\Gamma_{\rm Z}(\tau)
=
\frac{\Omega^2}{4}\tau
+
O(\tau^3)
```

であり、短時間域で測定間隔とともに低下する。有限幅測定中もRabi 項を非零に保ち、理想履歴則からの全変動距離を各段誤差の和で抑える。固定有限 $N_{\rm Z}$ ごとに任意精度で構成できるため、Q1-4を有限Zeno抑制の範囲で達成と判定する。$N_{\rm Z}\to\infty$ の完全凍結は主張しない。

第2の主結果は、別模型M37による空間Schrödinger 型包絡である。位置だけで局所結合した有限実古典振動子網を

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

とする。局所回転包絡は反回転項を含む厳密式

```math
i\mathcal J_0\dot b
=
h_Lb
+
h_Le^{2i\omega_0t}\overline b
```

を満たす。行列平方根を使う正常モード包絡は厳密だが一般に非局所である。弱結合量

```math
\eta
=
\frac{2\|h_L\|}{\mathcal J_0\omega_0}
<1
```

の下で、自然時間における局所包絡と目標Schrödinger 型解の差を $O(\eta)$ で抑える。Q3-1は、有限実振動子、実対称時間非依存演算子、弱結合・有限時間の範囲で達成と判定する。

第3の結果は、M35による一般有限 $L$ の固定基底測定である。任意有限基底変換を隣接2モード回路へ分解し、作用読出し、累積比較、滑らかな無反応領域、測定後状態、内部逆計算、無理数回転を $3L+4$ 正準対で構成する。長期分布と理想Born 型分布の距離は

```math
D_{\rm TV}
\leq
2(L-1)
\frac{Xe^{-\Lambda}}{I_{\rm ph}}
+
\varepsilon_{\rm cut}
```

である。一般有限 $L$ の外部記録、弱開放 reset、複数段測定、長距離時計配線は未完成である。一般有限次元への拡張は独立した長期目標とはせず、M35の適用範囲と一般化課題として扱う。

第4の結果はBell 型二側履歴模型M36である。反対称な左右集団交差相関から

```math
w_{AB}^{xy}
=
\frac14
\left[
1-AB\cos\Delta_{xy}
\right]
```

が代数的に得られる。独立局所Haar 角の基準測度を、余弦区間への整合事象 $G$ で条件付けると、余弦共同確率、非信号周辺、標準設定でのCHSH値 $2\sqrt2$、設定分布保存を得る。完全履歴測度は設定依存なので、Bell の前提違反は測定設定独立性にある。

ただし、余弦区間を単一試行の源変数から生成する有限Hamiltonian 、整合支持 $G$ の物理的必然性、完全境界流束測度の結果非依存因子化は未導出である。Q2-2は条件付き模型として部分達成である。

本文は8章から成る。第1章で記述層、測度、主結果の確立度を示す。第2章と第3章でM37の空間包絡、第4章でM38のQ1-1からQ1-4、第5章でM35の一般有限基底測定、第6章でBell 二側履歴、第7章で誤差と資源、第8章で反証条件、達成範囲、未完成課題を扱う。正常モード変換、作用区間、一般測定装置、Bell 境界、2モード完全周期、有限Zeno周期の詳細は付録A--Fへ置く。
