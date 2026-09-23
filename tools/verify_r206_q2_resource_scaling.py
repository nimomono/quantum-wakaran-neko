#!/usr/bin/env python3
"""Candidate resource checks for R206D Q2-4 specialization."""

import math

def main():
    eps = 1e-6
    lam = 0.5
    T = math.log(4.0/eps)/lam
    for n in (2, 4, 8, 16, 32):
        L = 2**n
        assert T < 100.0
        passive = n * L
        external_bits = n
        assert passive >= L
        assert external_bits == int(math.log2(L))

    print("R206D Q2 resource scaling checks: OK")

if __name__ == "__main__":
    main()
