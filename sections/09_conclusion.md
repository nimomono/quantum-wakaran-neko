@number: 9
@chapter: 本文
@title: 結論
@status: M54/M37の現行信号階層、Q1型局所信号＋Q2型辺結合からQ3空間 $(\pi,j)$ への接続、Q1/Q2のR191 2結果読出し、Q2-2の2端逐次R191、Q3のM57--R195--R161/R162--R185位置経路を総括する。

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

Q2-2では、固定一重項4モード信号にA設定を作用し、A端R191で $r$ を形成して結果成分 $P_{A,r}^{x}Z$ をB端へ渡し、B設定後のB端R191で $s$ を形成する。共同分布は

```math
P(r,s\mid x,y)
=
\frac{\|P_{B,s}^{y}P_{A,r}^{x}Z\|^2}{\|Z_{AB}\|^2}
```

であり、一重項型信号では余弦共同相関、非信号性、CHSH/Tsirelson値を再現する。この装置はA結果成分をB端へ渡す非空間分離装置であり、Bell局所性を主張しない。

Q3の粒子位置はQ1/Q2の測定結果とは別の因果鎖を持つ一方、その信号数学は共通である。Q1型の局所正準モードを空間頂点へ配置し、Q2型の2体系結合を辺へ反復すると、局所作用から $\pi$、連続方程式から反対称流 $j$ が得られる。M57はこの信号を、一個の局在tracer、2作用状態数、左右独立のpinned open transmission lineへ接続する。R195Aがchiral作用と状態数、R195Bがfinite port slaving・mixing・force correlation、R195CがGreen--Kubo/FDTとperiodic-tracer縮約、R195DがR161生成子への有限時間matchingを与える。

M57では

```math
I_++I_-=R_i+R_j,
\qquad
I_+-I_-=2\operatorname{Im}(Z_i^*Z_j)
```

によりsignal densityとcurrentを同じedge actionへ分解する。2作用状態数は $\Omega_i^\delta\propto R_i^\delta$ を与え、dual TLのwind/friction比はcurrent driftを作る。FDTとKramers/Lifson--Jackson縮約に対して

```math
g_Kc=\frac{4\nu}{a}
```

を課すと、長時間diffusion $D_{\rm hop}=\nu$ とcurrent drift係数が同じmatchingで一致する。R195Dはこのcoarse-grained tracer generatorをR161形式へ写し、signal-current理想生成子との差を有限誤差 $\varepsilon_{57}$ で制御する。

従ってQ3の現行因果鎖は、M37/M54空間信号からR195Aで2作用状態数とchiral作用 $I_\pm$ を取り出し、M57/R195B--R195Cで $(\pi,j,t)$ を形成し、R195D/R161で位置過程 $X_t$ へ接続した後、R185でNelson型時間対称Newton則へ進む。

R162のopen Poisson-jump過程はM57の基礎的実体ではなく、R195Dが比較するideal stochastic referenceとして残す。R185は同じ前向き経路法則のBayes反転から前進・後退平均微分と時間対称Newton則へ接続する。Q1/Q2の測定pointerをQ3粒子へ同一視しない。

今回の縮約により、R184の旧M37--M54空間率latchは補助結果へ下がり、M57主線の必須依存から外れた。M56 Brownian-spin Q3模型はspin-only代替研究線へ位置づける。R190A--R190C、R170、旧R180Bも現行Q1/Q2主線へ戻さない。これらは反証されたのではなく、別の物理実現・強化案として `notes/` とGit履歴へ保存する。

残る主要な物理課題は、R191の作用和・作用差transducer、Brownian macrospin、projector router、外部record、R179 resetを同じ具体装置へ統合すること、M37 signal sourceとM57 tracer、clock、終位置recordを単一反復周期へ統合すること、Q2-4の外部多項式資源条件を物理配線・較正・ノイズまで閉じること、Q3のcontinuous-space一様極限・多粒子拡張、Q3-6の位相量子化を閉じることである。
