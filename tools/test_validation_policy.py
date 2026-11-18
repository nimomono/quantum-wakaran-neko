#!/usr/bin/env python3
"""CIの読み取り専用性と主張台帳の空状態を自己検査する。"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    verify = (ROOT / ".github/workflows/verify.yml").read_text(encoding="utf-8")
    sync = (ROOT / ".github/workflows/sync-paper.yml").read_text(encoding="utf-8")
    assert "contents: read" in verify
    assert "git push" not in verify and "git commit" not in verify
    assert "workflow_dispatch:" in sync and "contents: write" in sync
    assert 'test "$TARGET_BRANCH" != "$DEFAULT_BRANCH"' in sync
    assert "python tools/check_generated.py" in verify
    assert "python tools/check_latex_semantics.py" in verify
    assert "python tools/check_project_consistency.py" in verify
    assert "なし。" in (ROOT / "rewrite/CLAIM_LEDGER.md").read_text(encoding="utf-8")
    print("validation_policy_test_ok")


if __name__ == "__main__":
    main()
