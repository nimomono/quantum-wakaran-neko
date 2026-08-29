# 検算と品質確認

この文書はdraft-55の定理・モデル集約、再現計算、静的整合性、PDF生成、目視確認の記録である。検証日は2026-08-29。

## 実行方法

リポジトリ直下で次を実行する。

```bash
python -m py_compile tools/*.py
for script in tools/verify_*.py; do python "$script"; done
python tools/build_paper.py
```

主要検算器を個別に実行するときは次を使う。

```bash
python tools/verify_common_canonical_control.py
python tools/verify_common_collision_thermodynamics.py
python tools/verify_q2_shell_and_locality.py
python tools/verify_m48_full_cycle.py
python tools/verify_common_signal_m50.py
```

## draft-55理論監査

- R90、R97--R99をR112へ吸収し、有限unitary、時計、安全比較・無反応、正準SWAP、テンプレート交換、局所記録、逆計算を一つの共通定理にした。独立M35は現行モデル一覧から外した。
- R164、R161、R162の定理文は第2章だけに置き、Q1章は二枝特殊化、付録K・Lは証明だけにした。旧R163の数式と検算は無番号の粗視化経路熱力学系として保持した。
- R170へ全変動距離、事象確率、有界観測量の共通安定性系を追加し、R124、R125、R155へ適用した。
- Q2-1ではR104、R105をR112の4モード特殊化へ、R157、R158をR159の入力準備節・同期CNOT節へ吸収した。R159は準備、同期、benchmark統計の三節を持ち、R160はQ2-2受渡しへ分離した。
- R123--R125の定理文は第7章だけに置き、付録Gは証明専用にした。静的検査はR161、R162、R164、R123--R125の定理宣言が各1回であることを確認する。
- 現行結果は29件から20件へ集約した。現行原稿、状態表、検算コードから吸収済み9結果IDとM35を除き、追跡情報を `notes/superseded_result_index.md`、変更履歴、Git履歴へ分離した。
- 固定長期目標と全ての達成判定語は変更していない。

## 数値・代数検証

`tools/verify_common_signal_m50.py` はR135、R168、R170に対応する31項目を確認した。主な数値は次の通り。

- R135 trace距離: `0.0003785985871776989`
- R135上界: `0.036319466370298495`
- R168可変作用反例のtrace距離: `0.24999999999999997`
- R170有限時間混合誤差: `1.6705734018351848e-13`
- R170混合予算: `0.003999999999999999`
- 例示誤差台帳: `epsilon_170 = 0.033`

確認数は各スクリプト内のスカラー検査または診断項目の数であり、独立な定理、証明、物理予測の数ではない。

| 検証 | 自動確認項目数 |
|---|---:|
| envelope reduction | 19 |
| common canonical control | 29 |
| M47 action-shell origin | 35 |
| common collision thermodynamics | 29 |
| M47 Hopf preparation | 20 |
| M47 Q1 instrument | 43 |
| M48 full cycle | 88 |
| M48 paired-Hopf | 56 |
| M49 joint-bath provider | 29 |
| common signal and M50 | 31 |
| phase correlation | 15 |
| Q2-1 gate | 25 |
| Q2 shell and locality | 33 |
| Q3 finite-graph phenomena | 36 |
| **合計** | **488** |

全項目が成功した。

## 静的整合性

- 定理系環境の開始・終了数は一致した。theorem 20、proposition 2、lemma 2、corollary 0、proof 34。
- 付録はA--Lの連番で、ファイル名、`@number`、章見出し、式参照を照合した。
- `README.md`、`PROJECT_STATUS.md`、`CHANGELOG.md`、`MANIFEST.md`、`CITATION.cff`、本文、付録をdraft-55へ同期した。
- 現行原稿と検算コードに吸収済み結果ID、M35、旧付録名、旧検算器名が残っていないことを確認した。
- `python -m py_compile tools/*.py` と `git diff --check` は成功した。

## PDF生成

- 出力: `paper.pdf`
- ページ数: 173
- 用紙: A4
- ファイルサイズ: 1,126,573 bytes
- SHA-256: `e49b0f03a017f78ab26ea620e153f1fecf53c6a5e311a47bccbe25e6ad6425ef`
- `SOURCE_DATE_EPOCH` は2026-08-29 00:00:00 UTCである。
- 連続2回の生成で `paper.md`、`main.tex`、`paper.pdf` のバイナリが一致した。
- 未解決のcitation/reference、overfull/underfull box、fatal error、欠落文字はない。
- Latin Modern Mathの一部にbold fallback警告があるが、文字欠落や配置崩れはない。

## PDF目視確認

全173ページを72 dpiでレンダリングし、20ページずつ9枚のコンタクトシートで通覧した。さらに1、9、12、16、28、35、60、86、113、142、153、173ページを150 dpiで重点確認した。対象には表紙、共通R112・R161・R162・R164・R170、R140、R143、R159、R155、R86、付録G・K・L、参考文献末尾を含む。

クリッピング、重なり、意図しない空白ページ、黒塗り領域、数式の欠落、表の破綻、見出しの破綻は見つからなかった。表紙の版表示はdraft-55で、ヘッダー、フッター、ページ番号、章・付録の切替も正常である。

## CI

GitHub Actionsは次を確認する。

- 現行14本の検証スクリプトとPython構文検査
- 付録A--L、現行検算器、退役索引の存在と旧現行パスの不在
- R112、R135、R161、R162、R164、R168、R170の共通層、R86、R140、R143、R147、R153、R155、R159の集約条件
- 固定長期目標の全達成判定語
- 現行原稿と検算コードにおける吸収済みモデルID・結果IDの不在
- `paper.md`、`main.tex`、`paper.pdf` の再生成差分
- 収録PDFと再生成PDFのテキスト層、ページ数、用紙寸法の一致
- LaTeXログに重大警告がないこと
- `git diff --check`
