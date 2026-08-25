# 検算と品質確認

この文書は draft-45B の再現計算、静的整合性、PDF 生成、および目視確認の記録である。検証日は 2026-08-26。

## 実行方法

リポジトリ直下で次を実行する。

```bash
python tools/verify_envelope_reduction.py
python tools/verify_phase_correlation.py
python tools/verify_action_distribution.py
python tools/verify_m47_q1_instrument.py
python tools/verify_m47_hopf_preparation.py
python tools/verify_q2_1_gate.py
python tools/verify_m48_paired_hopf.py
python tools/verify_m48_full_cycle.py
python tools/verify_realized_configuration.py
python tools/verify_q3_completion.py
python simulations/m45_open_quasicritical/verify.py --quick
python tools/build_paper.py
```

## draft-45B 理論監査

- R151 は M39 から M48 への破壊的 SWAP 引渡しと、反対称な paired-Hopf 制御入力を固定する。
- R152 は有限設定族ごとの有限状態 matching CTMC、正則化定常分布、paired-phase 流、および有限時間の準備誤差を明示する。
- R153 は結合切断時の matching fiber 条件を与える。連続分布から特異な ray fiber への有限時間収束を全状態の全変動距離で主張せず、半径誤差と共通位相商を含む射影的 paired-fiber 距離で評価する。
- R154 は切断後の局所分析器、再整合、傾斜固定、および局所記録を規定する。
- R155 は固定 singlet、有限設定族、有限誤差の範囲で余弦共同分布、無信号周辺分布、CHSH 値、および設定依存性をまとめる。
- R156 は fresh-cell reset を規定し、次試行への記憶持越しを排除する。
- Q2-2 は上記の限定された意味で「条件付き達成」とする。R152 の微視的導出、空間的局所性、自由設定、一般状態への拡張は未達である。
- M41 は現行モデルから外し、置換前の履歴として `notes/` に移した。
- Q1、Q2-1、Q2-3、Q3 の判定と既存の主張範囲は変更していない。

## 数値・代数検証

`tools/verify_m48_full_cycle.py` は R151--R156 に対応する 88 項目を確認する。主な確認対象は、反対称制御、分岐 seed、有限四頂点埋込み、正規化、詳細釣合い、定常残差、正のスペクトルギャップ、有限時間混合、余弦相関、無偏り周辺分布、CHSH 値、および reset である。

- 最小 matching gap: `1.900700696128881`
- 例示する draft-45B 誤差上界: `0.028`

既存検証を含む結果は次の通り。

| 検証 | 確認数 |
|---|---:|
| envelope reduction | 19 |
| phase correlation | 15 |
| action distribution | 40 |
| M47 Q1 | 43 |
| M47 Hopf | 20 |
| Q2-1 | 25 |
| M48 paired-Hopf | 56 |
| M48 full cycle | 88 |
| realized cycle | 42 |
| Q3 pair model | 36 |
| M45 quick diagnostics | 23 |
| **合計** | **407** |

全項目が成功した。

## 静的整合性

- 定理系環境の開始・終了数は一致した。theorem 34、proposition 5、lemma 4、corollary 3、proof 35。
- `PROJECT_STATUS.md`、`README.md`、`CHANGELOG.md`、`MANIFEST.md`、本文、および付録の draft-45B 表記と参照先を照合した。
- 現行検証から旧 M41 検証を外し、M48 full-cycle 検証へ置換した。
- Q2-3 節、Q3 節、Q3 付録、および M45 図版が基準コミットから不変であることを SHA-256 で確認した。
- `git diff --check` に空白エラーはない。

## PDF 生成

- 出力: `paper.pdf`
- ページ数: 192
- 用紙: A4
- ファイルサイズ: 1,383,568 bytes
- SHA-256: `b796fd2cc31323897f26dc359a4adda03a50061306c68e4f53b8f6d33d465a61`
- 未解決の citation/reference、overfull/underfull box、fatal error、欠落文字、過大 float はない。
- Latin Modern Math の一部に bold fallback 警告があるが、文字欠落や配置崩れはない。

## PDF 目視確認

全 192 ページを低解像度コンタクトシートで通覧した。さらに、物理ページ 1--10、45--54、123--132、177--190 を高解像度で確認し、表紙、目次、第 5 章の M48 方程式、付録 D の証明、付録 J の状態表を重点監査した。

クリッピング、重なり、意図しない空白ページ、黒塗り領域、数式の欠落、および見出しの破綻は見つからなかった。

## CI

GitHub Actions は次を確認する。

- 上記 11 本の検証スクリプト
- 現行章・付録・検証器の存在と旧 M41 現行パスの不在
- status guide と本文の整合性
- `paper.md`、`main.tex`、`paper.pdf` の再生成差分
- 192 ページであること
- LaTeX ログに重大警告がないこと
- `git diff --check`
