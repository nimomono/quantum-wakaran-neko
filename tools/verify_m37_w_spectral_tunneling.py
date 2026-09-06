#!/usr/bin/env python3
"""Numerical regression checks for R182 static W spectral/spatial tunnelling."""
from __future__ import annotations
import numpy as np
TOL=5e-10
checks=0

def check(c,m):
    global checks
    if not c: raise AssertionError(m)
    checks+=1

def sc(v):
    s=np.sign(np.real_if_close(v).real); s=s[s!=0]
    return int(np.count_nonzero(s[1:]*s[:-1]<0))

def wh(n,L=3.0,Vb=12.0):
    a=2*L/(n+1); x=-L+a*np.arange(1,n+1); V=Vb*(x*x-1.0)**2
    H=np.diag(1/a**2+V)+np.diag(np.full(n-1,-.5/a**2),1)+np.diag(np.full(n-1,-.5/a**2),-1)
    return x,H

def orient(U):
    p0=U[:,0].copy(); p1=U[:,1].copy()
    if p0.sum()<0: p0*=-1
    left=np.arange(len(p0))<len(p0)//2
    if np.sum(p0[left]*p1[left])<0: p1*=-1
    return p0,p1

def spectrum():
    ss=[]
    for n in (120,240,480):
        _,H=wh(n); w,U=np.linalg.eigh(H); ss.append(w[:5].copy())
        check(np.all(np.diff(w[:5])>0),f'simple N={n}')
        check([sc(U[:,k]) for k in range(4)]==[0,1,2,3],f'nodes N={n}')
    ratio=float(np.max(np.abs(ss[0]-ss[1]))/np.max(np.abs(ss[1]-ss[2])))
    check(ratio>3.5,'second order')
    x,H=wh(480); w,U=np.linalg.eigh(H)
    check(w[1]<12.0,'doublet below barrier'); gap=float(w[2]-w[1]); check(gap>1,'third gap')
    p0,p1=orient(U)
    check(abs(abs(float(np.dot(p0,p0[::-1])))-1)<1e-9,'even ground')
    check(abs(float(np.dot(p1,p1[::-1]))+1)<1e-9,'odd first')
    return x,w,p0,p1,ratio,gap

def functional():
    _,H=wh(120); w,U=np.linalg.eigh(H); norm=float(np.max(np.abs(w))); om=20*norm; eta=2*norm/om
    check(eta<1,'eta')
    f=lambda E: om*(np.sqrt(1+2*E/om)-1)
    lo=(1+eta)**-.5; hi=(1-eta)**-.5
    d=float(w[1]-w[0]); de=f(float(w[1]))-f(float(w[0])); r=de/d
    check(lo<=r<=hi,'split bound')
    g=float(w[2]-w[1]); ge=f(float(w[2]))-f(float(w[1])); check(lo<=ge/g<=hi,'gap bound')
    F=(U*np.array([f(float(z)) for z in w]))@U.T
    check(np.linalg.norm(F@H-H@F,ord=2)<2e-8,'commutes')
    return eta,r,de

def spatial(x,w,p0,p1):
    d=float(w[1]-w[0]); left=x<-.35; center=np.abs(x)<=.35; right=x>.35
    B=float(np.sum(p0[left]*p1[left])); check(B>0,'positive B')
    def rho(t):
        z=(np.exp(-1j*w[0]*t)*p0+np.exp(-1j*w[1]*t)*p1)/np.sqrt(2)
        return np.abs(z)**2
    th=np.pi/d; tp=2*np.pi/d; r0=rho(0); rh=rho(th); rp=rho(tp)
    for r,name in ((r0,'initial'),(rh,'half'),(rp,'period')): check(abs(float(r.sum())-1)<TOL,'norm '+name)
    check(np.max(np.abs(rh-r0[::-1]))<TOL,'half mirror')
    check(np.max(np.abs(rp-r0))<TOL,'period return')
    c0=float(r0[center].sum()); check(max(abs(float(rh[center].sum())-c0),abs(float(rp[center].sum())-c0))<TOL,'center constant')
    inc=float(rh[right].sum()-r0[right].sum()); check(abs(inc-2*B)<TOL,'cross increment'); check(inc>0,'positive increment')
    return B,th,inc

def exact_m37():
    _,H=wh(120); w,U=np.linalg.eigh(H); p0,p1=orient(U); norm=float(np.max(np.abs(w))); om=20*norm
    f=lambda E: om*(np.sqrt(1+2*E/om)-1); de=f(float(w[1]))-f(float(w[0])); th=np.pi/de; tp=2*np.pi/de
    def rho(t):
        z=(np.exp(-1j*f(float(w[0]))*t)*p0+np.exp(-1j*f(float(w[1]))*t)*p1)/np.sqrt(2); return np.abs(z)**2
    r0=rho(0); check(np.max(np.abs(rho(th)-r0[::-1]))<TOL,'exact M37 half'); check(np.max(np.abs(rho(tp)-r0))<TOL,'exact M37 period')
    return th

def main():
    x,w,p0,p1,cr,g=spectrum(); eta,sr,de=functional(); B,th,inc=spatial(x,w,p0,p1); exh=exact_m37()
    print(f'checks={checks}')
    print(f'E0={w[0]:.8f} E1={w[1]:.8f} E2={w[2]:.8f} barrier=12.00000000 gap={g:.8f}')
    print(f'convergence_ratio={cr:.6f}')
    print(f'eta={eta:.6f} splitting_ratio={sr:.9f} delta_ex={de:.9f}')
    print(f'B_left={B:.9f} right_increment={inc:.9f}')
    print(f'target_half_period={th:.9f} exact_m37_half_period={exh:.9f}')
if __name__=='__main__': main()
