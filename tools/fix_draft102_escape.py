#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).resolve().parent / "check_source.py"
b = p.read_bytes()
b = b.replace(b'"mu_{\rm_sh}"', b'"mu_sh"')
p.write_bytes(b)
print("draft102_escape_fix_ok")
