# 検算と品質確認

この文書はdraft-54の定理・モデル集約、再現計算、静的整合性、PDF生成、目視確認の記録である。検証日は2026-08-29。

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
python tools/verify_q2_shell_and_locality.py
python tools/verify_m48_full_cycle.py
python tools/verify_common_signal_m50.py
```

## draft-54理論監査

- 共通層では、有限unitary合成をR112へ、正確・摂動的な規格化第2モーメント輸送をR135へ、一般ray平均をR168へ、固定入力時刻instrumentをR170へ集約した。旧R89、R139、R167は独立結果として残していない。
- M37系列では、旧R83--R85、R87、R88の局所包絡、生成子誤差、有限時間誤差、作用変動、有限基底診断をR86へ集約した。Q3章はR135、R168、R170への特殊化だけを持つ。
- Q1系列では、制御、零傾斜占有振動、離調Rabi式、傾斜保持をR140へ、有限コントラストと結果別状態更新をR143へ集約した。旧R136、R141、R142は独立結果として残していない。
- Q2-1では、正確CNOT流、面積誤差、一般制御誤差、有限資源をR105へ集約した。旧R106は独立結果として残していない。
- Bell系列では、必要な非積構造をR147、準備とroutingをR153、局所応答・因子化・有限誤差・帰還をR155へ集約した。旧R146、R148、R149、R151、R154、R156、R166は独立結果として残していない。
- M43を独立モデルから外し、有限環境純位相緩和をR123へ吸収した。付録Mの独自内容だった条件付き局所因子化を付録Jへ移し、重複再掲を削除した。
- 現行原稿、状態表、検算コードから吸収済み結果ID、M43、旧付録名、旧検算器名を除いた。追跡情報は `notes/superseded_result_index.md`、変更履歴、Git履歴へ分離した。
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
| M35 canonical control | 29 |
| M47 action-shell origin | 35 |
| M47 collision thermodynamics | 29 |
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

- 定理系環境の開始・終了数は一致した。theorem 29、proposition 2、lemma 9、corollary 0、proof 34。
- 付録はA--Lの連番で、ファイル名、`@number`、章見出し、式参照を照合した。
- `README.md`、`PROJECT_STATUS.md`、`CHANGELOG.md`、`MANIFEST.md`、`CITATION.cff`、本文、付録をdraft-54へ同期した。
- 現行原稿と検算コードに吸収済み結果ID、M43、旧付録名、旧検算器名が残っていないことを確認した。
- `python -m py_compile tools/*.py` と `git diff --check` は成功した。

## PDF生成

- 出力: `paper.pdf`
- ページ数: 174
- 用紙: A4
- ファイルサイズ: 1,137,426 bytes
- SHA-256: `e9919f8b508fbff65341cd161be5d047a62e0371af47e4a53b45fc9f6f4054b8`
- `SOURCE_DATE_EPOCH` は2026-08-29 00:00:00 UTCである。
- 連続2回の生成で `paper.md`、`main.tex`、`paper.pdf` のバイナリが一致した。
- 未解決のcitation/reference、overfull/underfull box、fatal error、欠落文字はない。
- Latin Modern Mathの一部にbold fallback警告があるが、文字欠落や配置崩れはない。

## PDF目視確認

全174ページを72 dpiでレンダリングし、20ページずつ9枚のコンタクトシートで通覧した。さらに1、18、19、26、33、40、52、63、150、174ページを150 dpiで重点確認した。対象には表紙、共通R135・R168、R140、R143、R105、R155、R86、付録Jの条件付き局所因子化、参考文献末尾を含む。

クリッピング、重なり、意図しない空白ページ、黒塗り領域、数式の欠落、表の破綻、見出しの破綻は見つからなかった。表紙の版表示はdraft-54で、ヘッダー、フッター、ページ番号、章・付録の切替も正常である。

## CI

GitHub Actionsは次を確認する。

- 現行14本の検証スクリプトとPython構文検査
- 付録A--L、現行検算器、退役索引の存在と旧現行パスの不在
- R112、R135、R168、R170の共通層、R86、R140、R143、R105、R147、R153、R155の集約条件
- 固定長期目標の全達成判定語
- 現行原稿と検算コードにおける吸収済みモデルID・結果IDの不在
- `paper.md`、`main.tex`、`paper.pdf` の再生成差分
- 収録PDFと再生成PDFのテキスト層、ページ数、用紙寸法の一致
- LaTeXログに重大警告がないこと
- `git diff --check`
