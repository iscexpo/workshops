"""Lightweight checks for the ISC Expo Workshops repository.

Checks required files and relative targets in Markdown links. External links are
not requested, so this script runs without network access.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    "CONTENT-LICENSE.md",
    "workshops/README.md",
    "workshops/python-foundations/README.md",
    "workshops/git-github-collaboration/README.md",
    "workshops/web-development-basics/README.md",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/workshop_proposal.yml",
    ".github/workflows/validate.yml",
)
LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)


def check_required_files() -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"Missing required file: {relative}")
    return errors


def markdown_heading_slugs(text: str) -> set[str]:
    slugs: set[str] = set()
    occurrences: dict[str, int] = {}
    for match in HEADING_RE.finditer(text):
        heading = re.sub(r"`([^`]*)`", r"\1", match.group(1))
        heading = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", heading)
        slug = re.sub(r"[^\w -]", "", heading.lower())
        slug = re.sub(r"\s+", "-", slug.strip())
        if not slug:
            continue
        occurrence = occurrences.get(slug, 0)
        occurrences[slug] = occurrence + 1
        slugs.add(slug if occurrence == 0 else f"{slug}-{occurrence}")
    return slugs


def check_markdown_links() -> list[str]:
    errors: list[str] = []
    for markdown in sorted(ROOT.rglob("*.md")):
        if any(part in {".git", ".venv", "node_modules"} for part in markdown.parts):
            continue
        text = markdown.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            raw_target = match.group(1).strip()
            # Ignore optional link titles; this project uses simple Markdown links.
            target = raw_target.split(maxsplit=1)[0].strip("<>") if raw_target else ""
            parsed = urlparse(target)
            if not target or parsed.scheme or parsed.netloc:
                continue
            path_part = unquote(parsed.path)
            candidate = (markdown.parent / path_part).resolve() if path_part else markdown.resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"Link escapes repository: {markdown.relative_to(ROOT)} -> {target}")
                continue
            if not candidate.exists():
                errors.append(f"Broken local link: {markdown.relative_to(ROOT)} -> {target}")
                continue
            if parsed.fragment and candidate.suffix.lower() == ".md" and candidate.is_file():
                fragment = unquote(parsed.fragment)
                heading_slugs = markdown_heading_slugs(candidate.read_text(encoding="utf-8"))
                if fragment not in heading_slugs:
                    errors.append(
                        f"Broken Markdown fragment: {markdown.relative_to(ROOT)} -> {target}"
                    )
    return errors


def main() -> int:
    errors = check_required_files() + check_markdown_links()
    if errors:
        print("Repository validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Repository validation passed: required files and local Markdown targets exist.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
