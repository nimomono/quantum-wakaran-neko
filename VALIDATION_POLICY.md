# 自動検算ポリシー

この文書は、GitHub Actionsで何を恒久的なPR失敗条件にし、何を品質警告または一時的な移行検査として扱うかを定める。

## 基本原則

恒久検算へ追加してよいのは、理論の実装番号や文章表現を変更しても維持される**不変条件**だけとする。

新しい検算を追加するときは、必ず次を問う。

> モデル番号、結果番号、節名、ファイル名、文章表現を変更しても、この検査条件は真であるべきか。

YESなら恒久CI候補である。NOなら恒久CIへ入れず、移行検査、候補検算、または品質lintとして扱う。

検算を厳しくすることと、現在の理論スナップショットを固定することを区別する。前者は維持し、後者は避ける。

## 5つの検算層

1. **構造検査** — 原稿・状態表・結果宣言が機械的に整合しているか。
2. **科学検算** — 数式、数値、確率恒等式、誤差上界、parameter windowが成立するか。
3. **生成・組版検査** — 収録生成物が再生成可能で、重大なLaTeX異常がないか。
4. **品質lint** — 用語、Overfull/Underfullなど、科学的妥当性とは独立した編集品質。
5. **移行検査** — 特定PRで旧模型・旧依存・旧語を除去できたか。一時物であり恒久CIへ入れない。

## PRを止める恒久検査

- 章・付録構造の破綻、結果ID重複、状態表の自己矛盾
- 数式・数値・確率恒等式・誤差上界などrequired科学検算の失敗
- 生成済み `paper.md` / `main.tex` / `paper.pdf` と再生成物の不同期
- 未解決citation/reference、欠落文字、LaTeX fatal error
- 明白な機械置換崩れなど、文章が機械的に破損している表記

## warningまたは手動検査

- 標準表記から外れた旧英語説明語
- `Overfull \\hbox`
- `Underfull \\hbox`
- 研究中・強化目標・将来候補に対するcandidate科学検算
- 特定PRだけに必要な旧語・旧依存の除去確認

## 責務境界

- `check_source.py` はsyntax/schema/referential integrityなど長期不変の構造契約だけを見る。
- `verify_*.py` は数学・数値だけを見る。本文や状態文書を読まない。
- `candidate_checks/verify_*.py` は研究中・強化候補の数学・数値検算を置く。通常CIのhard checkには含めない。
- `check_generated.py` は生成物同期だけを見る。
- `check_latex_semantics.py` はLaTeXの重大異常だけを見る。
- `check_terminology.py` と `lint_typeset.py` は編集品質をlintする。
- `migrations/` は特定PRの移行確認専用で、通常CIから呼ばない。
- GitHub Actionsはread-onlyとし、自動commit/pushを行わない。

## 検算作成ルール

1. 恒久検算へモデル番号、結果番号、特定Q番号、節番号、特定sectionファイル名、本文の完全一致文を埋め込まない。
2. 理論移行の完全性確認は `tools/migrations/` に置き、通常CIへ恒久登録しない。
3. `check_source.py` は現在の証明経路や採用模型を判定しない。
4. `verify_*.py` は原稿・README・状態文書・節配置を読まない。
5. 科学検算の単位は、可能な限り結果番号ではなく数学的構造にする。
6. 部分達成・未監査・研究中の結果を不用意にrequired hard checkへ昇格しない。
7. parameter witnessは、可能なら単一点のmagic numberではなく許容領域の非空性または十分なmarginを検査する。
8. 独立な検算は最初の失敗で停止せず、可能な限り全件を実行して失敗一覧を返す。
9. 生成物同期、LaTeX semantic error、typeset lintは別々に報告する。
10. 新しい恒久ruleには、その責務境界が再び破られないための自己検査を追加する。
11. CIはread-onlyとし、移行スクリプトによるbranch自己書換えを行わない。
12. warningをhardへ昇格するときは、このポリシーに理由を明記する。

## required と candidate

現在の論文主張・固定達成が依存する数学検算は `tools/verify_*.py` に置き、通常CIでhard checkする。

研究中の強化、将来模型、まだ正本主張の依存に入っていない検算は `tools/candidate_checks/verify_*.py` に置く。candidate検算は手動で

```bash
python tools/run_physics_checks.py --include-candidate
```

として実行できるが、通常CIを赤くする理由にはしない。

## 移行検査

特定PRで「旧模型名が残っていない」「旧依存が復活していない」などを確認したい場合は `tools/migrations/` に一時検査を置く。

移行検査は完成状態を作るための作業ツールであり、恒久的な理論契約ではない。通常CIから呼ばず、原則として対象移行が完了したら削除する。残す場合も履歴・手順書としてのみ残す。

## 診断方針

厳格さを下げる代わりに失敗理由を見やすくする。

- physics runnerは全required verifierを最後まで実行し、失敗一覧をまとめる。
- artifact syncとLaTeX semantic errorを別検査として両方表示する。
- LaTeX hard errorは最初の1件だけでなく全件を表示する。
- quality warningはhard errorと別チャネルで表示する。

詳細な実装責務は `tools/README.md` を参照する。
