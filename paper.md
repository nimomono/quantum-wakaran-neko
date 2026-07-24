\chapter*{概要}

\addcontentsline{toc}{chapter}{概要}


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

# 問題設定、二部構成、仮定の台帳

\begin{statusbox}
位置づけ：Nelson 極限と Bell compatibility の論理的独立性を固定し、導出と境界原理を分離する。
\end{statusbox}


## 問題設定

Bell の定理は、局所応答、結果の確定性、測定設定独立性などの仮定を同時に満たす理論が、量子力学の特定の相関を再現できないことを示す \cite{bell1964,chsh1969}。古典的な Hamiltonian 模型が Bell--CHSH 不等式を超える相関を与えるなら、Bell の前提のどこかが外れていなければならない。本論文はこの論理を回避せず、軌道法則、準備測度、終端条件、履歴確率を別々に監査する。

本論文では次の二つの問題を扱う。

1. 可逆な有限 Hamiltonian 系の Gaussian 縮約から、Nelson 型作用をどこまで定量的に得られるか。
2. 有限 Hamiltonian 測定器に時間対称な境界統計原理を加えたとき、setting-blind な終端条件の整合体積から Bell 型共同確率を構成できるか。

第1の問題には、第4章のパラメータ $C^1$ 収束定理として答える。第2の問題には、第7章の二モード台帳 Bell compatibility 定理として答える。ただし第2の定理は、Hamilton 方程式だけから全履歴測度を導く定理ではない。物理的試行測度を定める境界原理 `[R]` を明示的に入力する。

## 二部の論理的独立性

第I部は、有限 Fourier--Gaussian 浴、有限分解能の前後記録、繰り込み済み作用を扱う。中心結果は、作用値と指定した有限次元パラメータ方向の第1変分が Guerra--Morato 型 Nelson 作用へ収束するという定量的定理である。

第II部は、局所 analyzer、definite pointer、共通未来の比較器、二モード台帳、terminal compatibility を扱う。Nelson 極限は Bell 重みを生成しない。両者に共通するのは、有限 Hamiltonian 系を出発点にしても、局所経路法則と全履歴の統計法則を同一視してはならないという方法論である。

従って

$$
\text{finite Hamiltonian core}
\longrightarrow
\text{Nelson action}
$$

と

$$
\text{finite Hamiltonian apparatus}
+
\text{boundary ensemble}
\longrightarrow
\text{Bell statistics}
$$

は別の論理鎖である。第I部だけを用いる読者は第4章で完結でき、第II部だけを検討する読者は `[R]` と準備条件を独立に監査できる。

## 有限閉鎖測定窓

一試行の測定窓では、source、setting controller、局所装置、messenger、比較器、台帳、clock、有限浴を含む有限 Hamiltonian 系を用いる。位相点を $z$、symplectic matrix を $J$ と書けば、

$$
\dot z
=
J\nabla H_{\rm tot}(z)
$$

である。標準時間反転 $\Theta(q,p)=(q,-p)$ に対して、自由 Hamiltonian と各 pulse の時系列を含む自律拡張が時間反転共役を持つよう構成できる。各軌道は滑らかで、位相体積を保存する。

有限閉鎖系には真の attractor も永久記録もない。局所記録が実用的に安定であるという主張は、

$$
\tau_{\rm meas}
\ll
\tau_{\rm record}
\ll
T_{\rm rec}
$$

という有限時間窓に限定する。$\tau_{\rm meas}$ は記録形成時間、$\tau_{\rm record}$ は必要な保持時間、$T_{\rm rec}$ は装置を含む有限系の再帰尺度である。

同一装置で無限回の試行を行うには、さらに仕事貯蔵系、記録消去、浴の再生を含む大きな周期を指定しなければならない。本論文の Bell 定理は一試行の完結履歴測度を扱い、開いた実験室での無限回リセットを確率生成機構として用いない。

## 仮定の台帳

第II部の仮定を次の五つに分ける。

### [H] 有限 Hamiltonian 構成

source、controller、局所測定器、有限 bath、common-future comparator、二モード台帳、return pair、相補的内部時計、pulse scheduler は有限個の canonical pair と滑らかな Hamiltonian で記述される。異なる setting と outcome に別の Hamiltonian function を割り当てない。setting は controller の初期 macroregion、outcome は局所 seed と pointer macroregion で表す。pulse scheduler と相補的内部時計は別自由度であり、前者は操作順序、後者は terminal half-space の正準実現を担う。

### [P] phase-locked source

左右へ送る二つの実二次元 messenger は、共通 phase reference と同じ基準作用を持つ。有限の amplitude mismatch と相対 phase noise は visibility $V$ に含める。この条件は第I部の Gaussian 浴だけから導出されない。

### [S] 対称な基準準備

`[R]` を適用する前の preparation Hamiltonian、準備 macroregion、基準 Liouville 測度は、左右の outcome seed を独立に反転する二つの変換に不変である。四つの seed sector が一つの軌道に沿って相互遷移する必要はない。必要なのは、基準測度に関して四 sector が同じ体積を持つことである。

### [M] 二モード台帳の入口測度

soft mode と ledger mode は比較時刻に固定総作用殻

$$
J_s+J_0
=
\frac{E_\ell}{\omega_\ell}
$$

上の正規化 Liouville 測度を持つ。これを直接の準備条件として用いる場合、soft energy の一様密度は厳密である。有限非線形 mixer による典型化を用いる場合は、任意の fine-grained 初期密度の強収束ではなく、有限分解能観測に対する粗視化混合を要求する。

### [R] 時間対称境界統計原理

基準初期密度 $\rho_S$ と全設定に共通な terminal function $G_R\geq0$ に対し、物理的履歴測度を

$$
d\mu_R^{a,b}(z_i)
=
\frac{
\rho_S(z_i)
G_R\!\left(\Phi_{a,b}^{T}z_i\right)
}{
Z_{a,b}
}
d\Gamma_i,
$$

$$
Z_{a,b}
=
\int
\rho_S(z_i)
G_R\!\left(\Phi_{a,b}^{T}z_i\right)
d\Gamma_i
$$

とする。$G_R$ は setting label、outcome label、目標相関を引数に持たない。`[R]` は有限性、再帰性、時間反転対称性から一意に導かれるとは主張しない。これはどの terminal-compatible histories を物理的 ensemble とみなすかを定める追加の境界統計原理である。相補的内部時計は後に $G_R=\mathbf1_{\{\Pi_R\geq0\}}$ の半空間を時計向き保存条件として実現するが、その半空間だけから物理的履歴測度を選ぶ原理は出ない。

## `[S]` と旧 equilibrium 仮定

旧構成では、四 sector に共通な絶対入口密度を一つの条件として置いていた。本論文ではこれを二つに分解する。

1. sector 内で soft energy が一様であることは、固定総作用を持つ二モード台帳の Liouville 幾何から導く。
2. sector の基準質量が等しいことは、準備測度の独立符号反転対称性から導く。

従って

$$
g_{AB}^{\rm ent}(h)
=
\frac{w_{AB}}{E_\ell}
$$

のうち、$1/E_\ell$ は二モード定理、$w_{AB}=1/4$ は `[S]` の対称性系論である。Hamiltonian の形だけでは初期密度を決められないため、準備測度という統計条件まで消えるわけではない。

## 一試行の物理的時系列

一試行を次の十段階に分ける。

1. phase-locked messenger pair と outcome seed を準備する。
2. 左右の controller macrostate により設定 $a,b$ を選ぶ。
3. 左右の局所 analyzer が messenger を回転し、局所 outcome $A,B$ を生成する。
4. bright response mode が局所信号を受ける。
5. anchor pointer が符号を記録し、局所有限浴が bright transient を分散する。
6. 記録の写しと messenger を通常の時間順序で共通未来へ搬送する。
7. setting-blind comparator が差動作用 $I_-$ を計算する。
8. 相補時計の初期相対運動量を $\Pi_R(0)=E_*$ とし、二モード台帳の soft energy $h$ と差動作用 $\kappa I_-$ による kick を加える。
9. 最終相対時計運動量 $\Pi_R(T)=E_*+\kappa I_- -h$ に固定 terminal macroregion $G_R$ を課す。
10. `[R]` により terminal-compatible histories の規格化測度を物理的試行集団とする。

左と右は局所記録が形成される前には共通浴を持たない。共通未来の相互作用は、すでに確定した記録の写しを処理する。このため Bell 相関を「共有浴ノイズが左右へ順時間的に漏れた結果」とは解釈しない。

## 主要結果

第I部の主要結果は次である。

- 有限 Fourier--Gaussian 条件付き作用の定量的パラメータ $C^1$ Nelson 極限。
- Schur 補完による前後両側条件付き Gaussian 法則。
- 正の Gaussian 密度領域における Guerra--Morato 表示と Nelson 表示の一致。

第II部の主要結果は次である。

- 実二次元比較器の差動作用に対する cos 恒等式。
- 固定総作用を持つ二モード台帳の一様 soft-energy 周辺定理。
- 対称準備から $w_{AB}=1/4$ を得る sector 等体積系論。
- setting-blind return pointer の terminal compatibility 積分。
- 相補的内部時計による terminal half-space の正準実現。
- branch-wise boundary preparation と matching を追加したときの `[R]` 積形式、および相補時計だけでは測度を選べないという限界。
- `[H,P,S,M,R]` の下での Bell 型共同確率。
- measurement independence failure、setting normalization、無信号性、CHSH の監査。
- 通過速度、滞在時間、共有浴漏れが試行頻度を作らないという否定結果。

## 先行研究との位置関係

Nelson の確率力学、確率変分法、Guerra--Morato 作用には確立した先行研究がある \cite{nelson1966,guerra_morato1983,yasue1981,zambrini1986,knorst_lopes2024}。Gaussian 条件づけは固定区間平滑化、相反過程、Schrödinger bridge、経路単位の Gaussian conditioning と関係する \cite{jamison1974,doob1957,leonard2014,chen_georgiou_pavon2016,rauch_tung_striebel1965,wilson_et_al2021,leonard_roelly_zambrini2014}。第I部の新規性は、指定した線形 Gaussian クラスに対し、有限 Fourier 浴から繰り込み作用のパラメータ $C^1$ 極限を明示率付きで与える点に限定される。

時間対称境界条件、局所逆因果模型、measurement independence を緩めた Bell 模型には先行研究がある \cite{wharton2010,wharton_argaman2020,hall2010,leifer_pusey2017,wood_spekkens2015,price_wharton2023,price_wharton2024,argaman2010,hossenfelder_palmer2020,thooft2016}。特に共通未来と境界制約による選別という発想自体は新規ではない。本論文の第II部が追加するのは、局所 pointer、実二次元差動比較器、固定総作用二モード台帳、setting-blind terminal coordinate を一つの有限 Hamiltonian network に接続し、旧共通入口密度を準備対称性と二モード位相体積へ分解する点である。

有限の非線形環境が中心振動子のエネルギー分散と実効熱化を起こし得ることは具体的な古典模型で調べられている \cite{marchiori_deaguiar2011}。ただし本論文は、その結果から任意初期密度の厳密一様化を推論しない。有限 Hamiltonian flow は fine-grained density を保存するため、mixing の使用範囲を粗視化時間頻度に限定する。

## 本論文が主張しないこと

本論文は次を主張しない。

- Bell の全仮定を保った古典模型による Bell 違反。
- `[R]` が有限 Hamiltonian 力学または相補的時計運動量だけから必然的に導かれること。
- 任意の初期台帳分布が厳密に一様密度へ収束すること。
- 局所記録後の共有浴ノイズが過去の outcome frequency を変えること。
- 長い return time または gate flux が結果確率を独立に生成すること。
- 任意の非平衡 preparation に対する no-signalling。
- cos 則または Tsirelson 限界が他の非負重みから一意に選ばれること。
- 第II部の cos 共同確率が Wallstrom の位相量子化問題を解くこと。
- 一般の非 Gaussian 状態、節を持つ波動関数、任意の量子測定、量子場を再現すること。

## 論文の構成

第2章は有限2次 Hamiltonian と Fourier--Gaussian 表示、第3章は前後両側条件付き Gaussian 法則、第4章は定量的 Nelson 極限を扱う。第5章は有限 Hamiltonian 測定器、境界集団、相補時計による terminal half-space の正準実現、第6章は差動比較器と二モード台帳、第7章は terminal compatibility と Bell 統計、第8章は頑健性、反証条件、証明台帳を扱う。付録AとBは第I部の評価、付録Cは第II部の正準計算、相補時計の二境界 matching と向き平均 no-go、位相体積、付録Dは Gaussian Nelson 例を収録する。

\part{有限調和 Gaussian 中核の Nelson 極限}

# 可逆な調和 Hamiltonian 中核と有限 Gaussian 表示

\begin{statusbox}
位置づけ：微視的可逆性と、証明に用いる線形 Gaussian 計算模型の関係を明示する。
\end{statusbox}


## 有限2次 Hamiltonian

位相空間を $\R^{2M}$、正準座標を $Z=(Q,P)$ とし、

$$
H_N(Z)=\frac12 Z^{\mathsf T}G_N Z,
\qquad
G_N=G_N^{\mathsf T}>0
$$

を考える。運動方程式は

$$
\dot Z=JG_NZ,
\qquad
Z(t)=e^{tJG_N}Z(0)
$$

である。$G_N$ が運動量に関して偶であれば、標準時間反転 $\Theta(Q,P)=(Q,-P)$ に対して

$$
\Theta e^{tJG_N}\Theta=e^{-tJG_N}
$$

が成立する。従って全微視軌道は時間反転対称であり、Liouville 体積を保存する。

正準変換で正規モードへ移れば、安定な部分は

$$
H_N
=
\sum_{n=1}^{N}
\frac12
\left(
P_n^2+\omega_n^2Q_n^2
\right)
$$

の形にできる。初期正準変数が中心 Gaussian 分布を持つなら、任意の線形観測量

$$
X_N(t)=L e^{tJG_N}Z(0)+\mu_N(t)
$$

は有限次元 Gaussian 過程である。従って、閉じた調和 Hamiltonian 系の観測座標は、平均と2時刻共分散だけで完全に記述できる。

## 反作用を含む標準的な調和浴

粒子座標 $q$ と調和浴を明示する代表例は

$$
H_{\rm core}
=
\frac{p^2}{2m}+V(q)
+
\sum_{n=1}^{N}
\left[
\frac{P_n^2}{2m_n}
+
\frac{m_n\omega_n^2}{2}
\left(
Q_n-\frac{c_nq}{m_n\omega_n^2}
\right)^2
\right]
$$

である \cite{ford1965,mori1965,zwanzig1973}。平方完成された結合は反作用と周波数補正を同時に含む。浴変数を厳密に消去すると、粒子は有限記憶核を持つ一般化 Langevin 方程式に従う。

$$
m\ddot q(t)
+V'(q(t))
+\int_0^t\Gamma_N(t-s)\dot q(s)\dd s
=
\xi_N(t)+F_{\rm slip}(t).
$$

ここで

$$
\Gamma_N(t)
=
\sum_{n=1}^{N}
\frac{c_n^2}{m_n\omega_n^2}
\cos\omega_nt
$$

であり、$\xi_N$ は浴初期座標の線形結合である。浴初期分布が Gaussian なら $\xi_N$ も有限 Gaussian 過程になる。有限 $N$ では記憶核も雑音も再帰的であり、白色雑音や散逸は微視的な基本法則ではない。

本論文の $C^1$ 定理は、この一般化 Langevin 方程式を任意の非線形 $V$ について直接扱うものではない。調和領域または線形化領域で観測される Gaussian 経路法則を、次節の有限 Fourier 表示で計算する。したがって、閉じた Hamiltonian 中核は微視的な可逆性を支え、線形 Gaussian 模型はその観測法則を計算する簡略表示である。

## 完全な有限 Fourier 浴

時間区間を $[0,T]$、$\omega_n=2\pi n/T$ とする。独立な標準 Gaussian ベクトル $Z_0,A_n,B_n\in\R^d$ を用いて

$$
\widetilde\eta_N(t)
=
\sqrt{\frac{2\nu}{T}}Z_0
+
\sqrt{\frac{4\nu}{T}}
\sum_{n=1}^{N}
\left[
A_n\cos\omega_nt
+B_n\sin\omega_nt
\right]
$$

と定義する。この過程は調和正規モードの初期振幅を読み出すことで実現できる。零周波数 $Z_0$ は保存された正準運動量または自由モードに対応する。

共分散は

$$
\E\left[
\widetilde\eta_N^i(t)
\widetilde\eta_N^j(s)
\right]
=
2\nu\,\delta^{ij}\delta_{T,N}(t-s),
$$

$$
\delta_{T,N}(\tau)
=
\frac1T
+
\frac2T
\sum_{n=1}^{N}\cos\omega_n\tau
$$

である。$\delta_{T,N}$ は周期 Dirichlet 核であり、滑らかな試験関数に対して周期デルタ分布へ収束する。

零周波数を最初から除いた

$$
2\nu
\left[
\delta_{T,N}(t-s)-\frac1T
\right]
$$

を普遍的な浴共分散とみなしてはならない。これは全ての線形系に共通な浴ではなく、自由増分の全期間積分を零にする条件を課したときに現れる特殊な条件付き共分散である。一般の線形な流れでは、終端条件による共分散修正は流れと観測行列に依存する Schur 補完になる。

## 線形 Gaussian 計算模型

実際の証明では、観測座標を

$$
\dot X_N(t)
=
F_\theta(t)X_N(t)
+f_\theta(t)
+\widetilde\eta_N(t),
\qquad
X_N(0)\sim N(m_{0,\theta},P_{0,\theta})
$$

で表す。$\theta$ は質量、周波数、外力、終端記録などをまとめた有限次元パラメータである。$F_\theta$ と $f_\theta$ は時間について十分滑らかとする。

基本行列 $\Phi_\theta(t,s)$ を

$$
\partial_t\Phi_\theta(t,s)
=
F_\theta(t)\Phi_\theta(t,s),
\qquad
\Phi_\theta(s,s)=I
$$

で定めると、

$$
X_N(t)
=
\Phi_\theta(t,0)X_N(0)
+\int_0^t
\Phi_\theta(t,s)
\left[
f_\theta(s)+\widetilde\eta_N(s)
\right]
\dd s
$$

である。従って $X_N$ は有限個の Gaussian 変数の線形像であり、平均 $\mu_N$ と共分散 $C_N$ を有限和として厳密に計算できる。

この方程式を微視的な一方向駆動と解釈する必要はない。調和 Hamiltonian 系の観測 Gaussian 法則を生成する最小の確率表示として用いる。作用、条件付き平均、条件付き共分散、および第1変分は経路法則だけで決まり、同じ平均と共分散を持つ Hamiltonian 正規モード表示と一致する。

## 極限拡散

$N\to\infty$ で積分雑音

$$
W_N(t)=\int_0^t\widetilde\eta_N(s)\dd s
$$

は、有限次元分布で共分散 $2\nu\min(s,t)$ を持つ Wiener 増分へ近づく。本論文の作用とパラメータ第1微分は2時刻の平均・共分散だけで評価するため、一般の経路空間位相における弱収束は主定理の仮定にも結論にも用いない。対応する線形拡散表示は

$$
\dd X(t)
=
\left[
F_\theta(t)X(t)+f_\theta(t)
\right]\dd t
+\sqrt{2\nu}\,\dd W_t
$$

である。有限 $N$ の各経路は微分可能であるが、極限経路は微分不可能である。粗視化作用に現れる発散は、この正則性の変化に由来する。

## OU 模型と Stratonovich 表現

$F=-\lambda I+\Omega J$ と選べば、2次元の回転を伴う OU 位相模型が得られる。これは減衰する位相振幅を扱う便利な具体例である。しかし OU の摩擦は縮約後の有効係数であり、微視的 Hamiltonian 中核そのものが時間反転を破ることを意味しない。本論文では OU 模型を基礎仮定とせず、付録Dの例として用いる。

雑音係数が状態に依存しないため、Itô 表現と Stratonovich 表現の変換補正は零である。従って、どちらの記法を選んでも本論文の線形 Gaussian 定理は変わらない。Stratonovich 微分は中心論証に必要ないため、以後は Itô 表現に統一する。

## 本章の結論

有限調和 Hamiltonian 系は、微視的可逆性と有限 Gaussian 経路法則を同時に与える。実際の計算には、同じ Gaussian 法則を持つ線形方程式を用いる。白色拡散は有限モードの特異極限であり、終端条件は浴そのものではなく Gaussian 条件づけとして導入する。次章では、その条件づけを有限 $N$ と極限拡散の双方で厳密に記述する。

# 前後両側から条件づけた線形 Gaussian 経路法則

\begin{statusbox}
位置づけ：有限分解能の終端記録を Gaussian Schur 補完として厳密に定義する。
\end{statusbox}


## なぜ有限分解能を用いるか

前章の $X_N$ に対し、初期側では Gaussian 準備分布を与え、終端側では測定装置が残す有限分解能の記録を条件として用いる。終端位置をデルタ関数で厳密固定すると、極限拡散の終端近傍で流れが特異になり、$C^1$ 評価に不要な境界層が生じる。実在する測定記録は有限分解能を持つため、本論文では正定値の読み出し雑音を含む条件づけを主定理に採用する。

時刻 $T$ の記録を

$$
Y=HX_N(T)+\varepsilon,
\qquad
\varepsilon\sim N(0,R),
\qquad
R\geq r_*I>0
$$

とする。実際に得られた記録値を $y$ とする。この条件は、尤度

$$
L_R(x)
=
\exp\left[
-\frac12(Hx-y)^{\mathsf T}R^{-1}(Hx-y)
\right]
$$

で経路を重みづけすることと同値である。

## 無条件 Gaussian 法則

有限 $N$ の平均と2時刻共分散を

$$
\mu_N(t)=\E[X_N(t)],
$$

$$
C_N(s,t)
=
\E\left[
(X_N(s)-\mu_N(s))
(X_N(t)-\mu_N(t))^{\mathsf T}
\right]
$$

とする。基本行列を使えば、平均は

$$
\mu_N(t)
=
\Phi(t,0)m_0
+\int_0^t\Phi(t,r)f(r)\dd r
$$

であり、共分散は初期共分散と有限 Fourier モードの寄与の和として書ける。

雑音を基底関数 $e_\alpha(t)$ と独立 Gaussian 係数 $\zeta_\alpha$ で

$$
\widetilde\eta_N(t)
=
\sum_{\alpha=0}^{2N}e_\alpha(t)\zeta_\alpha
$$

と書けば、

$$
K_{N,\alpha}(t)
=
\int_0^t\Phi(t,r)e_\alpha(r)\dd r
$$

により

$$
C_N(s,t)
=
\Phi(s,0)P_0\Phi(t,0)^{\mathsf T}
+\sum_{\alpha=0}^{2N}
K_{N,\alpha}(s)K_{N,\alpha}(t)^{\mathsf T}
$$

となる。この表示は、条件づけとパラメータ微分を有限行列計算へ帰着させる。

## Schur 補完による条件付き平均と共分散

記録共分散を

$$
S_N
=
HC_N(T,T)H^{\mathsf T}+R
$$

とする。$R\geq r_*I$ なので $S_N$ は一様に可逆である。

\begin{proposition}[有限 Gaussian 条件づけ]
条件 $Y=y$ の下で $X_N$ は Gaussian 過程のままであり、その平均と共分散は

$$
\mu_N^R(t)
=
\mu_N(t)
+C_N(t,T)H^{\mathsf T}S_N^{-1}
\left[y-H\mu_N(T)\right],
$$

$$
C_N^R(s,t)
=
C_N(s,t)
-C_N(s,T)H^{\mathsf T}S_N^{-1}HC_N(T,t)
$$

である。
\end{proposition}

\begin{proof}
有限個の時刻 $t_1,\ldots,t_k$ を固定すると、$(X_N(t_1),\ldots,X_N(t_k),Y)$ は結合 Gaussian ベクトルである。結合共分散行列の $Y$ 成分に関する Schur 補完を取れば上式を得る。任意の有限時刻集合で整合するため、条件付き過程全体が定まる。
\end{proof}

条件付き共分散の第2項は、終端記録により減少した不確かさを表す。これは力ではない。ある経路が終端記録とどれだけ整合するかという統計的更新である。

この計算は、新しい種類の Gaussian 条件づけではない。有限次元の状態を拡大して Fourier 係数まで含めれば、固定区間の線形 Gaussian 平滑化と同じ Schur 補完になる \cite{rauch_tung_striebel1965}。経路測度の立場では相反過程および Schrödinger 橋の線形 Gaussian 部分に属し \cite{jamison1974,leonard2014,chen_georgiou_pavon2016,leonard_roelly_zambrini2014}、経路単位の Gaussian 条件づけとしても標準的に表せる \cite{wilson_et_al2021}。本論文で必要なのは、この既知の条件づけを有限 Fourier 切断数 $N$ とパラメータ $\theta$ について一様に微分し、第4章の定量的 $C^1$ 評価へ接続することである。

## パラメータ微分

$F_\theta$ の変分 $\delta F$ に対して基本行列の第1変分は

$$
D\Phi_\theta[\delta F](t,s)
=
\int_s^t
\Phi_\theta(t,r)
\delta F(r)
\Phi_\theta(r,s)
\dd r
$$

である。逆行列の微分

$$
D(S^{-1})[\delta S]
=
-S^{-1}(\delta S)S^{-1}
$$

と合わせると、$\mu_N^R$、$C_N^R$ のパラメータ第1微分を明示できる。$S_N\geq r_*I$ により、条件づけの微分は $N$ に依存しない定数で制御される。

有限分解能 $R>0$ は、物理的に自然であるだけでなく、数学的にも重要である。$R=0$ で $H$ が全座標を固定すると、終端に近づくにつれて条件付き流れが $(T-t)^{-1}$ 型に発散し得る。点終端は $R\downarrow0$ の別極限として扱うべきであり、主定理には含めない。

## 極限拡散の条件付き流れ

$N\to\infty$ の無条件拡散を

$$
\dd X_t=b(X_t,t)\dd t+\sqrt{2\nu}\,\dd W_t,
\qquad
b(x,t)=F(t)x+f(t)
$$

とする。終端尤度の後方伝播を

$$
h_R(x,t)
=
\E\left[L_R(X_T)\mid X_t=x\right]
$$

と置く。線形 Gaussian 系では $h_R$ は指数2次関数で正である。条件付き前進流れは Doob 変換により

$$
b_+^R(x,t)
=
b(x,t)+2\nu\nabla\log h_R(x,t)
$$

となる \cite{jamison1974,doob1957}。$\nabla\log h_R$ は $x$ の1次式であるため、条件付き過程も線形 Gaussian である。

条件付き時刻密度を $\rho^R(x,t)$ とすると、後退流れは

$$
b_-^R(x,t)
=
b_+^R(x,t)-2\nu\nabla\log\rho^R(x,t)
$$

である。そこで

$$
v^R
=
\frac{b_+^R+b_-^R}{2},
\qquad
u^R
=
\frac{b_+^R-b_-^R}{2}
=
\nu\nabla\log\rho^R
$$

と定義する。$v^R$ は確率流の速度、$u^R$ は密度勾配に伴う浸透速度である。

## 自由系で現れる $-1/T$

$F=0$、$f=0$、$X_N(0)=x_0$ とし、終端を厳密に $X_N(T)=x_0$ へ固定する特殊な場合を考える。非零 Fourier モードは1周期積分すると零になるため、全期間変位を担うのは零周波数 $Z_0$ だけである。終端条件は $Z_0=0$ を意味する。従って条件付き雑音共分散は

$$
\E\left[
\widetilde\eta_N(t)
\widetilde\eta_N(s)^{\mathsf T}
\mid X_N(T)=x_0
\right]
=
2\nu
\left[
\delta_{T,N}(t-s)-\frac1T
\right]I.
$$

ここで初めて $-1/T$ が現れる。一般の $F\neq0$ では終端値は全 Fourier モードの線形結合に依存するため、条件付き修正は

$$
-\operatorname{Cov}(\widetilde\eta_N,Y)
\operatorname{Cov}(Y,Y)^{-1}
\operatorname{Cov}(Y,\widetilde\eta_N)
$$

という流れ依存の Schur 補完であり、単純な $-1/T$ ではない。

## 前後両側条件づけの物理的意味

初期準備と終端記録の双方を知った後に、途中経路の統計を求めることは、通常の条件付き確率である。終端記録が途中経路の条件付き平均を変えることは、終端装置が過去へ力を送ることを意味しない。

ただし、条件付き経路分布を物理的試行頻度として採用するには、どの完結履歴へ確率を置くかという追加の物理原理が必要である。Gaussian Schur 補完は、記録を与えた後の条件付き法則を計算するが、その法則が実験の無条件頻度として選ばれることまでは証明しない。第II部ではこの役割を時間対称境界統計原理 `[R]` として明示し、第4章の Nelson 極限からは導かない。

## 本章の結論

有限分解能の終端記録を用いれば、前後両側から条件づけた経路法則は通常の Gaussian Schur 補完として完全に定義できる。条件付き平均、共分散、そのパラメータ微分は一様に制御される。次章では、この安定性を用いて、有限浴の繰り込み済み作用とその第1変分を Nelson 極限へ移す。

# 繰り込み済み粗視化作用の Nelson 極限

\begin{statusbox}
位置づけ：線形 Gaussian・有限分解能・2次ポテンシャルの範囲で定量的 $C^1$ 収束を示す。
\end{statusbox}


## 粗視化作用

有限 $N$ の経路は微分可能であるが、$N\to\infty$ の拡散経路は微分不可能である。そのため、単純な運動エネルギー

$$
\frac m2\int_0^T|\dot X_N(t)|^2\dd t
$$

は極限で発散する。時間分解能 $h>0$ を固定し、有限差分

$$
D_hX_N(t)=\frac{X_N(t+h)-X_N(t)}{h}
$$

を用いる。拡散係数が $\nu$、空間次元が $d$ なら、雑音の普遍的発散は

$$
\frac m2\E|D_hX|^2
\sim
\frac{md\nu}{h}
$$

である。

差分商の運動項から軌道に依存しない発散定数を除き、有限な Guerra--Morato 項を残す原理自体は既知である \cite{nelson1966,guerra_morato1983}。本章の新規な主張は、有限 Fourier 切断、有限分解能の終端記録、滑らかな有限次元パラメータ族を同時に扱い、作用値とその第1偏微分へ共通の明示誤差評価を与える点にある。

外部ポテンシャルを $U_\theta(x,t)$ と書き、条件付き経路法則に対する繰り込み済み作用を

$$
\mathcal A_{N,h}^{R,U}(\theta)
=
\E_{N,\theta}^{R}
\int_0^{T-h}
\left[
\frac m{2h^2}
|X_N(t+h)-X_N(t)|^2
-\frac{md\nu}{h}
-U_\theta(X_N(t),t)
\right]\dd t
$$

と定義する。差し引く項は結果や設定に依存せず、有限差分の Gaussian 自己揺らぎだけを除く。

## 許容するパラメータ族

パラメータ集合 $K\subset\R^p$ をコンパクトとする。次を仮定する。

1. $F_\theta(t)$、$f_\theta(t)$ は $(\theta,t)$ について $C^2$ であり、$K\times[0,T]$ 上で2階まで一様有界である。
2. 初期平均 $m_{0,\theta}$ と初期共分散 $P_{0,\theta}$ は $C^2$ で、$P_{0,\theta}\geq p_*I>0$ である。
3. 終端観測 $H_\theta$、$y_\theta$、$R_\theta$ は $C^2$ で、$R_\theta\geq r_*I>0$ である。
4. 外部ポテンシャルは

$$
U_\theta(x,t)
=
\frac12x^{\mathsf T}K_\theta(t)x
+\ell_\theta(t)^{\mathsf T}x
+c_\theta(t)
$$

の形で、係数は $C^2$ かつ一様有界である。
5. Fourier 切断数 $N$ と粗視化幅 $h=h_N$ は

$$
h_N\longrightarrow0,
\qquad
N\left(\frac{h_N}{T}\right)^2\longrightarrow\infty
$$

を満たす。

$C^1(K)$ は作用値と $\theta$ に関する全ての第1偏微分の一様ノルムを表す。この定理は、任意の非線形な経路変分についての無限次元 $C^1$ 定理ではなく、指定した線形 Gaussian パラメータ族上の定理である。

## 極限作用

極限の条件付き拡散の前進流れを $b_{+,\theta}^R$、時刻密度を $\rho_\theta^R$ とする。Guerra--Morato 型作用を

$$
\mathcal A_{\GM}^{R,U}(\theta)
=
\int_0^T\int_{\R^d}
\rho_\theta^R(x,t)
\left[
\frac m2|b_{+,\theta}^R(x,t)|^2
+m\nu\nabla\cdot b_{+,\theta}^R(x,t)
-U_\theta(x,t)
\right]
\dd x\dd t
$$

と定義する \cite{guerra_morato1983}。線形 Gaussian 系では $b_+^R$ は $x$ の1次式、$\rho^R$ は正の Gaussian 密度なので、全ての積分は有限である。

## 線形 Gaussian $C^1$ 収束定理

\begin{theorem}[線形 Gaussian $C^1$ 極限]
第4.2節の仮定を満たすとする。ある定数 $C_K<\infty$ が存在し、十分大きい $N$ と $0<h<T/4$ に対して

$$
\left\|
\mathcal A_{N,h}^{R,U}
-
\mathcal A_{\GM}^{R,U}
\right\|_{C^1(K)}
\leq
C_K
\left(
\frac hT
+
\frac{T^2}{Nh^2}
\right)
$$

が成立する。従って $h_N\to0$ かつ $N(h_N/T)^2\to\infty$ なら

$$
\mathcal A_{N,h_N}^{R,U}
\longrightarrow
\mathcal A_{\GM}^{R,U}
\quad\text{in }C^1(K).
$$

特に $h_N=TN^{-1/3}$ なら誤差は $O(N^{-1/3})$ である。
\end{theorem}

この $N^{-1/3}$ は、共分散尾部を $O(N^{-1})$ と評価し、増分商の $h^{-2}$ と釣り合わせた現在の証明から得られる率である。下界または最適性は示していない。より滑らかな核、端点適合基底、相殺を用いれば改善される可能性があり、本質的な普遍指数とは主張しない。

\begin{proof}
証明は4段階からなる。詳細な評価は付録Bに示す。

第1に、線形解写像の核

$$
G_\theta(t,s)=\mathbf 1_{s\leq t}\Phi_\theta(t,s)
$$

の Fourier 係数は $O(n^{-1})$ であり、$\theta$ 微分後も同じ評価を持つ。従って共分散とその第1微分の切断尾部は一様に $O(T^2/N)$ である。

第2に、$R_\theta\geq r_*I$ により記録共分散 $S_N$ の逆行列は一様有界である。Schur 補完の式を微分すると、条件付き平均、共分散、その第1微分も $O(T^2/N)$ で極限へ収束する。

第3に、極限条件付き Gaussian 拡散の平均と共分散を $h$ について展開する。共分散の時間対角には $2\nu hI$ の折れ曲がりがあり、

$$
\frac1{h^2}\E^R|X(t+h)-X(t)|^2
=
\frac{2d\nu}{h}
+\E^R
\left[
|b_+^R(X_t,t)|^2
+2\nu\nabla\cdot b_+^R(X_t,t)
\right]
+O(h/T)
$$

が一様に成立する。$md\nu/h$ を差し引くと Guerra--Morato の運動項が残る。2次ポテンシャルの期待値は平均と共分散だけで決まるため、同じ展開を直接適用できる。

第4に、有限 $N$ と極限の増分共分散差は $O(T^2/N)$ である。作用では $h^{-2}$ が掛かるため、この誤差は $O(T^2/(Nh^2))$ となる。全ての式を $\theta$ で微分し、基本行列と Schur 補完の第1微分評価を使えば同じ上界を得る。4つの誤差を合わせて主張が従う。
\end{proof}

## Guerra--Morato 表示と Nelson 表示

前進・後退流れから

$$
v^R=\frac{b_+^R+b_-^R}{2},
\qquad
u^R=\frac{b_+^R-b_-^R}{2}
=\nu\nabla\log\rho^R
$$

を定義する。境界項が消える条件、例えば全空間での Gaussian 減衰、周期境界、または無流束境界を仮定する。

\begin{theorem}[Guerra--Morato 作用と Nelson 作用の一致]

$$
\mathcal A_{\GM}^{R,U}
=
\mathcal A_{\Nel}^{R,U},
$$

$$
\mathcal A_{\Nel}^{R,U}
=
\int_0^T\int_{\R^d}
\rho^R
\left[
\frac m2|v^R|^2
-\frac m2|u^R|^2
-U
\right]
\dd x\dd t.
$$
\end{theorem}

\begin{proof}
$b_+^R=v^R+u^R$ と $\nu\nabla\rho^R=\rho^Ru^R$ を用いる。空間部分積分により

$$
\int\rho^R m\nu\nabla\cdot b_+^R\dd x
=
-m\int\rho^R b_+^R\cdot u^R\dd x.
$$

従って

$$
\frac m2|b_+^R|^2
-m b_+^R\cdot u^R
=
\frac m2|v^R|^2
-\frac m2|u^R|^2.
$$

ポテンシャル項は共通なので結論を得る。
\end{proof}

この一致は近似ではない。$C^1$ 極限で得られた Guerra--Morato 作用は、正の Gaussian 密度領域では Nelson 作用そのものである \cite{nelson1966,guerra_morato1983,yasue1981,zambrini1986}。Guerra--Morato 作用の臨界点と第2変分を扱う近年の研究もあるが \cite{knorst_lopes2024}、本定理が扱う有限 Fourier 条件付き族の2尺度 $C^1$ 収束とは問題設定が異なる。

## 停留点について言えること

\begin{corollary}[収束する停留点]
$\theta_N\in\operatorname{int}K$ が

$$
D_\theta\mathcal A_{N,h_N}^{R,U}(\theta_N)=0,
\qquad
\theta_N\longrightarrow\theta_*
$$

を満たすなら、

$$
D_\theta\mathcal A_{\Nel}^{R,U}(\theta_*)=0
$$

である。
\end{corollary}

\begin{proof}
$C^1(K)$ 収束と $D\mathcal A_{N,h_N}(\theta_N)=0$ から

$$
\|D\mathcal A_{\Nel}(\theta_*)\|
\leq
\|D\mathcal A_{\Nel}(\theta_*)-D\mathcal A_{\Nel}(\theta_N)\|
+
\|D\mathcal A_{\Nel}(\theta_N)-D\mathcal A_{N,h_N}(\theta_N)\|
\longrightarrow0.
$$
\end{proof}

これは一方向の主張である。任意の Nelson 停留点が有限浴の停留点列から得られることには、Hessian の非退化性と少なくとも局所 $C^2$ 収束が必要である。また、微視的 Hamiltonian 方程式が粗視化作用の停留点を力学的に選ぶことは、この系からは従わない。

## 調和 Gaussian の物理像

1次元で

$$
\rho(x,t)
=
\frac1{\sqrt{2\pi}\sigma(t)}
\exp\left[
-\frac{(x-q(t))^2}{2\sigma(t)^2}
\right]
$$

とし、連続の式を満たす速度を

$$
v(x,t)
=
\dot q(t)
+\frac{\dot\sigma(t)}{\sigma(t)}[x-q(t)]
$$

とする。浸透速度は

$$
u(x,t)
=
-\nu\frac{x-q(t)}{\sigma(t)^2}
$$

である。調和ポテンシャル $U=m\Omega^2x^2/2$ に対する Nelson 作用は

$$
\mathcal A_G[q,\sigma]
=
\frac m2
\int_0^T
\left[
\dot q^2+\dot\sigma^2
-\frac{\nu^2}{\sigma^2}
-\Omega^2(q^2+\sigma^2)
\right]\dd t.
$$

変分すると

$$
\ddot q+\Omega^2q=0,
$$

$$
\ddot\sigma+\Omega^2\sigma
-\frac{\nu^2}{\sigma^3}=0
$$

を得る。中心は古典的な調和運動を行い、幅は通常の拡散で単調に広がるのではなく、調和閉じ込めと密度勾配の項の釣り合いで振動する。定常幅は

$$
\sigma_*^2=\frac\nu\Omega
$$

である。これは Nelson 作用が、単なる熱拡散ではなく、確率流と密度勾配の前後対称な変分力学を表すことを示す。

## 定理の範囲

本章で証明したのは線形 Gaussian 範囲の $C^1$ 極限である。次は主定理に含まれない。

- 状態依存の非線形な流れ。
- 退化した点終端 $R=0$。
- 硬いしきい値条件による非滑らかな経路選択。
- 2次を超える一般ポテンシャルに対する一様第1変分評価。
- 密度の節を横切る大域位相。
- 全ての Nelson 変分を尽くす無限次元 $C^1$ 収束。

これらを未証明のまま主定理へ含めるより、線形 Gaussian 定理を完結した形で提示する方が理論の見通しはよい。

\part{時間対称境界測度と二モード台帳による Bell 型統計}

# 有限 Hamiltonian 測定器と時間対称境界集団

\begin{statusbox}
位置づけ：局所 definite record と全履歴測度を分離し、`[R]` を第II部の確率原理として明示する。
\end{statusbox}


## 第II部の目的

第2章から第4章は、観測座標の線形 Gaussian 経路法則と Nelson 作用を扱った。そこから Bell 型結果重みは出ない。Bell 実験を記述するには、少なくとも次の構造が必要である。

1. 左右の setting controller。
2. 局所的に確定する2値 record。
3. 設定と結果符号を共通未来へ運ぶ messenger。
4. 二つの messenger を比較する setting-blind な二次形式。
5. 比較結果と未読台帳変数を照合する terminal coordinate。
6. terminal-compatible histories を物理的集団とする境界統計原理。

本章では1、2、3、5、6を有限 Hamiltonian 系として定式化する。比較器の cos 幾何と二モード台帳は第6章、共同確率は第7章で扱う。

## 正準変数

一試行の第II部に必要な正準変数を次のように取る。

- messenger pairs：$(Q_A,P_A)$、$(Q_B,P_B)$。
- outcome-seed pairs：$(s_A,\pi_A)$、$(s_B,\pi_B)$。
- setting-controller pairs：$(a,\alpha)$、$(b,\beta)$。
- bright response pairs：$(x_A,p_A)$、$(x_B,p_B)$。
- anchor-pointer pairs：$(Y_A,\Pi_A)$、$(Y_B,\Pi_B)$。
- local finite-bath pairs：$(r_{Xj},\varpi_{Xj})$、$X=A,B$、$1\leq j\leq n_X$。
- ledger pairs：$(q_s,p_s)$、$(q_0,p_0)$。
- return-comparator pair：$(Y_R,\Pi_R)$。
- complementary-clock center pair：$(\bar\tau,P_c)$。
- autonomous-clock pair：$(\vartheta,J_c)$。

messenger action を

$$
I_X
=
\frac12
\left(
Q_X^2+P_X^2
\right),
\qquad
X=A,B
$$

とする。ledger の二つの作用は

$$
J_s
=
\frac12
\left(
q_s^2+p_s^2
\right),
$$

$$
J_0
=
\frac12
\left(
q_0^2+p_0^2
\right)
$$

である。全 Hamiltonian の構造は

$$
H_{\rm tot}
=
H_{\rm src}
+H_{\rm ctrl}
+H_{\rm msg}
+H_{\rm seed}
+H_{\rm ptr}
+H_{\rm bath}
+H_\ell
+H_{\rm mix}
+H_{\rm cmp}
+H_{\rm or}
+H_{\rm clk}.
$$

各項の具体形は付録Cにまとめる。本章では各操作を有限時間の canonical map として明示する。

## outcome seed と設定 controller

$s_X$ を circle coordinate とし、互いに等しい Liouville 体積を持つ二つの plateau region $\Sigma_X^+$、$\Sigma_X^-$ を取る。滑らかな周期関数 $\sigma$ を

$$
\sigma(s)
=
+1
\qquad
\left(
s\in\Sigma^+
\right),
$$

$$
\sigma(s)
=
-1
\qquad
\left(
s\in\Sigma^-
\right)
$$

とし、二領域の間だけで滑らかに補間する。基準 preparation は補間領域に support を持たない。従って実際の support 上で

$$
\sigma'(s)=0.
$$

局所結果を

$$
A=\sigma(s_A),
\qquad
B=\sigma(s_B)
$$

とする。負符号 sector の indicator は

$$
\chi_-(s)
=
\frac{1-\sigma(s)}2
$$

である。

setting は controller coordinate の初期 macroregion で決まる。全試行に同じ Hamiltonian function を用い、

$$
a=\mathfrak a(\xi_A),
\qquad
b=\mathfrak b(\xi_B)
$$

という coarse map で設定を読み出す。以下では controller coordinate 自体を簡単に $a,b$ と書く。

この最小模型では outcome seed を明示的に置く。より一般の局所決定論 response

$$
A=\mathscr A(a,\lambda_A),
\qquad
B=\mathscr B(b,\lambda_B)
$$

も、局所 canonical preprocessing の後に同じ plateau record へ写せる。Bell 監査に必要なのは、fixed complete microstate における左の response が右の setting を参照せず、右も同様であることだけである。

## autonomous pulse Hamiltonian

clock angle $\vartheta$ 上に、互いに重ならない滑らかな profile $f_\nu(\vartheta)$ を置き、

$$
\int f_\nu(\vartheta)d\vartheta=1
$$

と規格化する。全 Hamiltonian に

$$
H_{\rm clk}
=
\Omega J_c
$$

と pulse 項

$$
H_{\rm pulse}
=
\Omega
\sum_\nu
f_\nu(\vartheta)K_\nu
$$

を加える。各 $K_\nu$ は $J_c$ に依存しないため、

$$
\dot\vartheta
=
\frac{\partial H_{\rm tot}}{\partial J_c}
=
\Omega
$$

が厳密に成立する。従って各 profile は生成子 $K_\nu$ の unit flow を実行する。clock action $J_c$ が pulse の backreaction を吸収し、拡張した全 Hamiltonian energy は保存される。

この自律化は、外部から setting ごとに異なる Hamiltonian を挿入する操作ではない。setting は phase space 内の controller state、操作順序は同じ clock orbit 上の異なる区間である。$(\vartheta,J_c)$ は pulse scheduler であり、第5.9節で導入する相補的内部時計ではない。両者を同一視すると、内部時計を逆向きに動かす Hamiltonian へ替えたときに pulse の単調な順序づけが失われるため、独立な canonical pair として保持する。

## 局所 analyzer と bright response

A 側の analyzer generator を

$$
K_A^{\rm an}
=
-\left[
\phi(a)
+\pi\chi_-(s_A)
\right]I_A
-x_A\sigma(s_A)
$$

とし、B 側も同様に

$$
K_B^{\rm an}
=
-\left[
\phi(b)
+\pi\chi_-(s_B)
\right]I_B
-x_B\sigma(s_B)
$$

とする。

$K_A^{\rm an}$ の unit flow parameter を $\tau$ とすると、seed plateau 上で

$$
\frac{dQ_A}{d\tau}
=
-\theta_A P_A,
\qquad
\frac{dP_A}{d\tau}
=
\theta_A Q_A,
$$

$$
\theta_A
=
\phi(a)+\pi\chi_-(s_A),
$$

および

$$
\frac{dp_A}{d\tau}
=
\sigma(s_A)=A,
\qquad
\frac{dx_A}{d\tau}=0
$$

を得る。bright momentum を $p_A^{\rm in}=0$ に準備すれば、

$$
p_A^{\rm out}=A.
$$

messenger は

$$
\begin{pmatrix}
Q_A\\
P_A
\end{pmatrix}_{\rm out}
=
R[\theta_A]
\begin{pmatrix}
Q_A\\
P_A
\end{pmatrix}_{\rm in}
=
A R[\phi(a)]
\begin{pmatrix}
Q_A\\
P_A
\end{pmatrix}_{\rm in}
$$

となる。B 側も

$$
p_B^{\rm out}=B,
$$

$$
u_B^{\rm out}
=
B R[\phi(b)]u_B^{\rm in}
$$

を満たす。

bright mode は setting pulse と local seed に強く応答する一時変数である。outcome probability を生成する浴ではない。各 trajectory の $A,B$ は seed と局所 Hamiltonian flow で一意に決まる。

## anchor pointer への記録固定

滑らかな plateau function $\zeta(p)$ を

$$
\zeta(p)=+1
\quad
\left(
|p-1|<\delta_p
\right),
$$

$$
\zeta(p)=-1
\quad
\left(
|p+1|<\delta_p
\right)
$$

となるよう取る。anchor transfer generator を

$$
K_X^{\rm lock}
=
-Y_X\zeta(p_X)
$$

とする。unit flow では

$$
\frac{d\Pi_X}{d\tau}
=
\zeta(p_X),
\qquad
\frac{dY_X}{d\tau}=0,
\qquad
\frac{dp_X}{d\tau}=0.
$$

従って $\Pi_X^{\rm in}=0$ なら

$$
\Pi_A^{\rm out}=A,
\qquad
\Pi_B^{\rm out}=B.
$$

二つの disjoint macroregion

$$
\Gamma_X^+
=
\left\{
\Pi_X>\frac12
\right\},
\qquad
\Gamma_X^-
=
\left\{
\Pi_X<-\frac12
\right\}
$$

を pointer record とする。anchor pair はこの後の common-future comparator から decouple される。従って comparison stage は過去の pointer sign を変更しない。

bright mode には、記録後に有限局所浴

$$
H_{{\rm bath},X}
=
\sum_{j=1}^{n_X}
\left[
\frac{\varpi_{Xj}^2}{2m_{Xj}}
+\frac{m_{Xj}\omega_{Xj}^2r_{Xj}^2}{2}
\right]
+\epsilon_X x_X
\sum_{j=1}^{n_X}
c_{Xj}r_{Xj}
$$

を結合できる。これは bright transient と位相情報を複数自由度へ分散し、有限観測窓での再読出し誤差を小さくする。ただし有限閉鎖浴は真の散逸を与えず、十分長時間では recurrence を持つ。record の主張は

$$
\tau_{\rm lock}
\ll
\tau_{\rm cmp}
\ll
T_{{\rm rec},X}
$$

の範囲に限る。

## common-future propagation

局所記録時刻を $t_A,t_B$、両 messenger が同じ時空領域へ到達できる時刻を $t_C$、terminal time を $T$ とし、

$$
t_A,t_B<t_C<T
$$

とする。$t_C$ より前の coupling graph は

$$
(u_A,s_A,a,x_A,Y_A,\Gamma_{{\rm bath},A})
$$

と

$$
(u_B,s_B,b,x_B,Y_B,\Gamma_{{\rm bath},B})
$$

に分離する。A 側の Hamiltonian は B 側の setting、seed、pointer を含まず、B 側も同様である。

$t_C$ 以後に二つの messenger を同じ comparator へ入れる。これは局所記録後の timelike common future における通常の相互作用であり、spacelike separated な記録形成へ遠隔 force を導入しない。第7章で現れる setting dependence は、common-future interaction 自体が過去を変更するためではなく、その interaction を含む全軌道に terminal boundary measure `[R]` を適用するためである。

## terminal function と履歴測度

初期 hypersurface 上の全 microstate を

$$
z_i=(\lambda,\eta,\xi_A,\xi_B)
$$

とする。$\lambda$ は outcome response を完結させる source と局所装置の変数、$\eta$ は後に積分する ledger、mixer、return pointer などの未読変数、$\xi_A,\xi_B$ は setting controller である。基準準備では

$$
\rho_S(\lambda,\eta,\xi_A,\xi_B)
=
\rho_S(\lambda,\eta)
\rho_A(\xi_A)
\rho_B(\xi_B)
$$

とする。

終端時刻 $T$ に、全設定と全 outcome に共通な非負関数

$$
G_R:\Gamma\longrightarrow[0,\infty)
$$

を固定する。`[R]` による条件付き履歴測度は

$$
d\mu_R^{a,b}(\lambda,\eta)
=
\frac{
\rho_S(\lambda,\eta)
G_R\!\left[
\Phi_{a,b}^{T}(\lambda,\eta)
\right]
}{
Z_{a,b}
}
d\lambda\,d\eta.
$$

$\lambda$ を固定して未読変数を積分した terminal compatibility を

$$
h_{a,b}(\lambda)
=
\int
\rho_S(\eta\mid\lambda)
G_R\!\left[
\Phi_{a,b}^{T}(\lambda,\eta)
\right]
d\eta
$$

と定義すると、source hypersurface 上の posterior は

$$
\rho_R(\lambda\mid a,b)
=
\frac{
\rho_S(\lambda)h_{a,b}(\lambda)
}{
Z_{a,b}
}
$$

となる。

\begin{proposition}[terminal compatibility criterion]
全 setting pair に対して同一の posterior $\rho_R(\lambda)$ が存在するための必要十分条件は、ある非負関数 $h(\lambda)$ と正定数 $c_{a,b}$ が存在して

$$
h_{a,b}(\lambda)
=
c_{a,b}h(\lambda)
$$

がほとんど至る所で成立することである。
\end{proposition}

Proof. 上式が成立すれば $c_{a,b}$ は規格化で消える。逆に posterior が全 setting で同じなら、

$$
\frac{h_{a,b}(\lambda)}{Z_{a,b}}
=
\frac{h_{a',b'}(\lambda)}{Z_{a',b'}}
$$

なので、各 compatibility は共通関数へ比例する。

従って固定した $G_R$ であっても、その Hamiltonian pullback

$$
G_R\circ\Phi_{a,b}^{T}
$$

が source variable を setting-dependent に再重みづけし得る。

## 相補的内部時計による terminal half-space の正準実現

return pair $(Y_R,\Pi_R)$ に center pair $(\bar\tau,P_c)$ を加え、二つの内部時計対を

$$
\tau_A
=
\bar\tau+\frac{Y_R}{2},
\qquad
\tau_B
=
\bar\tau-\frac{Y_R}{2},
$$

$$
\varrho_A
=
\frac{P_c}{2}+\Pi_R,
\qquad
\varrho_B
=
\frac{P_c}{2}-\Pi_R
$$

で定める。実際、

$$
\varrho_A\,d\tau_A
+
\varrho_B\,d\tau_B
=
P_c\,d\bar\tau
+
\Pi_R\,dY_R
$$

なので、これは正準変換である。

内部時計の自由 Hamiltonian を

$$
H_{\rm or}
=
\frac{\varrho_A^2+\varrho_B^2}{2M_\tau}
+
\frac{\kappa_c}{2}
\left(
\varrho_A+\varrho_B
\right)^2
$$

とする。center--relative 変数では

$$
H_{\rm or}
=
\frac{\Pi_R^2}{M_\tau}
+
\left(
\frac{1}{4M_\tau}
+
\frac{\kappa_c}{2}
\right)
P_c^2.
$$

相補的 sector

$$
P_c=0
$$

は自由運動と、$\bar\tau$ に依存しない comparator pulse の双方で保存される。この sector では

$$
\varrho_A=\Pi_R,
\qquad
\varrho_B=-\Pi_R,
$$

$$
\dot\tau_A
=
\frac{\Pi_R}{M_\tau},
\qquad
\dot\tau_B
=
-\frac{\Pi_R}{M_\tau}.
$$

従って $\Pi_R>0$ は A 時計が正向き、B 時計が負向きの順序付き相補性を表す。これは二粒子が実験室時刻に対して逆向きに伝播するという意味ではない。左右の粒子と messenger は通常どおり source から局所測定器、共通未来へ進み、反対になるのは内部時計または境界情報の向きである。

\begin{proposition}[terminal half-space の相補時計実現]
$P_c=0$、$\Pi_R(0)=E_*>0$ とし、comparator pulse が

$$
\Delta\Pi_R
=
\kappa I_- -h
$$

を与えるとする。このとき

$$
\Pi_R(T)
=
E_*+\kappa I_- -h.
$$

順序付き時計向きが終端まで保存される条件

$$
\varrho_A(T)\geq0,
\qquad
\varrho_B(T)\leq0
$$

は

$$
\Pi_R(T)\geq0
$$

と必要十分である。
\end{proposition}

これにより $\Pi_R$ は任意の return momentum ではなく二時計の相対運動量、$E_*$ は時計向きが反転するまでの初期 momentum margin、$G_R=\mathbf1_{\{\Pi_R(T)\geq0\}}$ は順序付き向き保存条件と読める。

ただし Hamilton 方程式は $\Pi_R(T)<0$ の軌道を禁止しない。この軌道では

$$
\varrho_A(T)<0,
\qquad
\varrho_B(T)>0
$$

となり、時計向きが交換されるだけである。従って相補的時計は terminal half-space の形を導くが、その半空間に入る履歴だけを物理的 ensemble とする `[R]` までは導かない。

## `[R]` と postselection

数式上、

$$
\rho_R
\propto
\rho_S G_R\circ\Phi^T
$$

は、実験後の rejection sampling と同じ条件付き確率に見える。本論文が `[R]` を境界 ontology として用いるためには、少なくとも次を要求する。

1. $G_R$ は Bell data を見る前に apparatus の terminal macroregion として固定する。
2. 全 setting と全 outcome に同じ terminal device と分解能を用いる。
3. 実現した pointer record を後から除外しない。
4. terminal width、ledger energy、comparator scale を独立 calibration で決める。
5. external launch count、pointer record count、terminal completion count の関係を報告する。

これらを満たせず、観測済み trial の一部を捨てて初めて Bell 値が出るなら、本構成は detector postselection に退化する。`[R]` を公理として書くだけではこの操作的区別は自動的に保証されない。

## 本章の結論

局所 analyzer、bright response、anchor record、有限局所浴、setting messenger、common-future propagation、terminal boundary measure を有限正準系の中に配置した。各履歴の outcome は局所 Hamiltonian flow で definite であり、common-future apparatus は記録後にのみ作動する。さらに return pair を相補的内部時計の相対 pair として正準実現し、terminal half-space を順序付き時計向き保存条件として解釈した。

一方、結果頻度を定める原理は局所浴の散逸、pointer の保持時間、comparison の速度、または時計相補性だけではない。物理的 ensemble を定める `[R]` と、次章で導く terminal compatibility の位相体積である。

# 共通未来の比較器と二モード台帳

\begin{statusbox}
位置づけ：cos 差動作用と sector 内の一様 soft-energy 密度を別々の位相空間幾何から導く。
\end{statusbox}


## phase-locked messenger

source が準備する二つの messenger を

$$
u_A^{(0)}
=
r_A n(\Theta_A),
\qquad
u_B^{(0)}
=
r_B n(\Theta_B),
$$

$$
n(\Theta)
=
\begin{pmatrix}
\cos\Theta\\
\sin\Theta
\end{pmatrix}
$$

とする。第5章の局所 pulse 後には

$$
u_A
=
A r_A R[\phi(a)]n(\Theta_A),
$$

$$
u_B
=
B r_B R[\phi(b)]n(\Theta_B)
$$

となる。$A,B$ は局所 anchor pointer にすでに記録されている。messenger はその符号と analyzer phase の写しを共通未来へ運ぶ。

相対角を

$$
\Delta_{ab}
=
\phi(a)-\phi(b)+\Theta_A-\Theta_B
$$

とする。setting が physical analyzer angle である場合、$\phi$ は装置表現に依存する。planar spin-like realization では $\phi(a)=a$、linear-polarization-like realization では double-angle map $\phi(a)=2a$ を用い得る。この写像は terminal rule ではなく、局所 analyzer の calibration に属する。

## 差動作用の cos 幾何

common-future difference mode の作用を

$$
I_-^{AB}
=
\frac14
\left\|
u_A-u_B
\right\|^2
$$

と定義する。直接展開すると

$$
I_-^{AB}
=
\frac14
\left[
r_A^2+r_B^2
-2ABr_Ar_B\cos\Delta_{ab}
\right].
$$

\begin{proposition}[実二次元比較器の cos 恒等式]
等振幅 $r_A=r_B=r$、固定相対 source phase $\Theta_A-\Theta_B=\Phi_0$ の下で、

$$
I_-^{AB}
=
I_0
\left[
1-AB\cos
\left\{
\phi(a)-\phi(b)+\Phi_0
\right\}
\right],
$$

$$
I_0=\frac{r^2}{2}
$$

である。
\end{proposition}

Proof. 回転行列の内積

$$
n(\Theta_A)^{\mathsf T}
R[\phi(b)-\phi(a)]
n(\Theta_B)
=
\cos\Delta_{ab}
$$

を差ベクトルの二乗へ代入すればよい。

cos は複素確率振幅、Born rule、量子内積から導入されていない。二つの実 canonical vector の Euclidean inner product

$$
u_A\cdot u_B
=
ABr_Ar_B\cos\Delta_{ab}
$$

から出る。

## amplitude mismatch と phase noise

source phase を

$$
\Theta_A-\Theta_B
=
\Phi_0+\delta
$$

とし、$r_A,r_B,\delta$ に setting と outcome sign から独立な準備分布を許す。terminal compatibility は $I_-$ に線形になるため、source variables を先に平均してよい。

$$
\overline I_-^{AB}
=
\frac14
\left\langle
r_A^2+r_B^2
\right\rangle
-\frac{AB}{2}
\operatorname{Re}
\left[
e^{i\{\phi(a)-\phi(b)+\Phi_0\}}
\left\langle
r_Ar_Be^{i\delta}
\right\rangle
\right].
$$

基準作用、visibility、phase offset を

$$
I_0
=
\frac14
\left\langle
r_A^2+r_B^2
\right\rangle,
$$

$$
V
=
\frac{
2
\left|
\left\langle
r_Ar_Be^{i\delta}
\right\rangle
\right|
}{
\left\langle
r_A^2+r_B^2
\right\rangle
},
$$

$$
\delta_0
=
\arg
\left\langle
r_Ar_Be^{i\delta}
\right\rangle
$$

と置けば、

$$
\overline I_-^{AB}
=
I_0
\left[
1-ABV
\cos
\left\{
\phi(a)-\phi(b)+\Phi_0+\delta_0
\right\}
\right].
$$

Cauchy--Schwarz 不等式から

$$
0\leq V\leq1
$$

である。以下では phase offset を $\Delta_{ab}$ に吸収し、

$$
\overline I_-^{AB}
=
I_0
\left[
1-ABV\cos\Delta_{ab}
\right]
$$

と書く。

## 二モード台帳

比較器の未読変数として、一つの soft mode と一つの ledger mode を置く。

$$
J_s
=
\frac12
\left(
q_s^2+p_s^2
\right),
\qquad
J_0
=
\frac12
\left(
q_0^2+p_0^2
\right).
$$

両 mode の基準周波数を同じ $\omega_\ell>0$ とし、

$$
J_\ell
=
J_s+J_0,
$$

$$
E_\ell
=
\omega_\ell J_\ell
$$

を固定する。soft energy を

$$
h
=
\omega_\ell J_s
$$

とする。ledger mode は、soft mode に入っていない残余作用

$$
E_\ell-h
=
\omega_\ell J_0
$$

を保持する。

二つの action-angle 座標を

$$
q_\nu
=
\sqrt{2J_\nu}\cos\theta_\nu,
\qquad
p_\nu
=
\sqrt{2J_\nu}\sin\theta_\nu,
\qquad
\nu=s,0
$$

と取れば、

$$
dq_\nu\,dp_\nu
=
dJ_\nu\,d\theta_\nu.
$$

固定総作用殻上の正規化 Liouville 測度を

$$
d\mu_\ell
=
\frac{
\delta\!\left(
E_\ell-\omega_\ell J_s-\omega_\ell J_0
\right)
dJ_s\,d\theta_s\,dJ_0\,d\theta_0
}{
\displaystyle
\int
\delta\!\left(
E_\ell-\omega_\ell J_s-\omega_\ell J_0
\right)
dJ_s\,d\theta_s\,dJ_0\,d\theta_0
}
$$

とする。

## 一様 soft-energy 周辺定理

\begin{theorem}[二モード台帳の一様周辺]
固定 $E_\ell>0$ の二モード作用殻上で、soft energy $h=\omega_\ell J_s$ の周辺密度は

$$
p_\ell(h)
=
\frac1{E_\ell}
\mathbf1_{\{0\leq h\leq E_\ell\}}
$$

である。
\end{theorem}

Proof. 位相角を積分すると $(2\pi)^2$ を得る。$h=\omega_\ell J_s$ を固定した未規格化密度は

$$
\int_0^\infty
dJ_0\,
\delta
\left(
E_\ell-h-\omega_\ell J_0
\right)
\frac{dh}{\omega_\ell}
=
\frac{dh}{\omega_\ell^2}
\mathbf1_{\{0\leq h\leq E_\ell\}}.
$$

全質量は

$$
\int_0^{E_\ell}
\frac{dh}{\omega_\ell^2}
=
\frac{E_\ell}{\omega_\ell^2}.
$$

規格化すると $p_\ell(h)=1/E_\ell$ である。

この定理は、二つの一自由度 harmonic mode の density of states がともに定数であることの帰結である。結果 sector、setting、source phase は ledger shell の定義に現れないため、`[M]` の入口測度が各 sector で共通なら

$$
p
\left(
h\mid A,B,a,b
\right)
=
\frac1{E_\ell}
$$

となる。

## 有限非線形 mixer

固定総作用を保ったまま、soft mode と ledger mode の向きを攪拌する生成子を構成できる。次の二次量を定義する。

$$
J_x
=
q_sq_0+p_sp_0,
$$

$$
J_y
=
q_sp_0-p_sq_0,
$$

$$
J_z
=
J_s-J_0.
$$

直接計算から

$$
\{J_\ell,J_x\}
=
\{J_\ell,J_y\}
=
\{J_\ell,J_z\}
=
0
$$

である。有限個の非線形環境変数を $\chi=(X_\alpha,P_\alpha)$ とし、

$$
H_\chi
=
\sum_{\alpha=1}^{m}
\left[
\frac{P_\alpha^2}{2M_\alpha}
+\frac{M_\alpha\Omega_\alpha^2X_\alpha^2}{2}
+\lambda_\alpha X_\alpha^4
\right]
+
\sum_{\alpha<\beta}
c_{\alpha\beta}X_\alpha^2X_\beta^2
$$

を一例とする。mixer coupling を

$$
K_M
=
\epsilon
\left[
g_x(\chi)J_x
+g_y(\chi)J_y
+g_z(\chi)J_z
\right]
$$

とすれば、

$$
\{J_\ell,K_M\}=0.
$$

従って

$$
H_{\ell\chi}
=
\omega_\ell J_\ell
+H_\chi
+K_M
$$

は有限で滑らかであり、総 ledger action を厳密に保存しながら、二 mode 間の作用配分と相対位相を変化させる。

有限の非線形環境が少数自由度でも中心振動子の実効的エネルギー分散と熱化を起こし得ることは、具体的な古典模型で確認されている \cite{marchiori_deaguiar2011}。ただし本論文で必要なのは bath が ledger energy を吸収することではない。$J_\ell$ を保ったまま、固定作用殻の orientation を有限分解能で攪拌することである。

## 不変測度と動的混合の区別

二モード定理には二つの読み方がある。

1. **ensemble reading**：比較器入口を固定作用殻の正規化 Liouville 測度で準備する。この場合 $p_\ell(h)=1/E_\ell$ は厳密である。
2. **typical-time reading**：一つの初期 microstate を finite mixer で長時間発展させ、有限分解能の time histogram を入口測度として用いる。この場合は mixing と時間尺度分離が必要である。

Hamiltonian flow は fine-grained Liouville density を保存する。従って任意の初期密度が $L^1$ または pointwise に一様密度へ収束するとは言えない。mixing が与え得るのは、滑らかな coarse observable $F$ に対する

$$
\frac1{\tau_{\rm cmp}}
\int_0^{\tau_{\rm cmp}}
F[h(t)]dt
\approx
\int_0^{E_\ell}
F(h)\frac{dh}{E_\ell}
$$

という有限時間平均、または初期 cell を粗視化した弱い収束である。

必要な時間尺度は

$$
\tau_{\rm mix}
\ll
\tau_{\rm cmp}
\ll
T_{\rm rec}.
$$

$\tau_{\rm mix}$ は coarse histogram の緩和、$\tau_{\rm cmp}$ は comparator が ledger state を読み出す前の混合窓、$T_{\rm rec}$ は有限 mixer の再帰尺度である。本論文は一般の $K_M$ に対してこの不等式を証明しない。これは数値検証すべき `[M]` の動力学部分である。

## 通常の多モード浴が失敗する理由

soft mode が $N$ 個の通常 ledger mode と固定総エネルギーを自由に分け合うとする。各 mode が一つの harmonic canonical pair で、全 simplex

$$
h+\sum_{j=1}^{N}e_j=E_\ell,
\qquad
h,e_j\geq0
$$

上の一様 Liouville measure を用いる。$h$ を固定した残余 simplex の体積は $(E_\ell-h)^{N-1}$ に比例するので、

$$
p_N(h)
=
\frac{N}{E_\ell}
\left(
1-\frac h{E_\ell}
\right)^{N-1},
\qquad
0\leq h\leq E_\ell.
$$

しきい値 $x$ 以下の累積重みは

$$
F_N(x)
=
\int_0^x p_N(h)dh
=
1-
\left(
1-\frac x{E_\ell}
\right)^N.
$$

$N=1$ のときだけ

$$
F_1(x)=\frac{x}{E_\ell}
$$

が線形である。$N>1$ では $x$ の二次以上の項が現れる。第7章のしきい値

$$
x_{AB}
=
E_*+\kappa I_0
\left(
1-ABV\cos\Delta_{ab}
\right)
$$

を代入すると、$\cos^2\Delta_{ab}$ 以上の高調波が一般に残る。

従って「大きな bath ほど Bell の cos 則に近づく」という主張は成立しない。純粋な線形 compatibility に必要なのは、

- 一つの soft canonical pair。
- 一つの ledger canonical pair。
- 総作用を保った orientation mixing。

という最小構造である。追加 bath は mixer の chaos を作る補助であり、threshold-dependent energy を自由に共有する ledger へしてはならない。

## sector 質量の対称性

二モード定理が決めるのは各 outcome sector 内の条件付き密度であり、sector 自体の基準質量ではない。基準 preparation measure における四 sector を

$$
\Sigma_{AB}
=
\left\{
\sigma(s_A)=A,\,
\sigma(s_B)=B
\right\}
$$

とし、

$$
w_{AB}
=
\mu_S(\Sigma_{AB})
$$

と定義する。

preparation stage に二つの measure-preserving involution

$$
\mathcal S_A:
\Sigma_{AB}
\longrightarrow
\Sigma_{-A,B},
$$

$$
\mathcal S_B:
\Sigma_{AB}
\longrightarrow
\Sigma_{A,-B}
$$

があり、$H_{\rm prep}$、preparation macroregion、$\mu_S$ を保つとする。二つの変換が生成する群は四 sector に推移的に作用する。

\begin{proposition}[対称準備の sector 等体積]
上の独立符号反転対称性 `[S]` の下で、

$$
w_{++}
=
w_{+-}
=
w_{-+}
=
w_{--}
=
\frac14
$$

である。
\end{proposition}

Proof. $\mathcal S_A$ と $\mathcal S_B$ は measure-preserving bijection なので、任意の二 sector の測度は等しい。四 sector が全 preparation support を分割するため、規格化すると各質量は $1/4$ である。

Hamiltonian の符号対称性だけでは不十分である。同じ Hamiltonian に非対称な初期密度を置くことも可能だからである。`[S]` は「対称な preparation macrostate 上の不変基準測度を採用する」という統計条件を含む。

## 共通入口密度

第6.5節と第6.9節を組み合わせると、比較器入口での outcome sector と soft energy の基準密度は

$$
g_{AB}^{\rm ent}(h)
=
\frac{w_{AB}}{E_\ell}
\mathbf1_{\{0\leq h\leq E_\ell\}}.
$$

`[S]` の下では

$$
g_{AB}^{\rm ent}(h)
=
\frac1{4E_\ell}
\mathbf1_{\{0\leq h\leq E_\ell\}}.
$$

この式で

- $1/E_\ell$ は二モード作用殻の幾何。
- $1/4$ は準備 sector の対称性。

から来る。二つを一つの「等基準因子」として仮定しないことが、本改訂の中心である。

## 本章の結論

Bell 型 cos 重みの角度依存性と線形確率変換は、異なる二つの幾何から生じる。cos は二つの実 messenger の差動作用、一様 threshold density は一つの soft pair と一つの ledger pair の固定総作用殻から生じる。

finite nonlinear bath は後者の不変測度を作る論理原理ではなく、その orientation を有限時間で典型化する候補機構である。sector mass はさらに preparation symmetry `[S]` を必要とする。次章では、setting-blind terminal coordinate へこの二つの結果を代入し、共同確率を導く。

# 終端整合測度と Bell 共同確率

\begin{statusbox}
位置づけ：setting-blind terminal condition の Hamiltonian pullback と二モード位相体積から Bell compatibility weight を導く。
\end{statusbox}


## return comparator

return pointer を $(Y_R,\Pi_R)$ とし、滑らかな bounded function $F_R$ を

$$
F_R(0)=0,
\qquad
F_R'(0)=1
$$

となるよう選ぶ。例えば

$$
F_R(Y)
=
\delta_R
\tanh
\left(
\frac{Y}{\delta_R}
\right)
$$

を用いられる。comparator generator を

$$
K_R
=
F_R(Y_R)
\left[
h-\kappa I_-
\right]
$$

とする。ここで $\kappa>0$ は比較器 scale、$h=\omega_\ell J_s$ は二モード台帳の soft energy である。$E_*\geq0$ は comparator generator の定数項には入れず、相補的内部時計の初期相対運動量として置く。

comparator pointer の初期状態を

$$
Y_R=0,
\qquad
\Pi_R=E_*
$$

とする。$K_R$ は $\Pi_R$ に依存しないため、pulse 中

$$
\frac{dY_R}{d\tau}=0.
$$

従って $Y_R=0$ が保たれ、

$$
\frac{d\Pi_R}{d\tau}
=
-F_R'(0)
\left[
h-\kappa I_-
\right]
$$

から unit pulse 後に

$$
\Pi_R(T)
=
E_*+\kappa I_- -h
$$

を得る。

$F_R(0)=0$ なので、comparator pulse は読出し軌道上で messenger と ledger の canonical variables を動かさない。相対時計運動量へ $\Delta\Pi_R=\kappa I_- -h$ を加えるだけである。$E_*$ は時計向きが反転するまでの初期 momentum margin である。

## 固定 terminal condition

terminal macroregion を

$$
G_R(z_T)
=
\mathbf1_{\{\Pi_R(T)\geq0\}}
$$

とする。これは

$$
G_R=1
\quad\Longleftrightarrow\quad
h\leq E_*+\kappa I_-
$$

と等価である。

第5.9節の相補的内部時計実現では $P_c=0$ なので、

$$
\varrho_A(T)=\Pi_R(T),
\qquad
\varrho_B(T)=-\Pi_R(T).
$$

従って同じ terminal condition は、source で選んだ順序付き時計向き

$$
\varrho_A\geq0,
\qquad
\varrho_B\leq0
$$

が終端まで保たれた条件である。これは terminal half-space の正準力学的起源を与えるが、その半空間だけを物理的履歴集団として数える `[R]` の統計原理を置き換えない。

$G_R$ の関数形は $a,b,A,B$ も $\cos\Delta_{ab}$ も参照しない。setting と outcome への依存は、局所 Hamiltonian rotation を含む flow で $G_R$ を初期面へ pullback したときにのみ現れる。

全 source support で cutoff に当たらない working range

$$
0
\leq
E_*+\kappa I_-
\leq
E_\ell
$$

を仮定する。理想等振幅模型では十分条件として

$$
E_*+\kappa I_0(1+V)
\leq
E_\ell
$$

を用いられる。finite amplitude distribution を許す場合は、その support 上で同じ上界を課す。cutoff に当たる場合の補正は第8章と付録Cで扱う。

## terminal compatibility の積分

outcome sector の基準質量を $w_{AB}$ とする。第6章の二モード定理により、sector 内の soft-energy density は $1/E_\ell$ である。source fluctuation を $\zeta$ とし、その基準分布を $d\nu(\zeta)$ と書くと、unnormalized terminal-compatible weight は

$$
W_{AB}(a,b)
=
w_{AB}
\int d\nu(\zeta)
\int_0^{E_\ell}
\frac{dh}{E_\ell}
\mathbf1_{\{
h\leq E_*+\kappa I_-^{AB}(\zeta)
\}}.
$$

working range の下で $h$ 積分は線形なので、

$$
W_{AB}(a,b)
=
\frac{w_{AB}}{E_\ell}
\left[
E_*+\kappa
\overline I_-^{AB}
\right].
$$

第6.3節の visibility 表示を代入すると、

$$
W_{AB}(a,b)
=
\frac{w_{AB}}{E_\ell}
\left[
E_*+\kappa I_0
\left(
1-ABV\cos\Delta_{ab}
\right)
\right].
$$

ここで

$$
\Delta_{ab}
=
\phi(a)-\phi(b)+\Delta_0
$$

であり、$\Delta_0$ は source phase offset を含む。

重要なのは、Bell compatibility weight の線形性が gate flux からではなく、固定総作用殻上の cumulative Liouville volume

$$
\int_0^x
\frac{dh}{E_\ell}
=
\frac{x}{E_\ell}
$$

から出ることである。

## 二モード台帳 Bell compatibility 定理

\begin{theorem}[二モード台帳を持つ時間対称 Bell compatibility]
次を仮定する。

1. `[H]`：第5章の有限 Hamiltonian 測定器と第7.1節の setting-blind comparator。
2. `[P]`：第6.3節の phase-locked source と visibility $0\leq V\leq1$。
3. `[S]`：四つの基準 outcome sector の独立符号反転対称性。
4. `[M]`：固定総作用 $E_\ell$ 上の二モード Liouville entrance measure。
5. `[R]`：第5.8節の時間対称境界統計原理。
6. working range：$0\leq E_*+\kappa I_-\leq E_\ell$ が source support 上で成立する。

このとき、規格化した terminal-compatible joint law は

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
\frac{\kappa I_0}{E_*+\kappa I_0}V.
$$

各履歴の局所 response は deterministic に因子化する。一方、Bell-complete source posterior は一般に setting-dependent である。
\end{theorem}

Proof. `[S]` から $w_{AB}=1/4$ である。第7.3節より

$$
W_{AB}
=
\frac1{4E_\ell}
\left[
E_*+\kappa I_0
-AB\kappa I_0V\cos\Delta_{ab}
\right].
$$

四 outcome を足すと

$$
Z_{a,b}
=
\sum_{A,B}W_{AB}
=
\frac{E_*+\kappa I_0}{E_\ell},
$$

なぜなら

$$
\sum_{A,B}AB=0
$$

だからである。$W_{AB}/Z_{a,b}$ を計算すれば主張の joint law を得る。

fixed complete microstate $\lambda$ では、

$$
A=\mathscr A(a,\lambda),
\qquad
B=\mathscr B(b,\lambda)
$$

であり、

$$
P(A,B\mid a,b,\lambda)
=
P(A\mid a,\lambda)
P(B\mid b,\lambda)
$$

と因子化する。しかし `[R]` 後の $\lambda$ 分布は第7.6節の通り setting-dependent である。

## 初期時計向き margin $E_*$ の役割

$E_*=0$ では

$$
V_{\rm eff}=V
$$

であり、理想 phase lock $V=1$ なら標準的な unit-visibility cosine law を得る。しかし $\Delta_{ab}=0$ かつ $AB=+1$ の channel では threshold が零になり、terminal-compatible volume も零になる。

$E_*>0$ は相補時計の正向き sector 内で向き反転までの初期運動量余裕を与える。同時に全 channel に正の compatibility floor を与え、

$$
E_*+\kappa I_-^{AB}\geq E_*
$$

とする。その代わり visibility は

$$
V_{\rm eff}
=
\frac{\kappa I_0}{E_*+\kappa I_0}V
<V
$$

へ低下する。従って $E_*$ は時計向きの頑健性および低 threshold の正則化と、Bell visibility の交換関係を与える。

## microscopic posterior と measurement independence

理想化して、Bell-relevant hidden data を $(A,B,h)$ とする。他の source variables が setting-independently factorize する場合、`[R]` 後の密度は

$$
\rho_R(A,B,h\mid a,b)
=
\frac1{
4(E_*+\kappa I_0)
}
\mathbf1_{\{
0\leq h\leq x_{AB}(a,b)
\}},
$$

$$
x_{AB}(a,b)
=
E_*+\kappa I_0
\left[
1-ABV\cos\Delta_{ab}
\right].
$$

setting を変えると各 outcome sector の support ceiling が変わるため、

$$
\rho_R(\lambda\mid a,b)
\neq
\rho_R(\lambda\mid a',b')
$$

が一般に成立する。

Bell--CHSH の標準導出では、四 setting pair に同じ $\rho(\lambda)$ を用いる。本構成で外れる仮定は measurement independence であり、fixed $\lambda$ における local response factorization ではない \cite{hall2010,leifer_pusey2017,hossenfelder_palmer2020,thooft2016}。

二つの setting pair に対応する

$$
c=\cos\Delta_{ab},
\qquad
c'=\cos\Delta_{a'b'}
$$

の間の全変動距離は、上の最小 posterior について

$$
D_{\rm TV}(c,c')
=
\frac{V_{\rm eff}}2
|c-c'|
$$

である。追加 hidden variables が setting-independently factorize する場合、この値は full posterior に対しても正確である。一般の追加構造を許す場合は、$(A,B,h)$ marginal が与える識別可能性の下界になる。

## setting frequency の保護

controller の基準分布を $P_S(a,b)$ とする。`[R]` を controller を含む全 ensemble へ適用すると、

$$
P_R(a,b)
\propto
P_S(a,b)Z_{a,b}.
$$

第7.4節で

$$
Z_{a,b}
=
\frac{E_*+\kappa I_0}{E_\ell}
$$

は setting-independent である。従って

$$
P_R(a,b)=P_S(a,b).
$$

実験者は巨視的 controller frequency を変更できる。一方、その setting macrostate と terminal condition の両方に compatible な microscopic source posterior は変化する。この意味で本構成は future-input-dependent または time-symmetric boundary class に属する \cite{wharton2010,wharton_argaman2020,price_wharton2023,price_wharton2024,argaman2010}。

## no-signalling と相関

joint law の一側周辺は

$$
P_R(A\mid a,b)
=
\sum_{B=\pm1}
P_R(A,B\mid a,b)
=
\frac12,
$$

$$
P_R(B\mid a,b)
=
\frac12.
$$

従って `[S]` の対称 ensemble では operational no-signalling が成立する。これは microscopic measurement independence が回復したことを意味しない。遠隔 setting dependence は hidden posterior に残るが、outcome-sign symmetry により一側周辺で相殺される。

相関は

$$
E(a,b)
=
\sum_{A,B}
ABP_R(A,B\mid a,b)
=
-V_{\rm eff}\cos\Delta_{ab}.
$$

標準 CHSH angle

$$
\phi(a_0)=0,
\qquad
\phi(a_1)=\frac\pi2,
$$

$$
\phi(b_0)=\frac\pi4,
\qquad
\phi(b_1)=-\frac\pi4
$$

では

$$
|\mathcal S|
=
2\sqrt2V_{\rm eff}.
$$

従って

$$
V_{\rm eff}
>
\frac1{\sqrt2}
$$

なら CHSH 不等式を破る。

## Bell 前提台帳

本構成の Bell 前提は次の通りである。

- outcome definiteness：満たす。各 Hamiltonian history は一つの anchor-pointer sector を持つ。
- local deterministic response：Bell-complete $\lambda$ 上で満たす。
- parameter independence at fixed $\lambda$：局所記録時刻について満たす。
- common measurement-independent distribution：満たさない。
- operational setting freedom：$Z_{a,b}$ が一定なので controller frequency を保つ。
- equilibrium no-signalling：`[S]` の下で満たす。
- arbitrary-preparation no-signalling：本論文では証明しない。
- absence of observed-data postselection：物理的実装条件として要求する。

従って本論文は Bell の定理を反駁しない。Bell 不等式を外れる共同確率と、外れた仮定を同じ模型の中で明示する。

## 流束、滞在時間、結果頻度

結果 $A,B$ が comparator 到達前に確定した順時間的 trial 列を考える。全 trial が有限時間で完了し、結果依存の除外がないなら、後段の reaction coordinate が持つ通過時間は、時刻を無作為に選んだときの occupancy を変えるが、trial number で数えた outcome ratio を変えない。

\begin{proposition}[後段時間による結果頻度不変]
$n$ 番目の trial の結果を $\kappa_n=(A_n,B_n)$、完了時間を $\tau_n<\infty$ とする。全 trial を結果に関係なく一度ずつ数えるなら、

$$
\frac1N
\sum_{n=1}^{N}
\mathbf1_{\{\kappa_n=(A,B)\}}
$$

は $\tau_n$ の値に依存しない。結果依存の timeout または非完了 trial の除外を導入した場合にのみ、観測された比率は再重みづけされる。
\end{proposition}

従って

- reaction gate の通過速度。
- 結果依存の待ち時間。
- 有限浴への順時間的 energy leakage。

は、それだけでは `[R]` の代わりにならない。本論文の $W_{AB}$ は gate capacity または completion flux ではなく、`[R]` が物理的集団とする terminal-compatible phase volume である。

## 本章の結論

setting-blind comparator は、相補時計の初期相対運動量 $\Pi_R(0)=E_*$ に $\kappa I_- -h$ を加えて

$$
\Pi_R(T)=E_*+\kappa I_- -h
$$

を作る。固定 terminal condition は順序付き時計向きの保存と同値であり、同時に $h$ の sublevel volume を測る。二モード台帳の一様密度と対称準備を用いると、Bell 型 cos 共同確率が通常の正の Liouville 積分として得られる。

確率の起源は `[R]` であり、時計相補性だけではない。cos dependence、linear threshold volume、terminal half-space の正準構造は Hamiltonian apparatus が計算する。Bell の前提違反は measurement independence に位置し、macroscopic setting frequency と equilibrium no-signalling は四 sector の対称性により保たれる。

# 頑健性、反証条件、証明台帳

\begin{statusbox}
位置づけ：`[R]`、mixing、preparation symmetry の残る地位と、模型を区別する観測量を明示する。
\end{statusbox}


## 到達した結果

第I部では、有限 Fourier--Gaussian bath から繰り込み済み作用の Nelson 極限を定量的に得た。第II部では、次の構造を一つの論理鎖にまとめた。

1. finite Hamiltonian local analyzer が definite anchor record を作る。
2. 二つの real messenger が common future で差動作用を形成する。
3. 差動作用は $1-ABV\cos\Delta_{ab}$ に比例する。
4. 一つの soft pair と一つの ledger pair の固定総作用殻が一様 threshold density を与える。
5. symmetric preparation が四 outcome sector の基準質量を $1/4$ にする。
6. return pair と center pair が、向きの相補的な二つの内部時計へ正準分解される。
7. setting-blind comparator が初期相対時計運動量 $E_*$ に $\kappa I_- -h$ を加え、$\Pi_R(T)=E_*+\kappa I_- -h$ を作る。
8. terminal half-space は順序付き時計向き保存条件として実現される。
9. `[R]` が terminal-compatible histories を物理的 ensemble とする。
10. 規格化後に Bell 型 joint law、no-signalling marginal、CHSH violation が得られる。
11. Bell の前提違反は measurement independence に現れる。

これは「閉じた Hamiltonian 方程式が forward evolution だけで Bell probability を生成した」という結果ではない。Hamiltonian dynamics、preparation measure、boundary ensemble の役割を分離した constructive compatibility theorem である。

## `[R]` の物理的地位

有限閉鎖 Hamiltonian 系は recurrence を持ち得る。時間反転可能な方程式は final boundary condition を数学的に許す。しかし

$$
\text{finiteness}
+
\text{recurrence}
+
\text{time-reversal symmetry}
$$

だけから

$$
d\mu_R
\propto
\rho_S
G_R\circ\Phi^T
d\Gamma
$$

を物理的 probability law として一意に選ぶことはできない。`[R]` は本理論を標準的な初期値統計力学から区別する中心原理である。

従って `[R]` を削除するなら、少なくとも次のいずれかで同じ役割を置き換えなければならない。

- two-boundary condition。
- all-at-once history measure。
- setting-dependent source preparation。
- common-future consistency condition。
- action principle による complete-history selection。

名称を変えても、setting-dependent terminal compatibility を物理的履歴重みへ変換する構造は残る。何も置き換えずに通常の forward Liouville ensemble へ戻せば、Bell weight は得られない。

相補的内部時計はこの区別をさらに明確にする。$\Pi_R(T)\geq0$ は source で選んだ時計向きの順序が終端まで保存された条件として導ける。しかし $\Pi_R(T)<0$ の軌道も Hamiltonian 解であり、時計向きが交換されるだけである。従って時計相補性は $G_R$ の半空間を説明するが、$G_R$ を履歴確率へ変換しない。

各時計枝をそれぞれの clock-past 境界から準備し、同じ Hamiltonian 履歴として matching する規則を追加するなら、履歴空間上で

$$
d\nu
\propto
\rho_S(z_i)
G_{\rm or}(z_f)
\delta
\left(
z_f-\Phi_{a,b}^{T}z_i
\right)
d\Gamma_i\,d\Gamma_f
$$

と書ける。$z_f$ を積分すると

$$
d\nu_i
\propto
\rho_S(z_i)
G_{\rm or}
\left(
\Phi_{a,b}^{T}z_i
\right)
d\Gamma_i
$$

となり `[R]` の積形式を再現する。ただし、branch-wise boundary preparation と matching が追加の all-at-once 統計原理である。

さらに同じ scalar readout $\Pi_R(T)=x-h$ に対し、二つの相補的 half-space $\Pi_R(T)\geq0$ と $\Pi_R(T)\leq0$ を等重みで平均すると、

$$
F_+(x)
=
\frac{x}{E_\ell},
\qquad
F_-(x)
=
1-\frac{x}{E_\ell},
$$

$$
\frac12
\left[
F_+(x)+F_-(x)
\right]
=
\frac12.
$$

従って Bell の cos 項は消える。単なる無向き相補性では足りず、順序付き sector、または時間反転した sector と comparator kick の符号を共変に結ぶ別の構造が必要である。

## 共有浴ノイズの順時間的漏れに関する否定結果

局所記録時刻 $t_m$ で、phase space を四つの disjoint record sector

$$
\Gamma_{AB}(t_m)
$$

に分ける。$t>t_m$ の共通浴を含む Hamiltonian flow を $\Phi^{t-t_m}$ とする。forward Liouville measure $\mu$ に対し、

$$
\mu
\left[
\Phi^{t-t_m}
\Gamma_{AB}(t_m)
\right]
=
\mu
\left[
\Gamma_{AB}(t_m)
\right]
$$

である。Hamiltonian flow は bijective かつ volume-preserving だからである。

従って、記録形成後に左右の copy を共通浴へ結合しても、全 trial を一度ずつ数える outcome-sector mass は変わらない。変わり得るのは

- bath state と record の相関。
- reaction time。
- 時刻占有率。
- finite timeout までの completion fraction。

である。

記録形成前に共通浴を左右へ結合すれば、相関を forward dynamics で作る余地はある。しかしその場合は spacelike-separated local response の coupling graph を改めて監査しなければならず、本論文の局所構成とは別模型になる。

従って本論文の Bell correlation は、共有浴ノイズの leakage ではない。共通未来の bath と mixer は、`[R]` の terminal compatibility を計算する装置部分である。

## `[S]`、biased preparation、no-signalling

一般の基準 sector weight を $w_{AB}$ とすると、

$$
P_w(A,B\mid a,b,R)
=
\frac{
w_{AB}
\left[
C-ABKc
\right]
}{
\displaystyle
\sum_{A',B'}
w_{A'B'}
\left[
C-A'B'Kc
\right]
},
$$

$$
C=E_*+\kappa I_0,
\qquad
K=\kappa I_0V,
\qquad
c=\cos\Delta_{ab}.
$$

同時 sign flip symmetry

$$
w_{++}=w_{--},
\qquad
w_{+-}=w_{-+}
$$

があれば一側 outcome marginal は $1/2$ に保たれる。しかし parity sector の基準質量が異なると、全 compatibility は

$$
Z_{a,b}
=
C
-Kc
\sum_{A,B}ABw_{AB}
$$

となり、setting frequency が変化し得る。outcome marginal と controller frequency の両方を最も単純に保つ条件は

$$
w_{AB}=\frac14
$$

である。

例えば Bob seed を $B=+1$ に限定した基準 subensemble が操作的に準備可能なら、

$$
w_{++}=w_{-+}=\frac12,
\qquad
w_{+-}=w_{--}=0.
$$

このとき

$$
P_R(A=+1\mid a,b,B=+1)
=
\frac12
\left[
1-V_{\rm eff}\cos\Delta_{ab}
\right]
$$

となり、Alice の marginal は Bob の setting に依存する。従って `[S]` の equilibrium no-signalling は arbitrary-preparation no-signalling ではない。

full theory には次のいずれかが必要である。

1. biased preparation apparatus を含む boundary problem が symmetry を回復する。
2. biased seed macroregion の terminal-compatible volume が零または操作不能になる。
3. biased preparation が可能で、模型は signalling prediction を持つ。

第三の場合、本模型は実験的に排除される。`[S]` は反証不能な言葉で隠すのではなく、preparability test の対象にすべきである。

## mixing の頑健性

二モード一様密度には三つの異なる誤差源がある。

1. **不完全 mixing**：finite observation window で $p(h)$ に residual structure が残る。
2. **action leakage**：$J_s+J_0$ が他 mode へ漏れ、fixed shell が崩れる。
3. **追加 ledger mode**：threshold-dependent energy を三つ以上の canonical pair が共有する。

入口密度を

$$
p(h)
=
\frac1{E_\ell}
\left[
1+\varepsilon r(h)
\right],
$$

$$
\int_0^{E_\ell}r(h)dh=0
$$

と書くと、compatibility weight は

$$
F(x)
=
\frac{x}{E_\ell}
+
\frac{\varepsilon}{E_\ell}
\int_0^x r(h)dh.
$$

$x=C-ABKc$ を代入したとき、第二項は一般に $c$ の非線形関数となる。従って不完全 mixing は visibility loss だけでなく、

$$
\cos2\Delta,
\qquad
\cos3\Delta,
\qquad
\ldots
$$

を生じ得る。

特に $N$ 個の通常 ledger mode に対する

$$
F_N(x)
=
1-
\left(
1-\frac x{E_\ell}
\right)^N
$$

は、$N>1$ で明示的な高次調波を持つ。高調波の上限を測ることは、二モード縮約が実際に成立しているかを検査する直接的な方法である。

## terminal width と cutoff

理想 terminal function

$$
G_R
=
\mathbf1_{\{\Pi_R\geq0\}}
$$

は sharp macroregion を用いる。有限分解能では、幅 $\epsilon_R$ の滑らかな response $g_{\epsilon_R}(\Pi_R)$ へ置き換える。compatibility は

$$
F_{\epsilon_R}(x)
=
\int_0^{E_\ell}
\frac{dh}{E_\ell}
g_{\epsilon_R}(x-h)
$$

となる。

$x$ が両端 $0,E_\ell$ から $\epsilon_R$ より十分離れ、response kernel が translation-covariant なら、主要項は $x/E_\ell$ である。endpoint に近づくと clipping correction が入り、零 threshold channel は有限の background weight を持ち得る。

従って実験または数値検証では、

- $E_\ell$。
- $E_*$。
- $\kappa I_0$。
- terminal width $\epsilon_R$。

を独立に変え、first harmonic、higher harmonics、normalization residual を同時に測る必要がある。

## reaction time と $E_*$ の交換関係

return pointer の後に、available energy

$$
x_{AB}
=
E_*+\kappa I_-^{AB}
$$

で自由 reaction coordinate を長さ $\ell_g$ だけ進ませるとする。質量を $M_g$ とすれば、理想自由飛行時間は

$$
\tau_g(x)
=
\ell_g
\sqrt{
\frac{M_g}{2x}
}.
$$

$E_*=0$ では $x\downarrow0$ の channel で時間が発散し得る。$E_*>0$ なら

$$
\tau_g(x_{AB})
\leq
\ell_g
\sqrt{
\frac{M_g}{2E_*}
}
$$

である。一方、Bell visibility は

$$
V_{\rm eff}
=
\frac{\kappa I_0}{E_*+\kappa I_0}V
$$

へ低下する。

従って $E_*$ を増やすと completion time は一様化するが、CHSH visibility は下がる。この同時変化は装置模型の反証可能な予測である。ただし $\tau_g$ は `[R]` で定まった weight を表示する後段時間であり、weight の起源ではない。

## cos 則と Tsirelson 限界

本構成が直接与えるのは、実二次元の等振幅 messenger と quadratic difference comparator による

$$
I_-
\propto
1-AB\cos\Delta
$$

である。従って

$$
|\mathcal S|
=
2\sqrt2V_{\rm eff}
\leq
2\sqrt2
$$

は $0\leq V_{\rm eff}\leq1$ と comparator design の帰結である。

一般の非負 scalar comparator $F(I_-)$ を許せば、異なる correlation table を構成できる。本論文は、回転対称性、合成則、情報原理、Hamiltonian stability などから quadratic comparator を一意に選ぶ定理を持たない。従って $2\sqrt2$ を一般原理から導いたとは言えない。

## Wallstrom 問題との関係

第I部の Nelson 表示から一般の Schrödinger theory を再構成するには、configuration space の閉路に沿う phase circulation を量子化する必要があり、Wallstrom 問題が残る \cite{wallstrom1994}。

第II部で現れる cos は、

$$
u_A\cdot u_B
\propto
\cos\Delta_{ab}
$$

という comparator geometry である。これは Bell experiment の設定差に対する共同確率を与えるが、configuration-space phase $S(x)$ の閉路条件

$$
\oint\nabla S\cdot d\ell
\in
2\pi\hbar\mathbb Z
$$

を導かない。従って Bell 型 cos 共同確率が得られたことは、Wallstrom 問題の解決を意味しない。

ただし、同じ有限 Hamiltonian source の action-angle variable が、Bell messenger phase と Nelson phase の双方を拘束する追加機構を作れれば、両問題を結ぶ研究方向にはなり得る。その場合でも必要なのは単なる cos law ではなく、全許容閉路に対する整数 winding selection である。

## 検証プログラム

最小の検証を次の五段階に分ける。

### 段階1：local measurement

canonical equations を積分し、messenger rotation、bright shift、anchor shift、record holding time を測る。energy error、symplectic error、anchor flip rate を報告する。

### 段階2：two-mode ledger

固定 $J_\ell$ 上で $h/E_\ell$ の histogram、autocorrelation、mixing time、recurrence time を測る。Kolmogorov 距離または低次 moment だけでなく、threshold CDF の最大偏差

$$
\epsilon_F
=
\sup_{0\leq x\leq E_\ell}
\left|
F_{\rm emp}(x)-\frac{x}{E_\ell}
\right|
$$

を用いる。

### 段階3：terminal compatibility

全 setting と outcome に同じ $G_R$ を用い、$W_{AB}$ の $I_-$ に対する線形性、cutoff、terminal-width correction を直接測る。

### 段階4：Bell audit

joint law、marginal、CHSH、setting normalization、source posterior の全変動距離を同じ sample から計算する。observed trial の除外がないことを確認する。

### 段階5：robustness and preparation

phase noise、amplitude mismatch、additional ledger mode、action leakage、biased seed preparation、$E_*$、terminal width を変え、first harmonic、higher harmonics、no-signalling residual、completion time を同時に測る。

## 証明状態の台帳

| 主張 | 状態 |
|---|---|
| finite Fourier--Gaussian 表示 | 厳密 |
| 条件付き Gaussian law の Schur 補完 | 厳密 |
| 繰り込み作用のパラメータ $C^1$ Nelson 極限 | 指定した線形 Gaussian class で厳密 |
| local bright/anchor record | finite pulse Hamiltonian で明示 |
| cos 型差動作用 | 厳密な二次形式恒等式 |
| 固定総作用殻上の $p(h)=1/E_\ell$ | 正規化 Liouville measure について厳密 |
| 任意初期密度からの厳密な一様化 | 不成立。粗視化 mixing `[M]` のみ |
| $w_{AB}=1/4$ | symmetric preparation `[S]` の下で厳密 |
| setting-blind terminal coordinate | finite Hamiltonian pulse で明示 |
| terminal half-space の相補時計実現 | canonical transformation と向き保存条件として厳密 |
| branch-wise boundary matching から `[R]` の積形式 | matching rule を追加した条件付き定理 |
| 二つの相補的 half-space の等重み平均 | cos 項が消えるという厳密な no-go |
| Bell joint law | `[H,P,S,M,R]` と working range の下で厳密 |
| macroscopic setting normalization | `[S]` の下で厳密 |
| equilibrium no-signalling | `[S]` の下で厳密 |
| arbitrary-preparation no-signalling | 未証明 |
| `[R]` の物理的必然性 | 未導出 |
| cos comparator の一意性 | 未導出 |
| Tsirelson bound の独立導出 | 行っていない |
| Wallstrom phase quantization | 未解決 |

## 最終結論

本論文の確立した第I部の中心結果は、有限調和 Gaussian 条件付き作用の定量的パラメータ $C^1$ Nelson 極限である。第II部の中心結果は、有限 Hamiltonian 測定器、phase-locked source、symmetric preparation、固定総作用二モード台帳、setting-blind terminal condition、時間対称境界統計原理を組み合わせた Bell compatibility theorem である。

旧構成で一つの仮定にまとめていた共通入口密度は、

$$
\text{two-mode Liouville geometry}
+
\text{sector symmetry}
$$

へ分解された。これにより、soft-energy density の形は位相体積から導かれ、残る統計入力は準備対称性として明示された。

相補的内部時計により、return momentum、terminal half-space、$E_*$ はそれぞれ相対時計運動量、順序付き時計向き保存、向き反転までの初期余裕として解釈できるようになった。これは terminal device の任意性を減らす進展である。一方、`[R]` は消去されていない。時計向きが交換される Hamiltonian 軌道を物理的集団から除くには、二境界 matching または同等の all-at-once 統計原理がなお必要である。

従って `[R]` は欠陥を隠すための補助仮定ではなく、本理論が通常の初期値統計力学と異なる位置を明示する中心原理である。今後の決定的課題は、branch-wise boundary preparation と matching をより大きな物理的境界値問題から導くこと、順序付き sector の時間反転共変な完成形を構成すること、またはその実験的含意を postselection と区別することである。

\appendix

# Fourier--Gaussian 近似と Schur 補完の評価

\begin{statusbox}
位置づけ：第3章と第4章で用いた有限モード収束と条件づけの安定性を補足する。
\end{statusbox}


## 基本核の Fourier 係数

線形方程式の雑音応答核を

$$
G_\theta(t,s)
=
\mathbf 1_{0\leq s\leq t}
\Phi_\theta(t,s)
$$

とする。$s=t$ に跳びがあるため、$s$ に関する Fourier 係数は一般に $O(n^{-1})$ である。

\begin{lemma}[一様 Fourier 尾部]
$F_\theta$ が第4.2節の仮定を満たすなら、ある $C_K$ が存在して

$$
\sup_{\theta\in K,\,t\in[0,T]}
\|\widehat G_{\theta,n}(t)\|
\leq
\frac{C_KT}{1+|n|},
$$

$$
\sup_{\theta\in K,\,t\in[0,T]}
\|D_\theta\widehat G_{\theta,n}(t)\|
\leq
\frac{C_KT}{1+|n|}
$$

が成立する。従って共分散尾部は

$$
\sup_{\theta,s,t}
\left(
\|C_N(s,t)-C(s,t)\|
+\|D_\theta C_N(s,t)-D_\theta C(s,t)\|
\right)
\leq
\frac{C_KT^2}{N}
$$

である。
\end{lemma}

\begin{proof}
$n\neq0$ に対して $e^{-i\omega_ns}$ を部分積分する。区間端と $s=t$ の跳びから $1/\omega_n$ の境界項が生じ、区間内部では $\partial_s\Phi(t,s)=-\Phi(t,s)F(s)$ が一様有界である。従って $|\widehat G_n|\leq C/|\omega_n|$ を得る。

$\theta$ 微分については

$$
D\Phi_\theta[\delta F](t,s)
=
\int_s^t
\Phi_\theta(t,r)
\delta F(r)
\Phi_\theta(r,s)
\dd r
$$

を使う。$D\Phi$ とその $s$ 微分も一様有界なので同じ部分積分評価が成立する。共分散は Fourier 係数の積の和であり、

$$
\sum_{|n|>N}\frac1{n^2}\leq\frac{C}{N}
$$

から結論を得る。
\end{proof}

## 平均の収束

本論文では $F_\theta$、$f_\theta$、初期平均は $N$ に依存しないため、無条件平均は $\mu_N=\mu$ である。浴切断に依存する補正平均を許す場合でも、Fourier 尾部が中心化されていれば平均差は零であり、非零の決定論的尾部を加えた場合はその $L^1$ ノルムで直接評価できる。

条件付き平均は $C_N(t,T)$ と $C_N(T,T)$ に依存するため、共分散尾部から $O(1/N)$ の差を持つ。

## Schur 補完の安定性

$S_N=HC_N(T,T)H^{\mathsf T}+R$、$S=HC(T,T)H^{\mathsf T}+R$ とする。$R\geq r_*I$ なので

$$
\|S_N^{-1}\|\leq r_*^{-1},
\qquad
\|S^{-1}\|\leq r_*^{-1}.
$$

逆行列恒等式

$$
S_N^{-1}-S^{-1}
=
S_N^{-1}(S-S_N)S^{-1}
$$

から

$$
\|S_N^{-1}-S^{-1}\|
\leq
r_*^{-2}\|S_N-S\|
$$

を得る。従って条件付き共分散について

$$
\sup_{s,t,\theta}
\|C_N^R(s,t)-C^R(s,t)\|
\leq
\frac{C_KT^2}{N}
$$

である。

第1微分では

$$
D(S^{-1})=-S^{-1}(DS)S^{-1}
$$

を用いる。$S_N^{-1}$、$DS_N$ が一様有界なので、積の各因子を1つずつ差し替えることで

$$
\sup_{s,t,\theta}
\|D C_N^R(s,t)-D C^R(s,t)\|
\leq
\frac{C_KT^2}{N}
$$

を得る。条件付き平均も同様である。

## 有限分解能の役割

$R>0$ は、観測値 $y$ の周囲に有限幅の終端領域を持たせる。これにより、条件付き共分散は $T$ で完全には消えず、条件付き流れの係数は閉区間 $[0,T]$ 上で有界に保たれる。

$R\downarrow0$ とすると、完全観測された方向の終端共分散は零へ近づく。自由拡散では前進条件付き流れに

$$
\frac{y-x}{T-t}
$$

型の項が現れる。点終端での定理を得るには、$t=T$ の境界層を除いた区間で先に $N\to\infty$、$h\to0$ を取り、その後に境界層と $R\downarrow0$ を別に評価する必要がある。

## 自由終端固定と零周波数

自由系では

$$
X_N(T)-X_N(0)
=
\int_0^T\widetilde\eta_N(t)\dd t
=
\sqrt{2\nu T}\,Z_0.
$$

従って $X_N(T)=X_N(0)$ は $Z_0=0$ と同値である。非零モードは終端条件と独立なので、条件付き共分散から零モードの寄与 $2\nu/T$ だけが除かれる。この計算は、旧来の $-1/T$ が浴の基本性質ではなく、自由終端固定の結果であることを最も直接に示す。

## 一般線形系では全モードが条件づけられる

$F\neq0$ では

$$
X_N(T)
=
\Phi(T,0)X_N(0)
+\sum_\alpha K_{N,\alpha}(T)\zeta_\alpha
+d_N(T)
$$

である。ここで $d_N(T)$ は決定論項であり、一般に $K_{N,\alpha}(T)\neq0$ である。終端記録は零周波数だけでなく全ての Fourier 係数の線形結合を拘束する。そのため条件付き雑音共分散の修正は階数有限の Schur 項となり、流れ $F$、観測 $H$、分解能 $R$ に依存する。

# 粗視化作用の $C^1$ 評価

\begin{statusbox}
位置づけ：時間粗視化誤差と Fourier 切断誤差を分離し、主定理の評価を補足する。
\end{statusbox}


## Gaussian 増分の正確な表示

条件付き Gaussian 過程の増分 $\Delta_hX(t)=X(t+h)-X(t)$ に対して

$$
\E^R|\Delta_hX(t)|^2
=
|\mu^R(t+h)-\mu^R(t)|^2
+\Tr\left[
C^R(t+h,t+h)+C^R(t,t)-2C^R(t+h,t)
\right]
$$

が厳密に成立する。従って粗視化作用の運動項は、条件付き平均と共分散だけで計算できる。

有限 $N$ でも同じ式が成立する。$C_N^R-C^R=O(1/N)$ なので、増分2乗の有限モード誤差は粗い評価で $O(1/N)$、$h^{-2}$ を掛けた作用誤差は $O(1/(Nh^2))$ となる。

## 時間対角の展開

極限拡散について、$X_t=x$ を固定した短時間増分は

$$
\Delta_hX
=
b_+^R(x,t)h
+\sqrt{2\nu}\Delta_hW
+O_{L^2}(h^{3/2})
$$

である。流れの空間依存と雑音の相関による交差項まで含めて平均すると

$$
\E^R
\left[
|\Delta_hX|^2\mid X_t=x
\right]
=
2d\nu h
+h^2
\left[
|b_+^R(x,t)|^2
+2\nu\nabla\cdot b_+^R(x,t)
\right]
+O(h^3).
$$

線形流れでは3階剰余を平均・微分した量も一様に有界である。$m/(2h^2)$ を掛けると

$$
\frac m{2h^2}\E^R|\Delta_hX|^2
-\frac{md\nu}{h}
=
\E^R
\left[
\frac m2|b_+^R|^2
+m\nu\nabla\cdot b_+^R
\right]
+O(h).
$$

積分上端を $T-h$ で止めたことによる欠落も $O(h)$ である。

## なぜ発散項が残るか

雑音の主要項 $2d\nu h$ だけを差し引いても、流れと短時間雑音の交差効果は $h^2$ の有限項として残る。それが

$$
m\nu\nabla\cdot b_+^R
$$

である。この項を落とすと、極限は正しい Guerra--Morato 作用にならず、Nelson 表示の負の Fisher 項も得られない。

## Fourier 切断誤差

付録Aの評価から

$$
\|C_N^R-C^R\|_{C^1(K;C([0,T]^2))}
\leq
\frac{C_KT^2}{N}
$$

である。増分共分散は4つの共分散値の線形結合なので、

$$
\left|
\E_N^R|\Delta_hX_N|^2
-
\E^R|\Delta_hX|^2
\right|_{C^1(K)}
\leq
\frac{C_KT^2}{N}.
$$

従って運動項の差は

$$
\frac{C_KT^2}{Nh^2}
$$

で抑えられる。この評価は最適とは限らないが、$N(h/T)^2\to\infty$ という単純な対角極限を与える。

## 2次ポテンシャル

$U(x,t)=x^{\mathsf T}K(t)x/2+\ell(t)^{\mathsf T}x+c(t)$ なら

$$
\E^R[U(X_t,t)]
=
\frac12\mu^R(t)^{\mathsf T}K(t)\mu^R(t)
+\frac12\Tr[K(t)C^R(t,t)]
+\ell(t)^{\mathsf T}\mu^R(t)
+c(t).
$$

従ってポテンシャル期待値とそのパラメータ第1微分は、$\mu_N^R$ と $C_N^R$ の $O(1/N)$ 収束から直接従う。これは運動項の $O(1/(Nh^2))$ より小さく、主定理の右辺へ吸収できる。

一般の滑らかな非2次ポテンシャルでは、Gaussian moment 展開または一様可積分性を用いて同様の結果を拡張できる可能性がある。しかし第1微分には解写像の応答と $\nabla U$ の積が現れるため、本論文では証明が閉じる2次範囲に限定する。

## パラメータ第1微分

作用を $\theta_j$ で微分すると、平均、共分散、条件付き Schur 項、ポテンシャル係数の微分が現れる。基本行列の微分公式と $R\geq r_*I$ により、全ての係数は $K$ 上で一様有界である。

時間対角展開を微分した剰余も $O(h)$、Fourier 尾部を微分した誤差も $O(T^2/(Nh^2))$ である。有限個の $\theta_j$ について最大を取れば

$$
\|\mathcal A_{N,h}^{R,U}-\mathcal A_{\GM}^{R,U}\|_{C^1(K)}
\leq
C_K
\left(
\frac hT+\frac{T^2}{Nh^2}
\right)
$$

を得る。

## 対角尺度の選択

$h/T=N^{-\alpha}$ と置くと、2つの誤差は

$$
N^{-\alpha},
\qquad
N^{2\alpha-1}
$$

である。両者を同じ次数にするには $\alpha=1/3$ とすればよい。従って

$$
h_N=TN^{-1/3},
\qquad
\varepsilon_N=O(N^{-1/3})
$$

となる。ここで $\varepsilon_N$ は全評価誤差を表す。

この選択は、粗視化窓を短くしすぎると未解像の Fourier 尾部が増幅され、長くしすぎると局所 Nelson 作用から外れる、という物理的な釣り合いを表す。

# 明示 Hamiltonian、二モード位相体積、補正項

\begin{statusbox}
位置づけ：第II部で用いた canonical map、作用殻測度、多モード補正を詳細に計算する。
\end{statusbox}


## Poisson structure

各 canonical pair $(q_j,p_j)$ に

$$
\{q_j,p_k\}
=
\delta_{jk}
$$

を置く。messenger vector $u=(Q,P)^{\mathsf T}$ と action

$$
I=\frac12(Q^2+P^2)
$$

に対し、生成子

$$
K_{\rm rot}
=
-\theta I
$$

の unit flow は

$$
\dot Q=-\theta P,
\qquad
\dot P=\theta Q
$$

なので

$$
u(1)
=
R(\theta)u(0).
$$

$\theta=\phi(a)+\pi\chi_-(s)$ とし、seed plateau 上で $A=\sigma(s)$ とすれば

$$
R
\left[
\phi(a)+\pi\chi_-(s)
\right]
=
A R[\phi(a)].
$$

従って outcome sign を messenger phase の $\pi$ shift として canonical に記録できる。

## bright shift と anchor shift

bright pair $(x,p)$ に対する生成子

$$
K_{\rm br}
=
-x\sigma(s)
$$

は

$$
\dot p
=
-\frac{\partial K_{\rm br}}{\partial x}
=
\sigma(s),
$$

$$
\dot x
=
\frac{\partial K_{\rm br}}{\partial p}
=
0
$$

を与える。$p(0)=0$ なら $p(1)=A$ である。

anchor pair $(Y,\Pi)$ に対する

$$
K_{\rm lock}
=
-Y\zeta(p)
$$

は

$$
\dot\Pi
=
-\frac{\partial K_{\rm lock}}{\partial Y}
=
\zeta(p),
$$

$$
\dot Y=0,
\qquad
\dot p=0
$$

を与える。$\zeta(\pm1)=\pm1$ の plateau で $\Pi(0)=0$ なら、

$$
\Pi(1)=A.
$$

二つの map は Hamiltonian flow なので phase volume を保存する。bright information を local bath へ分散した後も、anchor pair を decouple すれば comparator window 中の record sign は保たれる。

## autonomous clock

clock pair $(\vartheta,J_c)$ と mutually disjoint pulse profile $f_\nu(\vartheta)$ を用い、

$$
H
=
\Omega J_c
+H_0
+\Omega
\sum_\nu
f_\nu(\vartheta)K_\nu
$$

とする。$K_\nu$ と $H_0$ が $J_c$ に依存しないとき、

$$
\dot\vartheta=\Omega.
$$

$f_\nu$ を

$$
\int_{\operatorname{supp}f_\nu}
f_\nu(\vartheta)d\vartheta=1
$$

と規格化すれば、対応する time interval で

$$
\int
\Omega f_\nu[\vartheta(t)]dt=1.
$$

従って idealized nonoverlapping limit で $K_\nu$ の unit canonical map が得られる。有限 pulse overlap は Baker--Campbell--Hausdorff expansion に従う commutator correction を生む。operator norm が有界な working region では、overlap duration を $\delta_t$ として leading error は $O(\delta_t\| \{K_\mu,K_\nu\}\|)$ で評価できる。

## 相補的内部時計、二境界 matching、向き平均 no-go

まず、時計運動量を $\pm\varrho_0$ の極小へ固定するだけの Hamiltonian

$$
H_{\rm stop}
=
\frac{\kappa_c}{2}
\left(
\varrho_A+\varrho_B
\right)^2
+
\frac{\lambda_c}{4}
\sum_{X=A,B}
\left(
\varrho_X^2-\varrho_0^2
\right)^2
$$

は用いない。極小

$$
\left(
\varrho_A,\varrho_B
\right)
=
\left(
+\varrho_0,-\varrho_0
\right)
$$

では

$$
\dot\tau_X
=
\frac{\partial H_{\rm stop}}{\partial\varrho_X}
=
0
$$

となり、向きは区別できても時計が進まないからである。

実際に相補的な時計運動を作る最小の二次 Hamiltonian として

$$
H_{\rm or}
=
\frac{\varrho_A^2+\varrho_B^2}{2M_\tau}
+
\frac{\kappa_c}{2}
\left(
\varrho_A+\varrho_B
\right)^2
$$

を用いる。center--relative variables を

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

と定めると、

$$
\varrho_A\,d\tau_A
+
\varrho_B\,d\tau_B
=
P_c\,d\bar\tau
+
\Pi_R\,dY_R.
$$

従って変換は正準であり、

$$
H_{\rm or}
=
\frac{\Pi_R^2}{M_\tau}
+
\left(
\frac{1}{4M_\tau}
+
\frac{\kappa_c}{2}
\right)
P_c^2.
$$

$P_c=0$ 上では

$$
\varrho_A=\Pi_R,
\qquad
\varrho_B=-\Pi_R,
$$

$$
\dot\tau_A
=
\frac{\Pi_R}{M_\tau},
\qquad
\dot\tau_B
=
-\frac{\Pi_R}{M_\tau}.
$$

source で $\Pi_R(0)=E_*>0$ を準備し、return generator を

$$
K_R
=
F_R(Y_R)
\left(
h-\kappa I_-
\right)
$$

とする。$K_R$ は $\bar\tau$ に依存しないので $P_c=0$ は保たれる。また $Y_R=0$、$F_R'(0)=1$ の readout orbit 上で

$$
\Delta\Pi_R
=
\kappa I_- -h,
$$

$$
\Pi_R(T)
=
E_*+\kappa I_- -h.
$$

従って

$$
\Pi_R(T)\geq0
\quad\Longleftrightarrow\quad
\varrho_A(T)\geq0
\ \hbox{and}\
\varrho_B(T)\leq0.
$$

terminal half-space は、source で選んだ時計向きの順序を保存した履歴の集合として得られる。一方、$\Pi_R(T)<0$ の軌道も正則な Hamiltonian 軌道であり、時計向きが交換されるだけである。

この half-space から `[R]` の積形式を得るには、さらに二境界の statistical matching を置く必要がある。初期境界の密度を $\rho_S(z_i)$、逆向き時計の clock-past に対応する終端関数を $G_{\rm or}(z_f)$ とし、両枝が同じ Hamiltonian 履歴を表す条件を

$$
\delta
\left(
z_f-\Phi_{a,b}^{T}z_i
\right)
$$

で課す。履歴空間上の測度を

$$
d\nu
=
\frac1{\mathcal Z}
\rho_S(z_i)
G_{\rm or}(z_f)
\delta
\left(
z_f-\Phi_{a,b}^{T}z_i
\right)
d\Gamma_i\,d\Gamma_f
$$

とすれば、$z_f$ 積分により

$$
d\nu_i
=
\frac1{\mathcal Z}
\rho_S(z_i)
G_{\rm or}
\left(
\Phi_{a,b}^{T}z_i
\right)
d\Gamma_i.
$$

これは `[R]` と同じ積形式である。Hamiltonian flow の Jacobian が1であるため、逆向きに積分しても余分な密度因子は出ない。ただし二つの境界密度を掛け、matching する規則は Hamilton 方程式とは別の all-at-once 統計原理である。

最後に、向きの順序を指定しない素朴な平均を考える。同じ scalar readout

$$
\Pi_R(T)
=
x-h,
\qquad
x
=
E_*+\kappa I_-,
$$

に対して正向き half-space を $\Pi_R(T)\geq0$、相補的 half-space を $\Pi_R(T)\leq0$ とし、$0\leq x\leq E_\ell$ で一様な $h$ を積分すると、

$$
F_+(x)
=
\int_0^{E_\ell}
\frac{dh}{E_\ell}
\mathbf1_{\{h\leq x\}}
=
\frac{x}{E_\ell},
$$

$$
F_-(x)
=
\int_0^{E_\ell}
\frac{dh}{E_\ell}
\mathbf1_{\{h\geq x\}}
=
1-\frac{x}{E_\ell}.
$$

両者を等重みで足せば

$$
\frac12
\left[
F_+(x)+F_-(x)
\right]
=
\frac12
$$

となり、$I_-$ の cos dependence は消える。従って $\varrho_A=-\varrho_B$ という無向きの相補性だけでは Bell weight を保てない。順序付き boundary sector を採るか、時間反転した sector では comparator kick の符号も反転する共変な追加構造が必要である。

## difference-mode action

二つの messenger を

$$
u_A
=
A r_A R[\phi(a)]n(\Theta_A),
$$

$$
u_B
=
B r_B R[\phi(b)]n(\Theta_B)
$$

とする。symplectic beam splitter

$$
u_+
=
\frac{u_A+u_B}{\sqrt2},
\qquad
u_-
=
\frac{u_A-u_B}{\sqrt2}
$$

は total action を保存する。

$$
\frac12\|u_A\|^2
+\frac12\|u_B\|^2
=
\frac12\|u_+\|^2
+\frac12\|u_-\|^2.
$$

antisymmetric port の action は

$$
\frac12\|u_-\|^2
=
\frac14\|u_A-u_B\|^2
=
I_-.
$$

内積を展開して

$$
I_-
=
\frac14
\left[
r_A^2+r_B^2
-2ABr_Ar_B\cos\Delta_{ab}
\right]
$$

を得る。この物理的 beam-splitter map を実行してから antisymmetric port の action を comparator へ結合してもよく、同じ quadratic observable へ直接結合してもよい。

## return-pointer shift

return generator

$$
K_R
=
F_R(Y_R)
\left[
h-\kappa I_-
\right]
$$

に対して

$$
\dot Y_R
=
\frac{\partial K_R}{\partial\Pi_R}
=
0.
$$

$Y_R(0)=0$ なら $Y_R(\tau)=0$ である。$F_R(0)=0$ から、readout orbit 上で

$$
\dot q_s
=
\frac{\partial K_R}{\partial p_s}
=
0,
\qquad
\dot p_s
=
-\frac{\partial K_R}{\partial q_s}
=
0
$$

となり、messenger variables も同様に動かない。一方、

$$
\dot\Pi_R
=
-F_R'(0)
\left[
h-\kappa I_-
\right].
$$

$F_R'(0)=1$、$\Pi_R(0)=E_*$ なら

$$
\Pi_R(1)
=
E_*+\kappa I_- -h.
$$

従って comparator は $I_-$ と $h$ を破壊せずに差だけを pointer へ記録する。

## 二モード作用殻の正規化

二つの action-angle pair に対し、

$$
\mathcal N(E_\ell)
=
\int_0^\infty
dJ_s
\int_0^{2\pi}
d\theta_s
\int_0^\infty
dJ_0
\int_0^{2\pi}
d\theta_0
\delta
\left[
E_\ell-\omega_\ell(J_s+J_0)
\right].
$$

$J_0$ を積分すると

$$
\mathcal N(E_\ell)
=
\frac{(2\pi)^2}{\omega_\ell}
\int_0^{E_\ell/\omega_\ell}
dJ_s
=
\frac{(2\pi)^2E_\ell}{\omega_\ell^2}.
$$

$h=\omega_\ell J_s$ の interval $[h,h+dh]$ に入る shell measure は

$$
d\mathcal N_h
=
\frac{(2\pi)^2}{\omega_\ell^2}dh.
$$

従って

$$
p_\ell(h)dh
=
\frac{d\mathcal N_h}{\mathcal N(E_\ell)}
=
\frac{dh}{E_\ell}.
$$

equivalently、rescaled Cartesian coordinate

$$
\frac1{\sqrt{2J_\ell}}
\left(
q_s,p_s,q_0,p_0
\right)
$$

は3-sphere $S^3$ 上にあり、

$$
\frac{J_s}{J_\ell}
=
\frac{q_s^2+p_s^2}{
q_s^2+p_s^2+q_0^2+p_0^2
}
$$

は Beta$(1,1)$、すなわち $[0,1]$ 上の一様分布である。

## mixer generators

次を定義する。

$$
J_x=q_sq_0+p_sp_0,
$$

$$
J_y=q_sp_0-p_sq_0,
$$

$$
J_z=\frac12
\left(
q_s^2+p_s^2-q_0^2-p_0^2
\right),
$$

$$
J_\ell
=
\frac12
\left(
q_s^2+p_s^2+q_0^2+p_0^2
\right).
$$

Poisson bracket を直接計算すると、

$$
\{J_\ell,J_i\}=0,
\qquad
i=x,y,z.
$$

また、規格化の取り方に応じた定数因子を除き、$J_x,J_y,J_z$ は $\mathfrak{su}(2)$ 型の閉じた bracket を持つ。従って

$$
K_M
=
a_x(t)J_x+a_y(t)J_y+a_z(t)J_z
$$

の各 flow は $S^3$ 上の measure-preserving orientation map である。係数 $a_i(t)$ を有限 nonlinear environment と autonomous clock から生成すれば、全系を Hamiltonian に保ったまま複雑な orientation dynamics を作れる。

この事実は $p(h)$ の invariant reference measure を保証するが、特定の deterministic coefficient sequence が mixing であることを自動的には保証しない。mixing rate は別途 correlation decay または transfer-operator spectrum で検証する必要がある。

## 多モード simplex marginal

soft energy $h$ と $N$ 個の ledger energy $e_1,\ldots,e_N$ が

$$
h+\sum_{j=1}^{N}e_j=E_\ell
$$

を満たすとする。各 harmonic pair の phase angle を積分すると定数になる。$h$ を固定した残余 simplex

$$
\sum_{j=1}^{N}e_j=E_\ell-h,
\qquad
e_j\geq0
$$

の surface multiplicity は

$$
\frac{(E_\ell-h)^{N-1}}{(N-1)!}
$$

に比例する。規格化から

$$
p_N(h)
=
\frac{N}{E_\ell}
\left(
1-\frac h{E_\ell}
\right)^{N-1}.
$$

cumulative distribution は

$$
F_N(x)
=
1-
\left(
1-\frac x{E_\ell}
\right)^N.
$$

$N=1$ でのみ linear である。$x=C-ABKc$ と書けば、

$$
F_N(C-ABKc)
=
1-
\sum_{m=0}^{N}
\binom Nm
\left(
1-\frac C{E_\ell}
\right)^{N-m}
\left(
\frac{ABKc}{E_\ell}
\right)^m.
$$

偶数 $m$ は outcome parity に依存しない normalization correction、奇数 $m\geq3$ は $c^3,c^5,\ldots$ を通じて higher angular harmonics を生む。従って extra ledger modes は単なる visibility renormalization ではない。

## finite terminal width

sharp indicator を monotone response $g_\epsilon$ へ置き換える。

$$
G_{R,\epsilon}
=
g_\epsilon
\left(
E_*+\kappa I_- -h
\right).
$$

一様 soft density に対する compatibility は

$$
F_\epsilon(x)
=
\frac1{E_\ell}
\int_0^{E_\ell}
g_\epsilon(x-h)dh.
$$

$g_\epsilon$ が Heaviside function と symmetric smoothing kernel の convolution なら、

$$
\frac{dF_\epsilon}{dx}
=
\frac1{E_\ell}
\left[
g_\epsilon(x)-g_\epsilon(x-E_\ell)
\right].
$$

内部領域

$$
\epsilon\ll x\ll E_\ell-\epsilon
$$

では $g_\epsilon(x)\approx1$、$g_\epsilon(x-E_\ell)\approx0$ なので、

$$
\frac{dF_\epsilon}{dx}
\approx
\frac1{E_\ell}.
$$

endpoint 近傍でのみ slope と offset が変わる。従って $E_*$ は zero channel を boundary layer から離す一方、visibility を低下させる。

## forward-bath no-go

記録形成後の四 sector を $\Gamma_{AB}$ とし、共通浴を含む後段 flow を $\Psi^t$ とする。Liouville measure に関して

$$
\mu(\Psi^t\Gamma_{AB})
=
\int_{\Psi^t\Gamma_{AB}}d\Gamma
=
\int_{\Gamma_{AB}}
\left|
\det D\Psi^t
\right|
d\Gamma.
$$

Hamiltonian flow では

$$
\det D\Psi^t=1
$$

なので

$$
\mu(\Psi^t\Gamma_{AB})
=
\mu(\Gamma_{AB}).
$$

従って future bath coupling は forward ensemble の sector mass を変えない。terminal conditioning を加えると

$$
\mu_R(\Gamma_{AB})
\propto
\int_{\Gamma_{AB}}
G_R(\Psi^T z)
d\mu(z)
$$

となり、sector mass は変わり得る。しかし変化を生むのは bath noise の leakage そのものではなく、future flow と $G_R$ を組み合わせた boundary reweighting である。

## algebraic consistency checks

実装の最小 check は次である。

1. random angle と sign について、直接計算した $\|u_A-u_B\|^2/4$ と analytic $I_-$ を比較する。
2. $S^3$ 上の isotropic Gaussian vector を規格化し、$J_s/J_\ell$ の empirical CDF と uniform CDF を比較する。
3. $\Pi_R(0)=E_*$ と $\Delta\Pi_R=\kappa I_- -h$ から、相補時計の終端向き条件を検算する。
4. $h\leq E_*+\kappa I_-$ の indicator を Monte Carlo 積分し、analytic $W_{AB}$ と比較する。
5. 四 outcome を規格化し、marginal residual と CHSH を計算する。
6. $F_+(x)+F_-(x)=1$ を検算し、等重み orientation average で cos 項が消えることを確認する。
7. extra ledger modes を追加し、predicted $F_N(x)$ と higher harmonics を比較する。

これらは Hamiltonian mixing の証明ではない。幾何、normalization、sampling implementation に循環または符号誤りがないことを確認する代数的検証である。

# Gaussian Nelson 方程式、Schrödinger 表示、OU 例

\begin{statusbox}
位置づけ：主定理の極限作用が与える物理像と、その適用範囲を具体例で示す。
\end{statusbox}


## 連続の式を組み込んだ変分

Nelson 作用を

$$
\mathcal A_{\Nel}[\rho,v]
=
\int\rho
\left[
\frac m2|v|^2
-\frac{m\nu^2}{2}|\nabla\log\rho|^2
-U
\right]\dd x\dd t
$$

とする。制約

$$
\partial_t\rho+\nabla\cdot(\rho v)=0
$$

を Lagrange 乗数 $S$ で課す。$v$ について変分すると

$$
mv=\nabla S
$$

を得る。$\rho$ について変分すると

$$
\partial_tS
+\frac{|\nabla S|^2}{2m}
+U
-2m\nu^2
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=0
$$

となる。最後の項は密度勾配エネルギーの変分である。

## Schrödinger 表示

有効作用定数を

$$
\hbar_{\rm eff}=2m\nu
$$

とし、

$$
\psi=\sqrt\rho
\exp\left(\frac{iS}{\hbar_{\rm eff}}\right)
$$

と置く。連続の式と前節の Hamilton--Jacobi 型方程式を合わせると

$$
i\hbar_{\rm eff}\partial_t\psi
=
\left[
-\frac{\hbar_{\rm eff}^2}{2m}\Delta+U
\right]\psi
$$

を得る \cite{nelson1966,guerra_morato1983,yasue1981,zambrini1986}。

この変換は、$\rho>0$ で $v$ が局所的に勾配場となる領域では厳密である。しかし、多重連結領域の循環量子化、節を横切る位相接続、一般の重ね合わせ状態は追加条件を必要とする \cite{wallstrom1994}。本論文の線形 Gaussian 定理は正の密度領域に限定され、この大域位相問題を解かない。

## 1次元 Gaussian 変分

平均 $q(t)$、標準偏差 $\sigma(t)>0$ の Gaussian 密度を考える。

$$
\rho(x,t)
=
\frac1{\sqrt{2\pi}\sigma}
\exp\left[-\frac{(x-q)^2}{2\sigma^2}\right].
$$

連続の式を満たす最小の1次速度場は

$$
v=\dot q+\frac{\dot\sigma}{\sigma}(x-q),
$$

浸透速度は

$$
u=-\nu\frac{x-q}{\sigma^2}
$$

である。Gaussian 平均を取ると

$$
\E[v^2]=\dot q^2+\dot\sigma^2,
\qquad
\E[u^2]=\frac{\nu^2}{\sigma^2}.
$$

調和ポテンシャル $U=m\Omega^2x^2/2$ では

$$
\E[U]=\frac{m\Omega^2}{2}(q^2+\sigma^2)
$$

なので、第4.7節の有限次元作用を得る。

## 幅方程式の保存量

幅方程式

$$
\ddot\sigma+\Omega^2\sigma-\frac{\nu^2}{\sigma^3}=0
$$

には

$$
E_\sigma
=
\frac12\dot\sigma^2
+\frac12\Omega^2\sigma^2
+\frac{\nu^2}{2\sigma^2}
$$

という保存量がある。$\sigma\to0$ では最後の項が発散するため、正の初期幅は有限時間で零にならない。定常点 $\sigma_*^2=\nu/\Omega$ の周囲では幅が振動する。

この振る舞いは、通常の熱拡散が平衡へ単調緩和する像とは異なる。Nelson 作用では、確率流の運動項と密度勾配項が実時間の変分原理で釣り合い、可逆な幅運動を作る。

## 2次元 OU 位相模型

計算例として

$$
\dd Z_t
=
(-\lambda I+\Omega J)Z_t\dd t
+\sqrt{2D}\,\dd W_t,
\qquad
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
$$

を考える \cite{uhlenbeck_ornstein1930}。$\lambda>0$ なら定常共分散は

$$
\operatorname{Cov}(Z)=\frac D\lambda I
$$

である。$\Omega=0$ なら定常過程は詳細釣り合いを満たす。$\Omega\neq0$ では縮約された位相平面に定常回転流があり、通常の時間反転だけでは詳細釣り合いを満たさない。

このことは微視的 Hamiltonian 中核の可逆性と矛盾しない。$\lambda$ は消去した浴への有効緩和、$\Omega$ は残した調和回転を表す。OU 模型は観測部分系の計算表示であり、閉じた全系そのものではない。

## Itô と Stratonovich

一般に

$$
\dd X=b(X,t)\dd t+\sigma(X,t)\circ\dd W_t
$$

を Itô 表現へ変換すると、$\sigma$ の空間微分に比例する補正が流れへ加わる。本論文では $\sigma=\sqrt{2\nu}I$ が定数なので補正は零である。

従って線形 Gaussian 定理、Schur 補完、Guerra--Morato 作用、Nelson 表示のいずれも、Itô と Stratonovich の記法選択に依存しない。Stratonovich 微分は、乗法的雑音へ拡張するときに初めて本質的になる。

## Bell 部分との接続

2次元 Gaussian 位相変数は、第6章の実正準 messenger を具体化する候補になる。しかし、OU 定常分布だけでは左右の等振幅、共通生成時位相、四つの符号領域の対称性は自動的に保証されない。

従って

$$
\mathrm{OU}_{2D}
\quad\not\Rightarrow\quad
\mathrm{Bell\ cosine\ law}.
$$

Bell 系論には、phase-locked source `[P]`、symmetric preparation `[S]`、two-mode entrance measure `[M]`、boundary ensemble `[R]` が別に必要である。この点を保つことで、Gaussian Nelson 部分と Bell 部分の役割が明確になる。

# 測定依存度、CHSH 四設定、postselection 監査

\begin{statusbox}
位置づけ：第II部の Bell 分類を定量化し、装置 posterior と表現論的最小値を区別する。
\end{statusbox}


## Hall scale

setting-dependent hidden distribution に対する Hall の $L^1$ scale を

$$
M
=
\sup_{a,b,a',b'}
\int
\left|
\rho(\lambda\mid a,b)
-\rho(\lambda\mid a',b')
\right|
d\lambda
$$

とする。通常の total variation とは

$$
M=2D_{\rm TV}^{\max}
$$

の関係にある。

第7.6節の最小 two-mode posterior では、

$$
D_{\rm TV}(c,c')
=
\frac{V_{\rm eff}}2
|c-c'|
$$

なので、

$$
M_{\rm dev}
=
V_{\rm eff}
\sup_{a,b,a',b'}
\left|
\cos\Delta_{ab}
-\cos\Delta_{a'b'}
\right|.
$$

全角度を許せば

$$
M_{\rm dev}=2V_{\rm eff}.
$$

標準 CHSH の四 setting pair では cosine が $\pm1/\sqrt2$ なので、

$$
M_{\rm dev}^{(4)}
=
\sqrt2V_{\rm eff}.
$$

これは本文の具体的 device posterior が持つ値であり、同じ observable joint law を再現する全 local model の中で最小化した値ではない。

## ledger-only representation

hidden variable を

$$
\lambda_{\rm tab}
=
(A_*,B_*)
\in
\{\pm1\}^2
$$

とし、

$$
\mathscr A(a,\lambda_{\rm tab})=A_*,
\qquad
\mathscr B(b,\lambda_{\rm tab})=B_*,
$$

$$
\rho_{\rm tab}(A_*,B_*\mid a,b)
=
\frac14
\left[
1-A_*B_*V_{\rm eff}\cos\Delta_{ab}
\right]
$$

と置けば、local deterministic に目標 joint law を再現する。この representation は出力確率を hidden ledger に直接書き込んだものであり、物理的説明ではない。

Hall scale は

$$
M_{\rm tab}
=
V_{\rm eff}
\sup_{a,b,a',b'}
\left|
\cos\Delta_{ab}
-\cos\Delta_{a'b'}
\right|
$$

である。従って two-mode device posterior の coarse marginal と同じ値を持つ。この一致は装置構成の最適性を意味せず、両者が同じ support-length modulation を使っていることを示す。

## 標準 CHSH 四設定の最小値

標準 CHSH 四設定に対し、目標 visibility $V_{\rm eff}$ を再現する local deterministic、operationally no-signalling representation 全体で Hall scale を最小化した値を $M_{\min}^{(4)}(V_{\rm eff})$ とする。

$V_{\rm eff}\leq1/\sqrt2$ では全 CHSH inequality が満たされる。Fine の定理により setting-independent joint hidden distribution が存在するので \cite{fine1982}、

$$
M_{\min}^{(4)}(V_{\rm eff})
=
0,
\qquad
0\leq V_{\rm eff}\leq\frac1{\sqrt2}.
$$

$V_{\rm eff}>1/\sqrt2$ では、Hall の relaxed CHSH bound

$$
|\mathcal S|
\leq
2+\min\{3M,2\}
$$

と

$$
|\mathcal S|
=
2\sqrt2V_{\rm eff}
$$

から

$$
M_{\min}^{(4)}(V_{\rm eff})
\geq
\frac{
2\sqrt2V_{\rm eff}-2
}{3}
$$

を得る \cite{hall2010}。

この bound は、$V_{\rm eff}=1/\sqrt2$ の setting-independent Fine model と、$V_{\rm eff}=1$ で bound を saturate する Hall model を setting-independent flag で混合することで達成できる。従って

$$
M_{\min}^{(4)}(V_{\rm eff})
=
\max
\left\{
0,
\frac{
2\sqrt2V_{\rm eff}-2
}{3}
\right\}.
$$

特に $V_{\rm eff}=1$ では

$$
M_{\min}^{(4)}
=
\frac{
2(\sqrt2-1)
}{3},
$$

一方、本文の device posterior は

$$
M_{\rm dev}^{(4)}=\sqrt2.
$$

従って明示 device は measurement-dependence resource について最適でない。

この最小値は四つの観測分布に対する representation-theoretic quantity である。finite Hamiltonian apparatus が同じ最小値を実現できることを意味しない。全角度の cosine family に対する device-constrained minimum も本論文では求めない。

## setting frequency と source posterior

controller prior を $P_S(a,b)$ とし、full boundary measure を controller まで含めて規格化すると、

$$
P_R(a,b)
=
\frac{
P_S(a,b)Z_{a,b}
}{
\sum_{a',b'}
P_S(a',b')Z_{a',b'}
}.
$$

本文の symmetric model では

$$
Z_{a,b}
=
\frac{E_*+\kappa I_0}{E_\ell}
$$

が一定なので、

$$
P_R(a,b)=P_S(a,b).
$$

従って macroscopic setting frequency の自由と microscopic source posterior の setting dependence は両立する。これは measurement independence failure と、実験者が controller macrostate を変えられないという主張を区別する。

## launch count、record count、completion count

各 setting pair について次の三つの数を区別する。

1. external source が開始した launch count $N_{\rm launch}$。
2. 左右 pointer が definite result を持った record count $N_{\rm rec}$。
3. terminal apparatus が ready macroregion に入った completion count $N_R$。

boundary ontology `[R]` では、物理的に実現する trial 自体が terminal-compatible history であると解釈する。しかし laboratory implementation が単に

$$
N_R<N_{\rm rec}
$$

となる trial rejection を行うなら、observed sample は

$$
P_{\rm obs}(A,B\mid a,b)
=
\frac{
P_{\rm rec}(A,B\mid a,b)
\eta_{AB}(a,b)
}{
\sum_{A',B'}
P_{\rm rec}(A',B'\mid a,b)
\eta_{A'B'}(a,b)
}
$$

という detector-conditioned distribution になる。$\eta_{AB}$ は completion efficiency である。この場合、Bell violation は detection loophole で説明され得る。

従って physical boundary model と postselection を区別する最低条件は、

- 全 launch、record、completion count を setting ごとに報告する。
- outcome-dependent missing fraction を零または独立に有界化する。
- terminal device の calibration を Bell run より前に固定する。
- timeout を変えても、predicted finite-width correction 以外の joint-law drift がないことを確かめる。

である。

## biased preparation test

seed preparation apparatus を追加し、基準 sector weight $w_{AB}$ を操作する。本文模型が arbitrary preparation に対して operationally viable なら、次のいずれかが観測されなければならない。

1. $w_{AB}$ の操作が boundary compatibility によって自動的に相殺される。
2. biased macrostate が物理的に準備不能になる。
3. no-signalling residual が増大する。

no-signalling residual を

$$
\epsilon_{\rm NS}
=
\max_{a,b,b',A}
\left|
P_R(A\mid a,b)
-P_R(A\mid a,b')
\right|
$$

とする。ideal `[S]` ensemble では $\epsilon_{\rm NS}=0$ である。biased preparation に対し $\epsilon_{\rm NS}=O(1)$ が現れれば、equilibrium-only model の操作的限界が直接検出される。

\begin{thebibliography}{99}

\addcontentsline{toc}{chapter}{参考文献}

\bibitem{bell1964} J. S. Bell, ``On the Einstein Podolsky Rosen Paradox,'' Physics Physique Fizika 1, 195--200 (1964). \url{https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195}

\bibitem{chsh1969} J. F. Clauser, M. A. Horne, A. Shimony, and R. A. Holt, ``Proposed Experiment to Test Local Hidden-Variable Theories,'' Physical Review Letters 23, 880--884 (1969). \url{https://doi.org/10.1103/PhysRevLett.23.880}

\bibitem{nelson1966} E. Nelson, ``Derivation of the Schrödinger Equation from Newtonian Mechanics,'' Physical Review 150, 1079--1085 (1966). \url{https://doi.org/10.1103/PhysRev.150.1079}

\bibitem{guerra_morato1983} F. Guerra and L. M. Morato, ``Quantization of Dynamical Systems and Stochastic Control Theory,'' Physical Review D 27, 1774--1786 (1983). \url{https://doi.org/10.1103/PhysRevD.27.1774}

\bibitem{yasue1981} K. Yasue, ``Stochastic Calculus of Variations,'' Journal of Functional Analysis 41, 327--340 (1981). \url{https://doi.org/10.1016/0022-1236(81)90079-3}

\bibitem{zambrini1986} J.-C. Zambrini, ``Stochastic Mechanics According to E. Schrödinger,'' Physical Review A 33, 1532--1548 (1986). \url{https://doi.org/10.1103/PhysRevA.33.1532}

\bibitem{wharton2010} K. B. Wharton, ``Time-Symmetric Boundary Conditions and Quantum Foundations,'' Symmetry 2, 272--283 (2010). \url{https://doi.org/10.3390/sym2010272}

\bibitem{wharton_argaman2020} K. B. Wharton and N. Argaman, ``Colloquium: Bell's Theorem and Locally Mediated Reformulations of Quantum Mechanics,'' Reviews of Modern Physics 92, 021002 (2020). \url{https://doi.org/10.1103/RevModPhys.92.021002}

\bibitem{hall2010} M. J. W. Hall, ``Local Deterministic Model of Singlet State Correlations Based on Relaxing Measurement Independence,'' Physical Review Letters 105, 250404 (2010). \url{https://doi.org/10.1103/PhysRevLett.105.250404}

\bibitem{leifer_pusey2017} M. S. Leifer and M. F. Pusey, ``Is a Time Symmetric Interpretation of Quantum Theory Possible without Retrocausality?,'' Proceedings of the Royal Society A 473, 20160607 (2017). \url{https://doi.org/10.1098/rspa.2016.0607}

\bibitem{wood_spekkens2015} C. J. Wood and R. W. Spekkens, ``The Lesson of Causal Discovery Algorithms for Quantum Correlations,'' New Journal of Physics 17, 033002 (2015). \url{https://doi.org/10.1088/1367-2630/17/3/033002}

\bibitem{ford1965} G. W. Ford, M. Kac, and P. Mazur, ``Statistical Mechanics of Assemblies of Coupled Oscillators,'' Journal of Mathematical Physics 6, 504--515 (1965). \url{https://doi.org/10.1063/1.1704304}

\bibitem{mori1965} H. Mori, ``Transport, Collective Motion, and Brownian Motion,'' Progress of Theoretical Physics 33, 423--455 (1965). \url{https://doi.org/10.1143/PTP.33.423}

\bibitem{zwanzig1973} R. Zwanzig, ``Nonlinear Generalized Langevin Equations,'' Journal of Statistical Physics 9, 215--220 (1973). \url{https://doi.org/10.1007/BF01008729}

\bibitem{jamison1974} B. Jamison, ``Reciprocal Processes,'' Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete 30, 65--86 (1974). \url{https://doi.org/10.1007/BF00532864}

\bibitem{doob1957} J. L. Doob, ``Conditional Brownian Motion and the Boundary Limits of Harmonic Functions,'' Bulletin de la Société Mathématique de France 85, 431--458 (1957). \url{https://doi.org/10.24033/bsmf.1495}

\bibitem{landauer1961} R. Landauer, ``Irreversibility and Heat Generation in the Computing Process,'' IBM Journal of Research and Development 5, 183--191 (1961). \url{https://doi.org/10.1147/rd.53.0183}

\bibitem{bennett1982} C. H. Bennett, ``The Thermodynamics of Computation: A Review,'' International Journal of Theoretical Physics 21, 905--940 (1982). \url{https://doi.org/10.1007/BF02084158}

\bibitem{uhlenbeck_ornstein1930} G. E. Uhlenbeck and L. S. Ornstein, ``On the Theory of the Brownian Motion,'' Physical Review 36, 823--841 (1930). \url{https://doi.org/10.1103/PhysRev.36.823}

\bibitem{wallstrom1994} T. C. Wallstrom, ``Inequivalence between the Schrödinger Equation and the Madelung Hydrodynamic Equations,'' Physical Review A 49, 1613--1617 (1994). \url{https://doi.org/10.1103/PhysRevA.49.1613}

\bibitem{price_wharton2023} H. Price and K. Wharton, ``Bell Correlations as Selection Artefacts,'' arXiv:2309.10969v3 (2024). \url{https://arxiv.org/abs/2309.10969}

\bibitem{price_wharton2024} H. Price and K. Wharton, ``A Mechanism for Entanglement?,'' arXiv:2406.04571v1 (2024). \url{https://arxiv.org/abs/2406.04571}

\bibitem{argaman2010} N. Argaman, ``Bell's Theorem and the Causal Arrow of Time,'' American Journal of Physics 78, 1007--1013 (2010). \url{https://doi.org/10.1119/1.3456564}

\bibitem{hossenfelder_palmer2020} S. Hossenfelder and T. Palmer, ``Rethinking Superdeterminism,'' Frontiers in Physics 8, 139 (2020). \url{https://doi.org/10.3389/fphy.2020.00139}

\bibitem{thooft2016} G. 't Hooft, The Cellular Automaton Interpretation of Quantum Mechanics, Springer (2016). \url{https://doi.org/10.1007/978-3-319-41285-6}

\bibitem{leonard2014} C. Léonard, ``A Survey of the Schrödinger Problem and Some of Its Connections with Optimal Transport,'' Discrete and Continuous Dynamical Systems A 34, 1533--1574 (2014). \url{https://doi.org/10.3934/dcds.2014.34.1533}

\bibitem{chen_georgiou_pavon2016} Y. Chen, T. T. Georgiou, and M. Pavon, ``On the Relation between Optimal Transport and Schrödinger Bridges: A Stochastic Control Viewpoint,'' Journal of Optimization Theory and Applications 169, 671--691 (2016). \url{https://doi.org/10.1007/s10957-015-0803-z}

\bibitem{rauch_tung_striebel1965} H. E. Rauch, F. Tung, and C. T. Striebel, ``Maximum Likelihood Estimates of Linear Dynamic Systems,'' AIAA Journal 3, 1445--1450 (1965). \url{https://doi.org/10.2514/3.3166}

\bibitem{waalkens_schubert_wiggins2008} H. Waalkens, R. Schubert, and S. Wiggins, ``Wigner's Dynamical Transition State Theory in Phase Space: Classical and Quantum,'' Nonlinearity 21, R1--R118 (2008). \url{https://doi.org/10.1088/0951-7715/21/1/R01}

\bibitem{kramers1940} H. A. Kramers, ``Brownian Motion in a Field of Force and the Diffusion Model of Chemical Reactions,'' Physica 7, 284--304 (1940). \url{https://doi.org/10.1016/S0031-8914(40)90098-2}

\bibitem{chandler1978} D. Chandler, ``Statistical Mechanics of Isomerization Dynamics in Liquids and the Transition State Approximation,'' Journal of Chemical Physics 68, 2959--2970 (1978). \url{https://doi.org/10.1063/1.436049}

\bibitem{sigman_whitt2019} K. Sigman and W. Whitt, ``Marked Point Processes in Discrete Time,'' Queueing Systems 92, 47--81 (2019). \url{https://doi.org/10.1007/s11134-019-09612-3}

\bibitem{fuchs_goldt_seifert2016} J. Fuchs, S. Goldt, and U. Seifert, ``Stochastic Thermodynamics of Resetting,'' Europhysics Letters 113, 60009 (2016). \url{https://doi.org/10.1209/0295-5075/113/60009}

\bibitem{evans_majumdar_schehr2020} M. R. Evans, S. N. Majumdar, and G. Schehr, ``Stochastic Resetting and Applications,'' Journal of Physics A: Mathematical and Theoretical 53, 193001 (2020). \url{https://doi.org/10.1088/1751-8121/ab7cfe}

\bibitem{knorst_lopes2024} J. Knorst and A. O. Lopes, ``On the Quantum Guerra--Morato Action Functional,'' Journal of Mathematical Physics 65, 082102 (2024). \url{https://doi.org/10.1063/5.0207422}

\bibitem{wilson_et_al2021} J. T. Wilson, V. Borovitskiy, A. Terenin, P. Mostowsky, and M. P. Deisenroth, ``Pathwise Conditioning of Gaussian Processes,'' Journal of Machine Learning Research 22, 1--47 (2021). \url{https://jmlr.org/papers/v22/20-1260.html}

\bibitem{leonard_roelly_zambrini2014} C. Léonard, S. Rœlly, and J.-C. Zambrini, ``Reciprocal Processes. A Measure-Theoretical Point of View,'' Probability Surveys 11, 237--269 (2014). \url{https://doi.org/10.1214/13-PS220}

\bibitem{fine1982} A. Fine, ``Hidden Variables, Joint Probability, and the Bell Inequalities,'' Physical Review Letters 48, 291--295 (1982). \url{https://doi.org/10.1103/PhysRevLett.48.291}

\bibitem{asmussen2003} S. Asmussen, Applied Probability and Queues, 2nd ed., Springer, New York (2003). \url{https://doi.org/10.1007/b97236}

\bibitem{marchiori_deaguiar2011} M. A. Marchiori and M. A. M. de Aguiar, ``Energy Dissipation Via Coupling With a Finite Chaotic Environment,'' Physical Review E 83, 061112 (2011). \url{https://doi.org/10.1103/PhysRevE.83.061112}

\end{thebibliography}
