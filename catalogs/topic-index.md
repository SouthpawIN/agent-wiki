---
title: Topic Index
created: 2026-07-07
updated: 2026-07-07
type: catalog
tags: [goop, topics]
---

# Topic Index

Every topic = one user interest with its own full GOOP stack.

| Topic | Status | Agents | Skills | Loops |
|---|---|---|---|---|
| (no topics yet — chat with Nous Girl to create them) | | | | |

## Topic Structure

```
topics/<topic>/
├── README.md           ← human dashboard
├── .system/            ← machine internals
│   ├── continuity.md
│   ├── injections.md
│   └── queue.md
├── skills/
├── agents/
└── loops/
```

Each topic is self-contained. You can archive a topic by moving its directory to `_archive/`.
