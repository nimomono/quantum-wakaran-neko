@number: 0
@chapter: 概要
@title: 構造化誘導場を持つ弱開放古典 Hamiltonian 系の二側縮約：Fisher 応力と境界作用殻 Bell 型統計
@status: 共通のミクロ構成から2つの縮約経路を示す。Liouville モーメント式、補助 Gauss 型作用定理、作用殻幾何は厳密結果である。二側短記憶極限、Fisher 閉鎖、同じ誘導場からの全殻拡散は予想・未解決である。

本論文は、有限自由度の古典 Hamiltonian 系を基礎としながら、対象部分を外部との微小なエネルギー交換を伴う弱開放系として扱う。中心となる有限部分は、粒子または測定対象、構造化誘導場、測定器、記録器、境界3モードからなる。外部自由度と仕事源まで含む拡大全系を

```math
H_{\rm all}
=
H_{\rm fin}(z)
+
H_{\rm ext}(y)
+
\varepsilon_{\rm ext}H_{\rm link}(z,y)
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

となる。外部への常時のごく弱い漏れは、Fisher 応力や作用殻の等方性を直接生む入力ではない。主な役割は、欠陥成分の除去、有限浴の再帰抑制、記録安定化である。非零の準定常作用を保つには、流入または仕事源も必要になる。

現行モデルの共通部分は、時間に依存しない明・暗モード分解を持つ構造化誘導場である。第I部では、この誘導場を粒子の有効力学へ縮約する。第II部では、同じ物理構成を2粒子、左右測定器、共通境界3モードへ拡張し、境界作用殻の履歴測度へ縮約する。2つの縮約が同じ具体的な有限パラメータ集合から同時に成立することは未証明なので、1本の完成定理とは呼ばない。

第I部の有限誘導場を、粒子座標 $X$、運動量 $P$、場座標 $Q$、共役運動量 $\Pi$ により

```math
H_N
=
\frac{|P|^2}{2m}
+
V(X)
+
\frac12\Pi^{\mathsf T}\Pi
+
\frac12Q^{\mathsf T}K_NQ
-
G_N(X)^{\mathsf T}B^{\mathsf T}Q
+
H_{\rm leak,N}
```

と書く。直接駆動方向 $B$ は、装置構造だけから固定した明部分空間に属し、暗射影 $P_{\rm D}$ に対して

```math
P_{\rm D}B=0
```

を満たす。ただし $K_N$ の非対角部分による明モードから暗モードへの間接伝播は許す。位相整合成分と欠陥成分を分ける射影も、得られた密度や目標量子状態から逆算せず、$K_N$、$B$、保存作用、装置の固定スペクトル窓から事前に定める。

外部自由度を含む全 Liouville 密度を場、浴、外部変数について積分すると、粒子の配置密度 $\rho_N$ と平均速度 $v_N$ は正確に

```math
\partial_t\rho_N
+
\nabla\cdot(\rho_Nv_N)
=0,
```

```math
m\rho_N
\left(
\partial_t+v_N\cdot\nabla
\right)v_N
=
-\rho_N\nabla V
+
\rho_N\overline F_{{\rm G},N}
-
\frac1m
\nabla\cdot
\left(
\rho_N\Sigma_{p,N}
\right)
```

を満たす。$\overline F_{{\rm G},N}$ は誘導場の条件付き平均反作用、$\Sigma_{p,N}$ は位置を固定した運動量共分散である。これは近似でなく、Liouville 方程式の0次と1次のモーメント式である。

線形誘導場は、指定した初期条件または二側境界条件の下で Green 作用素により正確に消去できる。自己共役な二側 Green 核は時間対称な記憶作用を与えるが、それだけで Markov 拡散や Nelson の平均加速度は導かれない。短記憶化、条件付き均質化、前進・後退で共通な拡散係数、非 Markov 残差の抑制を別々の縮約条件として置く。

二側 Markov 拡散が得られた有効モデル内部では、前進・後退流れ $b_+,b_-$ から

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

が厳密に従う。このとき Bohm–Fisher 応力を

```math
P_F[\rho]
=
-m\nu^2\rho\,\nabla\nabla\log\rho
```

と定めれば、

```math
-\nabla\cdot P_F[\rho]
=
2m\nu^2\rho\,
\nabla
\left(
\frac{\Delta\sqrt\rho}{\sqrt\rho}
\right)
```

となる。

第I部の中心課題は、ミクロ反作用と運動量流束がこの応力へ閉じること、すなわち

```math
\rho_N\overline F_{{\rm G},N}
-
\frac1m
\nabla\cdot
\left(
\rho_N\Sigma_{p,N}
\right)
\longrightarrow
-\nabla\cdot P_F[\rho]
```

を一様な誤差評価とともに示すことである。本論文はこれを **Fisher 閉鎖予想** と呼ぶ。左辺の正確なモーメント式、右辺の二側拡散内部での代数、両者が一致するための目標式は得るが、中央の収束はまだ証明しない。

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
\frac hT+
\frac{T^2}{Nh^2}
\right)
```

を付録で保つ。これは二側拡散が得られた後の作用表示を制御する厳密結果であり、Fisher 閉鎖予想の証明ではない。$h_N=TN^{-1/3}$ なら誤差は $O(N^{-1/3})$ である。

第II部では、同じ構造化誘導場を、左右の局所反応座標、暗モード、共通境界3モードへ静的に分ける。局所測定窓の左右交差応答を $\varepsilon_{\rm loc}\ll1$ に抑え、共同重みは局所相互作用でなく、共通未来の境界適合ファイバーから得る。

境界3モードの作用を $J_+,J_s,J_r$ とし、共通総作用殻を

```math
J_++J_s+J_r=C_0
```

とする。縮約された殻接方向混合が非退化な $U(3)$ 等方拡散なら、共通殻上の正規化 Liouville 測度が一意な定常分布になる。この縮約方程式内部の一意性は厳密だが、同じ誘導場からその生成子を導くことは未解決である。

局所記録後の2つの実2次元伝達ベクトルから、固定した和・差基底により

```math
I_+^{AB}
=
I_0
\left[
1+ABV\cos\Delta_{ab}
\right],
\qquad
I_-^{AB}
=
I_0
\left[
1-ABV\cos\Delta_{ab}
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

履歴測度は、解空間へ直接 Liouville 測度を置くものではない。全境界正準位相空間の Liouville 測度を作用保存と境界適合条件で制限し、Hamiltonian の解写像で許容履歴空間へ押し出す。境界適合ファイバーが $a,b$ に依存するため、Bell の前提違反は測定設定独立性にある。対称セクターでは一側周辺が $1/2$ となる。

本論文が統合したのは、Fisher 側と Bell 側の完成導出ではなく、両者を同じ構造化誘導場、固定射影、二側条件付け、弱い外部交換という物理構成の下へ置き、どの縮約定理が未完成かを明示したことである。
