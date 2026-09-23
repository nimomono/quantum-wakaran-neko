# 理論系譜と現行正本への入口

このメモは、置換済み研究メモに残る「当時の現行」「次の置換先」と、現在の正本を混同しないための入口である。個別メモの本文は、その版で何を採用していたかを追跡できるよう原則として歴史的表現を保持する。**現在の採用状態そのものは `PROJECT_STATUS.md` を正本**とし、退役結果のID・旧用途・保存先は `superseded_result_index.md` を正本とする。

## 現行の主要因果鎖

### Q1/Q2の測定

現行の二結果測定は、保持済み射影作用をM65へ渡し、M65/R204D--R204Fで有限時間の結果形成とrecordを行い、R181Dで対応する非規格化射影成分を同じ試行の次段へ渡す。

```text
finite canonical signal
  -> projective actions
  -> M65 / R204D--R204F
  -> finite record
  -> R181D projector router
```

Q2-4で非終端結果の絶対作用下限を保つ必要がある場合だけR192を接続し、試行間のopen reset / renewalはR179が担う。

主要な旧測定経路は次の順に置換された。

```text
M35 long-time sampler
  -> M50 / R164 / R170 action-shell route
  -> R191 / R193 Brownian-macrospin route
  -> M65 / R204 canonical open selector
```

途中の模型・結果は反証されたという意味ではなく、現行fixed-goal因果鎖での責務をより短い経路へ置換したものである。

### Q3の粒子・Nelson経路

現行Q3では、M37/R86が古典空間signalを与え、M64/R203A--R203Dが一つのclassical tracerとsignal-driven thermal reservoirを接続する。finite-state表現はR161へ、1次元Nelson/time-symmetric Newton則はR185へ接続する。

```text
M37 / R86 signal
  -> M64 / R203A--R203D
  -> R161 canonical path law
  -> R185 time-symmetric Newton
```

finite graphでは同じM64/R203D tracerをR124、R182、R125の位置読出しへ接続する。R162はR161 lawのoptional open-Poisson realizationであり、現行Q3の基礎的物理存在論ではない。

Q3の主要な置換履歴は概略として

```text
M42 / R172--R174
  -> M55 / R183--R185
  -> M54 spatial + R184 auxiliary latch
  -> M64 / R203A--R203D + R161 / R185
```

である。M57/M59/M60/M61は途中で検討したより具体的なHamiltonian実装線であり、M64昇格後は現行主線から退役した。

### Q2 register / Bell経路

Q2の永続register・gateはM54/R181B--R181Cへ整理され、末端読出しはM65/R181Dへ統一されている。Q2-2の現行証人は、固定一重項4モードsignalにA設定を作用し、A端M65の結果でR181D型routerを制御して非規格化結果成分をB端へ渡し、B設定とB端M65を順に実行する非空間分離構成である。

旧M41 Bell周期、独立M48 paired-Hopf経路、M49/M52の中間register構成は、それぞれ個別の退役メモとGit履歴へ保存する。

## 履歴メモの読み方

1. 個別の `superseded_*.md` は、その模型・結果を退役させた時点の議論を保存する。本文中の「現行」「正本」「置換先」は、その時点の意味で残る場合がある。
2. 最新の正本を知りたい場合は、まず `PROJECT_STATUS.md` を読む。
3. ある退役結果の保存先を知りたい場合は `superseded_result_index.md` を読む。
4. 旧メモ中の中間置換先がさらに退役している場合、このメモの現行因果鎖まで辿る。
5. 旧番号は再利用しない。現行結果宣言と退役索引の結果IDが交差しないことはCIで機械検査する。
6. 完全な旧章・旧付録・旧検算コードはnotesへ複製せず、対応コミットとGit履歴を正本とする。

## 主な退役メモへの入口

- Q1/Q2作用殻測定: `superseded_r164_q1q2_measurement_role.md`、`superseded_r190_r170_measurement_path.md`
- Brownian macrospin測定: `superseded_r191_brownian_macrospin_projective_instrument.md`、`superseded_r193_q1_macrospin_bridge.md`
- Q3旧rate latch: `superseded_r184_m37_rate_latch.md`
- Q3旧Poisson存在論: `superseded_q3_poisson_microphysics.md`
- Q3旧連続粒子模型: `superseded_m42_continuous_particle_position.md`
- Q3旧Hamiltonian実装群: M57/M59/M60/M61関連のsuperseded notesとGit履歴
- Q2旧register/Bell: `superseded_m49_joint_bath_cnot_provider.md`、`superseded_m52_path_only_design.md`、`superseded_independent_m48_bell_protocol.md`

このメモは理論結果を追加せず、現行正本と歴史記録のナビゲーションだけを与える。

## M66/R205--R206 candidate branch

現行のQ2読出し系譜とは別に、draft-126で次のpromotion candidateを追加する。

\`\`\`text
terminal coherent signal
  -> local actions |Z_y|^2
  -> M66 / R205 common phase-volume reservoir
  -> R206 finite-L common-hub sampler
  -> n-bit terminal record
\`\`\`

このcandidateはQ2-1/Q2-3/Q2-4のterminal readerを一回のmulti-outcome samplingへ縮約する。現行M65/R181D/R192/R179を本draftでは退役させず、Q2-2のA端--B端逐次経路にも適用しない。後続promotionで依存切替を判定する。
