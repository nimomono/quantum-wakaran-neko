#!/usr/bin/env python3
import numpy as np

def drude_memory_error(theta: float, dt: float=2e-4, T: float=1.0) -> float:
    n=int(T/dt)
    y=0.0
    err=[]
    for j in range(n):
        t=j*dt
        h=0.23*np.sin(1.1*t)+0.09*np.cos(2.0*t)
        y += dt*(h-y)/theta
        if t>6*theta:
            err.append(y-h)
    return float(np.sqrt(np.mean(np.square(err))))

def main() -> None:
    # local tight-frame constant friction/noise and zero Stratonovich drift
    x=np.linspace(0.0,1.0,4001)
    c0=1-x
    c1=x
    gp=np.sqrt(2*c0*c1)
    frame=c0*c0+c1*c1+gp*gp
    assert np.max(np.abs(frame-1.0)) < 2e-15
    # d/dx sum g^2 = 0, evaluated away from endpoints
    dframe=np.gradient(frame,x)
    assert np.max(np.abs(dframe[5:-5])) < 1e-10

    # Drude short-memory error is first order for a smooth input.
    thetas=np.array([0.08,0.04,0.02,0.01])
    errs=np.array([drude_memory_error(t) for t in thetas])
    assert np.all(errs[1:] < errs[:-1])
    slope=float(np.polyfit(np.log(thetas),np.log(errs),1)[0])
    assert 0.78 < slope < 1.18, slope

    # Integrated Drude covariance differs from Brownian covariance by <= 2 gamma theta.
    gamma=1.7
    theta=0.03
    for t in (0.1,0.3,0.8):
        drude=2*gamma*(t-theta*(1-np.exp(-t/theta)))
        brown=2*gamma*t
        assert abs(drude-brown) <= 2*gamma*theta*(1+1e-12)

    # Finite frequency discretization must recur after the observation window.
    omega_max=80.0
    nmode=256
    domega=omega_max/nmode
    trec=2*np.pi/domega
    assert 1.5 < trec
    print("r209b_finite_bath_markov_fdt_check_ok", slope, trec)

if __name__=="__main__":
    main()
