---
title: Why does `hdiutil restore` fail here?
created: 2026-09-15
updated: 2026-09-15
type: query
tags: [question, tool, pain]
sources: [raw/inbox/2026-09-12.md, raw/inbox/2026-09-15.md]
confidence: medium
---

# Why does `hdiutil restore` fail here?

**Question:** Chris ran `hdiutil restore -nomount ~/tmp/omarchy/omarchy-4.0.3.iso /dev/rdisk4` and got `restore: verb not recognized` (exit 1), even though the man page documents `restore`. Why? [^raw1]

## What the raw log shows
- `hdiutil restore -h` and the full command both return `verb not recognized`. [^raw1]
- The verb list it prints does **not** include `restore`. [^raw1]
- The system man page **does** document `restore` (in the CD-restore section). [^raw1]

## Hypothesis (unverified)
A **man-page/binary mismatch** on this macOS build (26.6.2, Build 25G83): the man page ships the old verb list while the installed `hdiutil` binary no longer recognizes `restore`. This would be a per-build regression, not a user error.

## Open question
Is `restore` gone from this build, or is it a PATH/shim issue? Worth a direct check against `which hdiutil` and a rebuild/ reinstall note. [^raw1]

## Related
- [[topics/restore-hdiutil/wiki/entities/hdiutil|hdiutil / restore verb]] — the failure itself.
- [[topics/restore-hdiutil/wiki/comparisons/flash-methods|Flash methods]] — fallbacks.

---
[^raw1]: [raw/inbox/2026-09-12.md](raw/inbox/2026-09-12.md); verified live 2026-09-15.
