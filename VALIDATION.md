# 検算と品質確認

この文書はdraft-52の再現計算、静的整合性、PDF生成、および目視確認の記録である。検証日は2026-08-29。

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
python tools/verify_q2_action_shell_integration.py
python tools/verify_q2_1_gate.py
python tools/verify_m49_joint_bath_provider.py
python tools/verify_m48_paired_hopf.py
python tools/verify_m48_full_cycle.py
python tools/verify_m39_m48_ablation.py
python tools/verify_m37_m50_position_instrument.py
python tools/verify_q3_completion.py
python simulations/m45_open_quasicritical/verify.py --quick
python tools/build_paper.py
```

## draft-52理論監査

- M42を現行採用モデルから退役させた。旧R113--R118は `PROJECT_STATUS.md` の置換済み結果台帳と `notes/superseded_m42_continuous_particle_position.md` にだけ残し、現行章・付録・証拠鎖から除外した。
- 現行Q3受渡しをM37--R167--R168/R169--M50--R170に固定した。R167は単一試行の包絡誤差を集団の非中心化規格化第2モーメントへ持ち上げる。中心化共分散とは区別し、R168の支持結論へ中心化共分散だけを代入しない。
- R168は階数1支持から各試行のM50枝分布を導く。装置入力は集団因子または共分散でなく、同じ試行に存在するM37信号である。零信号、閾値未満、保持失敗は明示的無反応 $\varnothing$ とし、成功試行だけで再規格化しない。
- R169は高階数公式に固定全作用を要求する。可変作用反例 $Z=\sqrt3e_1,e_2$ ではray平均と規格化第2モーメントのtrace距離が $1/4$ になる。一般の作用変動はradial補正で評価する。
- R170は入力標本時刻 $t_\star$ と出力記録時刻 $t_{\rm out}>t_\star$ を分離する。入力以前の連続粒子位置等変性、Schrödinger型の装置内粒子軌道、初回到達、吸収、時間積分流束は主張しない。
- M50の状態数表示と殻消去表示を分けた。R170は $E_i^\delta=-\Theta\log\pi_i^\delta$ だけを有限熱化へ渡し、同じ分配関数で状態数を重ねて数えない。
- Q3-1とQ3-3は達成を維持した。Q3-4とQ3-5は、R170の作用容量結合、殻内平衡化、信号保持、衝突bath、枝固定、局所記録を同じ有限局所Hamiltonianへ統合していないため、条件付き達成へ改めた。
- 同じM37偏差を共分散誤差、ray誤差、容量誤差へ二重加算しない。R168経路またはR169経路の一方を選び、R170の完全結果集合上で誤差を合成する。

## 数値・代数検証

`tools/verify_m37_m50_position_instrument.py` はR167--R170に対応する31項目を確認する。主な数値は次の通り。

- R167 trace距離: `0.0003785985871776989`
- R167上界: `0.036319466370298495`
- R169可変作用反例のtrace距離: `0.24999999999999997`
- R170有限時間混合誤差: `1.6705734018351848e-13`
- R170混合予算: `0.003999999999999999`
- 例示誤差台帳: `epsilon_170 = 0.033`

混合時間は、例示誤差台帳の混合予算 `0.004` と同じ値から計算した。処理時間を別の緩い目標から選ばない。

確認数は各スクリプト内のスカラーassertionまたは診断項目の数であり、独立な定理、独立な証明、または独立な物理予測の数ではない。

| 検証 | 自動確認項目数 |
|---|---:|
| envelope reduction | 19 |
| phase correlation | 15 |
| action distribution | 40 |
| M47 Q1 | 43 |
| M47 Hopf | 20 |
| M47 collision thermodynamics | 29 |
| M47 action-shell origin | 35 |
| Q2 action-shell integration | 33 |
| Q2-1 | 25 |
| M49 joint-bath provider | 29 |
| M48 paired-Hopf | 56 |
| M48 full cycle | 88 |
| M39--M48 ablation | 16 |
| M37--M50 position instrument | 31 |
| Q3 pair model | 36 |
| M45 quick diagnostics | 23 |
| **合計** | **538** |

全項目が成功した。

## 静的整合性

- 定理系環境の開始・終了数は一致した。theorem 47、proposition 7、lemma 5、corollary 1、proof 40。
- `PROJECT_STATUS.md`、`README.md`、`CHANGELOG.md`、`MANIFEST.md`、`CITATION.cff`、本文、付録をdraft-52へ同期した。
- 現行 `sections/*.md` にM42またはR113--R118が残っていないことを静的に検査した。
- R167--R170、$t_\star<t_{\rm out}$、$\varepsilon_{170}$、M42の置換済み判定、M50のQ1・Q2・Q3共通判定をCIの必須条件にした。
- 旧付録Fと旧粒子位置検証器の不在、新付録F、新検証器、M42退役メモの存在を検査した。
- `python -m py_compile` と `git diff --check` は成功した。

## PDF生成

- 出力: `paper.pdf`
- ページ数: 235
- 用紙: A4
- ファイルサイズ: 1,594,273 bytes
- SHA-256: `ede3663778f59691847ec26eb00af22955bd3a46d0ab405cfd49df47d243f35b`
- `SOURCE_DATE_EPOCH` をdraft-52の公開日へ更新した。連続2回の生成でPDFバイナリが一致した。
- 未解決のcitation/reference、overfull/underfull box、fatal error、欠落文字、過大floatはない。
- Latin Modern Mathの一部にbold fallback警告があるが、文字欠落や配置崩れはない。

## PDF目視確認

全235ページを10枚の低解像度コンタクトシートで通覧した。さらに、R167--R170を含む第6章59--64ページと、新付録Fの138--144ページを144 dpiで重点監査した。

クリッピング、重なり、意図しない空白ページ、黒塗り領域、数式の欠落、表の破綻、見出しの破綻は見つからなかった。表紙、目次、ヘッダー、フッター、ページ番号、章・付録の切替も正常である。

## CI

GitHub Actionsは次を確認する。

- 上記16本の検証スクリプト
- 現行章・付録・検証器・退役メモの存在と旧現行パスの不在
- status guide、README、本文、付録の達成判定と結果IDの整合性
- 現行章におけるM42、R113--R118の不在
- `paper.md`、`main.tex`、`paper.pdf` の再生成差分
- 収録PDFと再生成PDFのテキスト層、ページ数、用紙寸法の一致
- LaTeXログに重大警告がないこと
- `git diff --check`
