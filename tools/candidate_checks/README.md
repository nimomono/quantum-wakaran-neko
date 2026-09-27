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

現行M65のfinite-Hamiltonian physical liftはこのdirectoryには置かず、後続M67/R211の理論・検算として扱う。phase-volume common identityはM66/R205のrequired checksで維持する。

### M66/R205--R206

draft-127でM66/R205--R206のfixed-goal coreをQ2-1/Q2-3/Q2-4主線へ昇格し、対応する有限次元・資源検算は `tools/verify_m66_common_phase_volume.py` と `tools/verify_r206_*.py` のrequired checksへ移した。

draft-129でR205C--R205Fの解析・generator回帰もrequired checksへ加える。このディレクトリへ今後置くM66系検算は、finite-bandwidth reservoir、full Brownian/chamber trajectory、具体spatial reservoirのcross-correlation、always-on coupling中のphase backreaction、具体Hamiltonian/回路liftなど、fixed-goal coreまたはcommon-parent定理に必須でないstrengtheningだけとする。

## M56/R194 alternative research line

- `verify_r194_brownian_spin_nelson.py`：M56/R194のBrownian-spin/Nelson接続を検査する代替研究線。
- M56/R194は現行fixed-goal主線の必須依存ではないためcandidate-onlyとし、通常required CIには含めない。

## M67/R208--R209 promotion history

draft-137/138ではM67/R208A--R209Cをcandidate-onlyとしてこのdirectoryで検査した。draft-139でM67をQ3 common physical parentへ昇格したため、対応する7本のverifierは tools/verify_*.py へ移動し通常required CIへ昇格した。R210A/R210Bもrequired verifierとして tools/ 直下に置く。

