@number: 0
@chapter: 概要
@title: 有限 Hamiltonian 中核の定量的 Nelson 極限と時間対称境界測度による Bell 型統計
@status: 有限 Gaussian 極限と二モード台帳型 Bell compatibility を論理的に分離し、仮定と導出を明示した改訂稿。

本論文は、有限個の正準自由度からなる可逆な Hamiltonian 系を基盤として、二つの独立な問題を扱う。第I部では、有限 Fourier--Gaussian 浴を前後の有限分解能記録で条件づけたとき、繰り込み済み粗視化作用が Nelson 型作用へ収束することを定量的に示す。第II部では、局所測定器、共通未来の比較器、固定総作用を持つ二モード台帳、および時間対称な境界統計原理を組み合わせ、setting-blind な終端条件の整合体積から Bell 型共同確率を得る。

第I部の微視的中核は、有限次元の2次 Hamiltonian と運動量反転対称な Gaussian 初期分布からなる。全軌道は滑らかで可逆であり、観測座標を残して浴を縮約すると有限 Fourier--Gaussian 経路法則が得られる。第1の主要結果は、有限分解能の前後記録で条件づけた線形 Gaussian 経路法則に対するパラメータ $C^1$ 収束定理である。時間刻み $h$ の繰り込み済み粗視化作用を $\mathcal A_{N,h}^{R,U}$ とすると、コンパクトな滑らかな有限次元パラメータ集合 $K$ 上で

$$
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
$$

を得る。$h_N=TN^{-1/3}$ なら右辺は $O(N^{-1/3})$ である。極限作用は正の Gaussian 密度領域で Guerra--Morato 表示と Nelson 表示の双方を持つ。この $C^1$ は任意の無限次元経路変分に関する主張ではなく、指定した有限次元パラメータ族に関する主張である。

第II部はこの Nelson 極限から Bell 重みを導かない。各試行では、左右の局所 analyzer が definite outcome $A,B\in\{\pm1\}$ を anchor pointer に記録し、設定と結果符号を担う二つの実正準ベクトルを記録後の共通未来へ送る。比較器が計算する差動作用は

$$
\overline I_-^{AB}
=
I_0
\left[
1-ABV\cos\Delta_{ab}
\right]
$$

である。ここで cos は確率公理ではなく、二つの実二次元正準ベクトルの内積から生じる。

比較器の未読変数として、一つの soft mode と一つの ledger mode を置く。

$$
J_s=\frac12(q_s^2+p_s^2),
\qquad
J_0=\frac12(q_0^2+p_0^2),
$$

$$
J_\ell=J_s+J_0,
\qquad
E_\ell=\omega_\ell J_\ell.
$$

固定総作用殻 $E_\ell={\rm const.}$ 上の正規化 Liouville 測度に関して、soft energy

$$
h=\omega_\ell J_s
$$

の周辺密度は厳密に

$$
p(h\mid A,B,a,b)
=
\frac1{E_\ell},
\qquad
0\leq h\leq E_\ell
$$

となる。これは旧構成で結果 sector ごとに仮定していた共通入口密度のうち、sector 内の密度形を二モード位相体積から導く結果である。任意の初期 fine-grained 密度が Hamiltonian 発展でこの分布へ強収束するとは主張しない。有限非線形 mixer は固定総作用殻上の向きを粗視化混合する候補機構であり、必要な時間尺度は

$$
\tau_{\rm mix}
\ll
\tau_{\rm cmp}
\ll
T_{\rm rec}
$$

である。

四つの基準 outcome sector の質量は、二モード幾何からは決まらない。preparation Hamiltonian、準備 macroregion、基準 Liouville 測度が二つの独立な符号反転に不変で、四 sector を推移的に入れ替えるとき、

$$
w_{++}=w_{+-}=w_{-+}=w_{--}=\frac14
$$

が従う。本論文ではこの対称準備条件を `[S]` と呼ぶ。従って旧 equilibrium 仮定は、sector 内の一様密度を与える二モード定理と、sector 質量をそろえる準備対称性へ分解される。

時間対称境界統計原理 `[R]` は、基準初期密度 $\rho_S$ と固定 terminal function $G_R$ から物理的履歴測度を

$$
d\mu_R^{a,b}(z_i)
=
\frac{
\rho_S(z_i)
G_R\!\left(\Phi_{a,b}^{T}z_i\right)
}{
Z_{a,b}
}
d\Gamma_i
$$

と定める。`[R]` は有限性、再帰性、時間反転対称性だけから導かれるとは仮定しない。これは Hamilton 方程式とは独立に、どの完結履歴を物理的確率集団とみなすかを定める境界原理である。

本改訂では、抽象的だった return pair に相補的な内部時計の意味を与える。二つの時計対 $(\tau_A,\varrho_A)$、$(\tau_B,\varrho_B)$ を

$$
\bar\tau
=
\frac{\tau_A+\tau_B}{2},
\qquad
Y_R
=
\tau_A-\tau_B,
$$

$$
P_c
=
\varrho_A+\varrho_B,
\qquad
\Pi_R
=
\frac{\varrho_A-\varrho_B}{2}
$$

へ正準変換する。相補的 sector $P_c=0$ では $\varrho_A=\Pi_R$、$\varrho_B=-\Pi_R$ である。従って順序付き時計向き

$$
\varrho_A\geq0,
\qquad
\varrho_B\leq0
$$

を保つ条件は $\Pi_R\geq0$ と一致する。これにより terminal half-space の形と $E_*$ に、それぞれ時計向き保存と向き反転までの初期運動量余裕という正準力学的意味が付く。pulse を順序づける既存の autonomous clock $(\vartheta,J_c)$ は、この内部時計対とは別自由度である。

return pointer の Hamiltonian pulse により

$$
\Pi_R(T)
=
E_*+\kappa I_- -h
$$

を記録し、全設定と全結果に共通な terminal condition

$$
G_R
=
\mathbf1_{\{\Pi_R(T)\geq0\}}
$$

を課す。この条件は setting label、outcome label、cos を引数に持たない。ここで $E_*$ は comparator の定数項ではなく、初期相対時計運動量 $\Pi_R(0)=E_*$ として置ける。comparator kick は $\Delta\Pi_R=\kappa I_- -h$ である。固定作用殻上で

$$
0
\leq
E_*+\kappa\overline I_-^{AB}
\leq
E_\ell
$$

なら、terminal-compatible weight は

$$
W_{AB}(a,b)
=
\frac{w_{AB}}{E_\ell}
\left[
E_*+\kappa I_0
\left(
1-ABV\cos\Delta_{ab}
\right)
\right]
$$

となる。対称準備 $w_{AB}=1/4$ の下で規格化すると、

$$
P_R(A,B\mid a,b)
=
\frac14
\left[
1-ABV_{\rm eff}\cos\Delta_{ab}
\right],
$$

$$
V_{\rm eff}
=
\frac{\kappa I_0}{E_*+\kappa I_0}V
$$

を得る。$E_*=0$ では $V_{\rm eff}=V$ である。四結果の和で cos 項が消えるため $Z_{a,b}$ は設定に依存せず、巨視的な setting frequency を保ったまま、微視的 source posterior は一般に

$$
\rho_R(\lambda\mid a,b)
\neq
\rho_R(\lambda)
$$

となる。各履歴の局所応答は因子化するため、Bell の前提違反は measurement independence に現れる。

本論文の Bell 部分は、順時間的な共有浴ノイズ、ゲート通過速度、長い滞在時間によって過去の結果頻度を作り直す模型ではない。結果確定後の有限浴と reaction coordinate は記録保持、比較、完了事象を物理化するが、試行測度を定めるのは `[R]` である。また、soft mode が複数の通常浴 mode と自由にエネルギー交換すると、

$$
p_N(h)
=
\frac{N}{E_\ell}
\left(
1-\frac h{E_\ell}
\right)^{N-1}
$$

となり、累積重みは線形でなくなる。従って純粋な cos 則に本質的なのは、大きな浴ではなく、一つの soft canonical pair と一つの ledger pair が作る線形位相体積である。

相補的時計は terminal half-space を正準実現するが、$\Pi_R(T)<0$ の軌道を Hamilton 方程式から消去しない。この軌道では時計向きが交換されるだけである。各時計枝をそれぞれの clock-past 境界から準備し、同一 Hamiltonian 履歴として matching する二境界積測度を追加すれば `[R]` の積形式を得るが、その matching rule 自体が追加の統計原理である。また二つの向きに対応する相補的半空間を同じ読出しに対して等重みで平均すると、$x=E_*+\kappa I_-$ に対し

$$
\frac12
\left[
\frac{x}{E_\ell}
+
\left(
1-\frac{x}{E_\ell}
\right)
\right]
=
\frac12
$$

となり、cos 項は消える。従って単なる無向きの $\varrho_A=-\varrho_B$ では足りず、順序付き相補性、または向きと comparator の符号を共変に結ぶ追加構造が必要である。

本論文は `[R]` の物理的必然性、任意初期密度からの厳密な一様化、任意の非平衡準備に対する無信号性、cos 則または Tsirelson 限界の一意な選択、一般の非 Gaussian 状態や節を持つ状態、および Wallstrom の位相量子化問題を解かない。確立するのは、有限 Hamiltonian 測定器、対称準備、二モード台帳、固定 terminal condition、時間対称境界測度を組み合わせたときの明示的な Bell compatibility 定理、および terminal half-space の相補時計実現とその限界である。

## 論理構造

| 階層 | 数学的対象 | 役割 | 状態 |
|---|---|---|---|
| 可逆中核 `[H]` | 有限2次 Hamiltonian | 系と調和浴の微視運動 | 明示構成 |
| Gaussian 縮約 | 有限 Fourier 経路法則 | 観測座標の粗視化 | 厳密計算 |
| Nelson 極限 | 繰り込み作用のパラメータ $C^1$ 収束 | 有効確率力学の変分構造 | 主定理 |
| 局所測定器 `[H]` | bright response、anchor record、有限浴 | definite local record | 明示構成 |
| phase-locked source `[P]` | 二つの実正準ベクトル | 差動作用の cos 幾何 | 準備条件 |
| 対称準備 `[S]` | 符号反転不変な基準測度 | $w_{AB}=1/4$ | 対称性からの系 |
| 二モード台帳 | 固定 $J_s+J_0$ 殻 | $p(h)=1/E_\ell$ | 不変測度について厳密 |
| 粗視化混合 `[M]` | 有限非線形 mixer | 入口測度の典型化 | 時間尺度仮定 |
| 相補的内部時計 | $(\bar\tau,P_c;Y_R,\Pi_R)$ | terminal half-space の正準実現 | 半空間は厳密、測度選択は未導出 |
| 境界統計 `[R]` | $G_R\circ\Phi_{a,b}^{T}$ | 物理的履歴測度 | 独立原理 |
| Bell compatibility | terminal-compatible phase volume | cos 共同確率 | `[H,P,S,M,R]` の下で厳密 |

## 本文構成

第1章は二部の独立性、有限測定窓、五つの仮定 `[H]`、`[P]`、`[S]`、`[M]`、`[R]` を定める。第I部の第2章から第4章は、可逆な調和 Hamiltonian 中核、Gaussian 条件づけ、定量的 $C^1$ Nelson 極限を扱う。第II部の第5章は局所測定器、境界集団、相補的内部時計による terminal half-space の正準実現、第6章は共通未来の比較器と二モード台帳、第7章は終端整合測度と Bell 共同確率、第8章は頑健性、反証条件、証明台帳を扱う。付録は Fourier--Schur 評価、$C^1$ 評価、明示 Hamiltonian、相補時計の二境界 matching と向き平均 no-go、台帳位相体積、Gaussian Nelson 方程式を収録する。
