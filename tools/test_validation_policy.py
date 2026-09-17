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


def test_source_checker_has_no_theory_snapshot_literals() -> None:
    path = TOOLS / "check_source.py"
    literals = string_literals(path)
    concrete_result = re.compile(r"(?<![A-Za-z0-9_\\])[MR]\d+[A-Z]?(?![A-Za-z0-9_])")
    concrete_goal = re.compile(r"(?<![A-Za-z0-9_\\])Q\d+-\d+[A-Z]?(?:-[A-Z])?(?![A-Za-z0-9_])")
    concrete_section = re.compile(r"(?:sections/)?A?\d+_[A-Za-z0-9_\-]+\.md")

    offenders: list[str] = []
    for value in literals:
        if concrete_result.search(value) or concrete_goal.search(value) or concrete_section.search(value):
            offenders.append(value)

    assert offenders == [], (
        "check_source.py contains theory-snapshot literals; "
        "move PR-specific checks to tools/migrations/: " + repr(offenders)
    )


def test_migrations_are_not_called_by_ci() -> None:
    workflow = (ROOT / ".github" / "workflows" / "verify.yml").read_text(encoding="utf-8")
    assert "migrations/" not in workflow
    assert "tools/migrations" not in workflow


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
    test_source_checker_has_no_theory_snapshot_literals()
    test_migrations_are_not_called_by_ci()
    test_physics_runner_does_not_stop_at_first_failure()
    test_generated_and_latex_semantics_are_separate()
    print("validation_policy_test_ok")


if __name__ == "__main__":
    main()
