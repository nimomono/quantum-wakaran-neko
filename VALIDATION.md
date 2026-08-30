# 検算と品質確認

この文書はdraft-57の共通開放準備改訂、再現計算、静的整合性、PDF生成、目視確認の記録である。検証日は2026-08-30。

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
python tools/verify_m51_common_open_preparation.py
python tools/verify_q2_shell_and_locality.py
python tools/verify_m48_full_cycle.py
python tools/verify_common_signal_m50.py
```

## draft-57方針監査

- M51を、有限個の実正準対、物理template、pump、transverse sink、clock、開放portからなる共通開放準備模型として追加した。複素信号は実正準変数の派生座標、rayと第2モーメントは試行集団の統計量として区別した。
- M51の採用開放方程式から、有限時間のray距離とrank-one第2モーメントの誤差率、port切断後の可逆正準伝播をR171として証明した。R171は採用drift後の厳密結果であり、pumpとsinkを有限閉鎖Hamiltonianから導いた結果ではない。
- 付録Mで、一般Hermitian生成子の実正準Hamiltonian表示、複素式と等価な実方程式、seed測度の押出し、安全事象と無反応、M50への単一試行受渡しを明示した。
- 二乗形の状態依存性をM51が準備する階数1第2モーメントへ、排他的な単一結果をM50/R164/R170へ割り当て、二つを独立な確率源として重ねない規約を本文全体へ反映した。
- R145をM51/R171のW型2モード特殊化として整理した。Q2-1では固定program ray、Q2-2では局所seed、Q3ではM37へ渡すrank-one初期標本という特殊化境界を明示した。
- M51の有限bath持上げ、雑音と揺らぎ散逸関係、総仕事・熱・エントロピー生成、M51--M37--M50の同一装置統合は未導出として残した。
- 固定長期目標と達成ラベルは変更していない。`PROJECT_STANCE.md` と `PROJECT_GUIDE.md` は具体的モデルを含めない方針を保ち、今回の改訂対象外とした。

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
| M51 common open preparation | 25 |
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
| **合計** | **513** |

全項目が成功した。

## 静的整合性

- 定理系環境の開始・終了数は一致した。theorem 21、proposition 2、lemma 2、corollary 0、proof 34。
- 付録はA--Mの連番で、ファイル名、`@number`、章見出し、式参照を照合した。
- `README.md`、`PROJECT_STATUS.md`、`CHANGELOG.md`、`MANIFEST.md`、`CITATION.cff`、本文、付録、検算器をdraft-57へ同期した。`PROJECT_STANCE.md` と `PROJECT_GUIDE.md` に具体的モデルの記述を追加していないことも確認した。
- R171の定理宣言が第2章に一つだけ存在し、付録Mは証明と実変数展開だけを持つことを確認した。
- M51、R171、付録M、新検算器が生成器とCIの必須対象であり、Q1--Q3の達成ラベルがdraft-56から変わっていないことを確認した。
- 現行原稿と検算コードに吸収済み結果ID、M35、旧付録名、旧検算器名が残っていないことを確認した。
- `python -m py_compile tools/*.py` と `git diff --check` は成功した。

## PDF生成

- 出力: `paper.pdf`
- ページ数: 185
- 用紙: A4
- ファイルサイズ: 1,172,988 bytes
- SHA-256: `9bcb988644d55a7a99a388a1bcf55e47bfae00bbfe0bc39ce6f770e45cbe4915`
- `SOURCE_DATE_EPOCH` は2026-08-29 00:00:00 UTCである。
- 連続2回の生成で `paper.md`、`main.tex`、`paper.pdf` のバイナリが一致した。
- 未解決のcitation/reference、overfull/underfull box、fatal error、欠落文字はない。
- Latin Modern Mathの一部にbold fallback警告があるが、文字欠落や配置崩れはない。

## PDF目視確認

全185ページを50 dpiでレンダリングし、20ページずつ10枚のコンタクトシートで通覧した。さらに物理PDFページ1、18--20、78--79、178--185を150 dpiで重点確認した。対象には表紙、第2章のM51方程式とR171、M51/R171誤差台帳、付録Mの実正準方程式・因果台帳・証明・M50受渡し、参考文献末尾を含む。

クリッピング、重なり、意図しない空白ページ、黒塗り領域、数式の欠落、表の破綻、見出しの破綻は見つからなかった。表紙の版表示はdraft-57で、ヘッダー、フッター、ページ番号、章・付録の切替も正常である。
第2章の長い章名による左右ヘッダーの重なりは章名を短縮して解消し、最終PDFの物理ページ18--20と1--40ページのコンタクトシートで再確認した。

## CI

GitHub Actionsは次を確認する。

- 現行15本の検証スクリプトとPython構文検査
- 付録A--M、現行検算器、退役索引の存在と旧現行パスの不在
- R112、R171、R135、R161、R162、R164、R168、R170の共通層、R86、R140、R143、R145、R147、R153、R155、R159の集約条件
- M51とR171の必須語、R171定理宣言の一意性、M51検算器の25項目
- 固定長期目標の全達成判定語
- Q2-3の固定名、多項式資源台帳、指数コスト除外条件、成功試行だけを再規格化しない条件
- Q1-4、Q2-3、Q3-2を凍結中と扱う旧記述の不在と、再開後の「未達」判定
- 現行原稿と検算コードにおける吸収済みモデルID・結果IDの不在
- `paper.md`、`main.tex`、`paper.pdf` の再生成差分
- 収録PDFと再生成PDFのテキスト層、ページ数、用紙寸法の一致
- LaTeXログに重大警告がないこと
- `git diff --check`
