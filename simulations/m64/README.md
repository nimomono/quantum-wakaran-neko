# M64 direct simulation plan

M64のA2では、導出後のSchrödinger方程式やR161だけを計算せず、採用したopen micro equationsそのものを同一parameter setで直接発展・標本化する。

## Canonical continuous profile

1. M37 signalを発展し、regularized density/current $\rho_\delta,J_\delta,v_\delta$ を記録する。
2. preparation windowではsignal densityを固定し、flow-to-tracer couplingを切った
   $dX=\nu\partial_X\log r_X^\delta dt+\sqrt{2\nu}\,dW$
   を直接標本化する。
3. mean-flow collective variableを $\tau_U\dot U=-U+c_Jr$ で発展し、$U-v_\delta$ とbound $\varepsilon_A+\tau_UM_q$ を比較する。
4. $t=0$ でsignal evolutionとflow-to-tracer couplingをreleaseし、
   $dX=[U_X+\nu\partial_X\log r_X^\delta]dt+\sqrt{2\nu}\,dW$
   を直接標本化する。
5. 経験位置分布を $\rho_\delta(t)$ と比較し、時間刻み、標本数、$\tau_U$、$a$、$\delta$ に対する収束を調べる。

## Finite-graph profile

有限graph signalについてlocal

```math
R_i^\delta,
\qquad
J_{ij},
\qquad
T_{ij}^\delta
=
\frac{|h_{ij}|}{\mathcal J_0}
(R_i^\delta+R_j^\delta)
```

から

```math
k_{i\to j}
=
\frac{T_{ij}^\delta+J_{ij}}{2R_i^\delta}
```

を構成し、jump trajectoryを直接標本化する。経験分布が $\pi^\delta(t)$ と一致すること、R125の2頂点再結合器でregularized TV差が保たれることを検査する。

## A2判定境界

required algebra checksは解析式の回帰でありA2達成ではない。A2には少なくともcanonical continuous runner、十分なtrajectory数、経験分布比較、同一parameter set、主要近似パラメータに対する収束性が必要である。finite-graph runnerはQ3-4A/Q3-4B/Q3-5のA2監査へ使う。Hamiltonian lift、finite bath、underdamped liftはM64 A2の必須条件ではない。
