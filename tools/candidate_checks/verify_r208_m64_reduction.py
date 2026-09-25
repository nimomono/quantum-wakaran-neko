#!/usr/bin/env python3
import numpy as np

def rms(tau,dt=2e-4,T=1.5):
    u=0.0; s=0.0; n=0
    for j in range(int(T/dt)):
        t=j*dt; v=0.18*np.sin(1.3*t)+0.05*np.cos(2.1*t)
        u += dt*(v-u)/tau
        if t>5*tau: s+=(u-v)**2; n+=1
    return np.sqrt(s/n)

def main() -> None:
    taus=np.array([0.08,0.04,0.02,0.01]); errs=np.array([rms(t) for t in taus])
    assert np.all(errs[1:]<errs[:-1])
    slope=np.polyfit(np.log(taus),np.log(errs),1)[0]
    assert 0.75<slope<1.2
    assert max(0.002,0.01,0.005)<0.2<min(2.0,5.0)
    print("r208_m64_reduction_check_ok",slope)

if __name__ == "__main__":
    main()
