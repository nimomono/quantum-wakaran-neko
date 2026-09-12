# 検算・生成ツールの責務

このディレクトリでは、論文の生成と検算を次の4層に分ける。

1. **原稿・状態の構造検査** — `check_source.py`
2. **数式・数値検算** — `verify_*.py`
3. **生成物の再現性検査** — `build_paper.py` + `check_generated.py`
4. **文章・組版品質lint** — `check_terminology.py` + `lint_typeset.py`

目的は検算を弱めることではなく、PRを止めるべき科学的・構造的・再現性的な失敗と、後から直せる品質上の警告を区別することである。

## hard check

次はCI失敗条件とする。

- 章・付録構造の破綻、結果ID重複、状態表の自己矛盾
- 数式、数値、確率恒等式、誤差上界など `verify_*.py` が検出する失敗
- `paper.md` / `main.tex` / `paper.pdf` の再生成結果と収録生成物の不同期
- PDFページ数またはページ寸法の不同期
- LaTeXの未解決citation/reference、欠落文字、fatal error
- 明白な機械置換崩れなど、文章そのものが壊れたと判定できるもの

## quality lint

次は警告として表示するが、通常のCIを失敗させない。

- 標準表記から外れた旧英語説明語
- `Overfull \\hbox`
- `Underfull \\hbox`

用語lintを厳格に確認したい場合はローカルで次を使う。

```bash
python tools/check_terminology.py --strict
```

品質lintをwarningにすることは、その表記や組版を推奨する意味ではない。科学的・構造的な妥当性判定と編集上の仕上げを別の信号として扱うためである。

## `check_source.py`

`check_source.py` は章・付録の構造、結果ID宣言の一意性、状態文書の一般的な形式、CIのread-only境界を検査する。特定のR番号が特定の付録に存在すること、特定の日本語文がそのまま存在することなど、現在の理論スナップショットを固定する検査は置かない。

## `verify_*.py`

`verify_*.py` は数式、数値、確率恒等式、誤差上界などの数学的・数値的主張だけを検査する。本文、README、`PROJECT_STATUS.md`、節番号、ファイル配置の文字列契約を検査してはならない。

新しい物理結果の検算器を追加する場合は `verify_*.py` として追加すれば `run_physics_checks.py` が自動的に実行する。退役結果の専用検算器は現行検算集合から外す。通常、その変更のためにGitHub Actions自体を修正する必要はない。

## `build_paper.py` と `check_generated.py`

`build_paper.py` は `sections/*.md` から `paper.md`、`main.tex`、`paper.pdf` を生成するだけのツールとする。固定目標、達成状態、Q/M/R依存関係、特定定理名、退役IDなどのプロジェクト状態を内部へ複製しない。

`check_generated.py` は隔離ディレクトリへ再生成した生成物と収録生成物の同期、および重大なLaTeX異常だけを検査する。`Overfull` / `Underfull` はここでは失敗条件にしない。

通常生成は次で行う。

```bash
python tools/build_paper.py
```

CIや検算ではworking treeを書き換えないよう、隔離ディレクトリへ生成する。

```bash
python tools/build_paper.py --output-dir build/ci
python tools/check_generated.py build/ci
python tools/lint_typeset.py build/ci/latex/main.log
```

## `latex_log.py` と検算方針の自己検査

LaTeXログのhard errorと品質warningの分類は `latex_log.py` を正本とする。`check_generated.py` と `lint_typeset.py` は同じ分類器を使い、判定規則を二重管理しない。

`test_validation_policy.py` は人工ログを使って、`Overfull` / `Underfull` がwarningであり、未解決citation/reference・欠落文字・fatal errorがhard errorであることを回帰検査する。

## CIの不変条件

GitHub Actionsはread-onlyとし、検算中に `git commit`、`git push`、PR branchの自己書換えを行わない。大規模な移行スクリプトを使う場合も、PR作成前または通常の作業コミットとして完成状態へ適用し、CIはその完成状態を検査するだけにする。

`原稿構造`、`数式・数値`、`論文生成` の3ジョブは互いに独立に走らせる。一つの軽微な失敗によって別種の検算結果が隠れないようにする。
