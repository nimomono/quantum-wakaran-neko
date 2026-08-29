# 検算と品質確認

この文書はdraft-56の固定目標改訂、凍結課題の再開、再現計算、静的整合性、PDF生成、目視確認の記録である。検証日は2026-08-29。

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

## draft-56方針監査

- Q2-3の固定目標を「多項式資源による量子ゲート型計算機」へ変更した。固定有限普遍ゲート集合から一様に生成される$n$量子ビット・深さ$d$の回路族、計算基底入力、最終計算基底出力分布、全変動距離$\epsilon$を対象とする。
- Q2-3の資源台帳は自由度、相互作用、補助装置、program、準備・実行・混合・測定・記録・reset時間、エネルギー・作用・動的範囲、制御・初期化・読出し精度、fresh cell、永久記録、失敗確率、期待試行回数を個別に$\operatorname{poly}(n,d,1/\epsilon)$で抑えることを要求する。
- 指数長の表のhard-code、$2^n$個のモード・枝、指数時間・並列度・エネルギー・作用、指数的に細かい精度、指数的に小さい成功確率、成功試行だけの再規格化によって指数コストを隠すことを除外した。
- M49/M50の直接モード一般化は$L=2^n$を要するため、現行のQ2-3候補としては資源判定に失敗する。ただし、これは有限古典Hamiltonian方式一般に対するno-go定理ではない。
- Q1-4とQ3-2の凍結を解除し、Q2-3と合わせて全て「未達」の研究課題として再開した。Q1-4は同一零傾斜Rabi対照と反復R143/R170測定によるZeno抑制余裕、Q3-2は閉路巻数、節を介した位相すべり、細分化安定性、非整数seamのエネルギー発散を検証線とする。
- 今回の改訂は固定目標、達成判定、検証線、文書構成の変更であり、新しい定理、モデル、数値結果を追加していない。

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
- `README.md`、`PROJECT_STATUS.md`、`PROJECT_STANCE.md`、`PROJECT_GUIDE.md`、`CHANGELOG.md`、`MANIFEST.md`、`CITATION.cff`、本文、付録をdraft-56へ同期した。
- Q1-4、Q2-3、Q3-2の達成判定が全て「未達」であること、Q2-3の固定名、全変動距離、期待試行回数、成功試行だけを再規格化しない条件が一致することを確認した。
- 現行方針文書と本文に、三課題を「凍結中」と扱う旧記述が残っていないことを確認した。
- 現行原稿と検算コードに吸収済み結果ID、M35、旧付録名、旧検算器名が残っていないことを確認した。
- `python -m py_compile tools/*.py` と `git diff --check` は成功した。

## PDF生成

- 出力: `paper.pdf`
- ページ数: 174
- 用紙: A4
- ファイルサイズ: 1,136,230 bytes
- SHA-256: `4ceacaab0d231621c223db77eec8671a7a2cebef8c217763f97897a89288bc8f`
- `SOURCE_DATE_EPOCH` は2026-08-29 00:00:00 UTCである。
- 連続2回の生成で `paper.md`、`main.tex`、`paper.pdf` のバイナリが一致した。
- 未解決のcitation/reference、overfull/underfull box、fatal error、欠落文字はない。
- Latin Modern Mathの一部にbold fallback警告があるが、文字欠落や配置崩れはない。

## PDF目視確認

全174ページを72 dpiでレンダリングし、20ページずつ9枚のコンタクトシートで通覧した。さらに1、14、35、36、70、79、80、83、174ページを150 dpiで重点確認した。対象には表紙、達成状況表、Q1-4の再開課題、Q3-2の再開課題、Q2-3の多項式資源判定、未完成目標の優先順位、結論、参考文献末尾を含む。

クリッピング、重なり、意図しない空白ページ、黒塗り領域、数式の欠落、表の破綻、見出しの破綻は見つからなかった。表紙の版表示はdraft-56で、ヘッダー、フッター、ページ番号、章・付録の切替も正常である。

## CI

GitHub Actionsは次を確認する。

- 現行14本の検証スクリプトとPython構文検査
- 付録A--L、現行検算器、退役索引の存在と旧現行パスの不在
- R112、R135、R161、R162、R164、R168、R170の共通層、R86、R140、R143、R147、R153、R155、R159の集約条件
- 固定長期目標の全達成判定語
- Q2-3の固定名、多項式資源台帳、指数コスト除外条件、成功試行だけを再規格化しない条件
- Q1-4、Q2-3、Q3-2を凍結中と扱う旧記述の不在と、再開後の「未達」判定
- 現行原稿と検算コードにおける吸収済みモデルID・結果IDの不在
- `paper.md`、`main.tex`、`paper.pdf` の再生成差分
- 収録PDFと再生成PDFのテキスト層、ページ数、用紙寸法の一致
- LaTeXログに重大警告がないこと
- `git diff --check`
