#!/usr/bin/env python3
import numpy as np

def main():
    xs=np.linspace(-10.0,10.0,400001)
    vals=[]
    for phi in (0.2,0.5,1.0,2.0,5.0):
        zs=phi*xs
        density=np.exp(-0.5*(zs/phi)**2)
        integ=np.trapezoid(density,zs)
        vals.append(integ/phi)
    ref=vals[2]
    assert max(abs(v-ref) for v in vals)<2e-10
    for ap,am in ((0.3,0.7),(2.0,5.0),(1e-2,0.9)):
        p=np.array([ap,am])/(ap+am)
        for scale in (0.1,3.0,20.0):
            pc=np.array([scale*ap,scale*am])/(scale*(ap+am))
            assert np.max(np.abs(pc-p))<1e-14
    print("m65_phase_volume_partition_ok")

if __name__=="__main__":
    main()
