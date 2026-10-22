#!/usr/bin/env bash
set -euo pipefail

REPO="iscexpo/workshops"

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is required. Install it from https://cli.github.com/ and retry." >&2
  exit 1
fi

gh auth status >/dev/null

if gh repo view "$REPO" >/dev/null 2>&1; then
  echo "Repository $REPO already exists or is visible to this account. Refusing to overwrite it." >&2
  echo "Review the repository before deciding how to publish this scaffold." >&2
  exit 1
fi

gh repo create "$REPO" --public --source=. --remote=origin --push

echo "Published https://github.com/$REPO"
