---
layout: page
title: Projects
permalink: /projects/
description: Selected research and technical work, with emphasis on validation, reproducibility, and practical results.
nav: true
nav_order: 3
display_categories: [research, machine-learning, data-science]
horizontal: true
---

<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category | replace: "-", " " | capitalize }}</h2>
  </a>
  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% endfor %}
{% endif %}
</div>
