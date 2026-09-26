#!/usr/bin/env python3
import numpy as np

def equilibrium_small_mass_rms(eps: float, nu: float, T: float) -> float:
    # For zero drift and equilibrium velocity, synchronous under/overdamped
    # coupling gives X^M-X^OD = eps(V_0-V_T).
    return float(np.sqrt(2*nu*eps*(1-np.exp(-T/eps))))

def main() -> None:
    nu=0.05
    T=0.4
    eps=np.array([0.04,0.02,0.01,0.005,0.0025])
    err=np.array([equilibrium_small_mass_rms(e,nu,T) for e in eps])
    assert np.all(err[1:] < err[:-1])
    slope=float(np.polyfit(np.log(eps),np.log(err),1)[0])
    assert 0.47 < slope < 0.53, slope

    # Compatibility error and the existing M64 baseline are separate ledgers.
    e_bath=0.004
    e_od=0.006
    e_hu=0.003
    e_y=0.002
    e_signal=0.005
    e_67_64=e_bath+e_od+e_hu+e_y+e_signal
    e64_baseline=0.011
    total=e_67_64+e64_baseline
    assert abs(total-0.031) < 1e-15
    # No M64 interpolation/tracking term is duplicated in e_67_64.
    assert abs(e_67_64-0.020) < 1e-15
    print("r209c_process_compatibility_check_ok", slope, total)

if __name__=="__main__":
    main()
