# M63 direct-simulation registry

This folder is the future A2 registry for the active M63/R202 topological-reservoir candidate in appendix Z.

At draft-107, the repository contains analytic/candidate checks for the local canonical filter bank, topological telescoping/Jacobian identity, and finite-width osmotic-force convergence. It does not yet contain a canonical full-Hamiltonian trajectory runner, so Q3-1-A2 and Q3-2-A2 remain unreviewed.

A complete M63 direct simulation should use one fixed parameter family and report at least:

1. kink stability together with signal/reservoir branch separation;
2. finite-time Schrödinger-envelope error for R202B;
3. direct conditional mean force versus `k_B T partial_X log r`;
4. signal distortion versus prepared physical action `N_0`, testing the predicted `N_0^{-1}` suppression;
5. reservoir force autocorrelation, memory kernel, and FDT comparison;
6. the same-field current-port response versus `j/rho`;
7. Peierls--Nabarro well relaxation and hopping statistics;
8. the finite-time generator error relative to R161.

Until those trajectory-level checks are reproducible from a documented runner, no M63 candidate value is a validated theorem bound or an A2 witness.
