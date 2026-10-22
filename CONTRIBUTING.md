# Contributing to ISC Expo Workshops

Thank you for helping make practical learning more accessible. Contributions can include fixing an error, clarifying a step, adding an exercise, improving accessibility, translating material, or proposing a new workshop.

## Before you start

1. Search existing issues and folders so work is not duplicated.
2. For a substantial change, open an issue first to discuss the learner need and scope.
3. Check source licenses and get permission before adding third-party text, images, datasets, or code.
4. Do not include private student data, credentials, or confidential event information.

## Contribution workflow

1. Fork the repository and create a focused branch.
2. Make a small, clearly scoped change.
3. Run the validation steps below.
4. Open a pull request describing the learner problem, what changed, and how you checked it.
5. Respond constructively to review feedback.

Suggested branch names: `docs/python-loops`, `lab/html-links`, or `fix/setup-instructions`.

## Workshop content checklist

- State the audience, estimated duration, level, prerequisites, and required equipment/software.
- Write measurable learning outcomes using plain language.
- Number the steps and explain important commands before asking learners to run them.
- Include expected output or a screenshot description, troubleshooting, and a short knowledge check.
- Provide a stretch activity and, where useful, a solution or facilitator notes.
- Keep examples small, reproducible, and free of real credentials or personal data.
- Use descriptive links, meaningful heading order, accessible tables, and text alternatives for meaningful images.
- Identify the content's status (`Draft`, `In review`, `Reviewed`, or `Maintained`) and the review date when applicable.
- Add sources and license/attribution notes for adapted materials.

## Local checks

From the repository root:

```bash
python scripts/validate.py
python -m unittest discover -s examples/python-hello/tests -v
```

If you add YAML issue forms, ensure they parse. On systems with Ruby installed:

```bash
ruby -e 'require "yaml"; Dir.glob(".github/ISSUE_TEMPLATE/*.yml").each { |file| YAML.load_file(file, aliases: true); puts "Validated #{file}" }'
```

The GitHub Actions workflow runs the repository validation and example tests for pushes and pull requests.

## Review principles

Maintainers review changes for learner value, clarity, technical accuracy, safety, attribution, accessibility, and maintainability. Review and response timing may vary. Content may be returned for revisions or declined if it is unsafe, unlicensed, misleading, or outside this repository's scope.

## Privacy and safety

Do not commit API keys, access tokens, passwords, private keys, `.env` files, student IDs, grades, attendance lists, private submissions, or personal contact details. Do not publish photos or work that identifies another person without appropriate permission. If you discover exposed information, do not repeat it in an issue; contact maintainers privately using the guidance in [SECURITY.md](SECURITY.md).
