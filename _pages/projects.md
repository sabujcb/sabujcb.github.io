---
layout: page
title: Projects
permalink: /projects/
description: Selected research and technical case studies in computational biology, machine learning, forecasting, computer vision, and signal processing.
nav: true
nav_order: 3
---

<style>
  .portfolio-projects {
    --project-radius: 1.1rem;
    --project-border: var(--global-divider-color, #d8dee4);
    --project-surface: var(--global-card-bg-color, var(--global-bg-color, #fff));
  }

  .projects-hero {
    position: relative;
    overflow: hidden;
    margin: 0 0 2.5rem;
    padding: clamp(1.5rem, 4vw, 3rem);
    border: 1px solid var(--project-border);
    border-radius: calc(var(--project-radius) + 0.25rem);
    background:
      radial-gradient(circle at top right, rgba(111, 66, 193, 0.16), transparent 40%),
      linear-gradient(135deg, rgba(0, 123, 255, 0.12), rgba(32, 201, 151, 0.08));
  }

  .projects-eyebrow {
    margin-bottom: 0.65rem;
    color: var(--global-theme-color);
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
  }

  .projects-hero h2 {
    max-width: 18ch;
    margin-bottom: 0.8rem;
    font-size: clamp(1.8rem, 4vw, 3rem);
    line-height: 1.08;
  }

  .projects-intro {
    max-width: 68ch;
    margin-bottom: 1.4rem;
    color: var(--global-text-color);
    font-size: 1.04rem;
    line-height: 1.7;
  }

  .projects-summary {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 0.75rem;
    max-width: 46rem;
  }

  .projects-summary-item {
    padding: 0.85rem 1rem;
    border: 1px solid var(--project-border);
    border-radius: 0.8rem;
    background: var(--project-surface);
  }

  .projects-summary-item strong {
    display: block;
    color: var(--global-theme-color);
    font-size: 1.35rem;
    line-height: 1.1;
  }

  .projects-summary-item span {
    display: block;
    margin-top: 0.3rem;
    font-size: 0.78rem;
    line-height: 1.35;
  }

  .projects-jump-links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.55rem;
    margin: 0 0 2.6rem;
  }

  .projects-jump-links a,
  .project-tag {
    border: 1px solid var(--project-border);
    border-radius: 999px;
    background: var(--project-surface);
  }

  .projects-jump-links a {
    padding: 0.48rem 0.85rem;
    color: var(--global-text-color);
    font-size: 0.86rem;
    font-weight: 600;
    text-decoration: none;
  }

  .projects-jump-links a:hover {
    border-color: var(--global-theme-color);
    color: var(--global-theme-color);
  }

  .project-section {
    margin: 0 0 3rem;
    scroll-margin-top: 5rem;
  }

  .project-section-heading {
    display: flex;
    align-items: end;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 1rem;
    padding-bottom: 0.7rem;
    border-bottom: 1px solid var(--project-border);
  }

  .project-section-heading h2 {
    margin: 0;
    font-size: clamp(1.35rem, 3vw, 1.85rem);
  }

  .project-section-heading span {
    color: var(--global-text-color-light, #6c757d);
    font-size: 0.82rem;
  }

  .project-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1.1rem;
  }

  .project-grid > .project-card:only-child {
    grid-column: 1 / -1;
  }

  .project-card {
    display: flex;
    flex-direction: column;
    min-width: 0;
    padding: 1.35rem;
    border: 1px solid var(--project-border);
    border-radius: var(--project-radius);
    background: var(--project-surface);
    box-shadow: 0 0.35rem 1.25rem rgba(0, 0, 0, 0.045);
    transition:
      transform 160ms ease,
      border-color 160ms ease,
      box-shadow 160ms ease;
  }

  .project-card:hover {
    transform: translateY(-3px);
    border-color: var(--global-theme-color);
    box-shadow: 0 0.75rem 1.75rem rgba(0, 0, 0, 0.08);
  }

  .project-card-topline {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.75rem;
    margin-bottom: 0.9rem;
  }

  .project-type,
  .project-status {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.045em;
    text-transform: uppercase;
  }

  .project-type {
    color: var(--global-theme-color);
  }

  .project-status {
    color: var(--global-text-color-light, #6c757d);
  }

  .project-card h3 {
    margin: 0 0 0.65rem;
    font-size: 1.28rem;
    line-height: 1.3;
  }

  .project-card h3 a {
    color: var(--global-text-color);
    text-decoration: none;
  }

  .project-card h3 a:hover {
    color: var(--global-theme-color);
  }

  .project-description {
    margin-bottom: 1rem;
    color: var(--global-text-color-light, #6c757d);
    line-height: 1.6;
  }

  .project-metric {
    display: grid;
    grid-template-columns: auto 1fr;
    align-items: center;
    gap: 0.8rem;
    margin-bottom: 1rem;
    padding: 0.85rem;
    border-left: 3px solid var(--global-theme-color);
    border-radius: 0.65rem;
    background: rgba(0, 123, 255, 0.065);
  }

  .project-metric strong {
    color: var(--global-theme-color);
    font-size: 1.35rem;
    line-height: 1;
  }

  .project-metric span {
    font-size: 0.78rem;
    line-height: 1.35;
  }

  .project-highlights {
    margin: 0 0 1rem;
    padding-left: 1.15rem;
    font-size: 0.91rem;
    line-height: 1.55;
  }

  .project-highlights li + li {
    margin-top: 0.35rem;
  }

  .project-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin: auto 0 1rem;
  }

  .project-tag {
    padding: 0.28rem 0.58rem;
    font-size: 0.72rem;
    line-height: 1.2;
  }

  .project-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 0.55rem;
    padding-top: 0.95rem;
    border-top: 1px solid var(--project-border);
  }

  .project-action {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.48rem 0.7rem;
    border: 1px solid var(--project-border);
    border-radius: 0.55rem;
    color: var(--global-text-color);
    font-size: 0.79rem;
    font-weight: 600;
    text-decoration: none;
  }

  .project-action-primary {
    border-color: var(--global-theme-color);
    background: var(--global-theme-color);
    color: #fff;
  }

  .project-action:hover {
    border-color: var(--global-theme-color);
    color: var(--global-theme-color);
  }

  .project-action-primary:hover {
    color: #fff;
    filter: brightness(0.92);
  }

  .project-principles {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 0.8rem;
    margin-top: 3.2rem;
    padding-top: 2rem;
    border-top: 1px solid var(--project-border);
  }

  .project-principle {
    padding: 1rem;
    border-radius: 0.8rem;
    background: rgba(0, 123, 255, 0.055);
  }

  .project-principle h3 {
    margin-bottom: 0.45rem;
    font-size: 1rem;
  }

  .project-principle p {
    margin: 0;
    color: var(--global-text-color-light, #6c757d);
    font-size: 0.85rem;
    line-height: 1.5;
  }

  .projects-resource-note {
    margin-top: 1.2rem;
    color: var(--global-text-color-light, #6c757d);
    font-size: 0.8rem;
  }

  @media (max-width: 767px) {
    .projects-summary,
    .project-grid,
    .project-principles {
      grid-template-columns: 1fr;
    }

    .project-section-heading {
      align-items: start;
      flex-direction: column;
      gap: 0.25rem;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .project-card {
      transition: none;
    }

    .project-card:hover {
      transform: none;
    }
  }
</style>

<div class="portfolio-projects">
  <section class="projects-hero" aria-labelledby="projects-introduction">
    <div class="projects-eyebrow">Selected work</div>
    <h2 id="projects-introduction">Research questions turned into reproducible evidence.</h2>
    <p class="projects-intro">
      My work spans computational biology, applied machine learning, forecasting, computer vision, and signal
      processing. Each case study emphasizes a clear validation question, transparent metrics, and limitations that
      matter beyond a single model score.
    </p>
    <div class="projects-summary" aria-label="Portfolio summary">
      <div class="projects-summary-item"><strong>6</strong><span>documented case studies</span></div>
      <div class="projects-summary-item"><strong>3</strong><span>technical focus areas</span></div>
      <div class="projects-summary-item"><strong>R + Python</strong><span>cross-language research workflows</span></div>
    </div>
  </section>

  <nav class="projects-jump-links" aria-label="Project categories">
    <a href="#research">Research &amp; computational biology</a>
    <a href="#machine-learning">Machine learning</a>
    <a href="#data-science">Data science &amp; signal processing</a>
  </nav>

{% assign category_keys = "research,machine-learning,data-science" | split: "," %}
{% assign category_titles = "Research & Computational Biology,Machine Learning,Data Science & Signal Processing" | split: "," %}
{% assign category_descriptions = "Multi-omics integration and group-aware scientific modeling,Generalization-focused predictive and computer-vision systems,Forecasting and physiological signal analysis" | split: "," %}

{% for category_key in category_keys %}
{% assign category_index = forloop.index0 %}
{% assign category_projects = site.projects | where: "category", category_key | sort: "featured_order" %}

<section id="{{ category_key }}" class="project-section" aria-labelledby="{{ category_key }}-heading">
<header class="project-section-heading">
<h2 id="{{ category_key }}-heading">{{ category_titles[category_index] }}</h2>
<span>{{ category_descriptions[category_index] }}</span>
</header>

      <div class="project-grid">
        {% for project in category_projects %}
          <article class="project-card">
            <div class="project-card-topline">
              <span class="project-type">{{ project.project_type }}</span>
              <span class="project-status">{{ project.status }}</span>
            </div>

            <h3><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
            <p class="project-description">{{ project.description }}</p>

            {% if project.metric_value %}
              <div class="project-metric">
                <strong>{{ project.metric_value }}</strong>
                <span>{{ project.metric_label }}</span>
              </div>
            {% endif %}

            {% if project.card_highlights %}
              <ul class="project-highlights">
                {% for highlight in project.card_highlights %}
                  <li>{{ highlight }}</li>
                {% endfor %}
              </ul>
            {% endif %}

            {% if project.tools %}
              <div class="project-tags" aria-label="Tools used">
                {% for tool in project.tools %}
                  <span class="project-tag">{{ tool }}</span>
                {% endfor %}
              </div>
            {% endif %}

            <div class="project-actions">
              <a class="project-action project-action-primary" href="{{ project.url | relative_url }}">
                Case study <span aria-hidden="true">→</span>
              </a>
              {% for resource in project.resources %}
                <a class="project-action" href="{{ resource.url }}" target="_blank" rel="noopener noreferrer">
                  {{ resource.label }} <span aria-hidden="true">↗</span>
                </a>
              {% endfor %}
            </div>
          </article>
        {% endfor %}
      </div>
    </section>

{% endfor %}

  <section class="project-principles" aria-label="Working principles">
    <div class="project-principle">
      <h3>Validation matches the question</h3>
      <p>Temporal, participant-aware, and group-aware splits are chosen to reflect the intended use of a model.</p>
    </div>
    <div class="project-principle">
      <h3>Reproducibility is engineered</h3>
      <p>Preprocessing, seeds, configurations, software versions, and intermediate outputs are made explicit.</p>
    </div>
    <div class="project-principle">
      <h3>Limitations stay visible</h3>
      <p>Results are presented with their dataset scope, uncertainty, and external-validation requirements.</p>
    </div>
  </section>

  <p class="projects-resource-note">
    Public code links are shown only where a matching repository is available. Other links lead to authoritative method
    documentation used to contextualize the case study.
  </p>
</div>
