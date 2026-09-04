@number: J
@chapter: 付録
@title: Q2永続共同bathの合成契約
@status: R176Aの反復tensor-lift、R176Bの同一8mode状態bath、R176Cの末端instrument、R177のGHZ--T--逆演算証人を統合し、2入力M52信号をR180 receiverへ渡す境界を区別する。

## J.1　目的と適用範囲

本付録はQ2-1とQ2-3を同じ機構で動かす契約を定める。三つのQ1型port $A,B,C$ から、R176Aをgate列の前に2回作用させて

```math
 Z_{ABC}=a\otimes b\otimes c\in\mathbb C^8
 \tag{J.1}
```

を作る。その後はR176Bにより同じ物理的状態bathへA--B、B--C、局所gate、逆gateを順に作用させ、R176Cにより末端だけを読む。

ここで「同じ機構」とは、mode数が常に4であることではない。固定された有限入力数に対応する受動的な内部modeをbathに任せ、外部controllerはport、gate種、対象、作用窓だけを指定することを意味する。

## J.2　1試行状態と集団momentの分離

$Z_{ABC}$ は同じ試行の実正準座標から得る8成分信号である。2入力の $Z_{AB}$ と、第5章R180がholdする $V=Z_{\rm out}/\|Z_{\rm out}\|$ も同じ種類の1試行信号である。Q2-2では $V$ をA設定basisで物理的にblock分解し、選択blockを同じ試行のreceiver sourceとして渡す。

一方、試行集団の交差moment

```math
 M_{AB}^{G}
 =\mathbb E[\mathbf1_Gz_Az_B^{\mathsf T}]
 \tag{J.2}
```

を推定して $Z_{AB}$、$Z_{ABC}$ またはR180のtemplateへ戻す操作は再準備である。Q2-1、Q2-2、Q2-3の状態受渡しには使わない。旧M48のBell周期は式(J.2)からsinglet型射影を作ったが、現行Q2-2の根拠から退役し、R180は実際のM52信号を直接受ける。

3入力liftの拡大状態は概念上

```math
 \Gamma_{ABC}
 =(Z_{ABC},G_{AB},G_{ABC},W_{AB},W_{ABC},\tau,H,R)
 \tag{J.3}
```

と書く。anti-registerとwork/historyは読出し対象ではないが、可逆性のため保持する。

## J.3　内部modeと外部interface

| 区分 | 役割 | 外部制御 |
|---|---|---|
| $Z_{ABC}$ | 8modeの永続状態bath | 個別modeをaddressしない |
| $G,W,H$ | anti、source、work、clock履歴 | 読出し・resetしない |
| gate窓 | 固定二次Hamiltonianを開閉 | gate種、対象port、時間だけ |
| 末端bath | hold、容量、作用殻、固定、記録 | 回路末尾だけ接続 |

内部に8つの複素modeがあることは、それ自体では指数長の外部registerを意味しない。Q2-3は入力数が固定された有限benchmarkである。一般の $N$ 入力でmode数が $2^N$ になるM52反復の一様性はここでは主張しない。Q2-4は別模型M53で扱う。

## J.4　二つのgate zone

R176Bの生成子を

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
 \right]
 \end{aligned}
 \tag{J.4}
```

とする。第1式はC因子を読まずにA--B CNOTを、第2式はA因子を読まずにB--C CNOTを実装する。clock Hamiltonian

```math
 H_{\rm tot}
 =P_\tau+H_{\rm hold}
 +g_{AB}(\tau)K_{AB}
 +g_{BC}(\tau)K_{BC}
 \tag{J.5}
```

で2つのcompact作用窓を交わらないようにする。B portは第1gateの出力と第2gateの入力を兼ねるが、中間handoff mapは存在しない。

## J.5　GHZ--T--逆演算証人

初期状態を $|000\rangle$ とし、AへHadamardを作用させる。前向き列は

```math
 |+00\rangle
 \xrightarrow{\operatorname{CX}_{A\to B}}
 \frac{|000\rangle+|110\rangle}{\sqrt2}
 \xrightarrow{\operatorname{CX}_{B\to C}}
 \frac{|000\rangle+|111\rangle}{\sqrt2}.
 \tag{J.6}
```

Aへ

```math
 T=\operatorname{diag}(1,e^{i\pi/4})
 \tag{J.7}
```

を作用させ、二つのCNOTと最初のHadamardを逆順に戻す。理想coherent出力は

```math
 \frac{1+e^{i\pi/4}}2|000\rangle
 +\frac{1-e^{i\pi/4}}2|100\rangle.
 \tag{J.8}
```

従って

```math
 P_{\rm coh}(000)=\cos^2\frac\pi8,
 \qquad
 P_{\rm coh}(100)=\sin^2\frac\pi8.
 \tag{J.9}
```

中間で完全dephaseした模型は

```math
 P_{\rm mix}(000)=P_{\rm mix}(100)=\frac12
 \tag{J.10}
```

を与え、両分布の全変動距離は

```math
 g_{\rm coh}
 =D_{\rm TV}(P_{\rm coh},P_{\rm mix})
 =\frac1{2\sqrt2}.
 \tag{J.11}
```

<!-- theorem-start:proposition -->
**命題（R177：二段共同bath合成のGHZ--T--逆演算証人）**

R176Aによる3入力lift、R176BによるA--B、B--C、局所 $T$、逆gate、およびR176Cによる末端instrumentが同じ永続状態bath上で合成されるとする。観測coherent分布と式(J.9)の距離を $\varepsilon_{\rm coh}$、任意の完全dephase模型の観測分布と式(J.10)の距離を $\varepsilon_{\rm mix}$ とする。このとき

```math
 \varepsilon_{\rm coh}+\varepsilon_{\rm mix}
 <\frac1{2\sqrt2}
```

なら両模型は正の有限余裕で識別できる。
<!-- theorem-end:proposition -->

## J.6　R177の証明

式(J.6)へ式(J.7)を作用させると $(|000\rangle+e^{i\pi/4}|111\rangle)/\sqrt2$ となる。逆CNOTをB--C、A--Bの順に作用させると $(|000\rangle+e^{i\pi/4}|100\rangle)/\sqrt2$ であり、AへのHadamardから式(J.8)、絶対値の二乗から式(J.9)を得る。

dephasingは $|000\rangle\langle111|$ とその随伴を消す。逆列は二つの対角成分を等重みのA結果へ移すので式(J.10)を得る。式(J.9)と式(J.10)の全変動距離は式(J.11)である。三角不等式から命題の識別条件が従う。証明終。

## J.7　有限誤差台帳

R177周期の誤差は

```math
 \begin{aligned}
 \varepsilon_{\rm coh}\leq{}&
 \varepsilon_{\rm lift}^{AB}
 +\varepsilon_{\rm lift}^{ABC}
 +\varepsilon_{\rm hold}
 +\varepsilon_{\rm clock}
 +\varepsilon_{AB}
 +\varepsilon_{BC}
 +\varepsilon_T\\
 &+\varepsilon_{BC}^{-1}
 +\varepsilon_{AB}^{-1}
 +\varepsilon_H
 +\varepsilon_{\rm leak}
 +\varepsilon_{\rm ray}
 +\frac{\delta}{1+\delta}
 +\varepsilon_{170}^{\rm end}
 +f_\varnothing.
 \end{aligned}
 \tag{J.12}
```

handoff、branch pairing、decoderを独立項として加えない。同じregisterを保持し、末端で同次元SWAPと容量latchを使うためである。各gateはmode数に依存する枝別和でなく

```math
 \inf_\chi
 \|\widetilde U-e^{i\chi}U\|_{\rm op}
 \leq\varepsilon
 \tag{J.13}
```

で評価する。無反応は最初のfailure cellで排他的に数え、成功試行だけを再規格化しない。

## J.8　末端instrument

R176Cを $L=8$ に特殊化する。実際の末端信号 $v=Z_{\rm out}(\omega)$ をcanonical SWAPでholdし、

```math
 \pi_{abc}^{\delta}(v)
 =\frac{|v_{abc}|^2/\|v\|^2+\delta q_{abc}}{1+\delta},
 \qquad
 \sum_{a,b,c}q_{abc}=1
 \tag{J.14}
```

を容量比として作用殻へ渡す。これはcoherent decoderを仮定しない。計算中にすでに存在する8mode信号を同次元blank registerへ可逆に保持し、その二乗容量を末端だけでlatchする。

末端のunresolved条件は、容量pointerとR164作用殻の境界、有限fiber混合の枝対称性、およびR170までの一体化である。これらはR176Cの条件へ集約する。

## J.9　R180の条件付き局所因子化との境界

2入力M52の末端には二つの異なるinterfaceがある。R176Cは末端計算基底分布を直接記録する。R180は実際の4mode信号をholdし、A設定で2つの直交blockへ分け、source-driven paired-Hopf流を通して2翼局所instrumentへ渡す。どちらも1試行信号を集団momentへ置換しない。

切断面で完全共通原因を $\Lambda$ とし、切断後の状態と生成子が

```math
 \mu_{AB}^{x,y}(d\gamma_A,d\gamma_B\mid\Lambda)
 =\mu_A^x(d\gamma_A\mid\Lambda)
 \mu_B^y(d\gamma_B\mid\Lambda),
 \tag{J.15}
```

```math
 L_{AB}^{x,y}(\Lambda)
 =L_A^x(\Lambda)\otimes I_B
 +I_A\otimes L_B^y(\Lambda)
 \tag{J.16}
```

と因子化すれば有限時間核も因子化する。これはR180Cの局所性監査に使う。$\Lambda$ にはM52信号、A設定、内部枝、paired位相、切断面の2翼状態、使用済みsource履歴を含めてよいが、切断後のA核へ $y$、B核へ反対翼の結果形成変数を入れない。

M52の1試行信号を式(J.2)へ置換したり、式(J.2)をM52またはR180へ再注入したりしない。R180Cで未解決なのは、hold、projector latch、選択block port、paired-Hopf pump・sink、中央切断、fresh局所作用殻、2翼R170を共通safe setと単一clockで統合する物理境界である。

## J.10　Q2-3の現在地と反証条件

R176A/Bにより3入力の有限tensor-liftと2つの有限Hamiltonian gate zoneは明示された。R177は同じregisterのcoherenceを検査する有限gapを与える。R176Cの物理境界と一体化が条件として残るため、Q2-3は条件付き達成である。

次のいずれかが必要なら現行候補は反証される。

- 第1gate後に枝またはmodeを一つ選ぶ。
- 第2gate前に集団momentを推定してfresh bathへ再準備する。
- B--C gateがA側係数または最終分布を外部から読み取る。
- 逆演算のために内部mode別の外部履歴回収が必要になる。
- 固定3入力でも各modeの個別較正、同期、address、resetが必要になる。
- 誤差上界が内部modeごとの粗い和にしかならない。

一般の $N$ に対するQ2-4はM53の直接モードsector-broadcastと逐次2枝標本化で扱う。これはR176A/Bのtensor-lift反復から自動的に従う結果ではない。
