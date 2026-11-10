#!/usr/bin/env python3
"""Check that relative Markdown links point to files or directories in this repository."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK_PATTERN = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
errors = []

for markdown_file in sorted(ROOT.rglob("*.md")):
    if any(part in {".git", ".venv", "build", "install", "log"} for part in markdown_file.parts):
        continue

    content = markdown_file.read_text(encoding="utf-8")
    for match in LINK_PATTERN.finditer(content):
        target = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
        parsed = urlsplit(target)

        if parsed.scheme or parsed.netloc or not parsed.path:
            continue

        relative_target = unquote(parsed.path)
        resolved = (markdown_file.parent / relative_target).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            errors.append(f"{markdown_file.relative_to(ROOT)}: link escapes repository: {target}")
            continue

        if not resolved.exists():
            line = content.count("\n", 0, match.start()) + 1
            errors.append(f"{markdown_file.relative_to(ROOT)}:{line}: missing target: {target}")

if errors:
    print("Markdown link check failed:")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print("Markdown link check passed.")
