@number: 2
@chapter: 本文
@title: 有限モード担体と共通正準モジュール
@status: M54をQ1・Q2の共通親模型族として定義し、R181A--R181Dを準備、tensor-lift、永続gate、projector-tree読出しの正本として置く。Q3はM54の準備portだけを上流契約として使う。

## 2.1 M54を親模型族とする範囲

M54は、有限個の実正準対から得る複素registerを、準備port、可逆gate、作用殻receiver、記録まで運ぶ模型族である。規模 $n$ の完全状態を

```math
\Gamma_{54}^{(n)}
=
(Z,S_{\rm port},G,W,J,A^\delta,X,C,
B_{\rm cold},B_{\rm spent},D,\tau)
```

と書く。$Z\in\mathbb C^{2^n}$ は物理的な実正準対の派生表示、$S_{\rm port}$ は有限次元source/template port、$G,W$ はanti-registerと可逆work、$J=(J_0,J_1)$ はraw作用容量、$A^\delta$ は作用殻容量、$X$ はselector、$C$ は有限衝突cellとその履歴、$B_{\rm cold},B_{\rm spent}$ は未使用・使用済みbank、$D$ は外部記録、$\tau$ は自律clockである。Q1では $n=1$、Q2-1・Q2-2では $n=2$、Q2-3では $n=3$、Q2-4では一般の $n$ を使う。

外部interfaceは、sourceまたは物理templateのload、固定有限gate名と対象bit、読出しbit、誤差予算、試行回数、clock開始だけに限る。振幅表、確率表、mode別較正値、試行中の状態依存制御を外部から与えない。lift、unitary gate、SWAP、latch、filter、記録は有限正準写像として扱う。template整列とradial repumpは採用開放方程式、R161/R162は有効率と有限衝突近似、R170を使う作用殻選択は条件付き構成、cold/spent供給は弱開放境界である。

```math
S_{\rm port}
\xrightarrow{\mathrm{R181A/R181B}}
Z
\xrightarrow{\mathrm{R181C}}
Z_{\rm out}
\xrightarrow{\mathrm{R181D}}
(D,B_{\rm spent}).
```

R181Aは物理templateに沿うray準備、R181Bは固定2・3入力の可逆tensor-lift、R181Cは同じregister上の局所gate列、R181DはR170で駆動する逐次projector-tree Born instrumentを与える。Q1とQ2はこの同じ状態型とport規約の特殊化であり、旧来の別模型を並置しない。ただし、全 $n$ を同じ製造済み装置で覆うことや、Q1とQ2の全パラメータを同一にすることは主張しない。Q1--Q3の単一反復装置M0は、M54より強い未完成の統合目標である。

| 系列 | M54の特殊化 | 準備 | 操作 | 排他的出力 |
|---|---|---|---|---|
| Q1 | $n=1$、W型2モード | R181A | R140 | R181Dの深さ1とR143 |
| Q2-1 | $n=2$ | R181B | R181C | R181Dの深さ2 |
| Q2-2 | $n=2$、固定singlet source | R181B/R181C | R180 setting-pre block | R181Dの局所nodeとR180C |
| Q2-3 | $n=3$ | R181Bを2回 | R181CとR177 | R181Dの深さ3 |
| Q2-4 | 一般 $n$、root input | R181Aのradial portとR179 | R181C | R181Dの深さ $n$ |
| Q3 | 有限空間セル | R181Aだけを上流契約として使用 | M37--M42 | 初期R164選択後は同じ粒子を記録 |

M54の $Z$ は各試行の物理的実状態から得る。解析上の $c$、$C_Z$、Born分布をcontrollerへ書き戻さない。Q3ではM54準備後の信号にR164を一度だけ適用してM42の初期位置を作り、終時刻に別の位置を再標本化しない。共通モデル族への整理は固定目標の文言や達成ラベルを変更しない。

## 2.2 有限正準信号の辺代数

有限グラフ $\mathcal G=(\Omega,E)$ の各頂点 $z$ に実正準対 $(Q_z,P_z)$ と複素信号

```math
d_z=\frac{Q_z+iP_z}{\sqrt{2\mathcal J_0}}
```

を置く。全信号作用は $J_{\rm sig}=\mathcal J_0d^\dagger d$ である。時間依存Hermitian行列 $h(t)$ に対するHamiltonian

```math
H_h(t)=d^\dagger h(t)d
```

は $i\mathcal J_0\dot d=h(t)d$ を与える。無向辺 $e=\{u,v\}$ の差モード射影と辺生成子を

```math
\Pi_e
=
\frac12
(|u\rangle-|v\rangle)
(\langle u|-\langle v|),
```

```math
G_e
=
\mathcal J_0d^\dagger\Pi_ed
=
\frac14
\left[(Q_u-Q_v)^2+(P_u-P_v)^2\right]
```

とする。

<!-- theorem-start:theorem -->
**定理（R112：有限正準信号の制御・比較・記録回路）**

有限正準信号の可逆有効力学は、有限配置グラフ上の頂点作用項と差モード辺生成子の有限プログラムとして表せる。連結グラフでは隣接2モード交換と局所位相から $U(L)$ の任意の有限unitaryを有限積として合成できる。さらに、固定有限個の信号register、時計、比較対象、安全領域、記録枝、テンプレートについて、次を有限個の正準対と滑らかな有限時計窓で実装できる。

1. 指定した有限unitary列の自律化と有限制御誤差評価。
2. 互いに素な安全領域の滑らかな比較と、境界失敗を含む正式な無反応結果。
3. 空registerと使用済みregisterを区別した正準SWAPおよび結果別テンプレート交換。
4. 各枝だけに支持を持つ局所記録と、外部履歴を残した内部作業registerの逆計算。

全入力、時計、使用済みcell、無反応、外部記録を含む拡大写像は1対1に保てる。Q1、Q2、Q3の違いは、頂点集合、信号の物理的由来、係数、時計窓、排他的出力の実装にある。本定理だけから枝確率、Born型状態数、粒子位置分布、無期限resetは従わない。
<!-- theorem-end:theorem -->

## 2.3 R112の役割境界

R112が現行主線へ供給するのは次の部品である。

1. 局所位相回転と隣接 $QQ+PP$ 交換による有限ユニタリ回路。
2. 時計窓の自律化と有限誤差制御。
3. 外部から与えた制御値に対する滑らかな比較器と正式な無反応領域。
4. 正準SWAP、局所記録、テンプレート交換、内部逆計算。

作用区間と一様選択器角から長期Born型頻度を得る旧経路は現行定理に使わない。R112は作用殻fiber内の平衡化も、結果列の独立同分布性も証明しない。旧正準標本器の確率生成経路は `notes/superseded_m35_born_sampler.md` に整理し、非確率的な制御・比較・記録内容はR112へ吸収する。

固定benchmarkのprogram順序を外部scheduleで作ることは許す。このscheduleは入力条件の提示であり、同じ試行のBorn型出力を生成する機構ではない。

## 2.4 M54物理template-port準備

各試行の物理状態として $m$ 個の実正準対 $(Q,P)\in\mathbb R^{2m}$ を置き、その派生座標を

```math
z=\frac{Q+iP}{\sqrt{2\mathcal J_0}}
```

とする。$z$ は実担体の表示であって追加の実体ではない。目標templateも実装置の正準対 $(Q^w,P^w)$ で保持し、そこから得る非零派生座標 $w$ を直接couplerへ入れる。規格化方向 $c=w/\|w\|$ と射影 $\Pi_c=cc^\dagger$ は解析記号に限り、controllerが状態依存除算を行って作る物理registerではない。

Hermitian生成子 $G(t)$ とそのunitary $U(t)$ に対し $w(t)=U(t)w(0)$ とする。目標作用 $J_*>0$ を固定し、M54の雑音零の採用開放方程式を

```math
\dot z
=
-\frac{i}{\mathcal J_0}G(t)z
+\lambda_{\rm prep}(t)
\left[
g(J_*-z^\dagger z)z
-\kappa\{(w^\dagger w)z-w(w^\dagger z)\}
\right]
```

と定める。$g,\kappa>0$、$\lambda_{\rm prep}\geq0$ である。第1項は実正準Hamiltonian伝播、動径項はpumpと飽和、中括弧は非規格化templateだけで書いたtransverse sink、$\lambda_{\rm prep}$ は物理clockが開閉するportである。$\kappa=0$ はR181Dが使うradial-only repump portである。最小M54は決定論的であり、Langevin雑音を含まない。

準備有効時間を

```math
\tau(t)=\int_{t_0}^t\lambda_{\rm prep}(s)\,\mathrm ds
```

とする。相互作用表示で $\widetilde z=ac+p$、$c^\dagger p=0$ と分解すると

```math
\frac{da}{d\tau}=g(J_*-\|\widetilde z\|^2)a,
\qquad
\frac{dp}{d\tau}
=
\left[g(J_*-\|\widetilde z\|^2)-\kappa\|w\|^2\right]p,
```

```math
\frac{\|p(\tau)\|}{|a(\tau)|}
=
\frac{\|p_0\|}{|a_0|}e^{-\kappa\|w\|^2\tau}
```

となる。初期seed測度 $\mu_0$ は目標階数1分布そのものとせず、固定 $a_*,R_*>0$ に対する安全事象

```math
G_*
=
\{|c^\dagger\widetilde z_0|\geq a_*\}
\cap
\{\|\widetilde z_0\|\leq R_*\}
```

を定める。$G_*^c$ はseed失敗として完全結果集合の無反応へ残す。目標依存の準備測度は、同じseed測度を上のdriftで押し出した $(\Phi_c^t)_\#\mu_0$ であり、階数1統計を初期測度へ直接置いたものではない。

<!-- theorem-start:theorem -->
**定理（R181A：物理template-port共通ray準備）**

$G_*$ 上で $q_*=(R_*^2-a_*^2)/a_*^2$ とする。M54の採用開放方程式では、各安全試行のray距離は

```math
D_{\rm pure}
\left(
\frac{zz^\dagger}{z^\dagger z},
\Pi_c(t)
\right)
\leq
\sqrt{q_*}e^{-\kappa\|w\|^2\tau(t)}.
```

安全試行の作用重み付き規格化第2モーメントを

```math
C_{Z,G_*}(t)
=
\frac{\mathbb E[\mathbf1_{G_*}Z_tZ_t^\dagger]}
{\mathbb E[\mathbf1_{G_*}Z_t^\dagger Z_t]}
```

とすれば

```math
D_{\rm tr}
\left(C_{Z,G_*}(t),\Pi_c(t)\right)
\leq
\sqrt{q_*}e^{-\kappa\|w\|^2\tau(t)}.
```

また、$a_0\neq0$ の各試行は $\tau\to\infty$ で作用 $J_*$ の位相円へ収束し、動径誤差を含む収束率は有界seed集合上で $\min\{2gJ_*,\kappa\|w\|^2\}$ により抑えられる。有限時刻 $t_{\rm cut}$ で $\lambda_{\rm prep}=0$ とした後は、各試行の実正準状態が $i\mathcal J_0\dot z=Gz$ に従い、R135の第2モーメント輸送が成り立つ。$G_*^c$ の確率は無反応質量として保持し、成功試行だけを結果分布として再規格化しない。物理couplerは $w$ だけを読み、$w/\|w\|$ を生成しない。
<!-- theorem-end:theorem -->

証明、複素式と等価な実変数方程式、pump・sink・template・clockの因果台帳は付録Mに置く。R181Aは採用開放方程式後の厳密結果である。pumpとsinkの環境自由度、仕事、熱、エントロピー生成を有限閉鎖系から導いた結果ではない。

## 2.5 有限信号集団の第2モーメント輸送

有限試行空間上の非零複素信号 $Z\in\mathbb C^m$ と、有限で正の集団作用

```math
S_Z=\mathbb E[Z^\dagger Z]
```

を考える。非中心化された規格化第2モーメントを

```math
C_Z
=
\frac{\mathbb E[ZZ^\dagger]}{S_Z}
```

と定める。これは通常の中心化共分散ではなく、$\mathbb E[Z]=0$ の場合にだけ中心化した量と比例して一致する。

<!-- theorem-start:theorem -->
**定理（R135：有限信号集団の規格化第2モーメント輸送）**

各試行の信号が同じ有限次元unitary $U(t)$ により $Z(t)=U(t)Z(0)$ と発展するなら、

```math
C_Z(t)=U(t)C_Z(0)U(t)^\dagger
```

であり、trace、正値性、rankは保存される。$i\mathcal J_0\dot U=G(t)U$ なら

```math
i\mathcal J_0\dot C_Z=[G(t),C_Z]
```

である。

さらに、同じ初期標本から作る理想信号 $\widetilde Z_t=U(t)\widetilde Z_0$ に対し

```math
\|Z_t-\widetilde Z_t\|
\leq
\varepsilon(T)\|\widetilde Z_0\|
```

が全試行、$0\leq t\leq T$ で一様に成り立つとする。$\widetilde S_0=\mathbb E\|\widetilde Z_0\|^2$、$S_t=\mathbb E\|Z_t\|^2$、

```math
\kappa_T
=
\sup_{0\leq t\leq T}
\frac{\widetilde S_0}{S_t}
```

と置けば、

```math
D_{\rm tr}
\left(
C_Z(t),
U(t)C_Z(0)U(t)^\dagger
\right)
\leq
\min
\left\{
1,
2\varepsilon(T)\sqrt{\kappa_T}
+\varepsilon(T)^2\kappa_T
\right\}.
```
<!-- theorem-end:theorem -->

階数1なら $C_Z=cc^\dagger$、$c^\dagger c=1$ と書け、非負量

```math
\mathbb E\|(I-cc^\dagger)Z\|^2
```

が零になるため、$Z=\alpha c$ がほとんど確実に成り立つ。$m=2$ では

```math
C_Z
=
\frac12
\left(I_2+\boldsymbol r\cdot\boldsymbol\sigma\right)
```

と書け、階数1条件は $|\boldsymbol r|=1$ と同値である。従ってBloch球はR135の2次元系であり、独立の結果を必要としない。正確輸送、有限時間誤差、階数1支持、2次元幾何を同じ第2モーメントの定理として使い、同じ上流偏差を複数の誤差項へ加算しない。証明は付録Fに置く。

## 2.6 一般ray平均からM50枝統計への受渡し

安全事象 $G$ 上の有限信号 $Z$ に対し、失敗質量を捨てない安全ray平均を

```math
R_Z^G
=
\mathbb E
\left[
\mathbf1_G
\frac{ZZ^\dagger}{Z^\dagger Z}
\right]
```

とする。等長埋込み $\Psi$ と $M_i=\Psi^\dagger|i\rangle\langle i|\Psi$ を固定する。

<!-- theorem-start:theorem -->
**定理（R168：一般ray平均からM50枝統計への受渡し）**

各安全試行にM50を適用し、安全事象外を無反応へ送ると、完全結果分布は

```math
P(i)
=
\frac{\operatorname{tr}(M_iR_Z^G)+\delta q_iP(G)}{1+\delta},
\qquad
P(\varnothing)=P(G^c)
```

である。さらに次が成り立つ。

1. $C_Z=cc^\dagger$ かつ $G$ 上で信号が非零なら、R135の支持節により $R_Z^G=P(G)cc^\dagger$ である。
2. $Z^\dagger Z=s_*>0$ がほとんど確実で $P(G)=1$ なら、$R_Z^G=C_Z$ である。
3. 一般の可変作用集団では $R_Z^G$ が読出し対象であり、$C_Z$ への置換には動径補正が必要である。
4. 安全な近似rayが目標rayから純粋状態距離 $s$ 以内なら、対応する枝分布の全変動距離は $s/(1+\delta)$ 以下である。

成功試行だけで再規格化しない。
<!-- theorem-end:theorem -->

$P(G)=1$、$\overline S=\mathbb E[Z^\dagger Z]$ の場合、動径補正は

```math
D_{\rm tr}(R_Z^G,C_Z)
\leq
\frac12
\mathbb E
\left|
\frac{Z^\dagger Z}{\overline S}-1
\right|
\leq
\frac12
\frac{\sqrt{\operatorname{Var}(Z^\dagger Z)}}{\overline S}
```

で抑えられる。R168はM37を前提とせず、Q1・Q2が単一試行信号をM50へ渡すとき、およびQ3が初期M42位置または固定時刻代替診断へ信号を渡すときの共通統計写像である。証明と可変作用反例は付録Fに置く。

## 2.7 M50の作用容量と枝状態数

非零有限信号 $v\in\mathbb C^m$、等長埋込み $\Psi:\mathbb C^m\to\mathbb C^L$、排他的枝 $i\in\mathcal I$ を考える。正の基準分布 $q_i>0$、$\sum_iq_i=1$ と正則化 $\delta>0$ を固定し、

```math
J_i(v)=\mathcal J_0|(\Psi v)_i|^2,
\qquad
A_i^\delta(v)=J_i(v)+\delta q_iJ_{\rm sig}(v)
```

と置く。各枝に2つの非負作用を持つ排他的作用殻を置く。

<!-- theorem-start:theorem -->
**定理（R164：有限信号作用のBorn型殻状態数）**

上の仮定の下で、全枝を同じLiouville母測度で数えると枝状態数は

```math
\Omega_i^\delta(v)
=
\frac{(2\pi)^2}{J_{\rm ref}}A_i^\delta(v)
```

であり、単一Liouville母測度を1回だけ規格化すると

```math
\pi_i^\delta(v)
=
\frac{\Omega_i^\delta(v)}{\sum_j\Omega_j^\delta(v)}
=
\frac{|(\Psi v)_i|^2/(v^\dagger v)+\delta q_i}{1+\delta}
```

となる。零信号、安全閾値未満、有限幅遷移域は無反応 $\varnothing$ へ送る。一般に各明反応枝が $q$ 個の独立な作用分配方向を持てば $\Omega_i\propto(A_i^\delta)^q$ であり、全容量族でBorn型線形則を保つのは $q=1$ に限る。
<!-- theorem-end:theorem -->

作用殻を消去する表示では

```math
E_i^\delta(v)=-\Theta\log\pi_i^\delta(v)
```

を条件付き中間状態有効自由エネルギーとして使う。状態数を残す表示と消去表示は同値であり、同じ縮約分配関数へ $\Omega_i^\delta e^{-E_i^\delta/\Theta}$ を入れて二重計数してはならない。

## 2.8 R161/R162の有限再平衡化

有限連結枝グラフ $G_X=(\mathcal I,E_X)$ で

```math
k_{i\to j}^\delta(v)
=
\kappa_Xa_{ij}
\sqrt{\frac{\pi_j^\delta(v)}{\pi_i^\delta(v)}}
```

を採用する。$q_{\min}=\min_iq_i$、$a_{\min}$ を正の最小辺重み、$\lambda_G$ を無重みグラフLaplacianの第1非零固有値とし、

```math
m_\delta=\frac{\delta q_{\min}}{1+\delta},
\qquad
\lambda_\delta=\kappa_Xa_{\min}m_\delta\lambda_G,
\qquad
C_\delta=\frac12\sqrt{m_\delta^{-1}-1}
```

と置く。

<!-- theorem-start:theorem -->
**定理（R161：任意の有限信号方向に対する粒子位置再平衡化）**

任意の非零入力 $v$ に対して $\pi^\delta(v)$ は上の連続時間跳躍過程の唯一の定常分布であり、任意の初期枝分布 $p_0$ から

```math
D_{\rm TV}(p_{\tau_X},\pi^\delta(v))
\leq
C_\delta e^{-\lambda_\delta\tau_X}
```

である。また理想枝重み $w_i(v)=|(\Psi v)_i|^2/(v^\dagger v)$ との差は $D_{\rm TV}(\pi^\delta,w)\leq\delta/(1+\delta)$ である。
<!-- theorem-end:theorem -->

<!-- theorem-start:theorem -->
**定理（R162：局所詳細釣合い率の有限衝突熱浴実現）**

各辺に対称障壁と有限個の入射cellを置き、入射位置、到着時計、運動方向、反射枝、出射エネルギー、履歴cellを完全状態へ含めれば、正逆衝突を1対1に対応させる有限Hamiltonian散乱でR161の率を任意精度で近似できる。固定観測時間での縮約経路測度誤差は、cell overflow、エネルギー尾部、閾値平滑化、時計、入力保持の誤差和で抑えられ、超過cellと比較境界は無反応へ送れる。
<!-- theorem-end:theorem -->

作用殻fiberは状態数を、衝突bathは粒子位置遷移を担い、同じ自由度ではない。

**系（粗視化経路熱力学）**

R161の局所詳細釣合い過程、またはR162の縮約過程の正逆protocolについて、粗視化経路エントロピー生成 $\Sigma$ は

```math
\frac{\mathcal P_F[\omega]}{\mathcal P_R[\omega^\dagger]}
=e^{\Sigma[\omega]},
\qquad
\left\langle e^{-\Sigma}\right\rangle_F=1,
\qquad
\langle\Sigma\rangle_F\geq0
```

を満たす。瞬間quench $v^-\to v^+$ では

```math
W_i^{\rm rel}
=\Theta\log\frac{\pi_i^\delta(v^-)}{\pi_i^\delta(v^+)},
\qquad
\left\langle e^{-\beta W^{\rm rel}}\right\rangle=1,
```

```math
\langle W^{\rm rel}\rangle
=\Theta D_{\rm KL}
\left(\pi^\delta(v^-)\|\pi^\delta(v^+)\right).
```

これは作用殻を消去した粒子位置跳躍過程の厳密な関係であり、全装置周期の機械仕事・微視的熱収支ではない。証明と表示間の仕事の換算は付録Kに置く。

## 2.9 R170：M50固定入力時刻有限枝instrument

<!-- theorem-start:theorem -->
**定理（R170：M50固定入力時刻有限枝instrument）**

非零入力 $v\in\mathbb C^m$、有限枝グラフ $G_X$、等長埋込み $\Psi$、$\delta>0$、入力時刻 $t_\star$ を固定する。次を指定誤差内で実行できると仮定する。

1. $t_\star$ の信号を空の有限正準registerへSWAPし、処理中に保持する。
2. R164の作用容量と排他的作用殻を準備する。
3. R161の有限再平衡化を行い、R162の有限衝突実現で近似する。
4. 入射セルを止め、枝間ゲートを閉じて粒子位置を固定する。
5. 各枝だけに支持を持つ局所関数で空の記録セルを動かす。
6. 無反応、時計、使用済み衝突セル、旧信号、記録を含む拡大履歴を1対1に保つ。

このとき有限の $t_{\rm out}>t_\star$ と完全結果集合 $\mathcal I\cup\{\varnothing\}$ を持つinstrumentを選べる。理想分布を

```math
p_v^{\rm id}(i)=\pi_i^\delta(v),
\qquad
p_v^{\rm id}(\varnothing)=0
```

とすると、実分布は

```math
D_{\rm TV}(p_v^{\rm out},p_v^{\rm id})
\leq
\varepsilon_{170}
```

を満たす。ただし

```math
\varepsilon_{170}
\leq
\varepsilon_{\rm hold}
+\varepsilon_{\rm cap}
+\varepsilon_{\rm shell}
+\varepsilon_{\rm mix}
+\varepsilon_{\rm coll}
+\varepsilon_{\rm lock}
+\varepsilon_{\rm rec}
+\varepsilon_{\rm clk}
+\varepsilon_{\varnothing}
```

であり、同じ物理偏差を複数項へ入れない。無反応を除いて再規格化しない。
<!-- theorem-end:theorem -->

R170は有限枝instrumentの共通定理であり、M37を前提にしない。Q1のR143、Q2-2のR180C、Q3の固定時刻読出しはこの定理の特殊化または合成である。完全な証明と誤差台帳は付録Kに置く。

**系（共通instrumentの安定性）**

理想分布 $p,p'$ と実分布 $q,q'$ が

```math
D_{\rm TV}(q,p)\leq\varepsilon,
\qquad
D_{\rm TV}(q',p')\leq\varepsilon'
```

を満たせば

```math
D_{\rm TV}(q,q')
\geq
D_{\rm TV}(p,p')-\varepsilon-\varepsilon'.
```

任意の事象 $A$ について

```math
|q(A)-q'(A)|
\geq
|p(A)-p'(A)|-\varepsilon-\varepsilon'
```

であり、任意の有界観測量 $f$ について

```math
|\mathbb E_qf-\mathbb E_pf|
\leq
\operatorname{osc}(f)\varepsilon,
\qquad
\operatorname{osc}(f)=\sup f-\inf f.
```

従って理想分布間の分離が誤差和より大きければ、有限装置でも区別可能性が残る。この系をR124/R125の識別とR180CのBell監査へ共通に用いる。

## 2.10 M54の一様register、port、bank

$n$ 量子ビット、深さ $d$、固定有限普遍ゲート集合から与えられる回路を考え、$L=2^n$ とする。M54では計算基底文字列 $x$ を受動信号モードへ直接対応させる。

```math
|x\rangle
\longleftrightarrow
Z_x,
\qquad
Z=(Z_x)_{x\in\{0,1\}^n}\in\mathbb C^L.
```

M54はsignal、anti-register、filter work、rejected-history、radial repump、raw/regularized容量pointer、一様gate bus、collision cell、cold bank、spent bank、出力記録、clockを持つ。内部の受動自由度、静的結合、状態容量、受動並列度は $2^n\operatorname{poly}(n,d)$ まで許す。一方、外部programが指定するのはgate種、1個または2個の対象量子ビット、gate順序、現在読む出力bit、blanking round、cell index、clock窓だけである。$2^n$ モードの列挙、モード別初期化・較正・読出し、指数長の係数表、回路別配線、出力確率の事前計算を許さない。

M54はR181Bの反復tensor-liftを一般 $n$ へ延長しない。R179でbankをblank化した後、定数次元sourceを $0^n$ root modeへ接続して計算基底入力を作る。別の基底入力は回路先頭の $X$ gateで作る。gate列はR181C、末端bit列はR181D、結果相関履歴の境界はR178D、供給はR179が担う。

## 2.11 R181B：Q1-port可逆tensor-lift

固定された2入力または3入力について、Q1型portの信号を $a,b$、blank共同registerを $Z$、anti-registerを $G$ とする。R112の三次乗算pulseを有限列 $S_0$ として使い、係数を測定または外部転記せず

```math
(a,b,0,0,W_0)
\longmapsto
(a,b,Z=a\otimes b,G=\overline{a\otimes b},W_1)
```

を作る。

<!-- theorem-start:theorem -->
**定理（R181B：非規格化Q1-port可逆tensor-lift）**

$a,b$ が固定安全集合にあり、共同registerとanti-registerが指定blank幅以内なら、有限個の実正準対、有限clock窓、R112型の可逆乗算pulseにより上の写像を任意の誤差 $\eta_{\rm lift}>0$ 以内で実装できる。拡大状態 $(a,b,Z,G,W)$ 上の写像は1対1で、逆clock列により入力とworkを回収できる。controllerは $a_j,b_k$ を読み出さず、積係数表を入力しない。3入力は同じliftを2回使って作る。本結果は入力数を固定したQ2-1--Q2-3の構成であり、一般 $n$ の多項式資源tensor-product準備を主張しない。
<!-- theorem-end:theorem -->

詳細なpulse列、参照位相、有限誤差は付録Cに置く。

## 2.12 R181C：永続register上の一様局所gate合成

対象量子ビット集合 $S$ の大きさを $k\in\{1,2\}$ とし、$g$ を固定有限gate集合の $2^k$ 次元unitaryとする。spectator labelを $r\in\{0,1\}^{n-k}$ と書き、同じ局所生成子 $h_g$ を全sectorへ置く。

```math
H_{g,S}
=
\bigoplus_r h_g^{(r)},
\qquad
U_{g,S}=g_S\otimes I_{\bar S}.
```

<!-- theorem-start:theorem -->
**定理（R181C：永続register上の一様局所gate合成）**

各sector blockが同じ局所規則から生成され、実装block $\widetilde g_r$ が一様に $\|\widetilde g_r-g\|\leq\eta_g$ を満たし、異なるsector間の漏れの作用素normが $\eta_{\rm leak}$ 以下とする。このとき1個の共有clock窓で全spectator sectorへgateを作用でき、

```math
\|\widetilde U_{g,S}-U_{g,S}\|
\leq
\eta_g+\eta_{\rm leak}
```

である。block数による和は生じない。深さ $d$ のgate列では、全gateのglobal phaseを除いた誤差は各窓の作用素norm誤差の和以下である。固定gate集合なら、対象指定、制御channel、命令数は $n,d$ の多項式、静的sector結合は指数的でも一様有限規則から生成できる。
<!-- theorem-end:theorem -->

固定 $n=2,3$ では同じ定理がCNOT、局所操作、逆演算の有限列を与える。一般 $n$ では上のsector-broadcastを使う。いずれも中間測定、共同momentへの置換、再準備を行わず、同じ $Z$ を全gate窓で保持する。3次元Euclid空間への局所埋込み、指数個の静的結合の総製造費、全結合を個別に調整する方法は主張しない。

## 2.13 R181Dで使うprojector latch・可逆filter補題

出力bit $k$ に対する計算基底射影を $P_{k,0},P_{k,1}$ とし、

```math
P_{k,0}+P_{k,1}=I,
\qquad
P_{k,0}P_{k,1}=0
```

とする。容量pointerへ保持する作用を

```math
J_{k,b}(Z)=\mathcal J_0Z^\dagger P_{k,b}Z
```

とする。signalとworkの2 bank上に

```math
F_{k,b}
=
\begin{pmatrix}
P_{k,b}&P_{k,1-b}\\
P_{k,1-b}&-P_{k,b}
\end{pmatrix}
```

を置く。

<!-- theorem-start:lemma -->
**補題（直交projector作用latchとinvolution filter）**

上の $F_{k,b}$ は

```math
F_{k,b}^\dagger F_{k,b}=I,
\qquad
F_{k,b}^2=I
```

を満たし、blank work bankに対して

```math
F_{k,b}(Z,0)
=
(P_{k,b}Z,P_{k,1-b}Z)
```

と作用する。容量latchを信号に対する制御剪断として実装すれば、blank容量momentum上で $J_{k,0},J_{k,1}$ をpointerへ保持し、理想信号 $Z$ を変更しない。計算基底bit projectorとfilterはbit labelだけから一様に生成され、$2^n$ 成分の列挙を必要としない。
<!-- theorem-end:lemma -->

この補題は確率的な枝選択を行わない。selectorの生成はR164/R170、選択後の信号更新はR181Dが担う。

## 2.14 R181D：R170駆動projector-tree Born instrument

第 $k$ 段、履歴node $u$ の入力を $Z_u\neq0$ とし、直交射影 $P_{u,0},P_{u,1}$ に対するraw容量を

```math
J_{u,b}=\mathcal J_0Z_u^\dagger P_{u,b}Z_u,
\qquad
J_\Sigma=J_{u,0}+J_{u,1}
```

とする。作用殻へ渡すregularized容量は、固定 $q_0,q_1>0$、$q_0+q_1=1$ に対し

```math
A_{u,b}^\delta=J_{u,b}+\delta q_bJ_\Sigma
```

である。R164/R170は $b$ を確率 $(p_{u,b}+\delta q_b)/(1+\delta)$ で選ぶ。cutoffは除算せず、raw比較 $J_{u,b}\gtrless\tau J_\Sigma$ を用いる。幅 $\gamma J_\Sigma$ のguard帯、selector plateau外、collision overflowは正式な無反応 $\varnothing$ へ送る。selectorをlockした後にfilter $F_{u,b}$ を作用し、非選択成分をwork/spentへ保持する。選択成分はR181Aの $\kappa=0$ radial-only port

```math
\dot Z=g(J_*-Z^\dagger Z)Z
```

で標準作用へ戻す。$J_{u,b}\geq\tau J_\Sigma$ の下限から固定repump時間を選び、未知の $p_{u,b}$ に依存するsqueezeをcontrollerへ入れない。

<!-- theorem-start:theorem -->
**定理（R181D：R170駆動projector-tree Born instrument）**

理想node instrumentを深さ $m$ まで合成すると、葉 $y=(y_1,\ldots,y_m)$ の確率は

```math
\prod_{k=1}^m p_{k,y_k}
=
\frac{
\|P_{m,y_m}\cdots P_{1,y_1}Z_0\|^2
}{
\|Z_0\|^2
}
```

となり、指定projector-treeのBorn分布に一致する。入力分布誤差を $\varepsilon_{\rm in}$、安全履歴上の第 $k$ node実装誤差を $\bar\varepsilon_k$ とすれば、無反応を含む完全結果分布は

```math
D_{\rm TV}(P_{\rm out},P_{\rm Born})
\leq
\varepsilon_{\rm in}
+\frac{m\delta}{1+\delta}
+2m(\tau+\gamma)
+\sum_{k=1}^m\bar\varepsilon_k.
```

$\bar\varepsilon_k$ にはR170選択、controlled filter、radial repump、routeを各1回だけ含める。filter作用素誤差が $\eta_F<\sqrt\tau$ なら、選択後の規格化ray誤差は $2\eta_F/(\sqrt\tau-\eta_F)$ 以下である。成功試行だけを再規格化しない。
<!-- theorem-end:theorem -->

R181DはQ1の深さ1、Q2-1の深さ2、Q2-3の深さ3、Q2-4の深さ $n$ に同じnode機構を使う。最終分布を段ごとの規格化成功分布へ比較せず、実際の初期信号が持つBorn分布と完全結果分布を末端で一度だけ比較する。

## 2.15 R178D：逐次history逆掃除・collective reset定理

$Y\in\{0,1\}^n$ をbit data記録、$F\in\{0,1\}$ を無反応flagとし、完全結果は $(Y,F)$ として保持する。以下の情報容量下界は $Y$ だけに対する弱い下界であり、flagと微視的履歴に必要な追加容量を除外しない。

<!-- theorem-start:theorem -->
**定理（R178D：逐次history逆掃除・collective reset定理）**

gate、latch、filter、clockの完全な微視的履歴を保持する。出力 $Y$ を別の記録へ可逆copyした後なら、出力記録と相関しないHamiltonian workを逆順に掃除できる。R181Aのradial repumpは採用開放流なので、その散逸履歴を含む無履歴の逆掃除は主張しない。

一方、$(Y,F)$ を保持したまま装置、bath、履歴の全てを同じ初期点へ戻す1対1写像は存在しない。結果と相関するselector、使用済みpointer、collision履歴、clock履歴はspent tapeへ送る必要がある。spent状態から $Y$ を復号する誤り率を $p_{\rm e}$ とし、Fano補正を $\eta_{\rm F}=h_2(p_{\rm e})+p_{\rm e}\log(|\mathcal Y|-1)$ と置く。natsで測ったspent側の情報容量 $C_{\rm spent}$ は

```math
C_{\rm spent}\geq H(Y)-\eta_{\rm F},
\qquad
H(Y)\leq n\log2
```

を満たす。熱的resetの仕事・熱下界は、bath温度と消去protocolを別に指定した場合だけ従う。
<!-- theorem-end:theorem -->

R170の粗視化Markov pathだけから微視的状態を逆算しない。逆転に使用できるのはR162の完全collision履歴、R181Dのselector/filter履歴、または開放portの環境履歴である。同じbath seedまたは同じ使用済みcellを再利用した試行列を独立同分布とは呼ばない。

旧fixed-volume aperture、first-index tape、dyadic threshold経路はR181Dへ統合せず退役させる。旧経路が誤りだと結論したのではなく、Q1とQ2で同じR170作用殻receiverを使うという今回の模型統一に不要だからである。式と旧誤差台帳は `notes/superseded_r178_aperture_sampler.md` とGit履歴に残す。

## 2.16 R179：一様blank-bank・collision-cell・spent供給定理

全補助bankを $W\in\mathbb C^{D_{n,d}}$、$D_{n,d}\leq2^np(n,d)$ とまとめる。各blanking roundでbank modeとincoming cold modeの対応pairへ同じ形式のpartial SWAPを並列に作用させる。couplerは一様有限規則から作る同一の静的二次Hamiltonianとし、受動clockがroundを進める。指数個のcouplerを外部から個別に開閉せず、外部quench workをbank次元へ比例させない。

```math
W_{r+1}=C_rW_r+S_rE_r,
\qquad
\|C_r\|\leq\rho<1,
\qquad
\|E_r\|\leq\eta_{\rm cold}.
```

pairごとの全変換は2-mode回転で実正準かつ可逆であり、cold側出力はspent側へ保持する。active成分だけを捨てて非可逆化しない。R162/R170が使うcollision cell、selector pointer、filter work、radial-port環境の各bankは同じindex規則で供給する。

<!-- theorem-start:theorem -->
**定理（R179：一様blank-bank・collision-cell・spent供給定理）**

次の条件を仮定する。

1. bank初期normは $R_{\rm in}\leq\exp p_1(n,d)$ である。
2. cold layerのaggregate誤差は $\eta_{\rm cold}$ 以下である。
3. partial SWAPの残留係数は一様に $\rho<1$ である。
4. collision cellの初期lawは回路出力と独立で、同じ有限局所規則から生成される。

このとき

```math
\|W_R\|
\leq
\rho^RR_{\rm in}
+\frac{\eta_{\rm cold}}{1-\rho},
```

```math
R
=
O\!\left(
n+\log d+\log(1/\varepsilon_{\rm blank})
\right)
```

で全bankを一様にblank化できる。続いて定数次元sourceをroot modeへSWAPし、R181Dの各nodeへ有限個のR162 collision cell、selector、filter workをclock順に供給できる。外部program長、準備時間、clock round、必要精度は $n,d,1/\epsilon$ の多項式である。静的couplerと受動clockが一括作用する限り、外部controllerの仕事をbank次元へ比例させない。cold bathとspent bathの受動自由度、状態容量、総作用移送、総熱は指数的でもよい。
<!-- theorem-end:theorem -->

R179は低作用bathを無から生成しない。供給測度は同じ局所lawを反復する回路非依存の規則であり、出力確率表を含まない。外部精度を多項式に保つには、exact invariant blankを持つcold source、またはbank全体のaggregate誤差を一様contractで保証するcold sourceが必要である。有限温度の独立noiseが各modeに定数作用を残す場合、aggregate blank誤差は $D_{n,d}$ とともに増大するためR179の仮定を満たさない。

## 2.17 M54の合成誤差と資源

M54の完全結果分布を $P_{\rm M54}$、理想回路Born分布を $P_{\rm circ}$ とする。誤差を重複計上しなければ、

```math
D_{\rm TV}(P_{\rm M54},P_{\rm circ})
\leq
\varepsilon_{179}
+d\eta_{\rm gate}
+\varepsilon_{\rm leak}
+\frac{n\delta}{1+\delta}
+2n(\tau+\gamma)
+\sum_{j=1}^n\bar\varepsilon_j.
```

ここで

```math
\varepsilon_{179}
\leq
C_{\rm root}
(\varepsilon_{\rm blank}
+\varepsilon_{\rm src}
+\varepsilon_{\rm swap})
+\varepsilon_{\rm coll}.
```

$\bar\varepsilon_j$ は第 $j$ 段のR170選択、controlled filter、radial repump、route、clockだけを含む。R179へ入れたcold floorとcollision誤差を再び含めない。

$\eta_{\rm gate}=O(\epsilon/d)$ とし、$\tau,\gamma,\delta,\bar\varepsilon_j$ はそれぞれ $O(\epsilon/n)$ と選べる。

保守的な逐次読出し時間は

```math
O\!\left(
\frac{n^2}{\epsilon}\log\frac n\epsilon
\right)
```

である。必要な殻stiffnessは $O(n^2/\epsilon^2)$、collision fluxは $O(\sqrt{n/\epsilon})$、barrier rangeは $O(\log(n/\epsilon))$ で抑えられる。受動modeとcold bath容量は指数的だが、回路記述、外部命令、準備round、gate窓、読出し時間、必要精度は多項式である。

## 2.18 Q2-4の判定と境界

R181Cは指数個の個別gate設定、R181Dは全 $2^n$ 葉の一括読出し、R179は指数個の個別blank初期化を避ける。従ってM54はQ2-4を条件付き達成へ進める。条件は、R170作用殻、R162 collision cell、controlled filter、radial repump、一様bank--bath結合を同じsafe setとclockで接続することである。

本構成は通常の計算量理論における多項式資源の古典simulationではない。指数個の受動自由度、静的結合、bath容量、総熱を許した上で、外部制御と総時間を多項式に抑える結果である。未知量子入力、適応中間測定、誤り訂正、固定容量bathによる無期限独立同分布標本は主張しない。M54はQ1・Q2の共通親模型族だが、同一の製造済み装置や同一パラメータを主張しない。

## 2.19 物理的意味と限界

熱化終了後の局所記録生成子は、枝 $i$ に支持を持つ滑らかな関数 $d_i(x)$ と空の記録運動量 $P_{D_i}$ を使い、

```math
G_{\rm rec}=\sum_i d_i(x)P_{D_i}
```

と書ける。これは記録時刻の排他的粒子位置を読む。入力時刻以前の粒子軌道、初回到達率、吸収率、時間積分流束を与えない。

R170は、列挙した部品を1つの具体的有限局所Hamiltonianへ統合済みだと主張しない。現行の条件付き達成または部分達成は、この未統合部分を明示して判定する。一意エルゴードな外部scheduleまたは有限熱化から、結果列の独立同分布性や二項型有限標本揺らぎも従わない。
