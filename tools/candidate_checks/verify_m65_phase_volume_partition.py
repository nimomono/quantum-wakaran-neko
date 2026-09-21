#!/usr/bin/env python3
import numpy as np

def main():
    zs=np.linspace(-10.0,10.0,400001)
    vals=[]
    for phi in (0.2,0.5,1.0,2.0,5.0):
        density=np.exp(-0.5*(zs/phi)**2)
        integ=np.trapezoid(density,zs)
        vals.append(integ/phi)
    ref=vals[2]
    assert max(abs(v-ref) for v in vals)<2e-5
    for ap,am in ((0.3,0.7),(2.0,5.0),(1e-2,0.9)):
        p=np.array([ap,am])/(ap+am)
        for c in (0.1,3.0,20.0):
            pc=np.array([c*ap,c*am])/(c*(ap+am))
            assert np.max(np.abs(pc-p))<1e-14
    print("m65_phase_volume_partition_ok")
if __name__=="__main__": main()
