---
type: loop
slug: weekly-cut
bot: youtube
schedule: "0 10 * * 0"
state: spec
skill: clip-assembly
created: 2026-11-07
---

# weekly-cut

Sunday 10:00. Pick the best unrendered session, assemble and package one video.

## Prompt

Choose the highest-ranked unrendered segment set from the past 7 days. Run
`clip-assembly`, then `package-and-chapters`. Write `upload.md` next to the
render and inject one line: video length, title, and that it awaits approval.
Never upload.

## Stop condition

One video per week maximum. If the best segment ranks below 0.45, produce
nothing and say the week was thin.
