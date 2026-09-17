---
title: southpawin.github.io
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/southpawin.github.io
status: dormant
tags: [repo]
---

# southpawin.github.io

> Southpaw personal site — TOWARDS SELF-IMPROVEMENT. Blog, projects, models, the pet.

**[Open on GitHub](https://github.com/SouthpawIN/southpawin.github.io)** · DORMANT (since 2026-07-08) · last push 2026-07-08

## Facts
- **Language:** Python
- **Stars / forks:** 1 / 0
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-06-08 · **Last push:** 2026-07-08
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-08)

## From the README

# sovthpaw — Personal Site

This repo is the front door for everything I build. It's deployed to
**https://southpawin.github.io/** via GitHub Pages.

## What's here

- **Blog** — long-form posts on the OmniSenter pipeline, the pet, the radio
- **Projects** — every repo, with descriptions and links
- **Models** — the curated catalog
- **Wiki** — the reference: every concept and entity, cross-linked

## How it works

- Source: Markdown in `docs/`
- Theme: MkDocs Material with custom Nous cosmic-variant CSS
- Build: GitHub Actions → `mkdocs build` → deploy to Pages
- Branch: `main`

## Local dev

```bash
pip install mkdocs mkdocs-material mkdocs-rss-plugin mkdocs-minify-plugin pymdown-extensions
mkdocs serve
```

Then visit `http://127.0.0.1:8765/`.

## Adding a post

1. Add a new `.md` file under `docs/blog/`
2. Add an entry to `docs/blog/CATALOG.md` if you want it in the master index
3. Push to `main`
4. The site redeploys automatically

## See also

- [nous-girl-agent](https://github.com/SouthpawIN/nous-girl-agent) — the pet
- [evolutionary-training](https://github.com/SouthpawIN/evolutionary-training) — the training pipeline
- [evolutionary-radio](https://github.com/SouthpawIN/evolutionary-radio) — the radio
- [omnisenter-blog](https://github.com/SouthpawIN/omnisenter-blog) — legacy blog repo (content moved here)


## Archived
Archived 2026-09-02 — absorbed into [[topics-wiki/youtube/README|youtube]] by merge-topics.py v1.1.0. Nothing here was deleted or rewritten.
