@number: 0
@chapter: 概要
@title: 概要

本論文の中心的な問いは、明示的な古典力学モデルから、量子力学に似た可逆操作、Born型測定統計、測定後状態、複合系相関、量子回路型処理、空間粒子力学がどこまで有効構造として現れるかである。有限次元Schrödinger方程式と同型の線形方程式を古典振動子で作ることと、1回の試行で排他的結果を形成し、その結果を次の物理操作へ渡すことは別の問題として扱う。

単一試行で実在するとみなすのは、実正準自由度、粒子位置、熱浴自由度または開放浴との物理接続、制御器、時計、記録器である。複素信号 $Z$ は実正準対 $(Q,P)$ の派生表示であり、密度、current、状態方向、規格化第2モーメント、確率分布は派生量または試行集団の統計量である。これらの統計量を、構成していない外部測定器を介して単一試行へ書き戻すことはしない。

現行理論は次の4層に整理できる。

| 層 | 主な識別 | 役割 |
|---|---|---|
| 実正準signal・状態構成 | M54、M37 | M54が共通状態・接続規約、M37が古典振動子によるsignal実装 |
| 共通thermal-reservoir interface | M66/R205 | phase-volume、mean-flow、thermal sampling、passive separation |
| 用途別の模型・特殊化 | M65/R181D、R206、M64/R161/R185、R207 | Q1逐次2値測定、Q2終端多結果、Q3粒子/Nelson、Q2-2 projection phase-volume二端模型 |
| 全周期統合 | M0 | 準備からrenewalまでを1つのjoint device/processへ統合 |


M54はQ1--Q3で共有する有限実正準信号、記憶部、作業領域、時計、記録、接続規約の有効状態構成族である。M37/R86はそのうち空間signalを局所結合古典振動子網として実装し、R187の条件下ではW型最低2正常モードをQ1の2モード制御信号へ接続する。

M66/R205A--R205Fは、resolved classical degreesとthermal reservoirの間に現れる共通物理原理だけを抽出する。中心量は正のphase-volume weight $w$、通常のenergy landscape $H_{\rm cfg}$、mean-flow port $U$ であり、

```math
F_{\rm res}
=
-k_BT\log w+C
```

およびR205Eの平衡分布

```math
p_{\rm eq}(Q)
\propto
w(Q)e^{-\beta H_{\rm cfg}(Q)}
```

を共通核とする。R205Cによりphase-volume weightとmean-flow shiftは同じreservoir内で両立し、R205Fは距離依存相互作用とreservoir cross-correlationが消えるときの受動的generator分離条件を与える。

この共通化は、M64またはM65の全模型をM66から導出したという主張ではない。M64のtracer/current dictionary、M65のcanonical 3状態open Markov lawは系列固有の責務として残る。M64/R203Bのpartition/free-energyとmean-flow sectorはR205C、M65/R204Bのphase-volume chamber実現はR205Dへ埋め込まれる。R206はM66の直接的なQ2終端多結果特殊化であり、R207はM66/R205A・R205E・R205FをQ2-2のprojection phase-volume共同準備・二端読出しへ特殊化する。

Q1では、M37弱結合W型の最低2正常モードをR187でM54のW2信号へ接続し、R140が有限 $SU(2)$ 操作とRabi運動を与える。測定軸に対する2つの射影作用

```math
J_\pm
=
\mathcal J_0Z^\dagger P_\pm Z
```

を保持し、M65の3状態open selectorへ渡す。理想極限では

```math
P(r=\pm)
=
\frac{J_\pm}{J_++J_-}.
```

結果固定後はR181Dが物理信号を非線形に規格化せず、選ばれた非規格化結果成分 $P_rZ$ を同じ試行の次操作へ渡す。R143--R144とR189A--R189Cを合わせ、Born型2結果、逐次測定、有限Rabi--Zeno比較を構成する。

Q2-1とQ2-3ではR181Bが固定入力のテンソル積信号を作り、R181Cが同じ永続記憶部上で局所gateと結合gateを作用する。末端4結果または8結果はM66の特殊化R206で1回に標本化する。Q2-4ではR206Eで $0^n$ rootを一様準備し、R181Cの一般gate列後に $L=2^n$ のR206 samplerへ直接接続する。R206A--R206Cは逐次leaf探索、最小Born重みに依存する混合時間、結果別routerを避ける。一方、M54 direct-amplitude registerへ全自由度加法ノイズが入るR186の障害は残るため、Q2-4は条件付き達成を維持する。

Q2-2 fixed-goalはR207 projection phase-volume経路を使う。setting方向とhidden directionsをnear-contactで共同thermal preparationし、projection phase volumeとisotropic lockから一般角度singlet共同統計へ接続する。finite-lockでは余弦形のvisibilityを解析的に与え、finite thicknessでは一様全変動誤差を持つ。分離後はlocal response factorizationを保つ一方、source hidden stateはsetting-dependentでありmeasurement independenceは成立しない。

Q3のsignal数学はQ1/Q2と別の代数ではない。Q1型局所正準モードを空間頂点へ配置し、Q2型2体系結合を辺へ反復すると、Schrödinger型signal、局所作用、反対称currentが得られる。M37/R86がこのsignalを実古典振動子網から実装する。

M64はM37型classical coherent signal、一つのclassical tracer、一つのsignal-driven thermal reservoirからなるQ3 open modelである。R203Aはregularized density/current dictionary、R203Bはphase-volume free energy、continuous/finite-graph initial preparationとfinite-time mean-flow tracking、R203Cはcanonical overdamped tracerからregularized diffusionへの縮約、R203DはR161/R185およびfinite-graph位置読出しへの接続を与える。R203Bのreservoir sectorはR205Cの共通原理と整合するが、tracer dynamicsとQ3位置法則はM64固有である。

Q3-2の現行因果鎖は、M37/R86 signal、M64/R203A--R203C、R203D/R161、R185の順に進み、Nelson型・時間対称Newton則へ接続する。finite graphではR124の有限障壁、R182のW型トンネル振動、R125の2経路干渉を同じM64 tracerの位置読出しへ接続する。

固定目標の達成は、その目標が要求する現象を1試行内で明示的な物理interfaceを通して合成できるかで判定する。準備、全操作、測定、永久記録、reset、物理clock、次試行renewalまでを同じ装置architectureと共通反復周期へ統合することはM0で別に要求する。M66でreservoir原理を共通化したことは、共通単一bathまたは1台の製造済み装置を得たことを意味しない。

現行の固定目標ではQ1-1、Q1-2、Q2-1、Q2-2、Q2-3、Q3-1--Q3-5を達成、Q2-4を条件付き達成、Q3-6を未達とする。A1/A2/B1--B3は固定目標と独立に監査する。置換済みの旧作用殻型測定経路、旧paired-Hopf受信機構、Brownian macrospin読出し、M60/M61旧Q3 Hamiltonian実装は現行主線へ重ねず、研究メモとGit履歴へ保存する。
