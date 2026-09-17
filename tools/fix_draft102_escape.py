#!/usr/bin/env python3
import re
from pathlib import Path

p = Path(__file__).resolve().parent / "check_source.py"
text = p.read_text(encoding="utf-8")
text, n = re.subn(r'"mu_\{\s*m_sh\}"', '"mu_sh"', text, flags=re.S)
if n != 1:
    raise SystemExit(f"expected one malformed mu marker, found {n}")
p.write_text(text, encoding="utf-8")
print("draft102_escape_fix_ok")
