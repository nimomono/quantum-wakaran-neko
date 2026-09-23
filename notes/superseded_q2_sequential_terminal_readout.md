# Q2旧逐次terminal readout経路の退役記録

> **現行注記（draft-127）**：Q2-1、Q2-3、Q2-4のterminal readoutはM66/R205--R206へ置換した。M65、R181D、R179そのものは退役していない。M65/R181DはQ1/Q2-2の逐次binary instrument、R179はQ2-2と全周期renewal側でactiveのままである。R192だけはfixed-goal上の責務を失ったためactive paperから退役した。

## 旧経路

draft-120--draft-126では、Q2のterminal計算基底読出しをbitごとのbinary treeで行っていた。

```text
terminal coherent signal
  -> projective actions for bit 1
  -> M65 selector
  -> R181D router
  -> non-normalized branch
  -> optional R192 action stabilization
  -> next bit
  -> ...
  -> R179 reset / renewal
```

固定有限深さのQ2-1/Q2-3ではこの経路で一試行interfaceを閉じていた。一般Q2-4では、小さい非終端branchを次のbinary selectorへ渡すためR192の作用下限回復と、反復運転にR179 open resetを直接依存として置いていた。

## 置換理由

M66/R206はterminal signalの全結果作用を同一規則のresult channelへ局所的に接続し、一回のfinite-$L$ common-hub samplingでjoint outputを作る。

```text
terminal coherent signal
  -> local actions |Z_y|^2
  -> M66 / R205 phase-volume reservoir
  -> R206A--R206D common-hub sampler
  -> joint result y
```

Q2-4ではさらに

```text
R206E root preparation
  -> R181C gate sequence
  -> R206D terminal sample
```

とする。

この変更により、

- terminal readoutの途中branchを次段へ渡さない。
- 最小Born重みがsampling mixing rateを縮めない。
- R181D treeをQ2-1/Q2-3/Q2-4で使わない。
- 非終端branch作用を回復するR192が不要になる。
- sampler pointerはR206A自身のmixingでrefreshでき、Q2-4の結果別resetにR179を使わない。

という責務縮約が起きる。

## 退役・維持の区別

- **R192**：責務消滅により退役。反証ではない。結果IDは再利用しない。
- **M65/R204**：Q1/Q2-2のbinary sequential instrumentとして維持。
- **R181D**：Q1逐次測定とQ2-2 A端--B端post-state handoffとして維持。
- **R179**：Q2-2およびM0/full-cycle renewal側のopen resetとして維持。
- **M66/R205--R206**：Q2-1/Q2-3/Q2-4 terminal readout正本へ昇格。
- **R186**：Q2-4 direct-amplitude registerのadditive-noise/precision障害として維持。

この退役はreader-side因果鎖の簡略化であり、Q2-1/Q2-3の達成ラベル、Q2-4の条件付き達成ラベルを変更しない。
