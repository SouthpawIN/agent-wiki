---
title: omnisenter-blog
updated: 2026-08-27
type: topic
repo: https://github.com/SouthpawIN/omnisenter-blog
status: dormant
tags: [repo]
---

# omnisenter-blog

> OmniSenter blog — a multi-stage agentic MoE with the Ohm self-evolution engine.

**[Open on GitHub](https://github.com/SouthpawIN/omnisenter-blog)** · DORMANT (since 2026-07-08) · last push 2026-07-08

## Facts
- **Language:** Python
- **Stars / forks:** 1 / 0
- **License:** MIT
- **Fork of:** original work
- **Created:** 2026-06-08 · **Last push:** 2026-07-08
- **Open issues:** 0
- **Status:** DORMANT (since 2026-07-08)

## From the README

# OmniSenter Blog

The public blog for the **OmniSenter** project — a multi-stage agentic
MoE with the Ohm self-evolution engine, built on Darwin Family
weight-space recombination.

**Live site:** https://southpawin.github.io/omnisenter-blog/

## What's here

- **13 blog posts** — the Omni Family catalog (naming, flagship, math,
  pipeline, concepts, integration, research)
- **Master wiki** — 11 concepts + 8 entity pages, in catalog order
- **9 hero images** — the cosmic-convergence concept art, the synth
  hero, the architecture diagram, etc.
- **Auto-deploy** to GitHub Pages on every push to `main`

## Local dev

```bash
pip install mkdocs mkdocs-material mkdocs-rss-plugin mkdocs-minify-plugin pymdown-extensions
mkdocs serve                  # live preview at http://127.0.0.1:8765
mkdocs build --strict         # build the static site to ./site
```

## X scheduler (posts one blog per week to @southpawin)

See [`scripts/post_x.py`](scripts/post_x.py). The script:

1. Reads a queue of 13 blog posts (in publishing order)
2. Formats each as a tweet (with cosmic hero image as media)
3. Posts via the [`xurl`](https://github.com/xdevplatform/xurl) CLI
4. Marks the post as posted, so it doesn't get re-posted

**First-time setup** (you, outside the agent — per the xurl skill's
safety rules):

```bash
# 1. Install xurl
curl -fsSL https://raw.githubusercontent.com/xdevplatform/xurl/main/install.sh | bash

# 2. Get an X developer app at https://developer.x.com/en/portal/dashboard
#    Set redirect URI to http://localhost:8080/callback

# 3. Register the app
xurl auth apps add omnisenter --client-id YOUR_CLIENT_ID --client-secret YOUR_CLIENT_SECRET
xurl auth oauth2 --app omnisenter YOUR_X_HANDLE
xurl auth default omnisenter

# 4. Verify
xurl whoami
```

**Posting manually:**

```bash
./scripts/post_x.py status      # show what's been posted
./scripts/post_x.py queue       # show the pending queue
./scripts/post_x.py post        # post the next item
```

**Posting on a schedule:**

Set up a cron job that runs `./scripts/post_x.py post` once a week (e.g.
Tuesday 9am). See `scripts/install_cron.sh` for the install command.

## Naming

The naming convention used throughout is defined in
[`docs/blog/the-omni-family.md`](docs/blog/the-omni-family.md):

- **Omni** = multimodal native
- **Senter** = Omni with the agentic core wired in
- **Ohm** = the self-evolution engine
- **Senter Ohm** = the flagship ~32A8B MoE (all three composited)
- **OmniSenter** = the project (umbrella), also the small Senter
  (`OmniSenter 12B`)

## Theme


*…truncated — full README at repo link*


## Archived
Archived 2026-09-02 — absorbed into [[topics/omnisenter-models/README|omnisenter-models]] by merge-topics.py v1.1.0. Nothing here was deleted or rewritten.
