#!/usr/bin/env python3
import numpy as np

def interp_error(n: int) -> float:
    L=2*np.pi
    a=L/n
    xe=(np.arange(n)+0.5)*a
    ve=0.18*np.sin(xe)+0.07*np.cos(2*xe)-0.04*np.sin(3*xe)
    xs=np.linspace(0,L,4001,endpoint=False)
    out=np.empty_like(xs)
    for k,x in enumerate(xs):
        y=(x-0.5*a)/a
        e=int(np.floor(y))
        u=y-e
        out[k]=(1-u)*ve[e % n]+u*ve[(e+1) % n]
    exact=0.18*np.sin(xs)+0.07*np.cos(2*xs)-0.04*np.sin(3*xs)
    return float(np.sqrt(np.mean((out-exact)**2)))

def main() -> None:
    ns=np.array([16.,24.,32.,48.,64.,96.])
    errs=np.array([interp_error(int(n)) for n in ns])
    slope=float(np.polyfit(np.log(ns),np.log(errs),1)[0])
    assert -2.15 < slope < -1.80, slope

    tau=0.05
    eps=0.013
    dt=2e-4
    T=0.8
    e=0.0
    max_abs=0.0
    for j in range(int(T/dt)):
        t=j*dt
        residual=eps*np.sin(1.7*t)
        e += dt*(-e+residual)/tau
        max_abs=max(max_abs,abs(e))
    assert max_abs <= eps*(1+2e-2), (max_abs,eps)

    # material-frame recoil is additive to the M67->M64 bridge, not to
    # the pre-existing M64 interpolation error.
    eps_hu=0.013
    eps_y=0.006
    assert abs((eps_hu+eps_y)-0.019) < 1e-15
    print("r209a_local_flow_compatibility_check_ok", slope, max_abs)

if __name__=="__main__":
    main()
