#!/usr/bin/env python3
import math

C = 2.0
gamma = 0.7
eps = 1e-4
T = math.log(C / eps) / gamma
assert C * math.exp(-gamma * T) <= eps * (1 + 1e-12)

eps_in = 2e-4
eps_mem = 3e-4
eps_mix = 4e-4
eps_sc = 5e-4
renewal = eps_in + eps_mem + eps_mix
kernel = renewal + eps_sc
assert abs(renewal - 9e-4) < 1e-12
assert abs(kernel - 1.4e-3) < 1e-12
assert abs((eps_mem + eps_mix) - 7e-4) < 1e-12
print("R179 open reset / renewal checks passed")
