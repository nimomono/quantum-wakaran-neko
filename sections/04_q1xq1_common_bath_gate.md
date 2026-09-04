@number: 4
@chapter: 本文
@title: M52のQ1×Q1可逆tensor-lift永続状態bath模型
@status: R176A/B/Cを分離し、一般積入力の可逆tensor-lift、同一永続状態上の有限gate列、末端Born型instrument接続を明示する。Q2-2には同じ実際の1試行末端信号を第5章R180へ渡す別interfaceを追加する。Q2-1の条件付き達成は維持する。

## 4.1　改訂した設計原則

Q2-1の固定目標は、2量子ビット型結合ゲートと同一の共同入力--出力統計を生成し、積入力を非分離な共同内部状態へ移し得る有限古典Hamiltonian過程を構成することである。M52は、この共同状態を経路だけに担わせる必要はない。4つまたはそれ以上の内部自由度が実在しても、それらが受動的なbath自由度であり、controllerが個別に扱う必要がなければ固定目標と両立する。

改訂後の設計原則は次のとおりである。

1. controllerが指定するのはQ1 port、lift窓、ゲート種、対象port、作用窓、末端読出しだけである。
2. 内部の4モードregister、8個の実正準座標、anti-register、work cell、clock履歴は許す。ただし各内部modeを外部から個別に初期化、較正、同期、address、読出し、resetしてはならない。
3. 一般入力から生じた同じ物理的状態bathを全ゲート間で保持し、中間で枝選択、粒子位置decode、tomography、集団moment推定、再準備をしない。
4. 可逆性に必要なanti-register、入力source、work、clock履歴を捨てない。
5. 排他的なBorn型結果は回路末尾だけでM50/R164/R170へ接続する。無反応も完全結果空間へ含める。

従って問題になるのは内部自由度の個数そのものではなく、外部interfaceが閉じているか、同一試行の状態が永続するか、余計な自由度をbathへ受動的に任せられるかである。旧M52の「4モードregisterを使わず経路だけで担う」という制約は撤回する。

## 4.2　M52の状態とinterface

2つのQ1入力を

```math
 a=(a_0,a_1)^{\mathsf T},
 \qquad
 b=(b_0,b_1)^{\mathsf T}
 \tag{4.1}
```

とする。lift後の状態bathに4成分の派生複素信号

```math
 Z_S=(Z_{00},Z_{01},Z_{10},Z_{11})^{\mathsf T}
 \in\mathbb C^4
 \tag{4.2}
```

を置く。これは1試行の実正準座標から得る物理的な派生信号であって、M51の集団統計量

```math
 c=\mathbb E[z],
 \qquad
 C_Z=\mathbb E[zz^\dagger]
 \tag{4.3}
```

ではない。記号も用途も分ける。

可逆liftは同時にanti-register

```math
 G_S=\overline{a\otimes b}
 \tag{4.4}
```

を生成する。全状態を概念上

```math
 \Gamma_{52}
 =(\Gamma_{Q1,A},\Gamma_{Q1,B},Z_S,G_S,W_S,\tau,E_R,H,R)
 \tag{4.5}
```

と書く。$W_S$ はsource、work、lift clock、gate clockの可逆履歴を含む。$G_S,W_S$ は出力結果として読まず、逆写像を可能にするbath自由度として保持する。

外部interfaceは

```math
 \mathfrak I_{52}
 =(A,B;\,L_{AB};\,\{(g_r,S_r,t_r)\}_{r=1}^{L};\,M_{\rm end})
 \tag{4.6}
```

だけである。$L_{AB}$ はlift窓、$g_r$ は有限個のゲート種、$S_r$ は対象port集合、$t_r$ は作用窓、$M_{\rm end}$ は末端instrumentである。内部index $00,01,10,11$ をcontrollerの4本の独立命令として公開しない。

## 4.3　R176A：可逆tensor-lift定理

各組 $(j,k)$ にblankな正準対

```math
 (x_{jk},\pi^x_{jk}),
 \qquad
 (y_{jk},\pi^y_{jk})
 \tag{4.7}
```

を用意し、$s_C=\sqrt{2J_C}$ として

```math
 w^x_{jk}=\frac{x_{jk}+i\pi^x_{jk}}{s_C},
 \qquad
 w^y_{jk}=\frac{y_{jk}+i\pi^y_{jk}}{s_C}
 \tag{4.8}
```

と置く。安全なcompact領域で1となる滑らかなcutoffを暗黙に掛け、lift Hamiltonianを

```math
 H_{\rm mult}
 =\chi(\tau)
 \sum_{j,k}
 \left(
 \pi^x_{jk}F^x_{jk}(a,b)
 +\pi^y_{jk}F^y_{jk}(a,b)
 \right)
 \tag{4.9}
```

とする。単位面積pulseに対して

```math
 F^x_{jk}=\sqrt2s_C\operatorname{Re}(a_jb_k),
 \qquad
 F^y_{jk}=\sqrt2s_C\operatorname{Im}(a_jb_k)
 \tag{4.10}
```

と選ぶ。係数 $\sqrt2$ は式(4.8)と後の正準混合の正規化に必要である。

各 $(j,k)$ で固定実正準行列

```math
 S_0=\frac1{\sqrt2}
 \begin{pmatrix}
 1&0&0&-1\\
 0&1&1&0\\
 1&0&0&1\\
 0&1&-1&0
 \end{pmatrix}
 \tag{4.11}
```

を $(x,\pi^x,y,\pi^y)$ に作用させる。出力の2つの派生複素modeは

```math
 Z_{jk}=a_jb_k,
 \qquad
 G_{jk}=\overline{a_jb_k}.
 \tag{4.12}
```

となる。

<!-- theorem-start:theorem -->
**定理（R176A：可逆tensor-lift定理）**

正規化された有限次元Q1入力 $a\in\mathbb C^m$、$b\in\mathbb C^n$ とblank targetを考える。式(4.9)--式(4.11)は安全compact領域上の有限時間Hamiltonian流として

```math
 (a,b,0)
 \longmapsto
 (a,b,Z_S=a\otimes b,G_S=\overline{a\otimes b},W_S)
```

を実現する。source、anti-register、work、clock履歴を保持すれば、$S_0^{-1}$ と逆pulseにより写像全体を反転できる。近似pulse、cutoff、blank誤差に対しては安全compact領域上のLipschitz定数による有限誤差評価を持つ。
<!-- theorem-end:theorem -->

積の非線形性は、式(4.9)がsourceとtargetを含む3次Hamiltonianであることに担わせる。blank manifold上ではtarget momentumが零のためsourceは理想的に動かず、targetだけが平行移動する。これは未知入力の係数をcontrollerが読み取って書き込む操作ではない。

R176Aは固定 $m,n$ に対する定理である。$m=n=2$ および3入力への2段liftには有限の受動modeしか要らない。一般の入力数 $N$ に対するtensor反復の一様性はR176Aから主張せず、Q2-4では別模型M53の直接モードsector-broadcastを使う。

## 4.4　R176B：永続状態bathゲート合成定理

lift後は同じ $Z_S$ を計算終了まで保持する。Hermitian行列 $h(t)$ に対して

```math
 H_h(t)=Z_S^\dagger h(t)Z_S,
 \qquad
 iJ_C\dot Z_S=h(t)Z_S
 \tag{4.14}
```

は有限mode上のunitaryを実正準Hamiltonian流として実装する。

Q2-1のCNOTはmode $10,11$ のswapである。差mode projectorを

```math
 \Pi_-^{10,11}
 =\frac12
 (|10\rangle-|11\rangle)
 (\langle10|-\langle11|)
 \tag{4.15}
```

とすれば

```math
 U_{\rm CX}=\exp(-i\pi\Pi_-^{10,11})
 \tag{4.16}
```

である。実正準座標では対応する生成子を

```math
 K_{A\to B}
 =\frac14
 \left[
 (Q_{10}-Q_{11})^2
 +(P_{10}-P_{11})^2
 \right]
 \tag{4.17}
```

と取れる。

3入力ではR176Aを2回使い、ゲート列の前に

```math
 Z_{ABC}=a\otimes b\otimes c
 \tag{4.18}
```

を作る。Q2-3の2つのCNOT生成子は

```math
 \begin{aligned}
 K_{AB}
 &=\frac14\sum_c
 \left[
 (Q_{10c}-Q_{11c})^2
 +(P_{10c}-P_{11c})^2
 \right],\\
 K_{BC}
 &=\frac14\sum_a
 \left[
 (Q_{a10}-Q_{a11})^2
 +(P_{a10}-P_{a11})^2
 \right].
 \end{aligned}
 \tag{4.19}
```

これはsectorごとの外部routingではなく、同じ有限二次形式を全該当modeへ受動的に作用させる1つのgate命令である。

gate clockを含む全Hamiltonianは

```math
 H_{\rm tot}
 =P_\tau+H_{\rm hold}
 +\sum_{r=1}^{L}g_r(\tau)K_r(Z_S)
 \tag{4.20}
```

とする。$g_r$ は互いに交わらないcompactな作用窓を持ち、出口では相互作用が零になる。clock momentumやworkは履歴を保持してよいが、$Z_S$ を交換または再準備しない。
本文式(4.17)、式(4.19)のCNOT窓では $\int g_r(t)dt=\pi$ とする。一般gateではこのpulse面積を対応するHermitian対数に置き換える。

<!-- theorem-start:theorem -->
**定理（R176B：永続状態bathゲート合成定理）**

R176Aで得た有限次元の同一状態bath $Z_S$ に、式(4.20)の有限個の非重複gate窓を作用させる。各理想gateを $U_r$、実装を $\widetilde U_r$ とし、

```math
 \inf_{\chi_r}
 \|\widetilde U_r-e^{i\chi_r}U_r\|_{\rm op}
 \leq\varepsilon_r
```

とする。このとき任意の有限参照因子に恒等作用を追加しても同じ評価が成立し、

```math
 \inf_\chi
 \|\widetilde U_L\cdots\widetilde U_1
 -e^{i\chi}U_L\cdots U_1\|_{\rm op}
 \leq\sum_{r=1}^{L}\varepsilon_r
```

を得る。CNOT、局所unitary、逆演算、およびQ2-3の2段CNOTは、中間decodeや再準備なしに同じ $Z_S$ 上で合成できる。
<!-- theorem-end:theorem -->

以前の「handoff map」は不要である。同じregisterを保持するため、有限誤差はlift、hold、clock、gate、leakageへ一度ずつ数える。経路展開は式(4.16)、式(4.19)の代数的な診断表示として残せるが、独立のR175や物理的経路分岐器を主結果鎖に置かない。

## 4.5　R176C：末端Born型instrument接続定理

回路末尾の実際の1試行信号を

```math
 v=Z_{\rm out}(\omega)
 \tag{4.23}
```

とする。これは理想係数の再構成値でも集団共分散でもない。R112の同次元blank hold-registerへのcanonical SWAPで $V$ へ保持し、信号bathを計算registerから切り離す。

各結果 $y$ の容量を

```math
 J_y(V)=J_0|V_y|^2,
 \qquad
 J_\Sigma(V)=\sum_yJ_y(V)
 \tag{4.24}
```

とし、正則化容量とlatchを

```math
 A_y^\delta(V)=J_y(V)+\delta q_yJ_\Sigma(V),
 \qquad
 H_{\rm latch}
 =\sum_yP_y^A A_y^\delta(V)
 \tag{4.25}
```

で定める。blank容量momentum $P_y^A=0$ ではpointerだけが移動し、理想的な $V$ は動かない。latch後に信号をdecoupleしてからR164の作用殻、R161/R162の有限混合、R170の衝突・固定・記録へ渡す。

<!-- theorem-start:theorem -->
**定理（R176C：末端Born型instrument接続定理）**

R176Bの末端信号 $v$ が零でなく、canonical SWAP、容量latch、作用殻、有限混合、収集、固定、記録がそれぞれ安全compact領域上で定義されるとする。完全結果空間を

```math
 \Omega_{\rm out}=I_L\sqcup\{\varnothing\}
```

とする。正規化rayの実装誤差が $\varepsilon_{\rm ray}$、無反応率が $f_\varnothing$、末端各段を一度ずつ合計した誤差が $\varepsilon_{170}^{\rm end}$ なら、

```math
 D_{\rm TV}(P_{\rm out},P_{\rm Born})
 \leq
 f_\varnothing
 +\varepsilon_{\rm ray}
 +\frac{\delta}{1+\delta}
 +\varepsilon_{170}^{\rm end}.
```

理想的な共通radial因子とglobal phaseは式(4.24)の規格化で消える。
<!-- theorem-end:theorem -->

R176Cは条件付き定理である。R164、R170の既存部品に加え、容量pointerから作用殻への境界、有限fiber混合の枝対称性、SWAPから記録までの一体化を同じ有限Hamiltonian実装で満たす必要がある。成功試行だけの再規格化は行わない。

## 4.6　Q2-1とQ2-3の識別力

$|+0\rangle$ からCNOTを作用させると

```math
 Z_{\rm Bell}
 =\frac{|00\rangle+|11\rangle}{\sqrt2}.
 \tag{4.28}
```

中間で2枝をdephaseした模型は計算基底周辺を再現できても、逆CNOTとHadamardを通した末端分布を再現しない。coherent出力とdephase出力の全変動距離は

```math
 D_{\rm TV}=\frac12
 \tag{4.29}
```

である。従ってR176Bの逆演算試験は、単なる4結果確率表より強い。

Q2-3では $Z_{ABC}$ に式(4.19)を順に作用させる。R177のGHZ--位相--逆演算試験は、coherent模型と中間枝選択模型の間に

```math
 D_{\rm TV}=\frac1{2\sqrt2}
 \tag{4.30}
```

の識別gapを与える。同じtensor-lift、同じ永続register、同じ二次gate、同じ末端instrumentを使うため、Q2-1、Q2-3は同一機構の有限次元特殊化である。

## 4.7　R180 setting-pre receiverへの末端interface

Q2-2の固定singlet sourceは、$|00\rangle$ のR176A tensor-lift後にR176Bの

```math
H_A,
\qquad
\operatorname{CX}_{A\to B},
\qquad
X_B,
\qquad
Z_A
```

を順に作用させて作る。理想末端信号は

```math
V_{\rm s}
=
\frac{|01\rangle-|10\rangle}{\sqrt2}.
\tag{4.31}
```

このgate列は設定生成前に終える。実際の末端信号 $v=Z_{\rm out}(\omega)$ をR112のcanonical SWAPで物理hold信号 $\widetilde V=v$ としてそのまま移し、第5章R180へ渡す。canonical SWAPは状態依存除算を含まない。R180では解析上だけ $V=\widetilde V/\|\widetilde V\|$ とし、A設定 $x$ が $\widetilde V$ の直交projector blockを選び、source-driven paired-Hopf receiverを通して2翼の局所M50/R170へ接続する。

このinterfaceはR176Cと役割が異なる。R176Cは末端計算基底分布を直接記録する。R180は同じ試行の4mode信号を記録前に2翼receiverへ渡す。1周期では選んだ一方だけを作動させる。

R180は $G_S$ を末端共役信号として使わない。R176A直後の $G_S=\overline{a\otimes b}$ はR176B後の $\overline{Z_{\rm out}}$ を意味しないからである。入力係数の外部読出し、試行集団momentへの縮約、fresh carrierへの再準備も行わない。

Q2-2がM52を根拠模型として共有しても、Q2-1の達成状態からQ2-2を推論しない。Q2-2はR180A--R180C固有のbranch作用、paired-Hopf、切断後局所性、完全結果誤差から独立に判定する。

## 4.8　誤差台帳と現在地

長さ $L$ の回路全体には

```math
 \varepsilon_{\rm circ}
 \leq
 \varepsilon_{\rm lift}
 +\varepsilon_{\rm hold}
 +\varepsilon_{\rm clock}
 +\sum_{r=1}^{L}\varepsilon_r
 +\varepsilon_{\rm leak}
 +\varepsilon_{\rm ray}
 +\frac{\delta}{1+\delta}
 +\varepsilon_{170}^{\rm end}
 +f_\varnothing
 \tag{4.32}
```

と整理する。中間handoff、枝pairing、coherent decoderを独立項として二重計上しない。

R176Aは明示的な有限Hamiltonian構成、R176Bは同一有限register上の作用素norm合成を与える。R176Cは既存の末端bath部品へ接続する条件付き評価を与える。このためQ2-1は「部分達成」から「条件付き達成」へ更新する。残る条件は主としてR176Cの物理境界と全末端工程の一体化である。

Q2-3も同じ理由で条件付き達成とする。Q2-2は本章の実際の1試行末端信号を第5章のsetting-pre paired-Hopf receiverへ渡す別interfaceを使い、R180Cの単一装置統合を条件として条件付き達成を維持する。Q2-4はM52の一般化ではなく、M53とR178A--R178F、R179を根拠に別途条件付き達成とする。
