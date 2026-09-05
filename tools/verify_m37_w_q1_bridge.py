#!/usr/bin/env python3
"""Finite M37/W/Q1 bridge checks; NumPy only, no Born sampling assumption.

J0=Mosc=1. W grid: 25 interior points of [-2,2], Dirichlet ends,
kinetic coefficient 0.12, potential 2*(x*x-1)**2. Exact static
Hamiltonian propagation is compared with full and projected unitary maps.
All operator errors are real-linear input-uniform errors, not one state fits.
Smooth checks use RK4 with two time steps and a separate work accumulator.
"""
from __future__ import annotations
import json
import numpy as np
from verify_m47_q1_instrument import record_max, record_min
from dataclasses import asdict


def op(a):
    return float(np.linalg.norm(a, 2))


def real_map(u):
    return np.block([[u.real, -u.imag], [u.imag, u.real]])


def unitary(h, t):
    e, v = np.linalg.eigh(h)
    return (v * np.exp(-1j * e * t)) @ v.conj().T


def physical(h, omega, t):
    e, v = np.linalg.eigh(h)
    freq = np.sqrt(omega**2 + 2 * omega * e)
    co = (v * np.cos(freq*t)) @ v.T
    si = np.sin(freq*t)
    upper = (v * (omega/freq*si)) @ v.T
    lower = (v * (-freq/omega*si)) @ v.T
    return np.block([[co, upper], [lower, co]])


def carrier_bound(h, omega, t):
    eta = 2*op(h)/omega
    if not eta < 1:
        raise ValueError('outside R86 weak-coupling domain')
    k = (1-eta)**(-.25)
    return k*(2*(k-1) + t*op(h)**2/(2*omega*(1-eta)**1.5))


def grid():
    x = np.linspace(-2, 2, 27)[1:-1]
    dx = 4/26
    lap = (2*np.eye(len(x))-np.eye(len(x), k=1)-np.eye(len(x), k=-1))/dx**2
    h = .12*lap + np.diag(2*(x*x-1)**2)
    e, vec = np.linalg.eigh(h)
    # Freeze a single physical left/right convention, including odd-mode sign.
    if vec[:, 0].sum() < 0: vec[:, 0] *= -1
    if vec[:, 0] @ (x*vec[:, 1]) > 0: vec[:, 1] *= -1
    V = vec[:, :2] @ (np.array([[1,1],[1,-1]])/np.sqrt(2))
    return x, h, e, V


def smooth_run(steps):
    n=3; omega=12.; T=.7
    base=np.diag([-.2,.1,.3]) + .08*(np.eye(n,k=1)+np.eye(n,k=-1))
    X=np.diag([-1.,0.,1.]); initial=np.arange(1,7,dtype=float);initial/=np.linalg.norm(initial)
    def hs(t):
        return base-.15*np.sin(np.pi*t/T)**2*X
    def rhs(t, state):
        mat=state[:-1].reshape(6,6);h=hs(t)
        K=np.block([[np.zeros((n,n)),omega*np.eye(n)],[-omega*np.eye(n)-2*h,np.zeros((n,n))]])
        q=(mat@initial)[:n]
        dh=-.15*np.pi/T*np.sin(2*np.pi*t/T)*X
        return np.r_[(K@mat).ravel(),q@dh@q]
    state=np.r_[np.eye(6).ravel(),0.];dt=T/steps
    for k in range(steps):
        t=k*dt;a=rhs(t,state);b=rhs(t+dt/2,state+dt*a/2)
        c=rhs(t+dt/2,state+dt*b/2);d=rhs(t+dt,state+dt*c)
        state+=dt*(a+2*b+2*c+d)/6
    mat=state[:-1].reshape(6,6);last=mat@initial
    def energy(y,h):return omega/2*(y@y)+y[:n]@h@y[:n]
    work_error=abs(energy(last,hs(T))-energy(initial,hs(0))-state[-1])
    # Compare with static base: ||h-base||=.15 sin^2, exact integral=.15*T/2.
    area=.15*T/2
    ramp_bound=2*np.exp((op(base)+.15)*T)*area
    ramp_error=op(mat-physical(base,omega,T))
    return mat,work_error,ramp_error,ramp_bound


def main():
    checks=[];rng=np.random.default_rng(69037)
    x,h0,e,V=grid();n=len(x);J=(e[1]-e[0])/2;G=e[2]-e[1]
    sx=np.array([[0.,1.],[1.,0.]]);sz=np.diag([1.,-1.]);X=np.diag(x)
    xp=V.T@X@V;I=np.eye(n);inj=real_map(V)
    checks.append(record_min('positive_doublet_gap',G,0.))
    checks.append(record_min('left_right_order',xp[1,1]-xp[0,0],.1))
    for F in [-.06,.06]:
        expected=np.mean(e[:2])*np.eye(2)-J*sx+F*(xp[1,1]-xp[0,0])/2*sz
        checks.append(record_max('signed_tilt_'+str(F),op(V.T@(h0-F*X)@V-expected),1e-12))
    # Exact differential identity at nonzero time and arbitrary physical state.
    q,p=rng.normal(size=(2,n));omega=500.;t=.137;h=h0-.04*X
    z=(q+1j*p)/np.sqrt(2);b=np.exp(1j*omega*t)*z
    qdot=omega*p;pdot=-omega*q-2*h@q
    bdot=1j*omega*b+np.exp(1j*omega*t)*(qdot+1j*pdot)/np.sqrt(2)
    checks.append(record_max('exact_counterrotating_equation',np.linalg.norm(1j*bdot-h@b-np.exp(2j*omega*t)*h@b.conj()),2e-11))
    report=[]
    times=[np.pi/(2*J),.4/J,.6/J]
    matrices=[h0,h0-.06*X,h0+.035*X]
    for omega in [2000.,20000.,200000.]:
        mic=np.eye(2*n);full=np.eye(n,dtype=complex);low=np.eye(2,dtype=complex)
        elapsed=0.;product=1.;residual=0.;max_env=0.;max_state=0.;max_leak=0.
        for h,T in zip(matrices,times):
            g=V.T@h@V;B=h@V-V@g
            for dt in np.linspace(0,T,7)[1:]:
                now=elapsed+dt
                Bmic=real_map(np.exp(1j*omega*now)*I)@physical(h,omega,dt)@mic@inj
                U=unitary(h,dt)@full;u=unitary(g,dt)@low
                env=op(Bmic-real_map(U@V))
                state=op(Bmic-real_map(V@u))
                bound=product*(1+carrier_bound(h,omega,dt))-1
                low_bound=residual+dt*op(B)
                checks.append(record_max('segment_env_bound_excess',max(0,env-bound),2e-7))
                checks.append(record_max('bridge_bound_excess',max(0,state-bound-low_bound),2e-7))
                checks.append(record_max('low_residual_bound_excess',max(0,op(U@V-V@u)-low_bound),2e-12))
                max_env=max(max_env,env);max_state=max(max_state,state)
                max_leak=max(max_leak,op((I-V@V.T)@U@V)**2)
            mic=physical(h,omega,T)@mic;full=unitary(h,T)@full;low=unitary(g,T)@low
            elapsed+=T;product*=1+carrier_bound(h,omega,T);residual+=T*op(B)
        final=real_map(np.exp(1j*omega*elapsed)*I)@mic@inj
        quarter=real_map(1j*np.eye(2))
        phase_error=op(final@quarter-real_map(1j*I)@final)
        checks.append(record_max('global_phase_defect_bound_excess',max(0,phase_error-2*(product-1)),2e-7))
        c=np.array([1.,1j])/np.sqrt(2);signals=[]
        for phi in np.linspace(0,2*np.pi,16,endpoint=False):
            a=np.exp(1j*phi)*c;y=final@np.r_[a.real,a.imag];signals.append(y[:n]+1j*y[n:])
        Z=np.array(signals).T;C=Z@Z.conj().T;C/=np.trace(C)
        target=full@V@c;D=C-np.outer(target,target.conj())
        trace_distance=.5*np.sum(np.abs(np.linalg.eigvalsh(D)))
        err=op(final-real_map(full@V))
        checks.append(record_max('ensemble_trace_bound_excess',max(0,trace_distance-2*err),2e-7))
        checks.append(record_max('action_error_bound_excess',max(0,op(final.T@final-np.eye(4))-(2*err+err**2)),2e-7))
        report.append(dict(omega=omega,eta_max=max(2*op(h)/omega for h in matrices),max_env=max_env,max_state=max_state,max_leak=max_leak,phase_error=phase_error,trace_distance=float(trace_distance),envelope_bound=product-1,residual_bound=residual))
    checks.append(record_min('carrier_convergence_ratio',report[0]['max_env']/report[-1]['max_env'],20.))
    # Negative control: probability leakage is not a bound on arbitrary effects.
    ell=1e-4;a=np.array([np.sqrt(1-ell),np.sqrt(ell)]);ref=np.array([1.,0.]);effect=np.ones((2,2))/2
    obs=abs(a@effect@a-ref@effect@ref)
    checks.append(record_min('leakage_probability_is_not_tv_bound',obs/ell,50.))
    # Three-level virtual-phase witness: small leakage need not imply small state error.
    hh=np.array([[0.,0.,.1],[0.,0.,0.],[.1,0.,1.]])
    cc=np.array([1.,1.,0.])/np.sqrt(2);out=unitary(hh,100)@cc
    phase_distance=np.sqrt(max(0,1-abs(np.vdot(cc,out))**2))
    checks.append(record_min('virtual_phase_exceeds_leakage',phase_distance-abs(out[2])**2,.1))
    # Invalid weak coupling must not be silently assigned an R86 bound.
    rejected=False
    try:carrier_bound(h0,op(h0),1.)
    except ValueError:rejected=True
    checks.append(record_min('strong_coupling_rejected',float(rejected),1.))
    coarse,wc,_,_=smooth_run(700);fine,wf,re,rb=smooth_run(1400)
    checks.append(record_max('smooth_step_convergence',op(coarse-fine),2e-8))
    checks.append(record_max('smooth_work_balance',wf,2e-8))
    checks.append(record_max('smooth_ramp_bound_excess',max(0,re-rb),2e-8))
    payload=dict(seed=69037,grid_size=n,dirichlet_domain=[-2,2],J=J,G=G,total_time=sum(times),cases=report,smooth_work_error=wf,smooth_ramp_error=re,smooth_ramp_bound=rb,check_count=len(checks),checks=[asdict(c) for c in checks],passed=all(c.passed for c in checks))
    print(json.dumps(payload,ensure_ascii=False,indent=2))
    if not payload['passed']:raise SystemExit(1)

if __name__=='__main__':main()
