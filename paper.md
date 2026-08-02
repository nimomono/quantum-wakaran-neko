# 概要


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

# 問題設定とモデル地図

> **位置づけ：** 位相接続、配置拡散、境界作用殻を同じ構造化誘導場アーキテクチャの異なる縮約経路として整理する。同じ完成 Hamiltonian からの同時導出は未完成である。


## 問題設定

本論文の目的は、明示的な古典 Hamiltonian 系から、量子力学に特徴的な確率構造が縮約された有効理論として出現し得るかを検証することである。量子力学をミクロ構成の入力には使わず、縮約後の式と比較するときだけ参照する。

中心問題を次の4点に分ける。

1. 有限2成分場との位相接続から、Nelson--Madelung 作用と Schrödinger 型力学を得られるか。
2. 場強度と粒子密度の一致を定義として置かず、入口の Liouville 流束から位置の Born 型重みを得られるか。
3. 運動量結合した有限誘導場から、実在的な前後 Markov 拡散と同じ有効作用定数を得られるか。
4. 境界作用殻の幾何から Bell 型共同統計を得て、Bell の前提違反と非信号条件を特定できるか。

本論文は1、2、4について限定された縮約模型内部の結果を与える。3と、全構成を1つの試行周期へ統合する部分は未完成である。

## 拡大全系と弱開放な有限部分

有限部分を

```math
H_{\rm fin}
=
H_{\rm obj}
+
H_{\rm phase}
+
H_{\rm bath}
+
H_{\rm dev}
+
H_\partial
+
H_{\rm fin-link}
```

と書く。外部環境と仕事源まで含む拡大全系は

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

である。拡大全系は Hamiltonian とし、有限部分だけを見た収支を

```math
\dot E_{\rm fin}
=
J_{\rm in}
-
J_{\rm out}
+
P_{\rm ctrl}
```

と表す。常時の弱い外部交換は、欠陥成分の除去、有限浴再帰の抑制、記録安定化、非零作用半径の維持に使う。Fisher 項、coherent状態、作用殻の方向一様性を、外部漏れから直接仮定しない。

1試行の測定窓では、外部交換の相対変化を小さくし、有限閉鎖 Hamiltonian 補助模型で正準写像、保存量、作用殻体積を計算する。試行間では、仕事源と外部流路を含めて再準備、記録消去、再初期化を扱う。

## 3つの縮約経路

3経路の役割は異なる。

| 経路 | ミクロな直接結合 | 得られるもの | 未完成な接続 |
|---|---|---|---|
| 位相接続経路 | $P-\mathcal J_\phi\mathbf a_\varepsilon(X)$ | 縮約作用、Madelung 方程式、局所 Schrödinger 型PDE、条件付き循環量子化 | coherent多様体の準備、維持、節の制御 |
| 配置拡散経路 | $P^{\mathsf T}C_N\Pi$ | 配置速度揺らぎ、反作用記憶、前後 Markov 拡散候補 | Brown 極限、配置 Markov 閉鎖、係数一致 |
| 境界作用殻経路 | 装置座標と明反応座標・境界モードの固定結合 | Born 型入口流束、Bell 型残余ファイバー体積 | 等方準備、一般測定器、完全周期 |

位相接続経路は、縮約多様体上で力学を閉じる。配置拡散経路は、Nelson の前後過程を実在的な確率過程として作る候補である。前者が後者を自動的に導くことも、後者が前者の作用変分を自動的に与えることもない。

両経路が同じ有効理論を表すためには、

```math
\hbar_{\rm eff}
=
|\mathcal J_\phi|
=
2m\nu_{\rm bath}
```

が必要である。これは定義ではなく、2つの独立な縮約係数の整合条件である。

## 固定部分空間による共存

構造化誘導場の基底を、設定、結果、目標密度を見て切り替えない。位相活性場、運動量結合浴、装置の明反応座標、境界モード、暗モードが張る部分空間を装置の組立時に固定する。

位相活性場と配置拡散浴を同じ正準変数へ無条件に重ねると、接続

```math
\mathbf a_\varepsilon(\boldsymbol\Phi)
```

が活性場に依存するため、線形浴消去式はそのまま使えない。統合候補の運動エネルギーは

```math
\widetilde P
=
P-\mathcal J_\phi\mathbf a_\varepsilon(X),
```

```math
H_{\rm kin}
=
\frac12
\begin{pmatrix}
\widetilde P\\
\Pi
\end{pmatrix}^{\mathsf T}
\begin{pmatrix}
m^{-1}I & C_N\\
C_N^{\mathsf T} & M_N^{-1}
\end{pmatrix}
\begin{pmatrix}
\widetilde P\\
\Pi
\end{pmatrix}.
```

Schur 補条件は

```math
M_N^{-1}
-
mC_N^{\mathsf T}C_N
>
0
```

である。しかし $\mathbf a_\varepsilon$ の場依存性は、浴方程式と粒子方程式へ新しい非線形交差項を加える。

本論文では、位相活性場と配置拡散浴を固定された別部分空間へ置き、交差作用を

```math
\varepsilon_{\rm cross}
```

として管理する。従って「1つの完成 Hamiltonian から全結果を導いた」とは主張せず、「1つの構造化誘導場アーキテクチャに置ける異なる縮約経路」と表現する。

## 現行モデルと補助モデル

| モデル | 運用状態 | 役割と限界 |
|---|---|---|
| 粒子、有限2成分場、配置拡散浴、測定器、外部流路を持つ弱開放系 | 現行モデル | 3経路の共通アーキテクチャ。完全周期と一様縮約定理は未完成 |
| 有限セル2成分位相場 | 補助モデル | 正準1形式、保存位相作用、局所作用分配を有限次元で計算する |
| 位相接続縮約模型 | 補助モデル | coherent多様体上の Nelson--Madelung 作用を与える |
| 2モード入口作用殻 | 補助モデル | 位置の Born 型入口流束を与える |
| 運動量結合した線形誘導場 | 補助モデル | 速度揺らぎと反作用記憶を正確に分ける |
| 配置変数の二側 Markov 拡散 | 補助モデル | 浸透速度と Fisher 項を整理する |
| 3モード境界作用殻 | 補助モデル | Bell 型残余ファイバー体積を計算する |
| $U(3)$ 等方殻拡散 | 補助モデル | 共通殻 Liouville 測度を定常分布として与える |

補助模型内部で厳密な結果が得られても、現行モデルから補助模型への縮約が未完成なら、現行モデル全体から導出済みとは呼ばない。

## 試行周期と排他的チャンネル

位置入口の標本化では、チャンネルを直積でなく排他的な和として扱う。

```math
\Gamma_\partial
=
\bigsqcup_i
\Gamma_{\partial,i}.
```

各履歴は1つの入口反応面だけを横切る。粒子位置窓 $\chi_i(X)$ が、セル $i$ の活性モードと1つの共有明反応座標を結合する。他セルの作用殻を同時に積分しない。

完全周期には少なくとも次が必要である。

1. coherent活性場と2モード作用殻の準備。
2. 全入口履歴を捨てない Liouville 流束標本化。
3. 結果情報の暗モードまたは記録器への可逆転送。
4. 活性場の coherent 部分空間への再埋め込み。
5. 明反応座標の基準状態への復元。
6. 設定、記録、garbage自由度の消去または外部への移送。
7. 次試行の再準備。

本論文が示すのは1と2の理想化された作用殻構造、および3以降に必要な保存則である。標本化後の完全な復元は未解決である。

## 導出状態の読み方

本論文では次を区別する。

- 縮約多様体に制限した後の代数、変分、作用殻体積は、明記した条件の下で厳密である。
- ミクロ時間発展がその多様体を準備し、観測窓で保ち、縮約作用の停留点を選ぶことは別の主張である。
- 閉鎖 Hamiltonian 流は位相体積を保存し、一般に低次元多様体へ吸引しない。
- 弱開放性は準備済み構造の安定化候補であり、coherent構造や一様作用殻を単独で生成しない。

この区別を、各章の位置づけと第8章の誤差表へ反映する。

# 第I部　位相接続と Nelson--Madelung 縮約

# 有限2成分誘導場と位相接続 Hamiltonian

> **位置づけ：** 有限セルの正準変換、内部回転対称性、保存位相作用、固定作用下の局所作用分配、粒子運動量消去は厳密結果である。coherent多様体の準備と連続極限は未完成である。


## 有限セルから始める理由

有限モード切断した場では、振幅 $r(x)$、位相 $\theta(x)$、局所作用 $j(x)$ は任意の独立関数ではない。切断された場多様体上の従属変数である。そこで、最初に有限個のセルを持つ正準系を定義し、連続表示はその後の近似として扱う。

セル $i=1,\ldots,L$ に2成分正準対

```math
\boldsymbol\Phi_i
=
\begin{pmatrix}
\Phi_{1,i}\\
\Phi_{2,i}
\end{pmatrix},
\qquad
\boldsymbol\Pi_i
=
\begin{pmatrix}
\Pi_{1,i}\\
\Pi_{2,i}
\end{pmatrix}
```

を置く。Poisson 括弧は

```math
\left\{
\Phi_{\alpha,i},
\Pi_{\beta,j}
\right\}
=
\delta_{\alpha\beta}\delta_{ij}.
```

$r_i>0$ の領域で

```math
\boldsymbol\Phi_i
=
r_i
\begin{pmatrix}
\cos\theta_i\\
\sin\theta_i
\end{pmatrix}
```

と書き、

```math
p_{r,i}
=
\boldsymbol\Pi_i\cdot
\frac{\boldsymbol\Phi_i}{r_i},
```

```math
j_i
=
\Phi_{1,i}\Pi_{2,i}
-
\Phi_{2,i}\Pi_{1,i}
```

と定める。

<!-- theorem-start:proposition -->
**命題（有限セル極座標の正準1形式）**
$r_i>0$ の各セルで、

```math
\boldsymbol\Pi_i\cdot d\boldsymbol\Phi_i
=
p_{r,i}\,dr_i
+
j_i\,d\theta_i
```

が成立する。従って $(r_i,p_{r,i})$ と $(\theta_i,j_i)$ は正準対である。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
単位ベクトル

```math
e_{r,i}
=
\begin{pmatrix}
\cos\theta_i\\
\sin\theta_i
\end{pmatrix},
\qquad
e_{\theta,i}
=
\begin{pmatrix}
-\sin\theta_i\\
\cos\theta_i
\end{pmatrix}
```

を用いると、

```math
d\boldsymbol\Phi_i
=
e_{r,i}\,dr_i
+
r_ie_{\theta,i}\,d\theta_i.
```

$p_{r,i}=\boldsymbol\Pi_i\cdot e_{r,i}$ と $j_i=r_i\boldsymbol\Pi_i\cdot e_{\theta,i}$ を代入すればよい。
<!-- theorem-end:proof -->

## 場 Hamiltonian と規格化

セル体積を $\Delta V$ とし、場強度を

```math
\mathcal N_\Phi
=
\sum_i r_i^2\Delta V
```

とする。理想縮約では $\mathcal N_\Phi=1$ を用いる。有限装置では、規格化逸脱を

```math
H_{\rm norm}
=
\frac{\lambda_{\rm norm}}{2}
\left(
\mathcal N_\Phi-1
\right)^2
```

でエネルギー的に抑えることができる。ただし $H_{\rm norm}$ は規格化を厳密に保存する制約ではない。厳密な固定規格化sectorを使うか、$\lambda_{\rm norm}$ が大きい観測窓で

```math
\left|
\mathcal N_\Phi-1
\right|
\ll1
```

を誤差として管理する。

回転不変な場 Hamiltonian の代表形を

```math
H_{\rm phase}
=
\sum_i
\left[
\frac{p_{r,i}^2}{2M_r}
+
\frac{j_i^2}{2Ir_i^2}
+
U(r_i)
\right]
\Delta V
+
H_{\rm grad}
+
H_{\rm norm}
```

とする。$H_{\rm grad}$ はセル差分に対して内部 $SO(2)$ 回転不変とし、連続極限で少なくとも

```math
H_{\rm grad}
\longrightarrow
\int
\left[
\kappa|\nabla r|^2
+
\kappa_\theta r^2|\nabla\theta|^2
\right]
\,dx
```

を含み得る。本論文の Nelson--Madelung 縮約では、振幅勾配係数 $\kappa$ を保持し、位相勾配の運動エネルギーは粒子流速側へ整理する。二重計数を避ける係数条件は第3章で明記する。

## 内部回転対称性と保存作用

全セルを共通角 $\alpha$ だけ回す変換を

```math
\boldsymbol\Phi_i
\longmapsto
R(\alpha)\boldsymbol\Phi_i,
\qquad
\boldsymbol\Pi_i
\longmapsto
R(\alpha)\boldsymbol\Pi_i
```

とする。生成子は

```math
\mathcal J_\phi
=
\sum_i j_i\Delta V.
```

場 Hamiltonian、粒子との結合、外部結合がこの共通回転に不変なら、

```math
\left\{
\mathcal J_\phi,
H_{\rm all}
\right\}
=
0.
```

局所位相勾配があると各 $j_i$ はセル間を流れるため、個別には保存されない。保存されるのは全位相作用 $\mathcal J_\phi$ である。

## 固定作用下の局所作用分配

規格化 $\mathcal N_\Phi=1$ と全作用 $\mathcal J_\phi$ を固定する。回転エネルギーは

```math
E_{\rm rot}
=
\sum_i
\frac{j_i^2}{2Ir_i^2}
\Delta V.
```

<!-- theorem-start:theorem -->
**定理（固定作用下の局所作用分配）**
$r_i>0$、$\sum_i r_i^2\Delta V=1$、$\sum_i j_i\Delta V=\mathcal J_\phi$ の下で、

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
\Delta V.
```

従って固定 $(r_i)$ に対する一意な最小配置は

```math
j_i
=
\mathcal J_\phi r_i^2
```

である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
右辺の平方項を展開すると、

```math
\sum_i
\frac{j_i^2}{2Ir_i^2}\Delta V
-
\frac{\mathcal J_\phi}{I}
\sum_i j_i\Delta V
+
\frac{\mathcal J_\phi^2}{2I}
\sum_i r_i^2\Delta V
+
\frac{\mathcal J_\phi^2}{2I}.
```

2つの制約を代入すると、最後の3項は相殺して $E_{\rm rot}$ が残る。平方項は非負であり、全て零のときだけ最小になる。
<!-- theorem-end:proof -->

この定理はエネルギー地形を定める。閉鎖 Hamiltonian 流が最小配置へ収束することは示さない。境界準備で最小配置を選ぶか、弱開放縮約でずれ

```math
\varepsilon_j
=
\left\|
j-\mathcal J_\phi r^2
\right\|
```

を小さく保つ必要がある。弱い漏れは準備済み配置の安定化候補であり、coherent配置の生成機構としては使わない。

## 位相接続

連続補間した2成分場に対し、

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

と定める。極座標では

```math
\mathbf a_\varepsilon
=
\frac{r^2}{r^2+\varepsilon^2}
\nabla\theta.
```

$r>0$ かつ $\varepsilon\to0$ の領域では $\mathbf a_\varepsilon\to\nabla\theta$ である。$r=0$ の節では位相が定義できず、正則化誤差を別に管理する。

粒子の正準対を $(X,P)$ とし、

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

とする。$\mathcal J_\phi$ は外から置く固定定数ではなく、場の共通内部回転の保存生成子である。固定 $\mathcal J_\phi$ sectorへ制限すると、有効結合定数として働く。

## 粒子運動量の消去

Hamilton 方程式から

```math
\dot X
=
\frac{
P-\mathcal J_\phi\mathbf a_\varepsilon(X)
}{
m
}
```

なので、

```math
P
=
m\dot X
+
\mathcal J_\phi\mathbf a_\varepsilon(X).
```

<!-- theorem-start:proposition -->
**命題（位相接続 Lagrangian）**
粒子正準運動量を消去すると、

```math
L_{\rm p}
=
\frac m2|\dot X|^2
+
\mathcal J_\phi
\mathbf a_\varepsilon(X)\cdot\dot X
-
V(X)
```

を得る。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
$L_{\rm p}=P\cdot\dot X-H_{\rm p}$ へ上の $P$ を代入し、平方を整理する。
<!-- theorem-end:proof -->

節から離れた極限では接続項は

```math
\mathcal J_\phi
\nabla\theta(X)\cdot\dot X.
```

粒子集団の密度 $\rho$ と平均流速 $v$ へ粗視化すると、

```math
\mathcal J_\phi
\int
\rho
v\cdot\nabla\theta
\,dx
```

となる。場の正準項と合わせた物質微分構造は第3章で導く。

## 時間反転

標準時間反転を

```math
\mathsf T:
\quad
X\mapsto X,
\quad
P\mapsto-P,
\quad
\boldsymbol\Phi\mapsto\boldsymbol\Phi,
\quad
\boldsymbol\Pi\mapsto-\boldsymbol\Pi
```

とする。このとき

```math
\mathcal J_\phi\mapsto-\mathcal J_\phi,
\qquad
\mathbf a_\varepsilon\mapsto\mathbf a_\varepsilon.
```

従って

```math
P-\mathcal J_\phi\mathbf a_\varepsilon
\mapsto
-
\left(
P-\mathcal J_\phi\mathbf a_\varepsilon
\right),
```

であり、$H_{\rm p}$ は不変である。固定符号の $\mathcal J_\phi$ sectorだけを取り出すと時間反転は反対sectorへ写す。全理論は両sectorを含めて時間反転対称である。

## coherent集中の意味

連続場の2次モーメントが rank-one に近いことだけでは、非線形比

```math
\frac{
\Phi_1\nabla\Phi_2-\Phi_2\nabla\Phi_1
}{
|\boldsymbol\Phi|^2+\varepsilon^2
}
```

の標本平均を閉じられない。本論文でいう coherent集中は、規格化された各標本が共通の $(r,\theta)$ 近傍に集中し、接続、正準項、勾配エネルギーの非線形平均を同じ代表場で評価できることを含む。

必要な誤差を

```math
\varepsilon_{\rm coh},
\qquad
\varepsilon_{\rm node},
\qquad
\varepsilon_{\rm radial}
```

とし、それぞれ coherent集中、節正則化、動径断熱化からのずれを表す。これらを有限 Hamiltonian 時間発展から一様に小さくする定理は未完成である。

# 縮約多様体と Nelson--Madelung 作用

> **位置づけ：** coherent縮約多様体に制限した作用、変分、Schrödinger 型方程式、同期差保存は厳密結果である。多様体の生成、安定化、微視的停留点選択は未完成である。


## 縮約条件

第2章の有限セル系から連続表示へ進むため、次の条件を分けて置く。

1. **coherent集中**：非線形接続と正準項を共通の代表場 $(r,\theta)$ で評価できる。
2. **固定作用sector**：全位相作用 $\mathcal J_\phi\neq0$ を固定する。
3. **局所作用分配**：

```math
j
=
\mathcal J_\phi r^2
+
O(\varepsilon_j).
```

4. **密度同期**：

```math
r^2
=
\rho
+
O(\varepsilon_\rho).
```

5. **接続極限**：節から離れた領域で

```math
\mathbf a_\varepsilon
=
\nabla\theta
+
O(\varepsilon_{\rm node}).
```

6. **単流束化**：条件付き速度分散による古典圧力を

```math
\varepsilon_{\rm press}
```

で抑える。
7. **動径断熱化**：$p_r^2/(2M_r)$ と高速振幅モードの作用寄与を

```math
\varepsilon_{\rm radial}
```

で抑える。
8. **位相勾配の非重複**：粒子流速へ入れた位相運動エネルギーと、場側の $r^2|\nabla\theta|^2$ を二重に数えない。

これらは縮約多様体の定義と誤差条件である。有限 Hamiltonian 時間発展が一般の初期状態からこの多様体へ吸引するとは仮定しない。

## 物質微分結合

場の正準1形式は連続表示で

```math
\int
\left(
p_r\partial_tr
+
j\partial_t\theta
\right)
\,dx.
```

局所作用分配を用いると、位相部分は

```math
\mathcal J_\phi
\int
r^2\partial_t\theta
\,dx.
```

粒子の位相接続項は

```math
\mathcal J_\phi
\int
\rho
v\cdot\nabla\theta
\,dx.
```

密度同期 $r^2=\rho$ の理想極限では、両者の和は

```math
\mathcal J_\phi
\int
\rho
\left(
\partial_t\theta
+
v\cdot\nabla\theta
\right)
\,dx.
```

従って、位相は粒子流に沿う物質微分として作用へ入る。

Schrödinger 表示の位相を

```math
S
=
-\mathcal J_\phi\theta
```

と定める。すると上の項は

```math
-\int
\rho
\left(
\partial_tS
+
v\cdot\nabla S
\right)
\,dx
```

となる。

## 縮約作用

固定 $\mathcal J_\phi$ sectorで定数となる回転基底エネルギーを除き、動径慣性と交差誤差を無視した理想縮約作用を

```math
\mathcal A_{\rm red}
\left[
\rho,v,S
\right]
=
\int
\left[
\frac m2\rho|v|^2
-
\rho V
-
\rho
\left(
\partial_tS
+
v\cdot\nabla S
\right)
-
\kappa
\left|
\nabla\sqrt\rho
\right|^2
\right]
\,dx\,dt
```

とする。

<!-- theorem-start:theorem -->
**定理（縮約多様体上の作用一致）**
第3.1節の理想縮約条件が成立し、

```math
\kappa
=
\frac{\mathcal J_\phi^2}{2m}
```

なら、$\mathcal A_{\rm red}$ は有効作用定数

```math
\hbar_{\rm eff}
=
|\mathcal J_\phi|
```

を持つ Nelson--Madelung 作用に一致する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
Nelson の浸透エネルギーは

```math
\frac m2
\int
\rho|u|^2
\,dx,
\qquad
u
=
\nu\nabla\log\rho.
```

恒等式

```math
\rho
\left|
\nabla\log\rho
\right|^2
=
4
\left|
\nabla\sqrt\rho
\right|^2
```

より、

```math
\frac m2
\int
\rho|u|^2
\,dx
=
2m\nu^2
\int
\left|
\nabla\sqrt\rho
\right|^2
\,dx.
```

$|\mathcal J_\phi|=2m\nu$ を用いると $2m\nu^2=\mathcal J_\phi^2/(2m)=\kappa$ である。残りの項は現在速度形式の Nelson--Madelung 作用と一致する。
<!-- theorem-end:proof -->

この定理は作用を縮約多様体へ制限した後の一致を述べる。ミクロ運動がその制限作用の停留点を選ぶことや、実在的な Markov 経路を作ることは含まない。

## 変分方程式

$S$、$v$、$\rho$ を独立に変分し、境界変分を零とする。

$S$ 変分から、

```math
\partial_t\rho
+
\nabla\cdot(\rho v)
=
0.
```

$v$ 変分から、

```math
mv
=
\nabla S.
```

$\rho$ 変分から、

```math
\frac m2|v|^2
-
V
-
\partial_tS
-
v\cdot\nabla S
+
\kappa
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=
0.
```

$mv=\nabla S$ を代入すると、

```math
\partial_tS
+
\frac{|\nabla S|^2}{2m}
+
V
-
\kappa
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=
0.
```

量子ポテンシャルに対応する項を

```math
Q[\rho]
=
-
\frac{\mathcal J_\phi^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}
```

と書ける。

## Schrödinger 型方程式

節を避ける単連結領域で

```math
\psi
=
\sqrt\rho
\exp
\left(
\frac{iS}{\hbar_{\rm eff}}
\right),
\qquad
\hbar_{\rm eff}
=
|\mathcal J_\phi|
```

とする。連続の式と Hamilton--Jacobi 式は

```math
i\hbar_{\rm eff}
\partial_t\psi
=
\left[
-
\frac{\hbar_{\rm eff}^2}{2m}
\Delta
+
V
\right]
\psi
```

に等価である。

活性場を

```math
\Psi_{\rm A}
=
re^{i\theta}
```

と書く。$S=-\mathcal J_\phi\theta$ なので、$\mathcal J_\phi>0$ sectorかつ $r^2=\rho$ では

```math
\psi
=
\Psi_{\rm A}^*.
```

活性場と Schrödinger 表示を同じ記号にしない。

## 係数不一致

場の振幅勾配係数が

```math
\kappa
=
\frac{\mathcal J_\phi^2}{2m}
+
\delta\kappa
```

なら、Hamilton--Jacobi 式には

```math
-\delta\kappa
\frac{\Delta\sqrt\rho}{\sqrt\rho}
```

が残る。$\hbar_{\rm eff}=|\mathcal J_\phi|$ で定義した $\psi$ に対して、これは標準 Schrödinger 方程式からの非線形残差になる。

従って

```math
\varepsilon_\kappa
=
\frac{
\left|
\delta\kappa
\right|
}{
\mathcal J_\phi^2/(2m)
}
```

を独立に管理する。$\kappa=\mathcal J_\phi^2/(2m)$ は内部回転対称性だけから従う定理ではなく、ミクロ係数の整合条件である。

## 密度同期差の保存

密度同期を作用へ代入する前の位相部分を

```math
\mathcal A_\theta
=
\int
\left[
j\partial_t\theta
+
\mathcal J_\phi
\rho v\cdot\nabla\theta
\right]
\,dx\,dt
```

とする。残余の場エネルギーが共通位相 $\theta$ に依存しない理想縮約では、$\theta$ 変分から

```math
\partial_tj
+
\mathcal J_\phi
\nabla\cdot(\rho v)
=
0
```

を得る。

<!-- theorem-start:proposition -->
**命題（coherent多様体上の同期差保存）**
$\mathcal J_\phi\neq0$、$j=\mathcal J_\phi r^2$、粒子密度が連続の式を満たすなら、

```math
\partial_t
\left(
r^2-\rho
\right)
=
0.
```
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
$j=\mathcal J_\phi r^2$ を位相保存式へ代入して $\mathcal J_\phi$ で割ると、

```math
\partial_tr^2
+
\nabla\cdot(\rho v)
=
0.
```

粒子の連続の式との差を取る。
<!-- theorem-end:proof -->

これは同期差の中立的保存である。$r^2\neq\rho$ の状態を同期へ引き戻す復元力は含まない。入口で $r^2=\rho$ を作る作用殻流束を第4章で与える。

## 循環量子化

2成分場が閉曲線 $\gamma$ 上で非零かつ単価なら、位相写像の巻数 $n\in\mathbb Z$ により

```math
\oint_\gamma
\nabla\theta\cdot d\ell
=
2\pi n.
```

従って

```math
\oint_\gamma
\nabla S\cdot d\ell
=
-2\pi\mathcal J_\phi n
=
2\pi\hbar_{\rm eff}N,
\qquad
N\in\mathbb Z.
```

最後の整数 $N$ は $-\operatorname{sgn}(\mathcal J_\phi)n$ である。

この命題は、単価な2成分場と非零経路を仮定した条件付き循環量子化である。次は未完成である。

- $r=0$ の節近傍における接続と $j^2/r^2$ の同時正則化。
- 節の生成・消滅時における巻数変化。
- 密度同期が節を含む領域で維持される条件。
- 全ての物理的初期流れが単価な活性場から準備されること。

従って位相量子化は部分達成であり、Wallstrom 問題への全面的回答ではない [19]。

## 作用一致と力学導出の境界

本章で厳密なのは、縮約条件を満たす多様体に制限した作用の代数、変分、局所 Schrödinger 表示、同期差保存、条件付き循環量子化である。

未解決なのは、

1. 一般の有限 Hamiltonian 初期集団から coherent多様体を準備すること。
2. 観測窓で $\varepsilon_{\rm coh}$、$\varepsilon_j$、$\varepsilon_\rho$、$\varepsilon_{\rm radial}$、$\varepsilon_{\rm press}$ を同時に小さくすること。
3. ミクロ運動の粗視化が $\mathcal A_{\rm red}$ の停留点を選ぶこと。
4. 実在的な前後 Markov 経路を同じ模型から得ること。

第5章の運動量結合経路は4の候補を与えるが、本章の導出を置換しない。

# 境界作用殻による Born 型入口標本化

> **位置づけ：** 一般作用殻体積、2モード殻の線形重み、共通流束因子の下での位置入口密度、直接作用分配次元の剛性は厳密結果である。等方準備と標本化後の再埋め込みは未完成である。


## 一般作用殻体積

$n$個の複素正準モードを

```math
a_k
=
\frac{
q_k+ip_k
}{
\sqrt2
},
\qquad
J_k
=
|a_k|^2
```

とする。作用角変数では

```math
dq_k\,dp_k
=
dJ_k\,d\theta_k.
```

固定総作用

```math
\sum_{k=1}^nJ_k=A,
\qquad
J_k\geq0
```

の未規格化 Liouville 殻容量を

```math
\Omega_n(A)
=
\int
\delta
\left(
A-\sum_{k=1}^nJ_k
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
(2\pi)^n
}{
(n-1)!
}
A^{n-1}.
```
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
角変数の積分が $(2\pi)^n$ を与える。残る作用変数の積分は、$J_k\geq0$ と $\sum_kJ_k=A$ が作る $(n-1)$ 次元単体のデルタ測度であり、$A^{n-1}/(n-1)!$ である。
<!-- theorem-end:proof -->

このべき指数が Born 型重みと Bell 型重みを決める。

## 局所作用と排他的入口チャンネル

第3章の活性場強度をセル表示へ戻し、

```math
\sum_i r_i^2\Delta V
=
1
```

とする。全入口作用 $A_{\rm tot}>0$ をセルへ

```math
A_i
=
A_{\rm tot}r_i^2\Delta V
```

と割り当てる。

入口反応面は

```math
\Gamma_\partial
=
\bigsqcup_i
\Gamma_{\partial,i}
```

という排他的な和とする。1つの履歴が通過するのは1つの $\Gamma_{\partial,i}$ だけである。他セルの入口殻を同時に積分しない。

比較器または反応座標は全チャンネルで共有する。粒子位置窓 $\chi_i(X)$ が、セル $i$ の活性モードと共有明反応座標を選択的に結合する。各排他的sectorで、活性側に残る作用を $K_i$、共有反応座標の作用を $I$ とし、

```math
K_i+I=A_i
```

を課す。

## 2モード殻の線形容量

$n=2$ の一般定理から、

```math
\Omega_2(A_i)
=
(2\pi)^2A_i.
```

正方向入口流束を

```math
\mathscr F_i
=
\int_{\Gamma_{\partial,i}}
\left(
\dot s_i
\right)_+
d\mu_i
```

とする。$s_i$ は反応面の法線座標、$d\mu_i$ は作用殻、spectator自由度、coarea因子を含む誘導測度である。

作用殻の線形容量以外を流束因子 $\lambda_i$ へまとめ、

```math
\mathscr F_i
=
\lambda_i\Omega_2(A_i)
```

と書く。$\lambda_i$ は、法線速度、障壁透過、反応面の向き、coarea Jacobian、spectatorモードの体積、有限入口窓を含む。

<!-- theorem-start:theorem -->
**定理（2モード入口殻からの Born 型位置重み）**
全チャンネルで

```math
\lambda_i=\lambda>0
```

が成立し、各開始履歴を正方向入口通過として1回ずつ数えるなら、

```math
P_i
=
\frac{
\mathscr F_i
}{
\sum_j\mathscr F_j
}
=
r_i^2\Delta V.
```

従ってセル平均の入口密度は

```math
\rho_{{\rm in},i}
=
r_i^2.
```
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
共通 $\lambda$ と $\Omega_2(A_i)=(2\pi)^2A_i$ により、

```math
P_i
=
\frac{A_i}{\sum_jA_j}.
```

$\sum_jA_j=A_{\rm tot}$ と $A_i=A_{\rm tot}r_i^2\Delta V$ を代入する。
<!-- theorem-end:proof -->

これは場強度を確率と定義した結果ではない。入口反応面を横切る Liouville 流束の相対頻度として得た結果である。

## 共通流束条件と誤差

一般には、基準流束因子 $\lambda>0$ に対する相対偏差を

```math
\frac{\lambda_i}{\lambda}
=
1+\delta_i
\qquad
\sum_i
r_i^2\Delta V\,\delta_i
=
0
```

と定義する。すると

```math
P_i
=
\frac{
r_i^2\Delta V
\left(
1+\delta_i
\right)
}{
\sum_j
r_j^2\Delta V
\left(
1+\delta_j
\right)
}.
```

従って

```math
\varepsilon_{\rm flux}
=
\max_i|\delta_i|
```

が Born 型重みからの主要な1次誤差になる。位置依存の障壁、セル体積、窓関数、法線速度を同じにしただけでは十分でなく、coarea Jacobian と解多重度も共通でなければならない。

## 作用分配次元の剛性

活性モードに加えて、作用を直接受け取る独立な明反応方向が $q$ 個あるとする。固定総作用殻は $q+1$ モードなので、

```math
\Omega_{q+1}(A_i)
\propto
A_i^q.
```

<!-- theorem-start:proposition -->
**命題（直接作用分配次元の剛性）**
共通流束因子の下で、入口重みは

```math
P_i
\propto
\left(
r_i^2\Delta V
\right)^q.
```

Born 型の線形則を得るには $q=1$ が必要である。
<!-- theorem-end:proposition -->

この結果は、任意に多数の比較器または明反応座標を追加できないことを示す否定的結果である。追加自由度が作用を直接分配せず、共通 spectator因子としてだけ現れるなら線形則を壊さない。

## 2モード殻の等方混合

排他的チャンネル $i$ で、選択された活性モードと共有明反応座標を

```math
a_i
=
\begin{pmatrix}
a_{{\rm A},i}\\
a_{\rm R}
\end{pmatrix}
```

とする。2モード総作用は

```math
A_i
=
a_i^\dagger a_i.
```

暗モード $z_{\rm D}$ が殻接方向だけを混ぜる候補 Hamiltonian を

```math
H_{\rm mix}^{(i)}
=
\varepsilon_{\rm mix}
\chi_i(X)
\sum_\alpha
\xi_\alpha(z_{\rm D})
a_i^\dagger T_\alpha a_i
```

とする。$T_\alpha$ は $u(2)$ の Hermitian 生成子である。

```math
\left\{
A_i,
H_{\rm mix}^{(i)}
\right\}
=
0
```

なので、暗モードが混合を駆動しても2モード総作用は保存される。暗モードへ作用を直接移す座標結合は、$K_i+I=A_i$ を壊すため採用しない。

Born 側で必要なのは、各排他的sectorの2モード殻全体に対する $U(2)$ 等方性である。これは第6章の Bell 側で「残余2モードの $U(2)$ だけでは不足する」という結果と矛盾しない。

- Born 側の $U(2)$ は、重みを比較する2モード殻全体へ作用する。
- Bell 側の残余 $U(2)$ は、固定 $J_+$ のファイバー内部だけへ作用し、異なる $J_+$ 間の質量を決めない。
- Bell 側では $J_+$ を含む3モード全殻の $U(3)$ 準備が必要である。

## 一般 Born 則との区別

本章の結果は次に限定される。

1. 位置入口チャンネルの標本頻度である。
2. 2モード作用殻と1つの直接作用分配方向を使う。
3. チャンネル間で流束因子が共通である。
4. 入口前に $A_i=A_{\rm tot}r_i^2\Delta V$ が準備されている。
5. 入口履歴を事後的に捨てない。

任意基底、一般の射影測定、連続スペクトルの有限分解能、複合系の一般 Born 則は示していない。それでも、確率重みを場強度の定義として置かず、作用殻の次元と Liouville 流束から位置重みを出した点で部分達成である。

## 標本化後の再埋め込み問題

2モード殻を混合すると、活性側に残る作用 $K_i$ は一般に標本化前の値と異なる。そのままでは、入口重みを与えた $r_{\rm in}$ と、その後の位相接続力学を担う $r$ が一致しない。

完全周期には、

1. 結果情報を暗モードまたは記録器へ可逆に転送する。
2. 活性場を同じ coherent部分空間へ再埋め込みする。
3. 共有明反応座標を基準状態へ戻す。
4. 全位相作用 $\mathcal J_\phi$ と規格化を保つ。
5. 結果別に履歴を捨てず、次試行を同じ準備分布から始める。

ことが必要である。再埋め込み誤差を

```math
\varepsilon_{\rm reset}
```

とする。本章は $\varepsilon_{\rm reset}$ を有限 Hamiltonian 周期から小さくする構成を与えない。これが現行モデルの最大の未解決問題である。

# 第II部　配置拡散経路と境界作用殻統計

# 運動量結合による配置拡散経路

> **位置づけ：** 運動量2次形式、配置流束、線形誘導場の消去、二側 Markov 拡散内部の Fisher 構造は厳密結果である。有限誘導場からの Brown 極限、配置 Markov 閉鎖、位相接続経路との同時実現は未完成である。


## この経路を残す理由

第3章は coherent縮約多様体上で Schrödinger 型PDEを閉じるが、粒子が実在的な前進・後退 Markov 経路を持つことは示さない。本章の運動量結合経路は、有限 Hamiltonian 誘導場の速度揺らぎから、その確率過程へ進む候補を与える。

両経路は役割を分ける。

- 位相接続経路：作用と有効PDEを与える。
- 運動量結合経路：配置軌道の拡散極限を与える候補である。
- 係数一致と同時実現：独立した未解決問題である。

## 運動量結合した有限誘導場

粒子正準対を $(X,P)$、誘導場正準対を $(Q,\Pi)$ とする。線形核を

```math
H_N^{\rm lin}
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
```

とする。$M_N$ と $K_N$ は正定値実対称行列である。

<!-- theorem-start:proposition -->
**命題（運動量2次形式の成立条件）**
運動量2次形式が正定値であるための必要十分条件は

```math
M_N^{-1}
-
mC_N^{\mathsf T}C_N
>
0
```

である。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
左上ブロック $m^{-1}I_d$ は正定値である。ブロック行列の Schur 補条件を適用する。
<!-- theorem-end:proof -->

Hamilton 方程式は

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
-K_NQ.
```

従って配置速度は

```math
U_N
=
\frac Pm
+
Y_N,
\qquad
Y_N
=
C_N\Pi.
```

正準運動量 $P$ と機械的運動量 $m\dot X$ は一致しない。

## 時間反転と配置流束

標準時間反転

```math
(P,\Pi)
\mapsto
(-P,-\Pi)
```

の下で運動量2次形式は不変である。$V$ と場ポテンシャルが座標だけに依存すれば、有限閉鎖核は時間反転対称である。

全 Liouville 密度を $F_N(X,P,Q,\Pi,t)$、配置周辺密度を

```math
\rho_N(x,t)
=
\int
F_N
\,dP\,dQ\,d\Pi
```

とする。Liouville 方程式を内部変数で積分すると、

```math
\partial_t\rho_N
+
\nabla\cdot
\left(
\rho_Nv_N
\right)
=
0,
```

```math
v_N
=
\mathbb E_N
\left[
\frac Pm+C_N\Pi
\mid
X=x
\right].
```

$P/m$ だけを配置速度としてはならない。

## 線形誘導場の正確な消去

質量規格化した場座標で、正定値周波数行列を $\Omega_N$ とする。指定初期値問題の解を粒子運動量から独立な自由解と強制解へ分けると、

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
\,ds.
```

第1項は初期誘導場に由来する自由速度揺らぎ、第2項は粒子から場への反作用速度記憶である。

指定した Gauss 型初期集団で、場のエネルギー尺度を $\Theta_N$ とすると、

```math
R_N(t-s)
=
\mathbb E
\left[
Y_N^{\rm free}(t)
\otimes
Y_N^{\rm free}(s)
\right]
```

```math
=
\Theta_N
C_N
\cos
\left[
\Omega_N(t-s)
\right]
C_N^{\mathsf T}.
```

有限 $N$ では相関は余弦関数の有限和である。厳密な OU 相関や無限時間の Brown 運動ではない [12--14]。

二側境界条件を用いる場合、自己共役な境界値問題では Green 核が時間交換対称になる。しかし、自己共役 Green 核だけから Nelson の時間対称平均加速度は従わない。

## 再帰前の Brown 極限

目標とする観測窓は

```math
\tau_{\rm corr}
\ll
T_{\rm obs}
\ll
T_{\rm rec}.
```

多数モード、短記憶、適切なスペクトル包絡、弱い外部交換の下で、

```math
\int_0^t
Y_N^{\rm free}(s)
\,ds
\Longrightarrow
\sqrt{2\nu_{\rm bath}}\,W_t
```

を示す必要がある。

反作用記憶項も同時に、

```math
\int_0^t
K_N(t-s)P(s)
\,ds
=
\delta m\,\dot X(t)
+
B_{\rm loc}(X_t,P_t)
+
\mathcal R_{\rm mem}(t)
```

のように、質量繰り込み、局所ドリフト、制御可能な残差へ分けなければならない。有限再帰、異方性、非 Gauss 性、外部交換を同じ上界で制御する定理は未完成である。

## 位相空間極限と配置 Markov 閉鎖

最初の有効候補は

```math
dX_t
=
\frac{P_t}{m}\,dt
+
\sqrt{2\nu_{\rm bath}}\,dW_t,
```

```math
dP_t
=
-\nabla V(X_t)\,dt
+
B_{\rm loc}(X_t,P_t)\,dt.
```

$(X,P)$ が Markov でも、$X$ だけの射影は一般に Markov ではない。配置変数だけの前進・後退拡散

```math
dX_t
=
b_+(X_t,t)\,dt
+
\sqrt{2\nu_{\rm bath}}\,dW_t^+,
```

```math
dX_t
=
b_-(X_t,t)\,dt
+
\sqrt{2\nu_{\rm bath}}\,dW_t^-
```

を得るには、運動量緩和、条件付き速度分散、記憶残差を消去する追加の時間尺度分離が必要である。

## 二側配置拡散内部の Fisher 構造

共通の正の密度 $\rho$ と共通の等方拡散係数 $\nu_{\rm bath}$ を持つ前進・後退 Markov 拡散が得られたとする。現在速度 $v$ と浸透速度 $u$ を

```math
v
=
\frac{b_++b_-}{2},
\qquad
u
=
\frac{b_+-b_-}{2}
```

と定める。前後 Fokker--Planck 方程式の差から、

```math
u
=
\nu_{\rm bath}
\nabla\log\rho.
```

従って、

```math
\frac m2
\int
\rho|u|^2
\,dx
=
\frac{
m\nu_{\rm bath}^2
}{
2
}
\int
\frac{
|\nabla\rho|^2
}{
\rho
}
\,dx
```

である。量子ポテンシャルに対応する項は

```math
Q_{\rm bath}[\rho]
=
-2m\nu_{\rm bath}^2
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
```

これは二側 Markov 拡散を仮定した補助模型内部の厳密結果である。

## 位相接続経路との係数整合

第3章の作用係数は

```math
\hbar_{\rm eff}
=
|\mathcal J_\phi|.
```

本章の Fisher 係数が同じ量子ポテンシャルを与えるには、

```math
|\mathcal J_\phi|
=
2m\nu_{\rm bath}.
```

同値に、

```math
\nu_{\rm bath}
=
\frac{
|\mathcal J_\phi|
}{
2m
}.
```

この一致は重要な反証条件である。位相作用と浴拡散係数を独立に測り、上式が成立しなければ、2経路は同じ有効理論を表さない。

## 時間対称 Newton 則との関係

配置拡散と Fisher 項だけから

```math
ma_{\rm ts}
=
-\nabla V
```

は従わない。時間対称 Green 応答、反作用記憶、条件付き変分からこの Newton 則へ進む問題は未解決である。

一方、第3章では、位相接続縮約作用の変分から同値な Madelung 動力学を得た。後者は、前者の確率過程導出を代替しない。

## 本章の結論

運動量結合した有限誘導場では、正定値条件、時間反転対称性、正確な配置流束、自由速度揺らぎと反作用記憶の分離を得る。二側配置 Markov 拡散が得られた後の浸透速度と Fisher 項も厳密である。

未解決なのは、有限誘導場からの Brown 極限、配置 $X$ だけの Markov 閉鎖、条件付き速度分散の抑制、時間対称 Newton 則、位相接続経路との係数一致と同時実現である。

# 3モード境界作用殻と誘導場内部混合による等方準備

> **位置づけ：** 和・差作用、U(2) の不足、U(3) 不変測度、共通殻の周辺密度、残余ファイバー体積は厳密結果である。同じ誘導場からの全殻等方拡散と半径安定化の導出は未解決である。


## 和・差作用の余弦幾何

生成源が準備する2つの伝達ベクトルを

```math
u_A^{(0)}
=
r_A n(\Theta_A),
\qquad
u_B^{(0)}
=
r_B n(\Theta_B),
```

```math
n(\Theta)
=
\begin{pmatrix}
\cos\Theta\\
\sin\Theta
\end{pmatrix}
```

とする。付録Cの局所記録後には

```math
u_A
=
A r_A R[\phi(a)]n(\Theta_A),
```

```math
u_B
=
B r_B R[\phi(b)]n(\Theta_B)
```

となる。$A,B\in\{-1,+1\}$ は局所固定指針に記録済みである。

相対角を

```math
\Delta_{ab}
=
\phi(a)-\phi(b)+\Theta_A-\Theta_B
```

とする。和・差作用は

```math
I_+^{AB}
=
\frac14
\left\|
u_A+u_B
\right\|^2,
```

```math
I_-^{AB}
=
\frac14
\left\|
u_A-u_B
\right\|^2
```

である。直接展開すると、

```math
I_\pm^{AB}
=
\frac14
\left[
r_A^2+r_B^2
\pm
2ABr_Ar_B\cos\Delta_{ab}
\right].
```

<!-- theorem-start:proposition -->
**命題（和・差作用の余弦恒等式）**
等振幅 $r_A=r_B=r$、固定相対生成源位相の下で、

```math
I_\pm^{AB}
=
I_0
\left[
1
\pm
AB\cos\Delta_{ab}
\right],
\qquad
I_0=\frac{r^2}{2}.
```

さらに、

```math
I_+^{AB}+I_-^{AB}=2I_0
```

である。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
2つのベクトルの内積は

```math
u_A\cdot u_B
=
ABr^2\cos\Delta_{ab}.
```

これを和ベクトルと差ベクトルの2乗へ代入すればよい。和と差を加えると内積項が消える。
<!-- theorem-end:proof -->

位相雑音 $\delta$ を許し、その分布が設定と結果符号に依存しないとする。重みが $I_\pm$ に線形であるため、位相を先に平均できる。可視度 $0\leq V\leq1$ と位相ずれを $\Delta_{ab}$ へ吸収すれば、

```math
\overline I_\pm^{AB}
=
I_0
\left[
1
\pm
ABV\cos\Delta_{ab}
\right].
```

総入力作用は平均後も $2I_0$ である。振幅揺らぎを許す場合は、各試行で $I_++I_-$ が固定される範囲に中心定理を限定する。総作用自体の揺らぎは第8章の殻幅誤差へ含める。

## 3モード共通作用殻

境界3モードを

```math
a_\nu
=
\frac{
q_\nu+ip_\nu
}{
\sqrt2
},
\qquad
J_\nu=|a_\nu|^2,
\qquad
\nu\in\{+,s,r\}
```

とする。作用角変数では

```math
q_\nu
=
\sqrt{2J_\nu}\cos\theta_\nu,
\qquad
p_\nu
=
\sqrt{2J_\nu}\sin\theta_\nu,
```

```math
dq_\nu\,dp_\nu
=
dJ_\nu\,d\theta_\nu.
```

総作用を

```math
C
=
J_++J_s+J_r
```

とする。固定値 $C_0>0$ の共通作用殻上の Liouville 測度は

```math
d\mu_{C_0}
=
\frac{
\delta
\left(
C_0-J_+-J_s-J_r
\right)
\prod_{\nu}
dJ_\nu\,d\theta_\nu
}{
\Omega_3(C_0)
},
```

```math
\Omega_3(C_0)
=
\frac{
(2\pi)^3C_0^2
}{
2
}.
```

これは第4章の一般式

```math
\Omega_n(A)
=
\frac{(2\pi)^n}{(n-1)!}
A^{n-1}
```

の $n=3$ の場合である。Born 側では2モード全殻の線形容量を用い、本章では3モード全殻を固定 $J_+$ で切った残余2モードの線形容量を用いる。

複素3成分ベクトル $a=(a_+,a_s,a_r)^{\mathsf T}$ で見れば、この殻は

```math
a^\dagger a=C_0
```

という5次元球面である。

局所記録と静的和・差変換が与える境界適合条件は

```math
J_+=I_+^{AB}(a,b).
```

従って結果セクター $(A,B)$ に残る作用は

```math
C_0-I_+^{AB}
=
J_s+J_r.
```

$C_0=J_*+2I_0$ とすれば、

```math
C_0-I_+^{AB}
=
J_*+I_-^{AB}.
```

この恒等式は作用保存だけから従う。相対確率を得るには、異なる $J_+$ のファイバーにどの測度を置くかを決めなければならない。

## 残余2モードの U(2) 等方性では不足する

固定 $J_+=x$ の下では、残余2モードは

```math
J_s+J_r=C_0-x
```

という3次元球面を作る。$(a_s,a_r)$ に $U(2)$ が作用すると、この球面上で推移的である。従って、固定 $x$ の内部では正規化された $U(2)$ 不変測度が一意になる。

この事実から、

```math
p
\left(
J_s\mid J_+=x
\right)
=
\frac{
1
}{
C_0-x
},
\qquad
0\leq J_s\leq C_0-x
```

という一様作用分配が従う。しかし、これは各ファイバー内部の条件付き分布であり、異なる $x$ のファイバー間の相対質量を決めない。

<!-- theorem-start:proposition -->
**命題（U(2) 等方性の不足）**
任意の非負可積分関数 $f$ に対し、

```math
d\mu_f
\propto
f(J_+)
\delta
\left(
C_0-J_+-J_s-J_r
\right)
\prod_\nu dJ_\nu\,d\theta_\nu
```

は、残余2モード $(a_s,a_r)$ に関して $U(2)$ 不変である。しかし、$J_+=x$ のファイバー質量は

```math
W_f(x)
\propto
f(x)(C_0-x)
```

となる。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
$f(J_+)$ は残余2モードの回転で変化しない。固定 $J_+=x$ で角変数を積分し、$J_r$ のデルタ関数積分を行うと、

```math
\int_0^{C_0-x}dJ_s
=
C_0-x
```

が残る。従って任意の $f(x)$ がファイバー間の相対質量へ残る。
<!-- theorem-end:proof -->

従って、残余2モードの等方性だけから Bell 重みを導くことはできない。必要なのは、$J_+$ を含む3モード共通殻全体の測度である。

## U(3) 不変測度

$U(3)$ は $a^\dagger a=C_0$ の球面上へ推移的に作用する。従って、正規化された $U(3)$ 不変確率測度は一意であり、固定作用殻の Liouville 測度 $d\mu_{C_0}$ と一致する。

<!-- theorem-start:proposition -->
**命題（共通殻不変測度の一意性）**
$S_{C_0}^5=\{a\in\mathbb C^3:a^\dagger a=C_0\}$ とする。$S_{C_0}^5$ 上の正規化 Borel 測度が全ての $U(3)$ 変換に不変なら、その測度は $d\mu_{C_0}$ に等しい。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
$U(3)$ は球面上で推移的であり、安定部分群は $U(2)$ である。従って球面は同次空間 $U(3)/U(2)$ と同一視できる。コンパクト群の正規化 Haar 測度を商空間へ押し出した測度は不変である。不変確率測度の平均作用を用いれば一意性が従う。作用角変数で書けば、その押し出しは $d\mu_{C_0}$ である。
<!-- theorem-end:proof -->

固定された損失のない3入力3出力接合部は $U(3)$ 変換を1つ実行するだけであり、単一の入力位相点を殻全体へ広げない。上の命題は不変測度の一意性を述べるのであって、Hamilton 方程式が確率測度を無から生成することを述べない。

## 誘導場内部混合による全殻等方拡散

境界3モードの準備窓で、構造化誘導場の多数の未読自由度と非線形内部混合を消去した縮約方程式を考える。理想的な殻接方向生成子を

```math
\mathcal L_{\rm iso}
=
D_\partial\Delta_{S^5},
\qquad
D_\partial>0
```

とする。$\Delta_{S^5}$ は固定作用殻の Laplace--Beltrami 作用素である。

この接方向生成子は、常時の外部漏れを直接拡散へ読み替えたものではない。Hamiltonian な内部混合が殻方向を探索し、弱い外部交換は欠陥除去、有限再帰の抑制、半径分布の維持を担う。2つの効果を同じ係数へまとめない。

<!-- theorem-start:theorem -->
**定理（等方殻拡散の定常測度）**
連結な固定作用殻 $S_{C_0}^5$ 上で

```math
\partial_t f
=
D_\partial\Delta_{S^5}f
```

を考える。規格化された非負密度の定常解は定数だけであり、$d\mu_{C_0}$ が一意な定常確率測度である。初期密度が $L^2$ なら、

```math
\left\|
f_t-1
\right\|_{L^2(d\mu_{C_0})}
\leq
e^{-D_\partial\lambda_1t}
\left\|
f_0-1
\right\|_{L^2(d\mu_{C_0})},
```

ここで $\lambda_1>0$ は殻上 Laplacian の第1非零固有値である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
定常密度 $f$ に対し、部分積分から

```math
\int
f\Delta_{S^5}f\,d\mu_{C_0}
=
-
\int
\left|
\nabla_{S^5}f
\right|^2
d\mu_{C_0}.
```

左辺は0なので、連結性から $f$ は定数である。規格化により $f=1$ となる。時間発展については定数成分を除いた固有関数展開を用い、第1非零固有値で評価する。
<!-- theorem-end:proof -->

混合不足の尺度を

```math
\varepsilon_{\rm mix}
=
\exp
\left(
-D_\partial\lambda_1\tau_{\rm prep}
\right)
```

とする。$\varepsilon_{\rm mix}\ll1$ なら、滑らかな観測量について初期の方向偏りは小さくなる。

有限 Hamiltonian 浴からこの拡散を得る候補は、$U(3)$ の Hamiltonian 生成子を、等方な相関行列を持つ浴変数へ弱く結合することである。弱結合・短相関時間極限では、2次の縮約生成子が $U(3)$ の Casimir 作用素へ近づく。付録Cに具体形を示す。

ただし、有限閉鎖 Hamiltonian 流れは微細 Liouville 密度を保存し、一般には $L^1$ で一様密度へ収束しない。有限浴だけで主張できるのは、有限時間・有限分解能の混合または弱い観測量収束である。不可逆な一意定常分布を用いる場合は、常時の弱い外部交換まで含む縮約が必要である。

## 異方性と半径方向の弱開放補正

現行の縮約生成子を

```math
\mathcal L
=
D_\partial\Delta_{S^5}
+
\varepsilon_{\rm aniso}\mathcal L_{\rm aniso}
+
\mathcal L_C
```

と分ける。$\mathcal L_{\rm aniso}$ は殻接方向の異方成分、$\mathcal L_C$ は総作用 $C$ の半径方向変化を表す。

半径方向の有効式の候補を

```math
dC_t
=
-\gamma_C
\left(
C_t-C_0
\right)dt
+
\sqrt{2D_C}\,dW_t
```

とする。これは、外部への漏れと仕事貯蔵系または微小揺らぎからの流入が $C_0$ 付近で釣り合う線形化である。定常幅は

```math
\sigma_C^2
=
\frac{D_C}{\gamma_C},
\qquad
\varepsilon_C
=
\frac{\sigma_C}{C_0}.
```

$\varepsilon_C\ll1$ なら、固定殻計算を狭い準定常殻へ適用できる。純粋な漏れ

```math
\dot C=-\gamma_C C
```

だけでは、$C=0$ へ落ちるだけで $C_0>0$ の定常殻を作らない。

異方性と半径幅が小さく、境界ファイバーが殻端から離れていれば、滑らかな結果重みの補正を

```math
O
\left(
\varepsilon_{\rm aniso}
+
\varepsilon_{\rm mix}
+
\varepsilon_C
\right)
```

と整理できる。全係数を同じ有限浴の尺度から与える一様上界は未完成であるため、現行モデルへの接続は近似結果である。

## 共通殻の周辺密度

<!-- theorem-start:theorem -->
**定理（和モード作用の周辺密度）**
3モード固定作用殻の正規化 Liouville 測度について、$J_+=x$ の周辺密度は

```math
p_+(x)
=
\frac{
2(C_0-x)
}{
C_0^2
}
\mathbf1_{\{0\leq x\leq C_0\}}.
```
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
角変数を積分すると $(2\pi)^3$ を得る。$J_+=x$ を固定した未規格化密度は

```math
(2\pi)^3
\int_0^\infty dJ_s
\int_0^\infty dJ_r\,
\delta
\left(
C_0-x-J_s-J_r
\right)
=
(2\pi)^3(C_0-x).
```

これを

```math
\Omega_3(C_0)
=
\frac{
(2\pi)^3C_0^2
}{
2
}
```

で規格化すればよい。
<!-- theorem-end:proof -->

この線形密度が Bell 重みの起源になる。重要なのは、各 $x$ の残余2モード分布を別々に質量1へ規格化しないことである。4つの結果セクターを同じ3モード作用殻の切断として比較する。

## 残余ファイバー体積

結果セクター $(A,B)$ の理想境界条件を

```math
g_{AB}
=
J_+-I_+^{AB}(a,b)
=
0
```

とする。作用座標でこの制約を用いる場合、$|\partial g_{AB}/\partial J_+|=1$ であり、coarea Jacobian は全結果と全設定に共通である。

<!-- theorem-start:proposition -->
**命題（残余ファイバーの線形体積）**
$0<I_+^{AB}<C_0$ とする。固定作用殻と $g_{AB}=0$ の交わりに誘導される未規格化 Liouville 体積は

```math
\Omega_{AB}
=
(2\pi)^3
\left(
C_0-I_+^{AB}
\right)
```

に比例する。共通定数を除けば、

```math
W_{AB}
\propto
C_0-I_+^{AB}
=
J_*+I_-^{AB}.
```
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
$J_+=I_+^{AB}$ を固定し、$J_r$ のデルタ関数積分を行う。許される $J_s$ は

```math
0\leq J_s\leq C_0-I_+^{AB}
```

なので、その長さが残る。3つの角変数は共通因子 $(2\pi)^3$ を与える。
<!-- theorem-end:proof -->

一般の境界写像では、解集合自体を無条件にシンプレクティック多様体と呼ばない。全境界正準位相空間の Liouville 測度を、作用殻と境界適合写像で制限して得る誘導測度として定義する。複数解、分岐、caustic がある場合は、Jacobianと多重度を含める必要がある。

## 有限分解能

現実の境界適合条件には幅 $\delta_J>0$ がある。共通窓関数 $K_{\delta_J}$ を用い、

```math
K_{\delta_J}
\left(
J_+-I_+^{AB}
\right)
```

で制限する。$I_+^{AB}$ が殻端から $\delta_J$ より十分離れ、$K_{\delta_J}$ が全結果に共通なら、

```math
W_{AB}^{(\delta_J)}
=
c_{\delta_J}
\left(
C_0-I_+^{AB}
\right)
+
O
\left(
\frac{\delta_J^2}{C_0}
\right).
```

$c_{\delta_J}$ は全セクターに共通で規格化時に消える。窓幅または Jacobian が結果や設定に依存する場合は、余分な重みを直接導入するため認めない。

## 本章の結論

残余2モードの $U(2)$ 等方性は、固定 $J_+$ のファイバー内部を一様にするだけで、ファイバー間の質量を決めない。この不足は任意関数 $f(J_+)$ を用いた反例で厳密に示せる。

3モード全体の $U(3)$ 等方性は共通作用殻上の測度を一意に決める。縮約された等方拡散では、その測度が一意な定常分布になる。固定殻の $J_+$ 周辺は $C_0-J_+$ に比例し、境界条件 $J_+=I_+^{AB}$ を課した残余ファイバー体積は

```math
W_{AB}
\propto
J_*+I_-^{AB}
```

となる。

固定殻の幾何と縮約拡散の定常測度は、指定した補助モデル内で厳密である。一方、同じ構造化有限浴と常時の弱い外部交換から、非退化な $U(3)$ 等方生成子、混合時間、異方誤差、殻幅を導くことは未完成である。次章では、共通殻の誘導測度を履歴空間へ押し出し、Bell 型共同確率と前提違反を計算する。

# 境界作用殻測度からの Bell 型共同法則

> **位置づけ：** 全境界正準位相空間の Liouville 測度を共通殻と境界適合で条件づけた後の共同確率は厳密結果である。全殻測度のミクロな準備、境界適合の装置実現、一般測定器は予想・未解決である。


## 履歴測度の定義

第6章で得た Liouville 測度は、境界3モードの正準位相空間上にある。Bell 実験の結果確率として用いるには、その測度を完結履歴の空間へ移す必要がある。

初期側の生成源、設定制御器、局所装置、指針、誘導場暗モードをまとめて $\lambda$ とし、境界3モードを $\eta=(a_+,a_s,a_r)$ とする。設定制御器の巨視領域が $a,b$ を定め、局所 Hamiltonian 流れが結果 $A,B$ と伝達ベクトル $u_A,u_B$ を定める。

全境界正準位相空間の基準測度を

```math
d\mu_0
=
\rho_{\rm prep}(\lambda)
d\lambda\,
d\mu_{C_0}(\eta)
```

とする。ここで $d\mu_{C_0}$ は3モード共通作用殻の正規化 Liouville 測度である。結果セクターを

```math
\Sigma_{AB}
=
\left\{
\lambda:
A(\lambda,a)=A,\,
B(\lambda,b)=B
\right\}
```

とする。

境界適合写像を

```math
g_{AB}^{a,b}(\lambda,\eta)
=
J_+(\eta)
-
I_+^{AB}(a,b;\lambda)
```

とする。理想境界条件は $g_{AB}^{a,b}=0$ である。有限分解能では、全セクターに共通な窓関数 $K_{\delta_J}$ を用いる。

設定 $(a,b)$ の履歴測度は、$d\mu_0$ を $\Sigma_{AB}$ と境界適合窓で制限し、Hamiltonian の解写像

```math
\mathcal F_{a,b}:
(\lambda,\eta)
\longmapsto
\gamma_{a,b}
```

により履歴空間へ押し出して定める。記号的には、

```math
d\mu_{\rm hist}^{a,b}
\propto
\left(
\mathcal F_{a,b}
\right)_\#
\left[
\rho_{\rm prep}(\lambda)
K_{\delta_J}
\left(
g_{AB}^{a,b}
\right)
d\lambda\,
d\mu_{C_0}(\eta)
\right].
```

この定義で数えるのは、解集合そのものに無条件で置いた Liouville 体積ではない。全境界正準位相空間の Liouville 測度を、作用保存と境界適合条件で制限し、解写像で履歴空間へ押し出した測度である。

## 結果セクターの基準対称性

共通作用殻が決めるのは、各境界適合ファイバーの作用体積である。局所結果セクター自体の基準質量は、準備対称性から別に決める。

境界条件を課す前の質量を

```math
w_{AB}
=
\int_{\Sigma_{AB}}
\rho_{\rm prep}(\lambda)\,d\lambda
```

とする。左右の結果符号を独立に反転する測度保存対合を

```math
\mathcal S_A:
\Sigma_{AB}
\longrightarrow
\Sigma_{-A,B},
```

```math
\mathcal S_B:
\Sigma_{AB}
\longrightarrow
\Sigma_{A,-B}
```

とする。$\mathcal S_A,\mathcal S_B$ が準備 Hamiltonian、準備巨視領域、$\rho_{\rm prep}d\lambda$ を保つなら、

```math
w_{++}
=
w_{+-}
=
w_{-+}
=
w_{--}
=
\frac14.
```

Hamiltonian の形式が符号反転対称なだけでは不十分である。同じ Hamiltonian に非対称な準備密度を置けるため、準備巨視領域と基準測度まで対称でなければならない。

## 結果の未規格化質量

理想境界条件と共通 Jacobian の下で、結果 $(A,B)$ の未規格化質量は

```math
\widetilde W_{AB}
=
w_{AB}
\int
\delta
\left(
C_0-J_+-J_s-J_r
\right)
\delta
\left(
J_+-I_+^{AB}
\right)
\prod_\nu dJ_\nu\,d\theta_\nu.
```

第6.8節の計算から、

```math
\widetilde W_{AB}
\propto
w_{AB}
\left(
C_0-I_+^{AB}
\right).
```

$C_0=J_*+2I_0$ と $I_++I_-=2I_0$ を用いれば、

```math
\widetilde W_{AB}
\propto
w_{AB}
\left(
J_*+I_-^{AB}
\right).
```

ここで $J_*$ は結果と設定に依存しない基準作用である。$J_*$ は、境界ファイバーが全結果で正の幅を持つための余裕でもある。$J_*$ が大きいほど角度依存の可視度は低下する。

有限分解能では、

```math
\widetilde W_{AB}^{(\delta_J)}
=
c_{\delta_J}
w_{AB}
\left(
C_0-I_+^{AB}
\right)
+
O
\left(
w_{AB}
\frac{\delta_J^2}{C_0}
\right).
```

$c_{\delta_J}$ が全結果と全設定に共通なら規格化で消える。結果ごとに異なる窓幅を用いると、欲しい重みを装置分解能へ直接書き込むことになる。

## Bell 型共同確率

位相雑音を平均した差作用を

```math
\overline I_-^{AB}
=
I_0
\left[
1
-
ABV\cos\Delta_{ab}
\right]
```

とする。$[S]$ の対称準備により $w_{AB}=1/4$ とする。

<!-- theorem-start:theorem -->
**定理（境界作用殻からの Bell 型共同法則）**
次を仮定する。

1. 境界3モードは1つの共通作用殻 $C_0=J_*+2I_0$ 上の Liouville 測度を持つ。
2. 4つの結果セクターの基準質量は等しい。
3. 境界条件は $J_+=I_+^{AB}$ であり、分解能と coarea Jacobian は全結果・全設定に共通である。
4. 生成源は固定総入力作用と可視度 $V$ を持つ。

このとき、

```math
P(A,B\mid a,b)
=
\frac14
\left[
1
-
V_{\rm eff}
AB\cos\Delta_{ab}
\right],
```

```math
V_{\rm eff}
=
\frac{
I_0
}{
J_*+I_0
}V.
```
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
未規格化質量は

```math
\widetilde W_{AB}
\propto
\frac14
\left[
J_*+I_0
-
AB I_0V\cos\Delta_{ab}
\right].
```

4セクターについて和を取ると、$AB$ に奇な項が消え、

```math
\sum_{A,B}
\widetilde W_{AB}
\propto
J_*+I_0.
```

従って各質量を総和で割れば主張を得る。
<!-- theorem-end:proof -->

$J_*=0$ かつ $V=1$ なら、

```math
P(A,B\mid a,b)
=
\frac14
\left[
1
-
AB\cos\Delta_{ab}
\right].
```

$J_*>0$ または $V<1$ なら、同じ余弦形で可視度が低下する。

## CHSH 値

相関関数は

```math
E(a,b)
=
\sum_{A,B}
AB
P(A,B\mid a,b)
=
-V_{\rm eff}\cos\Delta_{ab}.
```

標準的な4設定を選ぶと、

```math
|S_{\rm CHSH}|
=
2\sqrt2\,V_{\rm eff}.
```

従って CHSH 超過の条件は

```math
V_{\rm eff}
>
\frac1{\sqrt2}.
```

小さい補正 $\varepsilon_{\rm Bell}$ が相関へ一様に加わる場合、十分な超過余裕を持つには

```math
2\sqrt2\,V_{\rm eff}
-
2
\gg
O(\varepsilon_{\rm Bell})
```

が必要である。誤差の内訳は第8章で整理する。

## 非信号性

対称な共同確率をBについて和を取ると、

```math
\sum_B
P(A,B\mid a,b)
=
\frac12.
```

同様に、

```math
\sum_A
P(A,B\mid a,b)
=
\frac12.
```

従って一側周辺は反対側の設定に依存しない。この非信号性は、次の条件に依存する。

- $w_{AB}=1/4$。
- 共通の境界分解能。
- 共通の coarea Jacobian。
- $J_*$ と総入力作用が結果・設定に依存しない。
- 位相雑音と殻幅の分布が左右符号反転に不変。

これらが崩れる場合、一側周辺に残差が現れ得る。任意の偏った準備に対して非信号性が動的に回復することは示していない。

## 測定設定独立性

Bell の測定設定独立性は、完全な隠れた変数または履歴変数 $\Lambda$ の分布が

```math
\rho
\left(
\Lambda\mid a,b
\right)
=
\rho(\Lambda)
```

を満たすことを要求する。本モデルでは境界適合条件が

```math
J_+
=
I_+^{AB}(a,b)
```

であり、許容される残余ファイバーが設定によって変わる。従って、

```math
\rho_{\rm hist}
\left(
\Lambda\mid a,b
\right)
\neq
\rho_{\rm hist}(\Lambda)
```

が一般に成り立つ。

測定設定依存性は、初期密度へ結果式を直接書き込むことからではなく、同じ共通作用殻を設定依存の境界適合面で切ることから生じる。局所結果形成時に反対側の設定が Hamilton 方程式へ入ることを意味しない。

この構成は Bell の定理を否定しない。Bell 不等式を超えるために必要な前提違反を、完結履歴の測定設定独立性の破れとして明示する。

## 事後選別との区別

境界条件に適合しない軌道は、本理論上は実験後に捨てた記録済み試行ではなく、最初から指定した2境界値問題の解ではない。しかし、数学上の定義だけでは、実験装置が事後選別なしにその履歴集団を実現することを保証しない。

操作上は、少なくとも次を結果別・設定別に監査する。

1. 外部から与えた開始信号数。
2. 左右の局所指針が形成した記録数。
3. 境界段階まで完了した試行数。
4. 次試行へ再初期化できた回数。
5. 記録形成、殻準備、消去に要した時間と交換エネルギー。
6. 境界分解能と作用殻幅。

観測済み試行の一部を結果または設定に依存して除外しなければ Bell 値が出ない場合、本構成は検出事後選別へ退化する。開始数、記録数、完了数が共通係数だけで異なるなら、共同確率の規格化には影響しない。

## Bell 前提の一覧

| 前提または条件 | 本モデルでの地位 |
|---|---|
| 局所 Hamiltonian 応答 | 局所測定窓で $O(\varepsilon_{\rm loc})$ まで成立 |
| 結果の一意性 | 最小結果符号化器では成立。一般測定器は未構成 |
| 測定設定独立性 | 境界適合ファイバーの設定依存性により成立しない |
| 非信号性 | 対称準備と共通分解能の下で厳密 |
| 事後選別の不在 | 理論上は2境界解集合。装置実現では開始・記録・完了数の監査が必要 |
| 共通試行測度 | 全殻等方拡散の定常測度として縮約レベルで導出 |
| 全殻拡散のミクロ生成 | 予想・未解決 |

局所性と測定設定独立性を同じ条件として扱わない。局所 Hamilton 方程式の交差応答が小さくても、完結履歴の条件付き測度は設定に依存し得る。

## 旧終端関数との置換関係

旧構成では、基準初期密度へ終端関数を引き戻して

```math
\rho_{\rm old}
\propto
\rho_S
G_R\circ\Phi_{a,b}^{T}
```

とし、終端半空間の体積を Bell 重みへ変換していた。この構成では、Bell 固有の終端統計原理を独立入力として必要とした。

現構成では、

```math
d\mu_{C_0}
\longrightarrow
J_+=I_+^{AB}
\longrightarrow
W_{AB}
\propto
C_0-I_+^{AB}
```

という1つの共通作用殻の切断を用いる。設定名、結果名、目標相関を引数に持つ終端関数はない。中央比較器と相補時計も用いない。

ただし、これは境界条件付けを消したのではない。共通未来で $J_+=I_+^{AB}$ を要求し、許容履歴の測度を数える点で2境界構造は残る。未解決問題は、Bell 固有の終端関数の生成から、同じ構造化浴による全殻等方準備と共通境界適合の物理的実現へ移った。

## 本章の結論

3モード共通作用殻の Liouville 測度を、結果セクターと境界適合条件で制限し、履歴空間へ押し出す測度を定義した。対称な結果セクター、共通分解能、共通 Jacobian の下で、残余ファイバー体積は

```math
W_{AB}
\propto
J_*+I_-^{AB}
```

となり、Bell 型余弦共同確率が厳密に従う。

完全な余弦則には $J_*=0$ と $V=1$、CHSH 超過には $V_{\rm eff}>1/\sqrt2$ が必要である。対称準備では非信号性が成り立つ一方、完全履歴分布は設定に依存する。Bell の前提違反は測定設定独立性にある。

旧来の Bell 固有な終端関数と中央比較器は除いたが、共通未来を含む境界値問題は残る。全殻測度を同じ有限浴から準備すること、一般測定器を構成すること、事後選別なしの試行周期として実装することは未解決である。

# 誤差、適用限界、反証条件、結論

> **位置づけ：** 3つの縮約経路について、厳密結果、近似条件、未解決接続、反証可能な残差を分離する。完成 Hamiltonian と完全周期は未完成である。


## 3経路の導出状態

| 経路 | 本論文で得た結果 | 未完成な接続 |
|---|---|---|
| 位相接続 | 有限セル正準構造、保存位相作用、固定作用下の局所分配、縮約作用、Madelung 方程式、局所 Schrödinger 型PDE、同期差保存、条件付き循環量子化 | coherent多様体の準備・維持、節、係数整合、停留点選択 |
| 配置拡散 | 正定値運動量結合、正確な配置流束、線形浴消去、自由速度相関、二側 Markov 拡散内部の Fisher 項 | Brown 極限、配置 Markov 閉鎖、古典圧力、時間対称 Newton 則 |
| 境界作用殻 | 一般殻容量、Born 型位置入口流束、作用分配次元の剛性、3モード残余ファイバー、Bell 型共同確率、Bell 前提監査 | 等方準備、一般測定器、再埋め込み、再初期化、偏った準備での非信号性 |

補助模型内部の厳密性と、現行の弱開放ミクロ模型から補助模型への接続を混同しない。

## 位相接続側の主要誤差

| 誤差 | 内容 | 理想条件 |
|---|---|---|
| $\varepsilon_{\rm coh}$ | coherent集中からのずれ | 非線形接続を代表場で閉じられる |
| $\varepsilon_\rho$ | $r^2-\rho$ | 入口同期と内部保存 |
| $\varepsilon_j$ | $j-\mathcal J_\phi r^2$ | 固定作用最小配置 |
| $\varepsilon_{\rm radial}$ | 動径慣性と高速振幅モード | 断熱的に小さい |
| $\varepsilon_{\rm press}$ | 条件付き速度分散 | 単流束化 |
| $\varepsilon_\kappa$ | $\kappa-\mathcal J_\phi^2/(2m)$ | Nelson係数一致 |
| $\varepsilon_{\rm node}$ | 節正則化と接続誤差 | 非零領域または制御された極限 |
| $\varepsilon_{\rm cross}$ | 位相活性場と配置拡散浴の交差作用 | 固定部分空間で小さい |

理想縮約方程式の残差を

```math
\mathcal R_{\rm phase}
=
\mathcal R_{\rm coh}
+
\mathcal R_\rho
+
\mathcal R_j
+
\mathcal R_{\rm radial}
+
\mathcal R_{\rm press}
+
\mathcal R_\kappa
+
\mathcal R_{\rm node}
+
\mathcal R_{\rm cross}
```

と分ける。各項を個別に小さくしても、長時間での位相誤差蓄積が小さいとは限らない。観測時間に一様な上界が必要である。

## Born 型入口流束の誤差

理想重みは

```math
P_i^{(0)}
=
r_i^2\Delta V.
```

主要誤差は次である。

| 誤差 | 内容 |
|---|---|
| $\varepsilon_{\rm flux}$ | 法線速度、障壁、coarea Jacobian、解多重度のチャンネル差 |
| $\varepsilon_{\rm mix2}$ | 2モード殻準備の異方性と有限混合時間 |
| $\varepsilon_{\rm action}$ | $A_i-A_{\rm tot}r_i^2\Delta V$ |
| $\varepsilon_{\rm exclusive}$ | 複数入口チャンネルの同時開放 |
| $\varepsilon_{\rm reset}$ | 標本化後の活性場再埋め込みと明反応座標復元 |

直接作用分配方向が $q\neq1$ なら、これは小さい摂動ではなく構造的な変更であり、

```math
P_i
\propto
\left(
r_i^2\Delta V
\right)^q
```

となる。線形 Born 型重みは失われる。

## 配置拡散側の誤差

運動量結合経路の残差を

```math
\mathcal R_{\rm bath}
=
\mathcal R_{\rm spec}
+
\mathcal R_{\rm rec}
+
\mathcal R_{\rm mem}
+
\mathcal R_{\rm nonG}
+
\mathcal R_{\rm nonM}
+
\mathcal R_{\rm aniso}
+
\mathcal R_{\rm open}
```

と分ける。

- $\mathcal R_{\rm spec}$：有限スペクトル包絡と目標相関の差。
- $\mathcal R_{\rm rec}$：有限浴の再帰。
- $\mathcal R_{\rm mem}$：反作用記憶の非局所残差。
- $\mathcal R_{\rm nonG}$：高次 cumulant。
- $\mathcal R_{\rm nonM}$：配置射影の非 Markov 性。
- $\mathcal R_{\rm aniso}$：拡散係数の方向依存。
- $\mathcal R_{\rm open}$：外部流入・流出による補正。

さらに2経路の係数差を

```math
\varepsilon_\nu
=
\frac{
\left|
2m\nu_{\rm bath}
-
|\mathcal J_\phi|
\right|
}{
|\mathcal J_\phi|
}
```

とする。$\varepsilon_\nu$ が零へ近づかない模型では、配置拡散経路と位相接続経路は同じ有効理論へ収束しない。

## Bell 側の誤差

第7章の理想共同法則を

```math
P_0(A,B\mid a,b)
=
\frac14
\left[
1
-
V_{\rm eff}
AB\cos\Delta_{ab}
\right]
```

とする。主要誤差を

```math
\varepsilon_{\rm Bell}
\lesssim
C_{\rm loc}\varepsilon_{\rm loc}
+
C_{\rm aniso}\varepsilon_{\rm aniso}
+
C_{\rm mix}\varepsilon_{\rm mix3}
+
C_C\frac{\sigma_C}{C_0}
+
C_J\delta_J^2
+
C_{\rm jac}\varepsilon_{\rm jac}
+
C_{\rm sec}\varepsilon_{\rm sec}
+
C_{\rm mult}\varepsilon_{\rm mult}
```

と整理する。

- $\varepsilon_{\rm loc}$：左右局所測定窓の全交差応答。
- $\varepsilon_{\rm aniso}$：3モード殻接方向拡散の異方性。
- $\varepsilon_{\rm mix3}$：全殻混合不足。
- $\sigma_C/C_0$：総作用半径の幅。
- $\delta_J$：境界適合の有限分解能。
- $\varepsilon_{\rm jac}$：coarea Jacobian の結果・設定依存。
- $\varepsilon_{\rm sec}$：結果セクター基準質量の非対称。
- $\varepsilon_{\rm mult}$：解多重度と分岐の非共通性。

残余2モードの $U(2)$ 等方性は $\varepsilon_{\rm mix3}$ を制御しない。$J_+$ を含む全3モード殻の準備が必要である。

## CHSH超過と可視度

余弦相関

```math
E(a,b)
=
-V_{\rm eff}\cos\Delta_{ab}
```

に対する標準角では

```math
|S_{\rm CHSH}|
=
2\sqrt2V_{\rm eff}.
```

理想模型が古典限界を超える条件は

```math
V_{\rm eff}
>
\frac1{\sqrt2}.
```

確率誤差が各設定で全変動距離 $\delta_{\rm TV}$ 以下なら、CHSH値のずれは粗く

```math
\left|
\delta S_{\rm CHSH}
\right|
\leq
8\delta_{\rm TV}.
```

従って十分条件は

```math
2\sqrt2V_{\rm eff}
-
8\delta_{\rm TV}
>
2.
```

Tsirelson 限界を一般原理から導いたわけではない。理想余弦則と $V_{\rm eff}\leq1$ の範囲では上限が $2\sqrt2$ になるだけである。

## 否定的結果と適用限界

1. 閉鎖 Hamiltonian 流は、一般に低次元の coherent多様体へ吸引しない。
2. 固定作用下のエネルギー最小配置は、その配置の動力学的準備を意味しない。
3. rank-one 2次モーメントだけでは非線形位相接続の標本平均を閉じない。
4. $\kappa=\mathcal J_\phi^2/(2m)$ は内部回転対称性だけから従わない。
5. 同期差保存は、同期多様体への復元力ではない。
6. 条件付き循環量子化は、節を含む Wallstrom 問題の全面解決ではない [19]。
7. 位置入口の Born 型流束は、任意基底の一般 Born 則ではない。
8. 直接作用分配方向が複数なら、入口重みは一般に $A_i$ の高いべきになる。
9. 暗モードへ作用を直接移す結合は、2モード保存則を壊す。
10. 運動量結合が速度揺らぎを作っても、その積分が Brown 運動へ収束するとは限らない。
11. $(X,P)$ が Markov でも、$X$ だけの射影は一般に Markov ではない。
12. 二側配置拡散から Fisher 項が得られても、時間対称 Newton 則は自動的に従わない。
13. 残余2モードの $U(2)$ 等方性だけでは、Bell 結果ファイバー間の質量を決めない。
14. 固定正準接合部は Liouville 測度を保存するが、一様殻測度を単一状態から生成しない。
15. 純粋な一方向漏れは非零の定常作用殻を準備しない。
16. Bell 型余弦則は、Born 則、位相量子化、一般 Tsirelson 原理を単独では導かない。

## 反証に使える観測量

現行模型は次の量で反証または制約できる。

- coherent集中誤差と活性場2次モーメントの非 rank-one 成分。
- $j-\mathcal J_\phi r^2$ と $r^2-\rho$ の時間発展。
- $\kappa-\mathcal J_\phi^2/(2m)$。
- 巻数と粒子流速循環の不一致。
- チャンネル別の法線流束因子 $\lambda_i$。
- 入口頻度の $r_i^2\Delta V$ からのずれ。
- 標本化前後の活性場作用と $\varepsilon_{\rm reset}$。
- 浴拡散係数 $2m\nu_{\rm bath}$ と $|\mathcal J_\phi|$ の不一致。
- 配置変位の高次 cumulant、非 Markov残差、有限再帰。
- 3モード作用殻の異方性と混合時間。
- 設定別・結果別の coarea Jacobian、殻幅、解多重度。
- 開始数、入口数、記録数、完了数、再初期化数の不一致。

## 最重要の未解決問題

現在の最重要課題は次の順に整理できる。

1. 2モード入口作用殻を、場強度に対応する局所作用 $A_i$ と共通流束因子で偏りなく準備する。
2. 標本化後の結果情報を保存しつつ、活性場を coherent部分空間へ再埋め込みする。
3. 共有明反応座標、記録、garbage自由度を事後選別なしで復元し、次試行へ戻す。
4. coherent多様体上の縮約作用が、有限 Hamiltonian 粗視化運動を実際に支配することを示す。
5. 節を含む位相接続と循環量子化を制御する。
6. 運動量結合浴から Brown 極限と配置 Markov 閉鎖を導き、$2m\nu_{\rm bath}=|\mathcal J_\phi|$ を得る。
7. 同じ装置内で位相活性場、配置拡散浴、局所測定器、Bell 境界殻を同時に実現し、交差誤差を小さくする。
8. 任意基底と一般測定器へ Born 型流束を拡張する。
9. 偏った準備装置まで含めた非信号条件を示す。

中心的な未解決問題は、以前の「なぜ $r^2=\rho$ と置けるか」から、「入口でその同期を作用殻流束として作り、標本化後に同じ coherent場を復元する完全周期をどう構成するか」へ移った。

## 最終結論

有限2成分場の正準構造と位相接続を用いると、coherent縮約多様体上で Nelson--Madelung 作用、Madelung 方程式、局所 Schrödinger 型方程式を得る。保存位相作用は有効作用定数となり、単価な非零場は条件付き循環量子化を与える。

2モード作用殻の Liouville 流束は、共通流束因子と単一の直接作用分配方向の下で、位置の Born 型入口密度を与える。同じ一般作用殻幾何は、3モード境界殻の残余ファイバー体積を通じて Bell 型共同統計を与える。

運動量結合経路は、実在的な前後 Markov 拡散の候補として残る。位相接続経路との一致には

```math
2m\nu_{\rm bath}
=
|\mathcal J_\phi|
```

が必要である。

本論文は、Schrödinger 型力学、位置の Born 型重み、循環量子化候補、Bell 型統計を1つの構造化誘導場アーキテクチャへ整理した。しかし、coherent多様体の準備、2モード殻の等方化、標本化後の再埋め込み、一般測定器、完全な再初期化周期を1本の有限 Hamiltonian で完成していない。この境界を超えて主張しない。

# 付録

# 有限セル正準変換と位相接続縮約の詳細

> **位置づけ：** 第2章と第3章の正準変換、固定作用最小化、時間反転、縮約作用の変分を有限次元表示から補足する。


## 極座標正準変換

各セルで

```math
\boldsymbol\Phi
=
r e_r,
\qquad
e_r
=
\begin{pmatrix}
\cos\theta\\
\sin\theta
\end{pmatrix},
\qquad
e_\theta
=
\begin{pmatrix}
-\sin\theta\\
\cos\theta
\end{pmatrix}.
```

運動量を

```math
\boldsymbol\Pi
=
p_r e_r
+
\frac jr e_\theta
```

と分解する。すると

```math
d\boldsymbol\Phi
=
e_r\,dr
+
r e_\theta\,d\theta
```

なので、

```math
\boldsymbol\Pi\cdot d\boldsymbol\Phi
=
p_r\,dr
+
j\,d\theta.
```

従ってシンプレクティック2形式も

```math
d\boldsymbol\Pi\wedge d\boldsymbol\Phi
=
dp_r\wedge dr
+
dj\wedge d\theta
```

となる。$r=0$ では極座標が特異であるため、この変換を使う領域は $r>0$ に限定する。

## 固定作用最小化の Lagrange 乗数表示

固定振幅 $(r_i)$ の下で

```math
E_{\rm rot}
=
\sum_i
\frac{j_i^2}{2Ir_i^2}
\Delta V
```

を、制約

```math
\sum_i j_i\Delta V
=
\mathcal J_\phi
```

の下で最小化する。Lagrange 乗数を $\Lambda$ とすると、

```math
\frac{\partial}{\partial j_i}
\left[
E_{\rm rot}
-
\Lambda
\sum_kj_k\Delta V
\right]
=
\left(
\frac{j_i}{Ir_i^2}
-
\Lambda
\right)
\Delta V
=
0.
```

従って

```math
j_i
=
I\Lambda r_i^2.
```

規格化 $\sum_i r_i^2\Delta V=1$ と全作用制約から

```math
I\Lambda
=
\mathcal J_\phi.
```

よって $j_i=\mathcal J_\phi r_i^2$ を得る。Hessian は対角で

```math
\frac{\partial^2E_{\rm rot}}{\partial j_i\partial j_k}
=
\frac{\Delta V}{Ir_i^2}
\delta_{ik}
```

であり、$I>0$ と $r_i>0$ の下で正定値である。

## 連続極限と節正則化

連続表示の回転エネルギーは

```math
E_{\rm rot}
=
\int
\frac{j^2}{2Ir^2}
\,dx.
```

$r=0$ では特異なので、有限正則化では

```math
E_{\rm rot}^{(\varepsilon)}
=
\int
\frac{j^2}{2I(r^2+\varepsilon^2)}
\,dx
```

を使える。しかし、この正則化では最小配置が厳密な $j=\mathcal J_\phi r^2$ からずれる。接続だけを正則化して回転エネルギーの特異性を放置してはならない。

節から離れた領域

```math
r^2
\geq
c_{\rm node}
>
0
```

では、

```math
\left|
\frac{r^2}{r^2+\varepsilon^2}
-
1
\right|
\leq
\frac{\varepsilon^2}{c_{\rm node}}
```

なので、接続誤差は一様に制御できる。節を含む極限は別問題である。

## 位相接続の内部回転不変性

共通内部回転

```math
\boldsymbol\Phi
\mapsto
R(\alpha)\boldsymbol\Phi
```

の下で、行列式型の分子

```math
\Phi_1\nabla\Phi_2
-
\Phi_2\nabla\Phi_1
```

と分母 $|\boldsymbol\Phi|^2+\varepsilon^2$ は不変である。従って $\mathbf a_\varepsilon$ も不変である。

$\mathcal J_\phi$ はこの回転の生成子なので、全 Hamiltonian が共通回転不変なら Noether 量として保存される。固定 $\mathcal J_\phi$ sectorへの制限は、保存量の値を選ぶことであり、Hamiltonianへ外部パラメータを追加することではない。

## 粒子 Legendre 変換

```math
H_{\rm p}
=
\frac{
|P-\mathcal J_\phi\mathbf a|^2
}{
2m
}
+
V
```

から

```math
\dot X
=
\frac{
P-\mathcal J_\phi\mathbf a
}{
m
}
```

を得る。従って $P=m\dot X+\mathcal J_\phi\mathbf a$ であり、

```math
P\cdot\dot X
-
H_{\rm p}
=
\frac m2|\dot X|^2
+
\mathcal J_\phi\mathbf a\cdot\dot X
-
V.
```

接続項の符号は正である。$S=-\mathcal J_\phi\theta$ と定めることで、縮約作用の位相項は $-\rho(\partial_tS+v\cdot\nabla S)$ となる。

## 縮約作用の変分

作用密度を

```math
\mathcal L
=
\frac m2\rho|v|^2
-
\rho V
-
\rho\partial_tS
-
\rho v\cdot\nabla S
-
\kappa
\left|
\nabla\sqrt\rho
\right|^2
```

とする。

$S$ 変分では、

```math
\delta_S\mathcal A
=
\int
\left[
-\rho\partial_t\delta S
-
\rho v\cdot\nabla\delta S
\right]
\,dx\,dt
```

を部分積分し、

```math
\partial_t\rho
+
\nabla\cdot(\rho v)
=
0
```

を得る。

$v$ 変分では、

```math
\delta_v\mathcal A
=
\int
\rho
\left(
mv-\nabla S
\right)
\cdot\delta v
\,dx\,dt,
```

従って $mv=\nabla S$ である。

$q=\sqrt\rho$ と置くと、

```math
\delta
\left[
-
\kappa
\int
|\nabla q|^2
\,dx
\right]
=
2\kappa
\int
\delta q\,\Delta q
\,dx.
```

$\delta\rho=2q\delta q$ から、$\rho$ に関する汎関数微分は

```math
\kappa
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
```

この符号を使うと Hamilton--Jacobi 式の量子ポテンシャルは

```math
-\kappa
\frac{\Delta\sqrt\rho}{\sqrt\rho}
```

となる。

## 同期差保存の仮定

位相変分から

```math
\partial_tj
+
\mathcal J_\phi
\nabla\cdot(\rho v)
=
0
```

を得るには、縮約後に残る場 Hamiltonian が共通位相 $\theta$ そのものへ依存しないことが必要である。$r^2|\nabla\theta|^2$ の独立な場エネルギーを残すと、位相流束が追加される。

従って第3章の理想同期差保存は、位相勾配エネルギーを粒子流速の運動エネルギーへ吸収し、残差を $\varepsilon_{\rm cross}$ または $\varepsilon_{\rm press}$ へ含めた縮約に限定される。

## 変分縮約の限界

ミクロ作用を多様体へ制限してから変分する操作と、ミクロ方程式を解いてから粗視化する操作は一般に交換しない。必要なのは、少なくとも次のいずれかである。

1. 縮約多様体が近似不変であり、法線方向残差が小さい。
2. 高速法線モードを断熱消去し、有効作用の誤差を評価できる。
3. 弱開放縮約が法線方向だけを安定化し、接方向の Hamiltonian 構造を保つ。

本論文はこれらの一様誤差定理を与えない。第3章の定理は、制限作用内部の厳密結果として読む。

# 一般作用殻、coarea、入口流束の詳細

> **位置づけ：** 第4章と第6章で用いる作用殻容量、排他的入口面、coarea Jacobian、作用分配次元、殻接方向混合を補足する。


## 単体積分

作用殻容量を

```math
\Omega_n(A)
=
(2\pi)^n
\int_{J_k\geq0}
\delta
\left(
A-\sum_{k=1}^nJ_k
\right)
\prod_{k=1}^n dJ_k
```

とする。$n=1$ では

```math
\Omega_1(A)
=
2\pi.
```

再帰関係

```math
\Omega_n(A)
=
2\pi
\int_0^A
\Omega_{n-1}(A-J_n)
\,dJ_n
```

を用いると、

```math
\Omega_n(A)
=
\frac{(2\pi)^n}{(n-1)!}
A^{n-1}
```

が帰納的に従う。

## 排他的な和と直積の違い

位置チャンネルを排他的な和

```math
\Gamma_\partial
=
\bigsqcup_i
\Gamma_{\partial,i}
```

とすれば、全入口流束は

```math
\mathscr F
=
\sum_i\mathscr F_i
```

であり、各 $\mathscr F_i$ に局所作用 $A_i$ の線形因子が残る。

一方、全セルに独立な2モード作用殻を同時に課す直積構成では、容量は

```math
\prod_i\Omega_2(A_i)
\propto
\prod_iA_i
```

となる。1つのチャンネル $i$ を選ぶ相対重みではなく、全セル作用の積が現れる。この構成は位置の Born 型入口頻度を与えない。

## coarea公式

全入口正準位相空間を $\Gamma$、基準体積を $d\Gamma$ とする。固定作用制約と反応面制約を

```math
F_1(z)
=
A_i-K_i-I,
```

```math
F_2(z)
=
s_i(z)
```

とする。正方向流束は記号的に

```math
\mathscr F_i
=
\int_\Gamma
\rho_0(z)
\delta(F_1)
\delta(F_2)
\left(
\dot s_i
\right)_+
d\Gamma.
```

一般の滑らかな写像 $F=(F_1,F_2)$ に対し、coarea公式は

```math
\int_\Gamma
g(z)
\delta(F(z))
d\Gamma
=
\int_{F^{-1}(0)}
\frac{g(z)}{J_F(z)}
d\Sigma(z),
```

```math
J_F
=
\sqrt{
\det
\left[
DF
\left(
DF
\right)^{\mathsf T}
\right]
}.
```

従って共通流束因子には、$\dot s_i$ だけでなく $J_F^{-1}$、初期密度、解多重度、spectator体積が含まれる。

## 2モード殻の明示積分

理想作用角座標では、

```math
\int_0^\infty dK
\int_0^\infty dI
\,
\delta(A-K-I)
=
\int_0^A dK
=
A.
```

角積分を加えると、

```math
\Omega_2(A)
=
(2\pi)^2A.
```

入口法線速度と spectator因子が作用分配座標 $(K,I)$ に依存しない理想模型では、流束はこの容量に比例する。

## 有限入口幅

デルタ関数の代わりに偶関数窓

```math
K_{\delta_A}(y)
=
\frac1{\delta_A}
K
\left(
\frac y{\delta_A}
\right),
```

```math
\int K(y)\,dy=1,
\qquad
\int yK(y)\,dy=0
```

を用いる。理想2モード容量は $A$ に線形なので、窓が $A=0$ の端へ触れず、他の因子が一定なら、対称な有限幅平均は線形重みを変えない。

一般の滑らかな流束因子 $g(A)$ を含むと、

```math
\mathscr F_i^{(\delta_A)}
=
\mathscr F_i^{(0)}
+
O
\left(
\delta_A^2
\sup
\left|
\partial_A^2
\left[
Ag(A)
\right]
\right|
\right).
```

殻端の切断、非対称窓、結果依存幅では1次誤差が現れ得る。

## 作用分配方向の数

活性モード $K$ と $q$ 個の明反応作用 $I_1,\ldots,I_q$ が

```math
K+\sum_{\alpha=1}^qI_\alpha
=
A
```

を分配すると、

```math
\int_{K,I_\alpha\geq0}
\delta
\left(
A-K-\sum_\alpha I_\alpha
\right)
dK
\prod_\alpha dI_\alpha
=
\frac{A^q}{q!}.
```

従って線形則には $q=1$ が必要である。$q>1$ の追加明モードを導入しながら線形 Born 型重みを保つには、それらを直接作用分配から外し、共通 spectator因子にしなければならない。

## 殻接方向 Hamiltonian

$n$モード複素ベクトル $a$ と Hermitian 行列 $T_\alpha$ に対し、

```math
L_\alpha
=
a^\dagger T_\alpha a
```

を生成子とする。Poisson 括弧を

```math
\left\{
a_j,a_k^*
\right\}
=
-i\delta_{jk}
```

とすれば、

```math
\dot a
=
-iT_\alpha a,
```

```math
\left\{
a^\dagger a,
L_\alpha
\right\}
=
0.
```

従って

```math
H_{\rm mix}
=
\varepsilon
\sum_\alpha
\xi_\alpha(z_{\rm D})
L_\alpha
```

は総作用殻に接する Hamiltonian 混合を与える。

暗モードの相関が短く、生成子方向が等方なら、弱結合縮約は概念的に

```math
\mathcal L_{\rm eff}
=
D
\sum_\alpha
X_{L_\alpha}^2
```

となる。2モード全殻では $U(2)$、3モード全殻では $U(3)$ の Casimir型拡散に対応する。有限暗モードからこの生成子を一様誤差付きで導くことは未完成である。

## Born側とBell側の対応

| 用途 | 全殻 | 比較する量 | 線形因子 |
|---|---|---|---|
| Born 型位置入口 | 活性＋共有明反応座標の2モード殻 | チャンネルごとの全殻容量 | $A_i$ |
| Bell 型共同統計 | $J_+,J_s,J_r$ の3モード殻 | 固定 $J_+$ 後の残余ファイバー | $C_0-J_+$ |

両者は一般作用殻式の同じ指数則を使う。違いは、Born 側が2モード全殻をチャンネル間で比較し、Bell 側が3モード全殻の異なる切断を結果間で比較する点にある。

## 流束規格化と全試行監査

入口確率を

```math
P_i
=
\frac{\mathscr F_i}{\sum_j\mathscr F_j}
```

と定義するには、分母が全開始試行の入口通過を数えなければならない。次を監査する。

1. 各開始試行は高々1つの排他的入口面を正方向に横切る。
2. 入口へ到達しない試行を無言で除外しない。
3. 複数回交差を1試行としてどう数えるかを固定する。
4. 結果別に異なる停止時間または滞在時間を頻度へ重複計上しない。
5. 記録失敗、再埋め込み失敗、再初期化失敗を結果依存に捨てない。

これらを満たさなければ、作用殻体積が正しくても実験の無条件頻度にはならない。

## 再埋め込み写像に必要な保存量

標本化後の状態を $z_{\rm post}$、次試行の準備面を $\Gamma_{\rm prep}$ とする。理想的な再埋め込み写像

```math
\mathcal U_{\rm reset}:
z_{\rm post}
\longmapsto
z_{\rm next}\in\Gamma_{\rm prep}
```

は、拡大全系で正準かつ1対1でなければならない。結果情報を消去する場合、その情報とエントロピーは仕事源または外部自由度へ移す必要がある [17,18]。

有限装置部分だけで

```math
z_{\rm post}
\longmapsto
z_{\rm ref}
```

という多対1写像を置くことは Hamiltonian ではない。記録、garbage、外部仕事自由度を含む拡大全系で可逆に実装し、有限部分の復元だけを縮約として得る必要がある。

# 構造化誘導場、U(3) 殻拡散、境界ファイバー体積

> **位置づけ：** 配置拡散浴の運動量結合方向と測定器の座標結合方向を含む固定射影について、静的基底、全交差応答、和・差変換、作用保存、固定殻体積、coarea 計算を補足する。誘導場から等方拡散への縮約は候補構成であり、未完成である。


## 拡大全系とエネルギー収支

測定器と境界作用殻を含む拡大全系を

```math
H_{\rm all}
=
H_{\rm src}
+
H_{\rm set}
+
H_{\rm loc}
+
H_{\rm ptr}
+
H_{\rm med}
+
H_\partial
+
H_{\rm fin-link}
+
H_{\rm ext}
+
\varepsilon_{\rm ext}H_{\rm link}
+
H_{\rm work}
```

と書く。各項の役割は次である。

| 項 | 役割 |
|---|---|
| $H_{\rm src}$ | 固定総入力作用と位相基準を持つ伝達ベクトル対の準備 |
| $H_{\rm set}$ | 左右の設定制御器 |
| $H_{\rm loc}$ | 局所結果形成または最小結果符号化 |
| $H_{\rm ptr}$ | 固定指針への記録 |
| $H_{\rm med}$ | 左右局所反応座標、共通境界反応座標、暗モードを含む1つの構造化誘導場 |
| $H_\partial$ | 境界3モードの自由運動と弱い混合 |
| $H_{\rm fin-link}$ | 有限装置部分内の結合 |
| $H_{\rm ext}$ | 外部環境 |
| $\varepsilon_{\rm ext}H_{\rm link}$ | 常時のごく弱い漏れと流入 |
| $H_{\rm work}$ | 設定変更、記録消去、再初期化の仕事源 |

全 Hamiltonian に明示的な時間依存性がなければ、拡大全エネルギーは保存される。一方、有限装置部分

```math
H_{\rm fin}
=
H_{\rm all}
-
H_{\rm ext}
-
H_{\rm work}
```

の収支は

```math
\frac{dH_{\rm fin}}{dt}
=
\left\{
H_{\rm fin},
\varepsilon_{\rm ext}H_{\rm link}
+
H_{\rm work}
\right\}.
```

実験室の記号では、

```math
\dot E_{\rm fin}
=
J_{\rm in}
-
J_{\rm out}
+
P_{\rm ctrl}.
```

閉鎖補助モデルは $\varepsilon_{\rm ext}=0$ とし、仕事源を有限装置へ含めた短時間窓で用いる。現行モデルでは $\varepsilon_{\rm ext}$ を常時零にせず、測定窓内の相対エネルギー変化を小さい量として評価する。

## 静的誘導場基底の正準性

浴座標を $Q,\Pi\in\mathbb R^N$ とし、

```math
H_{\rm med}
=
\frac12\Pi^{\mathsf T}\Pi
+
\frac12Q^{\mathsf T}KQ
+
\varepsilon_{\rm nl}V_{\rm nl}(Q)
```

とする。$K$ は正定値実対称行列である。

第5章の粒子運動量結合方向を $\operatorname{Ran}C_N^{\mathsf T}$ とする。局所装置と境界装置が浴座標へ結合する方向を

```math
c_A,
\quad
c_B,
\quad
c_{\partial,1},
\ldots,
c_{\partial,m}
```

とする。$\operatorname{Ran}C_N^{\mathsf T}$ とこれらの座標結合方向が張る部分空間の正規直交基底を先頭に並べる直交行列 $O$ を固定し、

```math
\widetilde Q=OQ,
\qquad
\widetilde\Pi=O\Pi
```

と変換する。

<!-- theorem-start:proposition -->
**命題（直交浴基底変換の正準性）**
$O^{\mathsf T}O=I$ なら、$(Q,\Pi)\mapsto(\widetilde Q,\widetilde\Pi)$ は正準変換である。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
正準1形式は

```math
\Pi^{\mathsf T}dQ
=
\widetilde\Pi^{\mathsf T}
O
O^{\mathsf T}
d\widetilde Q
=
\widetilde\Pi^{\mathsf T}d\widetilde Q
```

と保存される。従ってシンプレクティック2形式も保存される。
<!-- theorem-end:proof -->

変換後の2次形式は

```math
H_{\rm med}^{(2)}
=
\frac12\widetilde\Pi^{\mathsf T}\widetilde\Pi
+
\frac12
\widetilde Q^{\mathsf T}
\widetilde K
\widetilde Q,
\qquad
\widetilde K
=
OKO^{\mathsf T}.
```

結合方向に適合した基底を取っても、$\widetilde K$ は一般にブロック対角ではない。局所、境界、暗モード間の動的結合は $\widetilde K$ の非対角ブロックと $V_{\rm nl}$ に残る。運動量結合と座標結合が同じ明部分空間にあるため、自由回転後には両者の混合応答も一般に残る。

従って、

```math
H_{\rm med}
=
H_A^{\rm loc}
+
H_B^{\rm loc}
+
H_\partial^{\rm glob}
+
H^{\rm dark}
+
H_{\rm cross}
```

という分解は、正準座標の厳密な分類と、動力学的な近似直和を分けて読む必要がある。

## 線形応答核

装置の座標結合だけに対する線形誘導場の運動方程式は

```math
\ddot Q+KQ
=
-\epsilon_Ac_Ax_A
-\epsilon_Bc_Bx_B
-\sum_\alpha
c_{\partial,\alpha}F_\alpha.
```

ここで $F_\alpha$ は境界モードから浴へ加わる一般化力である。初期値解は

```math
Q(t)
=
\cos
\left(
K^{1/2}t
\right)Q(0)
+
K^{-1/2}
\sin
\left(
K^{1/2}t
\right)\Pi(0)
```

```math
\quad
-
\int_0^t
K^{-1/2}
\sin
\left[
K^{1/2}(t-s)
\right]
F_{\rm dev}(s)\,ds,
```

```math
F_{\rm dev}
=
\epsilon_Ac_Ax_A
+
\epsilon_Bc_Bx_B
+
\sum_\alpha
c_{\partial,\alpha}F_\alpha.
```

A側の一般化力 $c_A^{\mathsf T}Q(t)$ にB側の $x_B$ が与える寄与は

```math
-\epsilon_B
\int_0^t
\chi_{AB}(t-s)x_B(s)\,ds,
```

```math
\chi_{AB}(t)
=
c_A^{\mathsf T}
K^{-1/2}
\sin
\left(
K^{1/2}t
\right)
c_B.
```

同様に $\chi_{BA}$ を得る。従って、$c_A^{\mathsf T}c_B=0$ でも $\chi_{AB}(t)$ は一般に零ではない。$K$ が $c_A,c_B$ の張る部分空間を別々に不変にするときだけ、座標–座標の線形交差応答は厳密に消える。

第5章の $P^{\mathsf T}C_N\Pi$ を同時に含めると、$Q$ と $\Pi$ の自由回転を通じて運動量–座標混合核も生じる。局所性の判定には、各核をまとめた応答作用素 $\mathcal R_{XY}(t)$ を使う。

局所測定窓 $0\leq t\leq T_{\rm meas}$ で

```math
\varepsilon_{\rm loc}
=
\frac{
\sup_t
\max
\left(
\|\mathcal R_{AB}(t)\|,
\|\mathcal R_{BA}(t)\|
\right)
}{
\sup_t
\min
\left(
\|\mathcal R_{AA}(t)\|,
\|\mathcal R_{BB}(t)\|
\right)
}
```

を用いる理由はここにある。非線形補正については、指定した準備領域のまわりで変分方程式を解き、同じ比を定義する。

## 局所結果符号化の生成子

結果種座標を $s_X$、伝達ベクトルを $(Q_X,P_X)$、応答モードを $(x_X,p_X)$ とする。平坦結果領域上で $\sigma(s_X)=X\in\{-1,+1\}$ とする。

局所分析の生成子を

```math
K_X^{\rm an}
=
-
\left[
\phi(a_X)
+
\pi\chi_-(s_X)
\right]
I_X
-
x_X\sigma(s_X),
```

```math
I_X
=
\frac12
\left(
Q_X^2+P_X^2
\right),
\qquad
\chi_-(s)
=
\frac{
1-\sigma(s)
}{
2
}
```

とする。生成子の単位流れで、

```math
u_X^{\rm out}
=
X R[\phi(a_X)]u_X^{\rm in},
\qquad
p_X^{\rm out}
=
p_X^{\rm in}+X.
```

$p_X^{\rm in}=0$ なら $p_X^{\rm out}=X$ である。

固定指針対を $(Y_X,\Pi_X)$ とし、平坦関数 $\zeta(p_X)$ が $p_X=\pm1$ の近傍で $\pm1$ を取るとする。転写生成子

```math
K_X^{\rm lock}
=
-Y_X\zeta(p_X)
```

の単位流れは

```math
\Pi_X^{\rm out}
=
\Pi_X^{\rm in}
+
\zeta(p_X).
```

$\Pi_X^{\rm in}=0$ なら $\Pi_X^{\rm out}=X$ となる。

自由 Hamiltonian と幅 $\tau_{\rm pulse}$ のパルスが同時に働く場合、理想単位流れとの差は、有界な適用領域で

```math
O(\varepsilon_{\rm pulse}),
\qquad
\varepsilon_{\rm pulse}
=
\tau_{\rm pulse}
\sup_{\mathcal K}
\left\|
X_{H_0}
\right\|
```

と評価する。局所誘導場の交差応答も加えると、指針の誤差は

```math
O
\left(
\varepsilon_{\rm pulse}
+
\varepsilon_{\rm loc}
+
\varepsilon_{\rm open}
\right).
```

この補助装置は既存の結果種を記録するだけであり、一般測定器ではない。

## 和・差基底の正準性

左右伝達ベクトルを正準対 $(Q_A,P_A)$、$(Q_B,P_B)$ とする。和・差座標を

```math
Q_\pm
=
\frac{
Q_A\pm Q_B
}{
\sqrt2
},
\qquad
P_\pm
=
\frac{
P_A\pm P_B
}{
\sqrt2
}
```

と定める。

<!-- theorem-start:proposition -->
**命題（和・差変換の正準性）**
上の変換は正準であり、

```math
P_A\,dQ_A
+
P_B\,dQ_B
=
P_+\,dQ_+
+
P_-\,dQ_-.
```
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
変換行列

```math
U
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}
```

は直交行列である。座標と運動量へ同じ $U$ を作用させるため、C.1節と同じ計算で正準1形式が保存される。
<!-- theorem-end:proof -->

和・差作用は

```math
I_\pm
=
\frac12
\left(
Q_\pm^2+P_\pm^2
\right)
=
\frac14
\left\|
u_A\pm u_B
\right\|^2.
```

直交性から、

```math
I_++I_-
=
I_A+I_B.
```

設定と結果は $I_+-I_-$ に入るが、総入力作用には入らない。

固定された $U$ は1つの正準写像であり、測度を生成しない。入力集団が Liouville 測度を持てば保存するが、単一入力を一様集団へ変えない。

## 3モード作用と U(3) 生成子

境界3モードを複素正準変数

```math
a
=
\begin{pmatrix}
a_+\\
a_s\\
a_r
\end{pmatrix},
\qquad
a_\nu
=
\frac{
q_\nu+ip_\nu
}{
\sqrt2
}
```

で表す。Poisson 括弧を

```math
\left\{
a_j,a_k^*
\right\}
=
-i\delta_{jk}
```

とする。総作用は

```math
C
=
a^\dagger a.
```

$T_\alpha$ を $u(3)$ の Hermitian 基底とし、

```math
L_\alpha
=
a^\dagger T_\alpha a
```

を Hamiltonian 生成子とする。$L_\alpha$ の流れは

```math
\dot a
=
-iT_\alpha a
```

であり、

```math
\left\{
C,L_\alpha
\right\}
=
0.
```

従って全ての $U(3)$ 生成子は総作用殻に接する。

構造化誘導場の未読変数 $\xi_\alpha(z_{\mathcal B})$ と弱く結合する候補 Hamiltonian を

```math
H_{\rm iso-link}
=
\epsilon_{\rm iso}
\sum_{\alpha=1}^{9}
\xi_\alpha(z_{\mathcal B})
L_\alpha(a)
```

とする。各瞬間の全 Hamiltonian 流れは $C$ を保存する。

浴相関が準備窓で

```math
\left\langle
\xi_\alpha(t)
\xi_\beta(0)
\right\rangle
\simeq
\delta_{\alpha\beta}
\kappa(t)
```

となり、相関時間が境界モードの緩和時間より短いとする。弱結合・長時間尺度での2次縮約生成子は概念的に

```math
\mathcal L_{\rm eff}
=
D_\partial
\sum_{\alpha=1}^{9}
X_{L_\alpha}^2
```

となる。同次空間 $U(3)/U(2)$ 上では、この Casimir 作用素は規格化を除いて $\Delta_{S^5}$ に一致する。

この縮約には、少なくとも次の近似が必要である。

1. $\epsilon_{\rm iso}\ll1$ の弱結合。
2. 浴相関時間と準備時間の分離。
3. 9方向の相関行列の等方性。
4. 有限誘導場の再帰時間より短い準備窓。
5. 外部交換による長時間再位相化の抑制。

本論文は、特定の有限 $V_{\rm nl}$ と外部結合について、これらの条件から $\mathcal L_{\rm eff}$ への一様誤差上界を証明しない。従ってこれはミクロ実現候補であり、導出済みの定理ではない。

## 等方拡散の定常測度

固定殻 $S_{C_0}^5$ 上の密度 $f$ が

```math
\partial_t f
=
D_\partial\Delta_{S^5}f
```

に従うとする。定常解は

```math
\Delta_{S^5}f=0
```

を満たす。部分積分により、

```math
0
=
\int
f\Delta_{S^5}f\,d\mu_{C_0}
=
-
\int
\left|
\nabla_{S^5}f
\right|^2
d\mu_{C_0}.
```

従って $f$ は定数であり、規格化すれば $f=1$ である。

異方摂動を

```math
\mathcal L_\varepsilon
=
D_\partial\Delta_{S^5}
+
\varepsilon_{\rm aniso}\mathcal L_1
```

とする。$\mathcal L_1$ が質量を保存し、等方生成子のスペクトルギャップに対して相対有界なら、定常密度の形式展開は

```math
f_\varepsilon
=
1
-
\frac{
\varepsilon_{\rm aniso}
}{
D_\partial
}
\left(
\Delta_{S^5}
\right)^{-1}_{0}
\mathcal L_1^*1
+
O
\left(
\varepsilon_{\rm aniso}^2
\right)
```

となる。逆作用素の添字0は平均零部分空間への制限である。この式は、異方性の影響が結合定数だけでなくスペクトルギャップに依存することを示す。

## 固定殻体積と周辺密度

作用角変数で、3モード固定殻の未規格化体積は

```math
\Omega_3(C_0)
=
(2\pi)^3
\int_0^\infty dJ_+
\int_0^\infty dJ_s
\int_0^\infty dJ_r\,
\delta
\left(
C_0-J_+-J_s-J_r
\right).
```

$J_r$ を積分すると、$J_+,J_s\geq0$ かつ $J_++J_s\leq C_0$ の三角形が残る。従って、

```math
\Omega_3(C_0)
=
(2\pi)^3
\int_0^{C_0}dJ_+
\int_0^{C_0-J_+}dJ_s
=
\frac{
(2\pi)^3C_0^2
}{
2
}.
```

$J_+=x$ の未規格化周辺は

```math
\omega_+(x)
=
(2\pi)^3
\int_0^\infty dJ_s
\int_0^\infty dJ_r\,
\delta
\left(
C_0-x-J_s-J_r
\right)
```

```math
=
(2\pi)^3
\left(
C_0-x
\right)
\mathbf1_{\{0\leq x\leq C_0\}}.
```

従って、

```math
p_+(x)
=
\frac{
\omega_+(x)
}{
\Omega_3(C_0)
}
=
\frac{
2(C_0-x)
}{
C_0^2
}.
```

固定 $x$ の条件付き分布では、

```math
p
\left(
J_s\mid J_+=x
\right)
=
\frac1{C_0-x}
```

である。条件付き密度の $1/(C_0-x)$ と、ファイバー総質量の $C_0-x$ を混同してはならない。

## coarea と境界ファイバー

一般の境界正準位相空間を $\Gamma_\partial$、基準体積を $d\Gamma_\partial$ とする。2つの制約を

```math
F_1
=
C_0-J_+-J_s-J_r,
```

```math
F_2
=
J_+-I_+^{AB}
```

とする。理想線形モデルでは、

```math
W_{AB}
\propto
\int_{\Gamma_\partial}
\delta(F_1)
\delta(F_2)
d\Gamma_\partial.
```

作用角座標に変換すると、変換 Jacobian は1である。$J_+$ と $J_r$ のデルタ関数積分を行えば、

```math
W_{AB}
\propto
(2\pi)^3
\int_0^{C_0-I_+^{AB}}dJ_s
```

```math
=
(2\pi)^3
\left(
C_0-I_+^{AB}
\right).
```

一般の滑らかな境界写像 $F=(F_1,F_2)$ では coarea 公式により、

```math
\int_{\Gamma_\partial}
\rho(z)
\delta
\left(
F(z)
\right)
d\Gamma_\partial
=
\int_{F^{-1}(0)}
\frac{
\rho(z)
}{
J_F(z)
}
d\Sigma(z),
```

```math
J_F
=
\sqrt{
\det
\left[
DF
\left(
DF
\right)^{\mathsf T}
\right]
}.
```

理想作用座標では $J_F$ が結果と設定に共通な定数へなる。非線形境界写像、分岐、caustic、解多重度がある場合は、この単純化を使えない。同じ巨視的結果へ対応する複数の解は、その局所 Jacobian と多重度を含めて数える。

## 有限分解能の展開

偶関数 $K$ を

```math
\int_{\mathbb R}K(y)\,dy=1,
\qquad
\int_{\mathbb R}yK(y)\,dy=0
```

と規格化し、

```math
K_{\delta_J}(y)
=
\frac1{\delta_J}
K
\left(
\frac y{\delta_J}
\right)
```

とする。$J_+$ 周辺密度 $p_+(x)$ は殻内部で線形なので、窓が殻端に触れない限り、

```math
\int
p_+(x)
K_{\delta_J}(x-I_+)\,dx
=
p_+(I_+)
```

が偶対称窓では厳密に成り立つ。一般の滑らかな Jacobian または殻幅分布を含めると、

```math
W_{AB}^{(\delta_J)}
=
c_{\delta_J}
\left(
C_0-I_+^{AB}
\right)
+
O
\left(
\delta_J^2
\sup
\left|
\partial_{J_+}^2
\frac{\rho}{J_F}
\right|
\right).
```

従って、理想線形作用殻では有限分解能自体が1次の角度誤差を生まない。主要な分解能誤差は、殻端の切断、非線形 Jacobian、結果依存窓、総作用幅との重なりから生じる。

## 半径方向の弱開放力学

総作用 $C$ の縮約式を

```math
dC_t
=
-\gamma_C
\left(
C_t-C_0
\right)dt
+
\sqrt{2D_C}\,dW_t
```

とする。定常密度は

```math
\rho_C(C)
\propto
\exp
\left[
-
\frac{
\gamma_C
}{
2D_C
}
\left(
C-C_0
\right)^2
\right],
```

その分散は

```math
\sigma_C^2
=
\frac{D_C}{\gamma_C}
```

である。

この式は、外部への漏れと流入を線形化した縮約候補である。基礎 Hamiltonian の総エネルギーが確率的に失われると仮定したものではない。外部環境と仕事源を消去した有限部分の有効式として読む。

角方向と半径方向が近似的に分離する条件を

```math
\tau_{\rm corr}
\ll
\tau_{\rm mix}
\ll
\tau_C,
\qquad
\tau_C=\gamma_C^{-1}
```

とする。$\tau_{\rm corr}$ は浴相関時間、$\tau_{\rm mix}$ は殻接方向混合、$\tau_C$ は半径変化である。$\tau_{\rm mix}\ll\tau_C$ なら、各半径で方向分布が先に等方化する。

純粋漏れでは

```math
dC_t=-\gamma_CC_t\,dt
```

となり、非零の定常殻は存在しない。流入または仕事源を含む復元項は、作用殻準備に不可欠である。

## ミクロ構成から未導出の事項

本付録で厳密に示したのは次である。

- 運動量結合方向と座標結合方向を含む1つの有限誘導場に対する静的な直交正準基底。
- 装置の座標–座標交差応答核と、混合応答を含めた全応答作用素の定義。
- 最小結果符号化器の理想正準写像。
- 和・差変換の正準性と作用保存。
- $U(3)$ Hamiltonian 生成子が総作用を保存すること。
- 3モード固定作用殻の体積、周辺密度、残余ファイバー体積。
- 理想線形境界写像の共通 coarea Jacobian。

次は未導出である。

- 特定の有限非線形浴が必要な時間窓で等方な相関行列を持つこと。
- 有限誘導場と常時の外部交換から $D_\partial\Delta_{S^5}$ を一様誤差付きで得ること。
- 異方誤差、混合時間、再帰時間を同じパラメータから同時に閉じること。
- 運動量–座標混合核を含む左右全交差応答を、Bell 測定窓で一様に抑えること。
- 半径方向の復元式とエネルギー収支を明示的な外部 Hamiltonian から導くこと。
- 一般測定器、境界適合、記録、消去、再初期化を1本の有限幅 Hamiltonian へ統合すること。

従って、作用殻の幾何計算は厳密結果、全殻拡散と半径安定化は縮約候補、現行の弱開放モデルへの接続は近似または予想・未解決として扱う。

# 参考文献


- [1] J. S. Bell, ``On the Einstein Podolsky Rosen Paradox,'' Physics Physique Fizika 1, 195--200 (1964). <https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195>
- [2] J. F. Clauser, M. A. Horne, A. Shimony, and R. A. Holt, ``Proposed Experiment to Test Local Hidden-Variable Theories,'' Physical Review Letters 23, 880--884 (1969). <https://doi.org/10.1103/PhysRevLett.23.880>
- [3] E. Nelson, ``Derivation of the Schrödinger Equation from Newtonian Mechanics,'' Physical Review 150, 1079--1085 (1966). <https://doi.org/10.1103/PhysRev.150.1079>
- [4] F. Guerra and L. M. Morato, ``Quantization of Dynamical Systems and Stochastic Control Theory,'' Physical Review D 27, 1774--1786 (1983). <https://doi.org/10.1103/PhysRevD.27.1774>
- [5] K. Yasue, ``Stochastic Calculus of Variations,'' Journal of Functional Analysis 41, 327--340 (1981). <https://doi.org/10.1016/0022-1236(81)90079-3>
- [6] J.-C. Zambrini, ``Stochastic Mechanics According to E. Schrödinger,'' Physical Review A 33, 1532--1548 (1986). <https://doi.org/10.1103/PhysRevA.33.1532>
- [7] K. B. Wharton, ``Time-Symmetric Boundary Conditions and Quantum Foundations,'' Symmetry 2, 272--283 (2010). <https://doi.org/10.3390/sym2010272>
- [8] K. B. Wharton and N. Argaman, ``Colloquium: Bell's Theorem and Locally Mediated Reformulations of Quantum Mechanics,'' Reviews of Modern Physics 92, 021002 (2020). <https://doi.org/10.1103/RevModPhys.92.021002>
- [9] M. J. W. Hall, ``Local Deterministic Model of Singlet State Correlations Based on Relaxing Measurement Independence,'' Physical Review Letters 105, 250404 (2010). <https://doi.org/10.1103/PhysRevLett.105.250404>
- [10] M. S. Leifer and M. F. Pusey, ``Is a Time Symmetric Interpretation of Quantum Theory Possible without Retrocausality?,'' Proceedings of the Royal Society A 473, 20160607 (2017). <https://doi.org/10.1098/rspa.2016.0607>
- [11] C. J. Wood and R. W. Spekkens, ``The Lesson of Causal Discovery Algorithms for Quantum Correlations,'' New Journal of Physics 17, 033002 (2015). <https://doi.org/10.1088/1367-2630/17/3/033002>
- [12] G. W. Ford, M. Kac, and P. Mazur, ``Statistical Mechanics of Assemblies of Coupled Oscillators,'' Journal of Mathematical Physics 6, 504--515 (1965). <https://doi.org/10.1063/1.1704304>
- [13] H. Mori, ``Transport, Collective Motion, and Brownian Motion,'' Progress of Theoretical Physics 33, 423--455 (1965). <https://doi.org/10.1143/PTP.33.423>
- [14] R. Zwanzig, ``Nonlinear Generalized Langevin Equations,'' Journal of Statistical Physics 9, 215--220 (1973). <https://doi.org/10.1007/BF01008729>
- [15] B. Jamison, ``Reciprocal Processes,'' Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete 30, 65--86 (1974). <https://doi.org/10.1007/BF00532864>
- [16] J. L. Doob, ``Conditional Brownian Motion and the Boundary Limits of Harmonic Functions,'' Bulletin de la Société Mathématique de France 85, 431--458 (1957). <https://doi.org/10.24033/bsmf.1495>
- [17] R. Landauer, ``Irreversibility and Heat Generation in the Computing Process,'' IBM Journal of Research and Development 5, 183--191 (1961). <https://doi.org/10.1147/rd.53.0183>
- [18] C. H. Bennett, ``The Thermodynamics of Computation: A Review,'' International Journal of Theoretical Physics 21, 905--940 (1982). <https://doi.org/10.1007/BF02084158>
- [19] T. C. Wallstrom, ``Inequivalence between the Schrödinger Equation and the Madelung Hydrodynamic Equations,'' Physical Review A 49, 1613--1617 (1994). <https://doi.org/10.1103/PhysRevA.49.1613>
- [20] H. Price and K. Wharton, ``Bell Correlations as Selection Artefacts,'' arXiv:2309.10969v3 (2024). <https://arxiv.org/abs/2309.10969>
- [21] H. Price and K. Wharton, ``A Mechanism for Entanglement?,'' arXiv:2406.04571v1 (2024). <https://arxiv.org/abs/2406.04571>
- [22] N. Argaman, ``Bell's Theorem and the Causal Arrow of Time,'' American Journal of Physics 78, 1007--1013 (2010). <https://doi.org/10.1119/1.3456564>
- [23] S. Hossenfelder and T. Palmer, ``Rethinking Superdeterminism,'' Frontiers in Physics 8, 139 (2020). <https://doi.org/10.3389/fphy.2020.00139>
- [24] G. 't Hooft, The Cellular Automaton Interpretation of Quantum Mechanics, Springer (2016). <https://doi.org/10.1007/978-3-319-41285-6>
- [25] C. Léonard, ``A Survey of the Schrödinger Problem and Some of Its Connections with Optimal Transport,'' Discrete and Continuous Dynamical Systems A 34, 1533--1574 (2014). <https://doi.org/10.3934/dcds.2014.34.1533>
- [26] Y. Chen, T. T. Georgiou, and M. Pavon, ``On the Relation between Optimal Transport and Schrödinger Bridges: A Stochastic Control Viewpoint,'' Journal of Optimization Theory and Applications 169, 671--691 (2016). <https://doi.org/10.1007/s10957-015-0803-z>
- [27] H. E. Rauch, F. Tung, and C. T. Striebel, ``Maximum Likelihood Estimates of Linear Dynamic Systems,'' AIAA Journal 3, 1445--1450 (1965). <https://doi.org/10.2514/3.3166>
- [28] J. Fuchs, S. Goldt, and U. Seifert, ``Stochastic Thermodynamics of Resetting,'' Europhysics Letters 113, 60009 (2016). <https://doi.org/10.1209/0295-5075/113/60009>
- [29] M. R. Evans, S. N. Majumdar, and G. Schehr, ``Stochastic Resetting and Applications,'' Journal of Physics A: Mathematical and Theoretical 53, 193001 (2020). <https://doi.org/10.1088/1751-8121/ab7cfe>
- [30] J. Knorst and A. O. Lopes, ``On the Quantum Guerra--Morato Action Functional,'' Journal of Mathematical Physics 65, 082102 (2024). <https://doi.org/10.1063/5.0207422>
- [31] J. T. Wilson, V. Borovitskiy, A. Terenin, P. Mostowsky, and M. P. Deisenroth, ``Pathwise Conditioning of Gaussian Processes,'' Journal of Machine Learning Research 22, 1--47 (2021). <https://jmlr.org/papers/v22/20-1260.html>
- [32] C. Léonard, S. Rœlly, and J.-C. Zambrini, ``Reciprocal Processes. A Measure-Theoretical Point of View,'' Probability Surveys 11, 237--269 (2014). <https://doi.org/10.1214/13-PS220>
- [33] M. A. Marchiori and M. A. M. de Aguiar, ``Energy Dissipation Via Coupling With a Finite Chaotic Environment,'' Physical Review E 83, 061112 (2011). <https://doi.org/10.1103/PhysRevE.83.061112>
