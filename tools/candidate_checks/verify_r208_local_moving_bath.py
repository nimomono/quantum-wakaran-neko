#!/usr/bin/env python3
import numpy as np

def main() -> None:
    x=np.linspace(0.0,1.0,2001); c0=1-x; c1=x
    gp=np.sqrt(2*c0*c1); frame=c0*c0+c1*c1+gp*gp
    assert np.max(np.abs(frame-1.0))<1e-12
    u0,u1=-0.3,0.8; ux=c0*u0+c1*u1
    assert np.max(np.abs(-(frame*0.4-ux)-(-(0.4-ux))))<1e-12
    gamma,kT=1.7,0.4
    assert np.max(np.abs(2*gamma*kT*frame-2*gamma*kT))<1e-12
    print("r208_local_moving_bath_check_ok")

if __name__ == "__main__":
    main()
