# OEHHA-NTES GitHub Pages Site

Welcome to the official website for the **New Toxicology Evaluations Section (NTES)** at the Office of Environmental Health Hazard Assessment (OEHHA).

## About NTES

The New Toxicology Evaluations Section provides independent, science-based evaluations of the hazards and risks posed by chemicals in the environment and consumer products. NTES develops new and scientifically valid approaches for understanding chemical hazards and translates that science into robust evaluations used to establish guidance levels, inform regulatory priorities, and support emergency response actions.

Our work protects public health by providing state guidance for regulators, policymakers, and emergency responders on harmful chemicals that might otherwise remain unassessed.

## Site Contents

- **About** (`_pages/about.md`) — Overview of NTES mission, values, and organizational structure.
- **Applications** (`_pages/apps.md`) — Links, quick-start guides, and documentation for NTES-hosted R/Shiny tools:
  - OEHHA Data Explorer
  - OEHHA PFAS PK Modelling Application
  - Leggett+ Lead PBPK
- **Publications** — BibTeX bibliography in `_bibliography/papers.bib` (auto-rendered via Jekyll Scholar).
- **News** — Announcements and updates in `_news/`.
- **Blog** — Technical posts and project updates in `_posts/`.

## Technology

This site uses:

- **Jekyll** — Static site generator
- **al-folio theme** — Clean, responsive academic website template
- **GitHub Pages** — Hosting and deployment
- **Docker** (optional) — Local development

## Quick Start

### Prerequisites

- **Ruby** 3.0+ with Bundler
- **Jekyll** (installed via Bundler)
- **Pandoc** (for rendering code blocks)

### Local Development

1. **Clone the repository:**

   ```bash
   git clone https://github.com/OEHHA-NTES/OEHHA-NTES.github.io.git
   cd OEHHA-NTES.github.io
   ```

2. **Install dependencies:**

   ```bash
   bundle install
   ```

3. **Serve locally:**

   ```bash
   bundle exec jekyll serve --livereload
   ```

   Then visit `http://127.0.0.1:4000` in your browser.

4. **Preview changes** as you edit files (live-reload enabled).

### Using Docker (Optional)

If you prefer Docker:

```bash
docker-compose up
# Visit http://localhost:4000
```

See `INSTALL.md` for detailed setup instructions.

## Repository Structure

```
├── _config.yml              # Site configuration (title, description, theme settings)
├── _pages/                  # Page content (About, Apps, Publications, etc.)
│   ├── about.md            # NTES overview and mission
│   ├── apps.md             # NTES-hosted applications directory
│   ├── publications.md      # Auto-generated publications page
│   └── ...
├── _posts/                  # Blog posts and announcements
├── _news/                   # News items (homepage announcements)
├── _bibliography/           # BibTeX files (papers.bib)
├── assets/                  # Images, CSS, JavaScript
│   ├── img/                # Images (including ntes_logo.jpg)
│   ├── css/
│   ├── js/
│   └── json/
├── _includes/              # Reusable layout components
├── _layouts/               # Page templates
├── _sass/                  # SCSS stylesheets
├── Gemfile                 # Ruby dependencies
├── docker-compose.yml      # Docker configuration
├── SITE_README.md          # This file
└── ...
```

## Editing Content

### Add/Update a Page

1. Create or edit a `.md` file in `_pages/`.
2. Include YAML front matter (title, permalink, layout, etc.).
3. Write content in Markdown.
4. Save and refresh the local server to preview.

**Example:**

```yaml
---
layout: page
title: My Page
permalink: /my-page/
---
# My Page Content

This is a paragraph.
```

### Add a Blog Post

1. Create a `.md` file in `_posts/` named `YYYY-MM-DD-title.md`.
2. Include YAML front matter.
3. Write your post in Markdown.

### Update Publications

1. Edit `_bibliography/papers.bib` to add or modify BibTeX entries.
2. Add `selected: true` to any entries you want featured on the homepage.
3. Save; Jekyll will auto-render the publications page.

### Add News/Announcements

1. Create a `.md` file in `_news/` named `YYYY-MM-DD-announcement.md`.
2. Include YAML front matter.
3. Content will auto-appear on the homepage feed.

## Configuration

Key settings in `_config.yml`:

- `title` — Site title
- `description` — Meta description
- `keywords` — SEO keywords
- `url` — Base URL (for GitHub Pages)
- `footer_text` — Footer copyright/attribution
- `enable_darkmode` — Light/dark theme toggle
- `enable_math` — MathJax math rendering
- `blog_name` — Blog title
- `blog_description` — Blog subtitle

See `_config.yml` for all available options and the [al-folio documentation](https://github.com/alshedivat/al-folio) for theme-specific settings.

## Deployment

The site is automatically deployed to GitHub Pages when you push to the `main` branch. Builds are handled by GitHub Actions (see `.github/workflows/` if configured).

### Manual Deploy

If using local Jekyll:

```bash
bundle exec jekyll build
# Output goes to _site/
```

Then commit and push:

```bash
git add .
git commit -m "Update content"
git push origin main
```

## Contributing

We welcome contributions! Please:

1. **Fork** the repository or create a feature branch.
2. **Make changes** and test locally with `bundle exec jekyll serve`.
3. **Commit** with clear, descriptive messages.
4. **Submit a pull request** with a brief description of changes.

### Guidelines

- Follow Markdown style conventions (headers, lists, code blocks).
- Test local builds before submitting PRs.
- Include images in `assets/img/` and reference them with relative paths.
- Link to NTES apps and external resources using full URLs or Jekyll `{{ site.baseurl }}/` references.

## Issues & Support

- **Bug reports or suggestions?** Open a GitHub Issue with a clear title and description.
- **General questions?** Contact NTES at [NTES@oehha.ca.gov](mailto:NTES@oehha.ca.gov).

## License

This repository and its content are available under the terms specified in the `LICENSE` file.

## Additional Resources

- **OEHHA Main Website:** https://oehha.ca.gov
- **al-folio Theme:** https://github.com/alshedivat/al-folio
- **Jekyll Documentation:** https://jekyllrb.com/docs/
- **Markdown Guide:** https://www.markdownguide.org/

---

Last updated: November 2025
