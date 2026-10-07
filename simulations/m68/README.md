# M68 supporting simulations

M68/R216A--R216Dはcandidate-onlyであり、このdirectoryのwitnessはfixed-goal/A2達成証拠ではない。

`run_joint_feedback_witness.py` はlinear Gaussian feedback toy modelを使い、single-tracer feedbackでannealed equivariance defectが \(O(C^{-1})\)、mean medium biasが \(O(C^{-2})\) になることをcapacity familyで確認する。finite-bath dumbbellのrequired bridgeはR214B/R209Bを再利用し、このscript単独ではfull finite-Hamiltonian trajectoryを証明しない。
