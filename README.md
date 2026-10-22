# ISC Expo Workshops

**Innovation, Skills & Career Expo**  
*Build skills. Explore technology. Shape your future.*

Hands-on learning resources, guided labs, starter projects, and workshop templates for learners, educators, mentors, and community contributors.

[Organization](https://github.com/iscexpo) · [Website](https://iscexpo.edu.bd) · [Support](mailto:info@iscexpo.edu.bd)

> **Repository status:** The public repository is established and the initial scaffold is published. Individual workshop materials may still be drafts until a maintainer marks them as reviewed. Check each workshop's status before using it in a live class or event.

## What you'll find here

- **Workshops** — step-by-step sessions with goals, prerequisites, timing, and hands-on activities.
- **Labs** — short exercises designed to help you learn by doing.
- **Examples** — small, runnable reference projects.
- **Templates** — reusable workshop, lab, and project outlines for contributors.
- **Learning paths** — suggested routes through related topics.

## Start learning

1. Browse the [workshop index](workshops/README.md).
2. Choose a workshop that matches your current experience and the requirements listed in its README.
3. Read the setup and safety notes before running commands or code.
4. Complete the exercises in order, then try the stretch task.
5. Share feedback by opening an issue using the appropriate template.

### Suggested first sessions

| Topic | Good first step | Folder |
|---|---|---|
| Python foundations | Run a tiny program and change its output | [Python foundations](workshops/python-foundations/README.md) |
| Git and GitHub | Learn how branches and pull requests work | [Git & GitHub collaboration](workshops/git-github-collaboration/README.md) |
| Web development | Build a basic HTML page and style it with CSS | [Web development basics](workshops/web-development-basics/README.md) |

## Use this repository locally

You need Git and a code editor. Some workshops need additional tools; their READMEs explain those requirements.

```bash
git clone https://github.com/iscexpo/workshops.git
cd workshops
```

Open a workshop directory and follow its instructions. For the Python example, from the repository root run:

```bash
python examples/python-hello/main.py
python -m unittest discover -s examples/python-hello/tests -v
```

Use `python3` instead of `python` if that is how Python is installed on your system.

## For educators and mentors

- Adapt the timing to your learners and local context.
- Explain unfamiliar terminology and show the expected result before independent work.
- Provide alternatives for learners using different devices or accessibility tools.
- Mark copied or adapted resources with attribution and make sure the license permits reuse.
- Do not publish learner names, student IDs, marks, private submissions, photos, or contact details without appropriate permission.
- Review code and commands before asking learners to run them. Never ask learners to paste secrets or credentials into public tools.

## Workshop quality and status

Every workshop should include learning outcomes, prerequisites, setup steps, time estimates, exercises, expected outcomes, troubleshooting, and a way to check learning. Use one of these status labels in its README:

- `Draft` — incomplete or not yet reviewed.
- `In review` — ready for feedback, but not yet approved for delivery.
- `Reviewed` — checked by a maintainer for clarity, safety, and technical correctness.
- `Maintained` — reviewed and has an identified owner for future updates.

These labels describe the contents of a workshop, not academic accreditation or certification.

## Contributing

Issues and pull requests are welcome for corrections, translations, new labs, accessibility improvements, and additional learning paths. Read [CONTRIBUTING.md](CONTRIBUTING.md), follow the [Code of Conduct](CODE_OF_CONDUCT.md), and use the templates in `templates/` as needed.

For the contributor workflow and local checks, see [PUBLISHING.md](PUBLISHING.md).

## Safety, privacy, and licensing

- Review commands before executing them; use a disposable environment for unfamiliar or destructive operations.
- Keep tokens, passwords, private keys, environment files, and personal/student data out of commits and issue reports.
- Report security concerns privately via [SECURITY.md](SECURITY.md).
- Source-code examples are covered by the [MIT License](LICENSE). Original lesson text, diagrams, and other learning content are covered by [CC BY 4.0](CONTENT-LICENSE.md), unless a file states otherwise. Third-party content retains its own license and attribution requirements.

## Repository map

```text
.
├── .github/                # Issue forms, PR template, CI
├── docs/                   # Learning paths and maintainer notes
├── examples/               # Small runnable reference projects
├── labs/templates/         # Template for standalone labs
├── scripts/                # Local validation scripts
├── templates/              # Workshop, lab, and project templates
└── workshops/              # Topic-based workshop materials
```

## Maintainers

For repository questions, contact [info@iscexpo.edu.bd](mailto:info@iscexpo.edu.bd). Public issues are for non-sensitive questions only.
