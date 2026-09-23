# PR固有の移行検査

このディレクトリは、特定の理論再編・名称変更・依存関係変更を安全に完了させるための一時検査を置く。

例:

- 旧模型名が現行説明へ残っていないか
- 退役した結果IDが現行の必須依存へ再混入していないか
- あるPRで置換対象にした旧文言が残っていないか
- 大規模移行で必要なファイル群が新体系へ同期したか

これらは重要な作業検査だが、長期に安定した理論不変条件ではない。

## ルール

- `.github/workflows/verify.yml` から呼ばない。
- `check_source.py` へ移植しない。
- 特定のM/R/Q番号、section名、文章断片を使ってよい。
- 対象PRの完成状態を作るために手動実行する。
- 移行完了後は削除してよい。
- 残す場合も履歴・再移行手順として扱い、恒久CIのhard contractにはしない。

恒久CIへ昇格させたくなった場合は、まずその検査を「番号や文章表現を変えても真である不変条件」に一般化できるかを確認する。


## draft-117 M65 open selector昇格

`check_draft117_m65_open_selector.py` は、M65がcandidate文言からcanonical open selectorへ同期され、R181Dがbinary selector contractへ一般化され、M65 core検算とHamiltonian/Brownian candidate検算の境界が正しく移行したことを確認する。PR固有の移行検査であり恒久CIへは入れない。


## draft-119 M65 retirement-readiness

`check_draft119_m65_retirement_readiness.py` は、M65のexact endpoint、finite record/latch、Q1 retirement-readiness合成、A12旧作用殻主線の整理を確認する。同時にA20/A21とR191/R193 required verifierがまだ存在することを検査し、本PRが退役そのものを先取りしていないことを固定する。


## draft-120 R191/R193 retirement

`check_draft120_retire_r191_r193.py` は、R191/R193のactive付録・required verifierが退役し、notesへ保存され、Q1/Q2 fixed-goal主線と状態表がM65/R204D--R204Fへ切り替わったことを確認する。過去draft記録中のR191/R193表記は履歴として許可する。

## draft-121 fixed-goal single-trial policy

`check_draft121_single_trial_fixed_goal_policy.py` は、個別固定目標を一試行内の物理interfaceで判定し、永久記録・試行間reset・物理clock・次試行renewalの全周期統合をM0へ分離した新原則を確認する。同時にQ2-1/Q2-2/Q2-3/Q3-4A/Q3-4B/Q3-5の達成、Q2-4の条件付き達成、Q3-6とM0の未達、および旧full-device残件文言のactive sourceへの再混入を検査する。

## draft-122 active dependency sync

`check_draft122_active_dependency_sync.py` は、固定目標の根拠欄を直接依存だけへ揃え、Q1/Q2をM65/R181D、Q3位置読出しをM64/R203Dへ同期したことを確認する。R164/R170/R184の退役は後続変更へ分離し、本検査ではこれらのactive theorem/proofがまだ存在することも確認する。

## draft-123 retire R184 Q3 rate-latch route

`check_draft123_retire_r184.py` は、R184がactive section・現行結果表・required verifier責務から外れ、M64/R203A--R203D→R161/R185へQ3主線が一本化されたことを確認する。R184の主張は退役メモとGit履歴へ保存し、R164/R170の次段退役はこの検査の対象外とする。

## draft-124 retire R164/R170 action-shell measurement route

`check_draft124_retire_r164_r170.py` は、旧作用殻測定経路がactive `sections/` から消え、付録Lが削除され、付録KがR161/R162の一般Markov経路だけへ縮約されたことを確認する。Q1/Q2はM65/R181D、Q3はM64/R203A--R203D/R161/R185へ一本化し、固定目標ラベルは変更しない。

## draft-125 history notes and permanent consistency checks

`check_draft125_history_consistency.py` は、履歴入口 `notes/theory_lineage.md`、退役メモの現行注記、恒久 `check_project_consistency.py`、通常CI接続、検算ポリシーの自己検査が同じ変更で導入されたことを確認する。固定目標の達成ラベルと理論主張を変更しないこともPR固有に確認する。

## draft-126 M66/R206 candidate

\`check_draft126_m66_r206_candidate.py\` は、A27のM66/R205--R206候補とcandidate verifierが存在し、Q2-1/Q2-2/Q2-3/Q2-4の達成ラベル、M65/R181D/R192/R179の現行主線、R186障害が変更されていないことをPR固有に検査する。後続promotion/retirementは別PRで扱う。

## draft-127 M66/R206 promotion and sequential Q2 terminal retirement

`check_draft127_promote_m66_r206.py` は、Q2-1/Q2-3/Q2-4の直接依存がM66/R206へ切り替わり、Q1-2/Q2-2のM65/R181D逐次interfaceが維持され、R192だけがactive theorem/required verifierから退役したことを確認する。Q2-4はR206E root preparation、R181C gate列、R206D terminal sampling、R186 robustnessへ縮約し、条件付き達成ラベルを維持する。

## draft-128 M65/M66 appendix split

`check_draft128_split_m66_appendix.py` は、M66/R205--R206がA24/付録Xへ移され、A26/付録ZがM65/R204専用へ戻ったことを確認する。R205/R206の結果ID、Q2-1/Q2-3/Q2-4の直接依存、Q1/Q2-2のM65/R181D主線、Q2-4の条件付き達成とR186障害が変わっていないこともPR固有に検査する。A26に残るR206への責務境界参照は許容し、M66本体節とR205/R206定理宣言だけを移設対象とする。理論拡張や新結果追加はこの検査の対象外とする。

## draft-129 M66 common-reservoir parent

`check_draft129_m66_common_reservoir_parent.py` は、R205C--R205FがA24で正式結果として宣言され、M66がcommon thermal-reservoir parentへ分類変更されたことを確認する。同時にM64/R203、M65/R204、R206の既存正本、Q1/Q2/Q3のfixed-goal直接依存・達成ラベル、R186障害が維持され、R207/Q2-2-Sを先取りしていないことをPR固有に検査する。

## draft-130 R207 Q2-2-S candidate

`check_draft130_r207_q2_2_s_candidate.py` は、A23/付録WのR207A--R207D、candidate verifier、R205E/Fとの接続を確認する。同時にQ2-2 fixed-goalのR180C--M65/R181D主線と達成ラベル、Q2-2-Sの未監査状態が維持され、R207がfixed-goal直接依存へ昇格せず、M67を新設していないことをPR固有に検査する。

## draft-131 Q2-2-S management sync

`check_draft131_q2_2_s_management_sync.py` は、第5章と `ENHANCEMENT_TARGETS.md` のS0--S4対応、finite-speed spatial reservoirをS2主要blockerとする現在地、R207のcandidate-only境界を確認する。同時にQ2-2 fixed-goalの直接依存・達成ラベルとQ2-2-S全体の `未監査` 状態が変わっていないことを検査する。理論式やcandidate physics verifierの変更は対象外とする。

