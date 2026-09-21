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


## M65 phase-volume projective instrument

draft-114ではR191/R193をまだ置換しないpromotion-ready candidateとして、M65/R204A--R204Fの6検算を置く。

- `verify_m65_phase_volume_partition.py`
- `verify_m65_matched_conductance.py`
- `verify_m65_brownian_reduction.py`
- `verify_m65_three_state_born.py`
- `verify_m65_projector_handoff.py`
- `verify_m65_resource_scaling.py`

R204Cのfull Hamiltonian--Brownian chamber縮約とdirect trajectory witnessがpromotion gateであり、candidate検算だけでR191/R193を退役させない。
