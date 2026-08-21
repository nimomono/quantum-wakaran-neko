# 図の管理

本文または付録で使う図を置く。図を追加するときは、元データ、生成処理、参照元の章を追跡できるようにする。

## M45開放自己組織化準臨界準備

- `m45_open_trap_diagnostics.png`：直接Langevin軌道の局所エネルギー、準備領域のエネルギー分布、捕捉位相体積比。`simulations/m45_open_quasicritical/run.py` が生成し、第8.13節と付録HのR127・R128を補助する。
- `m45_conditional_ground_comparison.png`：調和型・二重井戸型ポテンシャルについて、量子基底密度と3つの橋を入力した条件付きM45作用素の主固有密度を比較する。同じスクリプトが生成し、R129の条件付き作用素監査を補助する。直接Langevin軌道の基底状態比較ではない。

図の元データは `simulations/m45_open_quasicritical/reference/curves.csv`、集約指標は同フォルダーのJSONに保存する。
