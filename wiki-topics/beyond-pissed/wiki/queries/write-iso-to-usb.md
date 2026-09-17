---
title: Write Oh My Archi ISO to USB Without /dev/rdisk4 Permission Error
created: 2026-09-12
updated: 2026-09-12
type: query
tags: [question, pain, infra]
sources: [raw/inbox/2026-09-12.md]
confidence: medium
---

# Write Oh My Archi ISO to USB Without /dev/rdisk4 Permission Error

When flashing the Oh My Archi ISO to the USB stick, the raw-device write failed with a permission error. The open question is how to correctly flash the ISO on macOS.

> Command: # Check if we can write to raw device without sudo (operator group should work)
> ls -la /dev/rdisk4 2>/dev/null; echo "---"; # Try writing via Python (bypasses SIP restrictions on raw devices)
> Traceback ... PermissionError: [Errno 1] Operation not permitted: '/dev/rdisk4' ^[raw/inbox/2026-09-12.md]

Hermes's approach — a raw Python `open('/dev/rdisk4','wb')` write "to bypass SIP restrictions" — still raised `PermissionError`, meaning the write needs elevated privilege (sudo), not just a non-SIP code path.

See [[wiki-topics/beyond-pissed/wiki/entities/oh-my-archi|Oh My Archi]] and [[wiki-topics/beyond-pissed/wiki/concepts/beyond-pissed|Beyond Pissed]].

See also: [[wiki-topics/beyond-pissed/wiki/decisions/multi-project-order-of-operations|Multi-Project Order of Operations]]
