# 検算と品質確認

この文書はdraft-60のQ2固定目標本文同期、再現計算、静的整合性、PDF生成、目視確認の記録である。検証日は2026-09-01。

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

## draft-60方針監査

- Q2-1の本文と付録へ、4モードCNOTが積入力を2論理部分系に関して非分離な共同内部状態へ写すことを明記した。その状態を2つの物理的測定端へ接続して検査する課題はQ2-2に残した。
- Q2-3を、$L=2^n$ の同一直接モード担体上でR112の有限ゲート列を作用させ、途中で枝選択せず、回路末尾だけでM50/R164/R170を計算基底読出しへ特殊化する構成として本文へ追加した。最終分布の事前計算・直接埋込みを使わず、任意の固定有限回路と正の誤差について有限であることを確認した。
- Q2-3は有限部品と開放instrument契約の単一運転への接続を条件として条件付き達成へ更新した。独立の新定理または新しいミクロ模型を追加したものではない。
- Q2-4はQ2-3から分離し、$2^n$ モードと枝を含む指数資源を避ける一標本資源台帳として未達を維持した。resetは採用時だけ数え、無反応・失敗は完全結果空間上の全変動距離へ含める。
- Q2-5へ白石--松本型の量子熱化決定不能性を構成原理として追加し、既知の孤立量子系結果と本稿の未達な局所古典開放系目標を区別した。有限時間の非停止判定、超計算、量子出力サンプリングの高速化は非主張とした。
- `PROJECT_STATUS.md`、`README.md`、本文、付録、参考文献、CI、生成器の固定目標検査をQ2-3条件付き達成、Q2-4・Q2-5未達へ同期した。

## draft-59方針監査

- 旧Q1-4のZeno効果をQ1-2へ統合し、Q1-2を「射影測定統計とZeno効果」へ変更した。固定基準に2値Born分布、同軸反復分布、異軸逐次分布、有限回反復測定によるZeno型抑制を含めた。
- 旧Q1-3「完全操作・測定周期」を固定目標と現在地表から削除した。旧Q1-3と旧Q1-4のIDを再利用せず、完全周期、永久記録、内部逆計算、reset、周期総収支を実装・熱力学的強化課題へ移した。
- R143とR144の本文および付録B.12を照合し、Born分布、同軸反復分布、異軸逐次分布をQ1-2の導出済み部分とした。測定後固有状態は独立の固定条件から外し、これらの分布を支える現行実現機構として残した。
- Q1-2の現在地は部分達成を維持した。残件を、零傾斜Rabi対照、継続Rabi駆動下の有限回測定、flip・reflip・無反応を含む全履歴、tilt対照、有限誤差、資源台帳を備えた正のZeno抑制余裕に限定した。
- `PROJECT_STANCE.md` と `PROJECT_GUIDE.md` に、固定目標が明記しない有限局所Hamiltonian実装、有限閉鎖Hamiltonian持ち上げ、完全周期、周期総収支を達成条件から分離する規約を追加した。明示的な開放ミクロモデルも達成候補とする一方、要求された入出力または逐次過程の接続自体は必要とした。
- M51、R170、M47の有限局所Hamiltonian統合と周期総収支を未解決問題として保存したが、Q1-2の達成判定から外した。Q2とQ3の固定目標、現在地、達成判定には変更を加えていない。
- `notes/q1_zeno_revival.md` を `notes/q1_2_zeno_integration.md` へ改名し、旧結果の保存と現行Q1-2のZeno検証線を分けた。新しいモデルID、結果ID、定理、証明、数値結果は追加していない。

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
- `README.md`、`PROJECT_STANCE.md`、`PROJECT_GUIDE.md`、`PROJECT_STATUS.md`、`CHANGELOG.md`、`MANIFEST.md`、`CITATION.cff`、本文、付録、研究メモ、CIをdraft-60へ同期した。
- 現行固定目標表、現在地表、README、本文の達成表に旧Q1-3と旧Q1-4の行が残っていないことを確認した。履歴説明では旧IDを明示して統合・削除関係を保存した。
- 固定目標検査へQ1-2の新名称、Born分布、同軸反復分布、異軸逐次分布、Zeno型抑制、tilt対照の必須語と、旧Q1行の不在検査を追加した。
- 固定目標検査へQ2-1の非分離内部状態、Q2-3の有限回路直接モード合成、Q2-4の一標本多項式資源、Q2-5の白石--松本型構成と極限順序の必須語を追加した。現在地はQ2-3を条件付き達成、Q2-4・Q2-5を未達として全表で一致させた。
- `notes/q1_2_zeno_integration.md` の存在と旧Zenoメモ2パスの不在を、生成器とCIの必須条件へ変更した。
- 現行原稿と検算コードに吸収済み結果ID、M35、旧付録名、旧検算器名が残っていないことを確認した。
- 生成対象MarkdownにC0制御文字が含まれないことを検査する規則を追加した。
- `python -m py_compile tools/*.py` と `git diff --check` は成功した。

## PDF生成

- 出力: `paper.pdf`
- ページ数: 198
- 用紙: A4
- ファイルサイズ: 1,235,418 bytes
- SHA-256: `877b476547822221cdd20235a5d7a6a14dfef33476abf359ec46b6f02f64a14b`
- `SOURCE_DATE_EPOCH` は2026-09-01 00:00:00 UTCである。
- 連続2回の生成で `paper.md`、`main.tex`、`paper.pdf` のバイナリが一致した。
- 未解決のcitation/reference、overfull/underfull box、fatal error、欠落文字はない。
- Latin Modern Mathの一部にbold fallback警告があるが、文字欠落や配置崩れはない。

## PDF目視確認

全198ページを50 dpiでレンダリングし、20ページずつ10枚のコンタクトシートで通覧した。さらに物理PDFページ1、15--16、26--27、43--44、87--88、91--94、108、159、174、184、189、198を130 dpiで重点確認した。対象には表紙のdraft-60表示、目次、第1章のQ2現在地表、第2章のQ2-3有限回路直接モード合成、第4章と第5章のQ2-1非分離状態、第8章のQ2固定目標判定、第9章の結論、付録J--Mの接続条件、参考文献末尾を含む。

クリッピング、重なり、意図しない空白ページ、黒塗り領域、数式の欠落、表の破綻、見出しの破綻は見つからなかった。初回重点確認では2.10節の `\varepsilon_g` に混入した制御文字を検出したため、原稿を修正し、C0制御文字検査を生成器へ追加して再生成した。最終ログではoverfull、underfull、未定義参照、欠落文字はなく、ヘッダー、フッター、ページ番号、章・付録の切替も正常である。

## CI

GitHub Actionsは次を確認する。

- 現行16本の検証スクリプトとPython構文検査
- 付録A--N、現行検算器、退役索引の存在と旧現行パスの不在
- R112、R171--R174、R135、R161、R162、R164、R168、R170の共通層、R86、R123--R125、R140、R143、R145、R147、R153、R155、R159の集約条件
- M51/M37/M42とR171--R174の必須語、R172--R174定理宣言の一意性、M42検算器の26項目
- 固定長期目標の全達成判定語、Q1-2の新名称と統合基準、旧Q1-3・旧Q1-4行の不在
- Q2-1の非分離内部状態の位置づけ、Q2-3の有限回路機能再現、Q2-4の多項式資源台帳、Q2-5の自律計算・極限順序
- Q2-3--Q2-5、Q3-2を凍結中と扱う旧記述の不在と、Q2-3の「条件付き達成」、Q2-4・Q2-5・Q3-2の「未達」判定
- Q1-2 Zeno統合メモの存在と旧Zenoメモパスの不在
- 現行原稿と検算コードにおける吸収済みモデルID・結果IDの不在
- 生成対象MarkdownにおけるC0制御文字の不在
- `paper.md`、`main.tex`、`paper.pdf` の再生成差分
- 収録PDFと再生成PDFのテキスト層、ページ数、用紙寸法の一致
- LaTeXログに重大警告がないこと
- `git diff --check`
