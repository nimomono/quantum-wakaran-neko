# M67 二実体Hamiltonian candidate simulation

M67/R208A--R208Dのdirect-trajectory強化検証入口。draft-137ではQ3-1-A2/Q3-2-A2の公式状態を変更しない。

検査対象はM37 coherent sectorとの差、phase-volume force、local edge flow、finite moving bathのmemory/FDT/recurrence、tracer経験分布、Hamiltonian energy drift、N0/Nrho/格子幅/tau_U/tau_mem/bath mode数の独立sweepである。

`run_reduced_witness.py` は高速な縮約witnessである。draft-138では `run_full_compatibility_witness.py` を追加し、coherent signal、phase-volume bath、edge-flow reaction coordinate、finite flow bath、moving material frame、finite local drag bath、tracerを一つの有限Hamiltonian ODEで同時積分する。外部white noiseは注入せず、thermal randomnessは初期canonical ensembleだけから入れる。energy drift、M37 ideal signalとのray error、local flow error、material-frame recoil、finite-bath recurrenceを同じtrajectoryで監査する。これはM67→M64 compatibilityのdirect witnessであり、Q3-1-A2/Q3-2-A2の正式達成へは数えない。
