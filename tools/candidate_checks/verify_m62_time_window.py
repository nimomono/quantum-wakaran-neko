#!/usr/bin/env python3
def main() -> None:
    tau_mem,tau_ex,tau_mix=50.0,180.0,180.0
    t_obs,tau_n,t_nf=500.0,800.0,2200.0
    lower=max(tau_mem,tau_ex,tau_mix)
    upper=min(tau_n,t_nf)
    assert lower<t_obs<upper
    assert upper/lower>4.0
    print("m62_time_window_candidate_ok")
if __name__ == "__main__":
    main()
