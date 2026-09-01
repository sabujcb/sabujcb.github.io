---
name: github-pages-academic-portfolio
description: Design, audit, optimize, and maintain evidence-based academic or technical portfolios hosted on GitHub Pages, especially Jekyll and al-folio sites. Use for portfolio information architecture, visual systems, responsive components, accessibility, SEO, performance, GitHub Actions, or pull-request delivery; do not use for unrelated application development.
---

# GitHub Pages Academic Portfolio

Build a portfolio that makes the person's research direction, technical capability, and evidence easy to understand. Treat visual polish, accessibility, content integrity, and maintainability as one system.

## Start from repository evidence

1. Inspect the repository root, current branch, status, remote, theme/runtime version, page collection, layouts, styles, build workflow, and existing content conventions.
2. Preserve unrelated work and existing URLs. Prefer a focused feature branch.
3. Identify which files are owned locally and which are supplied by the theme or a gem. Prefer additive site-level layouts and partials to large upstream overrides. If an override is necessary, document why and keep it narrow.
4. Treat profile and CV claims as user-provided evidence. Do not invent publications, affiliations, metrics, credentials, project outcomes, or proficiency levels.
5. Never publish private source documents, salary data, personal addresses, signatures, identification numbers, or contract administration details.

## Choose the smallest useful mode

- **Audit:** assess information hierarchy, visual consistency, responsiveness, accessibility, SEO, performance, content evidence, and deployment reliability.
- **Design system:** define tokens, typography, spacing, surfaces, focus states, cards, navigation, buttons, and light/dark behavior before styling individual pages.
- **Portfolio implementation:** improve the homepage and relevant pages while preserving validated content and stable permalinks.
- **Content refinement:** structure each project around problem, method, validation, result, limitations, and resources. Separate verified outcomes from planned work.
- **Delivery:** validate locally, prepare a focused commit, and create or update a pull request only when remote writes are authorized.

Read [design system](references/design-system.md) before selecting colors or changing site-wide styling. Read [content and SEO](references/content-and-seo.md) when changing page structure, professional positioning, metadata, or project narratives. Read [validation](references/validation.md) before declaring the work complete.

## Implementation rules

- Use semantic HTML and native navigation landmarks. Keep one clear page heading and a logical heading hierarchy.
- Centralize shared visual rules. Do not duplicate a full design system inside individual page files.
- Use CSS custom properties as the public token layer. Define both light and dark values and keep component rules token-driven.
- Keep body copy comfortable at 16px-equivalent or larger in the browser. Limit prose width to roughly 65–75 characters.
- Use responsive grids that collapse without horizontal scrolling. Verify at mobile, tablet, desktop, and 200% text zoom.
- Make link, button, hover, active, and keyboard-focus states visibly distinct. Do not communicate meaning through color alone.
- Prefer restrained motion. Respect `prefers-reduced-motion` and avoid decorative animation that delays content.
- Optimize images with correct dimensions, descriptive alt text, and lazy loading except for the primary above-the-fold profile image.
- Keep external links explicit and safe. Use `rel="noopener noreferrer"` for new-tab links.
- Preserve working dark mode, search, CV download, structured metadata, canonical URLs, and deployment paths.

## Quality gates

Before handoff:

1. Run the repository formatter and production build.
2. Run `scripts/audit_portfolio.py REPOSITORY_ROOT` from this skill.
3. Check every foreground/background pair with `scripts/check_contrast.py`; normal text must reach 4.5:1 and large text or essential UI graphics 3:1.
4. Inspect the rendered homepage and every materially changed page at desktop and mobile widths, in light and dark modes.
5. Verify keyboard navigation, visible focus, image alt text, headings, landmarks, internal links, CV download, and external profile links.
6. Review the full branch diff for private information, unrelated files, generated clutter, and unsupported claims.
7. Report checks actually run, remaining limitations, files changed, and remote actions performed.

Do not describe a CI configuration as passing until the corresponding run completes successfully. If a production build cannot run locally, state that clearly and require the pull-request build to pass before recommending merge.
