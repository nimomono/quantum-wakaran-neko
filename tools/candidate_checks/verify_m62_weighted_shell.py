#!/usr/bin/env python3
def main() -> None:
    omega1,omega2,mu=1.19599,1.21700,1.0
    d1,d2=omega1-mu,omega2-mu
    a1=2.0*d1/(d1+d2)
    a2=2.0*d2/(d1+d2)
    assert a1>0.0 and a2>0.0 and abs(a1+a2-2.0)<1e-14
    assert abs(d1/a1-d2/a2)<1e-14
    S,u=0.013,0.37
    jac=abs((u/a1)*(-S/a2)-(S/a1)*((1.0-u)/a2))
    assert abs(jac-S/(a1*a2))<1e-14
    print("m62_weighted_shell_candidate_ok")
if __name__ == "__main__":
    main()
