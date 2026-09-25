# M67 二実体Hamiltonian candidate simulation

M67/R208A--R208Dのdirect-trajectory強化検証入口。draft-137ではQ3-1-A2/Q3-2-A2の公式状態を変更しない。

検査対象はM37 coherent sectorとの差、phase-volume force、local edge flow、finite moving bathのmemory/FDT/recurrence、tracer経験分布、Hamiltonian energy drift、N0/Nrho/格子幅/tau_U/tau_mem/bath mode数の独立sweepである。

run_reduced_witness.py は高速な縮約witnessであり、有限bath全自由度を含むA2 full trajectoryの代替ではない。
