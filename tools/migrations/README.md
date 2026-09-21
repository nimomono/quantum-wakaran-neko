# PR固有の移行検査

このディレクトリは、特定の理論再編・名称変更・依存関係変更を安全に完了させるための一時検査を置く。

例:

- 旧模型名が現行説明へ残っていないか
- 退役した結果IDが現行の必須依存へ再混入していないか
- あるPRで置換対象にした旧文言が残っていないか
- 大規模移行で必要なファイル群が新体系へ同期したか

これらは重要な作業検査だが、長期に安定した理論不変条件ではない。

## ルール

- `.github/workflows/verify.yml` から呼ばない。
- `check_source.py` へ移植しない。
- 特定のM/R/Q番号、section名、文章断片を使ってよい。
- 対象PRの完成状態を作るために手動実行する。
- 移行完了後は削除してよい。
- 残す場合も履歴・再移行手順として扱い、恒久CIのhard contractにはしない。

恒久CIへ昇格させたくなった場合は、まずその検査を「番号や文章表現を変えても真である不変条件」に一般化できるかを確認する。


## draft-117 M65 open selector昇格

`check_draft117_m65_open_selector.py` は、M65がcandidate文言からcanonical open selectorへ同期され、R181Dがbinary selector contractへ一般化され、M65 core検算とHamiltonian/Brownian candidate検算の境界が正しく移行したことを確認する。PR固有の移行検査であり恒久CIへは入れない。
