# 検算と品質確認

この文書はdraft-53の理論統合、再現計算、静的整合性、PDF生成、目視確認の記録である。検証日は2026-08-29。

## 実行方法

リポジトリ直下で次を実行する。

```bash
python -m py_compile tools/*.py
for script in tools/verify_*.py; do python "$script"; done
python tools/build_paper.py
```

主要検算器を個別に実行するときは次を使う。

```bash
python tools/verify_m35_canonical_control.py
python tools/verify_q2_action_shell_integration.py
python tools/verify_m48_full_cycle.py
python tools/verify_m50_instrument_and_q3_handoff.py
```

## draft-53理論監査

- Born型枝生成をM50/R164へ一本化した。M35検算から作用区間頻度、Born一致、可変作用標本化を外し、有限unitary、比較器、安全域、SWAP、記録、逆計算だけを29項目で確認した。
- R170を固定入力時刻有限枝instrumentの唯一の共通定理とした。R143はM47固有の分析器と結果別状態更新、R154は2翼局所合成と条件付きBell応答だけを追加することを本文、付録、状態表で照合した。
- 旧R168と旧R169を一般ray平均定理R168へ統合した。階数1支持、固定作用高階数、可変作用radial補正、安全事象外の無反応を同じ完全結果分布で検算した。
- 旧R152はR161のM48特殊化、旧R150はR155証明内の統計距離補題へ吸収した。旧R165は退役し、M49中央4枝をR157/R164の直接特殊化として検算した。
- 現行原稿、状態表、検算コードから旧モデル名、退役結果ID、旧付録名を除いた。追跡情報は `notes/superseded_result_index.md`、研究メモ、変更履歴、Git履歴へ分離した。
- 固定長期目標と全ての達成判定語は変更していない。

## 数値・代数検証

`tools/verify_m50_instrument_and_q3_handoff.py` はR167、R168、R170に対応する31項目を確認した。主な数値は次の通り。

- R167 trace距離: `0.0003785985871776989`
- R167上界: `0.036319466370298495`
- R168可変作用反例のtrace距離: `0.24999999999999997`
- R170有限時間混合誤差: `1.6705734018351848e-13`
- R170混合予算: `0.003999999999999999`
- 例示誤差台帳: `epsilon_170 = 0.033`

確認数は各スクリプト内のスカラー検査または診断項目の数であり、独立な定理、証明、物理予測の数ではない。

| 検証 | 自動確認項目数 |
|---|---:|
| envelope reduction | 19 |
| M35 canonical control | 29 |
| M47 action-shell origin | 35 |
| M47 collision thermodynamics | 29 |
| M47 Hopf preparation | 20 |
| M47 Q1 instrument | 43 |
| M48 full cycle | 88 |
| M48 paired-Hopf | 56 |
| M49 joint-bath provider | 29 |
| M50 instrument and Q3 handoff | 31 |
| phase correlation | 15 |
| Q2-1 gate | 25 |
| Q2 action-shell integration | 33 |
| Q3 finite-graph phenomena | 36 |
| **合計** | **488** |

全項目が成功した。

## 静的整合性

- 定理系環境の開始・終了数は一致した。theorem 41、proposition 5、lemma 11、corollary 0、proof 36。
- 付録はA--Mの連番で、ファイル名、`@number`、章見出し、式参照を照合した。
- `README.md`、`PROJECT_STATUS.md`、`CHANGELOG.md`、`MANIFEST.md`、`CITATION.cff`、本文、付録をdraft-53へ同期した。
- 現行原稿と検算コードにR150、R152、R165、R169、および旧モデル固有IDが残っていないことを確認した。
- `python -m py_compile tools/*.py` と `git diff --check` は成功した。

## PDF生成

- 出力: `paper.pdf`
- ページ数: 176
- 用紙: A4
- ファイルサイズ: 1,143,218 bytes
- SHA-256: `a98c7baee4c439e2751fa7f8b17326f4b373cf5164432379e3117fed29e5d310`
- `SOURCE_DATE_EPOCH` は2026-08-29 00:00:00 UTCである。
- 連続2回の生成で `paper.md`、`main.tex`、`paper.pdf` のバイナリが一致した。
- 未解決のcitation/reference、overfull/underfull box、fatal error、欠落文字はない。
- Latin Modern Mathの一部にbold fallback警告があるが、文字欠落や配置崩れはない。

## PDF目視確認

全176ページを72 dpiでレンダリングし、20ページずつ9枚のコンタクトシートで通覧した。さらに1、2、18、31、49、63、64、155、174、176ページを150 dpiで重点確認した。対象には表紙、目次、共通R170、R143、R154、一般R168、付録KのR170証明、参考文献の先頭と末尾を含む。

クリッピング、重なり、意図しない空白ページ、黒塗り領域、数式の欠落、表の破綻、見出しの破綻は見つからなかった。表紙の版表示はdraft-53で、ヘッダー、フッター、ページ番号、章・付録の切替も正常である。

## CI

GitHub Actionsは次を確認する。

- 現行14本の検証スクリプトとPython構文検査
- 付録A--M、現行検算器、退役索引の存在と旧現行パスの不在
- M50/R170統合、R143・R154特殊化、一般R168、M35限定の静的条件
- 固定長期目標の全達成判定語
- 現行原稿と検算コードにおける旧モデルID・退役結果IDの不在
- `paper.md`、`main.tex`、`paper.pdf` の再生成差分
- 収録PDFと再生成PDFのテキスト層、ページ数、用紙寸法の一致
- LaTeXログに重大警告がないこと
- `git diff --check`
