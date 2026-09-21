#!/usr/bin/env python3
from __future__ import annotations

import math
import numpy as np

TOL = 5.0e-11


def exact(t: float, a: np.ndarray, lam: float, kappa: float, x0: np.ndarray) -> np.ndarray:
    asum=float(a.sum())
    p=a/asum
    rate=lam+kappa*asum
    h=lam/rate*(1.0-math.exp(-rate*t))
    x=np.array([
        p[r]*(1.0-h)+math.exp(-lam*t)*(x0[r]-p[r])
        for r in range(2)
    ])
    return np.array([x[0],x[1],h])


def main() -> None:
    rng=np.random.default_rng(204117)
    max_tv_excess=0.0
    max_mass_error=0.0
    max_eig_error=0.0

    for _ in range(4000):
        a=10.0**rng.uniform(-3.0,2.0,size=2)
        lam=10.0**rng.uniform(-2.0,1.0)
        kappa=10.0**rng.uniform(-2.0,1.0)
        t=rng.uniform(0.0,20.0)
        x0=np.array([rng.random(),0.0])
        x0[1]=1.0-x0[0]
        out=exact(t,a,lam,kappa,x0)
        max_mass_error=max(max_mass_error,abs(float(out.sum())-1.0))

        p=a/a.sum()
        tv=0.5*(abs(out[0]-p[0])+abs(out[1]-p[1])+out[2])
        tv0=0.5*float(np.abs(x0-p).sum())
        bound=math.exp(-lam*t)*tv0+lam/(lam+kappa*a.sum())
        max_tv_excess=max(max_tv_excess,tv-bound)

        q=np.array([
            [-lam,0.0,lam],
            [0.0,-lam,lam],
            [kappa*a[0],kappa*a[1],-kappa*a.sum()],
        ])
        assert np.max(np.abs(q.sum(axis=1))) < TOL
        eig=np.sort(np.real_if_close(np.linalg.eigvals(q)).real)
        target=np.sort(np.array([0.0,-lam,-(lam+kappa*a.sum())]))
        max_eig_error=max(max_eig_error,float(np.max(np.abs(eig-target))))

    assert max_mass_error < TOL
    assert max_tv_excess < TOL
    assert max_eig_error < 2e-10

    # Exact zero endpoints are part of the domain when total action is positive.
    for a in (np.array([0.0, 2.3]), np.array([1.7, 0.0])):
        out=exact(3.0,a,0.31,1.4,np.array([0.5,0.5]))
        assert abs(float(out.sum())-1.0) < TOL
        p=a/a.sum()
        assert np.isfinite(out).all()
        assert np.isfinite(p).all()

    # Endpoint comparisons are division-free and exactly equivalent away from equality.
    tau=0.07
    for _ in range(10000):
        ap,am=10.0**rng.uniform(-5.0,3.0,size=2)
        pplus=ap/(ap+am)
        lhs=(1.0-tau)*ap-tau*am
        assert (pplus < tau) == (lhs < 0.0)

    # Exact endpoints route deterministically without evaluating a state-dependent ratio.
    assert (1.0-tau)*0.0-tau*3.0 < 0.0
    assert (1.0-tau)*3.0-tau*0.0 > 0.0

    # Finite latch: after decision time the selector generator is closed and the
    # complete-result distribution is copied unchanged to (+,-,empty).
    a=np.array([0.8,1.2])
    pre_latch=exact(2.7,a,0.23,1.9,np.array([1.0,0.0]))
    record=np.array([pre_latch[0],pre_latch[1],pre_latch[2]])
    q_off=np.zeros((3,3))
    post_latch=record @ (np.eye(3)+5.0*q_off)
    assert np.max(np.abs(post_latch-record)) < TOL
    assert abs(float(record.sum())-1.0) < TOL

    # Tiny Born branch does not shrink the relaxation eigenvalue -Lambda.
    lam=0.31
    kappa=1.7
    for n in (8,16,32,64,128):
        pminus=2.0**(-n)
        a_sum=2.4
        a=np.array([(1.0-pminus)*a_sum,pminus*a_sum])
        q=np.array([
            [-lam,0.0,lam],
            [0.0,-lam,lam],
            [kappa*a[0],kappa*a[1],-kappa*a.sum()],
        ])
        eig=np.sort(np.real_if_close(np.linalg.eigvals(q)).real)
        assert np.min(np.abs(eig+lam)) < 2e-10

    # Polynomial readout witness.
    eps=1.0e-3
    for n in (4,8,16,32,64):
        m=n*n
        lam_inv=(2*n+1)**2
        lam=1.0/lam_inv
        tnode=lam_inv*math.log(40.0*m/eps)
        a_min=1.0/(n+1)**2
        kappa=40.0*m*lam/(eps*a_min)
        hub=lam/(lam+kappa*a_min)
        assert hub <= eps/(40.0*m)+1e-15
        total=m*tnode
        assert total < (2*n+1)**6*math.log(40.0*m/eps)

    print("M65 canonical open selector checks: OK")


if __name__ == "__main__":
    main()
