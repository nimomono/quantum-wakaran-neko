#!/usr/bin/env python3
from __future__ import annotations

def main() -> None:
    # Illustrative only; this is not a proof of R198D mixing or a uniform M61 window.
    tau_sc,tau_bath,tau_track,tau_therm,t_sig,tau_return=0.02,0.05,0.20,1.0,20.0,100.0
    assert tau_sc<tau_track<t_sig<tau_return
    assert tau_bath<tau_track
    assert tau_therm<t_sig
    gamma_rad,gamma_x,mass_y,kbt=50.0,0.02,1.0,0.1
    assert (gamma_rad/mass_y)*t_sig>100.0
    assert gamma_x*kbt/(mass_y*gamma_rad)<1e-3
    print("m61_parameter_window_candidate_ok")

if __name__=="__main__":
    main()
