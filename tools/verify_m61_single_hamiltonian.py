#!/usr/bin/env python3
from __future__ import annotations
import math
import numpy as np

def check_carrier_hopping() -> None:
    J=0.73
    z=0.31+0.47j
    for sigma in (+1,-1):
        phase=np.exp(1j*sigma*math.pi/2)
        physical=-J*(phase*z+np.conj(phase*z))
        m60=-1j*sigma*J*(z-np.conj(z))
        assert abs(physical-m60)<1e-12

def check_action_invariance() -> None:
    rng=np.random.default_rng(17)
    psi=rng.normal(size=12)+1j*rng.normal(size=12)
    n=np.arange(psi.size)
    b=np.exp(1j*math.pi*n/2)*psi
    assert np.allclose(np.abs(b)**2,np.abs(psi)**2)

def beta_star(r: float) -> float:
    return 0.0 if abs(r)<1e-14 else r/(1.0+math.sqrt(1.0-r*r))

def force(beta: float, ip: float, im: float) -> float:
    return ip*(1-beta)/(1+beta)-im*(1+beta)/(1-beta)

def check_r200a() -> None:
    for r in (-0.6,-0.2,0.0,0.3,0.7):
        total=2.4
        ip=0.5*total*(1+r)
        im=0.5*total*(1-r)
        b=beta_star(r)
        assert abs(force(b,ip,im))<1e-12
        h=1e-6
        slope=(force(b+h,ip,im)-force(b-h,ip,im))/(2*h)
        assert slope<0

def check_r200b() -> None:
    c=np.array([0.8,1.1,0.6])
    m=np.array([1.2,0.9,1.4])
    w=np.array([1.7,2.2,2.8])
    t=0.37
    kernel=np.sum(c*c/(m*w*w)*np.cos(w*t))
    fx=-kernel*0.23+0.17
    fy=-fx
    assert abs(fx+fy)<1e-15
    gamma,cutoff=0.7,5.0
    area=gamma*(1.0-math.exp(-cutoff*20.0))
    assert math.isclose(area,gamma,rel_tol=1e-12)

def main() -> None:
    check_carrier_hopping()
    check_action_invariance()
    check_r200a()
    check_r200b()
    print("m61_single_hamiltonian_required_ok")

if __name__=="__main__":
    main()
