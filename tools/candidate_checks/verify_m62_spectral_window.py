#!/usr/bin/env python3
import math

def main() -> None:
    omega_pn=0.28284
    omega1=1.19599
    omega2=1.21700
    omega_cont=4.00659
    assert 0.0 < omega_pn < omega1 < omega2 < omega_cont
    assert 3.0*omega2 < omega_cont
    def disp2(q: float) -> float:
        return 16.0 + 400.0*(1.0-math.cos(q))/(5.0-3.0*math.cos(q))
    assert abs(math.sqrt(disp2(0.0))-4.0) < 1e-12
    assert abs(math.sqrt(disp2(math.pi))-math.sqrt(116.0)) < 1e-12
    print("m62_spectral_window_candidate_ok")
if __name__ == "__main__":
    main()
