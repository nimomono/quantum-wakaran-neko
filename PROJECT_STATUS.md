## draft-130：R207A--R207D Q2-2-S candidate

- A23/付録WへR207A--R207DをQ2-2-S spatial-preparation candidateとして追加する。
- R207AはM66/R205Eを使う対称joint Gibbs preparation、R207Bはdeep-well/strong-lock CHSH witness、R207CはR205F後のlocal responseとmeasurement-dependence監査、R207DはBell-local controlを与える。
- Q2-2 fixed-goalの現行R180C--M65/R181D証人、Q2-2達成ラベル、Q2-2-S未監査状態は変更しない。
- finite-speed spatial reservoir、continuous full SDE trajectory、実験装置は未監査とし、R207をfixed-goal直接依存へ追加しない。

## draft-129：M66 common-reservoir parent拡張・R205C--R205F正式化

- M66をphase-volume、mean-flow、thermal sampling、passive separationを共通化するthermal-reservoir parentへ拡張する。Q2-1/Q2-3/Q2-4の現行readoutはR206A--R206EをM66の特殊化として維持する。
- R205Cをphase-volume / mean-flow orthogonality、R205DをM65 fixed-hub specialization、R205Eをcommon thermal Gibbs sampler、R205Fをpassive separation principleとして正式化する。
- M64/R203A--R203D、M65/R204A--R204F、R206A--R206Eの責務、全fixed-goal直接依存・達成ラベル、R186障害、Q2-2現行逐次interfaceは変更しない。
- Q2-2-S/R207は後続PRへ分離する。

## draft-128：M65/M66付録分離

- M66/R205--R206をA26から新しい `sections/A24_m66_common_phase_volume_readout.md`（付録X）へ移し、A26をM65/R204専用の付録Zへ戻す。
- R205/R206の数式、定理・証明、結果ID、Q2-1/Q2-3/Q2-4の直接依存、達成ラベル、required physics verifierは変更しない。
- 第4章のM66/R206付録参照だけを付録Xへ同期し、A24/A26の責務分離をPR固有migration checkで検査する。
- M66のcommon-reservoir parent拡張、R205C以降の追加定理化、Q2-2-S/R207は後続変更へ分離する。

## draft-127：M66/R206正式昇格・Q2逐次terminal readout退役

- M66/R205--R206をQ2-1/Q2-3/Q2-4の現行terminal multi-outcome readoutへ正式昇格する。Q2-1は4結果、Q2-3は8結果、Q2-4は $2^n$ 結果を一回のcommon-hub samplerで標本化する。
- R206Cをfinite-time/fabrication-error定理として正式化し、R206E uniform root preparation / refreshを追加する。Q2-4ではR206E→R181C→R206Dを主線とし、sampler pointerはR206Aのmixingで結果別resetを不要にする。
- Q2-1/Q2-3/Q2-4からM65/R181D逐次terminal tree、R179直接reset依存を外す。M65/R181DはQ1/Q2-2の逐次binary instrumentとして、R179はQ2-2と全周期renewal側として維持する。
- R192は旧Q2-4非終端branchの作用回復責務が消滅したためactive paperから退役し、notes/Git履歴へ保存する。結果IDは再利用しない。
- Q2-1/Q2-3は達成、Q2-4は条件付き達成のまま維持する。Q2-4の主要fixed-goal残件はR186のdirect-amplitude register additive-noise/precision障害へ集中する。
- M66/R206の数学・資源検算をcandidateからrequiredへ昇格する。A1/A2/B判定、Q2-2現行逐次interface、Q3主線、M0判定は変更しない。

## draft-126：M66/R205--R206 共通多結果読出し候補

- M66/R205A--R205Dを、M64/R203BとM65/R204Bに共通するphase-volume reservoir原理のactive parent candidateとして追加する。
- R206A--R206Dは有限L結果common-hub sampler、一様passive (L=2^n) channel構成、L非依存誤差・資源境界、Q2 terminal readout bridgeを与える。
- Q2-1/Q2-3/Q2-4の現行fixed-goal主線はまだM65/R181D系のままとし、R181D/R192/R179の退役は行わない。
- Q2-4は条件付き達成を維持し、R186のdirect-amplitude register additive-noise障害を主要な未解決条件として保持する。
- Q2-2の現行逐次A端--B端interfaceとQ2-2-Sは本draftでは変更しない。

## draft-125：履歴メモと横断整合検査

- `notes/theory_lineage.md` を履歴入口として追加し、個別退役メモに残る退役当時の「現行」「置換先」と現在の正本を区別する。現行運用状態は引き続き本書を正本とする。
- `tools/check_project_consistency.py` を恒久構造検査として追加し、active定理宣言と現行結果表の一致、固定目標の直接根拠がactive結果だけを参照すること、active結果IDと退役索引の非交差、履歴メモ参照先の存在を番号非依存で検査する。
- `tools/test_validation_policy.py` で新checkerへの具体的M/R/Q番号・特定sectionパスのハードコード再流入を禁止し、通常CIから実行されることを自己検査する。
- 旧メモ本文は歴史記録として一括書換えせず、誤読しやすい退役メモに現行注記を追加する。理論式、現行模型、結果ID、固定目標、達成ラベル、A1/A2/B/S判定、required/candidate physics verifierは変更しない。

## draft-124：R164/R170作用殻測定経路のactive paper退役

- R164の作用殻状態数定理とR170の静的吸収pointer固定を現行結果一覧・active本文・付録から外し、結果番号を再利用しない退役結果としてnotes/Git履歴へ移す。R190A--R190Cは既に退役済みであり、これにより旧作用殻測定経路全体をactive paperから外す。
- 付録Lをactive section treeから削除し、付録KはR161の一般current--traffic Markov経路法則とR162 optional Poisson realizationだけへ縮約する。
- 第2章のQ3接続は作用殻状態数を介さず、local canonical signalとedge currentから $(\pi^\delta,j^\delta)$ を作り、M64/R203Dがactivityを与えてR161へ接続する形へ一本化する。
- Q1/Q2の結果形成はM65/R181D、Q3の粒子位置はM64/R203A--R203D/R161/R185だけをactive正本とする。固定目標の達成ラベル、A1/A2/B1/B2/B3/Q2-2-S判定は変更しない。
- R135/R168、R161/R162、R179、R181D、R192など作用殻測定経路から独立な現行結果は維持する。

## draft-123：Q3旧R184率latch経路の退役

- R184のM37開始作用保持機構を現行Q3結果一覧・active付録・required検算から外し、結果番号を再利用しない退役結果として `notes/superseded_r184_m37_rate_latch.md` と退役索引へ移す。
- 付録NはR161 canonical経路法則、Bayes後退率、有限格子速度、R185時間対称Newton則だけに縮約し、M37 signalからR161への現行物理接続はM64/R203A--R203Dに一本化する。
- 第6章、Q3本文、結論、固定時刻代替診断から旧率latch参照を外し、Q3-4A/Q3-4B/Q3-5の位置読出しはM64/R203D finite-graph tracerだけを使う。
- `tools/verify_m54_spatial_matching.py` はR161/R185の数学回帰へ縮約する。R184専用数値コードは複製せずGit履歴に保存する。
- 固定目標の達成ラベル、M64/R203A--R203D、R161、R185、R124/R182/R125、A1/A2/B/S判定は変更しない。

## draft-122：現行依存グラフの同期

- 固定目標表の「根拠となる結果」を、達成判定で直接参照する結果・interfaceだけを列挙する台帳として明確化し、個々の定理の推移的依存を重複列挙しない。
- Q1-2の直接根拠からR168を外し、R168は状態方向平均の支持結果として保持する。Q2-2の根拠表をR112/R180C/R181D/R204D--R204Eへ同期する。
- Q1/Q2の現行2結果読出しをM65/R204D--R204F＋R181D、Q3粒子位置をM64/R203A--R203D＋R161/R185へ統一し、A1・第3章・第6章に残ったR164/R170旧主線表現を代替研究線へ下げる。
- Q3-4A/Q3-4B/Q3-5の付録G読出しbridgeをR184からM64/R203D finite-graph tracerへ同期し、本文第7章の証明参照も付録G＋付録Yへ揃える。
- R164/R170/R184の定理自体は本draftでは退役させない。固定目標の達成ラベル、模型、結果ID、A1/A2/B/S判定、physics verifierは変更しない。

## draft-121：固定目標の一試行物理interface原則への統一

- 各固定目標は、その目標が要求する物理現象・観測統計・逐次過程を、一試行内で明示的な物理interfaceを介して合成できれば達成候補とする共通原則へ統一する。
- 準備、全操作、測定、永久記録、reset、物理clock、次試行renewalまでを一つのjoint microscopic device/processと共通反復周期へ統合することはM0でのみ要求し、個別固定目標が明記しない限り未達理由にしない。
- 固定有限深さでは未使用補助自由度を順次用いてよく、同一試行中に使用済み補助自由度を再利用する場合だけ当該resetを要求する。解析上の状態ベクトル、集団統計、Born重み、目標確率表の外部再注入は物理interfaceの代替としない。
- Q2-4は資源効率・反復回数・総時間・精度を固定目標自身が要求する例外として、一様装置族、R179/R192、R186の資源・ノイズ条件を固定目標内に維持する。
- 既存の一試行接続を再監査し、Q2-1、Q2-2、Q2-3、Q3-4A、Q3-4B、Q3-5を達成へ更新する。Q2-4は条件付き達成、Q3-6は未達、M0は未達のままとする。新しい模型、結果ID、定理、physics verifier、A1/A2/B/S状態は追加・変更しない。

## draft-120：R191/R193退役・M65 fixed-goal主線化

- Q1/Q2 fixed-goalの2結果selectorをM65/R204D--R204Fへ切り替え、R181D/R192/R179/R180A--R180Cの既存binary-selector interfaceへ接続する。
- Q1ではR189A保持作用をM65へ直接入力し、R143/R144/R189B/R189Cの現行証人をM65へ同期する。有限2回Zenoの理想余裕 $1/4$ と達成ラベルは変更しない。
- R191 Brownian macrospin読出しとR193 Q1直接decision bridgeは責務をM65へ吸収したため現行主線から退役し、A20/A21と専用verifierをnotesへ保存する。結果番号は再利用しない。
- Q2-1--Q2-4の達成ラベルは維持する。条件付き達成の残件はM65/R181D/記録/resetの装置統合、Q2-4の一様装置族とR186ノイズ条件へ更新する。
- M65のphase-volume/Hamiltonian--Brownian liftは引き続き強化実現であり、R186、M0、A/B/S判定、Q3主線は変更しない。

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

- 「採用開放方程式」「採用open model」のように「採用」を名詞修飾語として使う表記を現行正本から廃止する。
- Hamiltonian浴などの上位模型からの導出を前提とせず、方程式自体をミクロ模型の基本発展則として置く場合は、文章では「開放ミクロ方程式として直接定める」、名詞では「直接定めた開放ミクロ方程式」を標準表記とする。
- Hamiltonian浴から縮約導出した場合は「Hamiltonian浴から導出した開放方程式」と区別する。
- 本変更は用語整理のみであり、固定目標、達成ラベル、M0判定、A1/A2/B/S状態、現行模型・結果・数式・physics verifierを変更しない。

## draft-115：M0 open microscopic device 判定への一般化

- M0「単一ミクロ装置統一目標」の達成条件から、明示的なHamiltonian無限浴への持上げを外し、PROJECT_GUIDE 4.5.2の規約を満たす採用開放古典ミクロ方程式を認める。
- M0の強さはHamiltonian性ではなく、Q1/Q2/Q3の主要自由度、物理接続端、準備、操作、測定、記録、reset、clockを一つのjoint microscopic device/processと共通反復周期へ統合する範囲に置く。
- Hamiltonian無限浴への持上げ、複数reservoir portの共通単一bathへの統合、有限浴化、有限閉鎖Hamiltonian全系への持上げ、周期全体の完全な微視的熱力学収支は、M0より強い横断的強化課題へ分離する。
- 規模依存のQ2-4を含むため、M0は一台の固定有限装置ではなく、一様な有限規則から生成される同一architectureの装置族と一つのparameter familyを許す。入力、測定軸、ポテンシャル、回路規模に応じた有限設定値の変更は許す。
- M0の現在地は未達のまま維持する。Q1/Q2/Q3の固定目標・達成ラベル、A1/A2/B/S判定、R191/R193の現行主線、M65/R204A--R204Fのreplacement candidate状態は変更しない。

## draft-114：M65 phase-volume projective instrument置換候補

- M65/R204A--R204Fを、R191/R193をまだ置換しないpromotion-ready replacement candidateとして追加する。
- R203Bと共通のphase-volume Jacobianを二結果射影作用へ接続し、固定chamber--neck--hubのcapacity/conductance matching、Hamiltonian--Brownian縮約契約、有限時間Born読出し、R181D受渡し、Q1接続、Q2-4 polynomial readout-time条件を整理する。
- R204Cのfull HamiltonianからBrownian chamber networkへの有限誤差縮約をpromotion gateとして残し、R186の指数mode additive-noise/precision障害は未解決のまま維持する。
- 現行Q1/Q2 fixed-goal主線、達成ラベル、R191/R193 required verifier、R181D/R192/R179の定理文、M64 Q3主線は変更しない。

## draft-112：M64正式昇格・M60/M61退役

- M64/R203A--R203DをQ3の現行particle/Nelson open modelへ正式昇格する。Q3-1はM37/R86を達成証人とし、Q3-2はM37/R86 → M64/R203A--R203D → R161 → R185を現行主線とする。
- R203Dへfinite-graph initial preparation、Markov contraction、generator実装誤差、R124/R182/R125のregularized位置読出し条件を追加する。
- Q3-4A、Q3-4B、Q3-5の固定達成根拠をM60 transportからM64 finite-graph tracerへ移す。達成ラベルは変更しない。
- A22--A24のM60/M61旧Hamiltonian実装を現行論文から退役し、R195--R200は現行必須依存から外してGit履歴・退役索引に保存する。
- M64の6本の科学検算をrequiredへ昇格し、M60/M61専用required/candidate verifierを現行treeから退役する。
- Q3-1-A1/Q3-2-A1は部分達成、Q3-1-A2/Q3-2-A2は未監査のままとし、M64昇格だけから強化目標判定を変更しない。

## draft-111：M64 promotion bridge完成

- M64/R203A--R203Dを、M60/M61をまだ置換しないpromotion-ready replacement candidateへ更新する。
- R203Bにphase-volume reservoirからの有限時間initial tracer preparationと $U\to v_\delta$ のfinite-time tracking boundを追加し、R203Cの正本をcanonical overdamped open SDEへ単純化する。
- R203Aのtarget regularizationをR185と共通の $(\rho_\delta,J_\delta,v_\delta)$ へ揃え、R203Cのmicro-to-effective process reduction errorとR185 Newton residualを別々の誤差として管理する。
- R203Dを一般finite graphへ拡張し、local $R_i^\delta,J_{ij},T_{ij}^\delta$ からR161 rateを構成する。1次元特殊化はR185 activityと一致し、R125の2頂点再結合器へも直接接続する。
- 本draftではM61/M60 fixed-goal主線、Q3達成ラベル、A1/A2判定、M61/M60 required verifierを変更しない。M60/M61退役とM64 required昇格は独立promotion PRへ残す。
- A2 direct simulationは固定目標用M64 promotionの必要条件とせず、強化目標として独立に監査する。

## draft-110：M63退役

- M63/R202A--R202Fをactive single-field candidateから退役し、現行付録、candidate checks、simulation registryから削除する。過去draft記録とGit履歴は保存し、反証された模型とは扱わない。
- M64付録をA25/Yへ繰り上げるが、M64/R203A--R203Dはactive replacement candidateのままとし、M61/M60固定達成主線へ昇格させない。
- Q3-1/Q3-2固定達成、Q3-1-A1/Q3-2-A1部分達成、Q3-1-A2/Q3-2-A2未監査、M61/M60 required verifierは変更しない。
- M64昇格とM60/M61退役は、M64固有の残件を監査する後続PRへ分離する。
## draft-109：M64 三実体open-Q3置換候補

- M64/R203A--R203DをQ3のactive replacement candidateとして追加する。単一試行の物理実体をM37型classical coherent signal、独立tracer、signal-driven moving thermal reservoirの三つへ限定する。
- R203Aは既存current identityをM64へ再利用し、R203Bはdensity-dependent coordinate scalingとmean-flow momentum shiftを同じreservoirへ入れても $F_{\rm res}=-k_BT\log r_X^\delta+\mathrm{const}$ が保たれることをJacobian恒等式で示す。
- R203Cはconstant $T$、constant $\gamma_X$ のmoving Langevin reservoirからoverdamped drift $j/\rho+\nu\partial_x\log\rho$ とdiffusion $\nu=k_BT/\gamma_X$ を得る。R203DはPN/Eyring--Kramersを介さずsmooth diffusionをfinite-volume R161 chainへ直接接続する。
- M64ではcurrent mean-flow law $\tau_U\dot U=-U+c_Jr+R_U$ を採用open constitutive lawとし、その完全Hamiltonian scattering liftを本体達成条件へ入れない。single-field lift、finite-bath化、fresh-buffer等はstrengtheningへ分離する。
- 本draftではM61/M60の現行固定達成主線、M63/R202のactive single-field candidate、Q3-1/Q3-2固定達成、Q3-1-A1/Q3-2-A1部分達成、Q3-1-A2/Q3-2-A2未監査、required/candidate verifierを変更しない。M64昇格とM60/M61/M63の退役は次の独立PRで監査する。

## draft-108：M62退役・M63 current-transport具体化

- M62/R201を現行正本、candidate checks、simulation registryから退役し、旧付録・検算・集約witnessを削除する。過去draftの記録とGit履歴は保存する。
- M63/R202を付録Yへ移し、$v$-branchからsoft current-frame coordinate $Y$ と残余harmonic reservoirを固定正準変換で取り出す構成へ更新する。
- R202E1でsame-field signalの左右作用比から $j/\rho$ を読むcurrent dictionary、R202E2でT対称real-space weak scatteringによるframe tracking、R202E3で$X-\alpha_YY$に結合するharmonic reservoirのfrozen-coefficient GLE/FDTを追加する。
- R202Cのtopological partition identityはrelative-coordinate completed squareを追加しても $F_R=-k_BT\log r_K+\mathrm{const}$ のまま保たれ、等価PN minima間のBorn型位置重みを系として得る。
- R202E2のreal-space scattering有限誤差、loadを含むtracking window、slow coefficient/Ohmic補正、full trajectory、R202FのPN hopping--R161接続は未閉鎖とする。
- M61/M60は現行固定達成主線として維持し、Q3-1/Q3-2達成、A1部分達成、A2未監査、required verifierは変更しない。

## draft-107：M63 topological-reservoir 一成分Hamiltonian Q3統合候補

- M63/R202A--R202Fをactive single-field candidateとして新設する。一組の実格子正準変数 $(\phi_n,\pi_n)$ を2-site local canonical filter bankでkink/signal branchとreservoir branchへ分け、2-action shellを用いずreservoir phase-space Jacobianからosmotic free energyを直接生成する。
- R202Cでは $\gamma_m=s(\bar u_{m+1})-s(\bar u_m)$、$\sum_m\gamma_m=1$ と $\lambda_m=(r_m/r_*)^{-\gamma_m}$ から $F_R=-k_BT\sum_m\gamma_m\log r_m+\mathrm{const}$ を条件付きpartition identityとして得る。R202Dはsmooth-kink極の $k_BT\partial_X\log r$ と $O(N_0^{-1})$ signal backreactionを担う。
- R202Eのsame-field current port・reservoir GLE/FDT、R202FのPeierls--Nabarro hoppingからR161/R185への有限時間接続は未閉鎖とする。M63はM61/M60 fixed-goal主線をまだ置換しない。
- M62/R201はactive candidateから退役し、2-action shell型の歴史的candidateとして付録Y・candidate checks・simulation registryを保存する。
- 固定Q3-1/Q3-2達成、Q3-1-A1/Q3-2-A1部分達成、Q3-1-A2/Q3-2-A2未監査、required verifierは変更しない。

## draft-106：M62 一成分Hamiltonian lattice Q3統合候補

- M62を、一組の実格子正準変数 $(\phi_n,\pi_n)$ からkink位置、2 shell mode、signal continuum、prethermal reservoir、reaction-coordinate frameを同時に得るQ3単一場統合候補として追加する。R201A--R201Fでspectrum、same-field signal、weighted-shell normal form、reservoir交換、GLE/FDT、共通parameter有限時間合成へ責務分離する。
- M62/R201は現行M61/R200--M60/R198/R199/R196主線をまだ置換しない。R201Cのcontinuum-inclusive remainder、R201Dのvalidated exchange/prethermal lifetime、R201Eのfinite-memory Markov誤差、R201Fの十分な共通時間尺度分離を未閉鎖とする。
- 固定目標Q3-1/Q3-2の達成ラベルは変更しない。Q3-1-A1/Q3-2-A1は部分達成、Q3-1-A2/Q3-2-A2は未監査のままとし、M62の数値結果はcandidate witnessとして管理する。

## draft-105：M61 単一Hamiltonian Q3親模型

- M60を退役させず、その下位にM61を追加する。M61は一つのmultiband媒体と一つの複合mobile subsystemを単一の時間非依存 $H_{61}$ へ統合し、R200A--R200C/R200を介してM60へ縮約する。
- R200CはM37 signalとM60 chiral sectorの共通multiband媒体持上げ、R200Aはmoving branch-converter HamiltonianからR196A bath-frame則への縮約、R200Bは $X-Y$ に結合する内部harmonic continuumからGLE/FDTへの厳密縮約を担当する。
- 固定目標Q3-1/Q3-2の達成ラベルは変更しない。Q3-1-A1/Q3-2-A1は、R198Dの具体的core mixing、R199Aのcore--lead同時parameter witness、R200A/Bのtracking--thermal-load同時parameter witnessが残るため部分達成のままとする。A2はM61直接数値再現が未実施なので未監査とする。

## draft-103：M60 Duffing shell＋統一二成分chiral媒体への置換

- M59の実2-mode Duffing shellとその2-action Gibbs shell縮約は維持し、別実体だった二成分DNLS action reservoirとdual ballistic waveguideを、M60の一つの二成分非線形chiral Hamiltonian媒体へ統合する。同じ $b_{\pm n}$ 自由度がnonlinear coreではaction reservoir、弱非線形leadでは左右ballistic carrierとして働く。
- R198Aは実Duffingから2-action shellへの有限時間縮約として維持する。R198B--R198DはM60 nonlinear coreへ一般化し、R199Aを同一媒体のnonlinear-core / ballistic-lead有限時間分離と同時parameter windowの結果として追加する。R199Bは同じDuffing pairがchiral current情報も保持できる奇偶応答を統合強化として整理するが、固定Q3-2達成の必須依存にはしない。
- 独立M57親模型と独立dual ballistic TLは現行Q3主線から退役し、A22はM60 transport reductionへ責務変更する。R195Aのchiral current恒等式、R196Aのmoving-reflector、R196Bの平衡oscillator bath GLE/FDT、R196CのR161持上げは維持し、R196Aへの入射波だけをR199AのM60 ballistic leadへ差し替える。
- 固定目標Q3-1/Q3-2の達成ラベルは維持する。Q3-1-A1/Q3-2-A1は、R198Dの具体的core mixing/homogenization witnessとR199Aのcore--lead同時parameter witnessを残件として部分達成のまま保持し、A2は未監査とする。

## draft-102：M59 Duffing shell＋二保存action reservoirへの置換

- 旧M58のthermostatted 2-action shellを現行主線から退役し、M59をM37 signal＋実2-mode Duffing shell＋二成分DNLS action reservoir＋M57 transportからなる共通ミクロ模型として採用する。
- R198Aで非共鳴2-mode Duffingから2-action shellを有限時間縮約し、R198Bで二保存action有限reservoirのmicrocanonical marginalをM59 Gibbs shellへ $O(N^{-1})$ で接続する。
- R198Cで有限exchange couplingの奇数次補正消失、二次chemical-potential renormalization、残差 $O(\lambda^4)+O(\lambda^2/N)$ を整理する。R198Dは正温度・非凝縮sectorのmixing/homogenizationを明示仮定した有限時間thermalization定理とする。
- 固定目標Q3-1/Q3-2の達成ラベルは維持する。一方、M59のA1完全証人性にはR198Dの具体的mixing witnessが残るためQ3-1-A1/Q3-2-A1は部分達成へ戻す。A2は未監査のまま保持する。

## draft-101：M58 Q3共通ミクロ模型とR197統合

- M37 signal subsystem、thermostatted 2-action shell、M57 transport subsystemを同一試行上のM58へ統合し、R197A--R197CとR197を追加する。
- Q3-1はM58のsignal marginalからR86へ、Q3-2は同じM58のfull tracer marginalからR196A--R196C、R161、R185へ進む。固定目標の定義と達成ラベルは変更しない。
- A12の状態数自由エネルギーをR197A/Bの実際のGibbs周辺化へ接続し、A22で従来入力していた $-k_BT\log R^\delta$ を同じM58 shellの平均力として導出する。
- Q3-1-A1とQ3-2-A1をM58/R197により達成へ上げる。A2はM58採用SDE/PDEの直接数値再現が未実施なので未監査のまま保持する。

## draft-100：R161へ有限状態Markov経路法則を吸収

- R161の責務を、確率流・活動量からの有向率と周辺分布整合だけでなく、固定有限時間・有限状態・有界総hazard下の一意な非爆発canonical Markov経路法則とBayes後退率まで拡張する。
- Q3-2の達成根拠からR162を外し、M57/R195A・R196A--R196C → R161 → R185を現行因果鎖とする。
- R162は結果IDを維持するが、R161経路法則を独立Poisson random measuresでpathwiseに実現するoptional referenceへ責務を縮約する。現行Q3ミクロ物理層でもR185の必須依存でもない。
- 固定目標、達成ラベル、M57/R195A・R196A--R196C、R184、R185の内容は変更しない。

## draft-98：M57をdual ballistic TL＋moving equilibrium bathへ置換

- draft-95のpinned/weakly-anharmonic TL、TL mixing、force-correlation、drifting-Gibbs、TL自身へのFDTをQ3正本から退役し、M57をdual ballistic waveguide、moving bath-frame carrier $Y_e$、平衡oscillator bath、局在tracer $X$ の構造へ置換する。
- R195Aはchiral作用和・差に加えて $J_{ij}^{\rm sig}=\nu(I_+-I_-)/a^2$ と $u_{ij}^{\rm sig}=2\nu r/a$ の厳密恒等式まで強化する。旧R195B--R195Dは結果IDを再利用せず退役し、新系列R196A--R196Cを採用する。
- R196Aはmoving-reflectorのexact ballistic force、唯一安定fixed point $U_*=c\beta_*(r)$、有限時間tracking、weak-tap/backreaction scalingを与える。R196Bはmoving equilibrium oscillator bathからGLE/FDT、overdamped reduction、periodic homogenization、weak-loading scalingを与える。R196Cは $\mathcal A=4\beta_*(r)$ のmetastable well-index generatorをR161へ有限誤差で持ち上げる。
- 中心matchingは $D_0=\nu/g_K$ と $g_Kc=4\nu/a$。TLをthermalizeせず、current drift、osmotic drift、diffusionをそれぞれballistic mechanics、state-count free energy、equilibrium bathへ責務分離する。
- `tools/verify_m57_ballistic_tracer.py` でchiral恒等式、moving-reflector fixed point・安定性・tracking、weak-tap/loading scaling、Lifson--Jackson suppression、新R161 current correctionと時間尺度windowを検算する。
- R161/R162/R185の数学核、Q1/Q2、固定目標の定義と既存達成ラベルは変更しない。Q3-2の達成根拠だけを新M57/R195A/R196A--R196Cへ差し替える。

## draft-97：強化目標同期、Q2-2 Bell前提一般化、採用開放雑音模型の明確化

- Q2-2の固定目標から特定の「測定設定独立性の破れ」を必須条件として外し、Bell型共同統計を再現した古典構成についてBell不等式導出に用いられる前提の成立・不成立を物理的因果構造と確率因子化に対応させて監査する一般基準へ改める。Q2-2の条件付き達成ラベルは変更しない。
- `ENHANCEMENT_TARGETS.md` を固定目標に付随する強化目標A1/A2、Q1/Q2のB1/B2/B3、Q2-2-Sの正本として正式に接続し、全強化目標は未監査から開始する。
- A1ではHamiltonian無限浴に加え、Langevin型SDEなどの採用開放ミクロ方程式と理想白色雑音を許す。A2は採用したミクロODE/SDEそのものの直接数値再現を要求し、B2/B3では有限帯域雑音へ落として実験可能性を監査する。
- 固定目標のうちQ2-2以外の定義、全ての既存達成ラベル、現行結果IDは変更しない。

# 固定長期目標、現行モデル、現行結果

## draft-95：M57 dual-TL tracerをQ3ミクロ正本へ採用

- M37/M54の実正準空間信号を維持し、Q3の実在粒子輸送を、2作用状態数、左右独立のfinite pinned open transmission line、局在tracer、periodic/double-well potentialからなるM57へ置き換える。
- R195A--R195Dを追加し、chiral作用・状態数、finite-time port slavingとmixing、Green--Kubo/FDTとKramers matching、M57からR161生成子への有限時間持上げを分離する。
- R161は共通数学interface、R162はM57 coarse-grained pathと比較するideal open-jump reference、R185は同じ前向き経路法則からの時間反転・時間対称Newton縮約として維持する。
- R184は旧M37--M54空間率latchの補助結果として保持するが、Q3-2/Q3-4/Q3-5の現行必須依存から外す。M56はspin-only代替研究線、空間化Q1＋Q2模型はR161数学参照実現として残す。
- 明示parameter witnessと `tools/verify_m57_tl_tracer.py` により、finite $\tau_{\rm mix}$、finite $\tau_{\rm corr}$、$g_Kc=4\nu/a$、$D_{\rm hop}=\nu$、current-drift matchingの同時parameter windowが非空であることを検算する。
- Q1--Q3の固定目標と達成ラベルは変更しない。Q3-2の達成根拠を抽象open-Poissonミクロ存在論からM57/R195A--R195Dの明示TL-tracer縮約へ強化する。

## draft-94：R161共通数学核とQ1--Q3空間構造整理

- R161をQ3位置輸送の共通数学核として明示し、Q1型局所実正準信号を空間頂点へ配置し、Q2型2体系エルミート結合を辺へ反復するとQ3空間信号の $(\pi,j)$ が得られる構造を正本化する。
- 独立なQ1型モード列だけでは辺流がなくQ3にならないこと、対称活動量 $t$ は信号連続方程式から一意には決まらず位置輸送の物理実現が別途供給することを境界として明示する。
- R161の $(t,j)$ を対称基準活動度 $c$ と非平衡親和力 $\mathcal A$ へ厳密に書き換える等価表示と、同じ有向率を与えるミクロ模型をR161実現として同値とみなす規約を追加する。
- 空間化Q1＋Q2相互作用は数学的参照実現として扱い、M56などの具体模型は同じR161核のミクロ物理実現候補へ位置づける。新しいミクロHamiltonianは本改訂では採用しない。
- Q1--Q3の固定目標、達成ラベル、R161/R162/R184/R185の既存定理内容は変更しない。

## draft-93：Q3-1固定目標のモデル非依存化

- Q3-1の固定目標から「局所位置結合振動子網」という特定実装を外し、明示的な古典物理モデルからSchrödinger型空間有効力学を導く一般基準へ改訂する。
- 結合振動子、古典spin系、連続場、その他の局所古典自由度を許し、複素包絡は独立実体でなく実古典自由度の派生表示でもよい。
- 基礎自由度と運動方程式またはHamiltonian、Schrödinger型有効自由度への縮約または変数変換、有効Hamiltonian・質量・ポテンシャル・作用尺度の対応、適用範囲、有限時間誤差または制御された極限を明示することを要求する。
- Schrödinger方程式の実・虚部分解や設計済み正準座標への形式的な書換えだけでは達成としない。連続空間を主張する場合は制御された連続極限も要求する。
- 現行M37/R86は一般化後のQ3-1基準を満たす一つの達成証人として維持する。Q3-1の達成ラベル、他の固定目標と達成ラベルは変更しない。

## draft-91：R193 Q1作用保持--macrospin直接decision接続

- R193を追加し、R189Aが保持したQ1 W2左右作用座標をR191ブラウン巨視的スピンのdecision energyへ直接Hamiltonian結合する。
- decision中の保持座標不変、W2への直接反作用零、R189A作用比誤差から吸引域境界への $2\varepsilon_{189A}$ 評価、endpointの除算不要な線形比較を明示する。
- decision後の保持対共役運動量にmacrospin履歴が残るため、次回capture前の未使用保持対 SWAPまたはR179 open resetを必須境界とする。
- R193はQ1専用特殊化であり、Q2の一般R191 transducer契約を変更しない。Q1-1/Q1-2の達成ラベルと固定目標は変更しない。
- M0全体は未達のまま。Q1ではW2作用保持からmacrospin decision energyまでが具体化し、残件はmacrospin浴、吸収記録、R181D router、未使用保持対/reset、共通時計自由度の全周期統合へ縮約する。

## draft-90：R181A退役とR192方向不変作用安定化

- R181Aの状態方向準備を現行固定目標の主線から完全退役し、古典実正準系の初期状態方向は準備済み入力境界として扱う。
- R181Aのうち一般深さQ2-4で必要だった方向不変の作用下限回復だけをR192へ切り出す。
- R192は状態方向、Born重み、結果選択を生成せず、非零信号の方向を保存したまま作用だけを固定目標値へ有限時間で安定化する。
- Q1-2とQ3系列はR192へ依存しない。Q2-4だけが非終端の安全結果成分でR192を用いる。
- Q2-4は一般 $n$ の初期化にR181Bを用いず、R179後の定数次元供給源から $0^n$ 根モードを作る既存方針へ依存表を同期する。
- 固定長期目標と達成ラベルは変更しない。

## draft-89：R191測定主線の責務縮約

- Q1/Q2の2結果射影測定はR191を唯一の現行主読出しとする。
- R181Dはprojector routerと非規格化結果成分受渡しへ責務を縮約し、固定有限深さでは振幅再調整を必須にしない。
- R164はQ3開始配置、R179はopen reset/履歴排出へ責務を分離する。
- R190A--R190C、R170、R180B paired-Hopf受信機構は固定Q1/Q2の必須主線から退役し、notes/Git履歴へ保存する。
- Q2-2はA端R191からB端R191へ結果成分を渡す非空間分離2端装置へ縮約する。
- 固定長期目標と達成ラベルは変更しない。

この文書は固定長期目標と現在地、現行モデル、現行結果、未解決問題だけを管理する。置換済み模型、退役結果、独立研究線の最小索引は `notes/superseded_result_index.md`、詳細は各研究メモとGit履歴を正本とする。

## 固定長期目標

以下の目標ID、名称、意味、達成判定基準は通常の論文更新では変更しない。追加、削除、統合、分割または判定基準の変更は独立した方針変更として扱う。固定目標に付随するA1/A2、Q1/Q2のB1/B2/B3、Q2-2-Sの定義、適用範囲、現在地は `ENHANCEMENT_TARGETS.md` を正本とし、固定目標の達成状態とは独立に管理する。

### 固定目標一覧

#### 第1段階：単一量子ビット型装置

| ID | 固定目標 | 達成判定の中心 |
|---|---|---|
| Q1-1 | 単一量子ビット型可逆力学 | Bloch 球に相当する有効状態空間、共通位相不変性、任意の $SU(2)$ 操作を同じ古典ハミルトニアン信号系で実現する。Rabi 振動の振幅、振動数、離調依存性も含める |
| Q1-2 | 射影測定統計とZeno効果 | 任意のBloch軸について2値Born分布、同軸再測定の反復分布、異なる軸による逐次測定分布を明示的なミクロモデルから導く。さらに、同じミクロモデルでRabi型遷移と有限回の反復測定を接続し、測定間隔に応じたZeno型遷移抑制を有限誤差で示す。無反応を含む全履歴を保持し、摩擦、ハミルトニアンの停止、事後選別、傾斜だけによる抑制とは区別する |

旧Q1-4はQ1-2へ統合した。旧Q1-3は固定目標から削除し、完全操作・測定周期、永久記録、内部逆計算、リセット、周期全体の仕事・熱・エントロピー収支は、固定目標とは別の実装・熱力学的強化課題として管理する。旧IDは再利用しない。

#### 第2段階：複合系・量子計算

| ID | 固定目標 | 達成判定の中心 |
|---|---|---|
| Q2-1 | 2量子ビット型結合ゲート | 2量子ビット型結合ゲートと同一の共同入力--出力統計を生成する明示的な古典ミクロ過程を構成する。結合ゲートは、2論理部分系のテンソル積構造に関して積入力を非分離な共同内部状態へ移し得るものとする。二端Bell測定または多段ゲート合成はQ2-1単独の達成判定に含めない。 |
| Q2-2 | Bell 型測定統計 | 二体系の共同内部状態を2つの物理的な測定端へ接続し、各端での操作・測定・記録から、余弦共同確率、CHSH 不等式の破れ、Tsirelson 限界、非信号性を整合的に導く。さらに、その古典構成についてBell不等式の導出に用いられる前提のうち、どれが成立し、どれが成立しないかを、物理的因果構造および確率因子化と対応させて明示する。特定のQ2-1実装からの受渡しはQ2-2単独の達成条件にしない。 |
| Q2-3 | 3量子ビット型二段ゲート合成 | 3つのQ1型有限能動部分系 $A,B,C$ と永続状態浴を持つ明示的な古典ミクロ装置を構成し、2つの2量子ビット型結合ゲートを $A$--$B$、続いて $B$--$C$ へ作用させる。第1ゲート後の非分離状態と相対位相を、測定、経路選択、共同モーメントへの置換、再準備を行わず第2ゲートへ受け渡し、3体系の最終計算基底分布を再現する。局所位相操作と逆ゲート列により、ゲート間で保持されたコヒーレンスを正の有限余裕で検査する。 |
| Q2-4 | 多項式外部制御による量子出力サンプリング | 固定有限普遍ゲート集合から与えられる任意の $n$ 量子ビット・深さ $d$ の有限量子回路について、一出力標本を全変動距離 $\epsilon$ 以内で生成する。状態浴内部の受動的自由度、静的結合、状態容量、受動並列度は指数的でもよいが、一様な有限規則から生成され、個別の初期化、設定、較正、制御、リセット、読出しを必要としないことを示す。回路記述、コンパイル、外部制御、準備、操作、読出し、精度、反復回数、総時間は $n,d,1/\epsilon$ の多項式に抑える。最終出力分布を事前計算すること、指数長の係数表、回路ごとの配線変更、稀な成功、事後選別、指数時間は認めない。 |

旧Q2-3「有限回路の機能的再現」と旧Q2-5「自律非平衡計算と平衡化運命の決定不能性」は固定目標から削除した。旧Q2-3の直接モード構成は現行Q2-4の信号系へ再編して監査する。旧Q2-5は独立研究線として退役索引に保存する。Q2-5のIDは再利用しない。

#### Q2独立判定と共通ハードウェア努力目標

- Q2-1からQ2-4は互いに論理的に独立に判定し、あるQ2目標の達成を別のQ2目標の前提にしない。
- 独立判定とは、他のQ2目標の達成ラベルを前提にしないことを意味する。同じ模型または部品定理を複数の目標の根拠として使うことは禁止しない。
- 各目標の達成状態は、その行に明記した共通状態構成、物理信号系または物理実装層、系列固有手順または受信機構、根拠結果だけで判定する。目標ごとに信号系、浴、時計自由度、準備・読出し原理が異なっても、それだけでは不達としない。共通の有効状態構成または入出力契約を使うことと、同じ物理装置を使うことは区別する。
- 規模 $N$ ごとの一様な共通ハードウェア族へ統合することは、固定目標の達成条件ではなく実装上の努力目標とする。将来これを主張する場合は、同じ物理接続端、永続状態浴、相互作用区間族、時計自由度・制御バス、準備接続部、Born型読出し・記録接続部を共有する具体的装置族を別途示す。
- パラメータ値、使用する接続端、有限の外部制御列は目標と入力に応じて変えてよい。受動的な浴自由度、コヒーレント経路、静的結合、状態容量、受動並列度が指数的に増えても、それだけでは不達としない。ただし規模と構造を報告し、一様な有限規則で生成できることを要求する。
- Q2-4はブラックボックスとしての運用上の基準として判定する。受動貯蔵部の総容量、装置体積、低温／使用済み素子総数、総熱が指数的でもよいが、規模と構造を報告し、外部制御器が個別に個別指定、設定、較正、回収することは認めない。内部の指数構造が外部プログラム、精度、時間、試行回数へ露出した場合は外部運用資源として数える。この基準は通常の意味の効率的古典シミュレーションや量子計算機と同等の総物理資源を主張しない。
- 指数個の自由度を個別に初期化、設定、較正、同期、制御、リセット、読出しすること、指数長の係数表または配線表を与えること、全自由度を走査すること、指数的に細かい精度・小さい成功率・長い時間へ費用を移すことは認めない。

#### 第3段階：空間量子力学

| ID | 固定目標 | 達成判定の中心 |
|---|---|---|
| Q3-1 | 空間 Schrödinger 型有効力学 | 明示的な古典物理モデルから、1次元または有限空間格子上の複素包絡または同等な実正準自由度について、Schrödinger 型時間発展を有効力学として導く。結合振動子、古典spin系、連続場、その他の局所古典自由度を許す。基礎自由度と運動方程式またはHamiltonian、Schrödinger型有効自由度への縮約または変数変換、有効Hamiltonian・質量・ポテンシャル・作用尺度の対応、適用範囲、有限時間誤差または制御された極限を明示する。単なる形式的な正準書換えでは達成としない。連続空間を主張する場合は制御された連続極限も示す |
| Q3-2 | Nelson流の作用変分または時間対称Newton則の導出 | 明示的な古典ミクロモデルの縮約から、Nelson型確率力学における作用の停留原理、または前進・後退平均加速度を対称に組み合わせたNewton則を導く。対象となる確率過程、前進・後退平均微分、力とポテンシャル、適用時間、近似範囲および誤差を明示する。作用変分を用いる場合は、作用汎関数、許容変分および端点条件も示す |
| Q3-3A | 井戸型の束縛状態 | 1次元の井戸型ポテンシャルについて有限個の非縮退低位固有状態の固有値、密度、節構造を再現し、環境との弱結合を縮約したエネルギー固有基底で、非対角相関の有限時間減衰と対角占有率の安定性を導く |
| Q3-3B | 調和型の束縛状態 | 1次元の調和型ポテンシャルについて有限個の非縮退低位固有状態の固有値、密度、節構造を再現し、環境との弱結合を縮約したエネルギー固有基底で、非対角相関の有限時間減衰と対角占有率の安定性を導く |
| Q3-3C | W型の束縛状態 | 1次元の有限障壁を持つW型ポテンシャルについて有限個の非縮退低位固有状態の固有値、密度、節構造を再現し、環境との弱結合を縮約したエネルギー固有基底で、非対角相関の有限時間減衰と対角占有率の安定性を導く |
| Q3-4A | 有限障壁のトンネル効果 | 有限障壁を持つSchrödinger型発展で、障壁値より低いエネルギー成分だけからなる状態が障壁反対側へ正の位置確率を移すことを示し、その確率を単一試行の位置読出しへ接続する |
| Q3-4B | W型のトンネル振動 | 時間に依存しない対称W型ポテンシャルについて、障壁値より低い最低偶・奇固有状態のトンネル分裂から左右局在状態を構成し、外部駆動、傾斜切替または障壁低下を用いず、左右領域の占有率が周期的に交換されることを示す。振動数とトンネル分裂の関係、有限時間誤差および単一試行の位置読出しへの接続も示す |
| Q3-5 | 2重スリット干渉 | 有限空間グラフ上の2経路入力について、コヒーレント分布が非干渉混合と異なり、相対位相に応じて位置分布が変化することを示し、位置読出しへ接続する |
| Q3-6 | 位相量子化 | 閉路巻数、節、単価性、位相すべりを一貫して扱い、位相量子化の成立条件を示すことで、Wallstrom 問題へ限定的な回答を与える |

旧Q3-2「位相量子化」は意味と判定基準を保ってQ3-6へ移動した。新Q3-2は別の導出課題である。旧Q3-3はQ3-3A（井戸型）とQ3-3B（調和型）へ分割し、Q3-3C（W型）を追加した。旧Q3-4は意味と判定基準を保ってQ3-4Aへ移動し、Q3-4B（W型のトンネル振動）を追加した。Q3-3とQ3-4は系列の総称とし、独立した達成行は置かない。

#### Q3-1からQ3-6の達成判定の補足

- Q3-1は特定の実装形式を固定しない。結合振動子、古典spin系、連続場その他の局所古典自由度を許すが、採用した古典物理モデルの運動からSchrödinger型有効力学への縮約を示すことを要求する。複素振幅は独立実体でなく実古典自由度の派生表示でもよい。単なるSchrödinger方程式の実・虚部分解や設計済み正準座標への形式的埋め込みだけでは達成としない。現行M37/R86はこの一般基準を満たす一つの達成証人であり、Q3-1の達成ラベルは維持する。
- Q3-2は作用変分経路と時間対称Newton則経路の少なくとも一方を満たせばよく、両方の導出を必須にしない。対象の停留原理または時間対称Newton則をそのまま仮定することや、比較対象のSchrödinger方程式を外部から前提にして書き換えるだけでは達成としない。Schrödinger型発展をミクロから導出済みの場合も、対応する粒子確率過程、平均微分および縮約の接続を示す。位相量子化の大域条件はQ3-6で別に判定する。
- Q3-3A、Q3-3B、Q3-3Cはそれぞれ独立に、有限個の低位固有値・密度・節構造の収束と、明示した環境との弱結合を縮約した有限時間純位相緩和を要求する。環境自由度の有限性は達成条件にしない。現行の有限環境構成はこの条件を満たす強い証人として扱う。1試行の固有状態選択や基底状態への自発緩和は要求しない。
- Q3-4Aは、障壁値未満のスペクトル支持、障壁反対側確率の正の増分、同じ誤差範囲での位置読出し接続を要求する。連続散乱透過率、初回到達、吸収、時間積分流束は強い拡張とする。
- Q3-4Bは、最低偶・奇二重項が障壁値未満にあること、第3状態との正の間隔、静的零傾斜発展、トンネル分裂に一致する振動周期、反対側占有率の正の増分と一周期後の戻り、中央障壁領域を含む完全位置分布、同じ誤差範囲での位置読出し接続を要求する。低2モードの作用比だけを空間領域占有率へ読み替えない。障壁高・幅に対する指数的分裂則は強い拡張とする。
- Q3-5は、有限グラフ上の2経路入力、コヒーレント分布と混合の正の差、相対位相による正の分布差、位置読出し接続を要求する。幾何学的開口、多画素スクリーン、完全検出周期は強い拡張とする。
- Q3-6は未達の研究課題として再開する。非零閉路の整数巻数、零点を通らない変形での保存、節を介した位相すべり、離散化安定性、非整数モノドロミーの排除を全て要求する。

### 共通達成判定規則

各固定目標は、その目標が要求する物理現象、観測統計、入出力または逐次過程を、一試行内で明示的な物理interfaceを介して合成できることを達成判定の共通最低条件とする。上流の実際の物理状態または物理的に保持された出力量を下流へ渡し、解析上の状態ベクトル、試行集団の統計量、Born重み、目標確率表を外部から再注入して接続を代替しない。

固定有限深さの一試行では、有限個の未使用補助自由度、保持対、pointer、作業領域を順次用いてよい。準備、全操作、測定、永久記録、試行間reset、物理clock、次試行renewalを一つのjoint microscopic device/processと共通反復周期へ統合することはM0で要求し、個別固定目標自身が明記しない限りその未完成を未達理由にしない。ただし、同一試行中に使用済み補助自由度を再利用する場合は、その再使用に必要なresetを当該固定目標内で要求する。

固定目標自身が反復運転、一様装置族、資源効率、総時間、精度、反復回数またはresetコストを明示的に要求する場合は例外とする。Q2-4の一様有限規則、多項式外部運用資源、反復回数、総時間、精度およびR186ノイズ条件はQ2-4自身の達成条件として維持する。

### 現在地

「達成」は、固定範囲で基準を厳密に満たすか、任意の $\epsilon>0$ に対して誤差を $\epsilon$ 未満にする有限時間・有限能動部分系の明示構成を選べる状態を指す。浴は明示的なHamiltonian無限浴を用いてもよく、規約を満たす開放ミクロ方程式を基本方程式として直接定めてもよい。形式極限、構成のない収束仮定、無反応試行の事後除外は含めない。各固定目標は上の共通達成判定規則に従って一試行内の物理interfaceを監査し、全周期joint-device統合はM0へ分離する。

M54はQ1、Q2、Q3に共通する有効信号--配置状態構成族である。M37はQ3の空間信号部分系の物理実装層であり、R187条件下ではQ1 W2制御用信号系も局所ばね力学から実装する。M64はQ3の現行粒子・Nelson共通open modelであり、initial preparation、finite-time mean-flow tracking、R161/R185、finite-graph R124/R182/R125接続を担う。R181Bは固定入力テンソル積状態の生成、R181Cは永続記憶部ゲートを担う。M65/R181DはQ1/Q2-2の逐次binary resultとsame-trial post-state handoff、M66/R205A--R205Fは共通thermal-reservoir layer、R206A--R206EはそのQ2-1/Q2-3/Q2-4 terminal joint readout specialization、R206EはQ2-4 root preparation/refreshを担う。R180A/R180CはQ2-2のA端結果形成からB端へ非規格化結果成分を同じ試行のまま渡す2端逐次interfaceを与える。

「根拠となる結果」欄には、その固定目標の達成判定で直接参照する定理・interfaceだけを列挙する。ある直接根拠が内部で利用する結果は推移的依存として重複列挙せず、各定理の依存関係と本文の因果鎖で管理する。従って同じ結果が内部で使われていても、固定目標表へ必ずしも現れない。

| 目標ID | 現在地 | 共通状態構成 | 物理信号系 / 物理実装層 | 系列固有手順 / 受信機構 | 根拠となる結果 | 残る課題 |
|---|---|---|---|---|---|---|
| Q1-1 | 達成 | M54のW2静的状態構成 | M37弱結合W型の最低2正常モード、または抽象2モード実正準信号系 | Q1 W型2モード制御手順（旧M47） | R135、R140、R187 | R187で信号系段階の任意精度M37実装を追加。総時間は $O(\!1/J_\kappa)$ に増え得て、準備・測定機構の同一装置統合は別課題 |
| Q1-2 | 達成 | M54のW2静的状態構成 | R187によるM37のW2制御用信号系＋M65 open selector | Q1 W型2モード測定・Zeno手順（旧M47） | R140、R143--R144、R181D、R187、R189A--R189C、R204D--R204F | Born分布、同軸反復分布、異軸逐次分布と有限2回Zeno証人を導出。2結果主線はM65。全測定部分系の単一ミクロ装置統合は強化課題 |
| Q2-1 | 達成 | M54静的状態構成 | 永続4モード記憶部と逆演算用補助部／作業領域＋M66 terminal sampler | テンソル積状態の生成、ゲート、4結果terminal sampling | R112、R181B、R181C、R206D | 固定深さの一試行で実際の末端4モード信号をM66 terminal samplerへ直接接続し、一回の4結果samplingでBorn分布を得る。固定目標上の残件なし。全周期装置統合はM0課題 |
| Q2-2 | 達成 | M54静的状態構成 | 永続4モード記憶部とA/B二つの物理M65読出し端 | A設定gate、A端M65、projector router、B設定gate、B端M65 | R112、R180C、R181D、R204D--R204E | 固定一重項・固定有限設定族・非空間分離の範囲で一試行逐次interfaceを構成。空間隔離はQ2-2-S、全周期装置統合はM0課題 |
| Q2-3 | 達成 | M54三部分系静的状態構成 | 永続8モード記憶部と逆演算用補助部／作業領域＋M66 terminal sampler | 二段ゲート合成と8結果terminal sampling | R112、R177、R181B、R181C、R206D | 固定3入力の一試行内で第1ゲート後状態を再準備せず第2ゲートへ渡し、GHZ--$T$--逆演算後の8結果をR206Dで直接標本化する。一般サイズ資源効率はQ2-4、全周期装置統合はM0課題 |
| Q2-4 | 条件付き達成 | M54一般静的状態構成 | $2^n$ 受動直接モード記憶部＋M66一様common-reservoir interface | R206E root preparation、一般gate列、R206D $2^n$結果terminal sampling、$n$-bit record | R112、R181C、R186、R206D、R206E | reader側の準備・sampling・readout時間・個別較正条件はM66 common-reservoir samplerで閉じる。残る主要条件はR186のdirect-amplitude register additive-noise/precision障害を多項式外部資源で回避できること |
| Q3-1 | 達成 | M37空間signal | M37実正準空間信号 | Schrödinger型空間包絡 | R86 | clock・終位置record・resetを含む反復周期、A2直接数値再現は強化課題 |
| Q3-2 | 達成 | M37 signal＋M64 continuous tracer | M37実正準空間信号＋M64 signal-driven thermal reservoir＋classical tracer | Nelson型位置過程・時間対称Newton則 | R86、R161、R185、R203A--R203D | process reductionとNewton残差を分離。clock・record・reset反復周期、連続空間一様極限、多粒子は強化課題 |
| Q3-3A | 達成 | — | M37＋R123有限環境 | 束縛状態・純位相緩和 | R86、R123（井戸型） | — |
| Q3-3B | 達成 | — | M37＋R123有限環境 | 束縛状態・純位相緩和 | R86、R123（調和型） | — |
| Q3-3C | 達成 | — | M37＋R123有限環境 | W型束縛状態・純位相緩和 | R86、R123、R182 | — |
| Q3-4A | 達成 | M37有限graph信号＋M64 tracer | M37＋M64 finite-graph profile | 空間移動／終位置読出し | R86、R124、R161、R203D | R124の有限障壁確率移動をM64 tracerの単一試行位置読出しへ接続。clock・永久record・reset・renewalの全周期統合はM0課題 |
| Q3-4B | 達成 | M37静的W型信号＋M64 tracer | M37静的W型＋M64 finite-graph profile | 空間移動 / 半周期・一周期読出し | R86、R182、R161、R203D | R182の半周期移送・一周期回帰をM64 tracerの単一試行位置読出しへ接続。物理clock・永久record・reset・renewalの全周期統合はM0課題 |
| Q3-5 | 達成 | M37有限graph信号＋M64 tracer | M37＋M64 finite-graph profile | 空間移動／2経路位置読出し | R86、R125、R161、R203D | R125の位相依存2経路干渉をM64 tracerの単一試行位置読出しへ接続。clock・永久record・reset・renewalの全周期統合はM0課題 |
| Q3-6 | 未達 | — | 完結物理実装層なし | 完結手順なし | — | 閉路巻数、節を介した位相すべり、細分化安定性、非整数モノドロミー排除を同じ明示的な古典ミクロ構成で示す |

draft-71でR182、W型有限環境系、M42周期輸送系を本文・付録・検算・統合原稿・TeX原稿・PDFへ同期し、Q3-3Cを達成、Q3-4Bを条件付き達成へ更新した。固定目標の文言は変更していない。draft-69以前の履歴にある旧Q3-2は新Q3-6、旧Q3-3は新Q3-3A・Q3-3B、旧Q3-4は新Q3-4Aに対応する。旧稿の達成表現を新Q3-2、Q3-3C、Q3-4Bへ読み替えない。

## 現在の統一導出方針

物理的な導出の主線を、M37の実振動子運動から空間包絡へ進むQ3 signal経路、弱結合W型の低2正常モードからQ1制御運動へ進む経路、M37 signalからM64三実体open modelを介してR161/R185へ進むQ3 particle経路に分ける。R86の空間包絡、R140の射影内制御、R187のQ1受渡し、R203A--R203DのQ3位置過程を区別する。

| 接続 | 導出状態・残件 |
|---|---|
| 静的M37から空間包絡 | R86の既存結果 |
| M37空間signalからQ3粒子輸送 | M64/R203A--R203D。regularized density/current、phase-volume free energy、continuous/finite-graph初期準備、mean-flow tracking、canonical overdamped tracer、R161接続を同じ三実体open modelで閉じる |
| M64から時間対称Newton則 | R203Dの1次元specializationをR161/R185へ接続。process-law reduction errorとNewton force residualを別管理 |
| 静的W型スペクトル・空間トンネル | R182。W型低位スペクトル、障壁下二重項、M37の関数計算、完全位置密度、半周期・一周期を同じ静的系で閉じ、M64 finite-graph tracerへ接続 |
| W型から2準位制御 | R140の射影内結果。高モード漏れ確率と全状態誤差を分離 |
| 有限制御列のM37包絡 | R86の区間合成系と有限切替比較。入力一様な保守上界 |
| M37からQ1への受渡し | R187。弱結合W型で $J_\kappa/G_\kappa\to0$、結合後の低2モード部分空間、静的正常モード分裂較正、有限切替を合成し、固定 $U\in SU(2)$ を任意精度でM37信号系へ持ち上げる |
| W型入力からQ2共同信号系 | 物理抽出・転送が追加課題。既存Q2の必須依存ではない |
| 準備・測定・装置統合 | Q1では準備済み入力境界、射影作用保持、M65読出し、R181D振り分け、外部記録、R179 resetの統合が残る。Q3ではM37 signal、M64 reservoir/tracer、clock、終位置recordを一つの反復周期へ統合するM0が未構成 |

M54の共通状態型による記述、M37/M64による物理実装層実装、M0で要求する同一装置への統合、全外部流路の有限閉鎖Hamiltonian化を区別する。固定目標の達成だけではM0達成としない。

## 現行模型・物理実装層・手順の運用状態

### 共通有効模型族と物理実装層

| 識別 | 分類 | 運用状態 | 役割と限界 |
|---|---|---|---|
| M54 | 共通有効信号--配置状態構成族 | 現行Q1・Q2・Q3の共通有効層 | 準備済み古典入力境界、有限実正準信号、永続記憶部、作業領域、記録、時計自由度の共通型を与える。Q1/Q2-2ではM65/R181D、Q2-1/Q2-3/Q2-4ではM66/R206、Q3ではM37 signalとM64 particle interfaceへ接続する |
| M37 | 物理Hamiltonian信号実装層 | Q3の空間信号部分系、およびR187条件下のQ1 W2制御用信号系 | 局所位置結合された有限実古典振動子網からR86の空間包絡を導く。R187の弱結合W型族では最低2正常モードをM54のW2信号へ正準同定し、R140制御を任意精度で実装する |
| M64 | Q3共通open model | 現行Q3 particle/Nelson実装 | M37 signal、一つのclassical tracer、一つのsignal-driven thermal reservoirからなる三実体模型。R203A--R203Dでcontinuous profileとfinite-graph profileをR161/R185およびR124/R182/R125へ接続する。Hamiltonian lift、finite bath、underdamped lift、連続空間一様極限、多粒子、全周期clock/record統合は強化課題 |
| M65 | Q1/Q2-2 binary canonical open selector | 現行逐次fixed-goal正本模型 | 保持済み二作用を線形rateへ入れる $+,H,-$ の3状態連続時間Markov pointer。R204Dでfinite-time Born、R204Eでbinary selector contract、R204FでQ1 interface/latencyを与える。R204B/R204Cのphase-volume chamber/Hamiltonian liftは強化実現 |
| M66 | common thermal-reservoir parent model | 共通reservoir layer。現行fixed-goalでの直接specializationはQ2-1/Q2-3/Q2-4のR206 | R205A--R205Fでphase-volume、mean-flow、matched capacity--conductance、thermal Gibbs sampling、passive separationを共通化する。M64/M65のdomain modelは置換せず、R206A--R206EがQ2 terminal readoutを担う |

M50はM54の静的状態構成へ、M55はM54空間状態構成へ吸収した。M56はspin-only Q3代替研究線とし現行達成根拠へ使わない。M60/M61とそれ以前のM57/M59は旧Q3 Hamiltonian実装として現行主線から退役し、Git履歴へ保存する。旧状態方向準備、旧作用殻型Q1/Q2測定経路、旧2端再準備は現行必須依存から外し、退役索引と研究メモへ保存する。

M54による統一は共通状態型、因果契約、接続規約の有効層の統一である。M37はsignal、M64はQ3 particle/bathの直接定めた開放模型を与える。これらをM0のjoint device/process統一と同一視しない。

### 系列固有手順 / 受信機構

| 識別 | 使用する共通層 | 現行責務 |
|---|---|---|
| Q1 W型2モード手順（旧M47） | M54のW2静的状態構成＋R187のM37接続 | 準備済みW2入力、R187/R140による制御、射影作用保持、M65による2結果形成、R181Dによる非規格化射影成分受渡し、R143/R144、R189A--R189Cを接続する |
| R180 2端M65受信機構 | M54静的状態構成 | 固定一重項4モード信号にA設定を作用し、A端M65、R181D型の射影成分振り分け、B設定、B端M65を順に接続する非空間分離Q2-2手順。旧R180Bの2端再準備は使わない |

### 統合目標

| 識別 | 分類 | 運用状態 | 役割と限界 |
|---|---|---|---|
| M0 | 単一ミクロ装置統一目標 | 将来目標 | M54の状態構成、物理信号系、Q1/Q2-2の逐次読出し・射影成分振り分け、Q2-1/Q2-3/Q2-4のM66 terminal readout、Q3 particle/reservoir、準備、操作、測定、永久記録、reset、clock、次試行renewalを、有限な能動古典自由度と明示的な相互作用・接続端を持つ一つのjoint microscopic device/processと共通反復周期へ統合する。明示的Hamiltonian無限浴からの縮約、または規約を満たす開放古典ミクロ方程式を基本方程式として直接定めることを許す。Hamiltonian無限浴への持上げ、共通単一bath化、有限浴化、有限閉鎖Hamiltonian全系への持上げは達成条件としない |

M54は共通の状態型と因果契約を与えるが、同じ物理接続部、永続記憶部、制御バス、読出し、記録、リセットを一つの装置architectureと反復周期へ接続したことを意味しない。この強い統合はM0の未完成目標である。M0では規模ごとに同一の有限規則から生成される装置族を許し、設定値まで全規模で同一であることは要求しない。

### M0達成判定

M0は、個別のA1模型を並べるだけでは達成としない。少なくとも次を同時に要求する。

1. Q1/Q2/Q3で用いる主要な実在古典自由度、記録、clock、reset状態が、一つの装置architectureまたは規模ごとの一様な装置族の状態空間として定義されている。
2. module間の物理coupling、port、backreaction、入力境界と出力受渡しが明示され、目的の確率重みまたは量子出力表を外部から直接注入しない。
3. preparation、operation、measurement、record、resetを、同じclock規約を持つ一つの反復周期として接続する。複数のreservoir portを使ってよいが、それぞれの接続先と役割を明示する。
4. 開放模型を使う場合は、各部分のSDE/GLE等を別々に置くだけでなく、全装置のjoint evolutionまたはjoint path measureがwell-definedであることを示し、雑音間の独立性または相関、初期条件、renewal条件を明示する。
5. Hamiltonian無限浴から縮約する部分と、開放ミクロ方程式として直接定める部分を区別し、後者をHamiltonian浴から導出済みとは呼ばない。
6. 各系列の必要なparameter windowが一つのparameter family内で同時に非空であり、規模や入力に応じた有限設定変更を含めても共通interface規則を保つ。
7. Q2-4をM0へ含めて主張する場合は、同じ装置族でR186を含む既存の多項式外部制御・精度・時間条件を満たす。

従って全固定目標のA1達成だけからM0達成は従わない。一方、Hamiltonian無限浴への再導出、全reservoirの単一bath化、有限浴化、有限閉鎖Hamiltonian全系、全周期の完全な微視的仕事・熱・エントロピー収支はM0本体の必要条件ではなく、横断的な上位強化として扱う。

## 現行結果の導出状態

### 共通結果

| 結果 | 導出状態 | 内容 | 主な条件・限界 |
|---|---|---|---|
| R112 | 厳密結果 | 有限正準信号のユニタリ合成、有限時計、安全比較と無反応、正準SWAP、局所記録、テンプレート交換、逆計算 | 結果確率、Born型状態数、粒子位置分布、無期限リセットは従わない |
| R135 | 厳密結果・明示誤差付き結果 | 有限信号集団の規格化第2モーメント輸送、有限時間摂動、階数1支持、2次元Bloch幾何 | 非中心化第2モーメント。単一試行信号との区別が必要 |
| R161 | 厳密結果 | 正の対象分布、反対称確率流、対称活動量から前向き率を構成し、有界総hazard下で一意な非爆発canonical Markov経路法則とBayes後退率まで与える。静的特殊化で平方根型詳細釣り合い・一意定常分布・一様混合上界、空間特殊化で旧R183移動分布の整合を回収 | 固定有限時間・有限状態。静的/移動の活動量選択を別途指定。$\delta\downarrow0$ で資源発散 |
| R162 | optional Poisson realizationの厳密結果 | R161 canonical経路法則を独立Poisson random measuresでpathwiseに実現する。経路存在・周辺整合・Bayes後退率はR161側で既に閉じるため、Q3-2達成根拠には含めない | 固定有限時間・有限状態。有限衝突Hamiltonian列への持上げは強化結果として退役メモへ分離 |
| R168 | 厳密結果・明示誤差付き結果 | 安全事象を含む一般状態方向平均からM54条件付き結果統計への受渡し | 階数1、固定作用、可変作用補正を区別。無反応を再規格化しない |

### Q1結果

| 結果 | 導出状態 | 内容 |
|---|---|---|
| R140 | 厳密結果・明示誤差付き結果 | W型2モードの任意の $SU(2)$、零傾斜占有振動、離調Rabi式、傾斜保持 |
| R187 | 厳密有限次元結果・明示誤差付き構成 | M37弱結合W型で $J_\kappa/G_\kappa\to0$ を構成し、結合後の低2モード部分空間、静的正常モード分裂較正、有限切替、W2への正準接続端から固定 $U\in SU(2)$ の任意精度信号系実装を与える。総時間は $O(\!\mathcal J_0/J_\kappa)$ |
| R189A | 厳密有限次元結果・明示誤差付き構成 | 零傾斜R187 W2を停止せず、未使用作用容量指針変数への有限正準保持を行う。理想未使用運動量では信号反作用は零、対称有限窓の作用比誤差は $O(\!\Omega_\kappa^2)$ |
| R189B | 条件付き・明示誤差付き結果 | R189Aで固定した2作用を走行中信号から切り離してM65へ渡し、finite record後の有限後段窓で零傾斜Rabi継続中の階数1制御付き選別機構を完了する。選択遅延と選別窓重なりを明示評価し、中間傾斜・記録・R192を使わない |
| R189C | 条件付き・明示誤差付き有限証人 | 同一M37 W2で $N=2$、$\Omega_\kappa T=\pi/2$ を固定し、測定運転 $3/4$、自由・空操作対照 $1/2$、理想余裕 $1/4$ のRabi--Zeno比較を無反応を含む完全履歴と有限誤差で閉じる |
| R143 | 条件付き・明示誤差付き結果 | Q1 W型2モードの分析器、有限コントラスト、傾斜保持、局所記録とR181Dの深さ1測定後状態の受け渡しの特殊化 |
| R144 | 条件付き・明示誤差付き結果 | R143の固定有限段逐次測定合成、無反応を含む完全履歴分布、R181Dの選択後信号の直接受渡し、分布誤差とトレース距離による状態誤差の有限和 |

旧R181AのW型2モード準備対応は現行主線から退役し、notes/Git履歴へ保存する。付録HはR135/R140/R187/R189A--R189C/M65/R181DのW2対応表だけを置く。永久記録、補助逆計算、未使用素子交換リセットはR144から分離し、第3章と付録Bの無番号実装強化系として保持する。

### Q2結果

| 結果 | 導出状態 | 内容 |
|---|---|---|
| R181B | 厳密結果・明示誤差付き結果 | 一般積入力を係数読出しなしに $Z_S=a\otimes b$ と逆演算用補助記憶部へ写す有限時間可逆テンソル積状態の生成 |
| R181C | 厳密結果・明示誤差付き結果 | 同じ永続状態浴上の有限ゲート列、CNOT、局所操作、逆演算、参照系安定な作用素-ノルム誤差合成 |
| R181D | 条件付き・明示誤差付き結果 | binary selector contractで固定された2値結果に従う可逆projector routerと非規格化測定後状態受渡し。現行fixed-goalではQ1逐次測定とQ2-2 A端--B端handoffに用い、Q2-1/Q2-3/Q2-4のterminal samplingには用いない |
| R177 | 条件付き厳密結果 | R181B/R181CのA--B、B--C二段合成とR206Dの8結果terminal samplerを使うGHZ--$T$--逆演算証人。コヒーレント分布と完全位相緩和分布の全変動距離は $1/(2\sqrt2)$ |
| R179 | 直接定めた開放方程式に対する厳密結果・明示誤差付き結果 | 一様開放リセット、定常流入浴、流出履歴排出、反復時の履歴条件付きrenewal。現行fixed-goalではQ2-2と全周期renewal側に残し、Q2-4 direct dependencyから外す | 浴接続部は回路出力確率やモード別係数を入力しない一様有限記述。有限低温／使用済み貯蔵部と部分SWAP列は強化課題 |
| R186 | 厳密有限次元結果・明示誤差付き障害条件 | M54直接モードの射影型頑健性。疎な静的ハミルトニアン製造誤差、独立モード位相ノイズ、射影結果の固定機構の相対係数誤差は指数部分系数を直接加算せず評価できる。一方、各モードへ空状態でも作用を注入する等方加法ノイズでは横方向ノイズ作用が $(2^n-1)\sigma^2$ に比例し、多項式信号作用の下で指数ノイズ抑制が必要になる |
| R180A | 厳密結果・明示誤差付き結果 | M54の実際の1試行末端信号へA設定basis gateを作用し、A側射影作用をM65へ渡す。A結果でR181D型projector routerを制御し、非規格化結果成分をB端へ渡すQ2-2特殊化 |
| R180C | 条件付き・明示誤差付き結果 | A端M65、R181D型projector router、B設定gate、B端M65、二つの記録とR179 resetを合成し、固定一重項でBorn共同分布、非信号性、CHSH値、Bell前提監査を与える |

### Q3結果

| 結果 | 導出状態 | 内容 |
|---|---|---|
| R86 | 厳密結果・明示誤差付き結果 | M37の正確局所包絡方程式、生成子誤差、有限時間Schrödinger型近似、作用変動、有限基底診断 |
| R203A | 厳密恒等式・明示誤差付き近似 | M37 edge signalの作用和・差からregularized density/current dictionaryを作り、smooth sectorで $c_Jr_e$ を $v_{\delta,e}$ へ有限誤差で接続する |
| R203B | 厳密partition結果・有限時間結果 | signal-dependent reservoir phase volumeから $F_{\rm res}=-k_BT\log r_X^\delta+C$ を導き、continuous tracer初期準備とfinite-time mean-flow trackingを与える |
| R203C | 直接定めた開放SDEに対する厳密結果・明示誤差付き縮約 | canonical overdamped tracerをideal regularized diffusionへ有限時間 $W_1$ で縮約する |
| R203D | 厳密有限graph結果・明示誤差付き近似結果 | local $R_i^\delta,J_{ij},T_{ij}^\delta$ からR161 rateを構成し、finite-graph初期準備、1次元R185 activity、R124/R182/R125位置読出しへ接続する |
| R204A | 厳密結果 | M65の3状態canonical open generatorを定め、確率保存、保持作用への線形rate入力、Born確率表・状態依存除算を外部入力しないことを示す |
| R204B | 強化候補・reduced-law結果 | fixed-hub phase-volume chamberで $V_r,G_r\propto a_r$、$V_H$固定とし、R204Aのrateをcapacity/conductance比から再現する |
| R204C | 強化候補・明示誤差付き結果 | Hamiltonian bath、overdamped、phase-volume tracking、tube、lumping、calibrationからR204A open generatorへのfinite-time lift誤差を与える。M65正本の必須依存ではない |
| R204D | 厳密結果・明示誤差付き合成 | M65の有限時間Born readout、exact endpointを含む正式な無反応、decision終了時のR112型record/latch、complete-result TV上界、小Born重みでrelaxation rateが縮まないことを与える |
| R204E | 厳密系 | M65がR181Dのbinary selector contractを満たすことを示す |
| R204F | 条件付き・資源結果 | Q1 R189A→M65→R181D互換性、空操作対照の自由Rabi継続、弱結合latency極限を与える。Q2-4 terminal readout資源はR206C--R206Eへ移す |
| R205A | 厳密partition結果 | 正のlocal scaleをreservoir座標Jacobianへ入れるとcanonical phase volumeがscaleへ線形比例し、free energyが \(-k_BT\log w+C\) になる共通identity |
| R205B | 厳密reduced-law結果 | channel capacityとconductanceへ同じlocal scaleを掛けると、channel→hub rateがscale非依存、hub→channel rateがscale比例となるmatched capacity--conductance原理 |
| R205C | 厳密partition結果 | moving reservoirの運動量平行移動 $U$ とphase-volume weight $w$ がcanonical free energyで直交し、$F_{\rm res}=-k_BT\log w+C$ と $-\nabla F_{\rm res}=k_BT\nabla\log w$ を同時に与える |
| R205D | 厳密系 | R205Bのbinary fixed-hub特殊化からR204Bの $k_{y\to H}=\Lambda$、$k_{H\to y}=\kappa a_y$ を回収する |
| R205E | 厳密reversible open-SDE結果・条件付き有限時間結果 | $H_{\rm eff}=H_{\rm cfg}-k_BT\log w$ のoverdamped thermal samplerが $p_{\rm eq}\propto we^{-\beta H_{\rm cfg}}$ を可逆定常分布に持ち、Poincaré gap下で指数mixingする |
| R205F | 厳密generator結果・明示誤差付き分離 | 距離依存相互作用 $K(R)$ とreservoir cross-diffusion $C_{AB}(R)$ のgenerator defectを評価し、両者が消えると固定local bath couplingのまま $\mathcal L_A+\mathcal L_B$ へ分離する |
| R206A | 厳密有限状態結果 | 任意有限Lのcommon-hub samplerで \(d_y=x_y-p_y(1-h)\) が \(\dot d_y=-\Lambda d_y\) を満たし、mixing rateがLと最小Born重みに依存しない。任意pointer初期分布から指数収束する |
| R206B | 厳密一様構成結果 | \(L=2^n\) channelへ同一local scale則、\(V_H\propto L\) を用いて総hub escape rateをL非依存に保ち、regularized Born重みを個別係数表なしに実装する |
| R206C | 厳密有限時間・製造誤差結果 | finite-time mixing、hub residual、regularization、generator/record誤差をL非依存に合成し、local multiplicative/additive scale誤差の規格化TV上界を与える |
| R206D | 条件付きQ2 bridge | R181C後の実terminal signal作用を4・8・\(2^n\)結果common samplerへ接続し、Q2-1/Q2-3/Q2-4のone-shot terminal readoutを与える。外部Born表・振幅表・全channel走査を使わない |
| R206E | 直接定めた開放方程式に対する厳密結果 | 全mode共通減衰と固定 \(0^n\) root driveから任意前試行状態をrootへ指数収束させ、Q2-4準備時間を対数精度依存に抑える。sampler pointerはR206A mixingにより結果別reset不要 |
| R207A | Q2-2-S候補・厳密対称性結果 | M66/R205Eのcontinuous Gibbs preparationを二つのrotorと双安定setting precursorへ特殊化し、4 setting sectorの厳密な公平性 $P(x,y)=1/4$ を与える |
| R207B | Q2-2-S候補・解析存在結果＋数値witness | deep-well/strong-lock reductionでCHSH相関族を構成し、有限 $\kappa_*$ で $|S|=2\sqrt2$、各局所周辺 $1/2$ を与える。finite-lock witnessはcandidate quadratureで検査する |
| R207C | Q2-2-S候補・条件付き因果分離結果 | R205Fのpost-separation generator factorizationとlocal responseを使い、CHSH witnessではmeasurement independenceが成立しないことを分離して監査する。finite-speed spatial reservoirは未監査 |
| R207D | Q2-2-S候補・Bell-local control | measurement independenceとlocal response factorizationを同時に課す対照系で $|S|\le2$ を示し、strong-lock $\kappa=0$ では $|S|=2$ を回収する |
| R185 | 厳密有限格子結果・明示誤差付き近似結果 | 共通の確率分布の時間反転率、$D_\pm$、1次元node-free領域の時間対称Newton則。正則化残差 $O(\delta)$、格子残差 $C_{185,a}a^2$ を有限微分ノルムで明示 |
| R123 | 厳密結果・数値検証付き | 井戸型・調和型低位束縛状態と有限環境純位相緩和 |
| R124 | 厳密結果・数値検証付き | 障壁値未満スペクトル支持からの反対側確率増分 |
| R125 | 厳密結果・数値検証付き | 有限2経路のコヒーレント分布差と位相依存性 |
| R182 | 厳密結果・数値検証付き | 対称W型の固定低位スペクトル・密度・節収束、障壁値未満二重項と第3ギャップ、M37分裂評価、中央障壁込みの半周期鏡映と一周期回帰 |

## 物理的解釈と境界

- M54が準備する $C_Z\simeq cc^\dagger$ は試行集団の統計状態である。各試行の実体は実正準信号、開放接続部、制御器、記録器と履歴であり、$c$ または $C_Z$ を単一試行制御器へ再注入しない。
- Q3の単一試行ではM37の実正準空間信号、一つのclassical tracer、一つのsignal-driven thermal reservoirが物理過程を担う。複素包絡、$\rho$、$j$、$U$ は派生量またはcollective variableである。R162 Poisson realizationはR161 lawのoptional referenceであり、Q3-2の達成根拠にも基礎的存在論にも含めない。
- Q3の位置重みとosmotic driftはM64/R203Bのphase-volume free energyとregularized signal densityから導く。開始面で位置を一度だけ準備し、その後は同じtracerをcontinuous SDEまたはfinite-graph jump lawで発展させる。毎時刻再標本化しない。
- R161はM64に固有でなく、拡散を担う対称活動量と確率流を受け取り、有限状態canonical Markov経路法則まで定める共通数学interfaceである。$\delta>0$ はM64のregularization背景として用い、$\delta\downarrow0$ で率感度と実装資源が発散し得る。
- M54の $Z_S$ とR180が保持する $\widetilde V=Z_{\rm out}(\omega)$ は1試行の実正準状態から得る物理的な派生信号であり、M54の $c,C_Z$ または旧M48の集団交差モーメントではない。$V=\widetilde V/\|\widetilde V\|$ は解析上の状態方向であって、正準SWAPが状態依存除算を行うわけではない。
- M54の有限モード、逆演算用補助記憶部、供給源、作業領域、時計自由度履歴はゲート間で永続させる。外部制御器は内部モードを個別に初期化、較正、同期、個別指定、読出し、リセットしない。
- M54の指数的信号、作業領域、履歴、低温、使用済み自由度は受動貯蔵部として許す。外部制御器は局所ゲート名、ビット添字、時計自由度窓だけを指定し、Born重みまたは最終確率表を入力しない。
- Q2-4の比較対象はブラックボックスとしての運用上の複雑度である。内部モード、静的結合器、装置体積、総熱の総量は別の報告対象の内部資源として保持し、指数的であるだけでQ2-4を否定しない。ただしそれらがモード別較正、指数精度、指数時間として外部接続部へ露出すれば失敗とする。R186はこの露出のうち製造誤差とノイズの境界を定量化する。
- R181Dはbinary selector contractで固定された安全結果 $r$ に従い、可逆な射影成分の振り分けによって $P_rZ$ と補成分を分け、非規格化 $P_rZ$ を同じ試行の次段へ渡す。現行fixed-goalではQ1/Q2-2の逐次handoffにだけ使う。Q2-1/Q2-3/Q2-4はterminal M66/R206 samplingを用い、結果成分treeや作用回復を使わない。
- 現行R180CのCHSH不等式の破れは、設定前の一重項源を設定非依存に保ったままA端結果成分をB端へ物理的に渡す非空間分離逐次構成で得る。従って現行証人はBell局所因子化を満たす空間分離模型ではない。Q2-2固定目標は特定のBell前提違反を先に指定せず、採用構成ごとに前提の成立・不成立を監査する。
- 有限熱化または外部時刻割当から独立同分布型有限標本揺らぎは従わない。
- Q1--Q3を同じ装置、同じ基準分布、同じ反復周期へ統合したとは主張しない。

## 未解決問題

未解決問題では、有限閉鎖Hamiltonian化そのものを共通到達点としない。M0本体では有限な能動古典自由度、共通接続部、準備・操作・測定・記録・リセット・clockを一つのjoint microscopic device/processと反復周期へ統合する。浴・散逸・雑音は明示的Hamiltonian無限浴からの縮約として与えてもよく、規約を満たす開放ミクロ方程式として直接定めてもよい。Hamiltonian無限浴への持上げ、共通単一bath化、有限浴近似、有限再帰、有限総容量、全周期の完全な微視的熱力学は別の強化課題とする。

1. Q1ではR189A作用保持、M65 selector、R112型record、R181Dの射影成分振り分け、未使用保持対SWAP／R179 open resetをM37 W2信号系と同じ具体装置・時計自由度へ接続し、測定部分系の単一装置統合と周期収支を閉じる。
2. Q2-1/Q2-3では永続多モード記憶部、M66 terminal sampler、recordを同じ具体装置・時計割当へ統合することはA1/M0の強化課題として残る。fixed-goalの一試行interface自体はR206Dまで閉じている。
3. Q2-2について、固定一重項4モード信号、A/B設定操作、二つのM65読出し端、R181D型の射影成分振り分け、記録、R179開放リセットを同じ非空間分離装置と時計割当へ統合する。
4. Q2-4について、R206E root preparation、R181C gate列、R206 terminal samplerの一様規則と多項式外部運用資源はfixed-goal主線で閉じる。残る条件は、製造ばらつきと運転中の揺らぎを実装模型から導き、R186の多項式精度条件を満たし、全自由度へのadditive noiseが生む指数障害を回避できる範囲を示すことである。
5. Q3の強化として、M37空間signal source、M64のsignal-driven thermal reservoirとtracer、時計自由度、終位置recordを同じ反復装置周期へ統合し、M64で直接定めた開放方程式そのもののA2直接数値再現を行う。あわせて、生M37局所包絡から時間対称Newton則へより直接に進む縮約、finite-bandwidth/Hamiltonian lift、continuous-space一様極限、多粒子拡張を検討する。
6. Q3-6の位相量子化について、閉路巻数、節を介した位相すべり、細分化安定性、非整数モノドロミー排除を同じ明示的な古典ミクロ構成で閉じる。

## 置換・退役結果

現行因果鎖に含まれない模型と結果は本文へ再掲しない。主要な現行因果鎖と置換系譜の入口は `notes/theory_lineage.md`、ID、旧用途、退役時点の置換関係、研究メモへの対応は `notes/superseded_result_index.md` で管理する。個別退役メモに残る「現行」「置換先」はその版の歴史記録であり、現在の運用状態は本書を優先する。旧R113--R118、R147、R153、R155、R183は再利用しない。独立M48 Bell 手順はR180A--R180Cへ置換した。M42/R172--R174はdraft-72でM55/R183--R185へ移行し、draft-74でM55をM54空間状態構成、R183を一般R161へ吸収した。M50もM54静的状態構成へ吸収した。draft-95でR162のPoisson reservoirをQ3基礎ミクロ存在論からideal referenceへ責務変更し、旧位置づけは `notes/superseded_q3_poisson_microphysics.md` へ保存する。M56はspin-only代替研究線として保持する。draft-103でM59と独立M57/dual-TLの現行親模型としての役割をM60へ置換し、R195A/R196A--R196CはM60 transport reductionの結果IDとして継承した。draft-112ではM64/R203A--R203DをQ3現行主線へ昇格し、M60/M61とR195--R200を現行正本から退役する。draft-120ではM65/R204D--R204Fを当時のQ1/Q2 fixed-goal主線へ採用し、R191/R193を退役する。draft-127ではQ2-1/Q2-3/Q2-4のterminal readoutをM66/R206へ置換し、Q1/Q2-2のM65/R181Dを維持したまま、責務を失ったR192をactive paperから退役する。
