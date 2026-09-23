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

## M65 strengthening checks

M65本体の3状態open selectorはdraft-117で正本へ昇格し、required検算は `tools/verify_m65_open_selector.py` へ移す。

このディレクトリに残すM65検算は、正本に必須でない追加実現だけである。

- `verify_m65_phase_volume_partition.py` — R203B型phase-volume Jacobian。
- `verify_m65_matched_conductance.py` — fixed-hub capacity/conductanceからR204A rateを得る候補。
- `verify_m65_brownian_reduction.py` — fast-mixing micro-networkからcanonical 3-state lawへの数値witness。

Hamiltonian--Brownian liftやdirect trajectory witnessは強化課題であり、M65正本性やR191/R193退役の必要条件にはしない。

### M66/R205--R206

- \`verify_m66_common_phase_volume.py\` — R205A/R205BのJacobianとmatched capacity--conductance。
- \`verify_r206_multi_outcome_sampler.py\` — finite-\(L\) common-hub law、zero-weight、\(L\) 非依存mixing。
- \`verify_r206_uniform_passive_scaling.py\` — \(L=2^n\) passive scaling、regularization、aggregate fabrication error。
- \`verify_r206_q2_resource_scaling.py\` — Q2-4のsampling時間、passive internal resource、\(n\)-bit external readout。

これらはdraft-126時点ではcandidate checksであり、required physics checksではない。
