@number: 1
@chapter: 本文
@title: 問題設定、二部構成、仮定の台帳
@status: Nelson 極限と Bell compatibility の論理的独立性を固定し、導出と境界原理を分離する。

## 1.1 問題設定

Bell の定理は、局所応答、結果の確定性、測定設定独立性などの仮定を同時に満たす理論が、量子力学の特定の相関を再現できないことを示す [1,2]。古典的な Hamiltonian 模型が Bell--CHSH 不等式を超える相関を与えるなら、Bell の前提のどこかが外れていなければならない。本論文はこの論理を回避せず、軌道法則、準備測度、終端条件、履歴確率を別々に監査する。

本論文では次の二つの問題を扱う。

1. 可逆な有限 Hamiltonian 系の Gaussian 縮約から、Nelson 型作用をどこまで定量的に得られるか。
2. 有限 Hamiltonian 測定器に時間対称な境界統計原理を加えたとき、setting-blind な終端条件の整合体積から Bell 型共同確率を構成できるか。

第1の問題には、第4章のパラメータ $C^1$ 収束定理として答える。第2の問題には、第7章の二モード台帳 Bell compatibility 定理として答える。ただし第2の定理は、Hamilton 方程式だけから全履歴測度を導く定理ではない。物理的試行測度を定める境界原理 `[R]` を明示的に入力する。

## 1.2 二部の論理的独立性

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

## 1.3 有限閉鎖測定窓

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

## 1.4 仮定の台帳

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

## 1.5 `[S]` と旧 equilibrium 仮定

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

## 1.6 一試行の物理的時系列

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

## 1.7 主要結果

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

## 1.8 先行研究との位置関係

Nelson の確率力学、確率変分法、Guerra--Morato 作用には確立した先行研究がある [3--6,35]。Gaussian 条件づけは固定区間平滑化、相反過程、Schrödinger bridge、経路単位の Gaussian conditioning と関係する [15,16,26--28,36,37]。第I部の新規性は、指定した線形 Gaussian クラスに対し、有限 Fourier 浴から繰り込み作用のパラメータ $C^1$ 極限を明示率付きで与える点に限定される。

時間対称境界条件、局所逆因果模型、measurement independence を緩めた Bell 模型には先行研究がある [7--11,21--25]。特に共通未来と境界制約による選別という発想自体は新規ではない。本論文の第II部が追加するのは、局所 pointer、実二次元差動比較器、固定総作用二モード台帳、setting-blind terminal coordinate を一つの有限 Hamiltonian network に接続し、旧共通入口密度を準備対称性と二モード位相体積へ分解する点である。

有限の非線形環境が中心振動子のエネルギー分散と実効熱化を起こし得ることは具体的な古典模型で調べられている [40]。ただし本論文は、その結果から任意初期密度の厳密一様化を推論しない。有限 Hamiltonian flow は fine-grained density を保存するため、mixing の使用範囲を粗視化時間頻度に限定する。

## 1.9 本論文が主張しないこと

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

## 1.10 論文の構成

第2章は有限2次 Hamiltonian と Fourier--Gaussian 表示、第3章は前後両側条件付き Gaussian 法則、第4章は定量的 Nelson 極限を扱う。第5章は有限 Hamiltonian 測定器、境界集団、相補時計による terminal half-space の正準実現、第6章は差動比較器と二モード台帳、第7章は terminal compatibility と Bell 統計、第8章は頑健性、反証条件、証明台帳を扱う。付録AとBは第I部の評価、付録Cは第II部の正準計算、相補時計の二境界 matching と向き平均 no-go、位相体積、付録Dは Gaussian Nelson 例を収録する。
