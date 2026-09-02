@number: M
@chapter: 付録
@title: M51有限実正準担体の共通開放ray準備
@status: M51の単一試行実変数、採用開放方程式、seed測度の押出し、R171の有限時間率、切断後のR135輸送、M50への受渡し境界を証明する。

## M.1 目的と存在論

本付録は、量子状態に対応させる階数1統計を初期分布へ直接置かず、有限次元の実古典担体を開放driftで有限時間準備する共通模型M51を定義する。M51はQ1、Q2、Q3の同一ハードウェアを主張する模型ではない。各系列が同じ入出力契約を使えることだけを示す。

M51の記述階層は次の通りである。

| 階層 | M51での対象 | 因果的役割 |
|---|---|---|
| 単一試行の物理状態 | 実正準担体 $(Q,P)$、template正準対 $(Q^w,P^w)$、clock、port履歴 | 開放driftが直接作用し、切断面で下流へ渡る |
| 単一試行の派生座標 | $z=(Q+iP)/\sqrt{2\mathcal J_0}$、$w=(Q^w+iP^w)/\sqrt{2\mathcal J_0}$ | 実方程式を簡潔に表示する。追加の物理場ではない |
| 外部制御 | $g$、$\kappa$、$\lambda_{\rm prep}$、template設定 | pump、sink、port開閉を指定する |
| 集団統計 | $C_Z=\mathbb E[ZZ^\dagger]/\mathbb E[Z^\dagger Z]$、$c$、$\Pi_c$ | 準備結果を記述する。単一試行controllerへ書き戻さない |
| 下流の物理入力 | 各試行の $z(\omega)$ またはその正準SWAP先 | M50が作用容量を作る |
| 観測結果 | M51単独では存在しない | M50/R170が粒子位置と外部記録を作る |

templateの規格化方向 $c=w/\|w\|$ は、装置設定を表すと同時に準備後の統計因子をラベルする。同じ記号を使うのは両者を因果的に同一視するためではない。物理templateを設定し、その実変数から $c$ を計算し、開放流の押出し後に $C_Z\simeq cc^\dagger$ となる順序である。

## M.2 実正準担体と可逆生成子

$m$ 個の実正準対を列ベクトル $Q,P\in\mathbb R^m$ とする。派生複素座標を

```math
z=\frac{Q+iP}{\sqrt{2\mathcal J_0}}
```

と定める。Hermitian行列を

```math
G=A+iB,
\qquad
A^{\mathsf T}=A,
\qquad
B^{\mathsf T}=-B
```

と分解する。実Hamiltonian

```math
H_G
=
\frac{1}{2\mathcal J_0}
\left(Q^{\mathsf T}AQ+P^{\mathsf T}AP\right)
+\frac{1}{\mathcal J_0}P^{\mathsf T}BQ
```

は

```math
\dot Q
=
\frac{AP+BQ}{\mathcal J_0},
\qquad
\dot P
=
\frac{-AQ+BP}{\mathcal J_0}
```

を与え、複素表示では

```math
i\mathcal J_0\dot z=Gz
```

となる。従って有限次元の複素線形伝播は実正準担体の可逆運動として厳密に表せる。ただし、この代数的実現だけから、状態準備、Born型結果、粒子位置、局所性、熱力学的自然さは従わない。

$B=0$ なら $Q$ と $P$ の同じ実対称結合だけでよい。M37の位置ばね網は、さらに結合の局所性と正値性を課し、回転包絡に対して有限時間近似を与える制限された物理実現である。M51の一般 $H_G$ をM37の局所位置結合から導出済みとは扱わない。

## M.3 M51の開放方程式を実変数で書く

目標射影を

```math
\Pi_c=C+iD,
\qquad
C^{\mathsf T}=C,
\qquad
D^{\mathsf T}=-D
```

と書き、担体作用比を

```math
r
=
z^\dagger z
=
\frac{Q^{\mathsf T}Q+P^{\mathsf T}P}{2\mathcal J_0}
```

とする。第2章のM51方程式と等価な実方程式は

```math
\dot Q
=
\frac{AP+BQ}{\mathcal J_0}
+\lambda_{\rm prep}
\left[
g(1-r)Q
-\kappa\{(I-C)Q+DP\}
\right],
```

```math
\dot P
=
\frac{-AQ+BP}{\mathcal J_0}
+\lambda_{\rm prep}
\left[
g(1-r)P
-\kappa\{(I-C)P-DQ\}
\right].
```

これがM51の縮約ミクロ方程式である。$Q$ と $P$ が各試行の状態であり、右辺はそれらの有限次元driftとして完全に指定される。最小模型では確率微分項を置かない。

| 要素 | 方程式上の項 | 物理的分類 |
|---|---|---|
| 可逆担体 | $G$ または $A,B$ | Hamiltonian流 |
| 動径pump | $g(1-r)(Q,P)$ | action供給と飽和を表す開放drift |
| transverse sink | $-\kappa(I-\Pi_c)z$ | template直交成分を外部portへ捨てる開放drift |
| clock・切断器 | $\lambda_{\rm prep}$ | 準備portの接続時間を指定する外部制御 |
| template | $(Q^w,P^w)$ | 目標rayを物理的に保持する装置自由度 |

M51はpumpとsinkの背後にある有限bath自由度、衝突則、仕事源、排熱先を消去した基礎開放モデルである。従って上の式からの結論は厳密でも、この式を有限閉鎖Hamiltonianから導出したとは呼ばない。有限bath持上げ、雑音、揺らぎ散逸関係、総仕事・熱・エントロピー生成は後続課題である。

## M.4 seed測度、押出し測度、無反応

試行開始面で、実状態と空の履歴registerに基準測度

```math
\mu_0(dQ\,dP\,dH_{\rm port})
```

を置く。$\mu_0$ は目標射影そのものを階数1共分散として埋め込まない。template設定 $c$ に対するM51流を $\Phi_c^t$ と書けば、準備時刻の測度は

```math
\mu_c^t=(\Phi_c^t)_\#\mu_0
```

である。目標依存性は初期分布へ隠さず、template設定後のdriftに現れる。

相互作用表示の初期値を $\widetilde z_0=a_0c+p_0$、$c^\dagger p_0=0$ と分ける。安全事象を

```math
G_*
=
\{|a_0|\geq a_*\}
\cap
\{\|\widetilde z_0\|\leq R_*\}
```

とする。$a_0=0$ の直交超平面はM51で不変であり、そこから目標rayは生成されない。有限 $a_*$ を採ることで有限時間の一様上界を得る。$G_*^c$ を捨てず、下流の完全結果集合で無反応へ送る。

連続なseed測度では直交超平面の測度が零でも、$|a_0|$ が小さい近傍の質量は有限時間資源に影響する。$a_*\downarrow0$ とすると無反応質量は減らせるが、$q_*=(R_*^2-a_*^2)/a_*^2$ と必要準備時間が増える。この交換を無限時間極限で隠さない。

## M.5 R171の証明

M51のunitary $U(t)$ で回る相互作用表示を使う。$c$ を固定し、$\widetilde z=ac+p$、$c^\dagger p=0$ と置けば

```math
\frac{da}{d\tau}
=
g(1-\|\widetilde z\|^2)a,
\qquad
\frac{dp}{d\tau}
=
\left[g(1-\|\widetilde z\|^2)-\kappa\right]p.
```

$a\neq0$ では両式の共通動径項が消え、

```math
\frac{d}{d\tau}\left(\frac{p}{a}\right)
=
-\kappa\frac{p}{a},
\qquad
\frac{p(\tau)}{a(\tau)}
=
\frac{p_0}{a_0}e^{-\kappa\tau}
```

を得る。$G_*$ 上では

```math
\frac{\|p_0\|^2}{|a_0|^2}
\leq
\frac{R_*^2-a_*^2}{a_*^2}
=q_*.
```

純粋ray距離は

```math
D_{\rm pure}
\left(
\frac{\widetilde z\widetilde z^\dagger}
{\widetilde z^\dagger\widetilde z},
cc^\dagger
\right)
=
\frac{\|p\|}{\sqrt{|a|^2+\|p\|^2}}
\leq
\frac{\|p\|}{|a|}
\leq
\sqrt{q_*}e^{-\kappa\tau}.
```

unitary変換はこの距離を保存するので第2章の時刻 $t$ の上界が従う。

作用重み付き第2モーメントに対し、全安全試行で $\|p\|^2\leq q_*e^{-2\kappa\tau}|a|^2$ だから

```math
1-\operatorname{tr}(\Pi_cC_{Z,G_*})
\leq
\frac{q_*e^{-2\kappa\tau}}
{1+q_*e^{-2\kappa\tau}}.
```

純粋射影とのtrace距離に対する上界を使えば

```math
D_{\rm tr}(C_{Z,G_*},\Pi_c)
\leq
\sqrt{q_*}e^{-\kappa\tau}
```

となる。

動径収束も確認する。$q_0=\|p_0\|^2/|a_0|^2$、$y=|a|^{-2}$ と置けば、$\kappa\neq g$ で

```math
y(\tau)
=
1+(y_0-1)e^{-2g\tau}
+\frac{gq_0}{g-\kappa}
\left(e^{-2\kappa\tau}-e^{-2g\tau}\right).
```

$\kappa=g$ では最後の項を $2gq_0\tau e^{-2g\tau}$ に置き換える。従って $|a|\to1$、$p\to0$ であり、有界seed集合上の全ベクトル収束は $\min\{2g,\kappa\}$ で抑えられる。

準備終了後に $\lambda_{\rm prep}=0$ とすれば、開放項は消えて $i\mathcal J_0\dot z=Gz$ だけが残る。各試行の実正準状態は可逆に発展し、R135により第2モーメントはunitary共役で輸送される。以上でR171を得る。

## M.6 M50への受渡しと二乗則の位置

M51切断面の各安全試行について、M50へ渡すのは $c$ または $C_Z$ ではなく、実正準担体から得た $z(\omega)$ である。等長埋込み $\Psi$ に対するM50の理想ray重みは

```math
w_i(z)
=
\frac{|(\Psi z)_i|^2}{z^\dagger z}.
```

M51のray上界とR168により、無反応を含む実分布を、

```math
p_c^{\rm id}(i)
=
P(G_*)
\frac{|(\Psi c)_i|^2+\delta q_i}{1+\delta},
\qquad
p_c^{\rm id}(\varnothing)=P(G_*^c)
```

へ比較できる。M51由来のray誤差だけなら

```math
D_{\rm TV}(p^{\rm M51\to M50},p_c^{\rm id})
\leq
\frac{P(G_*)\sqrt{q_*}e^{-\kappa\tau}}
{1+\delta}
```

である。実際のR170では、これに容量、作用殻、混合、衝突、保持、固定、記録の誤差を別に加える。

ここで $|(\Psi c)_i|^2$ は、M51が作った階数1第2モーメントの対角である。同じ式をM50側では各試行の作用比として読む。従って二乗形の状態依存性は準備済み統計に由来し、排他的な単一結果はM50の作用殻状態数と粒子位置熱化に由来する。M51だけで結果頻度が生じるとも、M50が目標rayを無から準備するとも解釈しない。

## M.7 現行系列への特殊化と非主張

| 系列 | M51から供給できるもの | M51から従わないもの |
|---|---|---|
| Q1 | $m=2$、W型生成子、目標Bloch ray。R145はこの特殊化 | W型粒子位置、Born枝、測定後template交換、周期収支 |
| Q2-1 | 固定有限program rayの担体準備 | 未知入力の自己分解、CNOT、二粒子位置 |
| Q2-3 | 3部分系の初期rayを既存Q1 portから準備 | 2相互作用区間、非破壊な中間受渡し、最終Born型読出し |
| Q2-4 | 一般回路用rayの受動担体準備 | ゲート列、最終Born型読出し、$L=2^n$ 受動モードの個別制御を避ける資源性 |
| Q2-2 | setting-free局所seedまたは有限ray template | singlet交差モーメント、paired-Hopf強matching、Bell因果構造 |
| Q3 | M37へ渡すrank-one初期標本集団とM42初期位置用の単一試行信号 | M37--M42との同一局所Hamiltonian統合、空間伝播、終位置記録 |

M51/R171は状態準備の共通開放模型を与えるが、次を主張しない。

1. pump、sink、template、clockを含む有限閉鎖Hamiltonian実現。
2. 雑音付き定常測度、揺らぎ散逸関係、有限bathによる誤差上界。
3. M51とM37、M42、M47、M48、M49、M50が同じ物理装置であること。
4. M51単独で粒子位置、Born型排他的結果、測定後状態を生成すること。
5. template設定から独立に任意の未知入力状態を自己準備すること。
6. 試行列の独立同分布性または二項型有限標本揺らぎ。

これらを追加するときは、M51の開放portを構成する有限bath、仕事源、排熱、情報履歴を完全状態へ加え、準備前測度から切断面測度までの因果鎖を再監査する。
