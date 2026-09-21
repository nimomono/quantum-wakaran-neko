#!/usr/bin/env python3
import numpy as np

def rk4(y0,rhs,dt,steps):
    y=y0.copy()
    for _ in range(steps):
        k1=rhs(y); k2=rhs(y+0.5*dt*k1); k3=rhs(y+0.5*dt*k2); k4=rhs(y+dt*k3)
        y += dt*(k1+2*k2+2*k3+k4)/6
    return y

def main():
    k=6; p=np.array([0.37,0.63]); lam=0.4; mu=3.0; T=4.0; dt=5e-4; steps=int(T/dt)
    def lump(y):
        xp,xm,h=y
        return np.array([-lam*xp+mu*p[0]*h,-lam*xm+mu*p[1]*h,lam*(xp+xm)-mu*h])
    target=rk4(np.array([1.0,0.0,0.0]),lump,dt,steps)
    errors=[]
    for mix in (2.0,8.0,32.0):
        n=2*k+1; hub=2*k; Q=np.zeros((n,n))
        for off in (0,k):
            ids=list(range(off,off+k))
            for i in ids:
                for j in ids:
                    if i!=j: Q[i,j]+=mix/(k-1)
        Q[0,hub]+=lam*k; Q[k,hub]+=lam*k
        Q[hub,0]+=mu*p[0]; Q[hub,k]+=mu*p[1]
        for i in range(n): Q[i,i]=-Q[i].sum()
        y0=np.zeros(n); y0[:k]=1.0/k
        y=rk4(y0,lambda z:z@Q,dt,steps)
        agg=np.array([y[:k].sum(),y[k:2*k].sum(),y[hub]])
        errors.append(0.5*np.abs(agg-target).sum())
    assert errors[-1]<errors[0] and errors[-1]<0.04
    print("m65_brownian_reduction_witness_ok",errors)
if __name__=="__main__": main()
