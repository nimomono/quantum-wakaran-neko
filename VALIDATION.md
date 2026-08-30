# 検算と品質確認

この文書はdraft-58のM37担体・M42局在トークン再編、再現計算、静的整合性、PDF生成、目視確認の記録である。検証日は2026-08-30。

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
python tools/verify_m42_spatial_token.py
python tools/verify_q2_shell_and_locality.py
python tools/verify_m48_full_cycle.py
python tools/verify_common_signal_m50.py
```

## draft-58方針監査

- Q3のミクロ模型を、実振動子網と局所結合を持つM37担体層と、1個の局在位置、局所辺bath、clock、履歴、記録を持つM42粒子層に分けた。M37の実変数が単一試行の担体、複素包絡と位置重みが派生量・集団統計、M42位置が単一試行の粒子状態である。
- R86の反回転項を含む有限時間包絡縮約、実正準方程式、局所包絡、normal-mode表示と誤差評価を保持した。Q3-1の固定基準と達成根拠はR86のままであり、M42を遡及的な達成条件にしていない。
- M37有効辺流から局所最小jump率を作り、初期Born型位置分布を全有限時刻へ運ぶM42の等変輸送をR172として定理化した。
- 節で発散しない一様正則化率、正則化極限の全変動評価、方向タグ・物理閾値・仕事registerを持つ局所辺bathによる有限駆動衝突Hamiltonian近似をR173として定理化した。一般有向率へR162の詳細釣合い公式を誤用しない境界も明示した。
- M51準備、M50/R164による1回だけの初期位置選択、M37担体輸送、M42局所輸送、R112による終位置記録をR174の誤差台帳で接続した。終時刻に別のM50位置を再抽選せず、無反応質量を結果空間に保持する。
- 付録Nに、有限bath tapeと閾値を含むpiecewise deterministic open system、局所jump写像、overflow無反応枝、節正則化、有限衝突持上げ、Duhamel受渡し、R123--R125への接続を明示した。
- 第2章を「有限モード担体と共通正準モジュール」へ再編し、Q1の2モード、Q2の4モード、Q3の空間セル担体が同じ正準モジュールを共有しても同じhardwareではないことを明記した。
- 旧M42/R113--R118は退役履歴のまま残し、現行M42/R172--R174と混同しない索引を更新した。R168/R170はQ3の固定時刻統計診断として残すが、現行の同一試行輸送経路には用いない。
- 固定長期目標と達成ラベルは変更していない。`PROJECT_STANCE.md` と `PROJECT_GUIDE.md` は具体的モデルを含めない方針を保ち、今回の改訂対象外とした。

## 数値・代数検証

`tools/verify_common_signal_m50.py` はR135、R168、R170に対応する31項目を確認した。主な数値は次の通り。

- R135 trace距離: `0.0003785985871776989`
- R135上界: `0.036319466370298495`
- R168可変作用反例のtrace距離: `0.24999999999999997`
- R170有限時間混合誤差: `1.6705734018351848e-13`
- R170混合予算: `0.003999999999999999`
- 例示誤差台帳: `epsilon_170 = 0.033`

`tools/verify_m42_spatial_token.py` はR172--R174に対応する26項目を確認した。主な残差は次の通り。

- M37作用保存誤差: `8.881784e-16`
- 辺流の反対称性誤差: `3.469447e-18`
- 局所連続方程式誤差: `6.938894e-18`
- R172 master方程式誤差: `3.469447e-18`
- 正逆方向の駆動衝突率が各物理閾値から再現されること
- 初期作用殻選択の最大頻度誤差: `3.989125e-06`（上限 `5.000000e-06`）
- 完全結果分布の規格化誤差: `3.552714e-15`

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
| M42 spatial token | 26 |
| **合計** | **539** |

全項目が成功した。

## 静的整合性

- 定理系環境の開始・終了数は一致した。theorem 24、proposition 2、lemma 2、corollary 0、proof 37。
- 付録はA--Nの連番で、ファイル名、`@number`、章見出し、式参照を照合した。
- `README.md`、`PROJECT_STATUS.md`、`CHANGELOG.md`、`MANIFEST.md`、`CITATION.cff`、本文、付録、検算器をdraft-58へ同期した。`PROJECT_STANCE.md` と `PROJECT_GUIDE.md` に差分がないことも確認した。
- R172、R173、R174の定理宣言が第6章にそれぞれ一つだけ存在し、付録Nは完全形と証明だけを持つことを確認した。
- M42、R172--R174、付録N、新検算器が生成器とCIの必須対象であり、Q1--Q3の固定目標と達成ラベルがdraft-57から変わっていないことを確認した。
- 現行原稿と検算コードに吸収済み結果ID、M35、旧付録名、旧検算器名が残っていないことを確認した。
- `python -m py_compile tools/*.py` と `git diff --check` は成功した。

## PDF生成

- 出力: `paper.pdf`
- ページ数: 193
- 用紙: A4
- ファイルサイズ: 1,211,906 bytes
- SHA-256: `8a4cf0bcee47372dfa29901ce64e86760a7d310d3175fd3e20a7b688de9a7d8a`
- `SOURCE_DATE_EPOCH` は2026-08-30 00:00:00 UTCである。
- 連続2回の生成で `paper.md`、`main.tex`、`paper.pdf` のバイナリが一致した。
- 未解決のcitation/reference、overfull/underfull box、fatal error、欠落文字はない。
- Latin Modern Mathの一部にbold fallback警告があるが、文字欠落や配置崩れはない。

## PDF目視確認

全193ページを50 dpiでレンダリングし、20ページずつ10枚のコンタクトシートで通覧した。さらに物理PDFページ1、17--19、60--61、67、69、71--72、74、185--190、193を110 dpiで重点確認した。対象には表紙、第2章の層構造表、第6章のM37/M42二層定義、R172--R174と誤差台帳、付録Nの完全方程式・有限衝突持上げ・因果接続・非主張、参考文献末尾を含む。

クリッピング、重なり、意図しない空白ページ、黒塗り領域、数式の欠落、表の破綻、見出しの破綻は見つからなかった。表紙の版表示はdraft-58で、ヘッダー、フッター、ページ番号、第6章と付録Nの切替も正常である。第2章と第6章の長い章名も左右ヘッダーへ重ならないことを重点ページとコンタクトシートで確認した。

## CI

GitHub Actionsは次を確認する。

- 現行16本の検証スクリプトとPython構文検査
- 付録A--N、現行検算器、退役索引の存在と旧現行パスの不在
- R112、R171--R174、R135、R161、R162、R164、R168、R170の共通層、R86、R123--R125、R140、R143、R145、R147、R153、R155、R159の集約条件
- M51/M37/M42とR171--R174の必須語、R172--R174定理宣言の一意性、M42検算器の26項目
- 固定長期目標の全達成判定語
- Q2-3の固定名、多項式資源台帳、指数コスト除外条件、成功試行だけを再規格化しない条件
- Q1-4、Q2-3、Q3-2を凍結中と扱う旧記述の不在と、再開後の「未達」判定
- 現行原稿と検算コードにおける吸収済みモデルID・結果IDの不在
- `paper.md`、`main.tex`、`paper.pdf` の再生成差分
- 収録PDFと再生成PDFのテキスト層、ページ数、用紙寸法の一致
- LaTeXログに重大警告がないこと
- `git diff --check`
