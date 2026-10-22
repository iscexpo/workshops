# Publish this scaffold to GitHub

This scaffold has been prepared locally; the script below creates a **new public** repository and pushes the current directory. It will stop if `iscexpo/workshops` already exists or is visible to the authenticated account, so it will not overwrite an existing repository.

## Prerequisites

- Git installed
- GitHub CLI (`gh`) installed
- An account authorized to create public repositories in the `iscexpo` organization
- Approval from the organization owner if your account does not have permission

## Publish

From the root of this folder:

```bash
gh auth login
bash scripts/publish-repo.sh
```

Inspect the repository name, visibility, and files before confirming any GitHub CLI prompts. The script creates only `iscexpo/workshops`; it does not change organization settings or invite members.

If you prefer to create the repository manually, create a **public** empty repository named `workshops` under `iscexpo` (do not initialize it with a README, license, or `.gitignore`), then run:

```bash
git init -b main
git add .
git commit -m "chore: initialize ISC Expo workshops scaffold"
git remote add origin https://github.com/iscexpo/workshops.git
git push -u origin main
```

If the repository already exists, stop and inspect it. Do not force-push or replace existing content. For an existing project, integrate these files through a branch and pull request instead.
