# 現行パッケージ一覧

## draft-88のR191読出し再編

- 付録T `sections/A20_m54_brownian_macrospin_projective_instrument.md` を追加。
- `tools/verify_r191_macrospin.py` を追加し、Born吸引域恒等式、transducer誤差、Itô変換、scale density、有限時間上界、端点dispatcher、Lüders telescopingを検算する。
- Q1/Q2の2結果主線をR191へ接続し、R164/R190/R170を代替・強化経路として保持する。
- draft-88の `paper.md`、`main.tex`、`paper.pdf` は `tools/build_paper.py` から再生成する。


## draft-87のopen-bath簡略化

- R162を開放Poisson-jump実現へ再定義し、R188を有限閉鎖実装の強化結果へ退役。
- Q1/Q2静的選択をR164--R190--R179--R170へ一本化し、R170を吸収pointer、R179をopen reset / incoming-outgoing renewalへ再定義。
- R178DをQ2-4必須依存から外し、有限closed bank、partial-SWAP、cold/spent履歴を中心因果鎖から除去。
- 固定目標と達成ラベルは維持する。


## 統合原稿

- `paper.md`
- `main.tex`
- `paper.pdf`

## 現行章別 Markdown

- `sections/00_overview_and_contents.md`
- `sections/01_scope_and_cycle.md`
- `sections/02_common_canonical_modules.md`
- `sections/03_m47_controlled_w_instrument.md`
- `sections/04_m54_q2_specializations.md`
- `sections/05_m54_setting_pre_receiver.md`
- `sections/06_m37_spatial_envelope.md`
- `sections/07_q3_finite_graph_phenomena.md`
- `sections/08_errors_resources_open_targets.md`
- `sections/09_conclusion.md`
- `sections/A1_common_action_finite_basis.md`
- `sections/A2_m47_controlled_w_instrument_proofs.md`
- `sections/A3_m54_q2_specialization_proofs.md`
- `sections/A4_m54_receiver_cycle_proofs.md`
- `sections/A5_m37_envelope_proofs.md`
- `sections/A6_common_signal_statistics.md`
- `sections/A7_q3_completion_proofs.md`
- `sections/A8_m47_hopf_preparation.md`
- `sections/A9_m54_setting_pre_paired_hopf_receiver.md`
- `sections/A10_q2_common_bath_composition.md`
- `sections/A11_common_collision_bath_thermodynamics.md`
- `sections/A12_common_action_shell_state_count.md`
- `sections/A13_m54_template_port_preparation.md`
- `sections/A14_m54_spatial_moving_matching.md`
- `sections/A15_m54_uniform_register.md`
- `sections/A16_m54_projector_tree_receiver.md`
- `sections/A17_m54_uniform_supply.md`
- `sections/A18_m54_projective_robustness.md`
- `sections/A19_m54_drude_action_shell_bridge.md`
- `sections/90_references.md`

## 論文外の研究メモ

- `notes/README.md`
- `notes/project_sources_key_results.md`
- `notes/superseded_terminal_function_model.md`
- `notes/rejected_forward_weighting_models.md`
- `notes/complementary_terminal_halfspaces.md`
- `notes/gaussian_nelson_examples.md`
- `notes/measurement_dependence_comparisons.md`
- `notes/rejected_bell_causal_alternatives.md`
- `notes/rejected_m44_capture_entropy_preparation.md`
- `notes/rejected_m46_current_transducer.md`
- `notes/independent_m45_open_quasicritical_preparation.md`
- `notes/superseded_m35_born_sampler.md`
- `notes/superseded_result_index.md`
- `notes/superseded_m38_m42_q1.md`
- `notes/superseded_m41_bell_cycle.md`
- `notes/superseded_m41_cycle_proofs.md`
- `notes/superseded_m39_m48_handoff_claim.md`
- `notes/superseded_independent_m48_bell_protocol.md`
- `notes/superseded_m39_m42_q2_1.md`
- `notes/superseded_m49_joint_bath_cnot_provider.md`
- `notes/superseded_m52_path_only_design.md`
- `notes/superseded_separate_m51_m52_m53_models.md`
- `notes/superseded_separate_m50_m55_models.md`
- `notes/superseded_r178_aperture_sampler.md`
- `notes/superseded_m42_continuous_particle_position.md`
- `notes/superseded_r162_r188_finite_collision.md`
- `notes/strengthening_closed_reset_information_bound.md`
- `notes/q1_2_zeno_integration.md`
- `notes/superseded_position_coupling_fisher_closure.md`
- `notes/superseded_three_mode_bell_shell.md`
- `notes/superseded_two_component_induction_field.md`

## 状態・再現性

- `README.md`
- `PROJECT_STANCE.md`
- `PROJECT_GUIDE.md`
- `TERMINOLOGY.md`
- `PROJECT_STATUS.md`
- `CHANGELOG.md`
- `VALIDATION.md`
- `MANIFEST.md`
- `LICENSE_STATUS.md`
- `CITATION.cff`
- `references.bib`
- `tools/build_paper.py`
- `tools/verify_terminology.py`
- `tools/template.tex`
- `tools/verify_common_canonical_control.py`
- `tools/verify_envelope_reduction.py`
- `tools/verify_m47_q1_instrument.py`
- `tools/verify_common_matching_open_jump.py`
- `tools/verify_m47_action_shell_origin.py`
- `tools/verify_q2_shell_and_locality.py`
- `tools/verify_r180_m54_receiver.py`
- `tools/verify_r180_bell_cycle.py`
- `tools/verify_phase_correlation.py`
- `tools/verify_q1xq1_common_bath.py`
- `tools/verify_q1_live_zeno.py`
- `tools/verify_m54_static_instrument.py`
- `tools/verify_r192_radial_stabilizer.py`
- `tools/verify_m54_spatial_matching.py`
- `tools/verify_r181d_projector_tree.py`
- `tools/verify_r179_m54_supply.py`
- `tools/verify_r186_m54_projective_robustness.py`
- `tools/verify_m54_q2_composition.py`
- `tools/verify_m37_w_spectral_tunneling.py`
- `tools/verify_r187_m37_w_q1_bridge.py`
- `tools/verify_q3_completion.py`
- `figures/README.md`
- `.github/workflows/verify.yml`
- `.gitignore`

## 現行モデルの数値シミュレーション

- `simulations/README.md`

## 組版用フォント

- `fonts/README.md`
- `fonts/OFL.txt`
- `fonts/NotoSansJP-Bold.ttf`
- `fonts/NotoSansJP-Regular.ttf`
- `fonts/NotoSerifJP-Bold.ttf`
- `fonts/NotoSerifJP-Regular.ttf`

旧版セクション、旧数値コード、旧PDF、査読回答履歴は収録しない。置換・退役した理論の最小索引と再検討条件は `notes/` に残し、完全な原稿と実装はGit履歴から参照する。

## draft-86のPR #118後整合性校正

- Q3-2の旧「部分達成」残骸をREADME・第8章から除去し、R188による達成状態へ同期。
- Q3-3A/B/Cの達成判定補足と反証条件から有限環境の必須性を除去し、R123有限環境構成は強い現行証人として維持。
- Q1/Q2/Q3の装置統合残件を有限能動部分系＋Hamiltonian無限浴の単一ミクロ装置へ統一し、有限浴化を独立強化へ分離。
- 生成器・CIへ意味論的回帰検査を追加し、CITATION.cff、組版版表示、統合原稿、TeX、PDFをdraft-86へ同期。

## draft-85のR190 Drude作用殻平方根bridge

- R190A--R190Cで、2作用LC殻の作用保存型Drude混合、$I/A$ の有限時間一様化、対称作用開口からR161静的平方根kernelへの接続を追加。
- 反復collisionは履歴条件付きrenewalを別条件とし、R162の一般有向率と有限骨格履歴を置換しない。
- `sections/A19_m54_drude_action_shell_bridge.md`、`tools/verify_r190_drude_shell.py`、Kubo--Hashitsume文献[56]を追加。
- 生成器、CI、状態表、概要、誤差・資源、README、結論、用語、引用情報をdraft-85へ同期し、統合原稿、TeX、PDFを再生成。

## draft-83のQ1-2有限Zeno閉包

- R170直後に固定済み作用容量入力の静的選択・固定系を追加し、走行中W2信号をSWAP・保持しないZeno入口を分離。
- R189A--R189Cで走行中作用容量保持、零傾斜Rabi継続中の階数1射影選別、$N=2$ の有限Rabi--Zeno比較と空操作対照を追加。
- Q1-2を達成へ更新し、単一有限局所Hamiltonian装置への全統合と全周期収支は強化課題として維持。
- `tools/verify_q1_live_zeno.py`、生成器、CI、状態表、研究メモ、統合原稿、TeX、PDFをdraft-83へ同期。

## draft-82のR170選択・固定中核再編

- R170を静的排他的選択・固定の共通正本へ再定義し、旧無番号共通部を吸収。外部記録はR112または系列固有記録機構へ分離。
- R181DをR170下流の段階的射影選別・測定後状態受渡し、R180AをR170を共有する兄弟特殊化へ整理し、Q2-2のR181D依存を撤去。
- 誤差台帳を $\varepsilon_{170}$、$\varepsilon_{170}^{\rm obs}$、$\varepsilon_{181D}^{\rm end}$、$\varepsilon_{170}^{A,B}$ へ責務分離し、生成器・CIで再混入を検査。
- 固定目標と達成ラベルは維持し、`paper.md`、`main.tex`、`paper.pdf` をdraft-82として再生成する。

## draft-81の主目的再整理とQ2-4資源境界

- 保守整合として、R143/R181D/R144のQ1測定後状態責務を現行本文・付録へ同期し、Q1現役因果鎖から旧結果別テンプレート依存を除去。
- Q2-4の「R170衝突」をR162有限衝突部分系へ修正し、Q3-2残件をR184/R162からR185合成加速度への有限時間安定性・明示誤差へ限定。
- 生成器とCIに上記3境界の再混入防止検査を追加。固定目標、達成ラベル、結果ID、draft-81版番号は維持。

- 古典系から量子型有効構造を導くことをプロジェクト全体の主目的へ戻し、量子計算をQ2の副次的応用として整理。
- Chen/Sun/Zhang系列との先行研究境界を保持し、第1章で本稿の物理課題と既知の古典量子情報模擬を分離。
- Q2-4の外部運用資源規約とR186を維持し、指数信号作用による回避では外部資源への露出を別途監査することを明記。
- 現行本文・付録の日本語表記を修正し、「枝」を結果成分／結果経路へ統一。用語回帰検査を強化。
- `paper.md`、`main.tex`、`paper.pdf` をdraft-81として再生成する。
## draft-79のprojective-node共通化とQ1 state-update縮約

- R170/R181D/R180Aに共有するM54 static selection--lock coreとcommon projective nodeの責務を明文化。
- R181D rank-one safe-branch post-state handoffを追加し、Q1の結果別state template交換と測定後再matchingを削除。
- R143をW型読出し特殊化へ縮約し、R144はR181D selected signalの直接受渡しと標準trace-distance誤差合成へ更新。
- 固定目標と達成ラベルは維持し、Q1-2のZeno残件をM37 W2 carrierと反復common projective nodeの接続として保持。
- `tools/verify_r181d_projector_tree.py` と `tools/verify_m47_q1_instrument.py`、CIを新しいstate-update責務へ同期。
- draft-79へ再生成する `paper.md`、`main.tex`、`paper.pdf`。
## draft-78のblack-box operational基準とR186

- 中心目的をblack-box operational equivalenceとして明文化し、内部自由度と外部制御複雑度を分離。
- Q2-4固定目標と達成ラベルを維持し、operational resourceとreported internal resourceの境界を明示。
- R186で疎な静的製造誤差、独立phase noise、projector latch係数誤差のdimension-free評価と、extensive additive noiseのM54 direct-mode障害条件を追加。
- `sections/A18_m54_projective_robustness.md` と `tools/verify_r186_m54_projective_robustness.py` を追加。
- draft-78へ再生成する `paper.md`、`main.tex`、`paper.pdf`。

## draft-77のM37--W--Q1物理bridge

- R187を新設し、有限局所弱結合W型で $J_\kappa/G_\kappa\to0$ を構成。
- 傾斜時のdressed低2cluster、静的M37正常mode $f_{\omega_0}(h)$ の分裂較正、有限quench/smooth switchを合成し、固定 $U\in SU(2)$ の任意精度carrier実装を証明。
- 零傾斜全mode正常座標の最低2正準pairをM54 W2 static profileのsignal subsystemへcanonical同定し、高modeを捨てないhandoffを明示。
- Q1-1「達成」、Q1-2「部分達成」、Q2/Q3の達成ラベルは変更しない。R187はcarrier-level bridgeであり、R181A pump、R164/R170 instrument、記録、resetの同一装置統合は未完。
- `tools/verify_r187_m37_w_q1_bridge.py` でweak-link split、gap、lever arm、spectral projector、tilt hold、長時間static carrier、canonical mode変換を回帰。
- draft-77へ再生成する `paper.md`、`main.tex`、`paper.pdf`。

## draft-76のQ1定理階層整理

- R143を1段Q1 measurement instrument、R144を固定有限段逐次測定合成へ限定。
- R144の完全結果空間を $\{+1,-1,\varnothing\}^N$ とし、同軸反復、異軸逐次、段間状態受渡し、有限誤差和を定理責務として明示。
- 永久記録、補助逆計算、fresh-cell交換resetをR144から外し、無番号の実装強化系へ分離。
- Q1-2の達成ラベルと固定目標文言を維持し、Zeno残件をR140零傾斜Rabi対照とR144有限段測定の接続として整理。
- active verifierとCIにR144責務回帰を追加。
- draft-76へ再生成する `paper.md`、`main.tex`、`paper.pdf`。

## draft-75の模型階層・重複整理

- 現行模型階層をM54共通有効profile族、M37物理backend、M0 same-hardware統一目標へ整理。
- 旧M47をQ1 W型2モードprotocolの履歴IDへ降格し、現行模型表から分離。
- `PROJECT_STATUS.md` をprofile/backend/protocol/resultの完全依存台帳の唯一の正本とし、READMEと本文第1章を要約化。
- 付録HをW型2モードのパラメータ対応表へ縮約し、R181A/R135/R140の重複証明を削除。
- 第4章をR181B--R181DのQ2特殊化・適用章として明示。
- active verifierの旧M50ラベルと現行roadmapの旧R173参照を整理。
- 固定長期目標、達成ラベル、定理の数学的内容は変更しない。
- draft-75へ再生成する `paper.md`、`main.tex`、`paper.pdf`。

## draft-74の模型・matching統一

- M54をQ1/Q2/Q3共通signal--configuration親模型へ拡張し、M50をstatic-instrument profile、M55をspatial-moving profileへ吸収。
- R161をcurrent--traffic matchingへ一般化し、旧R183のmoving matchingをspatial特殊化として吸収。
- R162をgeneric directed-rate finite collisionとthermal detailed-balance特殊化へ一般化。
- 付録NをM54 spatial profileへ改名し、generic collision証明を付録Kへ集約。
- 検算器をM54 static/spatialとcommon matching/collisionへ再編。
- 固定長期目標と達成ラベルは変更しない。
- draft-74へ再生成する `paper.md`、`main.tex`、`paper.pdf`。

## draft-73の整合性修復

- R184のM37開始作用latch仕様と $L_\delta(\eta)\varepsilon_{\rm car}$ 評価。
- 一般有界有向率の有限collision-cell持上げ補題を付録Nへ自己完結に追加。
- R185の連続一様背景 $q_0=1/\ell$ と非零current数値回帰。
- M42退役メモ、現行依存台帳、README、PROJECT_STATUS、VALIDATION、CI、引用情報の同期。
- draft-73へ再生成した `paper.md`、`main.tex`、`paper.pdf`。

## draft-71の追加

- R182「M37静的W型スペクトル・空間トンネル縮約定理」と付録Gの完全証明。
- R182からR123有限環境純位相緩和へのW型系、およびR172--R174へのM42周期輸送系。
- \`tools/verify_m37_w_spectral_tunneling.py\`。
- Q3-3Cを達成、Q3-4Bを条件付き達成へ更新した状態表、誤差台帳、反証条件。
- draft-71へ同期した \`paper.md\`、\`main.tex\`、\`paper.pdf\`、引用情報、CI。

## draft-70の改訂

- Q3固定目標の新IDを本文、付録、現行研究メモ、統合原稿、TeX、PDFへ同期。
- 新Q3-2とQ3-6の未達課題、Q3-3CとQ3-4Bの部分達成境界を第7章、第8章、第9章へ追加。
- 新しいモデル、結果、数値検算器は追加していない。

## draft-69の追加

- `notes/m37_w_q1_unification_roadmap.md`
- `tools/verify_m37_w_q1_bridge.py`
## draft-89のR191測定主線圧縮

- `sections/A9_m54_setting_pre_paired_hopf_receiver.md` と `sections/A19_m54_drude_action_shell_bridge.md` を現行論文から外し、notesへ退役保存。
- Q1/Q2本文をR191主線へ同期し、Q2-2をA端R191→router→B端R191へ縮約。
- 退役検算器は `notes/retired_verifiers/` へ保存。
- `paper.md`、`main.tex`、`paper.pdf` は章別原稿から再生成する。

## draft-90の責務圧縮

- A8/A11/A12/A16とQ2-2証明をR191主線へ同期。
- `notes/superseded_r164_q1q2_measurement_role.md` と `notes/superseded_r180a_named_theorem.md` を追加。
- R181A/Hopf準備方程式は変更せず、理論変更を伴う準備模型再編は後続課題とする。
