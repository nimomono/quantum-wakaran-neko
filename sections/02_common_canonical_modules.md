@number: 2
@chapter: 本文
@title: 有限正準信号と共通熱浴モジュール
@status: M54をQ1・Q2・Q3の共通有効signal・状態構成層、M66/R205を共通thermal-reservoir interface、R161をQ3位置輸送の共通数学核とする。M64/M65は系列固有domain model、R206はM66のQ2 terminal specialization、R207はQ2-2-S strengthening candidateとして責務を分ける。

## 2.1 共通signal層と共通thermal-reservoir層

M54は有限個の実正準対から得るsignal、準備済み入力境界、永続記憶部、可逆作業領域、作用保持指針、粒子位置interface、記録、時計自由度を共通化する有効状態構成族である。これと独立にM66/R205A--R205Fは、resolved classical degreeとthermal reservoirの間に現れるphase-volume、mean-flow、thermal sampling、matched capacity--conductance、passive separationを共通化する。Q1--Q3の統一は、1つの万能模型へ潰すのではなく、この2つの共通層と用途別specializationの組合せとして扱う。

M66の共通入力を正のphase-volume weight $w(Q,t)>0$、通常のenergy landscape $H_{\rm cfg}(Q,t)$、mean-flow port $U(Q,t)$ とする。付録XのR205A/R205Cは

```math
F_{\rm res}(w)
=
-k_BT\log w+C
```

とmean-flow shiftの両立を与え、R205Eは

```math
p_{\rm eq}(Q)
\propto
w(Q)e^{-\beta H_{\rm cfg}(Q)}
```

のthermal sampler、R205Fは空間分離時のgenerator decouplingを与える。

| 用途 | 共通熱浴原理との対応 | 用途固有に残る責務 |
|---|---|---|
| M64 / Q3 | R203Bの $w=r_X^\delta/r_*$ とmean-flow sectorをR205Cへ埋め込む | R203A current dictionary、initial/flow trackingの具体実装、tracer、R203C/R203D |
| M65 / Q1・Q2-2 | R204B phase-volume chamberをR205Dのbinary fixed-hub specializationとして回収 | M65 canonical 3状態open law、R204D--R204F、R181D handoff |
| R206 / Q2-1・Q2-3・Q2-4 | M66のfinite-$L$ common-hub terminal specialization | Q2 terminal bridge、finite-time/fabrication error、Q2-4 root preparation |
| R207 / Q2-2-S | R205E joint thermal preparationとR205F passive separationを利用 | setting precursor、CHSH witness、Bell前提監査、finite-speed残件 |

従ってM66はM64/M65のwhole-model parentではなく、共通reservoir interfaceのparentである。共通化されたsectorと各domain model固有のsectorを混同しない。

M54から作る派生複素座標を

```math
Z=\frac{Q+iP}{\sqrt{2\mathcal J_0}}
```

とするが、$Z$ は独立した複素実体ではない。Q1/Q2-2では2結果射影作用をM65のbinary selector interfaceへ渡す。Q2-1/Q2-3/Q2-4ではterminal各結果作用をM66/R206へ渡す。Q3ではM37/R86が空間signalを与え、M64/R203A--R203Dが同じsignalからcontinuous/finite-graph tracerをR161へ渡す。R161自身が有限状態のcanonical Markov経路法則まで定め、R162は同じ経路法則を独立Poisson random measuresで実現するoptional referenceとして使う。測定結果用の旧静的配置pointerをM54共通状態へ置かない。

M65のopen pointer、M66のcommon-hub pointer、R179のopen reset浴は接続interfaceとして扱い、常設のM54信号座標とは分ける。

概念上の共通状態を

```math
\Gamma_{54}^{(\Lambda,\mathcal I)}
=
(Z,S_{\rm port},G,W,J,X,D,\tau)
```

と書く。$X$ はQ3でM64が与えるclassical tracerの有限状態表示である。Q1/Q2-2の逐次2値結果はM65、Q2-1/Q2-3/Q2-4のterminal joint resultはM66/R206が担う。

| 系列 | M54状態構成 | 準備・操作 | 現行出力 |
|---|---|---|---|
| Q1 | W型2モード信号 | 準備済み古典入力、R140、R187 | M65、R181D、R143--R144 |
| Q2-1 | 4モード永続記憶部 | R181B、R181C | M66/R206D 4結果terminal sampling |
| Q2-2 | 4モード＋2物理測定端 | R181B/R181C、設定gate | A端M65、router、B端M65、R180A/R180C |
| Q2-3 | 8モード永続記憶部 | R181Bを2回、R181C、R177 | M66/R206D 8結果terminal sampling |
| Q2-4 | $2^n$ 直接モード | R206E root preparation、R181C | M66/R206D $2^n$結果terminal sampling、R186監査 |
| Q3 | 空間信号＋classical tracer | 準備済み古典空間入力、M37/R86、M64/R203A--R203D | R161、R185、R124、R182、R125 |

M37はM54へ吸収しない。Q3では局所位置ばね網から空間信号を実装し、Q1ではR187の弱結合W型族に限って最低2正常モードをW2制御信号へ接続する。全系列を同一architectureの装置族、共通物理interface、一つのparameter family、共通反復周期へ統合するM0は別の未完成目標である。入力、測定軸、ポテンシャル、規模に応じた有限設定値の変更は許す。

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

## 2.4 初期状態の準備境界

各試行の物理状態は有限個の実正準対 $(Q,P)$ であり、派生複素座標

```math
Z=\frac{Q+iP}{\sqrt{2\mathcal J_0}}
```

は実正準信号系の表示にすぎない。本論文の固定目標では、初期状態方向を共通の状態非依存種から散逸的に生成することを必須条件にしない。Q1ではW型2モード、Q2では固定入力信号または一般 $n$ の $0^n$ 根モード、Q3では空間信号について、実正準初期条件またはその試行分布を準備済み古典入力として境界に置く。

入力境界は、結果確率表、Born重み、結果依存状態、規格化後の測定結果を外部から注入する許可ではない。境界以後の可逆発展、状態方向輸送、結果形成、射影結果成分受渡し、空間配置輸送は各現行結果から導く。入力誤差は、目標規格化第2モーメント $C_{\rm in}$ または目標単一試行信号に対する一つの $\varepsilon_{\rm in}$ として下流の誤差予算へ一度だけ入れる。

Q1のM37--W2接続ではR187または固定線形正準接続端を用い、Q2-1--Q2-3の固定積入力はR181Bへ渡す。Q2-4はR181Bを一般 $n$ へ反復せず、R206Eの一様open preparationで $0^n$ 根モードを作る。Q3は準備済み空間signalからM37/R86を経てM64/R203A--R203Dへ入り、continuous profileはR161/R185へ、finite-graph profileはR124/R182/R125の位置読出しへ接続する。R162はこの経路法則のoptional independent-Poisson realizationとして比較用途にだけ残す。

旧R181Aの物理テンプレート、横方向排出、共通初期種からの状態方向吸引は数学的結果として退役記録へ保存する。そこから一時切り出した方向不変作用回復R192も、draft-127でQ2-4逐次branchの責務消滅に伴い退役した。

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

## 2.7 Q1/Q2局所構造からQ3空間信号への持ち上げ

R161へ渡す位置重みと確率流は、追加の作用殻状態数を介さず、同じ有限実正準signalの空間特殊化から直接作る。有限配置グラフ $G_X=(\mathcal I,E_X)$ の各頂点 $i$ にQ1型の局所実正準モードを置き、

```math
Z_i
=
\frac{Q_i+iP_i}{\sqrt{2\mathcal J_0}},
\qquad
R_i=|Z_i|^2,
\qquad
S=\sum_iR_i
```

とする。$S>0$、$q_i>0$、$\sum_iq_i=1$、$\delta>0$ に対し、

```math
R_i^\delta
=
|Z_i|^2+\delta q_iS,
\qquad
\pi_i^\delta
=
\frac{R_i^\delta}{(1+\delta)S}
```

と定める。これはsignal densityへ正の背景を加えるregularizationであり、状態数を数える追加の物理ファイバーを導入しない。

一般のエルミート辺結合を加え、

```math
J_{i\to j}
=
\frac{2}{\mathcal J_0}
\operatorname{Im}
\left(Z_j^*h_{ji}Z_i\right),
\qquad
J_{i\to j}=-J_{j\to i}
```

と置くと $\dot R_i=\sum_jJ_{j\to i}$ である。$S$ が保存される区間では

```math
j_{ij}^\delta
=
\frac{J_{i\to j}}{(1+\delta)S},
\qquad
\dot\pi_i^\delta
=
\sum_jj_{ji}^\delta .
```

従ってQ1型局所signalとQ2型辺結合から $(\pi^\delta,j^\delta)$ が得られる。R161の対称活動量 $t_{ij}=t_{ji}\geq|j_{ij}|$ は位置輸送の物理実現が供給する独立入力であり、現行Q3ではM64/R203Dがfinite-graph activityとgeneratorを与える。

```math
\mathrm{local\ canonical\ signal}
+\mathrm{edge\ coupling}
\longrightarrow
(\pi^\delta,j^\delta),
\qquad
(\pi^\delta,j^\delta,t^\delta)
\xrightarrow{\mathrm{R161}}
X_t .
```

Q1/Q2のM65 pointerをQ3 tracerへ同一視する主張ではない。

## 2.8 R161の共通整合・Markov経路法則とM64/R162の物理・参照実現

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
**定理（R161：有限配置の確率流・活動量整合とMarkov経路存在）**

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

さらに固定有限時間 $0\leq t\leq T$ で $k^+_{i\to j}(t)$ がBorel可測かつ

```math
M_T
=
\sup_{0\leq t\leq T}
\max_i\sum_{j\ne i}k^+_{i\to j}(t)
<\infty
```

を満たすなら、この時間依存生成子を持つ非爆発càdlàg有限状態Markov過程は法則の意味で一意に存在する。Q3では許容された古典signal履歴 $Z_{[0,T]}=z_{[0,T]}$ を固定してこの条件付き経路法則を構成し、その後signal履歴の法則で混合して共同法則を得る。従ってR185が必要とする前向き経路法則とBayes後退率はR161自身の結論である。

Q3のfinite-graph特殊化では、M64/R203Dが上流signalから正の $\pi^\delta$、反対称current $j^\delta$、許容活動量 $t^\delta$ を局所的に構成し、この定理へ直接渡す。1次元特殊化では同じ経路法則をR185の前進・後退平均微分へ接続する。

<!-- theorem-end:theorem -->

### R161の活動量--親和力表示と実現同値

R161の各辺について $t_{ij}>|j_{ij}|$ とし、前向き・逆向きの確率流を

```math
q_{ij}^{+}
=\pi_i k^+_{i\to j}
=\frac{t_{ij}+j_{ij}}{2},
\qquad
q_{ij}^{-}
=\pi_j k^+_{j\to i}
=\frac{t_{ij}-j_{ij}}{2}
```

と置く。対称基準活動度と無次元親和力を

```math
c_{ij}
=\frac12\sqrt{t_{ij}^2-j_{ij}^2},
\qquad
\mathcal A_{ij}
=\log\frac{t_{ij}+j_{ij}}{t_{ij}-j_{ij}}
=2\operatorname{artanh}\frac{j_{ij}}{t_{ij}}
```

と定めると、厳密に

```math
q_{ij}^{\pm}
=c_{ij}e^{\pm\mathcal A_{ij}/2},
```

```math
t_{ij}
=2c_{ij}\cosh\frac{\mathcal A_{ij}}2,
\qquad
j_{ij}
=2c_{ij}\sinh\frac{\mathcal A_{ij}}2
```

である。従ってR161は、対称な遷移活動度 $c$ と反対称な非平衡親和力 $\mathcal A$ の表示へ等価に書き換えられる。境界 $t_{ij}=|j_{ij}|$ では $c\to0$、$|\mathcal A|\to\infty$ の極限表示となるため、有限量としては元の $(t,j)$ 表示を正本とする。

本稿では、同じ信号履歴と同じ初期粒子位置分布に対して2つのミクロ模型が同じ $\pi_i(t)$ と同じ有向率 $k_{i\to j}(t)$ を与えるとき、それらを **R161実現として厳密同値** と呼ぶ。物理自由度や存在論が同じことは要求しない。固定有限時間 $T$ 上で

```math
\varepsilon_{\rm gen}
=\sup_{0\leq t\leq T}
\max_i
\sum_{j\ne i}
\left|k^A_{i\to j}(t)-k^B_{i\to j}(t)\right|
```

なら、同じ初期分布から始めた周辺分布は

```math
\sup_{0\leq t\leq T}
D_{\rm TV}
\left(p_t^A,p_t^B\right)
\leq
T\varepsilon_{\rm gen}
```

を満たす。この生成子同値により、R161より前段の物理実現を交換しても、同じcanonical位置経路法則とR185の縮約を共通に扱える。現行主線のM64/R203Dは、1次元continuous profileではregularized smooth diffusionをR185と同一のfinite-volume R161 chainへ接続し、finite-graph profileではlocal phase-volume $R_i^\delta$、edge current $J_{ij}$、activity $T_{ij}^\delta$ から一般R161 rateを直接構成する。内部実体の一致でなく同じ $(\pi,j,t)$ とgenerator interfaceへの接続を比較基準とする。M60/M61は旧Hamiltonian実現としてGit履歴に保存する。R162はR161経路法則を独立Poisson random measuresでpathwiseに実現するoptional stochastic referenceとする。

<!-- theorem-start:theorem -->
**定理（R162：R161経路法則の独立Poisson-jump実現）**

固定有限グラフ、固定有限時間 $T$ 上で、R161の仮定を満たす有向率 $k_{i\to j}(t)\geq0$ を取る。R161によりcanonical Markov経路法則は既に一意に存在する。さらに

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

Poisson reservoirはR161 canonical経路法則の一つの明示的pathwise realizationである。現行Q3の物理存在論はM64の三実体が担い、Q3-2とR185の論理依存はR161だけで閉じる。R162は比較、シミュレーション、開放Poisson実装の参照に用いる。有限衝突Hamiltonian列への持上げは強化結果として論文外メモへ分離する。R161の静的 $j=0$ 特殊化は数学的比較用に残すが、Q1/Q2-2の逐次2結果読出しではM65、Q2-1/Q2-3/Q2-4のterminal readoutではM66/R206を使う。
<!-- theorem-end:theorem -->

R161は静的・移動の率構成に加え、有限状態のcanonical Markov経路法則まで共通に保つ。現行Q3の物理主線はM64/R203A--R203Dであり、R162は同じ経路法則を持つoptional Poisson realizationとして残す。Q1/Q2-2の逐次2結果測定はR161静的鎖を経由せずM65 binary selectorへ、Q2-1/Q2-3/Q2-4のterminal readoutはM66/R206へ接続する。旧有限衝突実装は退役メモに保存する。


### 2.9 M65：3状態open binary selector

M65のcanonical lawはM66から導出するのではなく、$+,H,-$ の3状態open Markov generatorとして直接定める。付録X/R205Dが共通化するのはR204Bのphase-volume chamber実現だけであり、M65自身のfixed-goal正本性はR204D--R204Fに依存する。

M65は $A_\pm\geq0$、$A_++A_->0$ を満たす二つの保持済み作用を読む古典open selectorである。固定 $A_*>0$ に対して $a_r=A_r/A_*$ とし、pointer $X_t\in\{+,H,-\}$ のrateを

```math
k_{+\to H}=k_{-\to H}=\Lambda,
\qquad
k_{H\to +}=\kappa a_+,
\qquad
k_{H\to -}=\kappa a_-
```

と直接定める。rateは保持作用へ線形であり、装置へBorn確率表または $A_r/(A_++A_-)$ を入力しない。

R204Dにより有限時間完全結果分布はBorn作用比へ近づき、R204Eにより後述のbinary selector contractを満たす。phase-volume chamberとHamiltonian--Brownian liftはR204B/R204Cの追加実現であり、M65の正本定義には含めない。

M65/R204D--R204FをQ1/Q2-2 fixed-goalの現行binary selectorとして採用する。decision終了時にはgeneratorを閉じてR112型recordへ完全結果を固定し、その後にR181D routerを開く。

## 2.10 M54の一様記憶部、接続端、貯蔵部

$n$ 量子ビット、深さ $d$、固定有限普遍ゲート集合から与えられる回路を考え、$L=2^n$ とする。M54では計算基底文字列 $x$ を受動信号モードへ直接対応させる。

```math
|x\rangle
\longleftrightarrow
Z_x,
\qquad
Z=(Z_x)_{x\in\{0,1\}^n}\in\mathbb C^L.
```

M54の能動部は信号、逆演算用補助記憶部、一様ゲートバス、出力記録、時計自由度を持つ。Q1/Q2-2の逐次2結果読出しはM65/R181Dを、Q2-1/Q2-3/Q2-4のterminal joint readoutはM66/R206を主線とする。内部の受動自由度、静的結合、状態容量、受動並列度は $2^n\operatorname{poly}(n,d)$ まで許す。一方、外部プログラムが指定するのはゲート種、1個または2個の対象量子ビット、ゲート順序、現在読む出力ビット、未使用化の回、素子添字、時計自由度窓だけである。$2^n$ モードの列挙、モード別初期化・較正・読出し、指数長の係数表、回路別配線、出力確率の事前計算を許さない。

M54はR181Bの反復テンソル積状態の生成を一般 $n$ へ延長しない。Q2-4ではR206Eの全mode共通減衰＋固定root driveで $0^n$ 根モードを作り、別の基底入力は回路先頭の $X$ ゲートで作る。ゲート列はR181C、末端ビット列はR206Dが一回で標本化する。sampler pointerはR206A自身のmixingを使い、結果別の明示resetを要求しない。

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

## 2.13 M54共通射影作用・binary selector・可逆選別

出力ビット $k$ に対する計算基底射影を $P_{k,0},P_{k,1}$ とし、

```math
P_{k,0}+P_{k,1}=I,
\qquad
P_{k,0}P_{k,1}=0.
```

未処理作用を

```math
J_{k,b}
=
\mathcal J_0Z^\dagger P_{k,b}Z
```

として保持する。

<!-- theorem-start:lemma -->
**補題（直交射影子作用保持機構と対合選別機構）**

結果 $b$ が固定された後に作用する

```math
F_{k,b}
=
\begin{pmatrix}
P_{k,b}&P_{k,1-b}\\
P_{k,1-b}&-P_{k,b}
\end{pmatrix}
```

は

```math
F_{k,b}^\dagger F_{k,b}=I,
\qquad
F_{k,b}^2=I,
```

かつ未使用作業領域に対して

```math
F_{k,b}(Z,0)
=
(P_{k,b}Z,P_{k,1-b}Z)
```

を満たす。作用保持を制御剪断として実装すれば理想信号を変更せず二作用を保持できる。
<!-- theorem-end:lemma -->

この補題自身は確率結果を選ばない。Q1/Q2-2の逐次binary主線は、二射影作用の保持、M65による完全結果固定、必要な局所記録、固定結果で制御した $F_{k,b}$、次節点または外部接続端への転送からなる。Q2-1/Q2-3/Q2-4のterminal readoutではこのbinary treeを使わず、各計算基底結果の局所作用をM66/R206へ直接接続する。

## 2.14 R181D：selector非依存の段階的射影選別・測定後状態受渡し

第 $k$ 段、履歴節点 $u$ の入力を $Z_u\neq0$ とし、

```math
J_{u,b}
=
\mathcal J_0Z_u^\dagger P_{u,b}Z_u,
\qquad
p_{u,b}
=
\frac{J_{u,b}}{J_{u,0}+J_{u,1}}
```

とする。

R181Dが上流に要求するbinary selector contractは、

```math
Y_u\in\{0,1,\varnothing\},
```

```math
D_{\rm TV}
(
\widetilde K_u,K_u^{\rm Born}
)
\leq
\varepsilon_{{\rm sel},u},
```

非空安全結果で

```math
p_{u,Y_u}
\geq
\tau_{{\rm state},u}>0,
```

結果固定後にだけrouterを開くこと、および無反応を除いて再規格化しないこと、である。

現行M65実装では

```math
\varepsilon_{{\rm sel},u}=\varepsilon_{65,u},
\qquad
\tau_{{\rm state},u}
=
\tau_{\rm cut}-\varepsilon_A.
```

<!-- theorem-start:theorem -->
**定理（R181D：binary selector後の段階的projector-routerと測定後状態受渡し）**

上のbinary selector contractを各節点で満たし、結果固定後にだけ $F_{u,b}$ を作用するとする。理想節点を深さ $m$ まで合成すると、

```math
\prod_{k=1}^{m}p_{k,y_k}
=
\frac{
\|P_{m,y_m}\cdots P_{1,y_1}Z\|^2
}{
\|Z\|^2
}
```

となる。

router実装誤差が

```math
\|\widetilde v-v\|
\leq
\eta_F\|Z_u\|,
\qquad
v=P_{u,b}Z_u,
```

かつ $\eta_F<\sqrt{\tau_{{\rm state},u}}$ なら、

```math
\left\|
\frac{\widetilde v}{\|\widetilde v\|}
-
\frac{v}{\|v\|}
\right\|
\leq
\frac{
2\eta_F
}{
\sqrt{\tau_{{\rm state},u}}-\eta_F
}.
```

入力分布誤差を $\varepsilon_{\rm in}$、各節点で実際に使うselector、router、転送、前段状態方向偏差を各1回だけまとめた誤差を $\bar\varepsilon_k$ とすれば、

```math
D_{\rm TV}
(
P_{\rm out},
P_{\rm Born}
)
\leq
\varepsilon_{\rm in}
+
\sum_{k=1}^{m}\bar\varepsilon_k.
```

R181Dの結論はselectorの内部物理に依存しない。
<!-- theorem-end:theorem -->

完全証明と適用境界は付録Pに置く。fixed-goalではQ1/Q2-2のsame-trial post-state handoffに用い、Q2-1/Q2-3/Q2-4のterminal samplingには用いない。

## 2.15 R178Dの本線退役：有限閉鎖リセットの情報容量境界

旧R178Dは、結果を保持したまま有限閉鎖系の全補助自由度を同じ初期点へ戻すことの制約と、使用済み側に必要な情報容量下界を与えていた。この内容は誤りとして撤回せず、有限閉鎖リセットを検査する強化結果として論文外メモへ移す。現行Q2-4はR206Eのopen root preparation/refreshとR206Aのpointer mixingを使うため、R178DもR179も直接依存に含めない。

## 2.16 R179：一様開放供給・リセット・再混合

逐次binary instrumentを反復使用する場合は、補助作業領域、binary selector指針変数、使用済み作用保持対を固定した一様規則を持つ流入／流出浴接続部へ接続する。未使用状態へのリセットは開放収縮として扱い、結果相関情報と使用済み環境自由度は流出経路へ流す。

<!-- theorem-start:theorem -->
**定理（R179：一様開放供給・リセット）**

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

理想定常流入部分系では $\varepsilon_{{\rm in},m}=0$ である。R179は結果確率や振幅表を外部から供給せず、浴接続部とリセット規則は回路規模に対して一様な有限記述から生成される。有限浴容量、低温／使用済み素子数、部分SWAP列は固定目標の必要条件にしない。
<!-- theorem-end:theorem -->

R179はR161/R162へ依存しない環境接続部結果である。現行fixed-goalではQ2-2の逐次binary instrumentおよび全周期renewal側のopen resetに残す。Q2-4のroot preparation/refreshはR206E、sampler pointer refreshはR206Aへ移す。有限閉鎖貯蔵部による近似は強化課題として退役メモに保存する。

### 2.16.1 R186：M54一様受動構造の射影型頑健性と加法ノイズ障害

一般 $n$ のM54信号を $N=2^n$、$Z\in\mathbb C^N$、$S=Z^\dagger Z>0$ とし、

```math
P_Z=\frac{ZZ^\dagger}{S}
```

を信号状態方向の射影子とする。大域位相を変える $cI$ はBorn分布と射影型状態を変えないので、エルミート摂動 $V$ の有害成分を

```math
\|V\|_{\rm proj}
=
\inf_{c\in\mathbb R}\|V-cI\|
```

で測る。加法ノイズの共分散を $Q_{\rm add}=BB^\dagger$ とし、現在の状態方向に垂直な作用注入率を

```math
q_\perp(Z)
=
\frac{\operatorname{tr}[(I-P_Z)Q_{\rm add}]}{S}
```

とする。

<!-- theorem-start:theorem -->
**定理（R186：M54一様受動構造の射影型頑健性と加法ノイズ障害）**

固定有限ゲート窓または保持窓について次が成り立つ。

1. 理想ハミルトニアン $H(t)$ にエルミート製造誤差 $V(t)$ を加えたユニタリ実装では、理想状態方向と実装状態方向の純粋状態トレース距離は

```math
D_{\rm tr}
\leq
\min\!\left\{
1,
\frac1{\mathcal J_0}
\int\|V(t)\|_{\rm proj}\,dt
\right\}.
```

各行に高々 $\Delta(n)$ 本の摂動を受けた結合器が入り、各局所係数誤差の絶対値が $\mu$ 以下なら、ある数値定数 $C$ に対して $\|V\|_{\rm proj}\leq C\Delta(n)\mu$ と評価できる。従って $\Delta(n)$ と総ゲート時間が多項式なら、指数個の部分系が存在しても局所製造精度は逆多項式で足りる。

2. 各モードに独立なStratonovich位相ノイズ

```math
dZ_x=-i\sigma Z_x\circ dW_x
```

だけが作用する時間 $T$ では、$p_x=|Z_x(0)|^2/S$ として

```math
\mathbb E F(T)
=
e^{-\sigma^2T}
+
\left(1-e^{-\sigma^2T}\right)
\sum_xp_x^2,
```

従って

```math
1-\mathbb E F(T)
\leq
1-e^{-\sigma^2T}
\leq
\sigma^2T.
```

ノイズ経路数 $N$ はこの上界へ現れない。指数個の独立ノイズ供給源が存在すること自体はQ2-4の失敗条件ではない。

3. 射影結果の固定機構で理想容量 $J_b=\sum_{x\in b}|Z_x|^2$ の各係数が $1+\delta_x$ へずれ、$|\delta_x|\leq\mu$ なら、

```math
|\widetilde J_b-J_b|\leq\mu J_b.
```

ここでも部分系数の和は現れない。

4. 一方、$N$ 次元信号空間上で

```math
Q_{\rm add}\succeq\sigma^2I_N
```

なら任意の非零信号に対して

```math
q_\perp(Z)\geq\frac{(N-1)\sigma^2}{S}.
```

さらに $H=0$、$B$ 一定の保持窓 $T$ では、横方向加法偏差 $\eta_\perp$ は

```math
\mathbb E\|\eta_\perp\|^2\geq(N-1)\sigma^2T.
```

従って $S$、$T$ と許容RMS状態方向誤差の逆数を多項式に抑えるM54直接モード実装では、等方加法ノイズの下限に対して $\sigma=O(2^{-n/2}\operatorname{poly}^{-1})$ 級の抑制が必要になる。これはQ2-4一般の不可能性定理ではなく、現在のM54直接振幅記憶部に対する障害条件である。

<!-- theorem-end:theorem -->

R186の第1項から第3項は、指数モード数を局所誤差の粗い総和へ置き換えないための正の頑健性条件である。第4項は空モードへも有限作用を注入する加法ノイズを区別する。M66/R206のterminal samplerはreader側のbranch問題を解消するが、signal registerで既に生じた横方向additive deviation自体を訂正しない。

第4項の指数ノイズ障害は、信号作用 $S$ を多項式に抑える場合の条件である。$S$ 自体を指数的に増やせば、この不等式だけから指数精度は直ちには従わない。しかし、その場合は大きな信号作用が外部制御仕事、準備、動的範囲、読出し分解能、リセット時間などの外部運用資源へ指数コストとして露出しないことをQ2-4の資源台帳で別に示す必要がある。付録Oの制御仕事式は信号作用に比例する上界を与えるが、それだけを指数仕事の下界とは解釈しない。従ってR186第4項は、現行M54直接モード実装においてノイズ抑制と信号作用のどちらへ費用が移るかを明示する障害条件である。

証明、sub-Gaussian製造ばらつきの最大偏差系、計算--逆計算診断は付録Rに置く。

## 2.17 M54の合成誤差と資源

Q2-1/Q2-3/Q2-4の完全結果分布を $P_{\rm M54}$、理想回路Born分布を $P_{\rm circ}$ とする。入力・root preparation誤差を $\varepsilon_{\rm prep}$、gate作用素ノルム誤差を $\eta_{\rm gate}$、leakageを $\varepsilon_{\rm leak}$、R206 terminal sampler誤差を $\varepsilon_{206}$ とすれば、誤差を重複計上せず

```math
D_{\rm TV}(P_{\rm M54},P_{\rm circ})
\leq
\varepsilon_{\rm prep}
+d\eta_{\rm gate}
+\varepsilon_{\rm leak}
+\varepsilon_{206}.
```

Q2-1/Q2-3では $\varepsilon_{\rm prep}$ にR181B入力・持ち上げ誤差、Q2-4ではR206E root preparation誤差を含める。$\varepsilon_{206}$ はR206Cのfinite-time、hub residual、regularization、generator、record、fabrication errorを一度だけまとめる。

R186の製造誤差・位相ノイズ条件は $\eta_{\rm gate}$、$\varepsilon_{\rm leak}$、$\varepsilon_{206}$ を物理部品誤差から評価する十分条件として使い、別の独立誤差として二重加算しない。R186の全自由度additive-noise障害がある場合は、この誤差予算を多項式精度で閉じられない条件として扱う。

R206C/R206Eよりsampling時間とroot preparation時間は対数精度依存であり、$L=2^n$ を直接掛けない。内部のsignal mode、result chamber、phase-volume自由度は指数的でも報告対象の受動内部資源として扱い、外部からの個別較正・全channel走査・指数長係数表を許さない。

## 2.18 Q2-4の判定と境界

Q2-4ではR206Eが $0^n$ rootを一様open lawで準備し、R181Cが固定有限普遍ゲート集合の局所gateを全該当sectorへ一括作用させ、R206Dが $L=2^n$ terminal resultを一回で標本化する。R206A--R206Cにより最小Born重みに依存する逐次branch時間、全葉走査、結果別router、非終端作用回復、結果別pointer resetを必要としない。

R186は指数モード数だけを理由に指数精度を要求せず、局所製造誤差と位相ノイズを射影型に評価する一方、全自由度に加わるadditive noiseが外部精度へ指数コストとして露出する境界を与える。従ってQ2-4は条件付き達成を維持し、現時点の主要fixed-goal残件をR186のdirect-amplitude register障害へ集中させる。

本構成は通常の計算量理論における多項式総物理資源の古典シミュレーションではない。指数個の受動自由度、静的結合、浴容量、総熱を許した上で、外部制御、準備、sampling、readout、精度、反復回数、総時間を多項式に抑えるblack-box operational主張である。

## 2.19 物理的意味と限界

熱化終了後の局所記録生成子は、結果成分 $i$ に支持を持つ滑らかな関数 $d_i(x)$ と空の記録運動量 $P_{D_i}$ を使い、

```math
G_{\rm rec}=\sum_i d_i(x)P_{D_i}
```

と書ける。これは記録時刻の排他的粒子位置を読む。入力時刻以前の粒子軌道、初回到達率、吸収率、時間積分流束を与えない。

M65は開放3状態Markov方程式を基本方程式として採用し、phase-volume chamber/Hamiltonian--Brownian liftは強化実現へ分離する。Q1/Q2-2では同じbinary selector interfaceを使う。Q2-1/Q2-3/Q2-4はM66/R206 terminal samplerで判定し、Q2-4だけはR186資源条件を含むため条件付き達成を維持する。有限浴化は別の強化課題である。一意エルゴードな外部時刻割当または有限熱化から、結果列の独立同分布性や二項型有限標本揺らぎも従わない。

### 共通熱浴層との対応

M66/R205の共通thermal-reservoir interfaceは2.1で定義した。ここで必要なのは、M65のcanonical law、M64 tracer dynamics、R206 terminal samplerを同一の完成装置とみなさないことである。R203B--R205C、R204B--R205D、R206、R205E/F--R207の対応は2.1の表と付録X/Wを参照する。

Q2-1/Q2-3/Q2-4ではR206をterminal readout正本とし、R206Eのuniform root preparation/refreshをQ2-4で併用する。Q1/Q2-2のM65/R181DとQ2-2/full-cycle側のR179は別責務として維持する。
