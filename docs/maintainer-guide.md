# Maintainer Guide

## Review before publishing a workshop

- [ ] Audience, duration, level, prerequisites, and required tools are stated.
- [ ] Learning outcomes are observable and achievable in the stated time.
- [ ] Every command and code sample has been tested in a clean environment.
- [ ] Exercises include clear instructions and expected results.
- [ ] Safety, privacy, accessibility, and offline/low-bandwidth considerations are addressed.
- [ ] Third-party materials have compatible licenses and attribution.
- [ ] The README includes a status and an owner/contact route.
- [ ] Internal Markdown links and example tests pass.

## Content lifecycle

1. **Draft:** author prepares content using the template.
2. **In review:** reviewer checks technical accuracy, pedagogy, accessibility, and safety.
3. **Reviewed:** required corrections are addressed and a review date is recorded.
4. **Maintained:** a named maintainer agrees to respond to issues and periodically recheck dependencies and tool versions.

Review status should not imply formal accreditation, course credit, or professional certification.

## Repository maintenance

- Keep pull requests focused and require human review of learning and safety claims.
- Review GitHub Actions permissions and third-party action changes before updating workflows.
- Rotate credentials if accidentally exposed and handle student or personal data privately.
- Periodically test workshops from a clean checkout and update version-specific instructions.
- Archive obsolete instructions with a visible notice rather than leaving learners to assume they are current.
