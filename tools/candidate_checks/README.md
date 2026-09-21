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
