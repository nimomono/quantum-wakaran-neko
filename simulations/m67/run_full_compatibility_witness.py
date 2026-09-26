#!/usr/bin/env python3
"""Direct finite-Hamiltonian M67 compatibility witness.

This is a compact regression witness, not a Q3-A2 promotion test.  It evolves
one closed finite Hamiltonian containing a coherent signal, phase-volume bath,
edge-flow reaction coordinates, finite flow baths, moving material frames,
finite local drag baths, and one tracer.  No external white noise is injected.
"""

import argparse
import json
import numpy as np


def drude_modes(n, omega_max, gamma, theta):
    dw=omega_max/n
    omega=(np.arange(n)+0.5)*dw
    weights=(2*gamma/np.pi)*dw/(1+(omega*theta)**2)
    c=omega*np.sqrt(weights)
    alpha=c/(omega**2)
    return omega,c,alpha


def ibeta(u):
    u=np.clip(u,0.0,1.0)
    phi=np.arcsin(np.sqrt(u))
    return phi/4-np.sin(4*phi)/16


class Model:
    def __init__(self, n=8, n0=300.0, seed=209):
        self.n=n
        self.L=2*np.pi
        self.a=self.L/n
        self.n0=n0
        self.nu=0.035
        self.kT=0.01
        self.delta=0.08
        self.Mrho=12
        self.K=90.0
        self.IU=0.02
        self.MY=20.0
        self.MX=0.08
        self.gammaU=5.0
        self.thetaU=0.035
        self.gammaX=1.0
        self.thetaX=0.035
        self.Mfb=4
        self.Mdb=4
        self.rng=np.random.default_rng(seed)
        self.xs=np.arange(n)*self.a
        self.ec=(np.arange(n)+0.5)*self.a

        off=-self.nu/self.a**2
        diag=2*self.nu/self.a**2
        h=np.diag(diag+0.02*np.cos(self.xs))
        for i in range(n):
            h[i,(i+1)%n]=off
            h[(i+1)%n,i]=off
        self.h=h
        self.off=off
        self.omrho=np.linspace(1.0,3.0,self.Mrho)
        self.omU,self.cU,self.alphaU=drude_modes(
            self.Mfb,50.0,self.gammaU,self.thetaU
        )
        self.omX,self.cX,self.alphaX=drude_modes(
            self.Mdb,50.0,self.gammaX,self.thetaX
        )

    def hat(self,X,offset):
        y=(X-offset)/self.a
        e=int(np.floor(y))
        u=y-e
        chi=np.zeros(self.n)
        dchi=np.zeros(self.n)
        chi[e%self.n]=1-u
        chi[(e+1)%self.n]=u
        dchi[e%self.n]=-1/self.a
        dchi[(e+1)%self.n]=1/self.a
        return chi,dchi

    def drag_geometry(self,X):
        g1=np.zeros(self.n)
        g2=np.zeros(self.n)
        s1=np.zeros(self.n)
        s2=np.zeros(self.n)
        for e,xe in enumerate(self.ec):
            d=X-xe
            winding=np.floor((d+self.a)/self.L)
            r=d-winding*self.L
            if r <= 0:
                u=(r+self.a)/self.a
                f1=self.a*u*u/2
                f2=self.a*ibeta(u)
                chi=u
            elif r <= self.a:
                u=r/self.a
                f1=self.a/2+self.a*(u-u*u/2)
                f2=self.a*np.pi/8+self.a*ibeta(u)
                chi=1-u
            else:
                f1=self.a
                f2=self.a*np.pi/4
                chi=0.0
            g1[e]=max(0.0,chi)
            g2[e]=np.sqrt(max(0.0,chi*(1-chi)))
            s1[e]=winding*self.a+f1
            s2[e]=winding*(self.a*np.pi/4)+f2
        return g1,g2,s1,s2

    def edge_flow(self,Z):
        v=np.zeros(self.n)
        gi=np.zeros(self.n,dtype=complex)
        gj=np.zeros(self.n,dtype=complex)
        bg=self.delta*self.n0/self.n
        for e in range(self.n):
            i=e
            j=(e+1)%self.n
            J=2*np.imag(np.conj(Z[j])*self.off*Z[i])
            r=0.5*(abs(Z[i])**2+abs(Z[j])**2)+bg
            dJi=1j*self.off*Z[j]
            dJj=-1j*self.off*Z[i]
            dri=0.5*Z[i]
            drj=0.5*Z[j]
            v[e]=self.a*J/r
            gi[e]=self.a*(dJi/r-J*dri/r**2)
            gj[e]=self.a*(dJj/r-J*drj/r**2)
        return v,gi,gj

    def initial(self):
        shape=(1+0.25*np.exp(1j*self.xs)
               +0.11*np.exp(-2j*self.xs+0.4j)
               +0.07*np.exp(2j*self.xs-0.3j))
        shape/=np.linalg.norm(shape)
        Z=np.sqrt(self.n0)*shape
        X=0.43
        PX=0.0

        chi,_=self.hat(X,0.0)
        r=chi@np.abs(Z)**2+self.delta*self.n0/self.n
        rstar=self.n0/self.n
        lam=(r/rstar)**(-1/self.Mrho)
        Q=self.rng.normal(size=self.Mrho)*np.sqrt(self.kT)/self.omrho
        qr=Q/lam
        pr=self.rng.normal(size=self.Mrho)*np.sqrt(self.kT)

        v,_,_=self.edge_flow(Z)
        U=v.copy()
        PU=np.zeros(self.n)
        Y=np.zeros(self.n)
        PY=np.zeros(self.n)

        qf=self.alphaU[None,:]*U[:,None]
        qf+=self.rng.normal(size=qf.shape)*np.sqrt(self.kT)/self.omU[None,:]
        pf=self.rng.normal(size=qf.shape)*np.sqrt(self.kT)

        g1,g2,s1,s2=self.drag_geometry(X)
        q1=self.alphaX[None,:]*(s1-Y)[:,None]
        q2=self.alphaX[None,:]*s2[:,None]
        q1+=self.rng.normal(size=q1.shape)*np.sqrt(self.kT)/self.omX[None,:]
        q2+=self.rng.normal(size=q2.shape)*np.sqrt(self.kT)/self.omX[None,:]
        p1=self.rng.normal(size=q1.shape)*np.sqrt(self.kT)
        p2=self.rng.normal(size=q2.shape)*np.sqrt(self.kT)

        return dict(Z=Z,X=X,PX=PX,qr=qr,pr=pr,U=U,PU=PU,Y=Y,PY=PY,
                    qf=qf,pf=pf,q1=q1,p1=p1,q2=q2,p2=p2)

    def deriv(self,s):
        Z=s["Z"]; X=s["X"]
        chi,dchi=self.hat(X,0.0)
        rho=np.abs(Z)**2
        r=chi@rho+self.delta*self.n0/self.n
        rx=dchi@rho
        rstar=self.n0/self.n
        lam=(r/rstar)**(-1/self.Mrho)
        Arho=np.sum((self.omrho*lam*s["qr"])**2)/self.Mrho
        dHdr=-Arho/r

        v,gi,gj=self.edge_flow(Z)
        mismatch=s["U"]-v
        grad=self.h@Z+dHdr*chi*Z
        for e in range(self.n):
            i=e; j=(e+1)%self.n
            grad[i]+=-self.K*mismatch[e]*gi[e]
            grad[j]+=-self.K*mismatch[e]*gj[e]

        Qf=s["qf"]-self.alphaU[None,:]*s["U"][:,None]
        Ffb=np.sum(self.cU[None,:]*Qf,axis=1)

        g1,g2,s1,s2=self.drag_geometry(X)
        Q1=s["q1"]-self.alphaX[None,:]*(s1-s["Y"])[:,None]
        Q2=s["q2"]-self.alphaX[None,:]*s2[:,None]
        f1=np.sum(self.cX[None,:]*Q1,axis=1)
        f2=np.sum(self.cX[None,:]*Q2,axis=1)
        Fdrag=g1@f1+g2@f2
        Frho=-dHdr*rx

        return dict(
            Z=-1j*grad,
            X=s["PX"]/self.MX,
            PX=Frho+Fdrag,
            qr=s["pr"],
            pr=-(self.omrho**2)*(lam**2)*s["qr"],
            U=s["PU"]/self.IU,
            PU=-self.K*mismatch-s["PY"]+Ffb,
            Y=s["PY"]/self.MY+s["U"],
            PY=-f1,
            qf=s["pf"],
            pf=-(self.omU[None,:]**2)*Qf,
            q1=s["p1"],
            p1=-(self.omX[None,:]**2)*Q1,
            q2=s["p2"],
            p2=-(self.omX[None,:]**2)*Q2,
        )

    def energy(self,s):
        Z=s["Z"]; X=s["X"]
        chi,_=self.hat(X,0.0)
        r=chi@np.abs(Z)**2+self.delta*self.n0/self.n
        lam=(r/(self.n0/self.n))**(-1/self.Mrho)
        Hsig=float(np.real(np.vdot(Z,self.h@Z)))
        Hrho=0.5*np.sum(s["pr"]**2+(self.omrho*lam*s["qr"])**2)
        v,_,_=self.edge_flow(Z)
        Hflow=np.sum(
            s["PU"]**2/(2*self.IU)
            +0.5*self.K*(s["U"]-v)**2
            +s["PY"]**2/(2*self.MY)
            +s["PY"]*s["U"]
        )
        Qf=s["qf"]-self.alphaU[None,:]*s["U"][:,None]
        Hfb=0.5*np.sum(s["pf"]**2+(self.omU[None,:]*Qf)**2)
        _,_,s1,s2=self.drag_geometry(X)
        Q1=s["q1"]-self.alphaX[None,:]*(s1-s["Y"])[:,None]
        Q2=s["q2"]-self.alphaX[None,:]*s2[:,None]
        Hdb=0.5*np.sum(
            s["p1"]**2+(self.omX[None,:]*Q1)**2
            +s["p2"]**2+(self.omX[None,:]*Q2)**2
        )
        HX=s["PX"]**2/(2*self.MX)
        return Hsig+Hrho+Hflow+Hfb+Hdb+HX


def add(a,b,factor):
    out={}
    for k in a:
        out[k]=a[k]+factor*b[k]
    return out


def rk4(model,s,dt):
    k1=model.deriv(s)
    k2=model.deriv(add(s,k1,dt/2))
    k3=model.deriv(add(s,k2,dt/2))
    k4=model.deriv(add(s,k3,dt))
    out={}
    for k in s:
        out[k]=s[k]+dt*(k1[k]+2*k2[k]+2*k3[k]+k4[k])/6
    return out


def ray_error(z,zid):
    z=z/np.linalg.norm(z)
    zid=zid/np.linalg.norm(zid)
    ov=abs(np.vdot(zid,z))
    return float(np.sqrt(max(0.0,1-ov*ov)))


def run(n0=300.0,T=0.08,dt=5e-4,seed=209):
    model=Model(n0=n0,seed=seed)
    s=model.initial()
    z0=s["Z"].copy()
    evals,evecs=np.linalg.eigh(model.h)
    e0=model.energy(s)
    max_edrift=0.0
    flow_sq=[]
    recoil_sq=[]
    for j in range(int(round(T/dt))):
        s=rk4(model,s,dt)
        en=model.energy(s)
        max_edrift=max(max_edrift,abs(en-e0)/max(1.0,abs(e0)))
        v,_,_=model.edge_flow(s["Z"])
        chi,_=model.hat(s["X"],model.a/2)
        flow_sq.append(float((chi@(s["U"]-v))**2))
        recoil_sq.append(float((chi@(s["PY"]/model.MY))**2))

    zid=evecs@(np.exp(-1j*evals*T)*(evecs.conj().T@z0))
    result={
        "scope":"full finite-Hamiltonian compatibility witness; not Q3-A2 promotion",
        "n0":n0,
        "energy_relative_drift_max":max_edrift,
        "signal_ray_error":ray_error(s["Z"],zid),
        "local_flow_rms":float(np.sqrt(np.mean(flow_sq))),
        "material_frame_recoil_rms":float(np.sqrt(np.mean(recoil_sq))),
        "flow_bath_recurrence_time":float(2*np.pi/(50.0/model.Mfb)),
        "observation_time":T,
    }
    return result


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--quick",action="store_true",help="kept for CI/readability; quick is the default")
    ap.add_argument("--sweep",action="store_true",help="also print a small N0 ray-error sweep")
    args=ap.parse_args()

    result=run()
    assert result["energy_relative_drift_max"] < 2e-4, result
    assert result["signal_ray_error"] < 8e-2, result
    assert result["local_flow_rms"] < 1.5e-1, result
    assert result["observation_time"] < result["flow_bath_recurrence_time"], result

    if args.sweep:
        sweep=[]
        for n0 in (100.0,300.0,1000.0):
            r=run(n0=n0,T=0.05,seed=209)
            sweep.append([n0,r["signal_ray_error"]])
        result["n0_ray_sweep"]=sweep
    print(json.dumps(result,sort_keys=True))


if __name__=="__main__":
    main()
