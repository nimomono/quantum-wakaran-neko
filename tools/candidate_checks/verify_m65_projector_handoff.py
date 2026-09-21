#!/usr/bin/env python3
import numpy as np

def normed(v): return v/np.linalg.norm(v)

def main():
    rng=np.random.default_rng(2045)
    for _ in range(2000):
        z=normed(rng.normal(size=8)+1j*rng.normal(size=8))
        mask=np.zeros(8); mask[:4]=1
        if rng.uniform()<0.5: mask=1-mask
        v=mask*z; p=float(np.vdot(v,v).real)
        if p<0.08: continue
        eta=0.02*np.sqrt(p)
        noise=normed(rng.normal(size=8)+1j*rng.normal(size=8))*eta
        lhs=np.linalg.norm(normed(v+noise)-normed(v))
        rhs=2*eta/(np.sqrt(p)-eta)
        assert lhs<=rhs+1e-12
    probs=np.array([0.11,0.19,0.27,0.43]); total=probs.sum()
    assert abs((probs[0]+probs[1])/total*probs[0]/(probs[0]+probs[1])-probs[0]/total)<1e-14
    print("m65_projector_handoff_ok")
if __name__=="__main__": main()
