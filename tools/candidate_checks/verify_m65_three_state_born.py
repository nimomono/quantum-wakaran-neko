#!/usr/bin/env python3
import math, numpy as np

def exact(t,p,lam,mu,x0):
    h=lam/(lam+mu)*(1-math.exp(-(lam+mu)*t))
    x=np.array([p[r]*(1-h)+math.exp(-lam*t)*(x0[r]-p[r]) for r in range(2)])
    return np.array([x[0],x[1],h])

def main():
    rng=np.random.default_rng(2044)
    for _ in range(3000):
        p0=rng.uniform(1e-6,1.0); p=np.array([p0,1-p0])
        lam=rng.uniform(0.05,3.0); mu=rng.uniform(0.05,8.0); t=rng.uniform(0,20.0)
        x0=np.array([rng.uniform(),0.0]); x0[1]=1-x0[0]
        out=exact(t,p,lam,mu,x0); assert abs(out.sum()-1)<2e-12
        tv=0.5*(abs(out[0]-p[0])+abs(out[1]-p[1])+out[2])
        tv0=0.5*np.abs(x0-p).sum()
        assert tv<=math.exp(-lam*t)*tv0+(lam/mu)/(1+lam/mu)+2e-12
        tiny=2.0**-40
        assert abs(lam*((1-tiny)+tiny)-lam)<1e-15
    print("m65_three_state_born_ok")
if __name__=="__main__": main()
