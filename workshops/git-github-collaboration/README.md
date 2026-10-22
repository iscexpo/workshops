# Git & GitHub Collaboration

**Level:** Beginner · **Duration:** 60–90 minutes · **Status:** Draft  
**Audience:** Learners collaborating on code or learning materials  
**Last reviewed:** Not yet reviewed

## Learning outcomes

Learners should be able to explain the difference between a repository and a commit, make a small change on a branch, and describe how a pull request helps others review work.

## Prerequisites

A Git installation, a terminal or GUI client, and a GitHub account if learners will push changes to GitHub. Account creation and access requirements should be arranged before class. Never share passwords or personal access tokens with a facilitator or classmate.

## Session plan

1. **Repository and history (10 min):** folders, commits, remotes, and the purpose of version control.
2. **Inspect and clone (10–15 min):** open a practice repository and read its README.
3. **Branch and edit (15 min):** create a branch and make a small documentation change.
4. **Commit and compare (10 min):** review the diff before committing.
5. **Pull request (15–20 min):** describe the change, request review, and respond to feedback.
6. **Reflection (5 min):** explain why a branch is helpful.

## Practice flow

Use a repository where you have permission to contribute. Replace `<your-branch>` with a short branch name.

```bash
git status
git switch -c docs/my-first-change
# Make and save a small, non-sensitive README edit.
git diff
git add README.md
git commit -m "docs: improve workshop introduction"
```

If you are authorized to push to the repository:

```bash
git push -u origin docs/my-first-change
```

Then open a pull request on GitHub and explain the reason for the change. In a fork-based workflow, push to your fork and open a pull request against the original repository.

## Review checklist

- Does the change solve the stated problem?
- Is the diff limited to the intended files?
- Is the title clear and the description useful?
- Have tests or documentation checks been run if relevant?
- Are there any secrets or private information in the diff?

## Safety notes

Never commit `.env` files, API keys, passwords, student records, or private contact details. Do not run scripts from an unknown repository without inspecting them first. For classroom practice, use a sandbox repository rather than changing production code.

## Reflection

In your own words: how does a branch differ from the main branch? What information should a useful pull request description include?
