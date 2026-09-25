#!/usr/bin/env python3
import numpy as np

def main() -> None:
    for K, M in ((3.0, 1.0), (2.0, 0.5), (10.0, 2.0)):
        q = np.array([[K, 1.0], [1.0, 1.0 / M]])
        assert np.linalg.eigvalsh(q).min() > 0.0
    print("m67_two_entity_hamiltonian_check_ok")

if __name__ == "__main__":
    main()
