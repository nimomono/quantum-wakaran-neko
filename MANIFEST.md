# 現行パッケージ一覧

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
- `tools/verify_m47_hopf_preparation.py`
- `tools/verify_common_matching_collision.py`
- `tools/verify_m47_action_shell_origin.py`
- `tools/verify_q2_shell_and_locality.py`
- `tools/verify_r180_m54_receiver.py`
- `tools/verify_r180_bell_cycle.py`
- `tools/verify_phase_correlation.py`
- `tools/verify_q1xq1_common_bath.py`
- `tools/verify_m54_static_instrument.py`
- `tools/verify_r181a_template_port.py`
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