# Validation and delivery

## Local checks

Run the repository's own commands first. For a typical Jekyll portfolio:

```bash
npm ci
npm run lint:prettier
JEKYLL_ENV=production bundle exec jekyll build
```

Then run the skill checks:

```bash
python SKILL_ROOT/scripts/audit_portfolio.py REPOSITORY_ROOT
python SKILL_ROOT/scripts/check_contrast.py --pair "body:#172033:#f7f9fc:4.5" --pair "link:#0b5cad:#ffffff:4.5"
```

Use the actual skill and repository paths; do not copy the placeholders literally.

## Rendered review

Inspect at minimum:

- homepage, Research, Projects, CV, and Contact;
- 375px, 768px, and wide desktop viewports;
- light and dark themes;
- keyboard-only navigation and visible focus;
- text zoom or browser zoom at 200%;
- profile image, internal links, project links, social profiles, and CV download;
- heading order, landmarks, accessible names, and alt text;
- overflow, clipping, awkward line breaks, layout shift, and insufficient card spacing.

When available, run Lighthouse or an equivalent accessibility/performance audit against the production build. Treat automated scores as signals, not proof of usability.

## Pull request

Keep the branch focused. The pull request should explain:

- the design and information-hierarchy problem;
- the new token system and major component changes;
- content or URL changes, if any;
- accessibility, responsive, performance, and build validation;
- theme overrides and future-upgrade implications;
- screenshots or preview artifacts when available;
- rollback, normally reverting the focused merge commit.

Wait for required checks. Fix failures on the same branch, rerun validation, and update the pull request rather than opening replacement pull requests for the same change.
