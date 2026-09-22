# 検算・生成ツールの責務

このディレクトリでは、検算を「現在の理論スナップショットを固定する仕組み」ではなく、長期に安定した不変条件を確認する仕組みとして管理する。正本のルールは `VALIDATION_POLICY.md` に置く。

## 構成

1. **原稿・状態の構造検査** — `check_source.py`
2. **履歴・依存の横断整合検査** — `check_project_consistency.py`
3. **required科学検算** — `verify_*.py`
4. **candidate科学検算** — `candidate_checks/verify_*.py`
5. **生成物同期** — `build_paper.py` + `check_generated.py`
6. **LaTeX semantic検査** — `check_latex_semantics.py`
7. **文章・組版品質lint** — `check_terminology.py` + `lint_typeset.py`
8. **PR固有の移行検査** — `migrations/`

目的は検算を弱めることではなく、科学的・構造的・再現性的な不変条件と、研究中の候補、特定PRだけの移行確認、編集上の仕上げを分離することである。

## hard check

通常CIを止めるのは次である。

- 章・付録構造の破綻、結果ID重複、状態表の自己矛盾
- active結果と現行結果表の不一致、固定目標の直接根拠から非active結果への参照、active/retired IDの交差、履歴メモ参照先の欠落
- `tools/verify_*.py` が検出するrequired数学・数値検算の失敗
- `paper.md` / `main.tex` / `paper.pdf` の再生成結果と収録生成物の不同期
- PDFページ数またはページ寸法の不同期
- LaTeXの未解決citation/reference、欠落文字、fatal error
- 明白な機械置換崩れ

## quality lint

次は警告として表示するが、通常CIを失敗させない。

- 標準表記から外れた旧英語説明語
- `Overfull \\hbox`
- `Underfull \\hbox`

用語lintを厳格に確認したい場合は

```bash
python tools/check_terminology.py --strict
```

を使う。

## `check_source.py`

`check_source.py` は長期に安定した構造契約だけを見る。

許される検査の例:

- `sections/*.md` がparseできる
- 必須metadataがある
- active結果IDが一意である
- status値が許可集合に入る
- 同じQに矛盾するstatusがない
- 固定目標表と強化目標表のQ ID集合が一致する
- CIがread-onlyである

置いてはならない検査の例:

- 特定のM/R/Q番号が特定ファイルにある
- 特定の結果番号が証拠欄に必須である
- 特定の日本語文が完全一致する
- 特定sectionファイル名に現在の模型がある
- 現在の達成状態そのものを固定する

「モデル番号、結果番号、節名、文章表現を変更しても真か」を判定基準とする。

## `check_project_consistency.py`

このcheckerは、現在の理論内容そのものではなく、正本間の集合・参照関係を検査する。

- `sections/*.md` で宣言されたactive結果ID集合と `PROJECT_STATUS.md` の現行結果表が一致する
- 固定目標の「現在地」表が直接根拠として参照する結果IDがactive結果に含まれる
- `notes/superseded_result_index.md` の退役結果IDとactive結果IDが交差しない
- 退役索引と `notes/README.md` から参照するMarkdownメモが実在する

個別の結果番号、模型番号、固定目標ID、特定sectionパスをcheckerへ列挙しない。理論移行時に特定IDの除去を確認する仕事は従来どおり `migrations/` に置く。

## required `verify_*.py`

`tools/verify_*.py` は数式、数値、確率恒等式、誤差上界、parameter windowなど数学的・数値的主張だけを検査する。本文、README、`PROJECT_STATUS.md`、節番号、ファイル配置の文字列契約を読んではならない。

新しいrequired verifierは `tools/verify_*.py` として追加すれば `run_physics_checks.py` が自動実行する。通常、そのためにGitHub Actionsを変更する必要はない。

可能ならファイル名・関数名も結果番号ではなく数学的構造に寄せる。既存verifierの改名は別途整理してよいが、番号付き名称を理由に直ちに失敗とはしない。

## candidate科学検算

まだ正本主張の必須依存でない強化・研究候補は `tools/candidate_checks/verify_*.py` に置く。

通常CIでは実行しない。必要なときは

```bash
python tools/run_physics_checks.py --include-candidate
```

でrequiredと合わせて実行する。

candidateをrequiredへ昇格するときは、まずその主張が正本の必須依存になったことを確認してから `tools/verify_*.py` へ移す。

## `run_physics_checks.py`

required verifierは全件を最後まで実行する。一つの失敗で後続を隠さず、最後にPASS/FAIL一覧をまとめる。

candidateを明示的に含めた場合も同様に全件を実行する。

## `build_paper.py` と `check_generated.py`

`build_paper.py` は `sections/*.md` から `paper.md`、`main.tex`、`paper.pdf` を生成するだけのツールとする。固定目標、達成状態、Q/M/R依存関係、特定定理名、退役IDなどのプロジェクト状態を内部へ複製しない。

`check_generated.py` は隔離ディレクトリへ再生成した生成物と収録生成物の同期だけを検査する。LaTeX semantic errorは扱わない。

通常生成:

```bash
python tools/build_paper.py
```

CI:

```bash
python tools/build_paper.py --output-dir build/ci
python tools/check_generated.py build/ci
python tools/check_latex_semantics.py build/ci/latex/main.log
python tools/lint_typeset.py build/ci/latex/main.log
```

## `check_latex_semantics.py` と `lint_typeset.py`

LaTeXログの分類は `latex_log.py` を正本とする。

`check_latex_semantics.py` は未解決citation/reference、欠落文字、fatal error等をhard errorとして扱い、検出した全件を表示する。

`lint_typeset.py` はOverfull/Underfull等をwarningとして扱う。

これにより、生成物同期が失敗してもLaTeX semantic errorの診断を隠さない。

## `migrations/`

特定PRでだけ必要な旧語・旧依存・旧模型の除去確認は `migrations/` に置く。

- 通常CIから呼ばない
- 恒久構造契約へ昇格させない
- 完了後は削除してよい
- 残す場合も履歴・手順として扱う

詳細は `migrations/README.md` を参照する。

## 検算方針の自己検査

`test_validation_policy.py` はLaTeX分類だけでなく、責務境界そのものを回帰検査する。

特に、

- `check_source.py` と `check_project_consistency.py` に具体的なM/R/Q番号や特定sectionパスが再流入していない
- `check_project_consistency.py` が通常CIの構造jobから実行されている
- `verify_*.py` が原稿文書を読んでいない
- migration checkが通常workflowから呼ばれていない
- physics runnerが最初のfailureでbreakしない
- artifact syncとLaTeX semantic検査が再結合されていない

ことを確認する。

## CIの不変条件

GitHub Actionsはread-onlyとし、検算中に `git commit`、`git push`、PR branchの自己書換えを行わない。

`原稿構造`、`数式・数値`、`論文生成` の3ジョブは独立に走らせる。論文生成job内でも、buildが成功した後はartifact sync、LaTeX semantic、typeset lintを互いの失敗で隠さない。
