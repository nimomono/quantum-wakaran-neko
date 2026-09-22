## draft-125：履歴メモと自動整合検査

- `notes/theory_lineage.md` を履歴入口として追加する。
- `notes/README.md`、`notes/superseded_result_index.md` と誤読しやすい退役メモ3件へ、歴史表現と最新正本を区別する注記を追加する。
- `tools/check_project_consistency.py` を追加し、`.github/workflows/verify.yml` の原稿構造jobから恒久実行する。
- `tools/test_validation_policy.py`、`VALIDATION_POLICY.md`、`tools/README.md`、`PROJECT_GUIDE.md` を新checkerの一般不変条件へ同期する。
- `PROJECT_STATUS.md`、`CHANGELOG.md`、`VALIDATION.md` を同期する。README、sections、physics verifier、paper生成物の理論内容は変更しない。

## draft-124：R164/R170作用殻測定経路のactive paper退役

- `sections/A12_common_action_shell_state_count.md` をactive section treeから削除し、R164の主要式・退役理由・履歴をnotesへ保存する。
- 付録KをR161/R162だけへ縮約し、静的作用殻Gibbs/free-energy、静的平方根特殊化、R170吸収pointer証明を削除する。
- 第2章、第3章、付録F、誤差・資源章と関連Q2/Q3節をM64/M65現行主線へ同期し、active `sections/` からR164/R170/R190測定経路の参照を除去する。
- `PROJECT_STATUS.md` の現行結果一覧からR164/R170/R190A--R190Cを外し、退役索引と研究メモへ移す。
- 固定目標ラベル、A/B/S判定、R135/R168、R161/R162、R179、R181D、R192とrequired physics verifierは維持する。

## draft-123：Q3旧R184率latch経路の退役

- `sections/A14_m54_spatial_moving_matching.md` からR184定理・証明・開始作用保持状態を外し、R161/R185付録へ縮約する。
- 第1・6・7・9章と付録Fの現行Q3説明からR184参照を外し、M64/R203A--R203D→R161/R185およびM64 finite-graph readoutへ統一する。
- `PROJECT_STATUS.md` の現行Q3結果一覧からR184を外し、`notes/superseded_r184_m37_rate_latch.md` と退役索引へ移す。
- `tools/verify_m54_spatial_matching.py` はR184専用latch検算を削除し、R161/R185 required回帰だけを維持する。旧コードはGit履歴を正本としnotesへ複製しない。
- 固定目標ラベル、M64/R203A--R203D、R161、R185、R124/R182/R125、A1/A2/B/S判定は変更しない。

## draft-122：現行依存グラフの同期

- `PROJECT_STATUS.md` の固定目標根拠欄を「達成判定で直接参照する結果・interface」に統一し、Q1-2/Q2-2の台帳差を解消する。
- `sections/A1_common_action_finite_basis.md`、第3章、第6章をM65/R181DおよびM64/R203主線へ同期する。
- `sections/A7_q3_completion_proofs.md` のR124/R125位置読出しをM64/R203D finite-graph tracerへ同期し、旧R184誤差を現行 $\varepsilon_{64,G}$ とregularizationへ置換する。
- 第7章の完全証明参照を付録Gへ、第8章のQ2根拠一覧を直接依存規約へ揃える。
- R164/R170/R184は本draftでは保持する。新模型、新結果ID、定理の退役、固定目標ラベル、強化目標状態、required physics verifierは変更しない。

## draft-121：固定目標の一試行物理interface原則への統一

- 固定目標の共通達成原則を「要求された現象・統計・逐次過程を、一試行内で明示的な物理interfaceを介して合成できること」へ統一する。
- 準備、全操作、測定、永久記録、試行間reset、物理clock、次試行renewalまでのjoint microscopic device/process統合はM0へ集約する。固定有限深さでは未使用補助自由度を順次使ってよく、解析上の状態・集団統計・Born重み・目標確率表の再注入はinterfaceの代用としない。
- Q2-1/Q2-3のM54→M65→R181D、Q2-2のA端M65→router→B端M65、Q3-4A/Q3-4B/Q3-5のM64 finite-graph tracer→位置読出しを既存結果だけで再監査し、6目標を達成へ更新する。
- Q2-4は資源効率・反復回数・総時間・精度を固定目標自身が要求する例外として条件付き達成を維持し、Q3-6とM0は未達のままとする。A1/A2/B1/B2/B3/Q2-2-Sの状態は変更しない。
- 新しい模型、結果ID、独立定理、physics verifierは追加しない。R180Cの仮定は共同分布の証明で実際に使う一試行有限順序付き操作へ整理し、full-cycle reset/clock条件をM0へ分離する。
- `tools/migrations/check_draft121_single_trial_fixed_goal_policy.py` で新ラベル、M0境界、旧full-device残件文言の再混入を検査し、生成物を再同期する。

## draft-120：R191/R193退役・M65 fixed-goal主線化

- Q1/Q2 fixed-goalの2結果selectorをM65/R204D--R204Fへ切り替え、R181D/R192/R179/R180A--R180Cの既存binary-selector interfaceへ接続する。
- Q1のR143/R144/R189B/R189CをM65へ同期し、R189A保持作用をM65へ直接入力する。有限2回Zenoの理想余裕 $1/4$ と達成ラベルは維持する。
- R191/R193のactive付録A20/A21をnotesへ移し、専用verifierも `notes/retired_verifiers/` へ移す。R191/R193の結果番号は再利用しない。
- Q2-1--Q2-4の達成ラベルは維持し、条件付き達成の残件をM65/R181D/record/resetの装置統合、Q2-4の一様装置族とR186ノイズ条件へ更新する。
- R186、M0、A/B/S判定、Q3主線、M65のHamiltonian/Brownian lift強化境界は変更しない。

## draft-119：M65 retirement-readiness整理

- M65の入力定義域を $A_\pm\ge0$、$A_++A_->0$ へ広げ、exact射影endpointを固定線形comparatorで直接処理できることを明記する。
- finite decision終了時にM65 generatorを閉じ、$X_T\in\{+,H,-\}$ をR112型recordへ写して $Y\in\{+,-,\varnothing\}$ を固定してからR181Dを開く有限latch interfaceを追加する。
- R204FにR189A→M65→R112 record→R181DのQ1 retirement-readiness合成と、routerを開かない空操作対照ではW2が自由Rabiを継続することを明記する。
- A12に残っていたR164--R190--R170旧Q1/Q2静的測定主線の残骸を代替作用殻研究線へ戻し、現行binary-selector主線と誤差を重複計上しない。
- R191/R193、A20/A21、R143/R144/R189B/R189Cの現行fixed-goal witness、required verifier、達成ラベルは変更しない。退役そのものは次の独立PRへ分離する。

## draft-117：M65 canonical open selector正式昇格・R181D interface一般化

- M65をreplacement candidateからQ1/Q2二結果射影用のcanonical open selector modelへ正式昇格する。正本発展則は保持済み二作用を線形rateへ入れる3状態連続時間Markov過程とし、Hamiltonian chamber/Brownian縮約は強化実現へ分離する。
- R181DをR191固有の節点契約から共通binary selector contractへ一般化し、R192、R179、R180A/R180Cもselector内部物理から切り離す。
- M65のexact open lawとfinite-time Born boundをrequired科学検算へ昇格し、phase-volume partition、matched conductance、Brownian reductionだけをcandidate検算に残す。
- R191/R193は本draftでは退役させず、Q1/Q2 fixed-goalの現行証人、A20/A21、required verifier、達成ラベルを維持する。M65へのfixed-goal実装切替は後続変更へ分離する。
- R186の指数mode additive-noise/precision障害、M0未達、A1/A2/B/S判定は変更しない。

## draft-116：開放ミクロ方程式の標準表記

- 「採用開放方程式」「採用open model」のように「採用」を名詞修飾語として使う現行表記を廃止する。
- Hamiltonian浴などの上位模型から導出せず、方程式自体をミクロ模型の基本発展則として置く場合は、「開放ミクロ方程式として直接定める」を標準の文章表現、「直接定めた開放ミクロ方程式」を標準の名詞表現とする。
- Hamiltonian浴から縮約導出した場合は「Hamiltonian浴から導出した開放方程式」と区別する。
- TERMINOLOGY、PROJECT_STATUS、PROJECT_STANCE、PROJECT_GUIDE、ENHANCEMENT_TARGETS、active sections、simulation規約、現行研究noteを同期する。
- 固定目標、達成ラベル、M0判定、A1/A2/B/S状態、模型・結果・数式・physics verifierは変更しない。
- 過去CHANGELOG、過去draft記録、superseded notesは歴史記録として書き換えない。

## draft-115：M0 open microscopic device 判定への一般化

- M0の達成条件からHamiltonian無限浴への持上げを外し、PROJECT_GUIDE 4.5.2を満たす採用openミクロ方程式を許す。
- M0を、Q1/Q2/Q3の主要自由度、物理接続端、準備、操作、測定、記録、reset、clockを一つのjoint microscopic device/processと共通反復周期へ統合する横断目標として再定義する。
- A1との差はHamiltonian性ではなく統合範囲に置き、全A1達成だけではM0達成としない。規模依存問題には同一architectureの一様装置族と一つのparameter familyを許す。
- Hamiltonian無限浴への持上げ、共通単一bath化、有限浴化、有限閉鎖Hamiltonian化、完全周期の微視的熱力学をM0より強い横断強化へ分離する。
- PROJECT_STATUS、PROJECT_GUIDE、PROJECT_STANCE、ENHANCEMENT_TARGETS、第1・2・3・6章と関連付録、現行notesを新基準へ同期し、PR固有の旧文言回帰は `tools/migrations/check_draft115_m0_open_device.py` で検査する。
- M0は未達のまま。固定目標・達成ラベル・A/B/S判定、R191/R193主線、M65/R204 candidate、既存物理定理とphysics verifierは変更しない。

## draft-114：M65 phase-volume projective instrument置換候補

- M65/R204A--R204Fを、R191/R193をまだ置換しないpromotion-ready replacement candidateとして追加する。
- R203Bと共通のphase-volume Jacobianを二結果射影作用へ接続し、固定chamber--neck--hubのcapacity/conductance matching、Hamiltonian--Brownian縮約契約、有限時間Born読出し、R181D受渡し、Q1接続、Q2-4 polynomial readout-time条件を整理する。
- R204Cのfull HamiltonianからBrownian chamber networkへの有限誤差縮約をpromotion gateとして残し、R186の指数mode additive-noise/precision障害は未解決のまま維持する。
- 現行Q1/Q2 fixed-goal主線、達成ラベル、R191/R193 required verifier、R181D/R192/R179の定理文、M64 Q3主線は変更しない。

## draft-113：M64昇格後の整合cleanup

- A25のconfiguration profile割当と $\varepsilon_{\rm prep}^{W_1}$ 定義を整合させる。
- ENHANCEMENT_TARGETSでQ3-1-A1とQ3-2-A1の候補責務を分離し、判定は変更しない。
- PROJECT_STATUSとnotes/READMEの旧主線に関する現在形表現だけを修正し、過去draft履歴は保持する。
- M64/R203A--R203D、R161/R185の理論内容とrequired verifierは変更しない。
- paper.md、main.tex、paper.pdf を修正後のsection treeから再生成する。

## draft-112：M64正式昇格・M60/M61退役

- M64/R203A--R203DをQ3の現行open modelへ昇格し、M37/R86 signal、R161/R185、R124/R182/R125位置読出しへ正本接続する。
- A22--A24のM60/M61旧Hamiltonian実装を現行section treeから削除し、Git履歴・退役索引へ保存する。
- M64の6本のverifierをrequiredへ昇格し、M60/M61専用verifierを退役する。
- README、PROJECT_STATUS、ENHANCEMENT_TARGETS、第0・1・2・6--9章、notes、simulation registry、VALIDATIONをM64主線へ同期する。
- fixed-goal達成ラベルとA1/A2判定は変更しない。
- paper.md、main.tex、paper.pdf を新しいsection treeから再生成する。

## draft-111：M64 promotion bridge完成

- R203AのregularizationをR185と共通の $\rho_\delta,J_\delta,v_\delta$ へ揃え、R203Bにfinite-time initial tracer preparationとmean-flow tracking boundを追加した。
- R203Cの正本をcanonical overdamped open SDEへ単純化し、ideal regularized diffusionへの有限時間process reductionを明示した。process reduction errorとR185 Newton residualは別々に管理する。
- R203Dを一般finite graphへ拡張し、local phase-volume/current/activityからR161 rateを構成した。1次元特殊化はR185と一致し、R125の2頂点再結合器へも接続した。
- M64をpromotion-ready replacement candidateとしたが、M61/M60主線、Q3達成ラベル、A1/A2判定、required verifierは本draftでは変更しない。
- `verify_m64_preparation_tracking.py` と `verify_m64_graph_r161.py` をcandidate checksへ追加した。A2 direct simulationはpromotion条件へ混ぜない。

## draft-110：M63退役

- `sections/A25_m63_topological_reservoir_q3_micro_model.md`、6本のM63 candidate checks、`simulations/m63/` を現行treeから削除し、M63/R202A--R202Fをactive candidateから退役する。
- M64付録を `sections/A26_m64_three_entity_open_q3_model.md` から `sections/A25_m64_three_entity_open_q3_model.md` へ繰り上げ、付録番号をZからYへ同期する。
- README、第0・1・2・6--9章、ENHANCEMENT_TARGETS、PROJECT_STATUS、VALIDATION、simulations registry、R161実現同値メモからM63のactive参照を除去する。
- M61/M60 fixed-goal主線、Q3達成ラベル、A1/A2判定、required verifier、M64 candidate判定は変更しない。
- `paper.md`、`main.tex`、`paper.pdf` を再生成する。
## draft-109：M64 三実体open-Q3置換候補

- `sections/A26_m64_three_entity_open_q3_model.md` を追加し、M64/R203A--R203DをM60/M61/M63をまだ置換しないactive replacement candidateとして収録する。
- M64の物理実体をM37型coherent signal、独立tracer、signal-driven moving thermal reservoirの三つへ限定し、density free energy、reservoir mean flow、friction/noiseを同じ環境の責務として整理する。
- `verify_m64_reservoir_partition.py`、`verify_m64_overdamped_reduction.py`、`verify_m64_r161_finite_volume.py` をcandidate checksとして追加する。
- `simulations/m64/README.md` にM37 signal、mean-flow relaxation、tracer Langevin SDEを同一parameter setで直接積分するA2計画を追加する。
- README、第0・1・2・6--9章、PROJECT_STATUS、ENHANCEMENT_TARGETS、VALIDATION、simulations registry、R161実現同値メモをM64 candidateへ同期する。
- M61/M60 fixed-goal主線、M63 active candidate、Q3達成ラベル、A1/A2判定、required/candidate verifierは変更しない。旧Q3模型の退役は次PRへ分離する。
- `paper.md`、`main.tex`、`paper.pdf` を再生成する。

## draft-108：M62退役・M63 current-transport具体化

- M63正本を `sections/A25_m63_topological_reservoir_q3_micro_model.md` へ移し、旧M62付録と旧A26を削除する。
- M62の3 candidate checksと `simulations/m62/` を削除し、過去の探索はGit履歴・過去draft記録へ委ねる。
- M63 current transport用に `verify_m63_current_dictionary.py`、`verify_m63_scatterer_tracking.py`、`verify_m63_relative_gle.py` を追加し、既存canonical/partition/osmotic checksを新定義へ同期する。
- README、第0・1・2・6--9章、ENHANCEMENT_TARGETS、PROJECT_STATUS、VALIDATION、simulations registry、R161実現同値メモを新R202E責務へ同期する。
- M61/M60 fixed-goal主線、required検算、Q3達成ラベルは変更しない。
- `paper.md`、`main.tex`、`paper.pdf` を再生成する。

## draft-107：M63 topological-reservoir 一成分Hamiltonian Q3統合候補

- `sections/A26_m63_topological_reservoir_q3_micro_model.md` を追加し、M63/R202A--R202Fをactive single-field strengtheningとして収録する。
- M62/R201は `sections/A25_m62_single_field_q3_micro_model.md` にhistorical candidateとして保存し、既存candidate checks・simulation witnessも削除しない。
- `tools/candidate_checks/verify_m63_canonical_filter_bank.py`、`verify_m63_topological_partition.py`、`verify_m63_osmotic_width.py` をcandidate検算として追加する。
- `simulations/m63/README.md` にfull trajectoryで検査すべきosmotic force、signal backreaction、GLE/FDT、current port、PN hopping--R161を記録する。
- README、PROJECT_STATUS、ENHANCEMENT_TARGETS、第0・1・2・6--9章、VALIDATION、CHANGELOGをM63 active candidate責務へ同期する。
- 固定Q3-1/Q3-2達成、A1部分達成、A2未監査、M61/M60 required主線は変更しない。
- `paper.md`、`main.tex`、`paper.pdf` を再生成する。

## validation-architecture-v2：検算アーキテクチャ

- `VALIDATION_POLICY.md` — 恒久検算・candidate・migration・quality lintの責務と検算作成ルールの正本。
- `tools/check_source.py` — 理論番号に依存しない構造契約だけを検査。
- `tools/run_physics_checks.py` — required科学検算を全件実行して集約報告。
- `tools/candidate_checks/README.md` — 研究中の非blocking科学検算の配置規約。
- `tools/migrations/README.md` — PR固有の一時移行検査の配置規約。
- `tools/check_generated.py` — 生成物同期専用。
- `tools/check_latex_semantics.py` — 未解決参照・欠落文字・fatal error等のLaTeX hard error専用。
- `tools/test_validation_policy.py` — 上記責務境界そのものの自己回帰検査。
- `.github/workflows/verify.yml` — read-onlyの3ジョブ構成を維持し、論文生成後の同期・semantic・lintを独立報告。

## draft-106：M62 一成分Hamiltonian lattice Q3統合候補

- `sections/A25_m62_single_field_q3_micro_model.md` を追加し、M62/R201A--R201FをM61/M60を置換しないQ3 single-field strengtheningとして収録する。
- `tools/candidate_checks/verify_m62_spectral_window.py`、`verify_m62_weighted_shell.py`、`verify_m62_time_window.py` をcandidate検算として追加する。
- `simulations/m62/README.md` と `simulations/m62/witness_summary.json` に探索的spectrum、exchange、memory、prethermal、normal-form時間尺度を集約し、A2未監査境界を明示する。
- README、PROJECT_STATUS、ENHANCEMENT_TARGETS、第0・1・2・6--9章、VALIDATION、CHANGELOGをM62 candidate責務へ同期する。
- 固定Q3-1/Q3-2達成、A1部分達成、A2未監査、M61/M60 required主線は変更しない。
- `paper.md`、`main.tex`、`paper.pdf` を再生成する。

## draft-105：M61 単一Hamiltonian Q3親模型

- `sections/A24_m61_single_hamiltonian_micro_model.md` を追加し、M61/R200A--R200C/R200をM60の下位Hamiltonian親層として正本化する。
- `tools/verify_m61_single_hamiltonian.py` をrequired、`tools/candidate_checks/verify_m61_parameter_window.py` をcandidateとして追加する。
- README、PROJECT_STATUS、ENHANCEMENT_TARGETS、第0・1・6・8・9章、A22/A23、VALIDATION、CHANGELOGをM61→M60階層へ同期する。
- 既存MANIFESTの章一覧から抜けていたA23を復旧し、新規A24を追加する。
- `paper.md`、`main.tex`、`paper.pdf` を再生成する。

## draft-104：M60 post-merge consistency cleanup

- 第0・2・6--9章の現行M57表現をM60へ同期し、履歴節・退役メモのM57/M59は保持する。
- 第6章のstate-count責務をR198A--R198D/R197Aへ、第7・8章のtransport誤差名をM60へ同期する。
- VALIDATION/MANIFESTのdraft-103記録をvalidation-architecture-v2のrequired/candidate分離へ同期する。
- notesの「現行M57」記述をM60へ更新し、PR固有migration検査は最終headに残さない。
- `paper.md`、`main.tex`、`paper.pdf` を再生成する。

## draft-103：M60 Duffing shell＋統一二成分chiral媒体

- `sections/A23_q3_common_micro_model.md` をM60正本へ更新し、実2-mode Duffing shellを維持したまま二保存action reservoirとdual ballistic waveguideを同一chiral媒体のcore/leadへ統合する。
- `sections/A22_m57_dual_tl_tracer_microphysics.md` をM60 transport reductionへ更新し、R195A・R196A--R196Cの機械的縮約を維持しつつR196Aの入力をM60 ballistic leadへ差し替える。
- R199Aは `tools/verify_q3_common_micro_model.py` のrequired検算、R199Bは `tools/candidate_checks/verify_chiral_shell_response.py` のcandidate検算として分離し、README、PROJECT_STATUS、ENHANCEMENT_TARGETS、第1・6--9章、VALIDATION、CHANGELOGを同期する。
- `paper.md`、`main.tex`、`paper.pdf` を再生成する。

## draft-102：M59 Duffing shell＋二保存action reservoir

- `sections/A23_q3_common_micro_model.md` をM59正本として全面改訂し、旧M58の直接thermostatをR198A--R198DのDuffing/action-reservoir持上げへ置換する。
- `tools/verify_q3_common_micro_model.py` をR198A--R198Dの係数、finite-$N$、exchange symmetry、parameter-window検算へ置換する。
- README、第1・6・8章、A22、PROJECT_STATUS、ENHANCEMENT_TARGETS、VALIDATION、CHANGELOG、source checksを同期する。
- `paper.md`、`main.tex`、`paper.pdf` を再生成する。

## draft-101：M58 Q3共通ミクロ模型とR197統合

- `sections/A23_q3_common_micro_model.md` を追加し、R197A--R197CとR197でQ3-1/Q3-2を同一M58過程の異なる周辺縮約として統合する。
- `tools/verify_q3_common_micro_model.py` を追加し、M37--M57辞書、shell分配関数・平均力・二乗平均、finite-width補正、共通weak scaling、時間尺度窓を検算する。
- A12/A22、第0・1・6・8・9章、README、PROJECT_STATUS、ENHANCEMENT_TARGETS、VALIDATION、CHANGELOGと生成物を同期する。

## draft-100：R161 canonical Markov path law

- R161へ、固定有限時間・有限状態・有界総hazard下の非爆発càdlàg Markov経路法則の存在・一意性を吸収した。
- R185の前向き・Bayes後向き平均微分はR161 lawへ直接依存させ、Q3-2根拠一覧からR162を除外した。
- R162は同じR161 lawの独立Poisson-random-measureによるoptional pathwise realizationへ責務を縮約した。結果IDは維持する。
- 固定目標、達成ラベル、M57/R195A・R196A--R196C、R184、R185の数式内容は変更していない。

## draft-98のM57 ballistic moving-bath正本化

- draft-95のthermalizing dual-TL M57を置換し、dual ballistic TL、moving bath-frame carrier、平衡oscillator bath、局在tracerを現行Q3ミクロ物理層とする。
- R195Aをchiral current恒等式まで強化し、新結果R196A--R196Cを追加する。旧R195B--R195DはGit履歴・退役索引へ保存する。
- `sections/A22_m57_dual_tl_tracer_microphysics.md`
- `sections/A23_q3_common_micro_model.md` を全面更新し、`tools/verify_m57_tl_tracer.py` を `tools/verify_m57_ballistic_tracer.py` へ置換する。
- README、PROJECT_STATUS、第0・1・2・6--9章、研究メモ、参考文献、生成物を新M57へ同期する。

## draft-97の強化目標・Bell前提・開放雑音方針同期

- `ENHANCEMENT_TARGETS.md` をA1/A2、Q1/Q2のB1/B2/B3、Q2-2-Sの正本として管理文書体系へ正式に追加する。
- Q2-2固定目標を特定のBell前提違反に限定しない一般監査へ改め、現行R180Cを非空間分離逐次証人として維持する。
- 採用開放SDEと理想白色雑音をA1/A2で許し、B2/B3では有限帯域雑音の実験可能領域を監査する。
- README、PROJECT_STANCE、PROJECT_GUIDE、PROJECT_STATUS、第0・1・5・8・9章、simulation規約、構造検査、用語lint、生成物を同期する。

# 現行パッケージ一覧

## draft-95のM57 dual-TL tracer正本化

- M57/R195A--R195DをQ3の現行ミクロ物理層へ採用し、R162をideal open-jump reference、R184を補助結果、M56を代替研究線へ整理する。
- `sections/A22_m57_dual_tl_tracer_microphysics.md` と `tools/verify_m57_tl_tracer.py` を追加する。
- `notes/superseded_q3_poisson_microphysics.md` に旧Poisson存在論の責務変更を記録する。
- `paper.md`、`main.tex`、`paper.pdf` はdraft-95正本から再生成する。

## draft-94のR161共通数学核整理

- Q1型局所正準信号＋Q2型辺結合からQ3の $(\pi,j)$ へ接続する構造を第1・2・6章、付録K・N、概要、結論へ明示する。
- R161の活動量--親和力等価表示、生成子同値、固定有限時間の全変動距離上界を追加する。
- `notes/r161_q1_q2_q3_realization_equivalence.md` を追加し、空間化Q1模型、現行M54/R162、M56等を同じR161核の実現として比較する規約を保存する。
- `tools/verify_m54_spatial_matching.py` に無結合局所モードの零辺流と活動量--親和力恒等式の検算を追加する。
- `paper.md`、`main.tex`、`paper.pdf` は章別正本から再生成する。

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
- `sections/A8_m47_w2_parameter_dictionary.md`
- `sections/A10_q2_common_bath_composition.md`
- `sections/A11_common_collision_bath_thermodynamics.md`
- `sections/A13_m54_radial_stabilizer.md`
- `sections/A14_m54_spatial_moving_matching.md`
- `sections/A15_m54_uniform_register.md`
- `sections/A16_m54_projector_tree_receiver.md`
- `sections/A17_m54_uniform_supply.md`
- `sections/A18_m54_projective_robustness.md`
- `sections/A20_m54_brownian_macrospin_projective_instrument.md`
- `sections/A21_q1_r193_macrospin_bridge.md`
- `sections/A25_m64_three_entity_open_q3_model.md`
- `sections/90_references.md`

## 論文外の研究メモ

- `notes/README.md`
- `notes/r161_q1_q2_q3_realization_equivalence.md`
- `notes/brownian_spin_q1_q3_unification.md`
- `notes/superseded_q3_poisson_microphysics.md`
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
- `ENHANCEMENT_TARGETS.md`
- `CHANGELOG.md`
- `VALIDATION.md`
- `MANIFEST.md`
- `LICENSE_STATUS.md`
- `CITATION.cff`
- `references.bib`
- `tools/build_paper.py`
- `tools/check_generated.py`
- `tools/check_latex_semantics.py`
- `tools/check_source.py`
- `tools/check_terminology.py`
- `tools/lint_typeset.py`
- `tools/paper_source.py`
- `tools/run_physics_checks.py`
- `tools/test_validation_policy.py`
- `tools/template.tex`
- `tools/verify_common_canonical_control.py`
- `tools/verify_common_matching_open_jump.py`
- `tools/verify_envelope_reduction.py`
- `tools/verify_m37_w_q1_bridge.py`
- `tools/verify_m37_w_spectral_tunneling.py`
- `tools/verify_m47_action_shell_origin.py`
- `tools/verify_m47_q1_instrument.py`
- `tools/verify_m54_q2_composition.py`
- `tools/verify_m54_spatial_matching.py`
- `tools/verify_m64_current_dictionary.py`
- `tools/verify_m64_graph_r161.py`
- `tools/verify_m64_overdamped_reduction.py`
- `tools/verify_m64_preparation_tracking.py`
- `tools/verify_m64_r161_finite_volume.py`
- `tools/verify_m64_reservoir_partition.py`
- `tools/verify_phase_correlation.py`
- `tools/verify_q1_live_zeno.py`
- `tools/verify_q1_r193_macrospin_bridge.py`
- `tools/verify_q1xq1_common_bath.py`
- `tools/verify_q2_shell_and_locality.py`
- `tools/verify_q3_completion.py`
- `tools/verify_r161_path_law.py`
- `tools/verify_r179_m54_supply.py`
- `tools/verify_r180_m54_receiver.py`
- `tools/verify_r181d_projector_tree.py`
- `tools/verify_r186_m54_projective_robustness.py`
- `tools/verify_r187_m37_w_q1_bridge.py`
- `tools/verify_r191_macrospin.py`
- `tools/verify_r192_radial_stabilizer.py`
- `tools/verify_r194_brownian_spin_nelson.py`
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

## draft-91のR193 Q1直接decision接続

- 付録U `sections/A21_q1_r193_macrospin_bridge.md` を追加し、R189A保持座標からR191 macrospin decision energyへのQ1専用直接Hamiltonian接続R193を正本化。
- `tools/verify_q1_r193_macrospin_bridge.py` を追加し、吸引域境界、誤差係数、dispatcher、未使用保持対境界を検算。
- Q1主線を `M37 W2 -> R189A -> R193 -> R191 -> R181D` へ同期し、Q2の一般R191 transducer契約は維持。
- `paper.md`、`main.tex`、`paper.pdf` は章別原稿から再生成する。


## draft-99のQ3 spine cleanup

- 現行Q3主線を `M37/M54 signal -> R195A -> R196A--R196C -> R161 -> R185` として表記同期し、R162はideal referenceへ限定する。
- 付録Nの存在論をR161/R185参照過程へ縮約し、退役R195D/R170の現行依存残骸を除去する。
- 歴史記録、notes、退役索引の旧模型記述は保存する。
