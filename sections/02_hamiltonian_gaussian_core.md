@number: 2
@chapter: 本文
@title: 運動量結合した粒子、構造化誘導場、外部流路
@status: 粒子と有限誘導場の運動量2次形式、正定値条件、時間反転対称性、Hamilton 方程式は厳密結果である。配置速度揺らぎの短記憶極限と選択的な欠陥減衰は近似候補である。

## 2.1 運動量結合した有限誘導場

粒子座標を $X\in\mathbb R^d$、その正準運動量を $P\in\mathbb R^d$ とする。有限誘導場は $M_N$ 個の実正準対

```math
(Q,\Pi)
\in
\mathbb R^{M_N}\times\mathbb R^{M_N}
```

で表す。$M_N=M_N^{\mathsf T}>0$ を場の質量行列、$K_N=K_N^{\mathsf T}>0$ を場の剛性行列、$C_N\in\mathbb R^{d\times M_N}$ を固定した運動量結合行列とする。有限部分の中心 Hamiltonian を

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

とする。$H_N^{\rm nl}$ は必要に応じて加える弱い内部非線形項である。中心変更は、粒子と場の直接結合を座標の積でなく

```math
P^{\mathsf T}C_N\Pi
```

という運動量の積にしたことである。これにより、場は粒子へ直接の乱雑力を加えるのでなく、粒子の配置速度へ直接入る。

## 2.2 正定値条件

運動量2次形式が下に有界である条件を明示する。粒子側のブロック $m^{-1}I_d$ は正定値なので、Schur 補完により必要十分条件は

```math
M_N^{-1}
-
mC_N^{\mathsf T}C_N
>
0
```

である。同じことは平方完成

```math
\frac{|P|^2}{2m}
+
P^{\mathsf T}C_N\Pi
+
\frac12\Pi^{\mathsf T}M_N^{-1}\Pi
=
\frac1{2m}
\left|P+mC_N\Pi\right|^2
+
\frac12\Pi^{\mathsf T}
\left(
M_N^{-1}-mC_N^{\mathsf T}C_N
\right)
\Pi
```

からも分かる。従って結合強度は任意に大きくできない。本論文ではこの正定値条件を有限モデルの成立条件とする。

## 2.3 Hamilton 方程式と配置速度

$H_N^{\rm nl}=0$ の線形核では、Hamilton 方程式は

```math
\dot X
=
\frac Pm
+
C_N\Pi,
\qquad
\dot P
=
-\nabla V(X),
```

```math
\dot Q
=
M_N^{-1}\Pi
+
C_N^{\mathsf T}P,
\qquad
\dot\Pi
=
-K_NQ
```

となる。場が配置速度へ加える成分を

```math
Y_N
=
C_N\Pi
```

と書く。この記号は第3章以降で固定する。

$P$ は正準運動量であり、機械的運動量 $m\dot X$ とは一致しない。

```math
m\dot X
=
P
+
mY_N
```

である。この区別を失うと、配置流束と運動量流束を取り違える。特に、配置密度の連続の式へ入る速度は $P/m$ だけでなく $Y_N$ を含む。

$H_N^{\rm nl}$ を残す場合は、$\dot X$ と $\dot Q$ にそれぞれ $\nabla_PH_N^{\rm nl}$ と $\nabla_\Pi H_N^{\rm nl}$、$\dot P$ と $\dot\Pi$ にそれぞれ $-\nabla_XH_N^{\rm nl}$ と $-\nabla_QH_N^{\rm nl}$ が加わる。本論文の正確な消去式は線形核について述べ、非線形項は混合と誤差の候補として分ける。

## 2.4 時間反転対称性

標準時間反転を

```math
\mathcal T:
(X,P,Q,\Pi,t)
\longmapsto
(X,-P,Q,-\Pi,-t)
```

とする。運動量結合項は

```math
(-P)^{\mathsf T}C_N(-\Pi)
=
P^{\mathsf T}C_N\Pi
```

なので時間反転で不変である。$H_N^{\rm nl}$ も全運動量の同時反転で偶関数なら、有限閉鎖核は時間反転対称である。

この対称性は、二側境界条件を置くことと両立する。しかし、時間反転対称な Hamiltonian だけから二側 Markov 拡散、共通拡散係数、Nelson の時間対称 Newton 則が自動的に従うわけではない。

## 2.5 静的な明・暗モード分解

運動量結合が場へ直接入る方向は

```math
\mathcal B_{\rm mom}
=
\operatorname{Ran}C_N^{\mathsf T}
```

である。第II部で使う装置の座標結合方向も含めた固定明部分空間を $\mathcal B_{\rm B}$、その直交補空間を $\mathcal B_{\rm D}$ とし、射影を $P_{\rm B},P_{\rm D}$ と書く。Fisher 側の運動量結合が暗モードを直接駆動しない条件は

```math
P_{\rm D}C_N^{\mathsf T}
=
0
```

である。

この条件は、$M_N^{-1}$ と $K_N$ が明・暗部分空間を保存することを意味しない。一般には

```math
P_{\rm D}K_NP_{\rm B}
\neq
0,
\qquad
P_{\rm D}M_N^{-1}P_{\rm B}
\neq
0
```

であり、内部発展による間接伝播が残る。この伝播は有限記憶、欠陥移送、Bell 側の局所セクター間交差応答の候補になる。

$\mathcal B_{\rm B}$ と $\mathcal B_{\rm D}$ に適合した直交行列 $O_N$ を固定し、

```math
\widetilde Q
=
O_NQ,
\qquad
\widetilde\Pi
=
O_N\Pi
```

と変換する。座標と共役運動量へ同じ直交行列を作用させるので、この変換は正準である。変換後の $O_NK_NO_N^{\mathsf T}$ と $O_NM_N^{-1}O_N^{\mathsf T}$ は一般にブロック対角ではない。静的な正準分類と動力学的な直和分離を混同しない。

## 2.6 位相整合成分と欠陥成分

長時間保つ位相整合成分と、外部へ移送する欠陥成分を分ける固定射影を

```math
P_{\rm c},
\qquad
P_\perp
=
I-P_{\rm c}
```

と書く。$P_{\rm c}$ は、$K_N$ と $M_N$ の固定スペクトル帯、$C_N^{\mathsf T}$ が生成する Krylov 部分空間、保存作用、装置構造から事前に定める。

得られた配置密度、目標量子状態、または欲しい Fisher 項を見て射影を選んではならない。正準な射影を定めたことは、その欠陥成分だけが不可逆に減衰することも、配置空間の Markov 性も意味しない。

## 2.7 外部流路を含む拡大全系

外部自由度を $(Z_{\rm ext},\Pi_{\rm ext})$、仕事貯蔵自由度を $z_{\rm work}$ とし、

```math
H_N^{\rm all}
=
H_N^{\rm fin}
+
H_{\rm ext}
+
\varepsilon_{\rm ext}H_{\rm link}
+
H_{\rm work}
+
H_{\rm ctrl}
```

とする。$H_{\rm ctrl}$ は自律時計を含む設定変更、記録、再準備の有限相互作用をまとめた記号である。

全 Hamiltonian に外からの陽な時間依存がなければ、拡大全エネルギーは保存される。有限部分だけを見た収支は

```math
\frac{\mathrm d}{\mathrm dt}H_N^{\rm fin}
=
\left\{
H_N^{\rm fin},
\varepsilon_{\rm ext}H_{\rm link}
+
H_{\rm ctrl}
\right\}
```

となる。弱開放性は基礎方程式へ摩擦や白色雑音を直接追加することではなく、外部自由度を消去した後の有限部分の収支として現れる。

## 2.8 選択的な弱漏れと時間窓

欠陥成分へ強く、位相整合成分へ弱く結合する候補は、$P_\perp Q$、$P_\perp\Pi$ と外部自由度の結合として構成できる。外部相関時間が短く、対象周波数帯でスペクトル密度が滑らかなら、欠陥成分の有効減衰率を $\gamma_\perp$、整合成分の漏れ率を $\gamma_{\rm c}$ として

```math
\tau_{\rm corr}
\ll
\gamma_\perp^{-1}
\ll
\tau_{\rm coh},
\qquad
\gamma_{\rm c}
\ll
\gamma_\perp
```

を目標にできる。有限モデルから一様な指数減衰と流入補正を証明したわけではないため、これは近似候補である。

観測窓 $T_{\rm obs}$ と有限浴の再帰時間 $T_{\rm rec}$ には

```math
\tau_{\rm corr}
\ll
T_{\rm obs}
\ll
T_{\rm rec}
```

を要求する。測定窓では外部交換を小さい補正として扱い、試行間の準備窓では欠陥除去と再帰抑制を利用する。

## 2.9 弱漏れが担わない役割

選択的な弱漏れが実現しても、次は自動的には従わない。

1. $\int_0^tY_N(s)\,\mathrm ds$ が Brown 運動へ近づくこと。
2. 反作用記憶項が局所ドリフトまたは制御可能な残差へ縮約されること。
3. 配置変数 $X$ だけの射影が Markov 過程になること。
4. 二側条件付け後の前後過程が同じ拡散係数を持つこと。
5. Nelson の時間対称 Newton 則が成立すること。
6. Bell 側の3モード作用殻が $U(3)$ 等方になること。

弱漏れの主な役割は欠陥除去と再帰抑制である。配置拡散には多数モードの短記憶極限、Fisher 項には二側配置拡散の運動学、時間対称 Newton 則には独立した動力学的縮約、作用殻の方向準備には Hamiltonian な内部混合が必要である。

## 2.10 本章の結論

運動量結合 $P^{\mathsf T}C_N\Pi$ により、誘導場は粒子の配置速度へ $Y_N=C_N\Pi$ として直接入る。運動量2次形式の正定値条件、Hamilton 方程式、時間反転対称性、正準運動量と機械的運動量の差は有限モデル内部の厳密結果である。

固定明部分空間は $\operatorname{Ran}C_N^{\mathsf T}$ と第II部の装置結合方向を含む。外部流路は欠陥除去と有限再帰の抑制に使うが、配置拡散、$X$ 射影の Markov 性、時間対称 Newton 則をそれだけで導くものではない。
