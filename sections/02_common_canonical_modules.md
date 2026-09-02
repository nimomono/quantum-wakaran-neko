@number: 2
@chapter: 本文
@title: 有限モード担体と共通正準モジュール
@status: Q1の2モード、Q2の4モード、Q3の有限空間セル担体に共通するR112、R171、R135、R164と、固定時刻枝instrumentのR161、R162、R168、R170を整理する。共通化は有限正準担体と操作契約に限り、Q3のM37--M42ミクロ装置をQ1・Q2と同一化しない。

## 2.1 共通主線と統一M0の違い

共通の階数1状態準備と固定時刻Born型instrumentは次の因果鎖を使う。

```math
\Gamma_0
\xrightarrow{\mathrm{M51/R171}}
C_Z\simeq cc^\dagger,
\qquad
Z(\omega)
\longrightarrow
\Omega_i^\delta(v)
\longrightarrow
\pi_i^\delta(v)
\longrightarrow
X=i
\longrightarrow
D_i.
```

M51は実正準担体と開放portのseed測度を有限時間押し出し、単一試行の派生信号 $Z(\omega)$ の集団第2モーメントを階数1射影へ近づける。統計因子 $c$ または $C_Z$ を単一試行controllerへ書き戻さず、各試行に実在する正準担体から得た $v=Z(\omega)$ だけをM50の作用容量へ渡す。Q1とQ2、および任意の固定時刻instrumentでは、R164で排他的枝の状態数を数え、R161/R162で粒子位置を有限時間再平衡化し、R170で枝を固定して局所記録する。

Q3の空間位置では、M51準備後の単一試行信号にR164を一度だけ適用してM42の初期粒子位置を作る。その後はM37担体の局所辺流とM42 bathが同じ粒子を輸送し、終時刻にはR112で既存位置を記録する。終時刻R170で別の位置を再標本化しない。

二乗形はM51が作る第2モーメントの対角とR164が数える単一試行作用の両方に現れるが、同じ因果段階ではない。M51はrayを準備し、R164はその方向を1個の排他的位置または枝へ物理化する。M51単独をBorn型標本器と呼ばず、初期M42選択と終時刻M50選択を2つの確率源として併用しない。

| 系列 | 有限担体の大きさ | 単一試行の実体 | 共通モジュール | 系列固有装置 |
|---|---:|---|---|---|
| Q1 | $L=2$ | 2モード実担体、粒子位置、bath、記録 | M51、R112、M50 | M47 W型分析器 |
| Q2 | $L=4$ | 4モード実担体、二粒子位置、共同bath、記録 | M51、R112、M50 | M49、M48 |
| Q3 | 空間セル数 $L$ | M37実振動子、M42局在粒子、局所辺bath、記録 | M51、R112、R135、初期R164 | M37--M42二層模型 |

同じ $L$ 次元正準代数を使うことは、担体のミクロHamiltonian、bath、粒子輸送則、時計、記録器が同じことを意味しない。

| 系列 | M51の役割 | M50へ渡す単一試行信号 | 排他的出力 | 系列固有部分 |
|---|---|---|---|---|
| Q1 | M51の2モード特殊化でW型rayを準備 | M47の信号bath座標 $Z(\omega)$ | 左右井戸 | W型制御、有限コントラスト、結果別テンプレート |
| Q2-1 | 固定programならM51で担体rayを準備可能 | M49のprogram担体 $d_{\rm prog}(\omega)$ | 4中央枝、2粒子位置 | 行分解bath、CNOT、直接枝decode |
| Q2-2 | M51は局所seedに使用可能。singlet交差統計はM48が別に準備 | M48切断後の各翼の局所信号 | 各翼2枝 | paired-Hopf準備、2翼局所合成、Bell監査 |
| Q3 | M51で初期rank-one集団を準備し、M37へ受渡し可能 | 準備終了面のM37標本包絡 $Z_{t_0}(\omega)$ | 初期M42位置。終時刻は同じ粒子を記録 | R172--R174の局所辺流、節正則化、有限衝突bath |

この表の共有は、現行M49とM48が同一ハードウェアであることを意味しない。Q2固定目標はそれぞれの根拠モデルと根拠結果から独立に判定し、同一装置への統合を要求しない。現行の有限担体と共通モジュールは将来の共通ハードウェア候補部品だが、統合結果ではない。M51は採用したdriftを持つ基礎開放モデル、M50は共通instrument仕様、M42はQ3だけの局在粒子輸送模型であり、いずれも単独では全周期装置ではない。M51のpump、sink、template、切断器を有限閉鎖Hamiltonianへ持ち上げたとは主張しない。全系列の信号準備、容量結合、作用殻、衝突bath、時計、記録、resetを1つの有限局所Hamiltonian周期へまとめるM0も、判定外の実装努力目標として未完成である。

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

## 2.4 M51有限実正準担体の共通開放ray準備

各試行の物理状態として $m$ 個の実正準対 $(Q,P)\in\mathbb R^{2m}$ を置き、その派生座標を

```math
z=\frac{Q+iP}{\sqrt{2\mathcal J_0}}
```

とする。$z$ は実担体の表示であって追加の実体ではない。目標templateも実装置の正準対 $(Q^w,P^w)$ で保持し、そこから得る非零派生座標 $w$、規格化方向 $c=w/\|w\|$、射影 $\Pi_c=cc^\dagger$ を使う。$c$ と $\Pi_c$ はtemplate設定および準備後集団統計の記述であり、各試行へ別に加える物理場ではない。

Hermitian生成子 $G(t)$ とそのunitary $U(t)$ に対し $c(t)=U(t)c(0)$、$\Pi_c(t)=c(t)c(t)^\dagger$ とする。M51の雑音零の採用開放方程式を

```math
\dot z
=
-\frac{i}{\mathcal J_0}G(t)z
+\lambda_{\rm prep}(t)
\left[
g(1-z^\dagger z)z
-\kappa(I-\Pi_c(t))z
\right]
```

と定める。$g,\kappa>0$、$\lambda_{\rm prep}\geq0$ である。第1項は実正準Hamiltonian伝播、動径項はpumpと飽和、射影直交項はtransverse sink、$\lambda_{\rm prep}$ は物理clockが開閉するportである。最小M51は決定論的であり、Langevin雑音を含まない。雑音付き拡張は別のモデルであり、R171の結論へ暗黙に含めない。

準備有効時間を

```math
\tau(t)=\int_{t_0}^t\lambda_{\rm prep}(s)\,\mathrm ds
```

とする。相互作用表示で $\widetilde z=ac+p$、$c^\dagger p=0$ と分解すると

```math
\frac{da}{d\tau}=g(1-\|\widetilde z\|^2)a,
\qquad
\frac{dp}{d\tau}
=
\left[g(1-\|\widetilde z\|^2)-\kappa\right]p,
```

```math
\frac{\|p(\tau)\|}{|a(\tau)|}
=
\frac{\|p_0\|}{|a_0|}e^{-\kappa\tau}
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
**定理（R171：M51共通開放ray準備の有限時間率と切断後輸送）**

$G_*$ 上で $q_*=(R_*^2-a_*^2)/a_*^2$ とする。M51の採用開放方程式では、各安全試行のray距離は

```math
D_{\rm pure}
\left(
\frac{zz^\dagger}{z^\dagger z},
\Pi_c(t)
\right)
\leq
\sqrt{q_*}e^{-\kappa\tau(t)}.
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
\sqrt{q_*}e^{-\kappa\tau(t)}.
```

また、$a_0\neq0$ の各試行は $\tau\to\infty$ で位相円へ収束し、動径誤差を含む収束率は有界seed集合上で $\min\{2g,\kappa\}$ により抑えられる。有限時刻 $t_{\rm cut}$ で $\lambda_{\rm prep}=0$ とした後は、各試行の実正準状態が $i\mathcal J_0\dot z=Gz$ に従い、R135の第2モーメント輸送が成り立つ。$G_*^c$ の確率は無反応質量として保持し、成功試行だけを結果分布として再規格化しない。
<!-- theorem-end:theorem -->

証明、複素式と等価な実変数方程式、pump・sink・template・clockの因果台帳は付録Mに置く。R171は採用開放方程式後の厳密結果である。pumpとsinkの環境自由度、仕事、熱、エントロピー生成を有限閉鎖系から導いた結果ではない。

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

R170は有限枝instrumentの共通定理であり、M37を前提にしない。Q1のR143、Q2-2のR155、Q3の固定時刻読出しはこの定理の特殊化または合成である。完全な証明と誤差台帳は付録Kに置く。

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

従って理想分布間の分離が誤差和より大きければ、有限装置でも区別可能性が残る。この系をR124/R125の識別とR155のBell監査へ共通に用いる。

## 2.10 Q2-4の直接モード候補

$n$ 量子ビット、有限長 $d$、固定有限普遍ゲート集合から与えられる回路を考え、$L=2^n$ とする。計算基底文字列 $x$ を共通担体の基底モードに対応させる。

```math
|x\rangle
\longleftrightarrow
d_x,
\qquad
d=(d_x)_{x\in\{0,1\}^n}\in\mathbb C^L.
```

計算基底入力を対応する1モードの有限作用初期状態として準備する。各1量子ビットまたは2量子ビットゲートを $L$ 次元空間へ恒等拡張し、R112の有限正準回路と時計窓で入力順に作用させる。積入力が途中で非分離になっても、状態を積因子またはClifford枝へ分解せず、同じ $L$ モード担体の係数として保持する。中間測定、枝選択、結果別再準備は行わない。

回路末尾でだけM50を $m=L$、$\Psi=I_L$、枝集合を計算基底文字列として特殊化し、R164の作用殻状態数とR170の有限時間再平衡化・記録を適用する。理想出力状態を $c_{\rm out}$ とすれば、正則化された枝分布は

```math
p_x^\delta
=
\frac{|(c_{\rm out})_x|^2+\delta q_x}{1+\delta}.
```

各ゲートの作用素誤差を $\varepsilon_g$、最終instrumentの正則化以外の全変動誤差を $\varepsilon_{M50}$ とすれば、三角不等式から

```math
D_{\rm TV}(p_{\rm phys},p_{\rm circuit})
\leq
\sum_{g=1}^{d}\varepsilon_g
+\varepsilon_{M50}
+\frac{\delta}{1+\delta}.
```

任意の有限 $n,d$ と任意の正の目標誤差について、有限個のゲート窓、有限正則化、有限混合時間を選べる。コンパイラが埋め込むのは入力回路の各ゲートと順序であり、最終出力分布またはその $2^n$ 個の確率を事前計算して装置係数へ書き込まない。これは旧Q2-3の有限回路構成であり、現行Q2-4では候補技術として扱う。

この構成の $L=2^n$ 個の信号モードと最終枝は、受動自由度としては許される。問題は、一般の密なゲートに許した $O(L^2)$ 個の校正窓、各モードの準備、末尾の全枝読出しが、指数個の個別設定または走査を必要とし得る点にある。受動モードと静的結合を一様な有限規則から生成し、外部制御channel数、命令数、制御列長、精度、反復回数、総時間を多項式に抑える証明はない。従ってQ2-4は未達である。未知量子入力、適応中間測定、誤り訂正、独立同分布型の反復標本もこの合成からは従わない。

## 2.11 物理的意味と限界

熱化終了後の局所記録生成子は、枝 $i$ に支持を持つ滑らかな関数 $d_i(x)$ と空の記録運動量 $P_{D_i}$ を使い、

```math
G_{\rm rec}=\sum_i d_i(x)P_{D_i}
```

と書ける。これは記録時刻の排他的粒子位置を読む。入力時刻以前の粒子軌道、初回到達率、吸収率、時間積分流束を与えない。

R170は、列挙した部品を1つの具体的有限局所Hamiltonianへ統合済みだと主張しない。現行の条件付き達成または部分達成は、この未統合部分を明示して判定する。一意エルゴードな外部scheduleまたは有限熱化から、結果列の独立同分布性や二項型有限標本揺らぎも従わない。
