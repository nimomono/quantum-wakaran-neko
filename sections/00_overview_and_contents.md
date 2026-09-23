@number: 0
@chapter: 概要
@title: 概要

本論文の中心的な問いは、明示的な古典力学モデルから、量子力学に似た可逆操作、Born型測定統計、測定後状態、結合ゲート、Bell型共同統計、空間伝播がどこまで有効構造として現れるかである。複素振幅は独立した実体ではなく実正準信号の派生表示とし、単一試行の物理信号と試行集団の統計量を区別する。

M54をQ1--Q3の共通有効信号構成族、M37を空間信号とW型低2モードの物理実装層とする。状態準備・可逆操作と、排他的な測定結果形成を同一視しない。Q1とQ2-2の逐次binary読出しはM65の3状態open selector、Q2-1/Q2-3/Q2-4のterminal joint readoutはM66/R206を正本とし、Q3ではM37/R86をsignal実装、M64/R203A--R203Dを粒子・Nelson open modelの正本とする。Q3の信号部分系はQ1/Q2と別の代数ではなく、Q1型局所正準信号を空間配置しQ2型2体系結合を辺へ反復した特殊化として整理する。

Q1とQ2-2の逐次測定主線は

```math
Z
\longrightarrow
(J_+,J_-)
\xrightarrow{\mathrm{M65/R204D}}
r
\xrightarrow{\mathrm{R181D\ router}}
P_rZ
```

である。$J_\pm=\mathcal J_0Z^\dagger P_\pm Z$ を保持し、M65は保持作用を3状態open pointerの線形rateへ入れる。理想極限では

```math
P(r=\pm)
=\frac{J_\pm}{J_++J_-}.
```

結果後は物理信号を非線形に規格化せず、R181Dの可逆projector routerが $P_rZ$ と補成分を分ける。次段M65はその時点の二射影作用を読み、同じBorn作用比を形成するため、Q1/Q2-2の固定有限深さでは振幅再調整を必須としない。

Q1ではM37弱結合W型の最低2正常モードをR187でM54のW2信号へ接続し、R140が有限 $SU(2)$ 操作とRabi運動を与える。R143--R144は分析器、有限コントラスト、局所記録、逐次測定の系列固有部分を担い、結果確率はM65、測定後結果成分はR181Dへ委ねる。R189A--R189Cは走行中作用保持と有限2回Rabi--Zeno比較を与える。

Q2-1とQ2-3ではR181Bが固定入力のテンソル積信号を作り、R181Cが同じ永続記憶部上で局所gateと結合gateを作用し、末端4結果/8結果をM66/R206で一回標本化する。Q2-4ではR206Eで $0^n$ rootを一様準備し、R181Cの一般gate列後にM66/R206の $2^n$ 結果samplerへ直接接続する。

Q2-2の現行証人は、固定一重項、固定有限設定族、非空間分離の逐次古典装置である。末端4モード信号にA設定を作用し、A端M65で結果 $r$ を形成した後、非規格化結果成分をprojector routerでB端へ渡す。B設定をそこで作用し、B端M65で $s$ を形成する。Q2-2固定目標は特定のBell前提違反を先に指定せず、採用した古典構成ごとに前提の成立・不成立を監査する。

```math
Z_{AB}
\xrightarrow{x}
\mathrm{M65}_A
\longrightarrow
P_{A,r}Z_{AB}
\xrightarrow{y}
\mathrm{M65}_B
\longrightarrow
(r,s).
```

局所射影が可換なので共同分布は

```math
P(r,s\mid x,y)
=
\frac{\|P_{B,s}^{y}P_{A,r}^{x}Z_{AB}\|^2}{\|Z_{AB}\|^2}.
```

一重項型信号では余弦共同統計、非信号性、CHSH/Tsirelson値を回収する。A結果成分がB端へ物理的に渡るため、現行証人はBell局所因子化を満たす空間分離模型ではない。自由設定・空間分離・loophole-free Bell実験の古典局所説明を現行証人から主張しない。測定窓内の因果隔離をどこまで強められるかはQ2-2-Sで別に監査する。

Q2-2-Sには付録WのR207A--R207Dを新しいcandidateとして置く。M66/R205Eのjoint thermal preparationとR205Fのpassive separationを使い、分離後local responseとmeasurement dependenceを分けて監査する。ただしfinite-speed spatial reservoirが未監査なので、Q2-2-Sの未監査状態は変更しない。

Q3の信号部分系はQ1/Q2と別の代数ではない。Q1で使うものと同じ局所実正準モードを有限配置グラフの頂点へ置き、Q2で用いるのと同型の2体系エルミート結合を辺へ反復すると、グラフLaplacian型の空間伝播と反対称確率流が生じる。M37/R86がこのSchrödinger型signalを古典実振動子網から有限時間で実装する。

Q3の粒子位置形成・輸送はM64/R203A--R203Dが担う。単一試行の実体はM37型classical coherent signal、一つのclassical tracer、一つのsignal-driven thermal reservoirの三つである。R203Aはregularized density/current dictionary、R203Bはphase-volume free energy・continuous/finite-graph initial preparation・finite-time mean-flow tracking、R203Cはcanonical overdamped tracerからideal regularized diffusionへの縮約、R203Dは1次元R161/R185と一般finite-graph R124/R182/R125位置読出しへの接続を与える。

Q3-2の現行因果鎖は、M37/R86 signalからM64/R203A--R203Cへ進み、R203D/R161を介してR185のNelson型・時間対称Newton則へ接続する。

M60/M61のDuffing shell、chiral-medium、ballistic lead、single-Hamiltonian parentはより複雑な旧Hamiltonian実装として現行主線から退役し、Git履歴に保存する。固定目標は一試行内の物理interfaceを共通最低条件として判定し、M64/R203DがR124/R182/R125を同じtracerの位置読出しへ接続するQ3-4A、Q3-4B、Q3-5は達成とする。A1/A2は固定目標と独立に監査し、本昇格だけから自動的に状態を変更しない。

R162のopen Poisson-jump過程はQ3の基礎的実体ではなく、その理想jump lawを表す参照過程として残す。R185は同じ前向き経路法則のBayes反転からNelson型の前進・後退平均微分と時間対称Newton則へ接続する。

この再編で、旧作用殻型測定経路、旧paired-Hopf受信機構、Brownian macrospin読出しとQ1直接decision bridgeは現行論文主線から退役した。M56 Brownian-spin Q3模型はspin-only代替研究線へ下げ、Q3の現行ミクロ主線には使わない。内容は `notes/` とGit履歴へ保存し、反証されたものとして扱わない。論文本文では同じBorn結果を複数の物理経路で重複説明せず、現在の最小因果鎖だけを正本とする。

## M66 common-reservoir parentとR206多結果readout

M66/R205A--R205Fは、phase-volume、mean-flow、thermal sampling、passive separationを共通化するthermal-reservoir parentである。M64/M65のdomain modelを置換せず、Q2-1/Q2-3/Q2-4のterminal readoutではR206A--R206EをM66の特殊化として使う。

```math
Z_{\rm out}
\longrightarrow
\{J_y=\mathcal J_0|Z_y|^2\}_{y\in\Omega_L}
\longrightarrow
\mathrm{R206}
\longrightarrow
Y\in\Omega_L
```

Q2-1では $L=4$、Q2-3では $L=8$、Q2-4では $L=2^n$ とする。R206Aのcommon-hub samplerはmixing rateを $L$ と最小Born重みに依存させず、R206Bは全channelを同一の局所phase-volume規則で実装する。R206Cはfinite-time/fabrication error、R206DはQ2 terminal bridge、R206EはQ2-4のuniform root preparation / refreshを与える。

R205CはM64/R203Bのpartition/free-energyとmean-flow分離、R205DはM65/R204Bのfixed-hub実現をcommon parentへ埋め込む。R205E/Fはgeneral thermal preparationとpassive spatial separationを与え、Q2-2-Sでは付録W/R207A--R207Dのcandidateへ接続する。ただしfinite-speed physical isolationは未監査である。

Q2-1/Q2-3/Q2-4ではterminal readout後に結果成分を次段へ渡さないためR181D treeやR192作用回復を使わない。Q1/Q2-2の逐次binary measurementはM65/R181Dを維持する。Q2-4の条件付き達成はR186のdirect-amplitude register additive-noise障害が残るため変更しない。
