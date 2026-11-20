"""Validate repository Markdown links and the required kickoff documents."""
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


inline_link = re.compile(
    r"""
    \]\(\s*
    (?: <(?P<angle>[^<>\n]*)> | (?P<bare>[^\s)]+) )
    (?: \s+ (?: "(?:\\.|[^"\\])*" | '(?:\\.|[^'\\])*' | \((?:\\.|[^()\\])*\) ) )?
    \s*\)
    """,
    re.VERBOSE,
)
root = Path(__file__).resolve().parents[2]
required = ["README.md", "docs/course.md", "docs/research-plan.md"]
errors = [f"Missing document: {name}" for name in required if not (root / name).is_file()]
for document in root.rglob("*.md"):
    if ".git" in document.relative_to(root).parts:
        continue
    content = document.read_text(encoding="utf-8")
    if not content.strip():
        errors.append(f"Empty document: {document.relative_to(root)}")
    for match in inline_link.finditer(content):
        target = match["bare"] if match["angle"] is None else match["angle"]
        url = urlsplit(target)
        if url.scheme or url.netloc or not url.path:
            continue
        if not (document.parent / unquote(url.path)).exists():
            errors.append(f"{document.relative_to(root)}: missing {target}")
if errors:
    sys.exit("\n".join(errors))
print("Required documents and relative Markdown links passed.")
