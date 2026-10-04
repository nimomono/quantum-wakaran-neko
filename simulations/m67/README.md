# M67 supporting simulations

M67の現行Q3 continuous supporting witnessはR214 dumbbell profile、Q2 thermal supporting witnessはR212、Q2 NBL/path candidate witnessはR213を使う。旧R208B/R208C/R209C phase-volume continuous bridgeの `run_full_compatibility_witness.py` はdraft-146でactive treeから退役し、Git履歴を保存先とする。

Q3-1-A2/Q3-2-A2の公式状態は変更しない。required解析検算とsupporting simulationを区別し、reduced witnessだけからA2を昇格しない。

## R212B spherical-rotor thermal witness

`run_r212b_rotor_mixing_witness.py` はR207で実際に使う `eta=1/4`、`epsilon=eta/8=1/32`、`k=2/eta=8` を固定し、`S^2 x S^2` のoverdamped rotational R205E lawを直接積分するsupporting witnessである。terminal lawを exact target `exp(k lambda_A.lambda_B) [w_A+w_B]` からの直接sampleと比較し、sphere constraint、coarse-grained TV距離、orientation memoryを確認する。R212B-rot本文のfinite-Hamiltonian→open reductionをこのsimulation単独で証明するものではない。

通常実行は45度settingの軽量witness、`--full` は6000 trajectory、`--angle-sweep` は0/45/90/135/180度を走らせる。finite harmonic bathの明示parameter windowとDrude kernel/recurrenceは `tools/verify_r212b_rotor_parameter_window.py` が別に検査する。このwitnessはR212B正本化後もsupporting numerical evidenceとして扱い、required CIやQ2-2 fixed-goal/A2判定を単独では変更しない。


## R213 NBL/path Q2 witness

`run_r213_nbl_q2_witness.py` はrandom H/T/CNOT回路についてdirect state-vector、phase-tagged path expansion、coherent collector出力を比較し、destructive-interference caseも検査する。R213A--R213Dのsupporting witnessであり、abstract unitary dilationのlocal physical decomposition、R206 full finite-Hamiltonian lift、Q2-4 promotionを単独では証明しない。

## R214 dumbbell Q3 witness

`run_r214_dumbbell_q3_witness.py` はrequired R214Bのreduced 3D overdamped dumbbellを直接標本化し、半径分布を $r^2\exp[-(r-\ell)^2/(2\sigma_T^2)]$ と比較するsupporting witnessである。finite harmonic bath→GLE/FDT→Markov極はgeneric R209B解析bridgeを再利用するため、このscript単独はfull finite-Hamiltonian direct trajectoryでもQ3-2-A2達成証拠でもない。
