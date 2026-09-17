@number: 0
@chapter: 概要
@title: 概要

本論文の中心的な問いは、明示的な古典力学モデルから、量子力学に似た可逆操作、Born型測定統計、測定後状態、結合ゲート、Bell型共同統計、空間伝播がどこまで有効構造として現れるかである。複素振幅は独立した実体ではなく実正準信号の派生表示とし、単一試行の物理信号と試行集団の統計量を区別する。

M54をQ1--Q3の共通有効信号構成族、M37を空間信号とW型低2モードの物理実装層とする。状態準備・可逆操作と、排他的な測定結果形成を同一視しない。Q1/Q2の2結果射影読出しはR191ブラウン巨視的スピンinstrumentを正本とし、Q3ではM60の統一二成分chiral媒体、moving bath-frame carrier、平衡oscillator bath、局在tracerを共通ミクロ物理層とする。Q3の信号部分系はQ1/Q2と別の代数ではなく、Q1型局所正準信号を空間配置しQ2型2体系結合を辺へ反復した特殊化として整理する。

Q1/Q2の測定主線は

```math
Z
\longrightarrow
(J_+,J_-)
\xrightarrow{\mathrm{R191}}
r
\xrightarrow{\mathrm{R181D\ router}}
P_rZ
```

である。$J_\pm=\mathcal J_0Z^\dagger P_\pm Z$ を保持し、R191は作用和と作用差からブラウン巨視的スピンの吸引域境界を作る。理想極限では

```math
P(r=\pm)
=\frac{J_\pm}{J_++J_-}.
```

結果後は物理信号を非線形に規格化せず、R181Dの可逆projector routerが $P_rZ$ と補成分を分ける。次段R191は残った作用和で自動的に条件付き確率を読むため、固定有限深さでは振幅再調整を必須としない。一般深さQ2-4で結果成分作用が読出し下限へ落ちる場合だけ補助的な再調整を許す。

Q1ではM37弱結合W型の最低2正常モードをR187でM54のW2信号へ接続し、R140が有限 $SU(2)$ 操作とRabi運動を与える。R143--R144は分析器、有限コントラスト、局所記録、逐次測定の系列固有部分を担い、結果確率はR191、測定後結果成分はR181Dへ委ねる。R189A、R193、R189B--R189Cは走行中作用保持と有限2回Rabi--Zeno比較を与える。

Q2-1とQ2-3ではR181Bが固定入力のテンソル積信号を作り、R181Cが同じ永続記憶部上で局所gateと結合gateを作用する。末端測定はR191とR181Dだけを使う。Q2-4では同じ2結果nodeを逐次使用し、R179は結果相関履歴の排出とopen resetだけを担う。

Q2-2の現行証人は、固定一重項、固定有限設定族、非空間分離の逐次古典装置である。末端4モード信号にA設定を作用し、A端R191で結果 $r$ を形成した後、非規格化結果成分をprojector routerでB端へ渡す。B設定をそこで作用し、B端R191で $s$ を形成する。Q2-2固定目標は特定のBell前提違反を先に指定せず、採用した古典構成ごとに前提の成立・不成立を監査する。

```math
Z_{AB}
\xrightarrow{x}
\mathrm{R191}_A
\longrightarrow
P_{A,r}Z_{AB}
\xrightarrow{y}
\mathrm{R191}_B
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

Q3の信号部分系はQ1/Q2と別の代数ではない。Q1で使うものと同じ局所実正準モードを有限配置グラフの頂点へ置き、Q2で用いるのと同型の2体系エルミート結合を辺へ反復すると、グラフLaplacian型の空間伝播と反対称確率流が生じる。R195Aは各辺の信号をchiral作用 $I_\pm$ へ局所変換し、その和から局所密度、差からsignal currentとedge velocityを厳密に得る。2作用状態数とosmotic free energyはM60のR198A--R198D/R197Aが担い、$\pi_i\propto|Z_i|^2$ へ接続する。

Q3の粒子位置形成・輸送はQ1/Q2の測定結果形成とは別の因果鎖である。

```math
Z
\xrightarrow{\mathrm{R195A}}
(R,I_+,I_-)
\xrightarrow{\mathrm{R199A\ lead}}
(e_+,e_-)
\xrightarrow{\mathrm{R196A}}
(R,U_{\rm bath})
\xrightarrow{\mathrm{R196B}}
X_t
\xrightarrow{\mathrm{R196C/R161}}
L_{\rm R161}
\xrightarrow{\mathrm{R185}}
\text{Nelson / time-symmetric Newton}.
```

R199AはM60の同一chiral媒体からballistic leadを有限時間で分離してincident energyへ接続し、R196Aはそのwave pressureだけでmoving bath frameを作る。chiral媒体のthermalizationをleadへ課したり、drifting-Gibbsや非平衡FDTを仮定したりしない。R196Bでは別の平衡oscillator bathだけにFDTを適用し、periodic homogenizationを経て $D=\nu$、$j/\rho+O(a^2)$、$\nu\partial_x\log\rho$ を得る。R196Cはwell-index generatorをR161へ有限誤差で接続する。

R162のopen Poisson-jump過程はQ3の基礎的実体ではなく、その理想jump lawを表す参照過程として残す。R185は同じ前向き経路法則のBayes反転からNelson型の前進・後退平均微分と時間対称Newton則へ接続する。

この再編で、旧R190A--R190Cの2作用LC殻Drude混合、R170静的吸収pointer、R180B paired-Hopf受信機構は固定Q1/Q2の必須主線から退役した。M56 Brownian-spin Q3模型はspin-only代替研究線へ下げ、Q3の現行ミクロ主線には使わない。内容は `notes/` とGit履歴へ保存し、反証されたものとして扱わない。論文本文では同じBorn結果を複数の物理経路で重複説明せず、現在の最小因果鎖だけを正本とする。
