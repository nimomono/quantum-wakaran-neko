@number: 9
@chapter: 本文
@title: 結論
@status: Q1/Q2のR191系と、Q3のM37/R86--M64/R203A--R203D--R161--R185現行階層を総括する。M60/M61旧Hamiltonian実装は現行主線から退役する。

本稿は、古典実正準信号の線形力学と、1試行1結果を作る開放古典instrumentを分離して構成した。有限次元Hilbert空間とunitaryを古典振動子へ写すこと自体ではなく、その同じ単一試行信号からBorn型排他的結果と測定後結果成分を作る物理接続を中心課題とした。

Q1/Q2の2結果測定はR191へ統一した。二つの射影作用

```math
J_\pm=\mathcal J_0Z^\dagger P_\pm Z
```

の和と差をブラウン巨視的スピンの一軸異方性とbiasへ結合すると、理想吸引域測度から

```math
P(\pm)=\frac{J_\pm}{J_++J_-}
```

を得る。R191は有限混合時間、transducer誤差、guard、有限温度retreat、有限decision時間、端点dispatcher、無反応、吸収記録を同じ完全結果誤差へまとめる。

結果後の状態更新はR181Dの可逆projector routerへ縮約した。物理信号を規格化し直さず

```math
Z\longmapsto P_rZ
```

を次段へ渡すだけで、次のR191が残った作用和を分母として条件付きBorn重みを読む。有限段では確率積がtelescopingしてLüders型共同分布を回収する。一般深さQ2-4で結果成分作用が読出し下限を下回る場合だけ振幅再調整を補助手段として残す。

Q1ではR187がM37弱結合W型最低2正常モードをW2制御信号へ接続し、R140がBloch球型可逆操作とRabi運動を与える。R143--R144は分析器・記録・逐次測定、R189A、R193、R189B--R189Cは走行中作用保持と有限Rabi--Zeno比較を担う。Born結果形成をW型粒子位置の再平衡化へ依存させない。R193はR189Aの保持座標をR191 macrospinのdecision energyへ直接Hamiltonian結合し、Q1に残っていた抽象transducer接続を具体化する。

Q2-1とQ2-3ではR181B/R181Cが永続多モード信号上のテンソル積状態とgate列を作り、末端R191/R181Dが出力を標本化する。Q2-4では同じ2結果nodeを一般回路出力へ逐次適用し、R179はopen resetと履歴排出、R186は外部運用資源とノイズ境界を監査する。

Q2-2の現行証人では、固定一重項4モード信号にA設定を作用し、A端R191で $r$ を形成して結果成分 $P_{A,r}^{x}Z$ をB端へ渡し、B設定後のB端R191で $s$ を形成する。Q2-2固定目標は特定のBell前提違反を先に指定せず、採用構成ごとに前提の成立・不成立を監査する。共同分布は

```math
P(r,s\mid x,y)
=
\frac{\|P_{B,s}^{y}P_{A,r}^{x}Z\|^2}{\|Z_{AB}\|^2}
```

であり、一重項型信号では余弦共同相関、非信号性、CHSH/Tsirelson値を再現する。この装置はA結果成分をB端へ渡す非空間分離装置であり、現行証人ではBell局所因子化を仮定しない。設定前の一重項源は設定非依存であり、現行証人のCHSH破れを測定設定独立性の破れへ限定して解釈しない。

Q3の粒子位置はQ1/Q2の測定結果とは別の因果鎖を持つ一方、そのsignal数学は共通である。Q1型の局所正準モードを空間頂点へ配置し、Q2型の2体系結合を辺へ反復すると、局所作用から位置重み、連続方程式から反対称currentが得られる。M37/R86はこのSchrödinger型signalを実古典振動子網から有限時間で実装する。

M64/R203A--R203Dは、このsignalへ一つのclassical tracerと一つのsignal-driven thermal reservoirを接続する現行Q3 open modelである。R203Aはregularized density/current dictionary、R203Bはphase-volume free energy、continuous/finite-graph initial preparationとfinite-time mean-flow tracking、R203Cはcanonical overdamped tracerのregularized diffusion縮約を与える。R203Dは1次元ではR161/R185へ、finite graphではR124、R182、R125の位置読出しへ接続する。

Q3-2の現行因果鎖は、M37/R86 signalからM64/R203A--R203Cへ進み、R203D/R161を介してR185のNelson型・時間対称Newton則へ接続する。

R185の時間対称Newton残差とM64 micro-to-effective process reduction errorは別々の量として管理する。finite graphでは初期準備、generator実装、終位置recordを一度ずつ数え、有限障壁、W型トンネル振動、2経路干渉の正の位置分布差が有限誤差後にも残る条件を明示する。

R162のopen Poisson-jump過程はM64の基礎的実体ではなく、R161 lawのoptional stochastic referenceとして残す。Q1/Q2の測定pointerをQ3粒子へ同一視しない。R184の旧空間率latchも補助結果であり、M64主線の必須依存ではない。

M60/M61のDuffing shell、統一chiral媒体、ballistic lead、moving reflector、single-Hamiltonian parentは、より複雑な旧Hamiltonian実装として現行論文主線から退役する。反証されたものとして扱わず、Git履歴に保存する。M56 Brownian-spin Q3模型は引き続きspin-only代替研究線とする。

残る主要な物理課題は、各固定目標について具体的古典ミクロ模型A1とその直接数値再現A2を独立に監査すること、Q1/Q2について具体的アナログ回路B1、実験可能パラメータ領域B2、回路直接数値再現B3へ進むこと、Q2-2で測定窓内の空間的・因果的隔離をQ2-2-Sで検査することにある。Q3ではM64採用open equationsのdirect A2、finite-bandwidth/Hamiltonian lift、clock・終位置record・resetを含む単一反復周期、連続空間一様極限、多粒子拡張、Q3-6の位相量子化を強化・未解決課題として残す。M64の正式昇格だけからA1/A2の状態を自動的に上げない。
