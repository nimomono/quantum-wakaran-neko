# 置換・退役結果索引

## draft-127で退役したR192とQ2逐次terminal route

M66/R205--R206をQ2-1/Q2-3/Q2-4のterminal readout正本へ昇格したため、旧binary treeで非終端branchの作用下限を回復していたR192はfixed-goal責務を失った。R192の数学結果を反証したものではなく、one-shot multi-outcome samplerによって必要な中間branch自体が消えたための退役である。M65/R181D/R179は別責務でactiveのまま残る。

| 結果 | 旧用途 | 現行の扱い | 保存先 |
|---|---|---|---|
| R192 | Q2-4逐次binary treeの非終端選択成分を次段M65感度域へ戻す方向不変作用安定化 | M66/R206 one-shot terminal samplerへ置換しactive theoremから退役。結果IDは再利用しない | `superseded_r192_radial_stabilizer.md`、`superseded_q2_sequential_terminal_readout.md`、draft-127直前Git履歴 |

旧Q2-1/Q2-3/Q2-4のM65→R181D→必要時R192というterminal treeの経路履歴は `superseded_q2_sequential_terminal_readout.md` に保存する。

この索引は退役時点の置換関係も履歴として保持するため、古い行の「現行の扱い」「置換先」がさらに後のdraftで退役している場合がある。2026-09-22時点の主要な現行因果鎖は `theory_lineage.md`、現行結果の運用状態は `PROJECT_STATUS.md` を参照する。退役行の第1列は退役した結果IDだけを記し、現行結果IDを退役項目の識別子として再利用しない。

## draft-124でactive paperから退役した作用殻測定経路

Q1/Q2の結果形成がM65/R181D、Q3の位置形成・輸送がM64/R203A--R203Dへ一本化されたため、作用殻状態数R164と静的吸収pointer R170をactive paperから退役した。R190A--R190Cはdraft-89以後すでに退役済みであり、これにより旧作用殻測定経路全体がnotes/Git履歴だけに残る。いずれも反証ではなく責務置換であり、結果番号は再利用しない。

| 結果 | 旧用途 | 現行の扱い | 保存先 |
|---|---|---|---|
| R164 | 排他的2作用殻のLiouville状態数から線形Born型重みを得る | Q1/Q2はM65、Q3はM64/R203へ置換しactive theoremから退役 | `superseded_r164_q1q2_measurement_role.md`、draft-49以後のGit履歴 |
| R170 | 静的選択分布を吸収pointerへ写して有限後段窓へ固定する | M65のfinite decision/recordへ置換しactive proofから退役 | `superseded_r190_r170_measurement_path.md`、draft-82以後のGit履歴 |
| R190A--R190C | 2作用LC殻Drude混合と静的平方根kernelの物理接続 | draft-89で既に退役。draft-124でactive paper中の代替経路参照も除去 | `superseded_r190_r170_measurement_path.md`、`superseded_A19_drude_action_shell_bridge.md` |

旧付録Lの完全証明と旧付録Kの静的特殊化・R170証明はGit履歴を正本とする。


## draft-123で退役したR184 Q3旧率latch

M64/R203A--R203DがM37 signalからcontinuous/finite-graph tracerとR161へ直接接続する現行Q3主線を閉じたため、R184をactive paperから退役した。これはR184の有限時間Lipschitz評価を反証したものではなく、旧M37→M54 spatial rate-latch bridgeの責務が現行主線で不要になったための退役である。結果番号は再利用しない。

| 結果 | 旧用途 | 現行の扱い | 保存先 |
|---|---|---|---|
| R184 | M37開始作用 $S_{\rm ref}$ を保持し、旧M54 spatial rateとの差を $L_\delta\varepsilon_{\rm car}$ で評価 | M64/R203A--R203D→R161/R185へ置換。active theorem・proof・required verifier責務から外す | `superseded_r184_m37_rate_latch.md`、draft-73および退役直前Git履歴 |

R184専用数値コードは研究メモへ複製せず、退役直前の `tools/verify_m54_spatial_matching.py` をGit履歴から参照する。


## draft-120で退役したR191/R193測定経路

M65/R204D--R204FをQ1/Q2 fixed-goalのcanonical open selectorへ採用したため、R191/R193を現行因果鎖から外した。これはR191のBrownian macrospin構成またはR193のHamiltonian bridgeを反証したものではなく、より短い共通open-selector主線へ責務を吸収したための退役である。結果番号は再利用しない。

| 結果 | 旧用途 | 現行の扱い | 保存先 |
|---|---|---|---|
| R191 | Brownian macrospinによるQ1/Q2共通2結果射影読出し | M65/R204A、R204D--R204Fの3状態open selectorへ置換 | `superseded_r191_brownian_macrospin_projective_instrument.md`、draft-88--draft-91 Git履歴 |
| R193 | R189A保持作用からR191 macrospin decision energyへのQ1専用直接接続 | R189A保持作用をM65へ直接入力するR204F接続へ置換 | `superseded_r193_q1_macrospin_bridge.md`、draft-91 Git履歴 |

専用数値検算は `notes/retired_verifiers/verify_r191_macrospin.py` と `verify_q1_r193_macrospin_bridge.py` に保存する。

この表は現行本文から外した結果への最小索引である。数式と証明は重複掲載せず、Git履歴と個別メモを正本とする。

## 退役した固定目標

| 旧目標 | 旧用途 | 現行の扱い | 参照先 |
|---|---|---|---|
| 旧Q2-3「有限回路の機能的再現」 | 任意の固定有限回路を $2^n$ 直接モード担体で有限合成し、末尾だけで読出す | 固定目標から削除。3量子ビット型二段ゲート合成を新Q2-3とし、直接モード構成はQ2-4の候補技術として資源監査を継続 | draft-60の本文、Git履歴、現行Q2-4 |
| 旧Q2-5「自律非平衡計算と平衡化運命の決定不能性」 | 白石--松本型の停止問題埋込みを局所古典開放系へ移す | 固定目標から削除し、量子出力サンプリングとは独立の研究線として保存。Q2-5のIDは再利用しない | draft-60の本文、Git履歴 |

退役は反証を意味しない。現在の固定目標と混同せず、必要な場合だけ独立研究線として再開する。


### draft-95 M57 thermalizing-TL定式化

| 結果 | 旧用途 | 現行の扱い | 参照先 |
|---|---|---|---|
| R195B | pinned weakly-anharmonic dual open TLのslaving・mixing・force correlation | draft-98で退役。ballistic moving-reflector定理R196Aへ置換 | draft-95 Git履歴、付録V |
| R195C | drifting-Gibbs、TLへのGreen--Kubo/FDT、Kramers/Lifson--Jackson matching | draft-98で退役。moving equilibrium bath・GLE・homogenizationのR196Bへ置換 | draft-95 Git履歴、付録V |
| R195D | $A=2r$ のKramers fluxからR161へ持上げ | draft-98で退役。$A=4\beta_*(r)$ のmetastable lift R196Cへ置換 | draft-95 Git履歴、付録V |

R195Aのchiral作用・状態数恒等式は保持し、signal current velocityまで強化する。結果番号は再利用しない。

| 結果 | 旧用途 | 現行の扱い | 参照先 |
|---|---|---|---|
| R171 | M51の共通開放ray準備 | 旧R181Aへ吸収後、draft-90で状態方向準備ごと退役 | `superseded_separate_m51_m52_m53_models.md`、`superseded_r181a_template_port_preparation.md` |
| R181A | 共通初期種から指定状態方向への開放準備と作用安定化 | 状態方向準備は現行固定目標から退役。動径部分は一時R192へ切り出されたが、draft-127でR192も責務消滅により退役 | `superseded_r181a_template_port_preparation.md`、`superseded_r192_radial_stabilizer.md` |
| R176A--R176C | M52のtensor-lift、永続gate、末端instrument | tensor-lift/gateはM54/R181B--R181Cへ、Q2-1/Q2-3 terminal readoutはM66/R206へ吸収。R181DはQ2-2等の逐次handoffに残る | `superseded_separate_m51_m52_m53_models.md`、第2章・第4章 |
| R178A--R178C | M53のsector gate、projector filter、逐次sampler | M54/R181C--R181Dへ吸収 | `superseded_separate_m51_m52_m53_models.md`、付録O・P |
| R178E--R178F | fixed-volume tapeと滑らかなaperture | Q1/Q2共通のR170選択・固定＋R181D段階的射影選別を採用したため現行因果鎖から退役 | `superseded_r178_aperture_sampler.md`、draft-67のGit履歴 |
| R145 | M51/R171のM47 W型2モード特殊化 | R181Aから従う無番号の系へ変更 | 付録H |
| R70--R72、R77、R78、R91 | M35作用区間によるBorn型長期頻度 | 確率源として退役。M50/R164へ一本化 | `superseded_m35_born_sampler.md` |
| R107--R111、R121 | M41 Bell周期 | M48/R151--R156、R166、R170へ置換 | `superseded_m41_bell_cycle.md` |
| R147、R153、R155 | 独立M48 setting-pre paired-Hopf Bell周期 | M54の実際の1試行末端信号を受けるR180A--R180Cへ置換 | `superseded_independent_m48_bell_protocol.md`、draft-65のGit履歴 |
| R113--R118 | 旧M42連続粒子位置閉包 | 退役。draft-58でM42/R172--R174、draft-72でM55/R183--R185を経て、draft-74でM54 spatial/R161/R184/R185へ統合 | `superseded_m42_continuous_particle_position.md`、Git履歴 |
| R172--R174 | draft-58再定義M42のQ3局在トークン輸送 | draft-72でM55/R183--R185へ移行し、draft-74でM54 spatial/R161/R184/R185へ再統合 | `superseded_m42_continuous_particle_position.md`、旧付録NのGit履歴 |
| R183 | M55 spatial moving-matching不変性 | 一般化R161のM54 spatial-moving特殊化へ吸収。定理内容は撤回せず、独立結果IDだけを退役 | `superseded_separate_m50_m55_models.md`、R161、付録K・N |
| R127--R129 | M45開放準臨界準備 | Q1--Q3と独立の研究線 | `independent_m45_open_quasicritical_preparation.md` |
| R130--R132 | M46のcapacity・半減衰・主モード計算 | 現行本文から退役。再検討用の有限次元計算 | `rejected_m46_current_transducer.md` |
| R133、R134 | M46 current恒等式と条件付きNelson恒等式 | 現行因果鎖では不採用 | `rejected_m46_current_transducer.md` |
| R137、R138 | M47旧連続matching保存と逆設計 | R161/R162/R170の操作面再平衡化へ置換 | `superseded_m42_continuous_particle_position.md` |
| R150 | 抽象matching下のBell有限誤差系 | R155証明内の統計補題へ吸収 | Git履歴 |
| R152 | M48局所matching生成子 | R161の $m=2$、$\Psi=\Phi$ 特殊化へ吸収 | R161、R162 |
| R165 | M49中央4枝とM35作用区間の同値性 | M35側を退役し、M49中央4枝をR164の直接特殊化としてR159入力準備節に保持 | R159、R164 |
| R159 | M49の入力準備、同期CNOT、固定有限共同入力--出力統計 | 固定benchmarkの代数は撤回しないが、4モード共同担体を現行Q2-1に採用せず退役 | `superseded_m49_joint_bath_cnot_provider.md`、draft-62のGit履歴 |
| R160 | M49固定singletからM48へのsetting-free同一register受渡し | M49の退役とともに現行模型間接続から外した。Q2-2はM48内部seedで独立に維持 | `superseded_m49_joint_bath_cnot_provider.md`、draft-62のGit履歴 |
| R175 | draft-63 M52の有限coherent経路和代数 | R181Cのunitary診断展開へ吸収。経路限定設計と独立の物理分岐器を主結果鎖から外す | `superseded_m52_path_only_design.md`、draft-63のGit履歴 |
| R169 | 固定全作用高階数読出し | 安全事象を含む一般ray平均定理R168へ吸収 | R168 |
| R89 | 隣接2モード回路による有限unitary合成 | R112の有限合成節へ吸収 | R112、付録A |
| R90、R97--R99 | 有限時計、比較・無反応、結果別SWAP、記録・逆計算 | R112の制御・比較・記録回路へ吸収 | R112、付録A |
| R83--R85、R87、R88 | M37の局所包絡、生成子誤差、作用比診断 | R86の節と有限基底分布系へ吸収 | R86、付録E |
| R136、R141 | W型占有振動と傾斜保持 | W型2モード制御定理の節へ吸収 | R140、付録B・H |
| R139、R167 | 2次元Bloch縮約とM37第2モーメント持上げ | 共通信号集団の正確・有限誤差輸送へ吸収 | R135、付録F |
| R142 | W型有限コントラスト読出し | M47読出し・状態更新定理の補題へ吸収 | R143、付録B |
| R104、R105、R106 | 4モード担体の操作代数、CNOT流、有限時間安定性と資源 | R112の4モード/CNOT特殊化へ吸収 | R112、付録C |
| R157、R158 | M49入力準備と担体・bath・粒子位置の同期CNOT | R159の入力準備節・同期CNOT節へ吸収 | R159、付録C |
| R163 | 粗視化粒子位置過程の経路確率比、積分ゆらぎ関係、相対有効仕事 | R161・R162から従う無番号の粗視化経路熱力学系へ変更 | 第2章、付録K |
| R146 | 積bath標本の直接singlet支持の不可能性 | R147の必要性を示す番号なし否定命題 | 付録I.2 |
| R148、R151 | singlet交差モーメントと安全盆routing | M48設定前・切断面準備へ吸収 | R153、付録D・I |
| R149、R154、R156、R166 | 理想Bell応答、2翼局所合成、帰還、条件付き因子化 | 完全Bell周期の節と補題へ吸収 | R155、付録D・I・J |

## draft-112で退役したQ3 Hamiltonian主線

M64/R203A--R203Dを現行Q3 particle/Nelson open modelへ昇格したため、M60/M61固有結果を現行論文の必須依存から外した。これは反証ではなく、固定目標に対してより短いopen-model主線へ責務を縮約したための退役である。

| 結果 | 旧用途 | 現行の扱い | 参照先 |
|---|---|---|---|
| R195A、R196A--R196C | chiral current、moving reflector、GLE/homogenization、metastable R161 transport | M64/R203A--R203Dへ置換 | draft-98--draft-111 Git履歴 |
| R197、R197A--R197C | M37 signalとM60 particleの共通模型・負荷安定性 | Q3-1はM37/R86、Q3-2はM64へ責務分離 | draft-101 Git履歴 |
| R198A--R198D | Duffing 2-action shell、有限reservoir、mixing window | M64/R203Bのphase-volume reservoirへ置換 | draft-102--draft-111 Git履歴 |
| R199A、R199B | chiral-medium core/ballistic lead同時windowと統合強化 | 現行固定主線から退役 | draft-103--draft-111 Git履歴 |
| R200A--R200C、R200 | M61 single-Hamiltonian parentからM60への持上げ | finite-Hamiltonian liftの旧強化経路として退役 | draft-105--draft-111 Git履歴 |

## 吸収済みモデルID

| モデル | 旧用途 | 現行の扱い | 参照先 |
|---|---|---|---|
| M51 | 有限実正準担体の共通開放ray準備 | 旧R181Aへ吸収後、draft-90で状態方向準備ごと退役 | `superseded_separate_m51_m52_m53_models.md`、`superseded_r181a_template_port_preparation.md` |
| M52 | 固定2・3入力の可逆tensor-lift永続register | M54の有限次元特殊化へ吸収 | `superseded_separate_m51_m52_m53_models.md`、R181B--R181D |
| M53 | 一般回路の直接mode・逐次sampler | direct-mode gateはM54/R181Cへ、Q2-4 terminal samplingはM66/R206へ置換。旧逐次sampler/aperture経路は退役 | `superseded_separate_m51_m52_m53_models.md`、`superseded_q2_sequential_terminal_readout.md` |
| M43 | 固有モード作用結合型有限環境 | 独立モデルから外し、R123の有限環境純位相緩和構成へ吸収 | R123、付録G |
| M35 | 作用区間によるBorn型標本器と有限正準制御補助 | 確率生成部は退役し、非確率的な制御・比較・記録部はR112へ吸収 | `superseded_m35_born_sampler.md`、R112、付録A |
| M50 | 有限信号作用・作用殻・static粒子位置熱化・旧measurement instrument | M54 static-instrument profileへ吸収後、Born型測定責務はM65へ置換。作用殻測定経路はdraft-124でactive paperから退役 | `superseded_separate_m50_m55_models.md`、`superseded_r164_q1q2_measurement_role.md`、`superseded_r190_r170_measurement_path.md` |
| M55 | 粒子--signal共同測度・spatial moving matching | M54 spatial-moving profileへ吸収。R184/R185を保持し、旧R183は一般R161へ吸収 | `superseded_separate_m50_m55_models.md`、第2章、第6章、付録N |

## 退役したモデルID

| モデル | 旧用途 | 現行の扱い | 参照先 |
|---|---|---|---|
| M61 | M37 signal、chiral sector、moving converter、harmonic bathを統合するsingle-Hamiltonian Q3親模型 | draft-112でM64 open modelを現行主線へ採用したため退役。有限Hamiltonian liftを再検討する際の旧強化経路としてGit履歴に保存 | draft-105--draft-111 Git履歴 |
| M60 | Duffing shell、統一chiral媒体、ballistic lead、moving-bath tracerからなるQ3共通縮約模型 | draft-112でM64/R203A--R203Dへ置換し現行正本から退役 | draft-101--draft-111 Git履歴 |
| M49 | 4モードprogram担体、行分解bath、二粒子位置によるQ2-1 CNOT供給 | 固定benchmarkは撤回せず退役。4mode自体でなく入力別template、外部routing、破壊的decode、閉じないinterfaceを不採用とし、Q2-1はM54/R181B--R181Dへ再構築 | `superseded_m49_joint_bath_cnot_provider.md`、draft-62のGit履歴 |
| M48 | 独立setting-pre paired-Hopf Bell protocol | paired-Hopf機構とBell監査はR180へ継承し、独立fair seedと集団交差momentを現行sourceから外す。Q2-2はM54/R180 receiverへ置換 | `superseded_independent_m48_bell_protocol.md`、draft-65のGit履歴 |

結果番号は再利用しない。現行結果の番号を詰めず、履歴参照を安定させる。
| 旧finite-collision実装・R188 | R162の旧有限衝突path liftとNelson安定性 | draft-87で現行のopen-Poisson R162へ簡略化。R162 ID自体はactiveのまま、有限閉鎖実装だけを強化結果として保存 | `superseded_r162_r188_finite_collision.md` |
| R178D | 有限閉鎖resetの情報容量境界 | draft-87でQ2-4必須依存から外し、強化結果へ降格 | `strengthening_closed_reset_information_bound.md` |


## draft-89で退役した測定経路

| 結果・模型 | 旧責務 | 現行置換 | 保存先 |
|---|---|---|---|
| R190A--R190C | 2作用LC殻Drude混合と静的平方根選択 | draft-89でR191へ置換後、draft-120でM65へ再置換 | `superseded_r190_r170_measurement_path.md`, `superseded_A19_drude_action_shell_bridge.md` |
| R170 | 静的選択結果の吸収pointer固定 | draft-89でR191へ置換後、draft-120でM65のfinite recordへ再置換 | `superseded_r190_r170_measurement_path.md` |
| R180B | 選択branchから2翼テンプレートをpaired-Hopfで再準備 | 現在はA端M65の非規格化branchをrouterでB端へ直接受渡し | `superseded_q2_2_paired_hopf_receiver.md`, `superseded_A9_paired_hopf_receiver.md` |

これらは反証ではなく責務縮約による退役である。固定Q1/Q2の誤差予算と必須依存には含めない。
