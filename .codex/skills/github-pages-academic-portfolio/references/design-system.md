# Academic portfolio design system

## Visual direction

Use a restrained institutional palette rather than a high-saturation product-marketing palette. A reliable pattern is:

- deep navy for authority, headings, and the primary dark surface;
- accessible blue for links and primary actions;
- teal for scientific or research emphasis;
- warm gold only for small decorative accents, never as low-contrast body text;
- cool off-white and blue-grey neutrals for reading surfaces and borders.

The palette should support the content hierarchy, not become the subject of the page. Use one dominant accent and one secondary accent per component.

## Recommended token model

Define semantic tokens rather than embedding colors in components:

- `--global-bg-color`, `--global-card-bg-color`, `--global-text-color`, `--global-text-color-light`;
- `--global-theme-color`, `--global-hover-color`, `--global-divider-color` for theme compatibility;
- site tokens such as `--academic-navy`, `--academic-teal`, `--academic-gold`, `--academic-surface-soft`, `--academic-shadow`, and `--academic-focus`;
- spacing, radius, maximum reading width, and transition tokens.

Every token that changes meaning between light and dark modes needs an explicit dark value. Component rules should consume tokens and should not repeat raw hex values except for fixed transparent overlays.

## Typography

- Prefer a neutral humanist sans serif for navigation and body text.
- A restrained serif may be used for major academic headings if it remains readable and loads efficiently.
- Keep line height around 1.55–1.75 for prose and 1.1–1.3 for headings.
- Use weight, size, spacing, and structure together; do not rely only on color.
- Avoid justified body text and overly narrow columns.

## Components

- **Navigation:** quiet surface, strong active state, adequate targets, stable mobile collapse, and clear focus rings.
- **Hero:** one career thesis, one short supporting paragraph, two primary actions at most, then compact evidence or focus labels.
- **Cards:** subtle border and shadow, consistent radii, no excessive hover lift, and no interaction styling on non-clickable cards.
- **Project evidence:** expose method, validation, result, limitation, and source links without burying them in decorative UI.
- **Calls to action:** primary action uses the accessible blue; secondary action uses a bordered surface. Both require hover and focus states.
- **Photography:** use one professional profile image with a quiet frame; do not add generic stock photography to technical portfolio pages.

## Accessibility invariants

- Normal text contrast: at least 4.5:1.
- Large text and essential non-text UI contrast: at least 3:1.
- Focus indicator: visible at 2px or stronger and distinguishable from the component and its surrounding surface.
- Target size: aim for at least 44px in the primary navigation and calls to action.
- Motion: disable non-essential transforms and transitions under `prefers-reduced-motion: reduce`.
- Zoom/reflow: content must remain usable at 200% text zoom and narrow mobile widths.

Use `scripts/check_contrast.py` for deterministic color-pair checks before relying on visual judgement.
