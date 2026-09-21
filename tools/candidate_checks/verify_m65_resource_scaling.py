#!/usr/bin/env python3
import math

def main():
    eps=1e-3
    for n in (4,8,16,32,64,128):
        d=n; m=n*d; lam_inv=(n+d+1)**2
        tnode=lam_inv*math.log(20*m/eps); total=m*tnode
        assert total < (n+d+1)**6*math.log(20*m/eps)
        assert eps/(20*m)>0
        tiny=2.0**(-n)
        assert abs((1-tiny)+tiny-1.0)<1e-14
    print("m65_resource_scaling_ok")
if __name__=="__main__": main()
