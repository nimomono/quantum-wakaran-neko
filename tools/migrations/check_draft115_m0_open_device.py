#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def require(path: str, *tokens: str) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    missing = [token for token in tokens if token not in text]
    if missing:
        raise AssertionError(f"{path}: missing draft-115 M0 policy tokens: {missing}")


def forbid(path: str, *tokens: str) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    hits = [token for token in tokens if token in text]
    if hits:
        raise AssertionError(f"{path}: legacy M0 requirement remains: {hits}")


def main() -> None:
    require(
        "PROJECT_STATUS.md",
        "M0達成判定",
        "joint microscopic device/process",
        "採用開放古典ミクロ方程式",
        "Hamiltonian無限浴への持上げ",
    )
    require(
        "PROJECT_GUIDE.md",
        "M0の強さはHamiltonian性ではなく統合範囲",
        "joint evolutionまたはjoint path measure",
    )
    require(
        "ENHANCEMENT_TARGETS.md",
        "Hamiltonian無限浴への持上げを必須にしない",
        "共通単一bath",
    )
    forbid(
        "PROJECT_STATUS.md",
        "M0本体では有限な能動部分系、共通接続部、明示的なHamiltonian無限浴",
        "有限な能動部分系と明示的なHamiltonian無限浴からなる単一ミクロ装置と共通反復周期へ統合する",
    )
    print("draft115_m0_open_device_migration_ok")


if __name__ == "__main__":
    main()
