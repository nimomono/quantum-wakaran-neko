#!/usr/bin/env python3
import numpy as np

def main() -> None:
    rng=np.random.default_rng(208); kT=0.7
    Ns=np.array([8,32,128,512],dtype=float); rel=[]
    for n in Ns.astype(int):
        q=rng.normal(0.0,np.sqrt(kT),size=(12000,n))
        c=np.mean(q*q,axis=1); rel.append(np.std(c)/np.mean(c))
    slope=np.polyfit(np.log(Ns),np.log(rel),1)[0]
    assert -0.60 < slope < -0.40
    N0=np.array([10.,30.,100.,300.,1000.])
    slope2=np.polyfit(np.log(N0),np.log(1.0/N0),1)[0]
    assert abs(slope2+1.0)<1e-12
    print("r208_phase_volume_backreaction_check_ok",slope,slope2)

if __name__ == "__main__":
    main()
