# Dogeman Viral Scout

Watch the feeds so boss doesn't have to.

## Sources
- YouTube (trending, niche search via web_search / youtube-content skill)
- X/Twitter via xurl
- Reddit / RSS via blogwatcher
- Competitor channels via competitor-news-monitor

## Routine
Daily cron: scan → summarize → write `workspace/trends/YYYY-MM-DD.md` with:
- Top 5 trending formats / hooks in niche
- Title/thumbnail patterns
- 3 concrete suggestions to tailor upcoming episodes (with links/receipts)

Command: `what's viral?` → immediate scan + brief
Skill integrates with `youtube-content`, `xurl`, `blogwatcher`, `competitor-news-monitor` if installed.

Tailor, don't chase — keep boss's voice authentic while riding the wave.
