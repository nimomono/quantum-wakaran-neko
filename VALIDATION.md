# 検算と品質確認

この文書は draft-49 の再現計算、静的整合性、PDF 生成、および目視確認の記録である。検証日は 2026-08-28。

## 実行方法

リポジトリ直下で次を実行する。

```bash
python tools/verify_envelope_reduction.py
python tools/verify_phase_correlation.py
python tools/verify_action_distribution.py
python tools/verify_m47_q1_instrument.py
python tools/verify_m47_hopf_preparation.py
python tools/verify_m47_collision_thermodynamics.py
python tools/verify_m47_action_shell_origin.py
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

## draft-49 理論監査

- R164 は旧R24の一般作用殻容量を現行M47へ移植し、単一試行信号作用のW型mode分解、正則化枝容量、排他的2作用殻、単一母Liouville測度からBorn型条件付き重みを導く。旧M15の入口標本化、等方混合、標本化後再埋込み、測定周期は復活させない。
- R164 の状態数は2作用殻で容量に線形であり、直接作用分配次元を増やすと一般に容量の冪になる。共通spectator因子は規格化で消えるが、枝依存spectator体積、coarea因子、入口流束は枝対称性誤差として残る。
- R164 は厳密作用殻に加えて滑らかな有限剛性殻を評価し、有限幅、枝対称性、作用容量結合、fiber内準備を独立誤差に分ける。正則化を外す極限では必要剛性が少なくとも $O(\delta^{-2})$ まで増え得る。
- R161 はR164で得た正則化条件付き状態数とmesostate有効自由エネルギーについて、平方根型局所率、詳細釣合い、一意定常分布、全ray一様混合率、共通位相・振幅不変性、node no-goを明示する。
- R162 は有限衝突bath、対称基準障壁、粗視化有効自由エネルギー保存散乱からR161の率を実現し、有限セルoverflow、有限エネルギー、閾値平滑化、時計、信号bath保持を誤差として分離する。fiberを含む全微視的Hamiltonianのエネルギー保存とは同一視しない。
- R163 は配置部分の正逆経路確率比、積分ゆらぎ関係、quench有効仕事と相対エントロピーの恒等式を与える。ゆらぎの定理はR164で得た地形の下流整合性検査であり、状態数の線形則を選ぶ起源ではない。
- R143、R144 は連続matching保存を仮定せず、操作面ごとの再平衡化、入射停止、辺閉鎖、局所記録、template交換、測定後再平衡化を合成する。
- Q1-2 は作用容量結合、fiber内平衡化、枝対称性、信号bath反作用を同じ有限局所Hamiltonian周期へ統合する問題を残し、Q1-3はHopf pumpからresetまでの周期総収支を残すため、いずれも部分達成を維持する。

- 付録KはQ2共同bath--実現配置の共通状態、cross matching、単一試行配置matching、row-major規約、setting-free受渡し面、破壊的dilationを固定する。
- R151 は M48 内部の setting-pre 等重み seed を履歴から独立に paired-Hopf 安全盆へ送る。M39共同配置をseedへ写す処理は任意adapterであり、M48の必須入力ではない。
- R152 はR161のBell限定形であり、有限設定族ごとの有限状態 matching CTMC、正則化定常分布、paired-phase 流、および有限時間の準備誤差を明示する。R162の有限衝突実現を利用できる。
- R153 は結合切断時の matching fiber 条件を与える。連続分布から特異な ray fiber への有限時間収束を全状態の全変動距離で主張せず、半径誤差と共通位相商を含む射影的 paired-fiber 距離で評価する。
- R154 は切断後の局所分析器、再整合、傾斜固定、および局所記録を規定する。
- R155 はM48単独周期について、固定 singlet、有限設定族、有限誤差の範囲で余弦共同分布、無信号周辺分布、CHSH 値、および設定依存性をまとめる。
- R156 は fresh-cell reset を規定し、次試行への記憶持越しを排除する。
- R157 はM49の同じ4モードprogram担体の作用区間から共同配置をdecodeし、行templateからcross momentと2端の単一試行配置matchingを同時に作る。固定有限program族の $\rho_*$、稀な行の作用下界、無反応込み誤差を分ける。
- R158 は担体、B bath、B配置へ同じCNOTを同一時計窓で作用させ、cross momentと共同配置を点ごとに同じ出力programへ写す。
- R159 はprogram、入力配置、出力読出しに独立な3選択器を使い、固定有限入力、入力頻度、固定積出力基底の共同統計を閉じる。1角共有反例と一意エルゴード性・混合性の区別を含む。
- R160 は固定singlet出力の同じbath・配置registerをsetting-free面からM48へ渡し、cross projector感度と枝biasを保存する。
- M48単独周期と固定目標Q2-2全体は、固定singlet型、固定有限設定族、準備先行、非空間分離、採用開放法則の限定された意味で「条件付き達成」とする。各翼のR164作用殻とR162、paired-Hopf・seed routing・2翼controllerの同一有限局所Hamiltonian統合、空間的局所性、自由設定、一般状態への拡張は未達である。
- M41 は現行モデルから外し、置換前の履歴として `notes/` に移した。
- M39を置換済みQ2-1模型へ移し、M42/R113をQ2-3・Q3だけに限定した。Q1、Q2-1、Q2-3、Q3 の判定は変更していない。

## 数値・代数検証

`tools/verify_m48_full_cycle.py` は R151--R156 に対応する 88 項目を確認する。主な確認対象は、固定pairing tensor、等重みseed、安全盆routing、有限四頂点埋込み、正規化、詳細釣合い、定常残差、正のスペクトルギャップ、有限時間混合、余弦相関、無偏り周辺分布、CHSH 値、および reset である。

`tools/verify_m39_m48_ablation.py` は16項目を確認する。10,000件の一般入力に対する旧controller ray collapse、M39枝と内部fair seedのBell共同分布一致、枝bias sweep、provenance条件付き不変性、一般複素行列のrow/column permutationを検査する。

`tools/verify_m49_joint_bath_provider.py` は29項目を確認する。10,000件の一般複素programについて、R157のcross moment・配置matching・稀な行の作用下界・有限失敗上界、R158の担体・bath・配置CNOT共変性、R159の固定有限benchmarkと1角共有反例、R160のsinglet fiber・state感度・枝bias保存を検査する。

`tools/verify_m47_collision_thermodynamics.py` は29項目を確認する。R164の作用殻容量から作るR161標的の正規化、詳細釣合い、一様スペクトルギャップ下界、正則化誤差、位相・振幅不変性、node no-go、R162の衝突率、粗視化有効自由エネルギー保存、逆散乱、有限セルoverflow、有限エネルギー尾、R163のquench有効仕事、相対エントロピー、経路積分ゆらぎ関係を検査する。

`tools/verify_m47_action_shell_origin.py` は31項目を確認する。R164の信号作用分解、正則化枝容量、一般作用殻公式、2作用殻の線形性、Born型規格化重み、有効自由エネルギー、作用分配次元の剛性、共通spectator因子の相殺、枝依存流束誤差、滑らかな有限幅殻、$\delta^{-2}$ 剛性増大、零seed、障壁gauge不変性、およびR161との詳細釣合い接続を検査する。

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
| M47 collision thermodynamics | 29 |
| M47 action-shell origin | 31 |
| Q2-1 | 25 |
| M49 joint-bath provider | 29 |
| M48 paired-Hopf | 56 |
| M48 full cycle | 88 |
| M39--M48 ablation | 16 |
| realized cycle | 42 |
| Q3 pair model | 36 |
| M45 quick diagnostics | 23 |
| **合計** | **512** |

全項目が成功した。

## 静的整合性

- 定理系環境の開始・終了数は一致した。theorem 45、proposition 7、lemma 5、corollary 2、proof 42。
- `PROJECT_STATUS.md`、`README.md`、`CHANGELOG.md`、`MANIFEST.md`、本文、および付録の draft-49 表記と参照先を照合した。
- 現行検証から旧 M41 検証を外し、M48 full-cycle 検証へ置換した。
- Q2-3・Q3の達成判定、Q3本体、Q3付録の定理・証明ブロック、および M45 図版が基準コミットから不変であることを確認した。Q2-3資源台帳はM49の直接モード費用へ更新し、付録Fは冒頭の適用範囲だけを「Q2-3・Q3」に更新した。
- `git diff --check` に空白エラーはない。

## PDF 生成

- 出力: `paper.pdf`
- ページ数: 224
- 用紙: A4
- ファイルサイズ: 1,545,851 bytes
- SHA-256: `04334da0523255844bdc84ae7d9d9778e50213316bd928e2bbb481518bfb8c4e`
- `SOURCE_DATE_EPOCH` と内容由来のPDF trailer IDを固定し、連続2回の生成でPDFバイナリが一致した。
- 未解決の citation/reference、overfull/underfull box、fatal error、欠落文字、過大 float はない。
- Latin Modern Math の一部に bold fallback 警告があるが、文字欠落や配置崩れはない。

## PDF 目視確認

全 224 ページを5枚の低解像度コンタクトシートで通覧した。さらに、物理ページ 14--33、193--221 を144--168 dpiで確認し、第1章の判定表、第3章のR164とQ1周期、付録LのR161--R163・有限衝突熱浴・有効仕事、付録Mの作用殻容量・R164・有限幅誤差・非主張を重点監査した。

クリッピング、重なり、意図しない空白ページ、黒塗り領域、数式の欠落、および見出しの破綻は見つからなかった。

## CI

GitHub Actions は次を確認する。

- 上記 15 本の検証スクリプト
- 現行章・付録・検証器の存在と旧 M41 現行パスの不在
- status guide と本文の整合性
- `paper.md`、`main.tex`、`paper.pdf` の再生成差分
- 収録PDFと再生成PDFのテキスト層、ページ数、用紙寸法の一致
- 224 ページであること
- LaTeX ログに重大警告がないこと
- `git diff --check`
