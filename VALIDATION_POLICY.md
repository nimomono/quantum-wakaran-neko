# 自動検算ポリシー

この文書は、GitHub Actionsで何をPRの失敗条件にし、何を品質警告として扱うかを簡潔に定める。

## PRを止める検査

- 数式・数値・確率恒等式・誤差上界の検算失敗
- 原稿構造、結果ID、状態表の自己矛盾
- 生成済み `paper.md` / `main.tex` / `paper.pdf` と再生成物の不同期
- 未解決citation/reference、欠落文字、LaTeX fatal error
- 明白な機械置換崩れなど、文章を機械的に破損している表記

## 警告として残す検査

- 標準表記から外れた旧英語説明語
- `Overfull \\hbox`
- `Underfull \\hbox`

警告は修正候補として残すが、それだけでは論文の科学的・構造的・再現性的妥当性を否定しない。

## 責務境界

- `verify_*.py` は数学・数値のみを見る。
- `check_source.py` は長期に安定した原稿・状態の構造契約だけを見る。
- `check_generated.py` は生成物同期と重大LaTeX異常だけを見る。
- `check_terminology.py` と `lint_typeset.py` は編集品質をlintする。
- GitHub Actionsはread-onlyとし、自動commit/pushを行わない。
- 原稿構造、数式・数値、論文生成は並列実行し、一つの失敗で他の結果を隠さない。

詳細な実装責務は `tools/README.md` を参照する。
