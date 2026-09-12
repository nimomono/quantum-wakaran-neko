#!/usr/bin/env python3
from __future__ import annotations

import re
import _cleanup_active_docs_v2_once as m


def sub_block(text: str, pattern: str, replacement: str, label: str) -> str:
    matches = list(re.finditer(pattern, text, flags=re.S))
    if len(matches) != 1:
        raise SystemExit(f"{label}: expected 1 match, found {len(matches)}")
    return re.sub(pattern, lambda _: replacement, text, count=1, flags=re.S)


def sub_line(text: str, pattern: str, replacement: str, label: str) -> str:
    matches = list(re.finditer(pattern, text, flags=re.M))
    if len(matches) != 1:
        raise SystemExit(f"{label}: expected 1 line match, found {len(matches)}")
    return re.sub(pattern, lambda _: replacement, text, count=1, flags=re.M)


m.sub_block = sub_block
m.sub_line = sub_line

m.patch_readme()
m.patch_project_status()
m.patch_a3()
m.patch_r144()
m.final_guards()
print("active_document_cleanup_ok")
