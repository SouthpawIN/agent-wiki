---
type: loop
slug: deadline-watch
bot: ssi
schedule: "0 7 * * *"
state: spec
skill: notice-response
created: 2026-11-07
---

# deadline-watch

Daily 07:00. Nothing else in this bot matters if a deadline slips.

## Prompt

Read `cases/_deadlines.md`. Report rows due in 10, 5, or 1 days, and anything
overdue, one line each: child initials, program, what is due, days left, and the
single action Chris must take. If nothing is within 10 days, say "clear" and stop.
Never contact an agency. Never mark something sent that Chris has not sent.

## Stop condition

Read-only, and silent when clear. If `_deadlines.md` does not exist, that is the
finding: intake has not started.
