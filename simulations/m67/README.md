# M67 Q3 physical-parent supporting simulations

M67/R208A--R210Bのsupporting direct-trajectory検証入口。draft-139でM67はQ3 physical parentへ昇格するが、Q3-1-A2/Q3-2-A2の公式状態は変更しない。

検査対象はM37 coherent sectorとの差、phase-volume force、local edge flow、finite moving bathのmemory/FDT/recurrence、tracer経験分布、Hamiltonian energy drift、N0/Nrho/格子幅/tau_U/tau_mem/bath mode数の独立sweepである。

`run_reduced_witness.py` は高速な縮約witnessである。draft-138では `run_full_compatibility_witness.py` を追加し、coherent signal、phase-volume bath、edge-flow reaction coordinate、finite flow bath、moving material frame、finite local drag bath、tracerを一つの有限Hamiltonian ODEで同時積分する。外部white noiseは注入せず、thermal randomnessは初期canonical ensembleだけから入れる。energy drift、M37 ideal signalとのray error、local flow error、material-frame recoil、finite-bath recurrenceを同じtrajectoryで監査する。これはM67→M64 compatibilityのdirect witnessであり、Q3-1-A2/Q3-2-A2の正式達成へは数えない。

draft-139ではR210A/R210Bをrequired解析検算へ追加し、既存full compatibility witnessはsupporting evidenceとして維持する。envelope-level full witnessだけをA2 promotion testへ読み替えず、M37 carrier反回転項はR210Aの解析bridgeで管理する。

## R212B spherical-rotor thermal witness

`run_r212b_rotor_mixing_witness.py` はR207で実際に使う `eta=1/4`、`epsilon=eta/8=1/32`、`k=2/eta=8` を固定し、`S^2 x S^2` のoverdamped rotational R205E lawを直接積分するsupporting witnessである。terminal lawを exact target `exp(k lambda_A.lambda_B) [w_A+w_B]` からの直接sampleと比較し、sphere constraint、coarse-grained TV距離、orientation memoryを確認する。R212B-rot本文のfinite-Hamiltonian→open reductionをこのsimulation単独で証明するものではない。

通常実行は45度settingの軽量witness、`--full` は6000 trajectory、`--angle-sweep` は0/45/90/135/180度を走らせる。finite harmonic bathの明示parameter windowとDrude kernel/recurrenceは `tools/verify_r212b_rotor_parameter_window.py` が別に検査する。このwitnessはR212B正本化後もsupporting numerical evidenceとして扱い、required CIやQ2-2 fixed-goal/A2判定を単独では変更しない。


## R213 NBL/path Q2 witness

`run_r213_nbl_q2_witness.py` はrandom H/T/CNOT回路についてdirect state-vector、phase-tagged path expansion、coherent collector出力を比較し、destructive-interference caseも検査する。R213A--R213Dのsupporting witnessであり、abstract unitary dilationのlocal physical decomposition、R206 full finite-Hamiltonian lift、Q2-4 promotionを単独では証明しない。

## R214 dumbbell Q3 witness

`run_r214_dumbbell_q3_witness.py` はR214Bのreduced 3D overdamped dumbbellを直接標本化し、半径分布を $r^2\exp[-(r-\ell)^2/(2\sigma_T^2)]$ と比較する。finite harmonic bath→GLE/FDT→Markov極はR209B型解析bridgeを再利用するため、このscript単独はfull finite-Hamiltonian direct trajectoryでもQ3-2-A2 promotion testでもない。
