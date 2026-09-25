#!/usr/bin/env python3
import json
import numpy as np

def main():
    x=np.linspace(0.0,1.0,10001); c0=1-x; c1=x; gp=np.sqrt(2*c0*c1)
    frame=float(np.max(np.abs(c0*c0+c1*c1+gp*gp-1.0)))
    taus=np.array([0.08,0.04,0.02,0.01]); errs=[]
    dt=2e-4; T=1.5
    for tau in taus:
        u=0.0; s=0.0; n=0
        for j in range(int(T/dt)):
            t=j*dt; v=0.18*np.sin(1.3*t)+0.05*np.cos(2.1*t)
            u += dt*(v-u)/tau
            if t>5*tau: s+=(u-v)**2; n+=1
        errs.append(float(np.sqrt(s/n)))
    slope=float(np.polyfit(np.log(taus),np.log(errs),1)[0])
    print(json.dumps({"scope":"reduced candidate witness, not A2 full trajectory","max_frame_defect":frame,"tracking_slope":slope,"tracking_rms":errs}))

if __name__=="__main__":
    main()
