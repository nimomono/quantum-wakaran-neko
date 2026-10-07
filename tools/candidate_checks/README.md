# candidate科学検算

ここには、研究中の強化目標・将来模型・まだ正本主張の必須依存に入っていない数学・数値検算を置く。

ファイル名は `verify_*.py` とする。

通常CIはこのディレクトリを実行しない。required検算と合わせて確認したい場合は、

```bash
python tools/run_physics_checks.py --include-candidate
```

を使う。

candidate結果が正本の必須依存になった時点で、十分に安定した検算を `tools/verify_*.py` へ移す。

candidateであっても本文や状態文書を文字列検査してはならず、数学・数値だけを検査する。

M64/R203A--R203Dはdraft-112で現行正本へ昇格し、対応する科学検算は `tools/verify_m64_*.py` のrequired checksへ移した。

## M65 strengthening history

draft-140でM65をtwo-result first-passage selectorへ簡素化し、旧R204B/R204C fixed-hub physical liftをactive strengtheningから退役した。旧M65専用candidate checks 3本は `notes/retired_verifiers/` へ移し、現行M65のrequired open-law検算は引き続き `tools/verify_m65_open_selector.py` で行う。

draft-141でM67/R211A--R211Cのfinite-Hamiltonian double-well selector liftを定理化し、R211A/R211Bの数学・数値回帰はtools/直下のrequired checksへ置く。このdirectoryにはfull finite-bath Q1 direct trajectoryなど、A2 strengtheningに属する未昇格検算だけを置く。phase-volume common identityはM66/R205のrequired checksで維持する。

### M66/R205--R206

draft-127でM66/R205--R206のfixed-goal coreをQ2-1/Q2-3/Q2-4主線へ昇格し、対応する有限次元・資源検算は `tools/verify_m66_common_phase_volume.py` と `tools/verify_r206_*.py` のrequired checksへ移した。

draft-129でR205C--R205Fの解析・generator回帰もrequired checksへ加える。このディレクトリへ今後置くM66系検算は、finite-bandwidth reservoir、full Brownian/chamber trajectory、具体spatial reservoirのcross-correlation、always-on coupling中のphase backreaction、具体Hamiltonian/回路liftなど、fixed-goal coreまたはcommon-parent定理に必須でないstrengtheningだけとする。

## M56/R194 alternative research line

- `verify_r194_brownian_spin_nelson.py`：M56/R194のBrownian-spin/Nelson接続を検査する代替研究線。
- M56/R194は現行fixed-goal主線の必須依存ではないためcandidate-onlyとし、通常required CIには含めない。

## M67/R208--R209 promotion history

draft-137/138ではM67/R208A--R209Cをcandidate-onlyとしてこのdirectoryで検査した。draft-139でM67をQ3 common physical parentへ昇格したため、対応する7本のverifierは tools/verify_*.py へ移動し通常required CIへ昇格した。R210A/R210Bもrequired verifierとして tools/ 直下に置く。draft-141のR211A/R211B Q1 selector-lift verifierも同じrequired層へ追加する。

## R212 thermal-sector promotion

draft-142でR212A--R212Cをrequired physical-parent bridgeへ昇格するため、parameter-window checkerは `tools/verify_r212b_rotor_parameter_window.py` へ移した。R212A/B/Cの解析・幾何・separation verifierもtools直下のrequired checksへ置く。このdirectoryにはR212BのMonte Carlo mixingやfull finite-bath direct trajectoryを置かず、supporting simulationsは `simulations/m67/` で管理する。


## R213 M67/NBL Q2 carrier candidate

- `verify_r213a_nbl_path_isometry.py`：reference-product isometryとfinite time-sampling rank境界。
- `verify_r213b_phase_tagged_gates.py`：H/T/CNOT phase-tagged path algebraとstate-vector一致。
- `verify_r213c_coherent_collector.py`：contraction/unitary dilationとcoherent collector Born action。
- `verify_r213d_resource_robustness.py`：signed analog bias obstructionとfinite-depth local-error scaling。
- R213A--R213DはM54/R186置換候補であり、draft-143ではcandidate-onlyとする。通常required physics CIへは含めず、fixed-goal直接依存・Q2-4達成判定を変更しない。

## R214 promotion記録

R214A--R214Bはdraft-145でrequiredへ昇格し、verifierは `tools/verify_r214a_dumbbell_partition.py` と `tools/verify_r214b_dumbbell_dynamic_bridge.py` へ移した。candidate treeには残さない。supporting reduced witnessは `simulations/m67/run_r214_dumbbell_q3_witness.py` に残るが、Q3-2-A2達成判定には使わない。


## R215 spatial-information candidate

- `verify_r215a_compatible_port_score.py`：projective compatibility、規格化continuity、Fokker--Planck score cancellation、Bayes $b_\pm=U\pm u$ を検査する。
- `verify_r215b_spatial_information_free_energy.py`：Fisher/free-energy identity、projective invariance、de Bruijn derivative、path-KL係数、translation Fisher曲率、node-safe regularization、functional derivativeを検査する。
- R215A/Bはcandidate strengtheningであり、通常required CIへ昇格しない。medium reversible closure、R215C/M68、Schrödinger再導出をcandidate検算だけから達成扱いしない。
