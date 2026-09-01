---
layout: page
permalink: /cv/
title: CV
nav: true
nav_order: 4
cv_pdf: /assets/rendercv/rendercv_output/Sabuj_C_Bhowmick_CV.pdf
description: Education, research experience, technical skills, and selected projects.
---

<style>
  .professional-cv {
    --cv-border: var(--global-divider-color, #d8dee4);
    --cv-surface: var(--global-card-bg-color, var(--global-bg-color, #fff));
    --cv-muted: var(--global-text-color-light, #6c757d);
  }

  .cv-hero {
    display: grid;
    grid-template-columns: minmax(0, 1fr) auto;
    gap: 1.5rem;
    align-items: center;
    margin-bottom: 2rem;
    padding: clamp(1.35rem, 4vw, 2.25rem);
    border: 1px solid var(--cv-border);
    border-radius: 1rem;
    background:
      radial-gradient(circle at top right, var(--academic-gold-soft), transparent 42%),
      linear-gradient(135deg, var(--academic-accent-soft), var(--academic-teal-soft));
  }

  .cv-eyebrow {
    margin-bottom: 0.5rem;
    color: var(--global-theme-color);
    font-size: 0.76rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }

  .cv-hero h2 {
    margin: 0 0 0.45rem;
    font-size: clamp(1.7rem, 4vw, 2.5rem);
    line-height: 1.1;
  }

  .cv-headline {
    margin: 0;
    color: var(--cv-muted);
    line-height: 1.55;
  }

  .cv-actions {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-end;
    gap: 0.55rem;
  }

  .cv-action {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.55rem 0.8rem;
    border: 1px solid var(--cv-border);
    border-radius: 0.6rem;
    background: var(--cv-surface);
    color: var(--global-text-color);
    font-size: 0.82rem;
    font-weight: 600;
    text-decoration: none;
  }

  .cv-action-primary {
    border-color: var(--global-theme-color);
    background: var(--global-theme-color);
    color: #fff;
  }

  .cv-action:hover {
    border-color: var(--global-theme-color);
    color: var(--global-theme-color);
  }

  .cv-action-primary:hover {
    color: #fff;
    filter: brightness(0.92);
  }

  .cv-jump-links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin-bottom: 2.4rem;
  }

  .cv-jump-links a {
    padding: 0.4rem 0.72rem;
    border: 1px solid var(--cv-border);
    border-radius: 999px;
    color: var(--global-text-color);
    font-size: 0.78rem;
    font-weight: 600;
    text-decoration: none;
  }

  .cv-jump-links a:hover {
    border-color: var(--global-theme-color);
    color: var(--global-theme-color);
  }

  .cv-section {
    margin-bottom: 2.6rem;
    scroll-margin-top: 5rem;
  }

  .cv-section-title {
    margin-bottom: 1rem;
    padding-bottom: 0.55rem;
    border-bottom: 1px solid var(--cv-border);
    font-size: 1.45rem;
  }

  .cv-profile {
    max-width: 76ch;
    font-size: 1rem;
    line-height: 1.75;
  }

  .cv-timeline {
    display: grid;
    gap: 0.9rem;
  }

  .cv-entry {
    display: grid;
    grid-template-columns: minmax(0, 1fr) auto;
    gap: 0.75rem 1.2rem;
    padding: 1.1rem 1.2rem;
    border: 1px solid var(--cv-border);
    border-radius: 0.85rem;
    background: var(--cv-surface);
  }

  .cv-entry h3 {
    margin: 0 0 0.25rem;
    font-size: 1.05rem;
    line-height: 1.4;
  }

  .cv-entry-subtitle {
    margin: 0;
    color: var(--cv-muted);
    font-size: 0.9rem;
    line-height: 1.5;
  }

  .cv-entry-date {
    color: var(--cv-muted);
    font-size: 0.8rem;
    font-weight: 600;
    white-space: nowrap;
  }

  .cv-entry-summary,
  .cv-entry-highlights {
    grid-column: 1 / -1;
  }

  .cv-entry-summary {
    margin: 0;
    font-size: 0.9rem;
    line-height: 1.6;
  }

  .cv-entry-highlights {
    margin: 0;
    padding-left: 1.15rem;
    font-size: 0.88rem;
    line-height: 1.55;
  }

  .cv-entry-highlights li + li {
    margin-top: 0.28rem;
  }

  .cv-skills-grid,
  .cv-project-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.8rem;
  }

  .cv-skill,
  .cv-project,
  .cv-language,
  .cv-interest {
    padding: 0.95rem 1rem;
    border: 1px solid var(--cv-border);
    border-radius: 0.75rem;
    background: var(--cv-surface);
  }

  .cv-skill h3,
  .cv-project h3,
  .cv-language strong,
  .cv-interest h3 {
    color: var(--global-text-color);
  }

  .cv-skill h3,
  .cv-project h3,
  .cv-interest h3 {
    margin: 0 0 0.4rem;
    font-size: 0.96rem;
  }

  .cv-skill p,
  .cv-project p,
  .cv-language span,
  .cv-interest p {
    margin: 0;
    color: var(--cv-muted);
    font-size: 0.84rem;
    line-height: 1.55;
  }

  .cv-project ul {
    margin: 0.65rem 0 0;
    padding-left: 1.05rem;
    font-size: 0.82rem;
    line-height: 1.5;
  }

  .cv-languages {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 0.65rem;
  }

  .cv-language strong,
  .cv-language span {
    display: block;
  }

  .cv-language strong {
    margin-bottom: 0.2rem;
    font-size: 0.9rem;
  }

  @media (max-width: 767px) {
    .cv-hero,
    .cv-entry,
    .cv-skills-grid,
    .cv-project-grid,
    .cv-languages {
      grid-template-columns: 1fr;
    }

    .cv-actions {
      justify-content: flex-start;
    }

    .cv-entry-date {
      grid-row: 2;
    }
  }
</style>

{% assign cv = site.data.cv.cv %}
{% assign sections = cv.sections %}

<div class="professional-cv">
  <header class="cv-hero">
    <div>
      <div class="cv-eyebrow">Curriculum vitae</div>
      <h2>{{ cv.name }}</h2>
      <p class="cv-headline">{{ cv.headline }}</p>
    </div>
    <div class="cv-actions" aria-label="CV and professional profiles">
      <a class="cv-action cv-action-primary" href="{{ page.cv_pdf | relative_url }}" target="_blank" rel="noopener">
        <i class="fa-solid fa-file-pdf" aria-hidden="true"></i> Download PDF
      </a>
      <a class="cv-action" href="https://github.com/sabujcb" target="_blank" rel="noopener noreferrer">
        <i class="fa-brands fa-github" aria-hidden="true"></i> GitHub
      </a>
      <a
        class="cv-action"
        href="https://www.linkedin.com/in/sabuj-bhowmick-34920874/"
        target="_blank"
        rel="noopener noreferrer"
      >
        <i class="fa-brands fa-linkedin" aria-hidden="true"></i> LinkedIn
      </a>
    </div>
  </header>

  <nav class="cv-jump-links" aria-label="CV sections">
    <a href="#profile">Profile</a>
    <a href="#experience">Experience</a>
    <a href="#education">Education</a>
    <a href="#skills">Skills</a>
    <a href="#selected-projects">Projects</a>
    <a href="#languages">Languages</a>
    <a href="#interests">Interests</a>
  </nav>

  <section id="profile" class="cv-section">
    <h2 class="cv-section-title">Profile</h2>
    <div class="cv-profile">
      {% for paragraph in sections.Profile %}
        {{ paragraph | markdownify }}
      {% endfor %}
    </div>
  </section>

  <section id="experience" class="cv-section">
    <h2 class="cv-section-title">Experience</h2>
    <div class="cv-timeline">
      {% for item in sections.Experience %}
        <article class="cv-entry">
          <div>
            <h3>{{ item.position }}</h3>
            <p class="cv-entry-subtitle">{{ item.company }}</p>
          </div>
          <div class="cv-entry-date">{{ item.start_date }} — {{ item.end_date }}</div>
          {% if item.summary %}<p class="cv-entry-summary">{{ item.summary }}</p>{% endif %}
          {% if item.highlights %}
            <ul class="cv-entry-highlights">
              {% for highlight in item.highlights %}
                <li>{{ highlight }}</li>
              {% endfor %}
            </ul>
          {% endif %}
        </article>
      {% endfor %}
    </div>
  </section>

  <section id="education" class="cv-section">
    <h2 class="cv-section-title">Education</h2>
    <div class="cv-timeline">
      {% for item in sections.Education %}
        <article class="cv-entry">
          <div>
            <h3>{{ item.degree }} · {{ item.area }}</h3>
            <p class="cv-entry-subtitle">{{ item.institution }}</p>
          </div>
          <div class="cv-entry-date">
            {% if item.start_date %}{{ item.start_date }} — {% endif %}{{ item.end_date }}
          </div>
          {% if item.highlights %}
            <ul class="cv-entry-highlights">
              {% for highlight in item.highlights %}
                <li>{{ highlight }}</li>
              {% endfor %}
            </ul>
          {% endif %}
        </article>
      {% endfor %}
    </div>
  </section>

  <section id="skills" class="cv-section">
    <h2 class="cv-section-title">Skills</h2>
    <div class="cv-skills-grid">
      {% for item in sections.Skills %}
        <article class="cv-skill">
          <h3>{{ item.label }}</h3>
          <p>{{ item.details }}</p>
        </article>
      {% endfor %}
    </div>
  </section>

  <section id="selected-projects" class="cv-section">
    <h2 class="cv-section-title">Selected Projects</h2>
    <div class="cv-project-grid">
      {% for item in sections.Projects %}
        <article class="cv-project">
          <h3>{{ item.name }}</h3>
          <p>{{ item.summary }}</p>
          {% if item.highlights %}
            <ul>
              {% for highlight in item.highlights %}
                <li>{{ highlight }}</li>
              {% endfor %}
            </ul>
          {% endif %}
        </article>
      {% endfor %}
    </div>
  </section>

  <section id="languages" class="cv-section">
    <h2 class="cv-section-title">Languages</h2>
    <div class="cv-languages">
      {% for item in sections.Languages %}
        <div class="cv-language">
          <strong>{{ item.label }}</strong>
          <span>{{ item.details }}</span>
        </div>
      {% endfor %}
    </div>
  </section>

  <section id="interests" class="cv-section">
    <h2 class="cv-section-title">Interests</h2>
    {% for item in sections.Interests %}
      <article class="cv-interest">
        <h3>{{ item.label }}</h3>
        <p>{{ item.details }}</p>
      </article>
    {% endfor %}
  </section>
</div>
