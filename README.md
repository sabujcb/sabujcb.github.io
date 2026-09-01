# Sabuj C. Bhowmick — Portfolio

Source for [sabujcb.github.io](https://sabujcb.github.io), a focused research and technical portfolio covering:

- data science and applied statistics;
- machine learning engineering and evaluation;
- bioinformatics, microbiome analytics, and multi-omics integration;
- reproducible scientific software and data-intensive workflows.

## Site structure

- **About** — professional profile and technical focus
- **Research** — current research direction and open-source contributions
- **Projects** — selected work with methods, validation, results, and limitations
- **CV** — education, experience, skills, and project record
- **Contact** — professional contact channels

## Local development

The site uses Jekyll and the [al-folio](https://github.com/alshedivat/al-folio) theme.

```bash
bundle install
npm ci
bundle exec jekyll serve
```

Run formatting and a production build before submitting changes:

```bash
npm run lint:prettier
JEKYLL_ENV=production bundle exec jekyll build
```

## Content policy

Portfolio claims should be supported by project records, repositories, reports, or reproducible results. Template demonstrations and unrelated sample material are intentionally excluded.

## Portfolio maintenance skill

The repository includes a reusable Codex skill at
`.codex/skills/github-pages-academic-portfolio/`. It defines the design, accessibility, evidence, SEO, validation, and
pull-request workflow for future portfolio work.

Invoke it with `$github-pages-academic-portfolio` when auditing, redesigning, optimizing, or extending this site.

## License

The site source is available under the terms in [LICENSE](LICENSE).
