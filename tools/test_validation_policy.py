#!/usr/bin/env python3
from __future__ import annotations

import ast
import re
from pathlib import Path

from latex_log import classify_latex_log

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"


def test_layout_warnings_are_not_hard() -> None:
    hard, style = classify_latex_log(
        "Overfull \\hbox (3.75pt too wide) in paragraph at lines 120--122\n"
        "Underfull \\hbox (badness 10000) in paragraph at lines 130--131\n"
    )
    assert hard == []
    assert [item.kind for item in style] == ["overfull", "underfull"]
    assert style[0].amount_pt == 3.75
    assert style[0].source_line == 120


def test_semantic_tex_failures_are_hard() -> None:
    hard, style = classify_latex_log(
        "LaTeX Warning: Citation `example' on page 2 undefined on input line 88.\n"
        "LaTeX Warning: Reference `eq:test' on page 3 undefined on input line 99.\n"
        "Missing character: There is no □ in font Latin Modern Math!\n"
        "!  ==> Fatal error occurred, no output PDF file produced!\n"
    )
    assert style == []
    assert {item.kind for item in hard} == {
        "undefined-citation",
        "undefined-reference",
        "missing-character",
        "fatal-error",
    }


def string_literals(path: Path) -> list[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    return [
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    ]


def test_structural_checkers_have_no_theory_snapshot_literals() -> None:
    concrete_result = re.compile(r"(?<![A-Za-z0-9_\\])[MR]\d+[A-Z]?(?![A-Za-z0-9_])")
    concrete_goal = re.compile(r"(?<![A-Za-z0-9_\\])Q\d+-\d+[A-Z]?(?:-[A-Z])?(?![A-Za-z0-9_])")
    concrete_section_path = re.compile(r"sections/[A-Za-z0-9_.\-/]+\.md")

    offenders: dict[str, list[str]] = {}
    for name in ("check_source.py", "check_project_consistency.py"):
        values = [
            value
            for value in string_literals(TOOLS / name)
            if concrete_result.search(value)
            or concrete_goal.search(value)
            or concrete_section_path.search(value)
        ]
        if values:
            offenders[name] = values

    assert offenders == {}, (
        "structural checker contains theory-snapshot literals; "
        "move PR-specific checks to tools/migrations/: " + repr(offenders)
    )


def test_project_consistency_checker_is_called_by_ci() -> None:
    workflow = (ROOT / ".github" / "workflows" / "verify.yml").read_text(encoding="utf-8")
    assert "python tools/check_project_consistency.py" in workflow


def test_migrations_are_not_called_by_ci() -> None:
    workflow = (ROOT / ".github" / "workflows" / "verify.yml").read_text(encoding="utf-8")
    assert "migrations/" not in workflow
    assert "tools/migrations" not in workflow


def test_verify_workflow_is_read_only_and_dispatchable() -> None:
    workflow = (ROOT / ".github" / "workflows" / "verify.yml").read_text(encoding="utf-8")
    assert "workflow_dispatch:" in workflow
    assert "contents: read" in workflow
    for forbidden in ("git push", "git commit", "contents: write"):
        assert forbidden not in workflow


def test_sync_paper_workflow_is_manual_and_scoped() -> None:
    workflow = (ROOT / ".github" / "workflows" / "sync-paper.yml").read_text(encoding="utf-8")
    assert "workflow_dispatch:" in workflow
    assert "\n  pull_request:" not in workflow
    assert "\n  push:" not in workflow
    assert "contents: write" in workflow
    assert "actions: write" in workflow
    assert "pull-requests: read" in workflow
    assert 'test "$TARGET_BRANCH" != "$DEFAULT_BRANCH"' in workflow
    assert 'gh pr list --repo "$GITHUB_REPOSITORY" --head "$TARGET_BRANCH" --state open' in workflow
    assert "git push --force" not in workflow
    assert "git push -f" not in workflow
    assert "git add -- paper.md main.tex paper.pdf" in workflow
    assert "gh workflow run verify.yml --ref \"$TARGET_BRANCH\"" in workflow


def test_physics_runner_does_not_stop_at_first_failure() -> None:
    tree = ast.parse((TOOLS / "run_physics_checks.py").read_text(encoding="utf-8"))
    breaks = [node for node in ast.walk(tree) if isinstance(node, ast.Break)]
    assert breaks == [], "physics runner must collect all independent failures"


def test_generated_and_latex_semantics_are_separate() -> None:
    generated = (TOOLS / "check_generated.py").read_text(encoding="utf-8")
    semantic = (TOOLS / "check_latex_semantics.py").read_text(encoding="utf-8")
    assert "latex_log" not in generated
    assert "classify_latex_log" in semantic


def main() -> None:
    test_layout_warnings_are_not_hard()
    test_semantic_tex_failures_are_hard()
    test_structural_checkers_have_no_theory_snapshot_literals()
    test_project_consistency_checker_is_called_by_ci()
    test_migrations_are_not_called_by_ci()
    test_verify_workflow_is_read_only_and_dispatchable()
    test_sync_paper_workflow_is_manual_and_scoped()
    test_physics_runner_does_not_stop_at_first_failure()
    test_generated_and_latex_semantics_are_separate()
    print("validation_policy_test_ok")


if __name__ == "__main__":
    main()
