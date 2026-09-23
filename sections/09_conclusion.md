@number: 9
@chapter: 本文
@title: 結論
@status: Q1/Q2-2のM65/R181D逐次系、Q2-1/Q2-3/Q2-4のM66/R206 terminal readout系、Q3のM37/R86--M64/R203A--R203D--R161--R185現行階層を総括する。R192、R191/R193、M60/M61旧実装は現行主線から退役する。

本稿は、古典実正準信号の線形力学と、1試行1結果を作る開放古典instrumentを分離して構成した。有限次元Hilbert空間とunitaryを古典振動子へ写すこと自体ではなく、その同じ単一試行信号からBorn型排他的結果と測定後結果成分を作る物理接続を中心課題とした。

Q1およびQ2-2の逐次2結果測定はM65へ統一した。二つの射影作用

```math
J_\pm=\mathcal J_0Z^\dagger P_\pm Z
```

を保持し、M65の3状態open pointerへ線形rateとして入力する。有限decision後にgeneratorを閉じてR112型recordへ結果を固定する。理想極限では

```math
P(\pm)=\frac{J_\pm}{J_++J_-}
```

を得る。M65はfinite-time relaxation、hub無反応、exact endpoint、有限recordを同じ完全結果誤差へまとめる。

Q1/Q2-2で結果後の状態を次操作へ渡す場合はR181Dの可逆projector routerへ縮約した。物理信号を規格化し直さず

```math
Z\longmapsto P_rZ
```

を次段へ渡すだけで、次のM65がその時点の二射影作用から条件付きBorn重みを形成する。有限段では確率積がtelescopingしてLüders型共同分布を回収する。

Q1ではR187がM37弱結合W型最低2正常モードをW2制御信号へ接続し、R140がBloch球型可逆操作とRabi運動を与える。R143--R144は分析器・記録・逐次測定、R189A--R189Cは走行中作用保持と有限Rabi--Zeno比較を担う。Born結果形成をW型粒子位置の再平衡化へ依存させず、R189Aの保持座標をM65へ直接入力する。

Q2-1とQ2-3ではR181B/R181Cが永続多モード信号上のテンソル積状態とgate列を作り、末端M66/R206が4結果/8結果を一回で標本化する。Q2-4ではR206Eで $0^n$ rootを一様準備し、R181Cの一般gate列後にM66/R206の $2^n$ 結果samplerへ接続する。reader側の逐次小branch、R181D tree、作用再調整、結果別resetは主線から消え、R186が外部運用資源とdirect-amplitude registerノイズ境界を監査する。Q2-4はR186条件が残るため条件付き達成を維持する。

Q2-2の現行証人では、固定一重項4モード信号にA設定を作用し、A端M65で $r$ を形成して結果成分 $P_{A,r}^{x}Z$ をB端へ渡し、B設定後のB端M65で $s$ を形成する。Q2-2固定目標は特定のBell前提違反を先に指定せず、採用構成ごとに前提の成立・不成立を監査する。共同分布は

```math
P(r,s\mid x,y)
=
\frac{\|P_{B,s}^{y}P_{A,r}^{x}Z\|^2}{\|Z_{AB}\|^2}
```

であり、一重項型信号では余弦共同相関、非信号性、CHSH/Tsirelson値を再現する。この装置はA結果成分をB端へ渡す非空間分離装置であり、現行証人ではBell局所因子化を仮定しない。設定前の一重項源は設定非依存であり、現行証人のCHSH破れを測定設定独立性の破れへ限定して解釈しない。

Q2-2-SについてはR207A--R207Dをcandidateとして追加した。R207Aは共通thermal preparationで公平なsetting sectorを作り、R207Bはdeep-well/strong-lock極で有限parameterのCHSH/Tsirelson witnessを与える。R207CはR205Fによる分離後local response factorizationとsource--setting measurement dependenceを分け、R207Dはmeasurement-independent local controlで $|S|\le2$ を回収する。finite-speed spatial reservoirとcontinuous full trajectoryが未監査なので、この追加だけからQ2-2-Sの達成状態は変更しない。

Q3の粒子位置はQ1/Q2の測定結果とは別の因果鎖を持つ一方、そのsignal数学は共通である。Q1型の局所正準モードを空間頂点へ配置し、Q2型の2体系結合を辺へ反復すると、局所作用から位置重み、連続方程式から反対称currentが得られる。M37/R86はこのSchrödinger型signalを実古典振動子網から有限時間で実装する。

M64/R203A--R203Dは、このsignalへ一つのclassical tracerと一つのsignal-driven thermal reservoirを接続する現行Q3 open modelである。R203Aはregularized density/current dictionary、R203Bはphase-volume free energy、continuous/finite-graph initial preparationとfinite-time mean-flow tracking、R203Cはcanonical overdamped tracerのregularized diffusion縮約を与える。R203Dは1次元ではR161/R185へ、finite graphではR124、R182、R125の位置読出しへ接続する。

Q3-2の現行因果鎖は、M37/R86 signalからM64/R203A--R203Cへ進み、R203D/R161を介してR185のNelson型・時間対称Newton則へ接続する。

R185の時間対称Newton残差とM64 micro-to-effective process reduction errorは別々の量として管理する。finite graphでは初期準備、generator実装、終位置recordを一度ずつ数え、有限障壁、W型トンネル振動、2経路干渉の正の位置分布差が有限誤差後にも残る条件を明示する。

R162のopen Poisson-jump過程はM64の基礎的実体ではなく、R161 lawのoptional stochastic referenceとして残す。Q1/Q2の測定pointerをQ3粒子へ同一視しない。置換済みの旧Q3率latchは現行論文の結果一覧と証拠鎖へ戻さず、研究メモとGit履歴に保存する。

M60/M61のDuffing shell、統一chiral媒体、ballistic lead、moving reflector、single-Hamiltonian parentは、より複雑な旧Hamiltonian実装として現行論文主線から退役する。反証されたものとして扱わず、Git履歴に保存する。M56 Brownian-spin Q3模型は引き続きspin-only代替研究線とする。

固定目標は一試行内の物理interfaceを共通最低条件とする。この基準でQ2-1、Q2-2、Q2-3、Q3-4A、Q3-4B、Q3-5は達成し、固定目標上の未完成はQ2-4の一様装置族・資源条件とQ3-6の位相量子化に残る。準備、全操作、測定、永久記録、reset、物理clock、次試行renewalまでを一つのjoint microscopic device/processへ統合することはM0で別に要求する。

残る主要な物理課題は、各固定目標について具体的古典ミクロ模型A1とその直接数値再現A2を独立に監査すること、Q1/Q2について具体的アナログ回路B1、実験可能パラメータ領域B2、回路直接数値再現B3へ進むこと、Q2-2で測定窓内の空間的・因果的隔離をQ2-2-Sで検査することにある。Q3ではM64で直接定めた開放方程式のA2直接数値再現、finite-bandwidth/Hamiltonian lift、永久record・reset・物理clock・renewalを含む単一反復周期、連続空間一様極限、多粒子拡張、Q3-6の位相量子化を強化・未解決課題として残す。M64の正式昇格だけからA1/A2の状態を自動的に上げない。


M65をQ1/Q2-2二結果逐次instrumentとして維持する。最小模型は $+,H,-$ の3状態Markov pointerであり、保持済み二作用はhubから各結果へのrateへ線形に入る。R204Dは有限時間Born誤差、R204Eは共通binary selector contract、R204FはQ1互換性と有限latency条件を与える。phase-volume chamberとHamiltonian--Brownian縮約はR204B/R204Cの追加実現・強化結果へ分離した。

R181DとR180A/R180Cはselector内部物理から独立なinterfaceを介してM65へ接続する。R179はQ2-2および全周期renewal側に残す。R192はQ2-4逐次treeの消滅に伴い退役する。旧R191 Brownian macrospin読出しとR193 Q1直接decision bridgeはM65へ責務を吸収したため現行主線から退役し、notes/Git履歴へ保存する。

## M66 common-reservoir parentとR206の現在地

M66/R205A--R205Fは、M64/R203B、M65/R204B、R206に共通するthermal-reservoir layerを抽出する。R205A/R205Cはphase-volume free energyとmean-flow shiftの両立、R205B/R205Dはmatched capacity--conductance、R205Eは $p_{\rm eq}\propto we^{-\beta H_{\rm cfg}}$ のthermal sampling、R205Fは距離増加による受動的generator separationを与える。M66はM64のQ3 tracer/Nelson modelやM65のbinary selectorそのものを置換しない。

Q2 terminal readoutはM66の特殊化R206A--R206Eを現行fixed-goal主線として維持する。Q2-1で4結果、Q2-3で8結果、Q2-4で $2^n$ 結果を同じ局所規則から標本化し、mixing時間とaggregate fabrication-error boundを $L$ に直接依存させない。R206Eは全mode共通減衰と固定root driveでQ2-4のroot preparation/refreshを与え、sampler pointerはR206A自身のmixingにより結果別resetを必要としない。

Q1/Q2-2のM65/R181D逐次interfaceは維持する。Q2-4の条件付き達成はR186のdirect-amplitude register additive-noise障害が残るため変更しない。R205FをQ2-2-Sの空間分離Bell構成へ適用する作業は後続強化へ残す。
