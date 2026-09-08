@number: 2
@chapter: 本文
@title: 有限モード信号系と共通正準モジュール
@status: M54をQ1・Q2・Q3の共通有効信号--配置状態構成族として定義する。R164の共通条件付き容量、R161の静的/移動分布の整合、新R162の開放jump実現、R190/R179の静的選択浴、R170の吸収pointer固定を分離し、R181A--R181Dを準備、テンソル積状態の生成、永続ゲート、段階的射影選別読出しの正本として置く。

## 2.1 M54をQ1--Q3共通有効状態構成族とする範囲

M54は、有限個の実正準対から得る信号と有限配置変数を、準備、可逆操作、整合、作用殻受信機構、記録まで運ぶ共通有効状態構成族である。有限信号添字集合 $\Lambda$ と有限配置集合 $\mathcal I$ に対する完全状態を

```math
\Gamma_{54}^{(\Lambda,\mathcal I)}
=
(Z,S_{\rm port},G,W,J,A^\delta,X,Y,D,\tau,S_{\rm ref})
```

と書く。$Z\in\mathbb C^\Lambda$ は実正準対 $Q,P$ の派生表示

```math
Z=\frac{Q+iP}{\sqrt{2\mathcal J_0}}
```

であり、独立した複素実体ではない。$X\in\mathcal I$ は状態構成に応じて測定結果成分選択機構または空間素子上の実在粒子位置を表す。$S_{\rm port}$ は供給源／テンプレート接続端、$G,W$ は逆演算用補助記憶部と可逆作業領域、$J,A^\delta$ は未処理・正則化作用容量、$X$ は配置または静的選択変数、$Y$ はR170の吸収指針変数、$D$ は外部記録、$\tau$ は能動制御に必要な時計自由度である。確率的jump、作用殻混合、リセット、排熱を担う浴は能動状態へ列挙せず、明示した環境接続端として別に扱う。$S_{\rm ref}$ はM37局所ばね物理実装層を使う空間状態構成だけが開始面で使う作用保持機構であり、他状態構成では空でよい。

M54は共通の状態型、因果契約、接続端規約を定める有効状態構成族であって、全状態構成を同じ製造済み装置または同一パラメータで実装したという主張ではない。M54の統一は有効記述と接続部の統一であり、物理実装層の同一性や単一ミクロ装置統一とは別に判定する。Q1--Q3の有限能動部分系と明示的なHamiltonian無限浴を同じ反復周期へ統合するM0は、引き続きM54より強い未完成目標である。有限浴または有限閉鎖Hamiltonian全系への持上げはM0の条件ではない。

外部接続部は、供給源または物理テンプレートの注入、有限ゲート/状態構成名、対象添字、読出し添字、誤差予算、試行回数、時計自由度開始に限る。振幅表、確率表、モード別較正値、集団統計、試行中の状態依存制御を外部から与えない。ユニタリ、SWAP、容量保持機構、選別機構、記録は有限正準写像、テンプレート整列と方向を変えない振幅再調整は採用開放方程式、R161は配置分布の整合、R162はQ3の開放jump実現、R190/R179はQ1/Q2の静的選択浴、R170は吸収指針変数固定として扱う。

| 系列 | M54状態構成 | 信号／配置 | 準備・操作 | 整合／出力 |
|---|---|---|---|---|
| Q1 | W型2モード静的状態構成 | $|\Lambda|=2$、2結果 $X$ | R181A、R140 | R164、R190、R179、R170、R143 |
| Q2-1 | 2ビット記憶部の静的状態構成 | $|\Lambda|=4$、段階的射影選別 $X$ | R181B、R181C | R164、R190、R179、R170、R181D |
| Q2-2 | 2ビット記憶部＋設定先行受信機構 | $|\Lambda|=4$、2翼局所 $X$ | R181B/R181C、R180 | 局所R164/R190/R179/R170、R180C |
| Q2-3 | 3ビット永続記憶部 | $|\Lambda|=8$ | R181Bを2回、R181C、R177 | R164、R190、R179、R170、R181D |
| Q2-4 | 一般 $n$ ビット記憶部 | $|\Lambda|=2^n$ | R181Aの振幅再調整用接続端、R179、R181C | R164、R190、R170、R181D |
| Q3 | 空間移動状態構成 | $\Lambda=\mathcal I=V$、$\Psi=I$ | R181Aを準備接続端として使用可、必要時M37/R184 | R161移動、R162の一般特殊化、R185、同じ $X_T$ を記録 |

Q1/Q2の静的状態構成では、各操作面または末端読出し面でR164の条件付き分布へ有限時間整合し、必要な結果成分を固定して記録する。Q3の空間状態構成では、開始面で同じ条件付き分布を準備した後、信号確率流に従うR161移動特殊化が同じ粒子を全時刻輸送する。したがって静的測定と空間運動は別の確率原理ではなく、同じ整合定理の $j=0$ と $j\neq0$ の特殊化である。

M37はM54へ吸収しない。Q3ではM54空間信号部分系を局所位置ばねで有限時間近似し、R86からR184へ誤差を渡す。Q1ではR187の弱結合W型族に限り、零傾斜最低2正常モードをM54のW2静的状態構成の制御用信号系へ正準同定する。M54のポンプ、作用殻、衝突、記録をM37から導出したとはしない。W型入力をQ2各目標の必須前提へ追加せず、固定目標と達成ラベルもこの物理接続だけでは変更しない。

## 2.2 有限正準信号の辺代数

有限グラフ $\mathcal G=(\Omega,E)$ の各頂点 $z$ に実正準対 $(Q_z,P_z)$ と複素信号

```math
d_z=\frac{Q_z+iP_z}{\sqrt{2\mathcal J_0}}
```

を置く。全信号作用は $J_{\rm sig}=\mathcal J_0d^\dagger d$ である。時間依存エルミート行列 $h(t)$ に対するハミルトニアン

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

有限正準信号の可逆有効力学は、有限配置グラフ上の頂点作用項と差モード辺生成子の有限プログラムとして表せる。連結グラフでは隣接2モード交換と局所位相から $U(L)$ の任意の有限ユニタリを有限積として合成できる。さらに、固定有限個の信号記憶部、時計、比較対象、安全領域、記録結果成分、テンプレートについて、次を有限個の正準対と滑らかな有限時計窓で実装できる。

1. 指定した有限ユニタリ列の自律化と有限制御誤差評価。
2. 互いに素な安全領域の滑らかな比較と、境界失敗を含む正式な無反応結果。
3. 空記憶部と使用済み記憶部を区別した正準SWAPおよび結果別テンプレート交換。
4. 各結果成分だけに支持を持つ局所記録と、外部履歴を残した内部作業記憶部の逆計算。

全入力、時計、使用済み素子、無反応、外部記録を含む拡大写像は1対1に保てる。Q1、Q2、Q3の違いは、頂点集合、信号の物理的由来、係数、時計窓、排他的出力の実装にある。本定理だけから結果確率、Born型状態数、粒子位置分布、無期限リセットは従わない。
<!-- theorem-end:theorem -->

## 2.3 R112の役割境界

R112が現行主線へ供給するのは次の部品である。

1. 局所位相回転と隣接 $QQ+PP$ 交換による有限ユニタリ回路。
2. 時計窓の自律化と有限誤差制御。
3. 外部から与えた制御値に対する滑らかな比較器と正式な無反応領域。
4. 正準SWAP、局所記録、テンプレート交換、内部逆計算。

作用区間と一様選択器角から長期Born型頻度を得る旧経路は現行定理に使わない。R112は作用殻ファイバー内の平衡化も、結果列の独立同分布性も証明しない。旧正準標本器の確率生成経路は `notes/superseded_m35_born_sampler.md` に整理し、非確率的な制御・比較・記録内容はR112へ吸収する。

固定ベンチマークのプログラム順序を外部時刻割当で作ることは許す。この時刻割当は入力条件の提示であり、同じ試行のBorn型出力を生成する機構ではない。

## 2.4 M54物理テンプレート-接続端準備

各試行の物理状態として $m$ 個の実正準対 $(Q,P)\in\mathbb R^{2m}$ を置き、その派生座標を

```math
z=\frac{Q+iP}{\sqrt{2\mathcal J_0}}
```

とする。$z$ は実信号系の表示であって追加の実体ではない。目標テンプレートも実装置の正準対 $(Q^w,P^w)$ で保持し、そこから得る非零派生座標 $w$ を直接結合器へ入れる。規格化方向 $c=w/\|w\|$ と射影 $\Pi_c=cc^\dagger$ は解析記号に限り、制御器が状態依存除算を行って作る物理記憶部ではない。

エルミート生成子 $G(t)$ とそのユニタリ $U(t)$ に対し $w(t)=U(t)w(0)$ とする。目標作用 $J_*>0$ を固定し、M54の雑音零の採用開放方程式を

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

と定める。$g,\kappa>0$、$\lambda_{\rm prep}\geq0$ である。第1項は実正準ハミルトニアン伝播、動径項はポンプと飽和、中括弧は非規格化テンプレートだけで書いた横方向排出先、$\lambda_{\rm prep}$ は物理時計自由度が開閉する接続端である。$\kappa=0$ はR181Dが使う方向を変えない振幅再調整用接続端である。最小M54は決定論的であり、Langevin雑音を含まない。

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

となる。初期分布 $\mu_0$ は目標階数1分布そのものとせず、固定 $a_*,R_*>0$ に対する安全事象

```math
G_*
=
\{|c^\dagger\widetilde z_0|\geq a_*\}
\cap
\{\|\widetilde z_0\|\leq R_*\}
```

を定める。$G_*^c$ は初期種失敗として完全結果集合の無反応へ残す。目標依存の準備分布は、同じ初期分布を上のドリフトで押し出した $(\Phi_c^t)_\#\mu_0$ であり、階数1統計を初期測度へ直接置いたものではない。

<!-- theorem-start:theorem -->
**定理（R181A：物理テンプレート-接続端共通状態方向準備）**

$G_*$ 上で $q_*=(R_*^2-a_*^2)/a_*^2$ とする。M54の採用開放方程式では、各安全試行の状態方向距離は

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

また、$a_0\neq0$ の各試行は $\tau\to\infty$ で作用 $J_*$ の位相円へ収束し、動径誤差を含む収束率は有界初期種集合上で $\min\{2gJ_*,\kappa\|w\|^2\}$ により抑えられる。有限時刻 $t_{\rm cut}$ で $\lambda_{\rm prep}=0$ とした後は、各試行の実正準状態が $i\mathcal J_0\dot z=Gz$ に従い、R135の第2モーメント輸送が成り立つ。$G_*^c$ の確率は無反応質量として保持し、成功試行だけを結果分布として再規格化しない。物理結合器は $w$ だけを読み、$w/\|w\|$ を生成しない。
<!-- theorem-end:theorem -->

証明、複素式と等価な実変数方程式、ポンプ・排出先・テンプレート・時計自由度の因果台帳は付録Mに置く。R181Aは採用開放方程式後の厳密結果である。ポンプと排出先を共通の明示的Hamiltonian無限浴へ接続した縮約、仕事、熱、エントロピー生成は未導出であるが、有限浴への持上げ自体は固定目標またはM0の必要条件ではない。

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

各試行の信号が同じ有限次元ユニタリ $U(t)$ により $Z(t)=U(t)Z(0)$ と発展するなら、

```math
C_Z(t)=U(t)C_Z(0)U(t)^\dagger
```

であり、トレース、正値性、階数は保存される。$i\mathcal J_0\dot U=G(t)U$ なら

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

## 2.6 一般状態方向平均から共通結果統計への受渡し

安全事象 $G$ 上の有限信号 $Z$ に対し、失敗質量を捨てない安全状態方向平均を

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
**定理（R168：一般状態方向平均から共通結果統計への受渡し）**

各安全試行にM54の条件付き作用容量状態構成を適用し、安全事象外を無反応へ送ると、完全結果分布は

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
4. 安全な近似状態方向が目標状態方向から純粋状態距離 $s$ 以内なら、対応する結果分布の全変動距離は $s/(1+\delta)$ 以下である。

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

で抑えられる。R168はM37を前提とせず、Q1・Q2の静的状態構成とQ3の空間状態構成が同じ単一試行信号から条件付き結果統計を読むときの共通統計写像である。証明と可変作用反例は付録Fに置く。

## 2.7 M54共通条件付き作用容量と結果別状態数

非零有限信号 $v\in\mathbb C^m$、等長埋込み $\Psi:\mathbb C^m\to\mathbb C^L$、排他的結果成分 $i\in\mathcal I$ を考える。正の基準分布 $q_i>0$、$\sum_iq_i=1$ と正則化 $\delta>0$ を固定し、

```math
J_i(v)=\mathcal J_0|(\Psi v)_i|^2,
\qquad
A_i^\delta(v)=J_i(v)+\delta q_iJ_{\rm sig}(v)
```

と置く。各結果成分に2つの非負作用を持つ排他的作用殻を置く。

<!-- theorem-start:theorem -->
**定理（R164：有限信号作用のBorn型殻状態数）**

上の仮定の下で、全結果成分を同じLiouville基準分布で数えると結果別状態数は

```math
\Omega_i^\delta(v)
=
\frac{(2\pi)^2}{J_{\rm ref}}A_i^\delta(v)
```

であり、単一Liouville基準分布を1回だけ規格化すると

```math
\pi_i^\delta(v)
=
\frac{\Omega_i^\delta(v)}{\sum_j\Omega_j^\delta(v)}
=
\frac{|(\Psi v)_i|^2/(v^\dagger v)+\delta q_i}{1+\delta}
```

となる。零信号、安全閾値未満、有限幅遷移域は無反応 $\varnothing$ へ送る。一般に各明反応結果成分が $q$ 個の独立な作用分配方向を持てば $\Omega_i\propto(A_i^\delta)^q$ であり、全容量族でBorn型線形則を保つのは $q=1$ に限る。
<!-- theorem-end:theorem -->

作用殻を消去する表示では

```math
E_i^\delta(v)=-\Theta\log\pi_i^\delta(v)
```

を条件付き中間状態有効自由エネルギーとして使う。状態数を残す表示と消去表示は同値であり、同じ縮約分配関数へ $\Omega_i^\delta e^{-E_i^\delta/\Theta}$ を入れて二重計数してはならない。

## 2.8 R161の共通整合とR162の開放jump実現

有限配置集合 $\mathcal I$ 上の正の時間依存確率分布 $\pi_i(t)>0$ を考える。辺ごとに反対称確率流と対称活動量

```math
j_{ij}=-j_{ji},
\qquad
t_{ij}=t_{ji}\geq |j_{ij}|
```

を取り、

```math
\dot\pi_i
=
\sum_jj_{ji}
```

を仮定する。前向き・共通の確率分布の後向き率を

```math
k^+_{i\to j}
=
\frac{t_{ij}+j_{ij}}{2\pi_i},
\qquad
k^-_{i\to j}
=
\frac{t_{ij}-j_{ij}}{2\pi_i}
```

と置く。

<!-- theorem-start:theorem -->
**定理（R161：有限配置の確率流・活動量整合）**

上の仮定の下で $k^\pm$ は非負であり、

```math
\pi_i k^+_{i\to j}
-
\pi_j k^+_{j\to i}
=
j_{ij}
```

なので、$\pi(t)$ は前向きマスター方程式の解である。初期分布が $\pi(0)$ なら全有限時刻で $P(X_t=i)=\pi_i(t)$ が成り立つ。同じ経路分布のBayes反転は

```math
\frac{\pi_jk^+_{j\to i}}{\pi_i}
=
k^-_{i\to j}
```

を満たす。

静的状態構成では $j=0$ とし、

```math
t_{ij}
=
2\kappa_Xa_{ij}\sqrt{\pi_i^\delta\pi_j^\delta}
```

を選ぶと

```math
k_{i\to j}
=
\kappa_Xa_{ij}
\sqrt{\frac{\pi_j^\delta}{\pi_i^\delta}}
```

となる。有限連結グラフ、$\pi_i^\delta\geq m_\delta=\delta q_{\min}/(1+\delta)$ では、この静的鎖の唯一の定常分布は $\pi^\delta$ であり、

```math
D_{\rm TV}(p_{\tau_X},\pi^\delta)
\leq
C_\delta e^{-\lambda_\delta\tau_X},
```

```math
\lambda_\delta
=
\kappa_Xa_{\min}m_\delta\lambda_G,
\qquad
C_\delta
=
\frac12\sqrt{m_\delta^{-1}-1}.
```

またR164の理想結果重みとの差は $\delta/(1+\delta)$ 以下である。

空間状態構成では $\Lambda=\mathcal I=V$、$\Psi=I$ とし、信号の連続方程式から得る $j$ と正の対称活動量 $t$ を代入する。付録Nの選択では旧R183の移動整合率がそのままR161の特殊化として得られる。
<!-- theorem-end:theorem -->

<!-- theorem-start:theorem -->
**定理（R162：局所有向率の開放Poisson-jump実現）**

固定有限グラフ、固定有限時間 $T$ 上で、R161が与える有向率 $k_{i\to j}(t)\geq0$ が可測かつ

```math
M_*=
\sup_{0\leq t\leq T}
\max_i\sum_{j\ne i}k_{i\to j}(t)
<\infty
```

を満たすとする。各有向辺へ独立なunit-rate Poisson reservoirを接続し、時刻 $t$ に配置が $i$ のとき、reservoir mark $u$ が $0<u<k_{i\to j}(t)$ を満たす流入 eventで $i\to j$ を起こす。この古典開放jump模型は固定有限時間で非爆発であり、生成子は

```math
(L_tf)(i)
=
\sum_{j\ne i}
k_{i\to j}(t)
[f(j)-f(i)]
```

である。従って周辺分布はR161の前向きmaster equationに厳密に従う。同じ前向き経路法則のBayes反転から得る後向き率はR161の $k^-$ と一致し、未来から作用する第2浴を必要としない。

Poisson reservoirは本稿で採用する明示的な古典開放ミクロ方程式である。これを有限衝突Hamiltonian列または特定のHamiltonian無限浴から導くことは固定目標の必要条件とせず、有限閉鎖系への持上げは強化結果として論文外メモへ分離する。R162はQ3の移動過程を担い、Q1/Q2の静的平方根選択の物理実現はR190/R179へ分離する。
<!-- theorem-end:theorem -->

R161は静的・移動の率構成を共通に保つが、物理実現を一種類の有限衝突装置へ統一しない。Q3では新R162の開放jump過程を直接使う。Q1/Q2の静的状態構成では、作用殻状態数をR164、平方根核の具体的混合・開口をR190、反復時のfreshnessをR179が担う。旧R162の有限衝突・熱的特殊化は有限閉鎖実装の強化結果として退役メモに保存する。

### 2.8.1### 2.8.1 R190A--R190C：2作用LC殻Drude混合と静的平方根衝突接続

R164だけからR161静的特殊化の平方根分割は一意に従わない。ここでは、固定済み正作用容量を2作用LC殻へ渡し、無限自由度の等方Drude浴で作用分配だけを混合した後、対称な作用開口を使う一つの具体的十分条件を与える。R190系列はR162を置き換えず、静的 $j=0$ の平方根率に対する作用殻明示表示の物理接続だけを担う。

<!-- theorem-start:theorem -->
**定理（R190A：2作用LC殻の作用保存型Drude混合）**

固定済み正作用容量 $\widehat A_i>0$ を取り、2つの同周波数LCモードの作用を $K_i,I_i\geq0$ として

```math
K_i+I_i=\widehat A_i
```

とする。対応するSchwinger型作用方向を $\boldsymbol n_i\in S^2$ とし、各生成子成分へ同型な無限古典調和浴をcounterterm込みで結合する。浴の記憶 核を

```math
\Gamma_{\rm D}(t)
=
\frac{g_{\rm D}}{\tau_{\rm D}}
e^{-t/\tau_{\rm D}},
\qquad
g_{\rm D}>0,
\quad
\tau_{\rm D}>0
```

とし、初期浴を固定した作用方向に条件付けたFDT整合Gaussian平衡状態から取る。

このとき全拡大Hamiltonian軌道で

```math
K_i(t)+I_i(t)=\widehat A_i
```

が厳密に保存される。浴自由度を消去した縮約運動は指数記憶を持つ一般化Langevin方程式であり、reaction variableを加えると有限次元のDrude fast--slow系へ書き直せる。

その短記憶極限を回転拡散係数 $D_{\rm rot}>0$ の球面拡散 $\boldsymbol N_t$、

```math
\operatorname{Gen}(\boldsymbol N)
=
D_{\rm rot}\Delta_{S^2}
```

とする。固定有限時間 $T$ では、同一Brownian運動上のcouplingを選んで

```math
W_1
\left(
\mathcal L(\boldsymbol n_i^{\tau_{\rm D}}(T)),
\mathcal L(\boldsymbol N_T)
\right)
\leq
C_{\rm str}
\left(
g_{\rm D},
D_{\rm rot}T
\right)
\sqrt{
D_{\rm rot}\tau_{\rm D}
}
```

とできる。$C_{\rm str}$ の一つの保守的明示式は付録Sに置く。有限長・有限モード浴への持ち上げは本定理の主張に含めない。
<!-- theorem-end:theorem -->

<!-- theorem-start:lemma -->
**補題（R190B：2作用分配の有限時間一様化）**

```math
X_i
=
\frac{I_i}{\widehat A_i}
=
\frac{1-n_{i,z}}2
\in[0,1]
```

とする。R190Aの理想回転拡散極限では

```math
\mathcal L_X
=
D_{\rm rot}
\left[
x(1-x)\partial_x^2
+
(1-2x)\partial_x
\right]
```

であり、唯一の定常分布は $U[0,1]$、スペクトルギャップは $2D_{\rm rot}$ である。$S=D_{\rm rot}T$、$q=e^{-4S}$ とすると任意の初期作用分配について

```math
D_{\rm TV}
\left(
\mathcal L(X_i(T)),
U[0,1]
\right)
\leq
\varepsilon_{\rm mix}^{190}(S)
:=
\min
\left\{
1,
\frac{\sqrt{q(3-q)}}{2(1-q)}
\right\}.
```

有限記憶 Drude系では

```math
W_1
\left(
\mathcal L(X_i^{\tau_{\rm D}}(T)),
U[0,1]
\right)
\leq
\eta_{190}(T),
```

```math
\eta_{190}(T)
=
\frac12
C_{\rm str}
\left(
g_{\rm D},
D_{\rm rot}T
\right)
\sqrt{
D_{\rm rot}\tau_{\rm D}
}
+
\varepsilon_{\rm mix}^{190}
\left(
D_{\rm rot}T
\right).
```

従って

```math
\sup_{0\leq x\leq1}
\left|
P
\left(
X_i^{\tau_{\rm D}}(T)\leq x
\right)
-
x
\right|
\leq
\sqrt{2\eta_{190}(T)}.
```
<!-- theorem-end:lemma -->

<!-- theorem-start:theorem -->
**定理（R190C：対称作用開口から静的平方根核への接続）**

正作用容量 $\widehat A_i,\widehat A_j>0$ と対称開口定数 $c_{ij}^{\rm ap}=c_{ji}^{\rm ap}>0$ を固定し、

```math
0
\leq
\alpha_{ij}
:=
c_{ij}^{\rm ap}
\sqrt{
\frac{\widehat A_j}{\widehat A_i}
}
\leq1
```

とする。結果成分 $i$ の混合作用 $I_i=\widehat A_iX_i$ に対し、理想通過条件を

```math
I_i^2
<
\left(
c_{ij}^{\rm ap}
\right)^2
\widehat A_i\widehat A_j
```

とする。R190Bの混合窓後に作用する有限Hamiltonian scattererの通過・反射誤差を $\varepsilon_{\rm sc}$ とすれば、

```math
\left|
P(i\to j)
-
c_{ij}^{\rm ap}
\sqrt{
\frac{\widehat A_j}{\widehat A_i}
}
\right|
\leq
\sqrt{
2\eta_{190}(T)
}
+
\varepsilon_{\rm sc}.
```

理想極限では

```math
\widehat A_iP(i\to j)
=
\widehat A_jP(j\to i)
=
c_{ij}^{\rm ap}
\sqrt{
\widehat A_i\widehat A_j
}.
```

特に $\widehat\pi_i=\widehat A_i/\sum_k\widehat A_k$ とし、試行 frequency $\nu_{ij}$ を

```math
\nu_{ij}c_{ij}^{\rm ap}
=
\kappa_Xa_{ij}
```

と校正すれば、各試行前の履歴条件付き作用比分布が同じ再混合誤差内にある場合に

```math
k_{i\to j}
=
\kappa_Xa_{ij}
\sqrt{
\frac{\widehat\pi_j}{\widehat\pi_i}
}
```

というR161静的平方根率を有限条件付き核誤差で回収する。反復衝突列のMarkov化にはこの履歴条件付き再混合を別条件として要求し、R190A--R190Cだけから独立同分布のfreshnessを主張しない。
<!-- theorem-end:theorem -->

完全証明、$C_{\rm str}$、Jacobi縮約、CDF評価、作用開口scatterer、反復時の再混合条件、正則化資源は付録Sに置く。R162の一般有向率、有限骨格全履歴、時間依存率、非零確率流、Q3移動特殊化は従来どおりR162が担う。

## 2.9 R170：固定作用容量入力の静的選択・吸収指針変数固定

R170を、Q1、Q2の段階的射影選別、R180Aの中央潜在選択、R180Cの局所読出し、Q3固定時刻診断で共有する静的選択・固定の正本とする。上流は正の固定済み作用容量 $\widehat A_i$ を保持し、R164/R190/R179が与える静的選択過程を有限時間走らせる。選択分布が目標容量比へ近づいた後は選択浴を切り、結果を開放吸収指針変数へ写して固定する。有限閉鎖Hamiltonianで入射停止、辺閉鎖、平坦域保持、全微視的履歴の1対1保存まで構成することはR170の必要条件にしない。

<!-- theorem-start:theorem -->
**定理（R170：固定作用容量入力の静的選択・吸収指針変数固定）**

有限結果集合 $\mathcal I$ に対して

```math
\widehat A_i>0,
\qquad
\widehat\pi_i
=
\frac{\widehat A_i}{\sum_j\widehat A_j}
```

を固定する。時刻 $t_s$ で静的選択変数 $X$ が

```math
D_{\rm TV}
\left(
\mathcal L(X_{t_s}),
\widehat\pi
\right)
\leq
\varepsilon_{\rm sel}
```

を満たすとする。$t_s$ で選択浴を切り、指針変数 $Y\in\{\varnothing\}\cup\mathcal I$ を $Y=\varnothing$ から開始する。固定区間では現在の $X=i$ に対して $\varnothing\to i$ だけを共通捕獲率 $\gamma>0$ で許し、一度 $Y=i$ になった後は吸収状態とする。

固定時間 $T_L$ の後、

```math
P(Y=\varnothing)
=
e^{-\gamma T_L}
```

であり、指針変数の有限漏れまたは捕獲実装誤差を $\varepsilon_{\rm ptr}$ とすれば

```math
D_{\rm TV}
\left(
\mathcal L(Y),
\widehat\pi
\right)
\leq
\varepsilon_{\rm sel}
+
e^{-\gamma T_L}
+
\varepsilon_{\rm ptr}.
```

安全な吸収状態 $Y=i$ は後段の記録、制御付き射影選別機構、転送を直接制御できる。外部記録はR112または系列固有機構、容量生成と保持はR181D、R189A、R180Aなどの上流結果が担い、同じ偏差をR170へ重複加算しない。成功試行だけを再規格化しない。
<!-- theorem-end:theorem -->

**系（R170選択結果の局所記録）**

R170の吸収指針変数をR112または系列固有記録機構へ誤差 $\varepsilon_{\rm rec}$ 以内で写すと、外部観測分布の全変動誤差は

```math
\varepsilon_{170}^{\rm obs}
\leq
\varepsilon_{\rm sel}
+
e^{-\gamma T_L}
+
\varepsilon_{\rm ptr}
+
\varepsilon_{\rm rec}
```

で抑えられる。記録は固定済み結果のデータ処理であり、Born型重みを新たに生成しない。

**系（共通選択・記録安定性）**

理想分布 $p,p'$ と実分布 $q,q'$ が $D_{\rm TV}(q,p)\leq\varepsilon$、$D_{\rm TV}(q',p')\leq\varepsilon'$ を満たせば

```math
D_{\rm TV}(q,q')
\geq
D_{\rm TV}(p,p')-\varepsilon-\varepsilon'.
```

従って理想分布間の分離が誤差和より大きければ、開放指針変数固定後にも区別可能性が残る。この系をR124/R125の識別とR180CのBell監査へ共通に用いる。

## 2.10 ## 2.10 M54の一様記憶部、接続端、貯蔵部

$n$ 量子ビット、深さ $d$、固定有限普遍ゲート集合から与えられる回路を考え、$L=2^n$ とする。M54では計算基底文字列 $x$ を受動信号モードへ直接対応させる。

```math
|x\rangle
\longleftrightarrow
Z_x,
\qquad
Z=(Z_x)_{x\in\{0,1\}^n}\in\mathbb C^L.
```

M54の能動部は信号、逆演算用補助記憶部、選別機構用作業領域、方向を変えない振幅再調整接続端、未処理／正則化容量指針変数、一様ゲートバス、吸収指針変数、出力記録、時計自由度を持つ。作用殻混合、再混合、リセット、散逸履歴はR190/R179の環境接続部へ置く。内部の受動自由度、静的結合、状態容量、受動並列度は $2^n\operatorname{poly}(n,d)$ まで許す。一方、外部プログラムが指定するのはゲート種、1個または2個の対象量子ビット、ゲート順序、現在読む出力ビット、未使用化の回、素子添字、時計自由度窓だけである。$2^n$ モードの列挙、モード別初期化・較正・読出し、指数長の係数表、回路別配線、出力確率の事前計算を許さない。

M54はR181Bの反復テンソル積状態の生成を一般 $n$ へ延長しない。R179の開放リセット後、定数次元供給源を $0^n$ 根モードへ接続して計算基底入力を作る。別の基底入力は回路先頭の $X$ ゲートで作る。ゲート列はR181C、末端ビット列はR181D、結果相関履歴の流出排出と補助部リセットはR179が担う。

## 2.11 R181B：Q1-接続端可逆テンソル積状態の生成

固定された2入力または3入力について、Q1型接続端の信号を $a,b$、未使用共同記憶部を $Z$、逆演算用補助記憶部を $G$ とする。R112の三次乗算パルスを有限列 $S_0$ として使い、係数を測定または外部転記せず

```math
(a,b,0,0,W_0)
\longmapsto
(a,b,Z=a\otimes b,G=\overline{a\otimes b},W_1)
```

を作る。

<!-- theorem-start:theorem -->
**定理（R181B：非規格化Q1-接続端可逆テンソル積状態の生成）**

$a,b$ が固定安全集合にあり、共同記憶部と逆演算用補助記憶部が指定未使用幅以内なら、有限個の実正準対、有限時計自由度窓、R112型の可逆乗算パルスにより上の写像を任意の誤差 $\eta_{\rm lift}>0$ 以内で実装できる。拡大状態 $(a,b,Z,G,W)$ 上の写像は1対1で、逆時計自由度列により入力と作業領域を回収できる。制御器は $a_j,b_k$ を読み出さず、積係数表を入力しない。3入力は同じ持ち上げを2回使って作る。本結果は入力数を固定したQ2-1--Q2-3の構成であり、一般 $n$ の多項式資源テンソル積準備を主張しない。
<!-- theorem-end:theorem -->

詳細なパルス列、参照位相、有限誤差は付録Cに置く。

## 2.12 R181C：永続記憶部上の一様局所ゲート合成

対象量子ビット集合 $S$ の大きさを $k\in\{1,2\}$ とし、$g$ を固定有限ゲート集合の $2^k$ 次元ユニタリとする。非作用ラベルを $r\in\{0,1\}^{n-k}$ と書き、同じ局所生成子 $h_g$ を全部分系へ置く。

```math
H_{g,S}
=
\bigoplus_r h_g^{(r)},
\qquad
U_{g,S}=g_S\otimes I_{\bar S}.
```

<!-- theorem-start:theorem -->
**定理（R181C：永続記憶部上の一様局所ゲート合成）**

各部分系ブロックが同じ局所規則から生成され、実装ブロック $\widetilde g_r$ が一様に $\|\widetilde g_r-g\|\leq\eta_g$ を満たし、異なる部分系間の漏れの作用素ノルムが $\eta_{\rm leak}$ 以下とする。このとき1個の共有時計自由度窓で全非作用部分へゲートを作用でき、

```math
\|\widetilde U_{g,S}-U_{g,S}\|
\leq
\eta_g+\eta_{\rm leak}
```

である。ブロック数による和は生じない。深さ $d$ のゲート列では、全ゲートの大域位相を除いた誤差は各窓の作用素ノルム誤差の和以下である。固定ゲート集合なら、対象指定、制御チャネル、命令数は $n,d$ の多項式、静的部分系結合は指数的でも一様有限規則から生成できる。
<!-- theorem-end:theorem -->

固定 $n=2,3$ では同じ定理がCNOT、局所操作、逆演算の有限列を与える。一般 $n$ では上の部分系一括作用を使う。いずれも中間測定、共同モーメントへの置換、再準備を行わず、同じ $Z$ を全ゲート窓で保持する。3次元Euclid空間への局所埋込み、指数個の静的結合の総製造費、全結合を個別に調整する方法は主張しない。

## 2.13 M54共通射影容量・選別機構：容量固定・R170選択固定・可逆選別

出力ビット $k$ に対する計算基底射影を $P_{k,0},P_{k,1}$ とし、

```math
P_{k,0}+P_{k,1}=I,
\qquad
P_{k,0}P_{k,1}=0
```

とする。容量指針変数へ保持する作用を

```math
J_{k,b}(Z)=\mathcal J_0Z^\dagger P_{k,b}Z
```

とする。信号と作業領域の2貯蔵部上に

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
**補題（直交射影子作用保持機構と対合 選別機構）**

上の $F_{k,b}$ は

```math
F_{k,b}^\dagger F_{k,b}=I,
\qquad
F_{k,b}^2=I
```

を満たし、未使用の作業領域貯蔵部に対して

```math
F_{k,b}(Z,0)
=
(P_{k,b}Z,P_{k,1-b}Z)
```

と作用する。容量固定機構を信号に対する制御剪断として実装すれば、未使用容量運動量上で $J_{k,0},J_{k,1}$ を指針変数へ保持し、理想信号 $Z$ を変更しない。計算基底ビット射影子と選別機構はビットラベルだけから一様に生成され、$2^n$ 成分の列挙を必要としない。
<!-- theorem-end:lemma -->

この補題は確率的な結果選択を行わない。確率的な排他的選択と固定はR170が担う。以後、射影測定で共有する操作列を **共通射影選別機構** と呼ぶ。段階は

1. この節の未処理射影子容量固定機構、
2. R170による排他的選択と選択結果の固定、
3. 必要ならR112または系列固有機構による局所記録、
4. 固定後の制御付き射影選別機構、
5. 選択後信号だけへの方向を変えない振幅再調整、
6. 次節点または外部接続端への転送

である。R170は段階2の共通親、R181Dは1--6を段階的に合成する下流定理、R180Aは1--2と同じ対合選別機構を中央潜在結果成分のブロック受け渡しへ使う兄弟特殊化である。外部記録の有無は結果確率を変える操作として扱わない。

## 2.14 R181D：M54段階的射影選別・測定後状態受渡し定理

第 $k$ 段、履歴節点 $u$ の入力を $Z_u\neq0$ とし、直交射影 $P_{u,0},P_{u,1}$ に対する未処理容量を

```math
J_{u,b}=\mathcal J_0Z_u^\dagger P_{u,b}Z_u,
\qquad
J_\Sigma=J_{u,0}+J_{u,1}
```

とする。作用殻へ渡す正則化容量は、固定 $q_0,q_1>0$、$q_0+q_1=1$ に対し

```math
A_{u,b}^\delta=J_{u,b}+\delta q_bJ_\Sigma
```

である。R170は $b$ を確率 $(p_{u,b}+\delta q_b)/(1+\delta)$ で選ぶ。カットオフは除算せず、未処理比較 $J_{u,b}\gtrless\tau J_\Sigma$ を用いる。幅 $\gamma J_\Sigma$ の保護帯とR170 指針変数未捕獲は正式な無反応 $\varnothing$ へ送る。吸収指針変数を固定した後に選別機構 $F_{u,b}$ を作用し、非選択成分を作業領域へ保持する。選択成分はR181Aの $\kappa=0$ 方向を変えない振幅再調整用接続端

```math
\dot Z=g(J_*-Z^\dagger Z)Z
```

で標準作用へ戻す。$J_{u,b}\geq\tau J_\Sigma$ の下限から固定再調整時間を選び、未知の $p_{u,b}$ に依存するスクイーズを制御器へ入れない。

<!-- theorem-start:theorem -->
**定理（R181D：M54段階的射影選別・測定後状態受渡し定理）**

理想節点測定機構を深さ $m$ まで合成すると、葉 $y=(y_1,\ldots,y_m)$ の確率は

```math
\prod_{k=1}^m p_{k,y_k}
=
\frac{
\|P_{m,y_m}\cdots P_{1,y_1}Z_0\|^2
}{
\|Z_0\|^2
}
```

となり、指定段階的射影選別のBorn分布に一致する。入力分布誤差を $\varepsilon_{\rm in}$、安全履歴上の第 $k$ 節点実装誤差を $\bar\varepsilon_k$ とすれば、無反応を含む完全結果分布は

```math
D_{\rm TV}(P_{\rm out},P_{\rm Born})
\leq
\varepsilon_{\rm in}
+\frac{m\delta}{1+\delta}
+2m(\tau+\gamma)
+\sum_{k=1}^m\bar\varepsilon_k.
```

$\bar\varepsilon_k$ にはR170選択・固定、必要な局所記録、制御付き選別機構、方向を変えない振幅再調整、転送を各1回だけ含める。選別機構作用素誤差が $\eta_F<\sqrt\tau$ なら、選択後の規格化状態方向誤差は
$2\eta_F/(\sqrt\tau-\eta_F)$ 以下である。さらに階数1 節点
$P_{u,b}=|b_u\rangle\langle b_u|$ では、安全な結果成分の理想選択後信号は
$P_{u,b}Z_u=\alpha_b|b_u\rangle$ である。従って方向を変えない振幅再調整後も同じ状態方向を保ち、条件付き規格化第2モーメントは

```math
D_{\rm tr}
\left(
C_{u,b}^{\rm out},
P_{u,b}
\right)
\leq
\varepsilon_{u,b}^{\rm state},
\qquad
\varepsilon_{u,b}^{\rm state}
\leq
\frac{2\eta_F}{\sqrt\tau-\eta_F}
```

を満たす。同じ単一試行信号を次節点へ直接渡せ、外部トモグラフィー、係数読出し、結果依存の状態再準備を必要としない。有限選別機構誤差のない理想節点ではこの条件付き状態誤差は零である。成功試行だけを再規格化しない。
<!-- theorem-end:theorem -->

R181DはQ1の深さ1、Q2-1の深さ2、Q2-3の深さ3、Q2-4の深さ $n$ に同じ節点機構を使う。Q1の階数1特殊化では、結果分布だけでなく安全な結果成分の測定後信号もこの節点の選別機構と方向を変えない振幅再調整から直接得る。最終分布を段ごとの規格化成功分布へ比較せず、実際の初期信号が持つBorn分布と完全結果分布を末端で一度だけ比較する。

## 2.15 R178Dの本線退役：有限閉鎖リセットの情報容量境界

旧R178Dは、結果を保持したまま有限閉鎖系の全補助自由度を同じ初期点へ戻すことの制約と、使用済み側に必要な情報容量下界を与えていた。この内容は誤りとして撤回せず、有限閉鎖リセットを検査する強化結果として論文外メモへ移す。現行Q2-4は開放リセットと流出浴を許すため、R178Dを必須依存に含めない。結果相関情報はR179の流出経路へ移り、能動系だけを未使用状態へ戻す。

## 2.16 R179：一様開放供給・リセット・再混合

M54の反復運転では、補助作業領域、指針変数、振幅再調整用接続端を有限閉鎖貯蔵部から供給せず、固定した一様規則を持つ流入/流出 reservoir interfaceへ接続する。未使用状態へのリセットは開放収縮として扱い、結果相関情報と使用済み環境自由度は流出経路へ流す。R190の反復作用殻混合では、各試行が過去に装置と相互作用していない定常流入浴部分系を使う。

<!-- theorem-start:theorem -->
**定理（R179：一様開放供給・リセット・再混合）**

補助能動自由度の未使用状態を分布 $\mu_{\rm blank}$ とし、一様リセット半群 $P_t^{\rm reset}$ が

```math
D
\left(
\mu P_t^{\rm reset},
\mu_{\rm blank}
\right)
\leq
C_{\rm reset}e^{-\gamma_{\rm reset}t}
```

を安全初期集合上で満たすとする。ここで $D$ は各節点で用いる全変動距離または状態ノルムに対応する縮約距離である。従って要求誤差 $\epsilon>0$ に対して

```math
T_{\rm reset}
\geq
\frac1{\gamma_{\rm reset}}
\log\frac{C_{\rm reset}}{\epsilon}
```

で能動補助部を一様に再使用できる。

さらに反復試行 $m$ ごとに、過去履歴 $\mathcal H_m$ と独立な定常流入浴部分系を接続し、使用後の部分系を流出経路へ送る。能動作用殻の初期状態に一様な混合核 $K_m$ が

```math
\sup_x
D
\left(
K_m(x,\cdot),
\pi_{\rm bath}
\right)
\leq
\varepsilon_{{\rm mix},m}
```

を満たせば、任意の過去履歴に条件付けても

```math
D
\left(
\mathcal L(X_m\mid\mathcal H_m),
\pi_{\rm bath}
\right)
\leq
\varepsilon_{{\rm in},m}
+
\varepsilon_{{\rm mix},m}.
```

理想定常 流入部分系では $\varepsilon_{{\rm in},m}=0$ である。R179は結果確率や振幅表を外部から供給せず、浴接続部とリセット規則は回路規模に対して一様な有限記述から生成される。有限浴容量、低温／使用済み素子数、部分SWAP列は固定目標の必要条件にしない。
<!-- theorem-end:theorem -->

R179はR161/R162へ依存しない環境接続部結果である。Q1/Q2のR190反復再混合、Q2-4の作業領域再使用、指針変数初期化、散逸履歴の流出排出に共通に使う。有限閉鎖貯蔵部による近似は強化課題として退役メモに保存する。

## 2.17 ## 2.17 M54の合成誤差と資源

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

R186の製造誤差、位相ノイズ、固定機構誤差は、それぞれ $\eta_{\rm gate}$、$\varepsilon_{\rm leak}$、$\bar\varepsilon_j$ を物理部品誤差から評価する十分条件として使い、別の独立誤差として二重加算しない。R186第4項の全自由度に加わる加法ノイズがある場合は、この誤差予算を多項式精度で閉じられない障害条件として扱う。

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

$\bar\varepsilon_j$ は第 $j$ 段のR170選択、制御付き選別機構、方向を変えない振幅再調整、転送、時計自由度だけを含む。R179へ入れた低温下限と衝突誤差を再び含めない。

$\eta_{\rm gate}=O(\epsilon/d)$ とし、$\tau,\gamma,\delta,\bar\varepsilon_j$ はそれぞれ $O(\epsilon/n)$ と選べる。

保守的な逐次読出し時間は

```math
O\!\left(
\frac{n^2}{\epsilon}\log\frac n\epsilon
\right)
```

である。必要な殻剛性は $O(n^2/\epsilon^2)$、衝突流束は $O(\sqrt{n/\epsilon})$、障壁範囲は $O(\log(n/\epsilon))$ で抑えられる。受動モードと低温浴容量は指数的だが、回路記述、外部命令、準備回、ゲート窓、読出し時間、必要精度は多項式である。

## 2.18 Q2-4の判定と境界

R181Cは指数個の個別ゲート設定、R181Dは全 $2^n$ 葉の一括読出し、R179は指数個の個別未使用初期化を避ける。R186は指数モード数だけを理由に指数精度を要求せず、局所製造誤差と位相ノイズを射影型に評価する一方、全自由度に加わる加法ノイズが外部精度へ指数コストとして露出する境界を与える。従ってM54はQ2-4を条件付き達成へ進める。条件は、射影容量保持機構、R190/R179静的選択機構、R170吸収指針変数、制御付き選別機構、方向を変えない振幅再調整、開放リセット/供給接続部を同じ安全集合と制御規約で接続することである。

本構成は通常の計算量理論における多項式資源の古典シミュレーションではない。指数個の受動自由度、静的結合、浴容量、総熱を許した上で、外部制御と総時間を多項式に抑える結果である。未知量子入力、適応中間測定、誤り訂正、固定容量浴による無期限独立同分布標本は主張しない。M54はQ1・Q2・Q3の共通親模型族だが、全状態構成で同一の製造済み装置や同一パラメータを主張しない。

## 2.19 物理的意味と限界

熱化終了後の局所記録生成子は、結果成分 $i$ に支持を持つ滑らかな関数 $d_i(x)$ と空の記録運動量 $P_{D_i}$ を使い、

```math
G_{\rm rec}=\sum_i d_i(x)P_{D_i}
```

と書ける。これは記録時刻の排他的粒子位置を読む。入力時刻以前の粒子軌道、初回到達率、吸収率、時間積分流束を与えない。

R170は、容量結合、作用殻、信号保持、混合・衝突、選択機構、固定機構を有限能動部分系＋明示的Hamiltonian無限浴の1つの具体的ミクロ装置へ統合済みだと主張しない。現行の条件付き達成は、この未統合部分を明示して判定する。有限浴化は別の強化課題である。一意エルゴードな外部時刻割当または有限熱化から、結果列の独立同分布性や二項型有限標本揺らぎも従わない。