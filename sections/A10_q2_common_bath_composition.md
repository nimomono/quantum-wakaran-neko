@number: J
@chapter: 付録
@title: Q2永続共同浴の合成契約
@status: R181Bの反復テンソル積状態の生成、R181Cの同一8モード状態浴、R181DのQ1向け段階的測定後状態受渡し、R177のGHZ--T--逆演算証人を統合する。Q2-2はM66/R205--R207を使う。

## J.1　目的と適用範囲

本付録はQ2-1とQ2-3を同じ機構で動かす契約を定める。三つのQ1型接続端 $A,B,C$ から、R181Bをゲート列の前に2回作用させて

```math
 Z_{ABC}=a\otimes b\otimes c\in\mathbb C^8
 \tag{J.1}
```

を作る。その後はR181Cにより同じ物理的状態浴へA--B、B--C、局所ゲート、逆ゲートを順に作用させ、R181Dにより末端だけを読む。

ここで「同じ機構」とは、モード数が常に4であることではない。固定された有限入力数に対応する受動的な内部モードを浴に任せ、外部制御器は接続端、ゲート種、対象、作用窓だけを指定することを意味する。

## J.2　1試行状態と集団モーメントの分離

$Z_{ABC}$ は同じ試行の実正準座標から得る8成分信号である。2入力の $Z_{AB}$ も同じ種類の1試行信号である。現行Q2-1/Q2-3ではこれらの末端信号を集団モーメントへ置換せずR206 terminal readoutへ渡す。Q2-2は別にM66/R205--R207を使う。

一方、試行集団の交差モーメント

```math
 M_{AB}^{G}
 =\mathbb E[\mathbf1_Gz_Az_B^{\mathsf T}]
 \tag{J.2}
```

を推定して $Z_{AB}$、$Z_{ABC}$ へ戻す操作は再準備である。Q2-1、Q2-3の状態受渡しには使わない。Q2-2はM66/R205--R207を使う。

3入力持ち上げの拡大状態は概念上

```math
 \Gamma_{ABC}
 =(Z_{ABC},G_{AB},G_{ABC},W_{AB},W_{ABC},\tau,H,R)
 \tag{J.3}
```

と書く。逆演算用補助記憶部と作業・履歴記憶部は読出し対象ではないが、可逆性のため保持する。

## J.3　内部モードと外部接続部

| 区分 | 役割 | 外部制御 |
|---|---|---|
| $Z_{ABC}$ | 8モードの永続状態浴 | 個別モードを個別指定しない |
| $G,W,H$ | 逆演算用補助部、供給源、作業領域、時計自由度履歴 | 読出し・リセットしない |
| ゲート窓 | 固定二次ハミルトニアンを開閉 | ゲート種、対象接続端、時間だけ |
| 末端読出し | 射影作用保持、M65 selector、record、R181D router | 回路末尾だけ接続 |

内部に8つの複素モードがあることは、それ自体では指数長の外部記憶部を意味しない。Q2-3は入力数が固定された有限ベンチマークである。一般の $N$ 入力でモード数が $2^N$ になるテンソル積状態の生成反復の一様性はここでは主張しない。Q2-4は同じM54親模型の根-モード・部分系一括作用特殊化で扱う。

## J.4　二つのゲート領域

R181Cの生成子を

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

とする。第1式はC因子を読まずにA--B CNOTを、第2式はA因子を読まずにB--C CNOTを実装する。時計自由度 ハミルトニアン

```math
 H_{\rm tot}
 =P_\tau+H_{\rm hold}
 +g_{AB}(\tau)K_{AB}
 +g_{BC}(\tau)K_{BC}
 \tag{J.5}
```

で2つのコンパクト作用窓を交わらないようにする。B接続端は第1gateの出力と第2gateの入力を兼ねるが、中間受け渡し写像は存在しない。

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

を作用させ、二つのCNOTと最初のHadamardを逆順に戻す。理想コヒーレント出力は

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
**命題（R177：二段共同浴合成のGHZ--T--逆演算証人）**

R181Bによる3入力持ち上げ、R181CによるA--B、B--C、局所 $T$、逆ゲート、およびR206Dの $L=8$ terminal samplerが同じ一試行signalへ接続されるとする。観測コヒーレント分布と式(J.9)の距離を $\varepsilon_{\rm coh}$、任意の完全dephase模型の観測分布と式(J.10)の距離を $\varepsilon_{\rm mix}$ とする。このとき

```math
 \varepsilon_{\rm coh}+\varepsilon_{\rm mix}
 <\frac1{2\sqrt2}
```

なら両模型は正の有限余裕で識別できる。
<!-- theorem-end:proposition -->

## J.6　R177の証明

式(J.6)へ式(J.7)を作用させると $(|000\rangle+e^{i\pi/4}|111\rangle)/\sqrt2$ となる。逆CNOTをB--C、A--Bの順に作用させると $(|000\rangle+e^{i\pi/4}|100\rangle)/\sqrt2$ であり、AへのHadamardから式(J.8)、絶対値の二乗から式(J.9)を得る。

位相緩和は $|000\rangle\langle111|$ とその随伴を消す。逆列は二つの対角成分を等重みのA結果へ移すので式(J.10)を得る。式(J.9)と式(J.10)の全変動距離は式(J.11)である。三角不等式から命題の識別条件が従う。証明終。

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
 +\varepsilon_{206}^{\rm end}.
 \end{aligned}
 \tag{J.12}
```

受け渡し、結果成分対応付け、復号器を独立項として加えない。同じ記憶部を保持し、末端で同次元SWAPと容量固定機構を使うためである。各ゲートはモード数に依存する結果成分別和でなく

```math
 \inf_\chi
 \|\widetilde U-e^{i\chi}U\|_{\rm op}
 \leq\varepsilon
 \tag{J.13}
```

で評価する。無反応は最初の失敗 素子で排他的に数え、成功試行だけを再規格化しない。

## J.8　末端測定機構

Q2-3ではR206Dを $L=8$ に特殊化し、実際の末端信号 $v=Z_{\rm out}(\omega)$ の各局所作用

```math
J_{abc}
=
\mathcal J_0|v_{abc}|^2
```

を同型M66 channelへ直接接続する。理想極限では

```math
P(abc)
=
\frac{|v_{abc}|^2}{\|v\|^2}.
```

R206Cのfinite-time、hub residual、regularization、generator、record誤差をまとめて $\varepsilon_{206}^{\rm end}$ とし、式(J.12)では一度だけ数える。Born表・振幅表・結果別係数表を外部から再注入せず、8個の結果channelを個別走査して標本を探さない。

Q2-3はterminal readout後に測定後signalを次段へ渡さないため、M65/R181Dの逐次projector treeを使わない。永久記録、試行間reset、物理clock、次試行renewalまでの全周期統合はM0へ分離する。

## J.9　Q2-3の現在地と反証条件

R181B/R181Cにより3入力の有限テンソル積状態の生成と2つの有限ハミルトニアン ゲート領域は明示された。R177は同じ記憶部のコヒーレンスを検査する有限ギャップを与える。第1gate後の単一試行状態を同じ8モード記憶部で保持して第2gateへ渡し、末端R206Dの8結果samplerまで接続できるため、固定3入力のQ2-3は達成である。一般入力数に対する資源効率はQ2-4、全周期装置統合はM0で扱う。

次のいずれかが必要なら現行候補は反証される。

- 第1gate後に結果成分またはモードを一つ選ぶ。
- 第2gate前に集団モーメントを推定して未使用浴へ再準備する。
- B--C ゲートがA側係数または最終分布を外部から読み取る。
- 逆演算のために内部モード別の外部履歴回収が必要になる。
- 固定3入力でも各モードの個別較正、同期、個別指定、リセットが必要になる。
- 誤差上界が内部モードごとの粗い和にしかならない。

一般の $N$ に対するQ2-4はM54の直接モード部分系一括作用とR206Dの $L=2^n$ terminal samplingで扱う。これはR181B/R181Cのテンソル積状態の生成反復から自動的に従う結果ではない。
