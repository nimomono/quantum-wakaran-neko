#!/usr/bin/env python3
from __future__ import annotations

from latex_log import classify_latex_log


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
        "LaTeX Warning: Citation `bell1964' on page 2 undefined on input line 88.\n"
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


def main() -> None:
    test_layout_warnings_are_not_hard()
    test_semantic_tex_failures_are_hard()
    print("validation_policy_test_ok")


if __name__ == "__main__":
    main()
