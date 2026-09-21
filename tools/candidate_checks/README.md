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

M64 promotion bridge checks:

- `verify_m64_reservoir_partition.py`: phase-volume partition identity.
- `verify_m64_preparation_tracking.py`: initial preparation and finite-time mean-flow tracking.
- `verify_m64_overdamped_reduction.py`: canonical regularized overdamped flux identity.
- `verify_m64_r161_finite_volume.py`: 1D regularized finite-volume R161 convergence.
- `verify_m64_graph_r161.py`: general finite-graph R161 positivity/current matching and R125 regularized distances.

These remain candidate checks until the separate M64 promotion audit; they do not by themselves establish A2.
