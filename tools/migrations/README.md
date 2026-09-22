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
