# M64 direct simulation registry

This folder is the future A2 registry for the M64/R203A--R203D three-entity open-Q3 replacement candidate.

M64 adopts three physical entities: an M37-type classical coherent signal, one classical tracer, and one signal-driven moving thermal reservoir. The reservoir density port, local mean flow, friction and thermal noise are different collective roles of the same environment rather than separate physical entities.

A direct M64 simulation should evolve the adopted equations themselves in one parameter set:

1. the M37 signal equation or its explicit real-canonical oscillator form;
2. the local reservoir-flow relaxation law
   `tau_U dU_e/dt = -U_e + c_J r_e + R_U,e`;
3. the tracer underdamped Langevin SDE with constant `T` and `gamma_X`.

At minimum report:

- current-dictionary error and `U-j/rho` tracking error;
- conditional mean force versus `k_B T partial_X log rho`;
- tracer forward drift versus `j/rho + nu partial_X log rho`;
- tracer diffusion coefficient versus `nu=k_B T/gamma_X`;
- empirical tracer density versus the signal density on the node-free safe sector;
- finite-volume R161 generator error versus grid spacing;
- convergence under decreasing `tau_U`, `tau_v=M_X/gamma_X`, `delta`, and lattice spacing.

The short scripts under `tools/candidate_checks/` test only algebraic identities and low-dimensional convergence diagnostics. They do not count as A2 direct simulation. Q3-1-A2 and Q3-2-A2 remain unreviewed until a canonical direct runner and aggregated reference results are added.
