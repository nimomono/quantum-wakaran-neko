#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def req(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"{label}: missing {needle!r}")


def forbid(text: str, needle: str, label: str) -> None:
    if needle in text:
        raise AssertionError(f"{label}: stale/forbidden {needle!r}")


def row(text: str, qid: str) -> str:
    for line in text.splitlines():
        if line.startswith(f"| {qid} |"):
            return line
    raise AssertionError(f"missing row {qid}")


def main() -> None:
    a27 = read("sections/A27_m67_two_entity_structured_reservoir.md")
    a24 = read("sections/A24_m66_common_phase_volume_readout.md")
    a23 = read("sections/A23_q2_2_spatial_preparation.md")
    status = read("PROJECT_STATUS.md")
    enh = read("ENHANCEMENT_TARGETS.md")
    readme = read("README.md")
    lineage = read("notes/theory_lineage.md")
    validation = read("VALIDATION.md")

    for needle in (
        "R212A：M67 universal phase-volume / mean-flow embedding",
        "R212B：M67 finite-Hamiltonian thermal sampler / R205E compatibility",
        "球面回転子版：M67 finite-Hamiltonian rotor / spherical R205E compatibility",
        "Q2-2二回転子版：R207A finite-Hamiltonian preparation lift",
        "R212C：M67 finite-Hamiltonian passive separation / R205F compatibility",
        "R206 common-hub apparatus全体",
        "Q2 signal/register/gate",
    ):
        req(a27, needle, "R212 active appendix")

    req(a24, "M67 thermal-sector open/effective interface", "M66 reclassification")
    for rid in ("R205A", "R205B", "R205C", "R205D", "R205E", "R205F",
                "R206A", "R206B", "R206C", "R206D", "R206E"):
        req(a24, rid, "M66/R205-R206 remain active")
    req(a24, "現行M65 physical liftには使わない", "R205D boundary")

    for rid in ("R207A", "R207B", "R207C", "R207D"):
        req(a23, rid, "R207 remains active")
    req(a23, "M67 finite-Hamiltonian lift", "R207 physical parent")
    req(a23, "R212B-rot", "R207 rotor bridge")
    req(a23, "R212C/R205F", "R207 separation bridge")

    # Fixed-goal status is intentionally unchanged.
    req(row(status, "Q2-1"), "| Q2-1 | 達成 |", "Q2-1 status")
    req(row(status, "Q2-2"), "| Q2-2 | 達成 |", "Q2-2 status")
    req(row(status, "Q2-3"), "| Q2-3 | 達成 |", "Q2-3 status")
    req(row(status, "Q2-4"), "| Q2-4 | 条件付き達成 |", "Q2-4 status")
    req(row(status, "Q2-4"), "R186", "R186 retained")
    req(row(status, "Q3-6"), "| Q3-6 | 未達 |", "Q3-6 status")
    req(status, "| M66 | M67 thermal-sector open/effective interface |", "M66 status")
    req(status, "| M67 | 二実体finite-Hamiltonian physical parent |", "M67 status")
    for rid in ("R212A", "R212B", "R212C"):
        req(status, f"| {rid} |", "R212 result ledger")

    # Strengthening states are not promoted by this PR.
    for q in ("Q2-1", "Q2-2", "Q2-3", "Q2-4"):
        req(enh, f"| {q} | 未監査 | 未監査 | 未監査 | 未監査 | 未監査 |",
            f"{q} strengthening unchanged")
    req(enh, "| Q3-1 | 部分達成 | 未監査 |", "Q3-1 strengthening unchanged")
    req(enh, "| Q3-2 | 部分達成 | 未監査 |", "Q3-2 strengthening unchanged")

    # The new hierarchy must be visible in current documentation.
    for text, label in ((readme, "README"), (lineage, "lineage")):
        req(text, "R212A--R212C", label)
        req(text, "M66", label)
        req(text, "R207", label)

    # Required R212 checks exist; stochastic mixing remains supporting simulation.
    for path in (
        "tools/verify_r212a_thermal_embedding.py",
        "tools/verify_r212b_flat_sampler.py",
        "tools/verify_r212b_rotor_geometry.py",
        "tools/verify_r212b_rotor_parameter_window.py",
        "tools/verify_r212c_passive_separation.py",
        "tools/verify_m66_common_phase_volume.py",
        "tools/verify_m66_thermal_gibbs_sampler.py",
        "tools/verify_m66_passive_separation.py",
        "tools/verify_r207_projection_phase_volume.py",
        "simulations/m67/run_r212b_rotor_mixing_witness.py",
    ):
        if not (ROOT / path).is_file():
            raise AssertionError(f"missing verifier/witness: {path}")

    if (ROOT / "tools/candidate_checks/verify_r212b_rotor_parameter_window.py").exists():
        raise AssertionError("promoted R212B parameter checker remains candidate")

    req(validation, "draft-142：M67 thermal-sector / R212検算", "validation ledger")
    req(lineage, "draft-142でM67 thermal sectorをM66/R205へ接続", "lineage ledger")

    # Do not imply that R212 closes the signal/NBL/R206-apparatus problem or M0.
    forbid(a27, "R206 common-hub apparatus全体を回収する", "R206 overclaim")
    forbid(a27, "NBL registerを回収する", "NBL overclaim")
    req(status, "| M0 | 単一ミクロ装置統一目標 | 将来目標 |", "M0 unchanged")

    print("draft142_m67_thermal_sector_check_ok")


if __name__ == "__main__":
    main()
