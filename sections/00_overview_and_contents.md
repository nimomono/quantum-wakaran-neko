@number: 0
@chapter: 概要
@title: 構造化誘導場を持つ弱開放古典 Hamiltonian 系の二側縮約：運動量結合による配置拡散と境界作用殻 Bell 型統計
@status: 運動量結合した有限誘導場の正定値条件、時間反転対称性、正確な消去、二側配置拡散内部の Fisher 恒等式、境界作用殻幾何は厳密結果である。配置拡散極限、配置変数の Markov 性、時間対称 Newton 則、同じ誘導場からの全殻拡散は予想・未解決である。

本論文は、有限自由度の古典 Hamiltonian 系を基礎とし、対象部分を外部との微小なエネルギー交換を伴う弱開放系として扱う。中心となる有限部分は、粒子または測定対象、構造化誘導場、測定器、記録器、境界3モードからなる。外部自由度と仕事源まで含む拡大全系を

```math
H_{\rm all}
=
H_{\rm fin}
+
H_{\rm ext}
+
\varepsilon_{\rm ext}H_{\rm link}
+
H_{\rm work}
```

と書く。全系は Hamiltonian とし、有限部分の収支だけが

```math
\dot E_{\rm fin}
=
J_{\rm in}
-
J_{\rm out}
+
P_{\rm ctrl}
```

となる。常時の弱い外部交換は、欠陥成分の除去、有限浴の再帰抑制、記録安定化、非零作用半径の維持に使う。Fisher 項や作用殻の方向一様性を外部漏れから直接仮定しない。

現行モデルの共通部分は、時間に依存しない明・暗モード分解を持つ構造化誘導場である。第I部では粒子と誘導場を運動量で結合し、配置速度揺らぎへ縮約する。第II部では同じ誘導場へ装置の座標結合を加え、2粒子、左右測定器、共通境界3モードの履歴測度へ縮約する。2種類の結合は役割が異なる。

第I部の有限 Hamiltonian を

```math
H_N^{\rm fin}
=
\frac12
\begin{pmatrix}
P\\
\Pi
\end{pmatrix}^{\mathsf T}
\begin{pmatrix}
m^{-1}I_d & C_N\\
C_N^{\mathsf T} & M_N^{-1}
\end{pmatrix}
\begin{pmatrix}
P\\
\Pi
\end{pmatrix}
+
V(X)
+
\frac12Q^{\mathsf T}K_NQ
+
H_N^{\rm nl}
```

とする。運動量2次形式の正定値条件は

```math
M_N^{-1}
-
mC_N^{\mathsf T}C_N
>
0
```

である。線形核の Hamilton 方程式は

```math
\dot X
=
\frac Pm
+
C_N\Pi,
\qquad
\dot P
=
-\nabla V(X)
```

を含む。従って誘導場速度

```math
Y_N
=
C_N\Pi
```

は配置流束へ直接入る。正準運動量 $P$ と機械的運動量 $m\dot X$ は一致しない。

質量規格化した線形誘導場を正確に消去すると、

```math
Y_N(t)
=
Y_N^{\rm free}(t)
-
\int_0^t
C_N\Omega_N
\sin
\left[
\Omega_N(t-s)
\right]
C_N^{\mathsf T}P(s)
\,\mathrm ds
```

を得る。第1項は初期場に由来する自由速度揺らぎ、第2項は粒子から場への反作用による速度記憶項である。有限浴の相関は余弦関数の有限和なので、厳密な OU 相関や無限時間の Brown 運動ではない。多数モード、短記憶、弱い外部交換を用い、

```math
\tau_{\rm corr}
\ll
T_{\rm obs}
\ll
T_{\rm rec}
```

という再帰前の窓で配置変位の拡散極限を調べる。

最初の有効候補は、配置雑音を持つ位相空間過程

```math
\mathrm dX_t
=
\frac{P_t}{m}
\,\mathrm dt
+
\sqrt{2\nu}
\,\mathrm dW_t,
\qquad
\mathrm dP_t
=
-\nabla V(X_t)
\,\mathrm dt
```

である。ただし $(X,P)$ が Markov でも、$X$ だけの射影は一般に Markov ではない。配置変数だけの前進・後退 Markov 拡散と共通拡散係数 $\nu$ を得ることは追加の縮約課題である。

この配置 Markov 拡散が得られた有効モデル内部では、現在速度 $v$ と浸透速度 $u$ は

```math
v
=
\frac{b_++b_-}{2},
\qquad
u
=
\frac{b_+-b_-}{2}
=
\nu\nabla\log\rho
```

を満たす。従って

```math
\frac m2
\int
\rho|u|^2
\,\mathrm dx
=
\frac{m\nu^2}{2}
\int
\frac{|\nabla\rho|^2}{\rho}
\,\mathrm dx
```

となり、Fisher 項は二側配置拡散の運動学から直接現れる。量子ポテンシャルに対応する項は

```math
Q[\rho]
=
-2m\nu^2
\frac{\Delta\sqrt\rho}{\sqrt\rho},
\qquad
\hbar_{\rm eff}
=
2m\nu
```

である。

ただし、配置拡散だけから時間対称 Newton 則

```math
ma_{\rm ts}
=
-\nabla V
```

は従わない。時間対称 Green 応答、反作用記憶、条件付き変分からこの動力学へ進む部分は独立した未解決問題である。従って旧稿の Fisher 力密度閉鎖は中心課題から外れるが、問題が全て解決したわけではない。

補助結果として、有限 Fourier–Gauss 型経路法則の繰り込み済み粗視化作用について

```math
\left\|
\mathcal A_{N,h}^{R,U}
-
\mathcal A_{\rm GM}^{R,U}
\right\|_{C^1(K)}
\leq
C_K
\left(
\frac hT
+
\frac{T^2}{Nh^2}
\right)
```

を保つ。これは二側配置拡散が得られた後の作用表示を制御する厳密な補助結果であり、ミクロな配置拡散極限や時間対称 Newton 則の証明ではない。

第II部では、同じ構造化誘導場の固定明部分空間が、$\operatorname{Ran}C_N^{\mathsf T}$ に加えて左右の装置結合方向と共通境界結合方向を含む。局所測定窓の左右交差応答には、座標–座標核だけでなく運動量–座標混合核も含め、全応答比 $\varepsilon_{\rm loc}\ll1$ を要求する。

境界3モードの作用を $J_+,J_s,J_r$ とし、共通総作用殻を

```math
J_+
+
J_s
+
J_r
=
C_0
```

とする。縮約された殻接方向混合が非退化な $U(3)$ 等方拡散なら、共通殻上の正規化 Liouville 測度が一意な定常分布になる。この縮約方程式内部の一意性は厳密だが、同じ誘導場からその生成子を導くことは未解決である。

局所記録後の2つの実2次元伝達ベクトルから、固定した和・差基底により

```math
I_+^{AB}
=
I_0
\left[
1
+
ABV\cos\Delta_{ab}
\right],
```

```math
I_-^{AB}
=
I_0
\left[
1
-
ABV\cos\Delta_{ab}
\right]
```

を得る。共通作用殻を境界条件 $J_+=I_+^{AB}$ で切ると、残余ファイバー体積は

```math
W_{AB}
\propto
C_0-I_+^{AB}
=
J_*+I_-^{AB}
```

となる。対称な結果セクター、共通分解能、共通 coarea Jacobian の下で、

```math
P(A,B\mid a,b)
=
\frac14
\left[
1
-
V_{\rm eff}AB\cos\Delta_{ab}
\right],
\qquad
V_{\rm eff}
=
\frac{I_0}{J_*+I_0}V
```

を得る。これは共通殻などの仮説の下での厳密な体積計算である。

履歴測度は、全境界正準位相空間の Liouville 測度を作用保存と境界適合条件で制限し、Hamiltonian の解写像で許容履歴空間へ押し出す。境界適合ファイバーが設定 $a,b$ に依存するため、Bell の前提違反は測定設定独立性にある。対称セクターでは一側周辺が $1/2$ となる。

本論文の前進は、第I部の遠回りな Fisher 力密度閉鎖を、運動量結合から配置拡散へ進む経路へ置き換えたことである。残る中心課題は、有限 Hamiltonian 誘導場からの配置拡散極限、配置 Markov 閉鎖、時間対称動力学と、第II部の全殻準備、一般測定器、事後選別のない試行周期である。
