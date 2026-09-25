# 理論系譜と現行正本への入口

このメモは、置換済み研究メモに残る「当時の現行」「次の置換先」と、現在の正本を混同しないための入口である。個別メモの本文は、その版で何を採用していたかを追跡できるよう原則として歴史的表現を保持する。**現在の採用状態そのものは `PROJECT_STATUS.md` を正本**とし、退役結果のID・旧用途・保存先は `superseded_result_index.md` を正本とする。

## 現行の統一構造

現行正本は、M54の共通signal・状態層とM66/R205の共通thermal-reservoir層を分け、その上へ用途別のM64、M65、R206、R207を接続する構造として読む。

```text
M54 signal/state layer
  ↑ M37 signal implementation

M66 / R205 reservoir layer
  ├─ R206A--R206D : Q2 terminal multi-outcome specialization
  ├─ R206E        : Q2-4 root preparation / refresh
  ├─ R205C ↔ M64 : shared reservoir principle
  ├─ R205D ↔ M65 : strengthening physical lift
  └─ R205A/E/F → R207 : Q2-2 fixed-goal Bell specialization
```

M66が共通化するのはreservoir sectorであり、M64全体やM65 canonical lawを置換しない。M0はさらに強いjoint device/process統合目標であり、この2つの共通層を持つだけでは達成しない。

## 現行の主要因果鎖

### Q1の逐次測定

現行の逐次二結果測定は、保持済み射影作用をM65へ渡し、M65/R204D--R204Fで有限時間の結果形成とrecordを行い、R181Dで対応する非規格化射影成分を同じ試行の次段へ渡す。draft-135以後、このfixed-goal経路を使うのはQ1である。Q2-2はM66/R205--R207へ一本化した。

```text
finite canonical signal
  -> projective actions
  -> M65 / R204D--R204F
  -> finite record
  -> R181D projector router
```

R179はfull-cycle reset/renewalの一般部品として別に保持する。

主要な旧binary測定経路は概略として

```text
M35 long-time sampler
  -> M50 / R164 / R170 action-shell route
  -> R191 / R193 Brownian-macrospin route
  -> M65 / R204 canonical open selector
```

と置換された。途中の模型・結果は反証されたという意味ではなく、現行fixed-goal因果鎖での責務をより短い経路へ置換したものである。

### Q2-1/Q2-3/Q2-4のterminal readout

draft-127以後、Q2-1/Q2-3/Q2-4のterminal readoutはM66/R205 common-reservoir interface上のR206A--R206Dへ一本化する。

```text
terminal coherent signal
  -> local actions |Z_y|^2
  -> M66 / R205A--R205F common thermal-reservoir layer
  -> R206A--R206D finite-L common-hub sampler
  -> joint terminal result
```

Q2-4ではその前にR206E uniform root preparationを置く。

```text
R206E root preparation
  -> R181C gate sequence
  -> R206D L=2^n terminal sample
  -> n-bit record
```

この置換によりQ2-1/Q2-3/Q2-4のterminal R181D tree、非終端branchのR192作用安定化、Q2-4のR179 direct reset依存を外す。R192は責務消滅として退役し、M65/R181D/R179は上記の別責務でactiveのまま残す。

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

Q2の永続register・gateはM54/R181B--R181Cへ整理される。Q2-1/Q2-3/Q2-4の末端readoutはR206A--R206D、Q2-4準備はR206Eが担う。

Q2-2はM66/R205A・R205E・R205FからR207A--R207Cへ進むprojection phase-volume二端模型を現行fixed-goal主線とする。setting-dependent source preparation、passive separation、local outcome/recordから一般Bloch方向のsinglet共同統計を閉じ、R207DをBell-local controlとする。

Bell経路の主要置換履歴は概略として

```text
M41 common-cause Bell cycle
  -> M48 paired-Hopf Bell protocol
  -> R180A/R180C sequential A-to-B witness
  -> R207 projection phase-volume mainline
```

である。draft-135でR180A/R180Cはactive paperから退役し、最終Theory Aは `superseded_r180_sequential_q2_2_witness.md` に保存する。M65/R181DはQ1責務でactiveのまま残る。

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
- Q2旧逐次terminal tree: `superseded_q2_sequential_terminal_readout.md`、`superseded_r192_radial_stabilizer.md`
- Q3旧rate latch: `superseded_r184_m37_rate_latch.md`
- Q3旧Poisson存在論: `superseded_q3_poisson_microphysics.md`
- Q3旧連続粒子模型: `superseded_m42_continuous_particle_position.md`
- Q3旧Hamiltonian実装群: M57/M59/M60/M61関連のsuperseded notesとGit履歴
- Q2旧register/Bell: `superseded_m49_joint_bath_cnot_provider.md`、`superseded_m52_path_only_design.md`、`superseded_independent_m48_bell_protocol.md`、`superseded_r180_sequential_q2_2_witness.md`

このメモは理論結果を追加せず、現行正本と歴史記録のナビゲーションだけを与える。

## draft-127で昇格したM66/R205--R206 branch

draft-126でreplacement candidateとして追加したM66/R205--R206は、draft-127でQ2-1/Q2-3/Q2-4のterminal readout正本へ昇格した。旧M65/R181D逐次terminal treeの履歴と責務分離は `superseded_q2_sequential_terminal_readout.md`、R192の完全保存は `superseded_r192_radial_stabilizer.md` を参照する。


## draft-129で拡張したM66/R205 parent

draft-129ではM66をQ2 readerそのものからcommon thermal-reservoir parentへ一般化した。R205CはM64/R203Bのpartition/free-energyとmean-flow分離、R205DはM65/R204Bのfixed-hub実現を共通原理へ埋め込む。R205Eはthermal Gibbs sampler、R205Fはpassive separationの一般generator結果である。Q2 terminal fixed-goal主線はR206、Q3 particle/Nelson主線はM64、Q1/Q2-2 binary主線はM65であり、Q2-2-S/R207はこのdraftでは導入しない。

## draft-130で追加したR207 Q2-2-S candidate

Q2-2 fixed-goalの現行主線は引き続きR180C--M65/R181Dである。R207A--R207DはQ2-2-S専用の別候補として、M66/R205Eのcommon preparationからR205Fのpassive separationへ進み、分離後のlocal responseとsource--setting measurement dependenceを監査する。R207Dはmeasurement-independent local controlを与える。finite-speed spatial reservoirが未閉包なのでQ2-2-S状態は未監査のままとする。



## draft-131で同期したQ2-2-S管理

draft-131では新しい理論結果を追加せず、第5章のR180C fixed-goal witnessとR207 strengthening candidateを明示的に分離した。S0--S4現在地は `ENHANCEMENT_TARGETS.md` を正本へ一本化し、S2の主要blockerをfinite-speed spatial reservoirとsetting確定後のtiming closureへ統一した。Q2-2 fixed-goal達成、Q2-2-S未監査、R207A--R207Dのcandidate分類は変更していない。


## draft-134で昇格したR207 projection phase-volume Q2-2主線

draft-130--draft-133のR207は4-setting Gibbs witnessを持つQ2-2-S candidateだった。draft-134ではprojection phase volumeとnear-contact isotropic lockへ模型を改訂した。R207Bは一般Bloch方向でfinite-lock余弦則を与え、R207CはM66/R205E preparation、R205F passive separation、local latch/recordを一試行へ接続する。このためR207A--R207CをQ2-2 fixed-goalの直接根拠へ昇格し、R180A/R180Cはactive alternate witnessへ下げた。R180系の完全退役は次の独立PRへ分離する。

旧4-setting Gibbs candidateは `superseded_r207_four_setting_gibbs_candidate.md` とGit履歴へ保存する。Q2-2-SはR207 fixed-goal baselineへfinite-speed causal isolationを追加する強化として再整理し、公式状態は未監査のまま維持する。


## draft-134--135のR207昇格とR180退役

draft-134でR207A--R207CをQ2-2 fixed-goalの直接根拠へ昇格し、R180A/R180Cをalternate witnessへ下げた。draft-135ではその移行を完了し、R180A/R180C、専用付録D、専用required verifierをactive treeから退役した。Q2-2達成、R207理論、Q2-2-S未監査は変更していない。


## draft-136で退役したQ2-2-S

draft-130--draft-131で、当時のQ2-2 fixed-goalとは別のR207空間分離候補を管理するためQ2-2-Sを導入した。draft-134でR207A--R207CがQ2-2 fixed-goalへ昇格し、draft-135でR180A/R180Cが退役した結果、Q2-2-Sは同じR207模型へfinite-speed causal-isolation条件を追加するだけの管理IDとなった。

draft-136ではfinite-speed spatial realizationを正式目標として要求しない方針へ変更し、Q2-2-Sを退役した。Q2-2はR207A--R207CとR207Dだけで管理し、Bell監査はmeasurement independence不成立を明示する。旧S0--S4と専用candidate checkerの位置づけは `superseded_q2_2_s_spatial_strengthening.md` に保存する。

## draft-137で追加したM67/R208 candidate branch

現行Q3正本は引き続き

```text
M37 / R86
  -> M64 / R203A--R203D
  -> R161 / R185
```

である。M67/R208はこの上に

```text
M67 / R208A--R208D
  - - > M64 / R203 effective target
```

というcandidate branchを追加する。M57--M63の旧single-field探索と異なり、M67は一つのstructured reservoir内でcoherent sectorとthermal sectorの正準分解を許し、別実体をclassical markerだけに限定する。draft-137ではpromotion/retirementを行わない。
