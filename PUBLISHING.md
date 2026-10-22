# Repository Maintenance and Publishing

The public repository already exists at [iscexpo/workshops](https://github.com/iscexpo/workshops). This guide describes how to work with the existing repository safely; it is not an instruction to create a second repository.

## Clone the existing repository

Prerequisites: Git, and a GitHub account with the appropriate permissions for the changes you intend to make.

```bash
git clone https://github.com/iscexpo/workshops.git
cd workshops
git switch -c docs/your-change
```

Make your edits, then run the local validation and tests:

```bash
python scripts/validate.py
python -m compileall -q examples workshops
python -m unittest discover -s examples/python-hello/tests -v
```

If Ruby is installed, also validate the GitHub issue-form YAML:

```bash
ruby -e 'require "yaml"; Dir.glob(".github/ISSUE_TEMPLATE/*.yml").each { |file| YAML.load_file(file, aliases: true); puts "Validated #{file}" }'
```

Review your diff and make sure you have not included credentials, private student information, or materials without permission:

```bash
git status --short
git diff --check
git diff
```

Commit your changes, push the branch, and open a pull request:

```bash
git add README.md PUBLISHING.md
git commit -m "docs: clarify repository maintenance workflow"
git push -u origin docs/your-change
gh pr create --repo iscexpo/workshops --base main --head docs/your-change
```

Adjust the `git add` paths to match the files you actually changed. If you do not have write access to the organization, fork the repository and open a pull request from your fork.

## CI validation

Every push and pull request triggers the workflow at `.github/workflows/validate.yml`. A successful run checks required files, local Markdown link targets, Python compilation, example tests, and issue-form YAML.

Inspect the workflow result before merging. A green check validates the automated checks; it does not replace human review of instructional accuracy, accessibility, safety, or license attribution.

## Repository creation script

`scripts/publish-repo.sh` is a guarded bootstrap helper intended for a fresh repository. Because `iscexpo/workshops` already exists, **do not run the creation script to publish this repository again**. It is designed to stop when the repository already exists or is visible to your account.

For future changes to this existing repository, use the clone → branch → test → pull request workflow above. Never force-push or replace the existing repository history as a publishing shortcut.

## Access and ownership

Creating repositories, changing organization security settings, branch protection, or team permissions requires an authorized organization account. If the CLI reports insufficient permission, ask an organization owner to grant the smallest suitable role rather than sharing credentials or tokens.
