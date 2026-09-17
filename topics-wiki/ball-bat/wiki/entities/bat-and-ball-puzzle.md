---
title: The Bat-and-Ball Puzzle
created: 2026-09-15
updated: 2026-09-15
type: entity
tags: [idea, question, pain]
sources: ["raw/inbox/2026-09-15.md"]
confidence: 0.95
---

# The Bat-and-Ball Puzzle

A classic cognitive-distraction puzzle that Chris posed twice verbatim on 2026-09-15 13:06: *"Solve: A bat and ball cost .10. The bat costs more than the ball. How much does the ball cost? Show your work."* ^[raw/inbox/2026-09-15.md]

The puzzle ships with a blank in the original — the bat's "more than" figure is missing. Hermes filled it with the canonical version: *"A bat and a ball cost $1.10. The bat costs $1.00 more than the ball."* ^[raw/inbox/2026-09-15.md]

## The trap
The intuitive answer is **10 cents** — but that only works if the bat is 90 cents, which contradicts "a dollar more." People reach it by subtracting `1.10 − 1.00 = 0.10` and stopping. ^[raw/inbox/2026-09-15.md]

## The correct answer
Let `x` = ball cost. Then bat = `x + 1.00`. So `x + (x + 1.00) = 1.10` → `2x = 0.10` → **x = 0.05**. The ball costs **5 cents** and the bat **$1.05**. ^[raw/inbox/2026-09-15.md]

## The general formula
If the missing number isn't $1.00, the ball is always `ball = (total − difference) / 2`. ^[raw/inbox/2026-09-15.md]

See also [[concepts/cognitive-distraction-trap|Cognitive Distraction Trap]] and [[comparisons/trap-answer-vs-correct|Trap Answer vs Correct Answer]].
