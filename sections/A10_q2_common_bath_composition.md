@number: J
@chapter: 付録
@title: Q2永続共同bathの合成契約
@status: M52の1試行coherent経路、二段interaction zone、R177のGHZ--T--逆演算証人、M48の集団交差モーメントとの境界を固定する。

## J.1　目的と適用範囲

本付録は、Q2-1候補M52をQ2-3の二段ゲートへ拡張するときの契約を定める。三つのQ1型部分系 $A,B,C$ と一つの永続状態bathを使い、第1のinteraction zoneをA--B、第2をB--Cへ作用させる。第1ゲート後の状態bathを測定、経路選択、集団モーメントへの置換、fresh bathへの再準備なしに第2ゲートへ渡す。

ここで「Q1型」は2状態の局所論理portを意味し、M47と同じ物理装置であることを要求しない。Q2-3の固定目標は変更しない。R175の代数から従う条件付き証人をR177として整理するが、R176の物理的Q1×Q1合成定理が未解決なのでQ2-3は部分達成のままである。

## J.2　1試行経路と集団交差モーメントの分離

三部分系の1試行経路族を

```math
 \Xi_{ABC}(\Gamma)
 =\{(\gamma_r,a_r,b_r,c_r,\ell_r):r\in\mathcal P_\Gamma\}
 \tag{J.1}
```

とし、派生振幅テンソルを

```math
 \Psi_\Gamma
 =\sum_{r\in\mathcal P_\Gamma}
 \gamma_ra_r\otimes b_r\otimes c_r
 \tag{J.2}
```

とする。式(J.2)は同じ試行に共存するbath sectorのcoherent和である。各経路の実正準座標と状態bathが物理状態であり、$\Psi_\Gamma$ はその診断表示である。

一方、M48で使う

```math
 M_{AB}^{G}
 =\mathbb E[\mathbf1_Gz_Az_B^{\mathsf T}]
 \tag{J.3}
```

は試行集団の交差モーメントである。式(J.3)を推定して式(J.1)へ戻す操作はcoherent handoffでなく再準備なので、Q2-1またはQ2-3の状態受渡しには使わない。M48のBell周期は独立の固定目標Q2-2に属し、内部のsetting-pre seedから開始する。

## J.3　状態bath、gate補助bath、読出しbath

装置自由度を次の三種類に分ける。

| 区分 | 役割 | ゲート間の条件 |
|---|---|---|
| 永続状態bath $E_S$ | 経路、相対位相、pairing、参照系相関 | 計算終了まで保持し、交換・再標本化しない |
| gate補助bath $E_{AB},E_{BC}$ | clock、interaction zone、可逆routing | 各ゲート後に状態bathからdecoupleすれば交換可能 |
| 末端読出しbath $E_R$ | coherent decoder後の作用殻、固定、記録 | 回路末尾だけで接続する |

第1ゲートのwhich-path情報が $E_{AB}$ に残り、第2ゲートがそれを参照しない場合、coherenceは失われる。従って補助bathは、各経路に依存しない基準状態へ戻すか、状態bathの一部として計上する。逆演算に不可欠な入力依存自由度を「補助」と呼んで資源台帳から外してはならない。

## J.4　二つのinteraction zone

理想A--BゲートはC因子を読まず

```math
 \Phi_{AB}:\Psi_\Gamma
 \longmapsto
 (U_{AB}\otimes I_C)\Psi_\Gamma,
 \tag{J.4}
```

B--CゲートはA因子を読まず

```math
 \Phi_{BC}:\Psi_\Gamma
 \longmapsto
 (I_A\otimes U_{BC})\Psi_\Gamma
 \tag{J.5}
```

と作用する。二つのzoneは同じ $E_S$ に順番に結合し、B portは第1ゲートの出力と第2ゲートの入力を兼ねる。第2zoneが $a_r$、全体テンソル、または最終分布を読み取る必要はない。全bath sectorへ同じ局所規則を一様に作用させる。

CNOTについては、A--B zoneで

```math
 a_r\otimes b_r\otimes c_r
 \longmapsto
 P_0a_r\otimes b_r\otimes c_r
 +P_1a_r\otimes Xb_r\otimes c_r,
 \tag{J.6}
```

B--C zoneで

```math
 a_r\otimes b_r\otimes c_r
 \longmapsto
 a_r\otimes P_0b_r\otimes c_r
 +a_r\otimes P_1b_r\otimes Xc_r
 \tag{J.7}
```

とする。各式の二項を排他的枝へ変えず、coherentな子sectorとして保持する。

## J.5　GHZ--T--逆演算証人

初期状態を $|000\rangle$ とし、AへHadamardを作用させて $|+00\rangle$ を作る。前向き列は

```math
 |+00\rangle
 \xrightarrow{\mathrm{CX}_{A\to B}}
 \frac{|000\rangle+|110\rangle}{\sqrt2}
 \xrightarrow{\mathrm{CX}_{B\to C}}
 \frac{|000\rangle+|111\rangle}{\sqrt2}.
 \tag{J.8}
```

ここでAへ

```math
 T=\operatorname{diag}(1,e^{i\pi/4})
 \tag{J.9}
```

を作用させ、二つのCNOTと最初のHadamardを逆順に戻す。理想coherent出力は

```math
 \frac{1+e^{i\pi/4}}{2}|000\rangle
 +\frac{1-e^{i\pi/4}}{2}|100\rangle.
 \tag{J.10}
```

従って

```math
 P_{\rm coh}(000)=\cos^2\frac{\pi}{8},
 \qquad
 P_{\rm coh}(100)=\sin^2\frac{\pi}{8},
 \tag{J.11}
```

であり、他の結果は零である。第1ゲート後または第2ゲート後に経路coherenceを失い、対応するGHZ枝を古典混合へ置換すると、同じ逆列の出力は

```math
 P_{\rm mix}(000)=P_{\rm mix}(100)=\frac12.
 \tag{J.12}
```

両分布の全変動距離は

```math
 g_{\rm coh}
 :=D_{\rm TV}(P_{\rm coh},P_{\rm mix})
 =\frac{1}{2\sqrt2}.
 \tag{J.13}
```

である。

<!-- theorem-start:proposition -->
**命題（R177：二段共同bath合成のGHZ--T--逆演算証人）**

R176を満たすA--B、B--Cの二つのQ1×Q1ゲートが同じ永続状態bath上で合成でき、局所Hadamard、局所 $T$、逆ゲート、末端計算基底decoderが同じ参照系安定誤差規約を満たすとする。このとき式(J.8)--式(J.11)を一つの試行周期内で実現できる。観測coherent分布と理想式(J.11)の距離を $\varepsilon_{\rm coh}$、任意の経路選択・完全dephasing模型の観測分布と式(J.12)の距離を $\varepsilon_{\rm mix}$ とすれば、

```math
 \varepsilon_{\rm coh}+\varepsilon_{\rm mix}
 <\frac{1}{2\sqrt2}
```

のとき両模型は正の有限余裕で識別できる。
<!-- theorem-end:proposition -->

R177はR176を仮定する条件付き結果である。現在のM52に二つの有限Hamiltonian zoneが存在することを証明せず、Q2-3を達成へ上げない。

## J.6　R177の証明

式(J.8)へ式(J.9)を作用させると $(|000\rangle+e^{i\pi/4}|111\rangle)/\sqrt2$ となる。$\mathrm{CX}_{B\to C}$、$\mathrm{CX}_{A\to B}$ を順に作用させると $(|000\rangle+e^{i\pi/4}|100\rangle)/\sqrt2$ である。AへのHadamardから式(J.10)、絶対値の二乗から式(J.11)を得る。

dephasingは $|000\rangle\langle111|$ とその随伴を消す。unitary逆列は二つの対角成分をそれぞれ等重みのA結果へ移すので式(J.12)を得る。式(J.11)と式(J.12)の差の絶対値は各非零結果で $1/(2\sqrt2)$、従って全変動距離は式(J.13)である。三角不等式より上の誤差不等式なら観測分布の距離は正である。証明終。

## J.7　有限誤差台帳

R177周期のcoherent側誤差を

```math
 \begin{aligned}
 \varepsilon_{\rm coh}\leq{}&
 \varepsilon_{\rm prep}
 +\varepsilon_{AB}
 +\varepsilon_{\rm hand}^{AB\to BC}
 +\varepsilon_{BC}\\
 &+\varepsilon_T
 +\varepsilon_{BC}^{-1}
 +\varepsilon_{\rm hand}^{BC\to AB}
 +\varepsilon_{AB}^{-1}\\
 &+\varepsilon_H
 +\varepsilon_{\rm dec}
 +\varepsilon_{\rm Born}
 +\varepsilon_{\rm rec}
 +f_\varnothing
 \end{aligned}
 \tag{J.15}
```

と整理する。同じclockずれ、bath leakage、経路欠損をforward、handoff、inverseへ重複加算せず、最初に現れる項へだけ入れる。$f_\varnothing$ は最初の失敗段階ごとに排他的に数え、成功試行だけを結果分布として再規格化しない。

経路数が $R$ のとき、各経路の誤差を $R$ 倍する粗い上界では指数精度を要求し得る。必要なのは状態bath全体の作用素距離で

```math
 \|\widetilde\Phi_{AB}-\Phi_{AB}\|_{\rm op}
 \leq\varepsilon_{AB},
 \qquad
 \|\widetilde\Phi_{BC}-\Phi_{BC}\|_{\rm op}
 \leq\varepsilon_{BC}
 \tag{J.16}
```

と一様に抑えることである。R176はこの意味の有限誤差を構成しなければならない。

## J.8　末端Born型読出し

末端decoderが規格化8成分信号 $c_{abc}$ を作れたとする。M50/R164を $m=L=8$、$\Psi=I_8$ へ特殊化すると

```math
 \pi_{abc}^{\delta}(c)
 =\frac{|c_{abc}|^2+\delta q_{abc}}{1+\delta},
 \qquad
 \sum_{a,b,c}q_{abc}=1
 \tag{J.17}
```

を得る。正則化だけによる理想Born分布からの全変動距離は高々 $\delta/(1+\delta)$ である。R170の混合、固定、記録誤差を加えて完全結果空間上で評価する。

8成分信号は末端の診断・読出しportであり、計算中の共同状態を一つの8モードregisterへ置換してよいという意味ではない。状態bathから式(J.17)へcoherentに集めるdecoderはR176の未解決部分である。

## J.9　M48の条件付き局所因子化との境界

M48の固定singlet型Bell周期は、M52またはR176を入力providerとして要求しない。M48内部の設定前等重みseed、paired-Hopf準備、2翼strong matching、切断後局所instrumentから独立に始まる。

M48の切断面で完全共通原因を $\Lambda$ とし、切断後の状態、生成子、noise、作用殻が

```math
 \mu_{AB}^{x,y}(d\gamma_A,d\gamma_B\mid\Lambda)
 =\mu_A^x(d\gamma_A\mid\Lambda)
 \mu_B^y(d\gamma_B\mid\Lambda),
 \tag{J.18}
```

```math
 L_{AB}^{x,y}(\Lambda)
 =L_A^x(\Lambda)\otimes I_B
 +I_A\otimes L_B^y(\Lambda)
 \tag{J.19}
```

と因子化すると、切断後の有限時間核も

```math
 K_{AB}^{x,y}
 =K_A^xK_B^y
 \tag{J.20}
```

と因子化する。これはM48/R155の局所性監査に使う。$\Lambda$ を平均した後の共同分布の対数を物理的な切断後ポテンシャルへ戻すと式(J.19)を破るため禁止する。

式(J.18)--式(J.20)はBell周期内の条件付き局所応答であり、M52のcoherent経路合成ではない。逆にM52の式(J.2)をM48の集団交差モーメントへ置換してはならない。二つの「共同bath」は目的、切断面、平均の位置が異なる。

## J.10　Q2-3の現在地と反証条件

Q2-3について確立しているのは、R175の参照系安定な経路代数を三部分系へ拡張できること、理想二段CNOT列とGHZ--T--逆演算の有限識別余裕をR177で計算できることである。M52上の一般入力lift、二つの有限Hamiltonian interaction zone、補助bath decoupling、coherent末端decoderは未完成であるため、現在地は部分達成である。

次のいずれかが必要なら現行候補は反証される。

- 第1ゲート後に経路を一つ選ぶ。
- 第2ゲート前に共同モーメントを推定してfresh bathへ再準備する。
- B--CゲートがA側係数または最終分布を読み取る。
- 逆演算にwhich-path履歴を回収する外部操作が必要である。
- 誤差上界がbath sector数に比例し、指数精度を要求する。
- 8出力を得る前に指数個のsectorを個別に読み出す。

これらを避ける有限装置が構成できれば、R176とR177を用いてQ2-1、Q2-3の再判定へ進む。
