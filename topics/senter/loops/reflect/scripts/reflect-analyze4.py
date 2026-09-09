import json
from datetime import datetime, timezone, timedelta

CDT = timezone(timedelta(hours=-5))
cutoff = datetime(2026, 9, 4, 5, 55, 0, tzinfo=CDT).timestamp()

path = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
with open(path) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except Exception:
            continue
        t = e.get("ts", 0)
        if t >= cutoff:
            ts = datetime.fromtimestamp(t, CDT).strftime("%H:%M:%S.%f")[:-3]
            bot = e.get("bot")
            kind = e.get("kind")
            tool = e.get("tool","")
            phase = e.get("phase","")
            summ = str(e.get("summary",""))[:130]
            extra = ""
            if e.get("argv"):
                extra = " argv=" + str(e.get("argv"))[:120]
            if kind == "turn" and "cron_" in str(summ):
                extra = " CRON=" + str(summ)[:80]
            print(f"{ts} | {bot} | {kind} | {tool} | {phase} | {summ}{extra}")
