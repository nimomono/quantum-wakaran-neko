#!/usr/bin/env python3
import numpy as np

def main():
    rng=np.random.default_rng(204)
    for _ in range(1000):
        a=rng.uniform(1e-3,10.0,size=2)
        vc0=rng.uniform(0.2,4.0); g0=rng.uniform(0.1,3.0); vh0=rng.uniform(0.05,2.0)
        v=a*vc0; g=a*g0
        assert np.max(np.abs(g/v-g0/vc0))<1e-12
        p=a/a.sum(); hub=a.sum()*vh0; mu=g0/vh0
        assert np.max(np.abs(g/hub-mu*p))<1e-12
    print("m65_matched_conductance_ok")
if __name__=="__main__": main()
