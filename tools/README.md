# 検算・生成ツールの責務

このディレクトリでは、論文の生成と検算を次の3層に分ける。

1. **原稿構造検査** — `check_*.py`
2. **数式・数値検算** — `verify_*.py`
3. **論文生成** — `build_paper.py`

## `check_*.py`

`check_source.py` は章・付録の構造、結果ID宣言の一意性、状態文書の一般的な形式、CIのread-only境界を検査する。特定のR番号が特定の付録に存在すること、特定の日本語文がそのまま存在することなど、現在の理論スナップショットを固定する検査は置かない。

`check_terminology.py` は文章規約だけを検査する。数学・数値検算には含めない。

`check_generated.py` は隔離ディレクトリへ再生成した `paper.md`、`main.tex`、`paper.pdf` と収録生成物の同期、およびLaTeXログを検査する。

## `verify_*.py`

`verify_*.py` は数式、数値、確率恒等式、誤差上界などの数学的・数値的主張だけを検査する。本文、README、`PROJECT_STATUS.md`、節番号、ファイル配置の文字列契約を検査してはならない。

新しい物理結果の検算器を追加する場合は `verify_*.py` として追加すれば `run_physics_checks.py` が自動的に実行する。退役結果の専用検算器は現行検算集合から外す。通常、その変更のためにGitHub Actions自体を修正する必要はない。

## `build_paper.py`

`build_paper.py` は `sections/*.md` から `paper.md`、`main.tex`、`paper.pdf` を生成するだけのツールとする。固定目標、達成状態、Q/M/R依存関係、特定定理名、退役IDなどのプロジェクト状態を内部へ複製しない。

通常生成は次で行う。

```bash
python tools/build_paper.py
```

CIや検算ではworking treeを書き換えないよう、隔離ディレクトリへ生成する。

```bash
python tools/build_paper.py --output-dir build/ci
python tools/check_generated.py build/ci
```

## CIの不変条件

GitHub Actionsはread-onlyとし、検算中に `git commit`、`git push`、PR branchの自己書換えを行わない。大規模な移行スクリプトを使う場合も、PR作成前または通常の作業コミットとして完成状態へ適用し、CIはその完成状態を検査するだけにする。
