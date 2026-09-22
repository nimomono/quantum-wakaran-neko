# R184 M37開始作用保持機構の退役記録

## 位置づけ

R184はdraft-73で導入した、M37局所包絡を旧M54 spatial-moving rateへ接続する補助結果である。開始面の総作用を単一試行ごとに保持し、M37包絡の有限時間誤差をMarkov率誤差と位置分布誤差へ渡すために使っていた。

draft-112でM64/R203A--R203DをQ3の現行particle/Nelson open modelへ昇格し、draft-122でQ3-4A/Q3-4B/Q3-5の位置読出しもM64/R203D finite-graph tracerへ完全に切り替えた。これによりR184を必要とする固定目標・現行証拠鎖がなくなったため、draft-123でactive paperから退役する。

退役はR184の数式を反証したことを意味しない。結果番号R184は再利用しない。

## 旧主張の核

M37局所包絡を $b(t)$、同じ初期値から進む理想信号を $b_L(t)$ とし、開始面で

```math
S_{\rm ref}=\|b(0)\|^2
```

を保持する。旧率構成では

```math
R_{i,37}^{\delta,\mathrm{lat}}(t)
=
|b_i(t)|^2+\delta q_iS_{\rm ref},
```

```math
T_{ij,37}^{\delta,\mathrm{lat}}(t)
=
\frac{|h_{ij}|}{\mathcal J_0}
\left(
R_{i,37}^{\delta,\mathrm{lat}}
+
R_{j,37}^{\delta,\mathrm{lat}}
\right),
```

```math
k_{i\to j}^{37,\mathrm{lat}}
=
\frac{
T_{ij,37}^{\delta,\mathrm{lat}}
+
J_{i\to j}(b)
}{
2R_{i,37}^{\delta,\mathrm{lat}}
}
```

を使う。R86のcarrier誤差を $\varepsilon_{\rm car}(T)$、局所化誤差を $\Delta=\delta_{\rm loc}(\eta)<1$ とすると、旧R184は

```math
\max_i\sum_{j\ne i}
|k_{i\to j}^{37,\mathrm{lat}}-k_{i\to j}^{L}|
\le
L_\delta(\eta)\varepsilon_{\rm car}(T)
```

を与えた。従って同じ初期位置分布から始める有限状態Markov過程について

```math
\sup_{0\le t\le T}
D_{\rm TV}
\left(
P(X_t^{37,\mathrm{lat}}\in\cdot),
P(X_t^L\in\cdot)
\right)
\le
T L_\delta(\eta)\varepsilon_{\rm car}(T)
```

と評価し、旧完全結果誤差を

```math
\varepsilon_{184}
=
\varepsilon_{\rm init}
+
T L_\delta\varepsilon_{\rm car}
+
\varepsilon_{\rm rec}
```

と整理していた。

## 退役理由

現行M64では開始作用を別の保持機構へ固定してM54率へ合わせる必要がない。R203AがM37 signalからregularized density/currentを直接作り、R203Bがinitial tracer preparation、R203Cがcanonical overdamped continuous tracer、R203Dがfinite-graph tracerとR161 rateを直接与える。

現行因果鎖は

```text
M37/R86 signal
→ M64/R203A--R203D
→ R161
→ R185
```

であり、Q3-4A/Q3-4B/Q3-5も

```text
R124 / R182 / R125 signal
→ M64/R203D finite-graph tracer
→ position readout
```

へ接続する。したがって旧M37→M54 rate-latch bridgeを併置すると、同じsignal-to-particle責務を二重化するだけになる。

## 再利用条件

将来、M64を使わず生M37局所包絡からR161 generatorへ直接持ち上げる有限Hamiltonian strengtheningを再検討し、開始総作用を固定背景として物理的に保持する必要が生じた場合には、R184のLipschitz評価を再利用できる。その場合も現行M64主線とは別の実装候補として扱う。

## 履歴

- 初出: draft-73
- 主定理追加: commit `10401e6b3e2b787344866862c7f31f9a15c08597`
- 数値回帰拡張: commit `79e0564612885add4412afa6dfe617a4f0195f24`
- 退役直前のactive版: commit `bbcf119cd9b1a25ddb5b0b6b36a20cb94557575b`
- 旧定理・完全証明: 退役直前の `sections/A14_m54_spatial_moving_matching.md`
- 旧数値検算: 退役直前の `tools/verify_m54_spatial_matching.py`

完全な旧証明・旧検算コードはGit履歴を正本とし、このメモへ複製しない。
