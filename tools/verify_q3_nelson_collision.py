from __future__ import annotations

import json
from dataclasses import asdict, dataclass
import itertools
import numpy as np

TOL = 2.0e-11


@dataclass
class Check:
    name: str
    value: float
    limit: float
    relation: str = "<="

    @property
    def passed(self) -> bool:
        if self.relation == "<=":
            return self.value <= self.limit
        if self.relation == ">=":
            return self.value >= self.limit
        raise ValueError(self.relation)


def tv(p: np.ndarray, q: np.ndarray) -> float:
    return float(0.5 * np.sum(np.abs(p - q)))


def exp_symmetric(generator: np.ndarray, time: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(generator)
    result = vectors @ np.diag(np.exp(values * time)) @ vectors.T
    result[np.abs(result) < 5.0e-16] = 0.0
    return result


def path_distribution(initial: np.ndarray, kernels: list[np.ndarray]) -> np.ndarray:
    size = len(initial)
    result = np.zeros((size,) * (len(kernels) + 1), dtype=float)
    for path in itertools.product(range(size), repeat=len(kernels) + 1):
        weight = initial[path[0]]
        for index, kernel in enumerate(kernels):
            weight *= kernel[path[index], path[index + 1]]
        result[path] = weight
    return result


def backward_kernel(pair: np.ndarray) -> np.ndarray:
    marginal = np.sum(pair, axis=0)
    result = np.zeros((pair.shape[1], pair.shape[0]))
    for target, mass in enumerate(marginal):
        if mass > 0.0:
            result[target] = pair[:, target] / mass
    return result


def forward_kernel(pair: np.ndarray) -> np.ndarray:
    marginal = np.sum(pair, axis=1)
    result = np.zeros_like(pair)
    for source, mass in enumerate(marginal):
        if mass > 0.0:
            result[source] = pair[source] / mass
    return result


def sampled_acceleration(
    forward_previous: np.ndarray,
    forward: np.ndarray,
    backward: np.ndarray,
    backward_next: np.ndarray,
    position: np.ndarray,
    tau: float,
) -> np.ndarray:
    return (
        2.0 * (forward @ position)
        - 2.0 * position
        + 2.0 * (backward @ position)
        - forward @ (backward_next @ position)
        - backward @ (forward_previous @ position)
    ) / (2.0 * tau**2)


def main() -> None:
    checks: list[Check] = []
    generator = np.array([
        [-0.7, 0.4, 0.3],
        [0.4, -0.9, 0.5],
        [0.3, 0.5, -0.8],
    ])
    position = np.array([-1.0, 0.25, 1.5])
    oscillation = float(np.max(position) - np.min(position))
    initial = np.full(3, 1.0 / 3.0)
    p_star = 1.0 / 3.0
    maximum_escape = float(np.max(-np.diag(generator)))

    h = 0.02
    exact_step = exp_symmetric(generator, h)
    euler_step = np.eye(3) + h * generator
    one_step_tv = max(tv(exact_step[i], euler_step[i]) for i in range(3))
    checks.append(Check("Euler kernel stochastic row sum", float(np.max(np.abs(np.sum(euler_step, axis=1) - 1.0))), TOL))
    checks.append(Check("Euler kernel nonnegative", max(0.0, -float(np.min(euler_step))), TOL))
    checks.append(Check("one-step Duhamel TV bound", one_step_tv - h**2 * maximum_escape**2, 2.0e-12))

    steps = 8
    exact_path = path_distribution(initial, [exact_step] * steps)
    euler_path = path_distribution(initial, [euler_step] * steps)
    skeleton_tv = tv(exact_path.ravel(), euler_path.ravel())
    checks.append(Check("finite-skeleton coupling bound", skeleton_tv - steps * one_step_tv, 2.0e-12))
    checks.append(Check("R162 uniform path bound", skeleton_tv - steps * h**2 * maximum_escape**2, 2.0e-12))

    exact_acceleration = -(generator @ (generator @ position))
    tau_values = [0.2, 0.1, 0.05, 0.025]
    time_errors: list[float] = []
    for tau in tau_values:
        kernel = exp_symmetric(generator, tau)
        sampled = sampled_acceleration(kernel, kernel, kernel, kernel, position, tau)
        time_errors.append(float(np.max(np.abs(sampled - exact_acceleration))))
    time_ratios = [time_errors[index] / time_errors[index + 1] for index in range(len(time_errors) - 1)]
    checks.append(Check("sampled Nelson first-order convergence", min(time_ratios), 1.80, ">="))

    tau = 0.12
    ideal_kernel = exp_symmetric(generator, tau)
    perturbation = 2.0e-4
    physical_kernel = ideal_kernel.copy()
    physical_kernel[0, 0] -= perturbation
    physical_kernel[0, 1] += perturbation
    physical_kernel[1, 1] -= perturbation
    physical_kernel[1, 2] += perturbation
    physical_kernel[2, 2] -= perturbation
    physical_kernel[2, 0] += perturbation

    ideal_path = path_distribution(initial, [ideal_kernel] * 3)
    physical_path = path_distribution(initial, [physical_kernel] * 3)
    history_tv = tv(ideal_path.ravel(), physical_path.ravel())
    checks.append(Check("history safety condition", history_tv, p_star / 2.0))

    ideal_pairs = [
        np.sum(ideal_path, axis=(2, 3)),
        np.sum(ideal_path, axis=(0, 3)),
        np.sum(ideal_path, axis=(0, 1)),
    ]
    physical_pairs = [
        np.sum(physical_path, axis=(2, 3)),
        np.sum(physical_path, axis=(0, 3)),
        np.sum(physical_path, axis=(0, 1)),
    ]
    ideal_forward = [forward_kernel(pair) for pair in ideal_pairs]
    physical_forward = [forward_kernel(pair) for pair in physical_pairs]
    ideal_backward = [backward_kernel(pair) for pair in ideal_pairs]
    physical_backward = [backward_kernel(pair) for pair in physical_pairs]

    conditional_bound = 2.0 * history_tv / p_star
    maximum_conditional_tv = max(
        *(tv(ideal_forward[1][i], physical_forward[1][i]) for i in range(3)),
        *(tv(ideal_backward[1][i], physical_backward[1][i]) for i in range(3)),
    )
    checks.append(Check("conditional-kernel TV lemma", maximum_conditional_tv - conditional_bound, 3.0e-12))

    ideal_acceleration = sampled_acceleration(
        ideal_forward[0], ideal_forward[1], ideal_backward[1], ideal_backward[2], position, tau
    )
    physical_acceleration = sampled_acceleration(
        physical_forward[0], physical_forward[1], physical_backward[1], physical_backward[2], position, tau
    )
    acceleration_error = float(np.max(np.abs(physical_acceleration - ideal_acceleration)))
    history_bound = 8.0 * oscillation * history_tv / (p_star * tau**2)
    checks.append(Check("history-to-acceleration bound", acceleration_error - history_bound, 3.0e-12))

    lattice_errors: list[float] = []
    for size in (64, 128, 256):
        grid = np.arange(size) * (2.0 * np.pi / size)
        spacing = 2.0 * np.pi / size
        field = np.sin(grid) + 0.17 * np.cos(2.0 * grid)
        exact_second = -np.sin(grid) - 0.68 * np.cos(2.0 * grid)
        discrete_second = (np.roll(field, -1) - 2.0 * field + np.roll(field, 1)) / spacing**2
        lattice_errors.append(float(np.max(np.abs(discrete_second - exact_second))))
    lattice_ratios = [lattice_errors[index] / lattice_errors[index + 1] for index in range(2)]
    checks.append(Check("R185 central-difference second-order convergence", min(lattice_ratios), 3.85, ">="))

    output = {
        "check_count": len(checks),
        "checks": [{**asdict(check), "passed": bool(check.passed)} for check in checks],
        "diagnostics": {
            "one_step_tv": one_step_tv,
            "skeleton_tv": skeleton_tv,
            "time_errors": time_errors,
            "time_ratios": time_ratios,
            "history_tv": history_tv,
            "maximum_conditional_tv": maximum_conditional_tv,
            "conditional_bound": conditional_bound,
            "acceleration_error": acceleration_error,
            "history_acceleration_bound": history_bound,
            "lattice_errors": lattice_errors,
            "lattice_ratios": lattice_ratios,
        },
        "passed": bool(all(check.passed for check in checks)),
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    if not output["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
