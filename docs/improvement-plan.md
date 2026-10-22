# Repository Analysis and Improvement Plan

## Current assessment

This repository is a clearly labeled initial scaffold for beginner workshops. It has a useful set of starter workshops, runnable examples, contribution guidance, reusable templates, licensing and privacy guidance, and a GitHub Actions workflow. The workshop index correctly labels the current workshops as drafts.

The main near-term gap is human review against the repository's own quality standards. All workshops now name a contactable maintainer team, but remain drafts and need technical and instructional review before live delivery. The Git workshop now includes an isolated local practice route, and Python Foundations links to its companion exercises.

Automated checks provide a good baseline: required-file and local Markdown target checks, Python compilation, example tests, and issue-form YAML parsing. The Markdown checker now checks fragments for same-page and local Markdown links, including duplicate heading slugs. Unit tests cover broken fragments, duplicate headings, URL-encoded paths, and links escaping the repository. It remains a lightweight parser and does not replace a full Markdown parser or human content review.

## Prioritized plan

### 1. Prepare workshops for human review

- Name a maintainer or accountable team for every workshop and provide a contact route.
- Complete the workshop template's missing learner-facing details consistently: setup verification, expected results, accessibility and safety notes, references, and facilitator guidance where applicable.
- Review each activity against the stated duration and learning outcomes; record a review date only after a real technical and instructional review.
- Follow the checklist in [the maintainer guide](maintainer-guide.md), including testing commands and examples from a clean environment.

**Done when:** every workshop has an accountable owner, and each status accurately reflects a documented human review.

**Progress:** All current workshops now name the maintainer team and contact route. Human review and review dates remain outstanding.

### 2. Make learner practice safer and easier to follow

- Give the Git workshop a disposable practice path, such as a local-only exercise or a clearly identified sandbox repository. Explain when a GitHub account and remote push are optional versus required.
- Link Python Foundations directly to the existing [Python labs](../workshops/python-foundations/labs/01-hello.py) and [mini challenge](../workshops/python-foundations/labs/02-mini-challenge.md), and include expected results for the guided activities.
- Test the Web Development starter on a narrow viewport and with keyboard navigation; add any discovered fixes to the starter and its activity instructions.
- For each workshop, verify prerequisites, commands, and expected outcomes on the operating systems and classroom setups the maintainers intend to support.

**Done when:** a learner can complete the core activities using the documented materials without relying on unstated setup or access.

**Progress:** The Git workshop now provides local-only practice, and Python Foundations links to its existing lab and challenge. Remaining setup, expected-result, and accessibility review should be done with the intended learner environments.

### 3. Strengthen automated validation

- Completed: validator tests cover broken heading fragments, duplicate heading slugs, URL-encoded paths, and links escaping the repository root.
- Consider lightweight checks for required workshop metadata, while keeping instructional quality and safety decisions in human review.
- Keep CI's compile, example-test, and YAML checks; ensure the same commands remain documented in [Contributing](../CONTRIBUTING.md).

**Done when:** the validator's documented scope matches its tested behavior, and CI catches representative link and metadata regressions.

### 4. Establish a sustainable feedback loop

- Gather feedback from learners and facilitators after a pilot; turn recurring setup, pacing, and comprehension issues into small, tracked updates.
- Set a review cadence for maintained workshops, especially where tools or external services can change.
- Prioritize accessibility, translation, offline or low-bandwidth options, and low-cost tooling based on the intended audience and feedback.

**Done when:** maintained workshops have an owner and review cadence, with improvements informed by actual use.

## Verification baseline

At the time this plan was written, these local checks passed:

- `python scripts/validate.py`
- `python -m unittest discover -s tests -v`
- `python -m unittest discover -s examples/python-hello/tests -v`
- `python -m compileall -q examples workshops`

These checks confirm repository structure and the current Python example baseline. They do not constitute a human review or approval to deliver draft workshops.