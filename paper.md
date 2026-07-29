# 概要


本論文は、有限個の正準自由度からなる可逆な古典 Hamiltonian 系を基盤として、2つの独立な問題を扱う。

1. 有限 Fourier--Gaussian 浴の縮約から、Nelson 型作用の形式をどこまで定量的に得られるか。
2. 有限 Hamiltonian 装置と2境界統計原理を組み合わせたとき、Bell 型共同確率をどこまで明示的に構成できるか。

第I部では、有限分解能の前後記録で条件づけた線形 Gaussian 経路法則を考える。時間刻み $h$ の繰り込み済み粗視化作用を $\mathcal A_{N,h}^{R,U}$ とすると、滑らかな有限次元パラメータ集合 $K$ 上で

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

を得る。$h_N=TN^{-1/3}$ なら誤差は $O(N^{-1/3})$ である。極限作用は正の Gaussian 密度領域で Guerra--Morato 表示と Nelson 表示を持つ。

この定理が示すのは、定義した粗視化作用とその有限次元パラメータ微分の収束である。微視的 Hamiltonian 運動が粗視化作用の停留点を選択すること、任意の Nelson 変分を有限浴が実現すること、または量子力学の有効力学全体が出現することまでは示さない。証明に用いる時間依存線形 Gaussian 方程式も確率計算用の表示であり、その全てを1つの有限自律 Hamiltonian へ埋め込む定理は本論文に含まれない。

第II部は第I部の Nelson 極限から Bell 重みを導かない。局所装置は結果符号を固定指針へ記録し、設定と符号を担う2つの実正準ベクトルを記録後の共通未来へ送る。比較器が計算する差動作用は

```math
\overline I_-^{AB}
=
I_0
\left[
1-ABV\cos\Delta_{ab}
\right]
```

である。余弦は確率公理ではなく、2つの実2次元ベクトルの内積から生じる。

比較器の未読変数には、1つのソフトモードと1つの残余作用モードを用いる。固定総作用殻

```math
E_\ell
=
\omega_\ell(J_s+J_0)
```

上の正規化 Liouville 測度では、ソフトモードのエネルギー $h=\omega_\ell J_s$ は

```math
p(h)
=
\frac1{E_\ell},
\qquad
0\leq h\leq E_\ell
```

という一様周辺密度を持つ。これは2モード位相体積の厳密な結果である。任意の微視的初期密度が Hamiltonian 発展によってこの密度へ強収束するとは主張しない。動的な典型化を用いる場合には、有限分解能での混合と時間尺度分離を追加で仮定する。

4つの結果領域の基準質量は、固定総作用殻の幾何だけでは決まらない。準備 Hamiltonian、準備巨視領域、基準 Liouville 測度が左右の符号反転に不変であるという `[S]` の下でのみ、

```math
w_{++}
=
w_{+-}
=
w_{-+}
=
w_{--}
=
\frac14
```

が従う。

終端読出しには、2つの内部時計の相対運動量 $\Pi_R$ を用いる。比較窓の生成子を

```math
K_R
=
Y_R
\left(
h-\kappa I_-
\right)
```

と取ると、内部時計の自由 Hamiltonian により $Y_R$ が動いても、$h$ と $I_-$ は保存される。規格化した比較パルスの後には厳密に

```math
\Pi_R(T)
=
E_*+\kappa I_- -h
```

を得る。従って、相補的時計領域 $P_c=0$ では

```math
\Pi_R(T)\geq0
```

が、初期に選んだ時計向きの順序を終端まで保つ条件と一致する。この修正により、比較パルス中に $Y_R=0$ が保たれるという仮定は不要になる。

一方、Hamilton 方程式は $\Pi_R(T)<0$ の軌道も許す。したがって相補的時計が与えるのは終端半空間の力学的意味であり、その半空間に入る履歴だけを物理的確率集団とする原理ではない。本論文では、基準初期密度 $\rho_S$ と全設定に共通な終端関数 $G_R$ から

```math
d\mu_R^{a,b}(z_i)
=
\frac{
\rho_S(z_i)
G_R\!\left(\Phi_{a,b}^{T}z_i\right)
}{
Z_{a,b}
}
d\Gamma_i
```

を定める追加原理を `[R]` と呼ぶ。これは「2境界統計原理」であり、時間反転共変な完成モデルが得られたことを意味しない。

適用範囲

```math
0
\leq
E_*+\kappa\overline I_-^{AB}
\leq
E_\ell
```

と `[H,P,S,M,R]` の下では、

```math
P_R(A,B\mid a,b)
=
\frac14
\left[
1-ABV_{\rm eff}\cos\Delta_{ab}
\right],
```

```math
V_{\rm eff}
=
\frac{\kappa I_0}{E_*+\kappa I_0}V
```

を得る。規格化因子は測定設定に依存せず、`[S]` の対称集団では非信号性が成り立つ。ただし、完全な微視状態の事後分布は一般に測定設定へ依存する。Bell の前提違反は測定設定独立性に現れ、Bell の定理を否定しない。

第II部の局所装置は、結果符号を記録する最小モデルである。現在の明示モデルでは $A=\sigma(s_A)$、$B=\sigma(s_B)$ と置いており、設定と到来信号から結果を生成する一般の測定相互作用までは構成していない。また、一般の局所パルスは自由運動との同時発展を含む短時間極限でのみ所望の正準写像へ近づく。比較読出しの式だけは、上の交換関係により有限幅パルスでも厳密である。

本論文が確立する内容と限界を次にまとめる。

| 項目 | 到達点 |
|---|---|
| 第I部 | 線形 Gaussian・有限分解能・2次ポテンシャルの範囲で、粗視化作用形式のパラメータ $C^1$ 収束を証明 |
| 局所装置 | 有限 Hamiltonian 部品による最小結果符号化モデル。一般測定相互作用は未構成 |
| 比較器 | $Y_R$ の自由運動を含めても $\Pi_R(T)=E_*+\kappa I_- -h$ を厳密に読出し |
| 2モード作用分配系 | 固定総作用殻の Liouville 測度について $p(h)=1/E_\ell$ を厳密に導出 |
| Bell 型共同確率 | `[H,P,S,M,R]` と適用範囲の下で成立 |
| `[R]` | Hamilton 方程式からは未導出。2境界照合を置けば積形式を得る |
| 非信号性 | 対称準備 `[S]` の下で成立。任意の偏った準備では未証明 |
| Born 則、Tsirelson 限界、Wallstrom 問題 | 力学的な一意導出には未達 |

本文は、物理的な入力、相互作用、保存量、出力、仮定を中心に述べる。長い正準計算、収束評価、2境界照合、測定設定依存度、数値検証手順は付録と `VALIDATION.md` に分けて置く。

# 問題設定、2部構成、仮定一覧

> **位置づけ：** Nelson 作用極限と Bell 型共同確率の論理的独立性を固定し、力学、準備測度、2境界統計原理を分離する。


## 問題設定

Bell の定理は、局所応答、結果の確定性、測定設定独立性などを同時に満たす理論が、特定の Bell--CHSH 相関を再現できないことを示す [1,2]。古典 Hamiltonian モデルが Bell--CHSH 不等式を超える相関を与えるなら、Bell の前提の少なくとも1つが成立していない。本論文はこの論理を回避せず、軌道法則、準備測度、終端条件、履歴確率を個別に監査する。

扱う問題は次の2つである。

1. 可逆な有限 Hamiltonian 系の Gaussian 縮約から、Nelson 型作用の形式をどこまで定量的に得られるか。
2. 有限 Hamiltonian 装置に2境界統計原理を加えたとき、設定名や結果名を直接参照しない終端条件の整合体積から Bell 型共同確率を構成できるか。

第1の問題には、第4章のパラメータ $C^1$ 収束定理として答える。第2の問題には、第7章の2モード作用分配系の定理として条件付きで答える。ただし第2の定理は、Hamilton 方程式だけから全履歴測度を導く定理ではない。物理的試行測度を定める `[R]` を明示的に入力する。

## 2部の論理的独立性

第I部は、有限 Fourier--Gaussian 浴、有限分解能の前後記録、繰り込み済み作用を扱う。中心結果は、作用値と指定した有限次元パラメータ方向の第1変分が Guerra--Morato 型 Nelson 作用へ収束するという定量的定理である。

第II部は、局所分析器、確定指針、共通未来の比較器、2モード作用分配系、終端整合性を扱う。第I部の Nelson 極限は Bell 重みを生成しない。両者に共通するのは、有限 Hamiltonian 系を出発点にしても、局所経路法則と全履歴の統計法則を同一視してはならないという方法論である。

したがって、「有限 Hamiltonian 中核から Nelson 作用形式へ進む論理鎖」と、「有限 Hamiltonian 装置に2境界統計原理を加えて Bell 型統計へ進む論理鎖」は別である。第I部だけを用いる読者は第4章で完結でき、第II部だけを検討する読者は `[R]` と準備条件を独立に監査できる。

## 有限閉鎖測定窓

1試行の測定窓では、生成源、設定制御器、局所装置、伝達ベクトル、比較器、作用分配系、時計、有限浴からなる有限正準系を用いる。位相点を $z$、標準シンプレクティック行列を $J$ と書けば、

```math
\dot z
=
J\nabla H_{\rm tot}(z)
```

である。各構成部品は滑らかな Hamiltonian 生成子を持ち、位相体積を保存する。操作順序は自律時計によって設定できる。

ただし本論文が明示するのは、測定窓を構成する正準写像と比較窓の Hamiltonian である。生成源、設定制御器、全自由発展、有限幅の全パルスを1本にまとめ、所望の写像を有限時間で誤差なく実行する完全な実験 Hamiltonian までは与えない。一般の局所パルスは短時間極限で所望の写像へ収束し、その誤差評価を付録Cに示す。第7章の比較読出しは、保存量との交換関係により有限幅でも厳密である。

有限閉鎖系には真のアトラクターも永久記録もない。局所記録が実用的に安定であるという主張は、

```math
\tau_{\rm meas}
\ll
\tau_{\rm record}
\ll
T_{\rm rec}
```

という有限時間窓に限定する。$\tau_{\rm meas}$ は記録形成時間、$\tau_{\rm record}$ は必要な保持時間、$T_{\rm rec}$ は装置を含む有限系の再帰尺度である。

同一装置で無限回の試行を行うには、仕事貯蔵系、記録消去、浴の再生を含む大きな周期を別に指定する必要がある。本論文は1試行の完結履歴測度を扱い、開いた実験室での無限回リセットを確率生成機構として用いない。

## 仮定一覧

第II部の仮定を次の5つに分ける。

### [H] 有限 Hamiltonian 部品

生成源、設定制御器、局所記録器、有限浴、共通未来の比較器、2モード作用分配系、相補的内部時計、パルス順序時計を有限個の正準対と滑らかな Hamiltonian 生成子で記述する。異なる測定設定と結果に別の Hamiltonian 関数を割り当てず、設定は制御器の初期巨視領域、結果は局所変数と指針領域で表す。

現在の局所モデルは、あらかじめ存在する2値の結果種を指針へ写す最小結果符号化モデルである。一般の

```math
A=\mathscr A(a,\lambda_A),
\qquad
B=\mathscr B(b,\lambda_B)
```

を到来信号との相互作用から実現する装置は、`[H]` に含めて仮定できるが、本論文では具体的に構成しない。

### [P] 位相同期した生成源

左右へ送る2つの実2次元伝達ベクトルは、共通の位相基準と同じ基準作用を持つ。有限の振幅不一致と相対位相雑音は可視度 $V$ に含める。この条件は第I部の Gaussian 浴だけから導出されない。

### [S] 対称な基準準備

`[R]` を適用する前の準備 Hamiltonian、準備巨視領域、基準 Liouville 測度は、左右の結果種を独立に反転する2つの変換に不変である。4つの結果領域が1つの軌道に沿って相互遷移する必要はない。必要なのは、基準測度に関して4領域が同じ体積を持つことである。

### [M] 2モード作用分配系の入口測度

ソフトモードと残余作用モードは比較時刻に固定総作用殻

```math
J_s+J_0
=
\frac{E_\ell}{\omega_\ell}
```

上の正規化 Liouville 測度を持つ。これを直接の準備条件として用いる場合、ソフトモードのエネルギー密度は厳密に一様である。有限非線形混合器による典型化を用いる場合は、任意の微視的初期密度の強収束ではなく、有限分解能観測に対する粗視化混合を要求する。

### [R] 2境界統計原理

基準初期密度 $\rho_S$ と全設定に共通な終端関数 $G_R\geq0$ に対し、物理的履歴測度を

```math
d\mu_R^{a,b}(z_i)
=
\frac{
\rho_S(z_i)
G_R\!\left(\Phi_{a,b}^{T}z_i\right)
}{
Z_{a,b}
}
d\Gamma_i
```

とする。$G_R$ は設定名、結果名、目標相関を引数に持たない。`[R]` は有限性、再帰性、時間反転対称性から一意に導かれるとは主張しない。相補的内部時計は

```math
G_R
=
\mathbf1_{\{\Pi_R\geq0\}}
```

という半空間へ時計向き保存の意味を与えるが、その半空間だけを物理的集団として数える原理は与えない。

## 準備対称性と2モード幾何の分離

旧構成では、4つの結果領域に共通な絶対入口密度を1つの条件として置いていた。本論文ではこれを次の2つに分解する。

1. 各結果領域の中でソフトモードのエネルギーが一様であることは、固定総作用を持つ2モード作用分配系の Liouville 幾何から導く。
2. 4つの結果領域の基準質量が等しいことは、準備測度の独立符号反転対称性から導く。

したがって

```math
g_{AB}^{\rm ent}(h)
=
\frac{w_{AB}}{E_\ell}
```

のうち、$1/E_\ell$ は2モード定理、$w_{AB}=1/4$ は `[S]` の帰結である。Hamiltonian の形だけでは初期密度を決められないため、準備測度という統計条件は残る。

## 1試行の物理的時系列

1試行を次の10段階に分ける。

1. 位相同期した伝達ベクトル対と局所結果種を準備する。
2. 左右の制御器巨視状態により設定 $a,b$ を選ぶ。
3. 局所分析器が伝達ベクトルを回転し、結果符号 $A,B$ を応答モードへ写す。
4. 固定指針が結果符号を記録する。
5. 局所有限浴が応答モードの一時情報を分散する。
6. 記録の写しと伝達ベクトルを通常の時間順序で共通未来へ運ぶ。
7. 比較器が差動作用 $I_-$ を計算する。
8. 初期相対時計運動量を $\Pi_R=E_*$ とし、ソフトモードエネルギー $h$ と差動作用 $\kappa I_-$ を比較する。
9. 終端相対時計運動量 $\Pi_R(T)=E_*+\kappa I_- -h$ に固定終端領域を課す。
10. `[R]` により終端整合履歴の規格化測度を物理的試行集団とする。

左と右は局所記録が形成される前には共通浴を持たない。共通未来の相互作用は、すでに確定した記録の写しを処理する。このため Bell 相関を「共有浴雑音が左右へ順時間的に漏れた結果」とは解釈しない。

## 主要結果

第I部では、有限 Fourier--Gaussian 条件付き作用が Nelson 作用形式へ収束することを、指定した線形 Gaussian パラメータ族について定量化する。これは作用形式の収束であり、微視的力学による停留点選択の導出ではない。

第II部では、次を示す。

- 実2次元比較器の差動作用に対する余弦恒等式。
- 固定総作用を持つ2モード作用分配系の一様なソフトモードエネルギー周辺定理。
- 対称準備から $w_{AB}=1/4$ を得る等体積命題。
- 内部時計の自由運動を含めた比較読出しの厳密式。
- 相補的内部時計による終端半空間の正準実現。
- `[H,P,S,M,R]` の下での Bell 型共同確率。
- 測定設定独立性、測定設定頻度、非信号性、CHSH 値の監査。
- 順時間的共有浴、滞在時間、多モード作用分配系では同じ重みを代替できないという否定結果。

## 先行研究との位置関係

Nelson の確率力学、確率変分法、Guerra--Morato 作用には先行研究がある [3--6,35]。Gaussian 条件づけは固定区間平滑化、相反過程、Schrödinger 橋、経路単位の Gaussian 条件づけと関係する [15,16,26--28,36,37]。第I部の新規性は、指定した線形 Gaussian クラスに対し、有限 Fourier 浴から繰り込み作用のパラメータ $C^1$ 極限を明示率付きで与える点に限定される。

2境界条件、局所逆因果モデル、測定設定独立性を緩めた Bell モデルにも先行研究がある [7--11,21--25]。共通未来と境界制約による選別という発想自体は新規ではない。第II部が追加するのは、局所指針、実2次元差動比較器、固定総作用をもつ2モード作用分配系、設定名を直接参照しない終端座標を有限 Hamiltonian 部品として接続し、旧共通入口密度を準備対称性と2モード位相体積へ分解する点である。

## 本論文が主張しないこと

本論文は次を主張しない。

- Bell の全仮定を保った古典モデルによる Bell 不等式の破れ。
- `[R]` が有限 Hamiltonian 力学または相補的時計運動量だけから必然的に導かれること。
- 局所装置が一般の設定依存結果を到来信号から生成する完全な測定モデルであること。
- 全装置部品を1本に統合した有限幅 Hamiltonian が、全ての理想正準写像を誤差なく実行すること。
- 作用分配系の任意の初期分布が厳密に一様密度へ収束すること。
- 任意の偏った準備に対する非信号性。
- 余弦則または Tsirelson 限界が追加原理から一意に選ばれること。
- Bell 型共同確率が Wallstrom 問題を解くこと。
- 第I部の作用収束が微視的な停留点選択または量子力学全体を導くこと。

## 論文の構成

第2章から第4章は、可逆な調和 Hamiltonian 中核、Gaussian 条件づけ、作用形式の定量的 Nelson 極限を扱う。第5章から第7章は、有限 Hamiltonian 装置部品、2モード作用分配系、2境界統計原理の下での Bell 型共同確率を扱う。第8章は適用範囲、否定結果、反証条件をまとめる。長い収束評価、正準計算、2境界照合、測定設定依存度、数値検証手順は付録と `VALIDATION.md` に置く。

# 第I部　有限調和 Gaussian 中核の Nelson 極限

# 可逆な調和 Hamiltonian 中核と有限 Gaussian 確率表示

> **位置づけ：** 微視的可逆性と、証明に用いる補助的な線形 Gaussian 確率表示の範囲を分離する。


## 有限2次 Hamiltonian

位相空間を $\mathbb{R}^{2M}$、正準座標を $Z=(Q,P)$ とし、

```math
H_N(Z)=\frac12 Z^{\mathsf T}G_N Z,
\qquad
G_N=G_N^{\mathsf T}>0
```

を考える。運動方程式は

```math
\dot Z=JG_NZ,
\qquad
Z(t)=e^{tJG_N}Z(0)
```

である。$G_N$ が運動量に関して偶であれば、標準時間反転 $\Theta(Q,P)=(Q,-P)$ に対して

```math
\Theta e^{tJG_N}\Theta=e^{-tJG_N}
```

が成立する。従って全微視軌道は時間反転対称であり、Liouville 体積を保存する。

正準変換で正規モードへ移れば、安定な部分は

```math
H_N
=
\sum_{n=1}^{N}
\frac12
\left(
P_n^2+\omega_n^2Q_n^2
\right)
```

の形にできる。初期正準変数が中心 Gaussian 分布を持つなら、任意の線形観測量

```math
X_N(t)=L e^{tJG_N}Z(0)+\mu_N(t)
```

は有限次元 Gaussian 過程である。従って、閉じた調和 Hamiltonian 系の観測座標は、平均と2時刻共分散だけで完全に記述できる。

## 反作用を含む標準的な調和浴

粒子座標 $q$ と調和浴を明示する代表例は

```math
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
```

である [12--14]。平方完成された結合は反作用と周波数補正を同時に含む。浴変数を厳密に消去すると、粒子は有限記憶核を持つ一般化 Langevin 方程式に従う。

```math
m\ddot q(t)
+V'(q(t))
+\int_0^t\Gamma_N(t-s)\dot q(s)\,\mathrm{d} s
=
\xi_N(t)+F_{\rm slip}(t).
```

ここで

```math
\Gamma_N(t)
=
\sum_{n=1}^{N}
\frac{c_n^2}{m_n\omega_n^2}
\cos\omega_nt
```

であり、$\xi_N$ は浴初期座標の線形結合である。浴初期分布が Gaussian なら $\xi_N$ も有限 Gaussian 過程になる。有限 $N$ では記憶核も雑音も再帰的であり、白色雑音や散逸は微視的な基本法則ではない。

本論文の $C^1$ 定理は、この一般化 Langevin 方程式を任意の非線形 $V$ について直接扱うものではない。調和領域または線形化領域で観測される Gaussian 経路法則を、次節の有限 Fourier 表示で計算する。したがって、閉じた Hamiltonian 中核は微視的な可逆性を支え、線形 Gaussian モデルはその観測法則を計算する簡略表示である。

## 完全な有限 Fourier 浴

時間区間を $[0,T]$、$\omega_n=2\pi n/T$ とする。独立な標準 Gaussian ベクトル $Z_0,A_n,B_n\in\mathbb{R}^d$ を用いて

```math
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
```

と定義する。この過程は調和正規モードの初期振幅を読み出すことで実現できる。零周波数 $Z_0$ は保存された正準運動量または自由モードに対応する。

共分散は

```math
\mathbb{E}\left[
\widetilde\eta_N^i(t)
\widetilde\eta_N^j(s)
\right]
=
2\nu\,\delta^{ij}\delta_{T,N}(t-s),
```

```math
\delta_{T,N}(\tau)
=
\frac1T
+
\frac2T
\sum_{n=1}^{N}\cos\omega_n\tau
```

である。$\delta_{T,N}$ は周期 Dirichlet 核であり、滑らかな試験関数に対して周期デルタ分布へ収束する。

零周波数を最初から除いた

```math
2\nu
\left[
\delta_{T,N}(t-s)-\frac1T
\right]
```

を普遍的な浴共分散とみなしてはならない。これは全ての線形系に共通な浴ではなく、自由増分の全期間積分を零にする条件を課したときに現れる特殊な条件付き共分散である。一般の線形な流れでは、終端条件による共分散修正は流れと観測行列に依存する Schur 補完になる。

## 証明用の線形 Gaussian 確率表示

実際の証明では、観測座標の確率法則を

```math
\dot X_N(t)
=
F_\theta(t)X_N(t)
+f_\theta(t)
+\widetilde\eta_N(t),
\qquad
X_N(0)\sim N(m_{0,\theta},P_{0,\theta})
```

で表す。$\theta$ は質量、周波数、外力、終端記録などをまとめた有限次元パラメータである。$F_\theta$ と $f_\theta$ は時間について十分滑らかとする。

基本行列 $\Phi_\theta(t,s)$ を

```math
\partial_t\Phi_\theta(t,s)
=
F_\theta(t)\Phi_\theta(t,s),
\qquad
\Phi_\theta(s,s)=I
```

で定めると、

```math
X_N(t)
=
\Phi_\theta(t,0)X_N(0)
+\int_0^t
\Phi_\theta(t,s)
\left[
f_\theta(s)+\widetilde\eta_N(s)
\right]
\,\mathrm{d} s
```

である。従って $X_N$ は有限個の Gaussian 変数の線形像であり、平均 $\mu_N$ と共分散 $C_N$ を有限和として厳密に計算できる。

この方程式は、有限 $N$ の平均と共分散を計算するための補助的な確率表示である。$\widetilde\eta_N$ 自体は有限 Hamiltonian 正規モードの初期振幅から作れるが、任意の時間依存係数 $F_\theta(t)$、$f_\theta(t)$ を含む上式全体が、1つの有限自律 Hamiltonian の観測座標として実現されることまでは示さない。

したがって、第4章の定理が直接扱うのはこの線形 Gaussian 確率表示のクラスである。特定の有限 Hamiltonian モデルと平均・共分散が一致する場合には同じ作用計算を移せるが、一般の時間依存線形系に対する Hamiltonian 埋め込みを定理の結論へ含めない。この区別により、「有限 Hamiltonian 中核の存在」と「証明に用いる全確率表示の Hamiltonian 実現」を混同しない。

## 極限拡散

$N\to\infty$ で積分雑音

```math
W_N(t)=\int_0^t\widetilde\eta_N(s)\,\mathrm{d} s
```

は、有限次元分布で共分散 $2\nu\min(s,t)$ を持つ Wiener 増分へ近づく。本論文の作用とパラメータ第1微分は2時刻の平均・共分散だけで評価するため、一般の経路空間位相における弱収束は主定理の仮定にも結論にも用いない。対応する線形拡散表示は

```math
\,\mathrm{d} X(t)
=
\left[
F_\theta(t)X(t)+f_\theta(t)
\right]\,\mathrm{d} t
+\sqrt{2\nu}\,\,\mathrm{d} W_t
```

である。有限 $N$ の各経路は微分可能であるが、極限経路は微分不可能である。粗視化作用に現れる発散は、この正則性の変化に由来する。

## OU モデルと Stratonovich 表現

$F=-\lambda I+\Omega J$ と選べば、2次元の回転を伴う OU 位相モデルが得られる。これは減衰する位相振幅を扱う便利な具体例である。しかし OU の摩擦は縮約後の有効係数であり、微視的 Hamiltonian 中核そのものが時間反転を破ることを意味しない。本論文では OU モデルを基礎仮定とせず、付録Dの例として用いる。

雑音係数が状態に依存しないため、Itô 表現と Stratonovich 表現の変換補正は零である。従って、どちらの記法を選んでも本論文の線形 Gaussian 定理は変わらない。Stratonovich 微分は中心論証に必要ないため、以後は Itô 表現に統一する。

## 本章の結論

有限調和 Hamiltonian 系は、微視的可逆性と有限 Gaussian 経路法則を同時に与える。実際の証明には補助的な線形 Gaussian 確率表示を用いるが、その一般形を有限自律 Hamiltonian へ埋め込んだとは主張しない。白色拡散は有限モードの特異極限であり、終端条件は浴そのものではなく Gaussian 条件づけとして導入する。次章では、その条件づけを有限 $N$ と極限拡散の双方で記述する。

# 前後両側から条件づけた線形 Gaussian 経路法則

> **位置づけ：** 有限分解能の終端記録を Gaussian Schur 補完として厳密に定義する。


## なぜ有限分解能を用いるか

前章の $X_N$ に対し、初期側では Gaussian 準備分布を与え、終端側では測定装置が残す有限分解能の記録を条件として用いる。終端位置をデルタ関数で厳密固定すると、極限拡散の終端近傍で流れが特異になり、$C^1$ 評価に不要な境界層が生じる。実在する測定記録は有限分解能を持つため、本論文では正定値の読み出し雑音を含む条件づけを主定理に採用する。

時刻 $T$ の記録を

```math
Y=HX_N(T)+\varepsilon,
\qquad
\varepsilon\sim N(0,R),
\qquad
R\geq r_*I>0
```

とする。実際に得られた記録値を $y$ とする。この条件は、尤度

```math
L_R(x)
=
\exp\left[
-\frac12(Hx-y)^{\mathsf T}R^{-1}(Hx-y)
\right]
```

で経路を重みづけすることと同値である。

## 無条件 Gaussian 法則

有限 $N$ の平均と2時刻共分散を

```math
\mu_N(t)=\mathbb{E}[X_N(t)],
```

```math
C_N(s,t)
=
\mathbb{E}\left[
(X_N(s)-\mu_N(s))
(X_N(t)-\mu_N(t))^{\mathsf T}
\right]
```

とする。基本行列を使えば、平均は

```math
\mu_N(t)
=
\Phi(t,0)m_0
+\int_0^t\Phi(t,r)f(r)\,\mathrm{d} r
```

であり、共分散は初期共分散と有限 Fourier モードの寄与の和として書ける。

雑音を基底関数 $e_\alpha(t)$ と独立 Gaussian 係数 $\zeta_\alpha$ で

```math
\widetilde\eta_N(t)
=
\sum_{\alpha=0}^{2N}e_\alpha(t)\zeta_\alpha
```

と書けば、

```math
K_{N,\alpha}(t)
=
\int_0^t\Phi(t,r)e_\alpha(r)\,\mathrm{d} r
```

により

```math
C_N(s,t)
=
\Phi(s,0)P_0\Phi(t,0)^{\mathsf T}
+\sum_{\alpha=0}^{2N}
K_{N,\alpha}(s)K_{N,\alpha}(t)^{\mathsf T}
```

となる。この表示は、条件づけとパラメータ微分を有限行列計算へ帰着させる。

## Schur 補完による条件付き平均と共分散

記録共分散を

```math
S_N
=
HC_N(T,T)H^{\mathsf T}+R
```

とする。$R\geq r_*I$ なので $S_N$ は一様に可逆である。

<!-- theorem-start:proposition -->
**命題（有限 Gaussian 条件づけ）**
条件 $Y=y$ の下で $X_N$ は Gaussian 過程のままであり、その平均と共分散は

```math
\mu_N^R(t)
=
\mu_N(t)
+C_N(t,T)H^{\mathsf T}S_N^{-1}
\left[y-H\mu_N(T)\right],
```

```math
C_N^R(s,t)
=
C_N(s,t)
-C_N(s,T)H^{\mathsf T}S_N^{-1}HC_N(T,t)
```

である。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
有限個の時刻 $t_1,\ldots,t_k$ を固定すると、$(X_N(t_1),\ldots,X_N(t_k),Y)$ は結合 Gaussian ベクトルである。結合共分散行列の $Y$ 成分に関する Schur 補完を取れば上式を得る。任意の有限時刻集合で整合するため、条件付き過程全体が定まる。
<!-- theorem-end:proof -->

条件付き共分散の第2項は、終端記録により減少した不確かさを表す。これは力ではない。ある経路が終端記録とどれだけ整合するかという統計的更新である。

この計算は、新しい種類の Gaussian 条件づけではない。有限次元の状態を拡大して Fourier 係数まで含めれば、固定区間の線形 Gaussian 平滑化と同じ Schur 補完になる [28]。経路測度の立場では相反過程および Schrödinger 橋の線形 Gaussian 部分に属し [15,26,27,37]、経路単位の Gaussian 条件づけとしても標準的に表せる [36]。本論文で必要なのは、この既知の条件づけを有限 Fourier 切断数 $N$ とパラメータ $\theta$ について一様に微分し、第4章の定量的 $C^1$ 評価へ接続することである。

## パラメータ微分

$F_\theta$ の変分 $\delta F$ に対して基本行列の第1変分は

```math
D\Phi_\theta[\delta F](t,s)
=
\int_s^t
\Phi_\theta(t,r)
\delta F(r)
\Phi_\theta(r,s)
\,\mathrm{d} r
```

である。逆行列の微分

```math
D(S^{-1})[\delta S]
=
-S^{-1}(\delta S)S^{-1}
```

と合わせると、$\mu_N^R$、$C_N^R$ のパラメータ第1微分を明示できる。$S_N\geq r_*I$ により、条件づけの微分は $N$ に依存しない定数で制御される。

有限分解能 $R>0$ は、物理的に自然であるだけでなく、数学的にも重要である。$R=0$ で $H$ が全座標を固定すると、終端に近づくにつれて条件付き流れが $(T-t)^{-1}$ 型に発散し得る。点終端は $R\downarrow0$ の別極限として扱うべきであり、主定理には含めない。

## 極限拡散の条件付き流れ

$N\to\infty$ の無条件拡散を

```math
\,\mathrm{d} X_t=b(X_t,t)\,\mathrm{d} t+\sqrt{2\nu}\,\,\mathrm{d} W_t,
\qquad
b(x,t)=F(t)x+f(t)
```

とする。終端尤度の後方伝播を

```math
h_R(x,t)
=
\mathbb{E}\left[L_R(X_T)\mid X_t=x\right]
```

と置く。線形 Gaussian 系では $h_R$ は指数2次関数で正である。条件付き前進流れは Doob 変換により

```math
b_+^R(x,t)
=
b(x,t)+2\nu\nabla\log h_R(x,t)
```

となる [15,16]。$\nabla\log h_R$ は $x$ の1次式であるため、条件付き過程も線形 Gaussian である。

条件付き時刻密度を $\rho^R(x,t)$ とすると、後退流れは

```math
b_-^R(x,t)
=
b_+^R(x,t)-2\nu\nabla\log\rho^R(x,t)
```

である。そこで

```math
v^R
=
\frac{b_+^R+b_-^R}{2},
\qquad
u^R
=
\frac{b_+^R-b_-^R}{2}
=
\nu\nabla\log\rho^R
```

と定義する。$v^R$ は確率流の速度、$u^R$ は密度勾配に伴う浸透速度である。

## 自由系で現れる −1/<i>T</i>

$F=0$、$f=0$、$X_N(0)=x_0$ とし、終端を厳密に $X_N(T)=x_0$ へ固定する特殊な場合を考える。非零 Fourier モードは1周期積分すると零になるため、全期間変位を担うのは零周波数 $Z_0$ だけである。終端条件は $Z_0=0$ を意味する。従って条件付き雑音共分散は

```math
\mathbb{E}\left[
\widetilde\eta_N(t)
\widetilde\eta_N(s)^{\mathsf T}
\mid X_N(T)=x_0
\right]
=
2\nu
\left[
\delta_{T,N}(t-s)-\frac1T
\right]I.
```

ここで初めて $-1/T$ が現れる。一般の $F\neq0$ では終端値は全 Fourier モードの線形結合に依存するため、条件付き修正は

```math
-\operatorname{Cov}(\widetilde\eta_N,Y)
\operatorname{Cov}(Y,Y)^{-1}
\operatorname{Cov}(Y,\widetilde\eta_N)
```

という流れ依存の Schur 補完であり、単純な $-1/T$ ではない。

## 前後両側条件づけの物理的意味

初期準備と終端記録の双方を知った後に、途中経路の統計を求めることは、通常の条件付き確率である。終端記録が途中経路の条件付き平均を変えることは、終端装置が過去へ力を送ることを意味しない。

ただし、条件付き経路分布を物理的試行頻度として採用するには、どの完結履歴へ確率を置くかという追加の物理原理が必要である。Gaussian Schur 補完は、記録を与えた後の条件付き法則を計算するが、その法則が実験の無条件頻度として選ばれることまでは証明しない。第II部ではこの役割を2境界統計原理 `[R]` として明示し、第4章の Nelson 作用極限からは導かない。

## 本章の結論

有限分解能の終端記録を用いれば、前後両側から条件づけた経路法則は通常の Gaussian Schur 補完として完全に定義できる。条件付き平均、共分散、そのパラメータ微分は一様に制御される。次章では、この安定性を用いて、有限浴の繰り込み済み作用とその第1変分を Nelson 極限へ移す。

# 繰り込み済み粗視化作用形式の Nelson 極限

> **位置づけ：** 線形 Gaussian・有限分解能・2次ポテンシャルの範囲で、定義した作用形式の定量的 $C^1$ 収束を示す。


## 粗視化作用

有限 $N$ の経路は微分可能であるが、$N\to\infty$ の拡散経路は微分不可能である。そのため、単純な運動エネルギー

```math
\frac m2\int_0^T|\dot X_N(t)|^2\,\mathrm{d} t
```

は極限で発散する。時間分解能 $h>0$ を固定し、有限差分

```math
D_hX_N(t)=\frac{X_N(t+h)-X_N(t)}{h}
```

を用いる。拡散係数が $\nu$、空間次元が $d$ なら、雑音の普遍的発散は

```math
\frac m2\mathbb{E}|D_hX|^2
\sim
\frac{md\nu}{h}
```

である。

差分商の運動項から軌道に依存しない発散定数を除き、有限な Guerra--Morato 項を残す原理自体は既知である [3,4]。本章の新規な主張は、有限 Fourier 切断、有限分解能の終端記録、滑らかな有限次元パラメータ族を同時に扱い、作用値とその第1偏微分へ共通の明示誤差評価を与える点にある。

ここで扱う粗視化作用は、有限 Hamiltonian 軌道の統計から定義する評価汎関数である。Hamilton 方程式そのものから、この汎関数を最小化または停留化する選択則が生じるとは仮定しない。本章の結論は作用形式の収束であり、有効運動方程式の動力学的選択まで含まない。

外部ポテンシャルを $U_\theta(x,t)$ と書き、条件付き経路法則に対する繰り込み済み作用を

```math
\mathcal A_{N,h}^{R,U}(\theta)
=
\mathbb{E}_{N,\theta}^{R}
\int_0^{T-h}
\left[
\frac m{2h^2}
|X_N(t+h)-X_N(t)|^2
-\frac{md\nu}{h}
-U_\theta(X_N(t),t)
\right]\,\mathrm{d} t
```

と定義する。差し引く項は結果や設定に依存せず、有限差分の Gaussian 自己揺らぎだけを除く。

## 許容するパラメータ族

パラメータ集合 $K\subset\mathbb{R}^p$ をコンパクトとする。次を仮定する。

1. $F_\theta(t)$、$f_\theta(t)$ は $(\theta,t)$ について $C^2$ であり、$K\times[0,T]$ 上で2階まで一様有界である。
2. 初期平均 $m_{0,\theta}$ と初期共分散 $P_{0,\theta}$ は $C^2$ で、$P_{0,\theta}\geq p_*I>0$ である。
3. 終端観測 $H_\theta$、$y_\theta$、$R_\theta$ は $C^2$ で、$R_\theta\geq r_*I>0$ である。
4. 外部ポテンシャルは

```math
U_\theta(x,t)
=
\frac12x^{\mathsf T}K_\theta(t)x
+\ell_\theta(t)^{\mathsf T}x
+c_\theta(t)
```

の形で、係数は $C^2$ かつ一様有界である。
5. Fourier 切断数 $N$ と粗視化幅 $h=h_N$ は

```math
h_N\longrightarrow0,
\qquad
N\left(\frac{h_N}{T}\right)^2\longrightarrow\infty
```

を満たす。

$C^1(K)$ は作用値と $\theta$ に関する全ての第1偏微分の一様ノルムを表す。この定理は、任意の非線形な経路変分についての無限次元 $C^1$ 定理ではなく、指定した線形 Gaussian パラメータ族上の定理である。

## 極限作用

極限の条件付き拡散の前進流れを $b_{+,\theta}^R$、時刻密度を $\rho_\theta^R$ とする。Guerra--Morato 型作用を

```math
\mathcal A_{\mathrm{GM}}^{R,U}(\theta)
=
\int_0^T\int_{\mathbb{R}^d}
\rho_\theta^R(x,t)
\left[
\frac m2|b_{+,\theta}^R(x,t)|^2
+m\nu\nabla\cdot b_{+,\theta}^R(x,t)
-U_\theta(x,t)
\right]
\,\mathrm{d} x\,\mathrm{d} t
```

と定義する [4]。線形 Gaussian 系では $b_+^R$ は $x$ の1次式、$\rho^R$ は正の Gaussian 密度なので、全ての積分は有限である。

## 線形 Gaussian <i>C</i><sup>1</sup> 収束定理

<!-- theorem-start:theorem -->
**定理（線形 Gaussian $C^1$ 極限）**
第4.2節の仮定を満たすとする。ある定数 $C_K<\infty$ が存在し、十分大きい $N$ と $0<h<T/4$ に対して

```math
\left\|
\mathcal A_{N,h}^{R,U}
-
\mathcal A_{\mathrm{GM}}^{R,U}
\right\|_{C^1(K)}
\leq
C_K
\left(
\frac hT
+
\frac{T^2}{Nh^2}
\right)
```

が成立する。従って $h_N\to0$ かつ $N(h_N/T)^2\to\infty$ なら、次の収束が $C^1(K)$ で成り立つ。

```math
\mathcal A_{N,h_N}^{R,U}
\longrightarrow
\mathcal A_{\mathrm{GM}}^{R,U}.
```

特に $h_N=TN^{-1/3}$ なら誤差は $O(N^{-1/3})$ である。
<!-- theorem-end:theorem -->

この $N^{-1/3}$ は、共分散尾部を $O(N^{-1})$ と評価し、増分商の $h^{-2}$ と釣り合わせた現在の証明から得られる率である。下界または最適性は示していない。より滑らかな核、端点適合基底、相殺を用いれば改善される可能性があり、本質的な普遍指数とは主張しない。

証明の中心は、Fourier 切断による共分散誤差 $O(T^2/N)$ と、時間対角展開による粗視化誤差 $O(h/T)$ を分離することである。増分商には $h^{-2}$ が掛かるため、前者は作用上で $O(T^2/(Nh^2))$ になる。有限分解能記録による Schur 補完の安定性と、パラメータ第1微分を含む全評価は付録Bに示す。

## Guerra--Morato 表示と Nelson 表示

前進・後退流れから

```math
v^R=\frac{b_+^R+b_-^R}{2},
\qquad
u^R=\frac{b_+^R-b_-^R}{2}
=\nu\nabla\log\rho^R
```

を定義する。境界項が消える条件、例えば全空間での Gaussian 減衰、周期境界、または無流束境界を仮定する。

<!-- theorem-start:theorem -->
**定理（Guerra--Morato 作用と Nelson 作用の一致）**

```math
\mathcal A_{\mathrm{GM}}^{R,U}
=
\mathcal A_{\mathrm{N}}^{R,U},
```

```math
\mathcal A_{\mathrm{N}}^{R,U}
=
\int_0^T\int_{\mathbb{R}^d}
\rho^R
\left[
\frac m2|v^R|^2
-\frac m2|u^R|^2
-U
\right]
\,\mathrm{d} x\,\mathrm{d} t.
```

<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
$b_+^R=v^R+u^R$ と $\nu\nabla\rho^R=\rho^Ru^R$ を用いる。空間部分積分により

```math
\int\rho^R m\nu\nabla\cdot b_+^R\,\mathrm{d} x
=
-m\int\rho^R b_+^R\cdot u^R\,\mathrm{d} x.
```

従って

```math
\frac m2|b_+^R|^2
-m b_+^R\cdot u^R
=
\frac m2|v^R|^2
-\frac m2|u^R|^2.
```

ポテンシャル項は共通なので結論を得る。
<!-- theorem-end:proof -->

この一致は近似ではない。$C^1$ 極限で得られた Guerra--Morato 作用は、正の Gaussian 密度領域では Nelson 作用そのものである [3--6]。Guerra--Morato 作用の臨界点と第2変分を扱う近年の研究もあるが [35]、本定理が扱う有限 Fourier 条件付き族の2尺度 $C^1$ 収束とは問題設定が異なる。

## 停留点について言えること

<!-- theorem-start:corollary -->
**系（収束する停留点）**
$\theta_N\in\operatorname{int}K$ が

```math
D_\theta\mathcal A_{N,h_N}^{R,U}(\theta_N)=0,
\qquad
\theta_N\longrightarrow\theta_*
```

を満たすなら、

```math
D_\theta\mathcal A_{\mathrm{N}}^{R,U}(\theta_*)=0
```

である。
<!-- theorem-end:corollary -->

<!-- theorem-start:proof -->
**証明**
$C^1(K)$ 収束と $D\mathcal A_{N,h_N}(\theta_N)=0$ から

```math
\|D\mathcal A_{\mathrm{N}}(\theta_*)\|
\leq
\|D\mathcal A_{\mathrm{N}}(\theta_*)-D\mathcal A_{\mathrm{N}}(\theta_N)\|
+
\|D\mathcal A_{\mathrm{N}}(\theta_N)-D\mathcal A_{N,h_N}(\theta_N)\|
\longrightarrow0.
```

<!-- theorem-end:proof -->

これは一方向の条件付き主張である。まず有限モデルのパラメータ停留点列が存在し、その列が収束する場合に限って、極限点が Nelson 作用の停留点になる。任意の Nelson 停留点を有限浴の停留点列で近似するには、Hessian の非退化性と少なくとも局所 $C^2$ 収束が必要である。さらに、微視的 Hamiltonian 方程式が粗視化作用の停留点を力学的に選ぶことは、この系から従わない。

## 調和 Gaussian の物理像

1次元で

```math
\rho(x,t)
=
\frac1{\sqrt{2\pi}\sigma(t)}
\exp\left[
-\frac{(x-q(t))^2}{2\sigma(t)^2}
\right]
```

とし、連続の式を満たす速度を

```math
v(x,t)
=
\dot q(t)
+\frac{\dot\sigma(t)}{\sigma(t)}[x-q(t)]
```

とする。浸透速度は

```math
u(x,t)
=
-\nu\frac{x-q(t)}{\sigma(t)^2}
```

である。調和ポテンシャル $U=m\Omega^2x^2/2$ に対する Nelson 作用は

```math
\mathcal A_G[q,\sigma]
=
\frac m2
\int_0^T
\left[
\dot q^2+\dot\sigma^2
-\frac{\nu^2}{\sigma^2}
-\Omega^2(q^2+\sigma^2)
\right]\,\mathrm{d} t.
```

変分すると

```math
\ddot q+\Omega^2q=0,
```

```math
\ddot\sigma+\Omega^2\sigma
-\frac{\nu^2}{\sigma^3}=0
```

を得る。中心は古典的な調和運動を行い、幅は通常の拡散で単調に広がるのではなく、調和閉じ込めと密度勾配の項の釣り合いで振動する。定常幅は

```math
\sigma_*^2=\frac\nu\Omega
```

である。これは Nelson 作用が、単なる熱拡散ではなく、確率流と密度勾配の前後対称な変分力学を表すことを示す。

## 定理の範囲

本章で証明したのは、線形 Gaussian 範囲における作用形式の $C^1$ 極限である。次は主定理に含まれない。

- 状態依存の非線形な流れ。
- 退化した点終端 $R=0$。
- 硬いしきい値条件による非滑らかな経路選択。
- 2次を超える一般ポテンシャルに対する一様第1変分評価。
- 密度の節を横切る大域位相。
- 全ての Nelson 変分を尽くす無限次元 $C^1$ 収束。
- 微視的 Hamiltonian 運動による粗視化作用の停留点選択。
- 一般の時間依存線形 Gaussian 表示を有限自律 Hamiltonian へ埋め込む定理。

したがって本章の結果を「Nelson 有効力学の動力学的出現」とは呼ばない。確立した内容は、明示した確率表示と粗視化規則に対する作用形式の収束である。

# 第II部　2境界統計原理と2モード作用分配系による Bell 型統計

# 有限 Hamiltonian 装置部品と2境界履歴集団

> **位置づけ：** 最小結果符号化モデル、終端比較器、全履歴測度を分離し、`[R]` を独立な2境界統計原理として明示する。


## 第II部の目的

第2章から第4章は、観測座標の線形 Gaussian 経路法則と Nelson 作用形式を扱った。そこから Bell 型結果重みは出ない。Bell 実験を記述するには、少なくとも次の構造が必要である。

1. 左右の測定設定制御器。
2. 局所的に確定する2値記録。
3. 設定と結果符号を共通未来へ運ぶ伝達ベクトル。
4. 2つの伝達ベクトルを比較する、設定名を直接参照しない二次形式。
5. 比較結果と未読の作用分配変数を照合する終端座標。
6. 終端整合履歴を物理的集団とする2境界統計原理。

本章では、これらを有限 Hamiltonian 部品として定式化し、各部品が何を実現するかを分けて示す。局所装置は結果符号を指針へ写す最小符号化モデルであり、一般の測定相互作用ではない。一般の局所パルスは短時間極限で所望の正準写像へ近づく。第7章の終端比較器だけは、保存量との交換関係を用いて有限幅でも厳密な読出しを与える。

## 正準変数

1試行の第II部に必要な正準変数を次のように取る。

- 伝達ベクトル対：$(Q_A,P_A)$、$(Q_B,P_B)$。
- 結果種対：$(s_A,\pi_A)$、$(s_B,\pi_B)$。
- 測定設定制御対：$(a,\alpha)$、$(b,\beta)$。
- 応答モード対：$(x_A,p_A)$、$(x_B,p_B)$。
- 固定指針対：$(Y_A,\Pi_A)$、$(Y_B,\Pi_B)$。
- 局所有限浴対：$(r_{Xj},\varpi_{Xj})$、$X=A,B$、$1\leq j\leq n_X$。
- 作用分配用の正準対：$(q_s,p_s)$、$(q_0,p_0)$。
- 終端比較対：$(Y_R,\Pi_R)$。
- 相補時計中心対：$(\bar\tau,P_c)$。
- 自律順序時計対：$(\vartheta,J_c)$。

伝達ベクトルの作用を

```math
I_X
=
\frac12
\left(
Q_X^2+P_X^2
\right),
\qquad
X=A,B
```

とする。作用分配系の2つの作用は

```math
J_s
=
\frac12
\left(
q_s^2+p_s^2
\right),
```

```math
J_0
=
\frac12
\left(
q_0^2+p_0^2
\right)
```

である。装置部品を自律時計で接続した形式的な全 Hamiltonian は

```math
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
```

と書ける。各項の具体形と誤差の地位は付録Cにまとめる。この式は部品表であり、全自由項を含む有限幅発展が各理想正準写像を厳密に実行するという意味ではない。比較窓については、必要な全項を第7.1節で1本の Hamiltonian として明示する。

## 結果種と測定設定制御器

$s_X$ を円周座標とし、互いに等しい Liouville 体積を持つ2つの平坦領域 $\Sigma_X^+$、$\Sigma_X^-$ を取る。滑らかな周期関数 $\sigma$ を

```math
\sigma(s)
=
+1
\qquad
\left(
s\in\Sigma^+
\right),
```

```math
\sigma(s)
=
-1
\qquad
\left(
s\in\Sigma^-
\right)
```

とし、2領域の間だけで滑らかに補間する。基準準備は補間領域に台を持たない。したがって実際の台上で

```math
\sigma'(s)=0.
```

局所結果を

```math
A=\sigma(s_A),
\qquad
B=\sigma(s_B)
```

とする。負符号領域の指示関数は

```math
\chi_-(s)
=
\frac{1-\sigma(s)}2
```

である。

測定設定は制御座標の初期巨視領域で決まる。全試行に同じ Hamiltonian 関数を用い、

```math
a=\mathfrak a(\xi_A),
\qquad
b=\mathfrak b(\xi_B)
```

という粗視化写像で設定を読み出す。以下では制御座標自体を簡単に $a,b$ と書く。

この最小モデルでは結果種を明示的に置き、$A$ と $B$ は測定設定や到来する伝達ベクトルに依存しない。したがって、この部品は結果を生成する測定器ではなく、既存の2値符号を応答モードと固定指針へ写す結果符号化器である。

より一般の局所決定論応答

```math
A=\mathscr A(a,\lambda_A),
\qquad
B=\mathscr B(b,\lambda_B)
```

を扱うには、設定 $a$、到来変数、局所微視状態を結合する具体的な局所 Hamiltonian 前処理を追加する必要がある。本論文はその一般前処理を構成せず、第7章では上の最小結果符号化モデルを用いる。Bell 監査に必要な局所因子化は満たすが、これだけで一般の物理的測定過程を実現したとはみなさない。

## 自律パルス Hamiltonian

時計角 $\vartheta$ 上に、互いに重ならない滑らかなパルス形 $f_{\nu,\epsilon}(\vartheta)$ を置き、

```math
\int f_{\nu,\epsilon}(\vartheta)d\vartheta=1
```

と規格化する。全 Hamiltonian に

```math
H_{\rm clk}
=
\Omega J_c
```

とパルス項

```math
H_{\rm pulse}
=
\Omega
\sum_\nu
f_{\nu,\epsilon}(\vartheta)K_\nu
```

を加える。各 $K_\nu$ は $J_c$ に依存しないため、

```math
\dot\vartheta
=
\frac{\partial H_{\rm tot}}{\partial J_c}
=
\Omega
```

が厳密に成立する。$J_c$ はパルスの反作用を受け、拡張した全 Hamiltonian のエネルギーは保存される。

ただし、自由 Hamiltonian $H_0$ もパルス中に同時に働く。したがって、一般にはパルスの全流れが生成子 $K_\nu$ の単位流れと厳密に一致するわけではない。パルスの時間幅を $\epsilon_\nu$ とし、有界な適用領域 $\mathcal K$ 上で関係する Hamiltonian ベクトル場と第1微分が有界なら、

```math
\sup_{z\in\mathcal K}
\left\|
\Phi_{\rm full}^{(\nu)}(z)
-
e^{X_{K_\nu}}z
\right\|
\leq
C_{\mathcal K}\epsilon_\nu
```

となる。詳細は付録C.3に示す。以後、局所分析と指針固定の式は短時間パルス極限の理想写像として書き、有限幅では $O(\epsilon_\nu)$ の補正を伴うものとする。

この自律化は、測定設定ごとに異なる Hamiltonian を外から挿入する操作ではない。測定設定は位相空間内の制御器状態、操作順序は同じ時計軌道上の異なる区間である。$(\vartheta,J_c)$ は操作順序時計であり、第5.9節の相補的内部時計とは別自由度である。

## 局所分析器と応答モード

A 側の分析器生成子を

```math
K_A^{\rm an}
=
-\left[
\phi(a)
+\pi\chi_-(s_A)
\right]I_A
-x_A\sigma(s_A)
```

とし、B 側も同様に

```math
K_B^{\rm an}
=
-\left[
\phi(b)
+\pi\chi_-(s_B)
\right]I_B
-x_B\sigma(s_B)
```

とする。

$K_A^{\rm an}$ の単位流れのパラメータを $\tau$ とすると、結果種の平坦領域上で

```math
\frac{dQ_A}{d\tau}
=
-\theta_A P_A,
\qquad
\frac{dP_A}{d\tau}
=
\theta_A Q_A,
```

```math
\theta_A
=
\phi(a)+\pi\chi_-(s_A),
```

および

```math
\frac{dp_A}{d\tau}
=
\sigma(s_A)=A,
\qquad
\frac{dx_A}{d\tau}=0
```

を得る。応答運動量を $p_A^{\rm in}=0$ に準備すれば、理想写像では

```math
p_A^{\rm out}=A.
```

伝達ベクトルは

```math
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
```

となる。B 側も

```math
p_B^{\rm out}=B,
```

```math
u_B^{\rm out}
=
B R[\phi(b)]u_B^{\rm in}
```

を満たす。有限幅の全流れでは、これらの右辺に第5.4節の $O(\epsilon_{\rm an})$ 補正が加わる。補正が平坦領域と指針領域の幅より十分小さいことを、局所装置の適用条件とする。

応答モードは測定設定パルスと局所結果種に応答する一時変数である。結果確率を生成する浴ではない。各軌道の $A,B$ は結果種と局所 Hamiltonian 流れで一意に決まる。

## 固定指針への記録

滑らかな平坦関数 $\zeta(p)$ を

```math
\zeta(p)=+1
\quad
\left(
|p-1|<\delta_p
\right),
```

```math
\zeta(p)=-1
\quad
\left(
|p+1|<\delta_p
\right)
```

となるよう取る。固定指針への転写生成子を

```math
K_X^{\rm lock}
=
-Y_X\zeta(p_X)
```

とする。単位流れでは

```math
\frac{d\Pi_X}{d\tau}
=
\zeta(p_X),
\qquad
\frac{dY_X}{d\tau}=0,
\qquad
\frac{dp_X}{d\tau}=0.
```

したがって理想写像で $\Pi_X^{\rm in}=0$ なら

```math
\Pi_A^{\rm out}=A,
\qquad
\Pi_B^{\rm out}=B.
```

2つの互いに交わらない巨視領域

```math
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
```

を指針記録とする。有限幅補正が $1/2$ の領域間隔より十分小さければ、記録符号は変わらない。固定指針対はこの後の共通未来比較器から切り離すため、比較段階は過去の指針符号を変更しない。

応答モードには、記録後に有限局所浴

```math
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
```

を結合できる。これは応答モードの一時情報と位相情報を複数自由度へ分散し、有限観測窓での再読出し誤差を小さくする。ただし有限閉鎖浴は真の散逸を与えず、十分長時間では再帰を持つ。記録の主張は

```math
\tau_{\rm lock}
\ll
\tau_{\rm cmp}
\ll
T_{{\rm rec},X}
```

の範囲に限る。

## 共通未来への伝播

局所記録時刻を $t_A,t_B$、両伝達ベクトルが同じ時空領域へ到達できる時刻を $t_C$、終端時刻を $T$ とし、

```math
t_A,t_B<t_C<T
```

とする。$t_C$ より前の結合図は

```math
(u_A,s_A,a,x_A,Y_A,\Gamma_{{\rm bath},A})
```

と

```math
(u_B,s_B,b,x_B,Y_B,\Gamma_{{\rm bath},B})
```

に分離する。A 側の Hamiltonian は B 側の測定設定、結果種、指針を含まず、B 側も同様である。

$t_C$ 以後に2つの伝達ベクトルを同じ比較器へ入れる。これは局所記録後の時間的な共通未来における通常の相互作用であり、空間的に分離した記録形成へ遠隔力を導入しない。第7章で現れる測定設定依存性は、共通未来の相互作用自体が過去を変更するためではなく、その相互作用を含む全軌道へ `[R]` を適用するためである。

## 終端関数と履歴測度

初期超曲面上の全微視状態を

```math
z_i=(\lambda,\eta,\xi_A,\xi_B)
```

とする。$\lambda$ は結果応答を完結させる生成源と局所装置の変数、$\eta$ は後に積分する作用分配系、混合器、終端比較対などの未読変数、$\xi_A,\xi_B$ は測定設定制御変数である。基準準備では

```math
\rho_S(\lambda,\eta,\xi_A,\xi_B)
=
\rho_S(\lambda,\eta)
\rho_A(\xi_A)
\rho_B(\xi_B)
```

とする。

終端時刻 $T$ に、全測定設定と全結果に共通な非負関数

```math
G_R:\Gamma\longrightarrow[0,\infty)
```

を固定する。`[R]` による条件付き履歴測度は

```math
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
```

$\lambda$ を固定して未読変数を積分した終端整合度を

```math
h_{a,b}(\lambda)
=
\int
\rho_S(\eta\mid\lambda)
G_R\!\left[
\Phi_{a,b}^{T}(\lambda,\eta)
\right]
d\eta
```

と定義すると、生成源超曲面上の事後分布は

```math
\rho_R(\lambda\mid a,b)
=
\frac{
\rho_S(\lambda)h_{a,b}(\lambda)
}{
Z_{a,b}
}
```

となる。

<!-- theorem-start:proposition -->
**命題（終端整合度の判定条件）**
全測定設定対に対して同一の事後分布 $\rho_R(\lambda)$ が存在するための必要十分条件は、ある非負関数 $h(\lambda)$ と正定数 $c_{a,b}$ が存在して

```math
h_{a,b}(\lambda)
=
c_{a,b}h(\lambda)
```

がほとんど至る所で成立することである。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
上式が成立すれば $c_{a,b}$ は規格化で消える。逆に事後分布が全測定設定で同じなら、

```math
\frac{h_{a,b}(\lambda)}{Z_{a,b}}
=
\frac{h_{a',b'}(\lambda)}{Z_{a',b'}}
```

なので、各終端整合度は共通関数へ比例する。
<!-- theorem-end:proof -->

したがって固定した $G_R$ であっても、その Hamiltonian 引き戻し

```math
G_R\circ\Phi_{a,b}^{T}
```

が生成源変数を測定設定に依存して再重みづけし得る。

## 相補的内部時計による終端半空間の正準実現

終端比較対 $(Y_R,\Pi_R)$ に中心対 $(\bar\tau,P_c)$ を加え、2つの内部時計対を

```math
\tau_A
=
\bar\tau+\frac{Y_R}{2},
\qquad
\tau_B
=
\bar\tau-\frac{Y_R}{2},
```

```math
\varrho_A
=
\frac{P_c}{2}+\Pi_R,
\qquad
\varrho_B
=
\frac{P_c}{2}-\Pi_R
```

で定める。実際、

```math
\varrho_A\,d\tau_A
+
\varrho_B\,d\tau_B
=
P_c\,d\bar\tau
+
\Pi_R\,dY_R
```

なので、これは正準変換である。

内部時計の自由 Hamiltonian を

```math
H_{\rm or}
=
\frac{\varrho_A^2+\varrho_B^2}{2M_\tau}
+
\frac{\kappa_c}{2}
\left(
\varrho_A+\varrho_B
\right)^2
```

とする。中心・相対変数では

```math
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
```

相補的領域

```math
P_c=0
```

は自由運動と、$\bar\tau$ に依存しない比較パルスの双方で保存される。この領域では

```math
\varrho_A=\Pi_R,
\qquad
\varrho_B=-\Pi_R,
```

```math
\dot\tau_A
=
\frac{\Pi_R}{M_\tau},
\qquad
\dot\tau_B
=
-\frac{\Pi_R}{M_\tau}.
```

したがって $\Pi_R>0$ は A 時計が正向き、B 時計が負向きの順序付き相補性を表す。これは2粒子が実験室時刻に対して逆向きに伝播するという意味ではない。左右の粒子と伝達ベクトルは通常どおり生成源から局所装置、共通未来へ進み、反対になるのは内部時計または境界情報の向きである。

<!-- theorem-start:proposition -->
**命題（終端半空間の相補時計実現）**
$P_c=0$、比較パルス直前の $\Pi_R=E_*>0$ とする。比較生成子を

```math
K_R
=
Y_R
\left(
h-\kappa I_-
\right)
```

とし、$g_R(t)=\Omega f_R[\vartheta(t)]$ の時間積分を1とする。比較窓の自由 Hamiltonian が $h$ と $I_-$ を保存するなら、

```math
\dot\Pi_R
=
g_R(t)
\left(
\kappa I_- -h
\right),
\qquad
\dot Y_R
=
\frac{2\Pi_R}{M_\tau}
```

である。$Y_R$ はパルス中も一般に動くが、$\dot\Pi_R$ は $Y_R$ に依存しない。したがって有限幅パルスの後に厳密に

```math
\Pi_R(T)
=
E_*+\kappa I_- -h.
```

順序付き時計向きが終端まで保存される条件

```math
\varrho_A(T)\geq0,
\qquad
\varrho_B(T)\leq0
```

は

```math
\Pi_R(T)\geq0
```

と必要十分である。
<!-- theorem-end:proposition -->

証明の要点は

```math
\{h,K_R\}
=
\{I_-,K_R\}
=
0
```

である。比較パルスは作用分配系と差動モードの角変数を動かし得るが、読出しに必要な2つの作用は変えない。完全な比較窓 Hamiltonian と積分は第7.1節および付録C.6に示す。

これにより $\Pi_R$ は任意の終端運動量ではなく2時計の相対運動量、$E_*$ は時計向きが反転するまでの初期運動量余裕、$G_R=\mathbf1_{\{\Pi_R(T)\geq0\}}$ は順序付き向き保存条件と読める。

ただし Hamilton 方程式は $\Pi_R(T)<0$ の軌道を禁止しない。この軌道では

```math
\varrho_A(T)<0,
\qquad
\varrho_B(T)>0
```

となり、時計向きが交換されるだけである。したがって相補的時計は終端半空間の形を導くが、その半空間に入る履歴だけを物理的集団とする `[R]` までは導かない。

## `[R]` と事後選別

数式上、

```math
\rho_R
\propto
\rho_S G_R\circ\Phi^T
```

は、実験後の棄却抽出と同じ条件付き確率に見える。本論文が `[R]` を物理的な境界原理として用いるためには、少なくとも次を要求する。

1. $G_R$ は Bell データを見る前に装置の終端巨視領域として固定する。
2. 全測定設定と全結果に同じ終端装置と分解能を用いる。
3. 実現した指針記録を後から除外しない。
4. 終端幅、作用分配系の総エネルギー、比較尺度を独立な較正で決める。
5. 外部開始数、指針記録数、終端完了数の関係を報告する。

これらを満たせず、観測済み試行の一部を捨てて初めて Bell 値が出るなら、本構成は検出事後選別に退化する。`[R]` を公理として書くだけでは、この操作上の区別は保証されない。

## 本章の結論

局所分析器、応答モード、固定指針、有限局所浴、設定伝達ベクトル、共通未来への伝播、終端履歴測度を有限正準部品の中に配置した。ただし局所装置は結果符号化器であり、一般の測定相互作用ではない。局所パルスの理想写像には有限幅で $O(\epsilon)$ の補正がある。

終端比較対は相補的内部時計の相対対として正準実現できる。比較生成子を線形な $K_R=Y_R(h-\kappa I_-)$ としたことで、内部時計の自由運動により $Y_R$ が変化しても、終端運動量の読出しは厳密に保たれる。

結果頻度を定める原理は、局所浴の散逸、指針の保持時間、比較速度、時計相補性のいずれでもない。物理的履歴集団を定める `[R]` と、次章で導く終端整合体積である。

# 共通未来の比較器と2モード作用分配系

> **位置づけ：** 余弦型差動作用と結果領域内の一様なソフトモードエネルギー密度を、別々の位相空間幾何から導く。


## 位相同期した伝達ベクトル

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

とする。第5章の局所パルス後には

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

となる。$A,B$ は局所固定指針にすでに記録されている。伝達ベクトルは、その符号と分析器位相の写しを共通未来へ運ぶ。

相対角を

```math
\Delta_{ab}
=
\phi(a)-\phi(b)+\Theta_A-\Theta_B
```

とする。測定設定が物理的な分析器角である場合、$\phi$ は装置表現に依存する。平面回転型では $\phi(a)=a$、直線偏光型では倍角写像 $\phi(a)=2a$ を用い得る。この写像は終端規則ではなく、局所分析器の較正に属する。

## 差動作用の余弦幾何

共通未来の差動モード作用を

```math
I_-^{AB}
=
\frac14
\left\|
u_A-u_B
\right\|^2
```

と定義する。直接展開すると

```math
I_-^{AB}
=
\frac14
\left[
r_A^2+r_B^2
-2ABr_Ar_B\cos\Delta_{ab}
\right].
```

<!-- theorem-start:proposition -->
**命題（実2次元比較器の余弦恒等式）**
等振幅 $r_A=r_B=r$、固定相対生成源位相 $\Theta_A-\Theta_B=\Phi_0$ の下で、

```math
I_-^{AB}
=
I_0
\left[
1-AB\cos
\left\{
\phi(a)-\phi(b)+\Phi_0
\right\}
\right],
```

```math
I_0=\frac{r^2}{2}
```

である。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
回転行列の内積

```math
n(\Theta_A)^{\mathsf T}
R[\phi(b)-\phi(a)]
n(\Theta_B)
=
\cos\Delta_{ab}
```

を差ベクトルの2乗へ代入すればよい。
<!-- theorem-end:proof -->

余弦は複素確率振幅、Born 則、量子内積から導入されていない。2つの実正準ベクトルの Euclid 内積

```math
u_A\cdot u_B
=
ABr_Ar_B\cos\Delta_{ab}
```

から出る。

## 振幅不一致と位相雑音

生成源位相を

```math
\Theta_A-\Theta_B
=
\Phi_0+\delta
```

とし、$r_A,r_B,\delta$ に測定設定と結果符号から独立な準備分布を許す。終端整合重みは $I_-$ に線形になるため、生成源変数を先に平均してよい。

```math
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
```

基準作用、可視度、位相ずれを

```math
I_0
=
\frac14
\left\langle
r_A^2+r_B^2
\right\rangle,
```

```math
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
```

```math
\delta_0
=
\arg
\left\langle
r_Ar_Be^{i\delta}
\right\rangle
```

と置けば、

```math
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
```

Cauchy--Schwarz 不等式から

```math
0\leq V\leq1
```

である。以下では位相ずれを $\Delta_{ab}$ に吸収し、

```math
\overline I_-^{AB}
=
I_0
\left[
1-ABV\cos\Delta_{ab}
\right]
```

と書く。

## 2モード作用分配系

比較器の未読変数として、1つのソフトモードと1つの残余作用モードを置く。

```math
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
```

両モードの基準周波数を同じ $\omega_\ell>0$ とし、

```math
J_\ell
=
J_s+J_0,
```

```math
E_\ell
=
\omega_\ell J_\ell
```

を固定する。ソフトモードのエネルギーを

```math
h
=
\omega_\ell J_s
```

とする。残余作用モードは、ソフトモードに入っていない残余作用

```math
E_\ell-h
=
\omega_\ell J_0
```

を保持する。

2つの作用・角変数を

```math
q_\nu
=
\sqrt{2J_\nu}\cos\theta_\nu,
\qquad
p_\nu
=
\sqrt{2J_\nu}\sin\theta_\nu,
\qquad
\nu=s,0
```

と取れば、

```math
dq_\nu\,dp_\nu
=
dJ_\nu\,d\theta_\nu.
```

固定総作用殻上の正規化 Liouville 測度を

```math
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
```

とする。

## 一様なソフトモードエネルギー周辺定理

<!-- theorem-start:theorem -->
**定理（2モード作用分配系の一様周辺）**
固定 $E_\ell>0$ の2モード作用殻上で、ソフトモードのエネルギー $h=\omega_\ell J_s$ の周辺密度は

```math
p_\ell(h)
=
\frac1{E_\ell}
\mathbf1_{\{0\leq h\leq E_\ell\}}
```

である。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
位相角を積分すると $(2\pi)^2$ を得る。$h=\omega_\ell J_s$ を固定した未規格化密度は

```math
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
```

全質量は

```math
\int_0^{E_\ell}
\frac{dh}{\omega_\ell^2}
=
\frac{E_\ell}{\omega_\ell^2}.
```

規格化すると $p_\ell(h)=1/E_\ell$ である。
<!-- theorem-end:proof -->

この定理は、2つの1自由度調和モードの状態密度がともに定数であることの帰結である。結果領域、測定設定、生成源位相は固定総作用殻の定義に現れないため、`[M]` の入口測度が各結果領域で共通なら

```math
p
\left(
h\mid A,B,a,b
\right)
=
\frac1{E_\ell}
```

となる。

## 有限非線形混合器

ソフトモードと残余作用モードの総作用 $J_\ell$ を保存したまま、2モード間の作用配分と相対位相を変える有限 Hamiltonian 生成子を構成できる。必要な生成子は

```math
\{J_\ell,K_M\}=0
```

を満たす。具体的には、2モードの双線形生成子と有限個の非線形環境変数を結合すればよい。全生成子、Poisson 括弧、保存則は付録C.8に示す。

この構成が保証するのは、固定総作用殻とその Liouville 測度が不変であることだけである。特定の有限混合器が必要な時間窓で十分に混合することは、生成子の存在からは従わない。混合速度、再帰時間、有限分解能での偏差は別に検証する必要がある。

## 不変測度と動的混合の区別

2モード定理には2つの読み方がある。

1. **集団としての準備**：比較器入口を固定作用殻の正規化 Liouville 測度で準備する。この場合 $p_\ell(h)=1/E_\ell$ は厳密である。
2. **時間典型性による準備**：1つの初期微視状態を有限混合器で長時間発展させ、有限分解能の時間頻度分布を入口測度として用いる。この場合は混合と時間尺度分離が必要である。

Hamiltonian 流れは微細 Liouville 密度を保存する。したがって任意の初期密度が $L^1$ または各点で一様密度へ収束するとは言えない。混合が与え得るのは、滑らかな粗視化観測量 $F$ に対する

```math
\frac1{\tau_{\rm cmp}}
\int_0^{\tau_{\rm cmp}}
F[h(t)]dt
\approx
\int_0^{E_\ell}
F(h)\frac{dh}{E_\ell}
```

という有限時間平均、または初期小領域を粗視化した弱い収束である。

必要な時間尺度は

```math
\tau_{\rm mix}
\ll
\tau_{\rm cmp}
\ll
T_{\rm rec}.
```

$\tau_{\rm mix}$ は粗視化頻度分布の緩和、$\tau_{\rm cmp}$ は比較器が作用分配系の状態を読み出す前の混合窓、$T_{\rm rec}$ は有限混合器の再帰尺度である。本論文は一般の $K_M$ に対してこの不等式を証明しない。これは数値検証すべき `[M]` の動力学部分である。

## 通常の多モード浴が失敗する理由

ソフトモードが $N$ 個の残余作用モードと固定総エネルギーを自由に分け合うとする。各モードが1つの調和正準対で、全単体

```math
h+\sum_{j=1}^{N}e_j=E_\ell,
\qquad
h,e_j\geq0
```

上の一様 Liouville 測度を用いる。$h$ を固定した残余単体の体積は $(E_\ell-h)^{N-1}$ に比例するので、

```math
p_N(h)
=
\frac{N}{E_\ell}
\left(
1-\frac h{E_\ell}
\right)^{N-1},
\qquad
0\leq h\leq E_\ell.
```

しきい値 $x$ 以下の累積重みは

```math
F_N(x)
=
\int_0^x p_N(h)dh
=
1-
\left(
1-\frac x{E_\ell}
\right)^N.
```

$N=1$ のときだけ

```math
F_1(x)=\frac{x}{E_\ell}
```

が線形である。$N>1$ では $x$ の二次以上の項が現れる。第7章のしきい値

```math
x_{AB}
=
E_*+\kappa I_0
\left(
1-ABV\cos\Delta_{ab}
\right)
```

を代入すると、$\cos^2\Delta_{ab}$ 以上の高調波が一般に残る。

したがって「大きな浴ほど Bell の余弦則に近づく」という主張は成立しない。純粋な線形整合重みに必要なのは、

- 1つのソフトモードの正準対。
- 1つの残余作用モードの正準対。
- 総作用を保つ向き混合。

という最小構造である。追加浴は混合器のカオスを作る補助であり、しきい値依存エネルギーを自由に共有する作用分配自由度にしてはならない。

## 結果領域の質量対称性

2モード定理が決めるのは各結果領域内の条件付き密度であり、領域自体の基準質量ではない。基準準備測度における4領域を

```math
\Sigma_{AB}
=
\left\{
\sigma(s_A)=A,\,
\sigma(s_B)=B
\right\}
```

とし、

```math
w_{AB}
=
\mu_S(\Sigma_{AB})
```

と定義する。

準備段階に2つの測度保存対合

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

があり、$H_{\rm prep}$、準備巨視領域、$\mu_S$ を保つとする。2つの変換が生成する群は4領域に推移的に作用する。

<!-- theorem-start:proposition -->
**命題（対称準備の結果領域等体積）**
上の独立符号反転対称性 `[S]` の下で、

```math
w_{++}
=
w_{+-}
=
w_{-+}
=
w_{--}
=
\frac14
```

である。
<!-- theorem-end:proposition -->

<!-- theorem-start:proof -->
**証明**
$\mathcal S_A$ と $\mathcal S_B$ は測度保存全単射なので、任意の2領域の測度は等しい。4領域が準備測度の全台を分割するため、規格化すると各質量は $1/4$ である。
<!-- theorem-end:proof -->

Hamiltonian の符号対称性だけでは不十分である。同じ Hamiltonian に非対称な初期密度を置くことも可能だからである。`[S]` は「対称な準備巨視状態上の不変基準測度を採用する」という統計条件を含む。

## 共通入口密度

第6.5節と第6.9節を組み合わせると、比較器入口での結果領域とソフトモードエネルギーの基準密度は

```math
g_{AB}^{\rm ent}(h)
=
\frac{w_{AB}}{E_\ell}
\mathbf1_{\{0\leq h\leq E_\ell\}}.
```

`[S]` の下では

```math
g_{AB}^{\rm ent}(h)
=
\frac1{4E_\ell}
\mathbf1_{\{0\leq h\leq E_\ell\}}.
```

この式で

- $1/E_\ell$ は2モード作用殻の幾何。
- $1/4$ は準備領域の対称性。

から来る。2つを1つの「等基準因子」として仮定しないことが、本改訂の中心である。

## 本章の結論

Bell 型余弦重みの角度依存性と線形確率変換は、異なる2つの幾何から生じる。余弦は2つの実伝達ベクトルの差動作用、一様なしきい値密度は1つのソフトモードの正準対と1つの残余作用モードの正準対がつくる固定総作用殻から生じる。

有限非線形浴は後者の不変測度を作る論理原理ではなく、その向きを有限時間で典型化する候補機構である。結果領域の質量はさらに準備対称性 `[S]` を必要とする。次章では、設定名を直接参照しない終端座標へこの2つの結果を代入し、共同確率を導く。

# 終端整合測度と Bell 型共同確率

> **位置づけ：** 2モード位相体積と `[R]` を組み合わせ、測定設定独立性の破れを含む条件付き共同確率を導く。


## 有限幅の終端比較器

第5.9節の内部時計自由 Hamiltonian、差動モード、2モード作用分配系、自律順序時計を含む比較窓 Hamiltonian を

```math
H_{\rm win}
=
H_{\rm or}
+
\omega_- I_-
+
\omega_\ell(J_s+J_0)
+
\Omega J_c
+
\Omega f_R(\vartheta)
Y_R
\left(
h-\kappa I_-
\right)
```

とする。ここで

```math
h=\omega_\ell J_s,
\qquad
\int f_R(\vartheta)d\vartheta=1
```

である。$f_R$ は有限幅で滑らかとし、比較窓では他のパルスと重ならない。

$H_{\rm win}$ は $J_c$ へ線形なので、

```math
\dot\vartheta=\Omega
```

が厳密に成り立つ。また、

```math
\{I_-,H_{\rm win}\}=0,
\qquad
\{h,H_{\rm win}\}=0
```

である。したがって、比較パルス中も $I_-$ と $h$ は保存される。終端比較運動量は

```math
\dot\Pi_R
=
-
\frac{\partial H_{\rm win}}{\partial Y_R}
=
\Omega f_R(\vartheta)
\left(
\kappa I_- -h
\right)
```

に従う。一方、相補時計の自由運動により

```math
\dot Y_R
=
\frac{\partial H_{\rm win}}{\partial\Pi_R}
=
\frac{2\Pi_R}{M_\tau}
```

であり、$Y_R$ は一般に一定ではない。しかし $\dot\Pi_R$ は $Y_R$ に依存しない。パルス直前の運動量を $\Pi_R=E_*$ とすると、

```math
\int
\Omega f_R[\vartheta(t)]dt
=
1
```

より、有限幅パルスの後に厳密に

```math
\Pi_R(T)
=
E_*+\kappa I_- -h
```

を得る。

比較パルスは差動モードと残余作用モードの角変数を動かし得るが、読出しに必要な作用 $I_-$ と $h$ は変えない。したがって、旧構成で用いた「パルス中に $Y_R=0$ が保たれる」という仮定は不要である。全計算は付録C.6に示す。

## 固定終端条件

終端巨視領域を

```math
G_R(z_T)
=
\mathbf1_{\{\Pi_R(T)\geq0\}}
```

とする。これは

```math
G_R=1
\quad\Longleftrightarrow\quad
h\leq E_*+\kappa I_-
```

と同値である。

第5.9節の相補的内部時計では $P_c=0$ なので、

```math
\varrho_A(T)=\Pi_R(T),
\qquad
\varrho_B(T)=-\Pi_R(T).
```

したがって同じ終端条件は、初期に選んだ順序付き時計向き

```math
\varrho_A\geq0,
\qquad
\varrho_B\leq0
```

が終端まで保たれた条件である。これは終端半空間の正準力学的意味を与えるが、その半空間だけを物理的履歴集団として数える `[R]` を置き換えない。

$G_R$ の関数形は $a,b,A,B$ も $\cos\Delta_{ab}$ も参照しない。測定設定と結果への依存は、局所 Hamiltonian 回転を含む流れで $G_R$ を初期面へ引き戻したときにのみ現れる。

全生成源の台上で切断端に当たらない適用範囲

```math
0
\leq
E_*+\kappa I_-
\leq
E_\ell
```

を仮定する。理想等振幅モデルでは、十分条件として

```math
E_*+\kappa I_0(1+V)
\leq
E_\ell
```

を用いられる。有限の振幅分布を許す場合は、その台上で同じ上界を課す。

## 終端整合体積

結果領域の基準質量を $w_{AB}$ とする。第6章の2モード定理により、各結果領域内のソフトモードエネルギー密度は $1/E_\ell$ である。生成源揺らぎを $\zeta$、その基準分布を $d\nu(\zeta)$ と書くと、未規格化の終端整合重みは

```math
W_{AB}(a,b)
=
w_{AB}
\int d\nu(\zeta)
\int_0^{E_\ell}
\frac{dh}{E_\ell}
\mathbf1_{\{
h\leq E_*+\kappa I_-^{AB}(\zeta)
\}}.
```

適用範囲の下で $h$ 積分は線形なので、

```math
W_{AB}(a,b)
=
\frac{w_{AB}}{E_\ell}
\left[
E_*+\kappa
\overline I_-^{AB}
\right].
```

第6.3節の可視度表示を代入すると、

```math
W_{AB}(a,b)
=
\frac{w_{AB}}{E_\ell}
\left[
E_*+\kappa I_0
\left(
1-ABV\cos\Delta_{ab}
\right)
\right].
```

Bell 型重みの線形性は、通過流束や滞在時間ではなく、固定総作用殻上の累積 Liouville 体積

```math
\int_0^x
\frac{dh}{E_\ell}
=
\frac{x}{E_\ell}
```

から生じる。

## 2モード作用分配系 Bell 型整合性定理

<!-- theorem-start:theorem -->
**定理（2モード作用分配系を持つ2境界 Bell 型整合性）**
次を仮定する。

1. `[H]`：第5章の局所理想写像または同じ記録領域を保つ有限幅実装、および第7.1節の厳密な終端比較器。
2. `[P]`：第6.3節の位相同期した生成源と可視度 $0\leq V\leq1$。
3. `[S]`：4つの基準結果領域の独立符号反転対称性。
4. `[M]`：固定総作用 $E_\ell$ 上の2モード Liouville 入口測度。
5. `[R]`：第5.8節の2境界統計原理。
6. 適用範囲：$0\leq E_*+\kappa I_-\leq E_\ell$ が生成源の台上で成立する。

このとき、規格化した終端整合共同法則は

```math
P_R(A,B\mid a,b)
=
\frac14
\left[
1-ABV_{\rm eff}\cos\Delta_{ab}
\right],
```

```math
V_{\rm eff}
=
\frac{\kappa I_0}{E_*+\kappa I_0}V
```

である。各履歴の局所応答は因子化するが、Bell の完全な微視状態の事後分布は一般に測定設定へ依存する。
<!-- theorem-end:theorem -->

<!-- theorem-start:proof -->
**証明**
`[S]` から $w_{AB}=1/4$ である。第7.3節より

```math
W_{AB}
=
\frac1{4E_\ell}
\left[
E_*+\kappa I_0
-AB\kappa I_0V\cos\Delta_{ab}
\right].
```

4つの結果を足すと余弦項が消え、

```math
Z_{a,b}
=
\sum_{A,B}W_{AB}
=
\frac{E_*+\kappa I_0}{E_\ell}
```

となる。$W_{AB}/Z_{a,b}$ を計算すれば共同法則を得る。
<!-- theorem-end:proof -->

局所有限幅パルスが伝達作用や結果領域を $O(\epsilon)$ だけ変える場合、上の共同法則にも一般に $O(\epsilon)$ の補正が入る。定理の厳密式は、理想局所写像または有限幅でも同じ $I_-^{AB}$ を実現する較正済み装置を仮定した結果である。

## 初期時計向き余裕 <i>E</i><sub>∗</sub>

$E_*=0$ では

```math
V_{\rm eff}=V
```

であり、理想位相同期 $V=1$ なら単位可視度の余弦則を得る。しかし $\Delta_{ab}=0$ かつ $AB=+1$ の結果領域では、しきい値と終端整合体積が零になる。

$E_*>0$ は相補時計の正向き領域内で、向き反転までの初期運動量余裕を与える。同時に全結果領域へ正の整合性下限を与える。その代わり可視度は

```math
V_{\rm eff}
=
\frac{\kappa I_0}{E_*+\kappa I_0}V
<
V
```

へ低下する。したがって $E_*$ は、時計向きの頑健性と Bell 可視度の交換関係を表す。

## 微視的事後分布と測定設定独立性

Bell に関係する未読変数を $(A,B,h)$ に限定し、他の生成源変数が測定設定と独立に因子化するとする。`[R]` 後の密度は

```math
\rho_R(A,B,h\mid a,b)
=
\frac1{
4(E_*+\kappa I_0)
}
\mathbf1_{\{
0\leq h\leq x_{AB}(a,b)
\}},
```

```math
x_{AB}(a,b)
=
E_*+\kappa I_0
\left[
1-ABV\cos\Delta_{ab}
\right]
```

である。測定設定を変えると各結果領域の台の上端が変わるため、

```math
\rho_R(\lambda\mid a,b)
\neq
\rho_R(\lambda\mid a',b')
```

が一般に成り立つ。

Bell--CHSH の標準導出では、4つの測定設定対に同じ $\rho(\lambda)$ を用いる。本構成で外れる仮定は測定設定独立性であり、固定した完全微視状態における局所応答の因子化ではない [9,10,24,25]。

2つの測定設定対に対応する

```math
c=\cos\Delta_{ab},
\qquad
c'=\cos\Delta_{a'b'}
```

の間の全変動距離は、上の最小事後分布について

```math
D_{\rm TV}(c,c')
=
\frac{V_{\rm eff}}2
|c-c'|
```

である。追加の未読変数が測定設定と独立に因子化する場合、この値は完全事後分布に対しても正確である。

## 測定設定頻度

制御器の基準分布を $P_S(a,b)$ とする。`[R]` を制御器まで含む全履歴集団へ適用すると、

```math
P_R(a,b)
\propto
P_S(a,b)Z_{a,b}.
```

第7.4節で

```math
Z_{a,b}
=
\frac{E_*+\kappa I_0}{E_\ell}
```

は測定設定に依存しない。したがって

```math
P_R(a,b)=P_S(a,b).
```

巨視的な制御器頻度を保ちながら、その設定巨視状態と終端条件の両方に整合する微視的生成源事後分布は変化する。この意味で本構成は、未来入力依存または2境界条件付きのモデルに属する [7,8,21--23]。

## 非信号性と相関

共同法則の一側周辺は

```math
P_R(A\mid a,b)
=
\sum_{B=\pm1}
P_R(A,B\mid a,b)
=
\frac12,
```

```math
P_R(B\mid a,b)
=
\frac12
```

である。したがって `[S]` の対称集団では操作上の非信号性が成立する。これは微視的な測定設定独立性が回復したことを意味しない。遠隔設定依存性は未読事後分布に残るが、結果符号対称性により一側周辺で相殺される。

相関は

```math
E(a,b)
=
\sum_{A,B}
ABP_R(A,B\mid a,b)
=
-V_{\rm eff}\cos\Delta_{ab}
```

である。標準 CHSH 角

```math
\phi(a_0)=0,
\qquad
\phi(a_1)=\frac\pi2,
```

```math
\phi(b_0)=\frac\pi4,
\qquad
\phi(b_1)=-\frac\pi4
```

では

```math
|\mathcal S|
=
2\sqrt2V_{\rm eff}.
```

したがって $V_{\rm eff}>1/\sqrt2$ なら CHSH 不等式を破る。

## Bell 前提の一覧

本構成の Bell 前提を次のように分類する。

- 結果の確定性：満たす。各履歴は1つの固定指針領域を持つ。
- 局所決定論応答：完全な微視状態上で満たす。
- 固定微視状態での遠隔設定非依存性：局所記録時刻について満たす。
- 共通の測定設定独立分布：満たさない。
- 操作上の測定設定頻度：$Z_{a,b}$ が一定なので保つ。
- 対称準備での非信号性：`[S]` の下で満たす。
- 任意準備での非信号性：証明していない。
- 観測済みデータの事後選別がないこと：物理的実装条件として別に要求する。

したがって本論文は Bell の定理を否定しない。Bell 不等式を破る共同確率と、そのために外れた前提を同じモデルの中で示す。

## 後段時間は結果重みを作らない

局所結果が確定した後、全試行を結果に関係なく1回ずつ数えるなら、比較器への到達時間、後段反応座標の滞在時間、有限浴へのエネルギー移動は、試行番号で数えた結果比率を変えない。変化し得るのは時刻占有率または有限期限までの完了率である。

結果依存の未完了試行や時間切れ試行を除けば、事後選別が生じる。本論文の $W_{AB}$ は通過流束や完了率ではなく、`[R]` が物理的集団とする終端整合位相体積である。共有浴と待ち時間を含む一般的な否定結果は第8.3節と付録C.11にまとめる。

## 本章の結論

比較窓を1本の有限 Hamiltonian として書き、内部時計の自由運動により $Y_R$ が変化しても

```math
\Pi_R(T)
=
E_*+\kappa I_- -h
```

が厳密に成り立つことを示した。固定終端条件は順序付き時計向きの保存と同値であり、同時に $h$ の下位体積を測る。

2モード作用分配系の一様密度、対称準備、`[R]` を用いると Bell 型余弦共同確率を得る。確率重みの原理は `[R]` であり、時計相補性や順時間的待ち時間ではない。Bell の前提違反は測定設定独立性に位置し、巨視的な測定設定頻度と対称準備での非信号性は保たれる。

# 適用範囲、否定結果、反証条件

> **位置づけ：** 導出済み、条件付き、未導出、否定結果を分離し、モデルを区別する観測量を示す。


## 現在の到達点

本論文の証明状態を要約する。

| 項目 | 状態 |
|---|---|
| 第I部の粗視化作用形式の $C^1$ 収束 | 指定した線形 Gaussian クラスで証明済み |
| 微視的 Hamiltonian 運動による Nelson 停留点の選択 | 未導出 |
| 局所結果符号化器 | Hamiltonian 部品として構成。一般パルスは短時間極限 |
| 有限幅の終端比較読出し | 第7.1節の比較窓 Hamiltonian について厳密 |
| 2モード作用分配系の $p(h)=1/E_\ell$ | 固定総作用殻の Liouville 測度について厳密 |
| Bell 型共同確率 | `[H,P,S,M,R]` と適用範囲の下で成立 |
| `[R]` の Hamiltonian 力学からの導出 | 未達 |
| 対称準備での非信号性 | `[S]` の下で成立 |
| 任意の偏った準備での非信号性 | 未証明 |

第II部は「閉じた Hamiltonian 方程式の順時間発展だけが Bell 型確率を生成した」という結果ではない。Hamiltonian 装置、準備測度、2境界履歴測度の役割を分けた条件付き構成である。

## `[R]` の物理的地位

有限閉鎖 Hamiltonian 系は再帰を持ち得る。時間反転可能な方程式は終端境界条件を数学的に許す。しかし、有限性、再帰性、時間反転対称性を合わせただけでは

```math
d\mu_R
\propto
\rho_S
G_R\circ\Phi^T
d\Gamma
```

を物理的確率法則として一意に選ぶことはできない。`[R]` は、本構成を通常の初期値統計力学から区別する独立原理である。

相補的内部時計はこの区別を明確にする。$\Pi_R(T)\geq0$ は、初期に選んだ時計向きの順序が終端まで保存された条件として導ける。しかし $\Pi_R(T)<0$ の軌道も Hamiltonian 解であり、時計向きが交換されるだけである。したがって時計相補性は $G_R$ の半空間を説明するが、$G_R$ を履歴確率へ変換しない。

初期境界密度 $\rho_S(z_i)$ と終端関数 $G_{\rm or}(z_f)$ を同一 Hamiltonian 履歴として照合する規則を追加すれば、

```math
d\nu
\propto
\rho_S(z_i)
G_{\rm or}(z_f)
\delta
\left(
z_f-\Phi_{a,b}^{T}z_i
\right)
d\Gamma_i\,d\Gamma_f
```

から `[R]` の積形式を得る。ただし2つの境界密度を掛けて照合する規則自体が、追加の全履歴統計原理である。

同じ読出し $\Pi_R(T)=x-h$ に対し、2つの相補的半空間を等重みで平均すると

```math
\frac12
\left[
\frac{x}{E_\ell}
+
1-\frac{x}{E_\ell}
\right]
=
\frac12
```

となり、差動作用の余弦項は消える。無向きの時計相補性だけでは Bell 重みを保てない。

## 順時間的共有浴と待ち時間の否定結果

局所記録時刻 $t_m$ で、位相空間を4つの互いに交わらない記録領域

```math
\Gamma_{AB}(t_m)
```

に分ける。$t>t_m$ の共有浴を含む Hamiltonian 流れを $\Phi^{t-t_m}$ とする。Liouville 測度 $\mu$ に対して

```math
\mu
\left[
\Phi^{t-t_m}\Gamma_{AB}(t_m)
\right]
=
\mu
\left[
\Gamma_{AB}(t_m)
\right]
```

である。Hamiltonian 流れが全単射で位相体積を保存するからである。

したがって記録形成後に左右の写しを共有浴へ結合しても、全試行を1回ずつ数える結果領域の質量は変わらない。結果に依存する後段時間についても同じである。$n$ 番目の試行の結果を $\kappa_n=(A_n,B_n)$、有限の完了時間を $\tau_n$ とすると、全試行を数える頻度

```math
\frac1N
\sum_{n=1}^{N}
\mathbf1_{\{\kappa_n=(A,B)\}}
```

は $\tau_n$ に依存しない。

共有浴や待ち時間が変え得るのは、浴状態との相関、時刻占有率、有限期限までの完了率である。結果に依存する時間切れまたは未完了試行を除外すれば、観測分布は再重みづけされるが、それは事後選別である。

したがって、順時間的な共有浴雑音の漏れ、結果依存滞在時間、反応座標の通過速度は、それだけでは `[R]` の代わりにならない。

## `[S]` と偏った準備

一般の基準結果重みを $w_{AB}$ とすると、

```math
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
```

```math
C=E_*+\kappa I_0,
\qquad
K=\kappa I_0V,
\qquad
c=\cos\Delta_{ab}.
```

同時符号反転対称性

```math
w_{++}=w_{--},
\qquad
w_{+-}=w_{-+}
```

があれば一側結果周辺は $1/2$ に保たれる。しかし偶奇領域の基準質量が異なると、全整合体積

```math
Z_{a,b}
=
C
-Kc
\sum_{A,B}ABw_{AB}
```

が測定設定に依存し得る。結果周辺と設定頻度の両方を最も単純に保つ条件は $w_{AB}=1/4$ である。

例えば B 側の結果種を $B=+1$ に限定した準備が操作可能なら、

```math
P_R(A=+1\mid a,b,B=+1)
=
\frac12
\left[
1-V_{\rm eff}\cos\Delta_{ab}
\right]
```

となり、A 側周辺は B 側の測定設定に依存する。したがって `[S]` の非信号性は平衡的な対称準備についての結果であり、任意準備についての定理ではない。

## 2モード作用分配系の頑健性

一様密度からのずれを

```math
p(h)
=
\frac1{E_\ell}
\left[
1+\varepsilon r(h)
\right],
\qquad
\int_0^{E_\ell}r(h)dh=0
```

と書くと、累積整合重みは

```math
F(x)
=
\frac{x}{E_\ell}
+
\frac{\varepsilon}{E_\ell}
\int_0^x r(h)dh
```

となる。$x=C-ABK\cos\Delta$ を代入したとき、第2項は一般に高次調波を生む。

ソフトモードが $N$ 個の残余作用モードと総エネルギーを共有する場合には、

```math
F_N(x)
=
1-
\left(
1-\frac{x}{E_\ell}
\right)^N
```

であり、$N>1$ では線形でない。したがって不完全混合、総作用の漏れ、追加の残余作用モードは、可視度低下だけでなく高次調波として現れ得る。

## 終端幅と切断端

理想終端関数

```math
G_R
=
\mathbf1_{\{\Pi_R\geq0\}}
```

を幅 $\epsilon_R$ の滑らかな応答 $g_{\epsilon_R}$ へ置き換えると、

```math
F_{\epsilon_R}(x)
=
\int_0^{E_\ell}
\frac{dh}{E_\ell}
g_{\epsilon_R}(x-h)
```

となる。$x$ が $0$ と $E_\ell$ の両端から十分離れ、応答核が平行移動共変なら、主要項は $x/E_\ell$ である。両端へ近づくと切断補正が入り、零しきい値領域にも有限の背景重みが生じ得る。

## 追加反応座標に依存する帰結

終端比較器の後に、利用可能エネルギー

```math
x_{AB}
=
E_*+\kappa I_-^{AB}
```

で自由反応座標を距離 $\ell_g$ だけ進ませる追加設計を考える。質量を $M_g$ とすれば、

```math
\tau_g(x)
=
\ell_g
\sqrt{
\frac{M_g}{2x}
}.
```

$E_*>0$ なら完了時間に一様上界がつく一方、Bell 可視度は下がる。この同時変化は、自由反応座標を追加した特定の表示装置の帰結である。第II部の必須モデルから一般に従う予測ではなく、後段設計を採用した場合だけ検査できる。

## 余弦則と Tsirelson 限界

本構成が直接与えるのは、実2次元の等振幅伝達ベクトルと2次差動比較器による

```math
I_-
\propto
1-AB\cos\Delta
```

である。したがって

```math
|\mathcal S|
=
2\sqrt2V_{\rm eff}
\leq
2\sqrt2
```

は $0\leq V_{\rm eff}\leq1$ と、この比較器設計の帰結である。

一般の非負スカラー比較関数を許せば、異なる相関表を構成できる。本論文は、回転対称性、合成則、情報原理、Hamiltonian 安定性から2次比較器を一意に選ぶ定理を持たない。したがって Tsirelson 限界を独立な一般原理から導いたとは言えない。

## Wallstrom 問題

第I部の Nelson 表示から一般の Schrödinger 理論を再構成するには、配置空間の閉路に沿う位相循環を量子化する必要があり、Wallstrom 問題が残る [20]。

第II部の余弦は、伝達ベクトルの内積

```math
u_A\cdot u_B
\propto
\cos\Delta_{ab}
```

から生じる。これは Bell 実験の設定差に対する共同確率を与えるが、配置空間位相 $S(x)$ の閉路条件

```math
\oint\nabla S\cdot d\ell
\in
2\pi\hbar\mathbb Z
```

を導かない。したがって Bell 型余弦共同確率は Wallstrom 問題を解かない。

## 反証に使える観測量

モデルを区別する主要な観測量は次である。

1. 比較パルス前後の $I_-$、$h$、$\Pi_R$ を測り、2つの作用保存と読出し誤差を検査する。
2. ソフトモードエネルギーの累積分布と Bell 角依存性の高次調波を測り、2モード作用分配系からのずれを検査する。
3. 偏った結果種準備で非信号性残差を測り、`[S]` の適用範囲を検査する。
4. 開始数、指針記録数、終端完了数を分け、結果依存の欠測と事後選別を検査する。
5. 局所パルス幅を変え、結果符号、伝達作用、Bell 共同確率の補正が $O(\epsilon)$ で減るかを検査する。

具体的な数値手順、誤差指標、再現命令は付録C.12、付録E、`VALIDATION.md` に置く。

## 残る課題

最重要の未解決問題は次である。

1. `[R]` の2境界照合規則を、より大きな閉じた境界値理論から導けるか。
2. 設定と到来変数から結果を生成する一般の局所 Hamiltonian 測定相互作用を構成できるか。
3. 全装置部品と全自由発展を1本の有限 Hamiltonian に統合し、有限幅誤差を一様に評価できるか。
4. 有限非線形混合器の混合時間、再帰時間、総作用漏れを定量化できるか。
5. 偏った準備装置まで含めた2境界問題が非信号性を回復するか。
6. 2次比較器と Tsirelson 限界を追加原理から選べるか。
7. Nelson 位相と生成源の作用角位相を結び、Wallstrom 量子化へ進めるか。

## 最終結論

第I部で確立したのは、指定した線形 Gaussian 確率表示に対する、繰り込み済み粗視化作用形式の定量的パラメータ $C^1$ 収束である。これは微視的 Hamiltonian 運動による Nelson 停留点選択の導出ではない。

第II部では、局所結果符号化器、実2次元差動比較器、2モード作用分配系、相補的内部時計を有限 Hamiltonian 部品として接続した。終端比較器は、内部時計の自由運動を含む有限幅 Hamiltonian でも

```math
\Pi_R(T)
=
E_*+\kappa I_- -h
```

を厳密に読出す。対称準備と `[R]` を追加すると Bell 型余弦共同確率が得られ、Bell の前提違反は測定設定独立性に現れる。

一方、`[R]` は Hamilton 方程式から導かれておらず、局所装置も一般測定相互作用には達していない。したがって現在の到達点は、Bell 型確率構造の完全な力学的導出ではなく、力学的に実現した部分と独立な統計入力の境界を明示した条件付き構成である。

# 付録

# Fourier--Gaussian 近似と Schur 補完の評価

> **位置づけ：** 第3章と第4章で用いた有限モード収束と条件づけの安定性を補足する。


## 基本核の Fourier 係数

線形方程式の雑音応答核を

```math
G_\theta(t,s)
=
\mathbf 1_{0\leq s\leq t}
\Phi_\theta(t,s)
```

とする。$s=t$ に跳びがあるため、$s$ に関する Fourier 係数は一般に $O(n^{-1})$ である。

<!-- theorem-start:lemma -->
**補題（一様 Fourier 尾部）**
$F_\theta$ が第4.2節の仮定を満たすなら、ある $C_K$ が存在して

```math
\sup_{\theta\in K,\,t\in[0,T]}
\|\widehat G_{\theta,n}(t)\|
\leq
\frac{C_KT}{1+|n|},
```

```math
\sup_{\theta\in K,\,t\in[0,T]}
\|D_\theta\widehat G_{\theta,n}(t)\|
\leq
\frac{C_KT}{1+|n|}
```

が成立する。従って共分散尾部は

```math
\sup_{\theta,s,t}
\left(
\|C_N(s,t)-C(s,t)\|
+\|D_\theta C_N(s,t)-D_\theta C(s,t)\|
\right)
\leq
\frac{C_KT^2}{N}
```

である。
<!-- theorem-end:lemma -->

<!-- theorem-start:proof -->
**証明**
$n\neq0$ に対して $e^{-i\omega_ns}$ を部分積分する。区間端と $s=t$ の跳びから $1/\omega_n$ の境界項が生じ、区間内部では $\partial_s\Phi(t,s)=-\Phi(t,s)F(s)$ が一様有界である。従って $|\widehat G_n|\leq C/|\omega_n|$ を得る。

$\theta$ 微分については

```math
D\Phi_\theta[\delta F](t,s)
=
\int_s^t
\Phi_\theta(t,r)
\delta F(r)
\Phi_\theta(r,s)
\,\mathrm{d} r
```

を使う。$D\Phi$ とその $s$ 微分も一様有界なので同じ部分積分評価が成立する。共分散は Fourier 係数の積の和であり、

```math
\sum_{|n|>N}\frac1{n^2}\leq\frac{C}{N}
```

から結論を得る。
<!-- theorem-end:proof -->

## 平均の収束

本論文では $F_\theta$、$f_\theta$、初期平均は $N$ に依存しないため、無条件平均は $\mu_N=\mu$ である。浴切断に依存する補正平均を許す場合でも、Fourier 尾部が中心化されていれば平均差は零であり、非零の決定論的尾部を加えた場合はその $L^1$ ノルムで直接評価できる。

条件付き平均は $C_N(t,T)$ と $C_N(T,T)$ に依存するため、共分散尾部から $O(1/N)$ の差を持つ。

## Schur 補完の安定性

$S_N=HC_N(T,T)H^{\mathsf T}+R$、$S=HC(T,T)H^{\mathsf T}+R$ とする。$R\geq r_*I$ なので

```math
\|S_N^{-1}\|\leq r_*^{-1},
\qquad
\|S^{-1}\|\leq r_*^{-1}.
```

逆行列恒等式

```math
S_N^{-1}-S^{-1}
=
S_N^{-1}(S-S_N)S^{-1}
```

から

```math
\|S_N^{-1}-S^{-1}\|
\leq
r_*^{-2}\|S_N-S\|
```

を得る。従って条件付き共分散について

```math
\sup_{s,t,\theta}
\|C_N^R(s,t)-C^R(s,t)\|
\leq
\frac{C_KT^2}{N}
```

である。

第1微分では

```math
D(S^{-1})=-S^{-1}(DS)S^{-1}
```

を用いる。$S_N^{-1}$、$DS_N$ が一様有界なので、積の各因子を1つずつ差し替えることで

```math
\sup_{s,t,\theta}
\|D C_N^R(s,t)-D C^R(s,t)\|
\leq
\frac{C_KT^2}{N}
```

を得る。条件付き平均も同様である。

## 有限分解能の役割

$R>0$ は、観測値 $y$ の周囲に有限幅の終端領域を持たせる。これにより、条件付き共分散は $T$ で完全には消えず、条件付き流れの係数は閉区間 $[0,T]$ 上で有界に保たれる。

$R\downarrow0$ とすると、完全観測された方向の終端共分散は零へ近づく。自由拡散では前進条件付き流れに

```math
\frac{y-x}{T-t}
```

型の項が現れる。点終端での定理を得るには、$t=T$ の境界層を除いた区間で先に $N\to\infty$、$h\to0$ を取り、その後に境界層と $R\downarrow0$ を別に評価する必要がある。

## 自由終端固定と零周波数

自由系では

```math
X_N(T)-X_N(0)
=
\int_0^T\widetilde\eta_N(t)\,\mathrm{d} t
=
\sqrt{2\nu T}\,Z_0.
```

従って $X_N(T)=X_N(0)$ は $Z_0=0$ と同値である。非零モードは終端条件と独立なので、条件付き共分散から零モードの寄与 $2\nu/T$ だけが除かれる。この計算は、旧来の $-1/T$ が浴の基本性質ではなく、自由終端固定の結果であることを最も直接に示す。

## 一般線形系では全モードが条件づけられる

$F\neq0$ では

```math
X_N(T)
=
\Phi(T,0)X_N(0)
+\sum_\alpha K_{N,\alpha}(T)\zeta_\alpha
+d_N(T)
```

である。ここで $d_N(T)$ は決定論項であり、一般に $K_{N,\alpha}(T)\neq0$ である。終端記録は零周波数だけでなく全ての Fourier 係数の線形結合を拘束する。そのため条件付き雑音共分散の修正は階数有限の Schur 項となり、流れ $F$、観測 $H$、分解能 $R$ に依存する。

# 粗視化作用の <i>C</i><sup>1</sup> 評価

> **位置づけ：** 時間粗視化誤差と Fourier 切断誤差を分離し、主定理の評価を補足する。


## Gaussian 増分の正確な表示

条件付き Gaussian 過程の増分 $\Delta_hX(t)=X(t+h)-X(t)$ に対して

```math
\mathbb{E}^R|\Delta_hX(t)|^2
=
|\mu^R(t+h)-\mu^R(t)|^2
+\operatorname{tr}\left[
C^R(t+h,t+h)+C^R(t,t)-2C^R(t+h,t)
\right]
```

が厳密に成立する。従って粗視化作用の運動項は、条件付き平均と共分散だけで計算できる。

有限 $N$ でも同じ式が成立する。$C_N^R-C^R=O(1/N)$ なので、増分2乗の有限モード誤差は粗い評価で $O(1/N)$、$h^{-2}$ を掛けた作用誤差は $O(1/(Nh^2))$ となる。

## 時間対角の展開

極限拡散について、$X_t=x$ を固定した短時間増分は

```math
\Delta_hX
=
b_+^R(x,t)h
+\sqrt{2\nu}\Delta_hW
+O_{L^2}(h^{3/2})
```

である。流れの空間依存と雑音の相関による交差項まで含めて平均すると

```math
\mathbb{E}^R
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
```

線形流れでは3階剰余を平均・微分した量も一様に有界である。$m/(2h^2)$ を掛けると

```math
\frac m{2h^2}\mathbb{E}^R|\Delta_hX|^2
-\frac{md\nu}{h}
=
\mathbb{E}^R
\left[
\frac m2|b_+^R|^2
+m\nu\nabla\cdot b_+^R
\right]
+O(h).
```

積分上端を $T-h$ で止めたことによる欠落も $O(h)$ である。

## なぜ発散項が残るか

雑音の主要項 $2d\nu h$ だけを差し引いても、流れと短時間雑音の交差効果は $h^2$ の有限項として残る。それが

```math
m\nu\nabla\cdot b_+^R
```

である。この項を落とすと、極限は正しい Guerra--Morato 作用にならず、Nelson 表示の負の Fisher 項も得られない。

## Fourier 切断誤差

付録Aの評価から

```math
\|C_N^R-C^R\|_{C^1(K;C([0,T]^2))}
\leq
\frac{C_KT^2}{N}
```

である。増分共分散は4つの共分散値の線形結合なので、

```math
\left|
\mathbb{E}_N^R|\Delta_hX_N|^2
-
\mathbb{E}^R|\Delta_hX|^2
\right|_{C^1(K)}
\leq
\frac{C_KT^2}{N}.
```

従って運動項の差は

```math
\frac{C_KT^2}{Nh^2}
```

で抑えられる。この評価は最適とは限らないが、$N(h/T)^2\to\infty$ という単純な対角極限を与える。

## 2次ポテンシャル

$U(x,t)=x^{\mathsf T}K(t)x/2+\ell(t)^{\mathsf T}x+c(t)$ なら

```math
\mathbb{E}^R[U(X_t,t)]
=
\frac12\mu^R(t)^{\mathsf T}K(t)\mu^R(t)
+\frac12\operatorname{tr}[K(t)C^R(t,t)]
+\ell(t)^{\mathsf T}\mu^R(t)
+c(t).
```

従ってポテンシャル期待値とそのパラメータ第1微分は、$\mu_N^R$ と $C_N^R$ の $O(1/N)$ 収束から直接従う。これは運動項の $O(1/(Nh^2))$ より小さく、主定理の右辺へ吸収できる。

一般の滑らかな非2次ポテンシャルでは、Gaussian モーメント展開または一様可積分性を用いて同様の結果を拡張できる可能性がある。しかし第1微分には解写像の応答と $\nabla U$ の積が現れるため、本論文では証明が閉じる2次範囲に限定する。

## パラメータ第1微分

作用を $\theta_j$ で微分すると、平均、共分散、条件付き Schur 項、ポテンシャル係数の微分が現れる。基本行列の微分公式と $R\geq r_*I$ により、全ての係数は $K$ 上で一様有界である。

時間対角展開を微分した剰余も $O(h)$、Fourier 尾部を微分した誤差も $O(T^2/(Nh^2))$ である。有限個の $\theta_j$ について最大を取れば

```math
\|\mathcal A_{N,h}^{R,U}-\mathcal A_{\mathrm{GM}}^{R,U}\|_{C^1(K)}
\leq
C_K
\left(
\frac hT+\frac{T^2}{Nh^2}
\right)
```

を得る。

## 対角尺度の選択

$h/T=N^{-\alpha}$ と置くと、2つの誤差は

```math
N^{-\alpha},
\qquad
N^{2\alpha-1}
```

である。両者を同じ次数にするには $\alpha=1/3$ とすればよい。従って

```math
h_N=TN^{-1/3},
\qquad
\varepsilon_N=O(N^{-1/3})
```

となる。ここで $\varepsilon_N$ は全評価誤差を表す。

この選択は、粗視化窓を短くしすぎると未解像の Fourier 尾部が増幅され、長くしすぎると局所 Nelson 作用から外れる、という物理的な釣り合いを表す。

# Hamiltonian 装置部品、2モード位相体積、補正項

> **位置づけ：** 第II部の理想正準写像、有限幅誤差、厳密な比較窓、作用殻測度、多モード補正を計算する。


本付録が与えるのは、装置を構成する有限 Hamiltonian 部品と、その正準計算である。生成源、設定制御器、全自由発展を含む1本の完全な実験 Hamiltonian が、全ての理想写像を有限時間で誤差なく実行するとは主張しない。一般の局所パルスは短時間極限で理想写像へ近づき、第7.1節の比較読出しだけは、保存量との交換関係により有限幅でも厳密である。

## Poisson 構造

各正準対 $(q_j,p_j)$ に

```math
\{q_j,p_k\}
=
\delta_{jk}
```

を置く。伝達ベクトル $u=(Q,P)^{\mathsf T}$ と作用

```math
I=\frac12(Q^2+P^2)
```

に対し、生成子

```math
K_{\rm rot}
=
-\theta I
```

の単位流れは

```math
\dot Q=-\theta P,
\qquad
\dot P=\theta Q
```

なので

```math
u(1)
=
R(\theta)u(0).
```

$\theta=\phi(a)+\pi\chi_-(s)$ とし、結果種の平坦領域上で $A=\sigma(s)$ とすれば

```math
R
\left[
\phi(a)+\pi\chi_-(s)
\right]
=
A R[\phi(a)].
```

したがって結果符号を伝達ベクトル位相の $\pi$ 移動として正準的に記録できる。

## 応答モードと固定指針の移動

応答モード対 $(x,p)$ に対する生成子

```math
K_{\rm br}
=
-x\sigma(s)
```

は

```math
\dot p
=
-\frac{\partial K_{\rm br}}{\partial x}
=
\sigma(s),
```

```math
\dot x
=
\frac{\partial K_{\rm br}}{\partial p}
=
0
```

を与える。$p(0)=0$ なら $p(1)=A$ である。

固定指針対 $(Y,\Pi)$ に対する

```math
K_{\rm lock}
=
-Y\zeta(p)
```

は

```math
\dot\Pi
=
-\frac{\partial K_{\rm lock}}{\partial Y}
=
\zeta(p),
```

```math
\dot Y=0,
\qquad
\dot p=0
```

を与える。$\zeta(\pm1)=\pm1$ の平坦領域で $\Pi(0)=0$ なら、

```math
\Pi(1)=A.
```

2つの写像は Hamiltonian 流れなので位相体積を保存する。応答モードの情報を局所浴へ分散した後も、固定指針対を切り離せば比較窓の記録符号は保たれる。

## 自律順序時計と有限幅誤差

時計対 $(\vartheta,J_c)$ と、互いに重ならないパルス形 $f_{\nu,\epsilon}(\vartheta)$ を用い、

```math
H
=
\Omega J_c
+H_0
+\Omega
\sum_\nu
f_{\nu,\epsilon}(\vartheta)K_\nu
```

とする。$K_\nu$ と $H_0$ が $J_c$ に依存しないとき、

```math
\dot\vartheta=\Omega.
```

$f_{\nu,\epsilon}$ を

```math
\int_{\operatorname{supp}f_{\nu,\epsilon}}
f_{\nu,\epsilon}(\vartheta)d\vartheta=1
```

と規格化すれば、対応する時間区間で

```math
\int
\Omega f_{\nu,\epsilon}[\vartheta(t)]dt=1.
```

自由 Hamiltonian $H_0$ を無視すれば、この積分は $K_\nu$ の単位正準写像を与える。しかし全 Hamiltonian では $H_0$ も同時に働く。相互作用表示で Duhamel 展開を用いると、パルスの時間幅を $\epsilon_\nu$ として、有界な適用領域 $\mathcal K$ 上で

```math
\sup_{z\in\mathcal K}
\left\|
\Phi_{\rm full}^{(\nu)}(z)
-
e^{X_{K_\nu}}z
\right\|
\leq
C_{\mathcal K}\epsilon_\nu
```

となる。定数 $C_{\mathcal K}$ は、$\mathcal K$ 上の $X_{H_0}$、$X_{K_\nu}$、それらの第1微分の上界で決まる。したがって、本文の局所分析器と指針固定は短時間パルス極限の理想写像であり、有限幅では $O(\epsilon_\nu)$ の補正を持つ。

パルス形の台が重なる場合には、さらに Poisson 括弧 $\{K_\mu,K_\nu\}$ に比例する補正が生じる。本論文では台を分離し、この補正を使わない。第7.1節の比較読出しは、読出し対象の作用が全比較窓 Hamiltonian と交換するため、この一般誤差評価より強い厳密式を持つ。

## 相補的内部時計、2境界照合、向き平均の否定結果

まず、時計運動量を $\pm\varrho_0$ の極小へ固定するだけの Hamiltonian

```math
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
```

は用いない。極小

```math
\left(
\varrho_A,\varrho_B
\right)
=
\left(
+\varrho_0,-\varrho_0
\right)
```

では

```math
\dot\tau_X
=
\frac{\partial H_{\rm stop}}{\partial\varrho_X}
=
0
```

となり、向きは区別できても時計が進まないからである。

実際に相補的な時計運動を作る最小の二次 Hamiltonian として

```math
H_{\rm or}
=
\frac{\varrho_A^2+\varrho_B^2}{2M_\tau}
+
\frac{\kappa_c}{2}
\left(
\varrho_A+\varrho_B
\right)^2
```

を用いる。中心・相対変数を

```math
\bar\tau
=
\frac{\tau_A+\tau_B}{2},
\qquad
Y_R
=
\tau_A-\tau_B,
```

```math
P_c
=
\varrho_A+\varrho_B,
\qquad
\Pi_R
=
\frac{\varrho_A-\varrho_B}{2}
```

と定めると、

```math
\varrho_A\,d\tau_A
+
\varrho_B\,d\tau_B
=
P_c\,d\bar\tau
+
\Pi_R\,dY_R.
```

したがって変換は正準であり、

```math
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
```

$P_c=0$ 上では

```math
\varrho_A=\Pi_R,
\qquad
\varrho_B=-\Pi_R,
```

```math
\dot\tau_A
=
\frac{\Pi_R}{M_\tau},
\qquad
\dot\tau_B
=
-\frac{\Pi_R}{M_\tau}.
```

比較パルス直前に $\Pi_R=E_*>0$ を準備し、終端比較生成子を

```math
K_R
=
Y_R
\left(
h-\kappa I_-
\right)
```

とする。$K_R$ は $\bar\tau$ に依存しないので $P_c=0$ は保たれる。さらに

```math
\{h,K_R\}
=
\{I_-,K_R\}
=
0
```

なので、比較パルス中も $h$ と $I_-$ は保存される。相補時計の自由運動により

```math
\dot Y_R
=
\frac{2\Pi_R}{M_\tau}
```

であり、$Y_R$ は一般に動く。一方、規格化したパルス係数を $g_R(t)$ とすれば

```math
\dot\Pi_R
=
g_R(t)
\left(
\kappa I_- -h
\right),
\qquad
\int g_R(t)dt=1
```

である。したがって有限幅パルスでも厳密に

```math
\Delta\Pi_R
=
\kappa I_- -h,
```

```math
\Pi_R(T)
=
E_*+\kappa I_- -h.
```

したがって

```math
\Pi_R(T)\geq0
\quad\Longleftrightarrow\quad
\varrho_A(T)\geq0
\quad\land\quad
\varrho_B(T)\leq0.
```

終端半空間は、初期に選んだ時計向きの順序を保存した履歴の集合として得られる。一方、$\Pi_R(T)<0$ の軌道も正則な Hamiltonian 軌道であり、時計向きが交換されるだけである。

この半空間から `[R]` の積形式を得るには、さらに2境界の統計的照合を置く必要がある。初期境界の密度を $\rho_S(z_i)$、逆向き時計の時計過去に対応する終端関数を $G_{\rm or}(z_f)$ とし、両枝が同じ Hamiltonian 履歴を表す条件を

```math
\delta
\left(
z_f-\Phi_{a,b}^{T}z_i
\right)
```

で課す。履歴空間上の測度を

```math
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
```

とすれば、$z_f$ 積分により

```math
d\nu_i
=
\frac1{\mathcal Z}
\rho_S(z_i)
G_{\rm or}
\left(
\Phi_{a,b}^{T}z_i
\right)
d\Gamma_i.
```

これは `[R]` と同じ積形式である。Hamiltonian 流れの Jacobian が1であるため、逆向きに積分しても余分な密度因子は出ない。ただし2つの境界密度を掛けて照合する規則は、Hamilton 方程式とは別の全履歴統計原理である。

最後に、向きの順序を指定しない素朴な平均を考える。同じスカラー読出し

```math
\Pi_R(T)
=
x-h,
\qquad
x
=
E_*+\kappa I_-,
```

に対して正向き半空間を $\Pi_R(T)\geq0$、相補的半空間を $\Pi_R(T)\leq0$ とし、$0\leq x\leq E_\ell$ で一様な $h$ を積分すると、

```math
F_+(x)
=
\int_0^{E_\ell}
\frac{dh}{E_\ell}
\mathbf1_{\{h\leq x\}}
=
\frac{x}{E_\ell},
```

```math
F_-(x)
=
\int_0^{E_\ell}
\frac{dh}{E_\ell}
\mathbf1_{\{h\geq x\}}
=
1-\frac{x}{E_\ell}.
```

両者を等重みで足せば

```math
\frac12
\left[
F_+(x)+F_-(x)
\right]
=
\frac12
```

となり、$I_-$ の余弦依存性は消える。したがって $\varrho_A=-\varrho_B$ という無向きの相補性だけでは Bell 重みを保てない。順序付き境界領域を採るか、時間反転した領域では比較パルスの符号も反転する共変な追加構造が必要である。

## 差動モード作用

2つの伝達ベクトルを

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

とする。シンプレクティック分岐器

```math
u_+
=
\frac{u_A+u_B}{\sqrt2},
\qquad
u_-
=
\frac{u_A-u_B}{\sqrt2}
```

は総作用を保存する。

```math
\frac12\|u_A\|^2
+\frac12\|u_B\|^2
=
\frac12\|u_+\|^2
+\frac12\|u_-\|^2.
```

反対称出力の作用は

```math
\frac12\|u_-\|^2
=
\frac14\|u_A-u_B\|^2
=
I_-.
```

内積を展開して

```math
I_-
=
\frac14
\left[
r_A^2+r_B^2
-2ABr_Ar_B\cos\Delta_{ab}
\right]
```

を得る。この物理的な分岐写像を実行してから反対称出力の作用を比較器へ結合してもよく、同じ2次観測量へ直接結合してもよい。

## 有限幅の終端比較読出し

比較窓 Hamiltonian を

```math
H_{\rm win}
=
H_{\rm or}
+
\omega_-I_-
+
\omega_\ell(J_s+J_0)
+
\Omega J_c
+
\Omega f_R(\vartheta)
Y_R
\left(
h-\kappa I_-
\right)
```

とする。$f_R$ の台は他のパルスと交わらず、

```math
\int f_R(\vartheta)d\vartheta=1
```

と規格化する。$H_{\rm win}$ は $J_c$ へ線形なので

```math
\dot\vartheta=\Omega
```

である。差動作用とソフトモードのエネルギーについて、

```math
\dot I_-
=
\{I_-,H_{\rm win}\}
=
0,
```

```math
\dot h
=
\{h,H_{\rm win}\}
=
0
```

が厳密に成り立つ。比較パルスは対応する角変数を移動させるが、2つの作用を変えない。

終端比較対については

```math
\dot\Pi_R
=
\Omega f_R(\vartheta)
\left(
\kappa I_- -h
\right),
```

```math
\dot Y_R
=
\frac{2\Pi_R}{M_\tau}.
```

したがって $Y_R$ は一般にパルス中も動く。旧生成子 $F_R(Y_R)(h-\kappa I_-)$ に対して $Y_R=0$ を仮定する方法は、$H_{\rm or}$ との同時発展を無視していた。

修正後の線形生成子では $\dot\Pi_R$ が $Y_R$ に依存しない。$I_-$ と $h$ も定数なので、

```math
\Pi_R(T)-\Pi_R(t_R^-)
=
\left(
\kappa I_- -h
\right)
\int_{t_R^-}^{t_R^+}
\Omega f_R[\vartheta(t)]dt
=
\kappa I_- -h.
```

したがって $\Pi_R(t_R^-)=E_*$ なら

```math
\Pi_R(T)
=
E_*+\kappa I_- -h
```

が有限幅パルスで厳密に成り立つ。比較器は $I_-$ と $h$ を非破壊的に読み出すが、それらの角変数を不変に保つとは主張しない。

## 2モード作用殻の正規化

2つの作用・角変数対に対し、

```math
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
```

$J_0$ を積分すると

```math
\mathcal N(E_\ell)
=
\frac{(2\pi)^2}{\omega_\ell}
\int_0^{E_\ell/\omega_\ell}
dJ_s
=
\frac{(2\pi)^2E_\ell}{\omega_\ell^2}.
```

$h=\omega_\ell J_s$ の区間 $[h,h+dh]$ に入る作用殻測度は

```math
d\mathcal N_h
=
\frac{(2\pi)^2}{\omega_\ell^2}dh.
```

従って

```math
p_\ell(h)dh
=
\frac{d\mathcal N_h}{\mathcal N(E_\ell)}
=
\frac{dh}{E_\ell}.
```

同じ結果は、尺度を変えた Descartes 座標

```math
\frac1{\sqrt{2J_\ell}}
\left(
q_s,p_s,q_0,p_0
\right)
```

が3次元球面 $S^3$ 上にあることからも分かる。

```math
\frac{J_s}{J_\ell}
=
\frac{q_s^2+p_s^2}{
q_s^2+p_s^2+q_0^2+p_0^2
}
```

は Beta$(1,1)$、すなわち $[0,1]$ 上の一様分布である。

## 混合器生成子

次を定義する。

```math
J_x=q_sq_0+p_sp_0,
```

```math
J_y=q_sp_0-p_sq_0,
```

```math
J_z=\frac12
\left(
q_s^2+p_s^2-q_0^2-p_0^2
\right),
```

```math
J_\ell
=
\frac12
\left(
q_s^2+p_s^2+q_0^2+p_0^2
\right).
```

Poisson 括弧を直接計算すると、

```math
\{J_\ell,J_i\}=0,
\qquad
i=x,y,z.
```

また、規格化の取り方に応じた定数因子を除き、$J_x,J_y,J_z$ は $\mathfrak{su}(2)$ 型の閉じた括弧を持つ。したがって

```math
K_M
=
a_x(t)J_x+a_y(t)J_y+a_z(t)J_z
```

の各流れは $S^3$ 上の測度保存向き写像である。係数 $a_i(t)$ を有限非線形環境と自律時計から生成すれば、全系を Hamiltonian に保ったまま複雑な向き運動を作れる。

この事実は $p(h)$ の不変基準測度を保証するが、特定の決定論的係数列が混合を起こすことを自動的には保証しない。混合率は、相関減衰または転送作用素のスペクトルで別に検証する必要がある。

## 多モード単体の周辺分布

ソフトモードエネルギー $h$ と $N$ 個の残余作用エネルギー $e_1,\ldots,e_N$ が

```math
h+\sum_{j=1}^{N}e_j=E_\ell
```

を満たすとする。各調和対の位相角を積分すると定数になる。$h$ を固定した残余単体

```math
\sum_{j=1}^{N}e_j=E_\ell-h,
\qquad
e_j\geq0
```

の面上の重複度は

```math
\frac{(E_\ell-h)^{N-1}}{(N-1)!}
```

に比例する。規格化から

```math
p_N(h)
=
\frac{N}{E_\ell}
\left(
1-\frac h{E_\ell}
\right)^{N-1}.
```

累積分布は

```math
F_N(x)
=
1-
\left(
1-\frac x{E_\ell}
\right)^N.
```

$N=1$ でのみ線形である。$x=C-ABKc$ と書けば、

```math
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
```

偶数 $m$ は結果の偶奇に依存しない規格化補正、奇数 $m\geq3$ は $c^3,c^5,\ldots$ を通じて高次角度調波を生む。したがって追加の残余作用モードは単なる可視度の再規格化ではない。

## 有限終端幅

鋭い指示関数を単調応答 $g_\epsilon$ へ置き換える。

```math
G_{R,\epsilon}
=
g_\epsilon
\left(
E_*+\kappa I_- -h
\right).
```

一様なソフトモードエネルギー密度に対する整合重みは

```math
F_\epsilon(x)
=
\frac1{E_\ell}
\int_0^{E_\ell}
g_\epsilon(x-h)dh.
```

$g_\epsilon$ が Heaviside 関数と対称平滑化核の畳み込みなら、

```math
\frac{dF_\epsilon}{dx}
=
\frac1{E_\ell}
\left[
g_\epsilon(x)-g_\epsilon(x-E_\ell)
\right].
```

内部領域

```math
\epsilon\ll x\ll E_\ell-\epsilon
```

では $g_\epsilon(x)\approx1$、$g_\epsilon(x-E_\ell)\approx0$ なので、

```math
\frac{dF_\epsilon}{dx}
\approx
\frac1{E_\ell}.
```

両端近傍でのみ傾きと切片が変わる。したがって $E_*$ は零しきい値領域を境界層から離す一方、可視度を低下させる。

## 順時間的共有浴と待ち時間の否定結果

記録形成後の4領域を $\Gamma_{AB}$ とし、共有浴を含む後段流れを $\Psi^t$ とする。Liouville 測度に関して

```math
\mu(\Psi^t\Gamma_{AB})
=
\int_{\Psi^t\Gamma_{AB}}d\Gamma
=
\int_{\Gamma_{AB}}
\left|
\det D\Psi^t
\right|
d\Gamma.
```

Hamiltonian 流れでは

```math
\det D\Psi^t=1
```

なので

```math
\mu(\Psi^t\Gamma_{AB})
=
\mu(\Gamma_{AB}).
```

したがって共通未来の浴結合は、順時間的集団の結果領域質量を変えない。終端条件づけを加えると

```math
\mu_R(\Gamma_{AB})
\propto
\int_{\Gamma_{AB}}
G_R(\Psi^T z)
d\mu(z)
```

となり、結果領域質量は変わり得る。しかし変化を生むのは浴雑音の漏れそのものではなく、共通未来の流れと $G_R$ を組み合わせた境界再重みづけである。

同じ結論は後段の待ち時間にも成り立つ。$n$ 番目の試行の結果を $\kappa_n$、有限完了時間を $\tau_n$ とする。全試行を結果に関係なく1回ずつ数えるなら、

```math
\frac1N
\sum_{n=1}^{N}
\mathbf1_{\{\kappa_n=(A,B)\}}
```

は $\tau_n$ に依存しない。待ち時間は時刻占有率を変えるが、試行番号で数えた結果頻度を変えない。結果に依存する未完了試行または時間切れ試行を除外したときだけ観測頻度が変わり、その場合は事後選別である。

## 代数的整合性検査

実装の最小検査は次である。

1. 無作為な角と符号について、直接計算した $\|u_A-u_B\|^2/4$ と解析式 $I_-$ を比較する。
2. $S^3$ 上の等方 Gaussian ベクトルを規格化し、$J_s/J_\ell$ の経験累積分布と一様累積分布を比較する。
3. $Y_R$ を自由運動させた有限幅比較パルスを積分し、$I_-$ と $h$ の保存および $\Delta\Pi_R=\kappa I_- -h$ を検査する。
4. 終端半空間と相補時計の向き保存条件を検査する。
5. $h\leq E_*+\kappa I_-$ の指示関数を Monte Carlo 積分し、解析的な $W_{AB}$ と比較する。
6. 4つの結果を規格化し、一側周辺残差と CHSH 値を計算する。
7. $F_+(x)+F_-(x)=1$ を検査し、等重み向き平均で余弦項が消えることを確認する。
8. 追加の残余作用モードを加え、予測される $F_N(x)$ と高次調波を比較する。

これらは Hamiltonian 混合の証明ではない。幾何、規格化、標本化実装に循環または符号誤りがないことを確認する代数的検証である。

# Gaussian Nelson 方程式、Schrödinger 表示、OU 例

> **位置づけ：** 主定理の極限作用が与える物理像と、その適用範囲を具体例で示す。


## 連続の式を組み込んだ変分

Nelson 作用を

```math
\mathcal A_{\mathrm{N}}[\rho,v]
=
\int\rho
\left[
\frac m2|v|^2
-\frac{m\nu^2}{2}|\nabla\log\rho|^2
-U
\right]\,\mathrm{d} x\,\mathrm{d} t
```

とする。制約

```math
\partial_t\rho+\nabla\cdot(\rho v)=0
```

を Lagrange 乗数 $S$ で課す。$v$ について変分すると

```math
mv=\nabla S
```

を得る。$\rho$ について変分すると

```math
\partial_tS
+\frac{|\nabla S|^2}{2m}
+U
-2m\nu^2
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=0
```

となる。最後の項は密度勾配エネルギーの変分である。

## Schrödinger 表示

有効作用定数を

```math
\hbar_{\rm eff}=2m\nu
```

とし、

```math
\psi=\sqrt\rho
\exp\left(\frac{iS}{\hbar_{\rm eff}}\right)
```

と置く。連続の式と前節の Hamilton--Jacobi 型方程式を合わせると

```math
i\hbar_{\rm eff}\partial_t\psi
=
\left[
-\frac{\hbar_{\rm eff}^2}{2m}\Delta+U
\right]\psi
```

を得る [3--6]。

この変換は、$\rho>0$ で $v$ が局所的に勾配場となる領域では厳密である。しかし、多重連結領域の循環量子化、節を横切る位相接続、一般の重ね合わせ状態は追加条件を必要とする [20]。本論文の線形 Gaussian 定理は正の密度領域に限定され、この大域位相問題を解かない。

## 1次元 Gaussian 変分

平均 $q(t)$、標準偏差 $\sigma(t)>0$ の Gaussian 密度を考える。

```math
\rho(x,t)
=
\frac1{\sqrt{2\pi}\sigma}
\exp\left[-\frac{(x-q)^2}{2\sigma^2}\right].
```

連続の式を満たす最小の1次速度場は

```math
v=\dot q+\frac{\dot\sigma}{\sigma}(x-q),
```

浸透速度は

```math
u=-\nu\frac{x-q}{\sigma^2}
```

である。Gaussian 平均を取ると

```math
\mathbb{E}[v^2]=\dot q^2+\dot\sigma^2,
\qquad
\mathbb{E}[u^2]=\frac{\nu^2}{\sigma^2}.
```

調和ポテンシャル $U=m\Omega^2x^2/2$ では

```math
\mathbb{E}[U]=\frac{m\Omega^2}{2}(q^2+\sigma^2)
```

なので、第4.7節の有限次元作用を得る。

## 幅方程式の保存量

幅方程式

```math
\ddot\sigma+\Omega^2\sigma-\frac{\nu^2}{\sigma^3}=0
```

には

```math
E_\sigma
=
\frac12\dot\sigma^2
+\frac12\Omega^2\sigma^2
+\frac{\nu^2}{2\sigma^2}
```

という保存量がある。$\sigma\to0$ では最後の項が発散するため、正の初期幅は有限時間で零にならない。定常点 $\sigma_*^2=\nu/\Omega$ の周囲では幅が振動する。

この振る舞いは、通常の熱拡散が平衡へ単調緩和する像とは異なる。Nelson 作用では、確率流の運動項と密度勾配項が実時間の変分原理で釣り合い、可逆な幅運動を作る。

## 2次元 OU 位相モデル

計算例として

```math
\,\mathrm{d} Z_t
=
(-\lambda I+\Omega J)Z_t\,\mathrm{d} t
+\sqrt{2D}\,\,\mathrm{d} W_t,
\qquad
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
```

を考える [19]。$\lambda>0$ なら定常共分散は

```math
\operatorname{Cov}(Z)=\frac D\lambda I
```

である。$\Omega=0$ なら定常過程は詳細釣り合いを満たす。$\Omega\neq0$ では縮約された位相平面に定常回転流があり、通常の時間反転だけでは詳細釣り合いを満たさない。

このことは微視的 Hamiltonian 中核の可逆性と矛盾しない。$\lambda$ は消去した浴への有効緩和、$\Omega$ は残した調和回転を表す。OU モデルは観測部分系の計算表示であり、閉じた全系そのものではない。

## Itô と Stratonovich

一般に

```math
\,\mathrm{d} X=b(X,t)\,\mathrm{d} t+\sigma(X,t)\circ\,\mathrm{d} W_t
```

を Itô 表現へ変換すると、$\sigma$ の空間微分に比例する補正が流れへ加わる。本論文では $\sigma=\sqrt{2\nu}I$ が定数なので補正は零である。

従って線形 Gaussian 定理、Schur 補完、Guerra--Morato 作用、Nelson 表示のいずれも、Itô と Stratonovich の記法選択に依存しない。Stratonovich 微分は、乗法的雑音へ拡張するときに初めて本質的になる。

## Bell 部分との接続

2次元 Gaussian 位相変数は、第6章の実正準伝達ベクトルを具体化する候補になる。しかし、OU 定常分布だけでは左右の等振幅、共通生成時位相、4つの符号領域の対称性は自動的に保証されない。

従って

```math
\mathrm{OU}_{2D}
\quad\not\Rightarrow\quad
\mathrm{Bell\ cosine\ law}.
```

Bell 系論には、位相同期した生成源 `[P]`、対称準備 `[S]`、2モード入口測度 `[M]`、2境界履歴集団 `[R]` が別に必要である。この点を保つことで、Gaussian Nelson 部分と Bell 部分の役割が明確になる。

# 測定設定依存度、CHSH 4設定、事後選別監査

> **位置づけ：** 第II部の Bell 分類を定量化し、装置事後分布と表現論的最小値を区別する。


## Hall 尺度

測定設定に依存する未読変数分布に対する Hall の $L^1$ 尺度を

```math
M
=
\sup_{a,b,a',b'}
\int
\left|
\rho(\lambda\mid a,b)
-
\rho(\lambda\mid a',b')
\right|
d\lambda
```

とする。通常の全変動距離とは

```math
M=2D_{\rm TV}^{\max}
```

の関係にある。

第7.6節の最小2モード事後分布では、

```math
D_{\rm TV}(c,c')
=
\frac{V_{\rm eff}}2
|c-c'|
```

なので、

```math
M_{\rm dev}
=
V_{\rm eff}
\sup_{a,b,a',b'}
\left|
\cos\Delta_{ab}
-
\cos\Delta_{a'b'}
\right|.
```

全角度を許せば

```math
M_{\rm dev}=2V_{\rm eff}.
```

標準 CHSH の4測定設定対では余弦が $\pm1/\sqrt2$ なので、

```math
M_{\rm dev}^{(4)}
=
\sqrt2V_{\rm eff}.
```

これは本文の具体的な装置事後分布が持つ値であり、同じ観測共同法則を再現する全ての局所モデルの中で最小化した値ではない。

## 確率表を直接埋め込む表現

未読変数を

```math
\lambda_{\rm tab}
=
(A_*,B_*)
\in
\{\pm1\}^2
```

とし、

```math
\mathscr A(a,\lambda_{\rm tab})=A_*,
\qquad
\mathscr B(b,\lambda_{\rm tab})=B_*,
```

```math
\rho_{\rm tab}(A_*,B_*\mid a,b)
=
\frac14
\left[
1-A_*B_*V_{\rm eff}\cos\Delta_{ab}
\right]
```

と置けば、局所決定論的に目標共同法則を再現する。この表現は出力確率を未読変数へ直接書き込んだものであり、物理的説明ではない。

Hall 尺度は

```math
M_{\rm tab}
=
V_{\rm eff}
\sup_{a,b,a',b'}
\left|
\cos\Delta_{ab}
-
\cos\Delta_{a'b'}
\right|
```

である。したがって本文の2モード装置事後分布の粗視化周辺と同じ値を持つ。この一致は装置構成の最適性を意味せず、両者が同じ台の長さ変調を用いていることを示す。

## 標準 CHSH 4設定の最小値

標準 CHSH 4設定に対し、目標可視度 $V_{\rm eff}$ を再現する局所決定論的で操作上非信号な表現全体について、Hall 尺度を最小化した値を $M_{\min}^{(4)}(V_{\rm eff})$ とする。

$V_{\rm eff}\leq1/\sqrt2$ では全 CHSH 不等式が満たされる。Fine の定理により測定設定と独立な共同未読変数分布が存在するので [38]、

```math
M_{\min}^{(4)}(V_{\rm eff})
=
0,
\qquad
0\leq V_{\rm eff}\leq\frac1{\sqrt2}.
```

$V_{\rm eff}>1/\sqrt2$ では、Hall の緩和 CHSH 上界

```math
|\mathcal S|
\leq
2+\min\{3M,2\}
```

と

```math
|\mathcal S|
=
2\sqrt2V_{\rm eff}
```

から

```math
M_{\min}^{(4)}(V_{\rm eff})
\geq
\frac{
2\sqrt2V_{\rm eff}-2
}{3}
```

を得る [9]。

この下界は、$V_{\rm eff}=1/\sqrt2$ の測定設定独立 Fine モデルと、$V_{\rm eff}=1$ で下界を達成する Hall モデルを、測定設定と独立な補助符号で混合することで達成できる。したがって

```math
M_{\min}^{(4)}(V_{\rm eff})
=
\max
\left\{
0,
\frac{
2\sqrt2V_{\rm eff}-2
}{3}
\right\}.
```

特に $V_{\rm eff}=1$ では

```math
M_{\min}^{(4)}
=
\frac{
2(\sqrt2-1)
}{3},
```

一方、本文の装置事後分布は

```math
M_{\rm dev}^{(4)}=\sqrt2.
```

したがって明示装置は、測定設定依存度について最適ではない。

この最小値は4つの観測分布に対する表現論的な量である。有限 Hamiltonian 装置が同じ最小値を実現できることを意味しない。全角度の余弦族に対する、装置構造を固定した最小値も本論文では求めない。

## 測定設定頻度と生成源事後分布

制御器の事前分布を $P_S(a,b)$ とし、制御器まで含む全2境界測度を規格化すると、

```math
P_R(a,b)
=
\frac{
P_S(a,b)Z_{a,b}
}{
\sum_{a',b'}
P_S(a',b')Z_{a',b'}
}.
```

本文の対称モデルでは

```math
Z_{a,b}
=
\frac{E_*+\kappa I_0}{E_\ell}
```

が一定なので、

```math
P_R(a,b)=P_S(a,b).
```

したがって巨視的な測定設定頻度の自由と、微視的な生成源事後分布の測定設定依存性は両立する。これは測定設定独立性の破れと、実験者が制御器巨視状態を変えられないという主張を区別する。

## 開始数、記録数、完了数

各測定設定対について次の3つの数を区別する。

1. 外部生成源が開始した試行数 $N_{\rm launch}$。
2. 左右指針が確定結果を持った記録数 $N_{\rm rec}$。
3. 終端装置が完了巨視領域へ入った完了数 $N_R$。

`[R]` では、物理的に実現する試行自体が終端整合履歴であると解釈する。しかし実験室での実装が単に

```math
N_R<N_{\rm rec}
```

となる試行棄却を行うなら、観測標本は

```math
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
```

という検出条件付き分布になる。$\eta_{AB}$ は完了効率である。この場合、Bell 不等式の破れは検出の抜け穴で説明され得る。

物理的2境界モデルと事後選別を区別する最低条件は次である。

- 全開始数、記録数、完了数を測定設定ごとに報告する。
- 結果依存の欠測率を零または独立に有界化する。
- 終端装置の較正を Bell 実行より前に固定する。
- 時間切れ条件を変えても、予測される有限幅補正以外の共同法則変動がないことを確かめる。

## 偏った準備の検査

結果種の準備装置を追加し、基準結果重み $w_{AB}$ を操作する。本文モデルが任意準備に対して操作可能であるなら、次のいずれかを判定する必要がある。

1. $w_{AB}$ の操作が2境界整合性によって自動的に相殺される。
2. 偏った巨視状態が物理的に準備不能になる。
3. 非信号性残差が増大する。

非信号性残差を

```math
\epsilon_{\rm NS}
=
\max_{a,b,b',A}
\left|
P_R(A\mid a,b)
-P_R(A\mid a,b')
\right|
```

とする。理想 `[S]` 集団では $\epsilon_{\rm NS}=0$ である。偏った準備に対して $\epsilon_{\rm NS}=O(1)$ が現れれば、対称準備だけで成り立つモデルの操作上の限界が直接検出される。

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
- [19] G. E. Uhlenbeck and L. S. Ornstein, ``On the Theory of the Brownian Motion,'' Physical Review 36, 823--841 (1930). <https://doi.org/10.1103/PhysRev.36.823>
- [20] T. C. Wallstrom, ``Inequivalence between the Schrödinger Equation and the Madelung Hydrodynamic Equations,'' Physical Review A 49, 1613--1617 (1994). <https://doi.org/10.1103/PhysRevA.49.1613>
- [21] H. Price and K. Wharton, ``Bell Correlations as Selection Artefacts,'' arXiv:2309.10969v3 (2024). <https://arxiv.org/abs/2309.10969>
- [22] H. Price and K. Wharton, ``A Mechanism for Entanglement?,'' arXiv:2406.04571v1 (2024). <https://arxiv.org/abs/2406.04571>
- [23] N. Argaman, ``Bell's Theorem and the Causal Arrow of Time,'' American Journal of Physics 78, 1007--1013 (2010). <https://doi.org/10.1119/1.3456564>
- [24] S. Hossenfelder and T. Palmer, ``Rethinking Superdeterminism,'' Frontiers in Physics 8, 139 (2020). <https://doi.org/10.3389/fphy.2020.00139>
- [25] G. 't Hooft, The Cellular Automaton Interpretation of Quantum Mechanics, Springer (2016). <https://doi.org/10.1007/978-3-319-41285-6>
- [26] C. Léonard, ``A Survey of the Schrödinger Problem and Some of Its Connections with Optimal Transport,'' Discrete and Continuous Dynamical Systems A 34, 1533--1574 (2014). <https://doi.org/10.3934/dcds.2014.34.1533>
- [27] Y. Chen, T. T. Georgiou, and M. Pavon, ``On the Relation between Optimal Transport and Schrödinger Bridges: A Stochastic Control Viewpoint,'' Journal of Optimization Theory and Applications 169, 671--691 (2016). <https://doi.org/10.1007/s10957-015-0803-z>
- [28] H. E. Rauch, F. Tung, and C. T. Striebel, ``Maximum Likelihood Estimates of Linear Dynamic Systems,'' AIAA Journal 3, 1445--1450 (1965). <https://doi.org/10.2514/3.3166>
- [29] H. Waalkens, R. Schubert, and S. Wiggins, ``Wigner's Dynamical Transition State Theory in Phase Space: Classical and Quantum,'' Nonlinearity 21, R1--R118 (2008). <https://doi.org/10.1088/0951-7715/21/1/R01>
- [30] H. A. Kramers, ``Brownian Motion in a Field of Force and the Diffusion Model of Chemical Reactions,'' Physica 7, 284--304 (1940). <https://doi.org/10.1016/S0031-8914(40)90098-2>
- [31] D. Chandler, ``Statistical Mechanics of Isomerization Dynamics in Liquids and the Transition State Approximation,'' Journal of Chemical Physics 68, 2959--2970 (1978). <https://doi.org/10.1063/1.436049>
- [32] K. Sigman and W. Whitt, ``Marked Point Processes in Discrete Time,'' Queueing Systems 92, 47--81 (2019). <https://doi.org/10.1007/s11134-019-09612-3>
- [33] J. Fuchs, S. Goldt, and U. Seifert, ``Stochastic Thermodynamics of Resetting,'' Europhysics Letters 113, 60009 (2016). <https://doi.org/10.1209/0295-5075/113/60009>
- [34] M. R. Evans, S. N. Majumdar, and G. Schehr, ``Stochastic Resetting and Applications,'' Journal of Physics A: Mathematical and Theoretical 53, 193001 (2020). <https://doi.org/10.1088/1751-8121/ab7cfe>
- [35] J. Knorst and A. O. Lopes, ``On the Quantum Guerra--Morato Action Functional,'' Journal of Mathematical Physics 65, 082102 (2024). <https://doi.org/10.1063/5.0207422>
- [36] J. T. Wilson, V. Borovitskiy, A. Terenin, P. Mostowsky, and M. P. Deisenroth, ``Pathwise Conditioning of Gaussian Processes,'' Journal of Machine Learning Research 22, 1--47 (2021). <https://jmlr.org/papers/v22/20-1260.html>
- [37] C. Léonard, S. Rœlly, and J.-C. Zambrini, ``Reciprocal Processes. A Measure-Theoretical Point of View,'' Probability Surveys 11, 237--269 (2014). <https://doi.org/10.1214/13-PS220>
- [38] A. Fine, ``Hidden Variables, Joint Probability, and the Bell Inequalities,'' Physical Review Letters 48, 291--295 (1982). <https://doi.org/10.1103/PhysRevLett.48.291>
- [39] S. Asmussen, Applied Probability and Queues, 2nd ed., Springer, New York (2003). <https://doi.org/10.1007/b97236>
- [40] M. A. Marchiori and M. A. M. de Aguiar, ``Energy Dissipation Via Coupling With a Finite Chaotic Environment,'' Physical Review E 83, 061112 (2011). <https://doi.org/10.1103/PhysRevE.83.061112>
