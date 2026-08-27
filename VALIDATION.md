# 検算と品質確認

この文書は draft-47 の再現計算、静的整合性、PDF 生成、および目視確認の記録である。検証日は 2026-08-27。

## 実行方法

リポジトリ直下で次を実行する。

```bash
python tools/verify_envelope_reduction.py
python tools/verify_phase_correlation.py
python tools/verify_action_distribution.py
python tools/verify_m47_q1_instrument.py
python tools/verify_m47_hopf_preparation.py
python tools/verify_q2_1_gate.py
python tools/verify_m49_joint_bath_provider.py
python tools/verify_m48_paired_hopf.py
python tools/verify_m48_full_cycle.py
python tools/verify_m39_m48_ablation.py
python tools/verify_realized_configuration.py
python tools/verify_q3_completion.py
python simulations/m45_open_quasicritical/verify.py --quick
python tools/build_paper.py
```

## draft-47 理論監査

- 付録KはQ2共同bath--実現配置の共通状態、cross matching、単一試行配置matching、row-major規約、setting-free受渡し面、破壊的dilationを固定する。
- R151 は M48 内部の setting-pre 等重み seed を履歴から独立に paired-Hopf 安全盆へ送る。M39共同配置をseedへ写す処理は任意adapterであり、M48の必須入力ではない。
- R152 は有限設定族ごとの有限状態 matching CTMC、正則化定常分布、paired-phase 流、および有限時間の準備誤差を明示する。
- R153 は結合切断時の matching fiber 条件を与える。連続分布から特異な ray fiber への有限時間収束を全状態の全変動距離で主張せず、半径誤差と共通位相商を含む射影的 paired-fiber 距離で評価する。
- R154 は切断後の局所分析器、再整合、傾斜固定、および局所記録を規定する。
- R155 はM48単独周期について、固定 singlet、有限設定族、有限誤差の範囲で余弦共同分布、無信号周辺分布、CHSH 値、および設定依存性をまとめる。
- R156 は fresh-cell reset を規定し、次試行への記憶持越しを排除する。
- R157 はM49の同じ4モードprogram担体の作用区間から共同配置をdecodeし、行templateからcross momentと2端の単一試行配置matchingを同時に作る。固定有限program族の $\rho_*$、稀な行の作用下界、無反応込み誤差を分ける。
- R158 は担体、B bath、B配置へ同じCNOTを同一時計窓で作用させ、cross momentと共同配置を点ごとに同じ出力programへ写す。
- R159 はprogram、入力配置、出力読出しに独立な3選択器を使い、固定有限入力、入力頻度、固定積出力基底の共同統計を閉じる。1角共有反例と一意エルゴード性・混合性の区別を含む。
- R160 は固定singlet出力の同じbath・配置registerをsetting-free面からM48へ渡し、cross projector感度と枝biasを保存する。
- M48単独周期と固定目標Q2-2全体は、固定singlet型、固定有限設定族、準備先行、非空間分離、採用開放法則の限定された意味で「条件付き達成」とする。R152 の微視的導出、空間的局所性、自由設定、一般状態への拡張は未達である。
- M41 は現行モデルから外し、置換前の履歴として `notes/` に移した。
- M39を置換済みQ2-1模型へ移し、M42/R113をQ2-3・Q3だけに限定した。Q1、Q2-1、Q2-3、Q3 の判定は変更していない。

## 数値・代数検証

`tools/verify_m48_full_cycle.py` は R151--R156 に対応する 88 項目を確認する。主な確認対象は、固定pairing tensor、等重みseed、安全盆routing、有限四頂点埋込み、正規化、詳細釣合い、定常残差、正のスペクトルギャップ、有限時間混合、余弦相関、無偏り周辺分布、CHSH 値、および reset である。

`tools/verify_m39_m48_ablation.py` は16項目を確認する。10,000件の一般入力に対する旧controller ray collapse、M39枝と内部fair seedのBell共同分布一致、枝bias sweep、provenance条件付き不変性、一般複素行列のrow/column permutationを検査する。

`tools/verify_m49_joint_bath_provider.py` は29項目を確認する。10,000件の一般複素programについて、R157のcross moment・配置matching・稀な行の作用下界・有限失敗上界、R158の担体・bath・配置CNOT共変性、R159の固定有限benchmarkと1角共有反例、R160のsinglet fiber・state感度・枝bias保存を検査する。

- 最小 matching gap: `1.900700696128881`
- 例示するM48単独周期の誤差上界: `0.028`

既存検証を含む結果は次の通り。確認数は各スクリプト内のスカラーassertionまたは診断項目の数であり、独立な定理、独立な証明、または独立な物理予測の数ではない。

| 検証 | 自動確認項目数 |
|---|---:|
| envelope reduction | 19 |
| phase correlation | 15 |
| action distribution | 40 |
| M47 Q1 | 43 |
| M47 Hopf | 20 |
| Q2-1 | 25 |
| M49 joint-bath provider | 29 |
| M48 paired-Hopf | 56 |
| M48 full cycle | 88 |
| M39--M48 ablation | 16 |
| realized cycle | 42 |
| Q3 pair model | 36 |
| M45 quick diagnostics | 23 |
| **合計** | **452** |

全項目が成功した。

## 静的整合性

- 定理系環境の開始・終了数は一致した。theorem 37、proposition 5、lemma 4、corollary 2、proof 37。
- `PROJECT_STATUS.md`、`README.md`、`CHANGELOG.md`、`MANIFEST.md`、本文、および付録の draft-47 表記と参照先を照合した。
- 現行検証から旧 M41 検証を外し、M48 full-cycle 検証へ置換した。
- Q2-3・Q3の達成判定、Q3本体、Q3付録の定理・証明ブロック、および M45 図版が基準コミットから不変であることを確認した。Q2-3資源台帳はM49の直接モード費用へ更新し、付録Fは冒頭の適用範囲だけを「Q2-3・Q3」に更新した。
- `git diff --check` に空白エラーはない。

## PDF 生成

- 出力: `paper.pdf`
- ページ数: 196
- 用紙: A4
- ファイルサイズ: 1,418,045 bytes
- SHA-256: `e2ac3cfa708b583186ca1ac2e2bbae0882a66e7e50cff9d274ec9860458332db`
- `SOURCE_DATE_EPOCH` と内容由来のPDF trailer IDを固定し、連続2回の生成でPDFバイナリが一致した。
- 未解決の citation/reference、overfull/underfull box、fatal error、欠落文字、過大 float はない。
- Latin Modern Math の一部に bold fallback 警告があるが、文字欠落や配置崩れはない。

## PDF 目視確認

全 196 ページを低解像度コンタクトシートで通覧した。さらに、物理ページ 1、15--18、39--44、78、116--144、177--193 を高解像度または重点コンタクトシートで確認し、表紙、第1章の判定表、第4章のR157--R160、第5章のM48境界、第8章の誤差表、付録C・D・F・Jの証明、付録Kの受渡し契約を重点監査した。

クリッピング、重なり、意図しない空白ページ、黒塗り領域、数式の欠落、および見出しの破綻は見つからなかった。

## CI

GitHub Actions は次を確認する。

- 上記 13 本の検証スクリプト
- 現行章・付録・検証器の存在と旧 M41 現行パスの不在
- status guide と本文の整合性
- `paper.md`、`main.tex`、`paper.pdf` の再生成差分
- 収録PDFと再生成PDFのテキスト層、ページ数、用紙寸法の一致
- 196 ページであること
- LaTeX ログに重大警告がないこと
- `git diff --check`
