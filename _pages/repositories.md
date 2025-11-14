---
layout: page
permalink: /repositories/
title: repositories
description: Public GitHub repositories for the NTES organization.
nav: true
nav_order: 4
---

The NTES organization maintains public source code and applications on GitHub. View the full list of repositories at:

- https://github.com/OEHHA-NTES

The following repositories are highlighted here:

{% if site.data.repositories.github_repos %}
<ul>
  {% for repo in site.data.repositories.github_repos %}
    <li><a href="https://github.com/{{ repo }}" target="_blank">{{ repo }}</a></li>
  {% endfor %}
</ul>
{% else %}
No repositories configured. Update `_data/repositories.yml`.
{% endif %}
