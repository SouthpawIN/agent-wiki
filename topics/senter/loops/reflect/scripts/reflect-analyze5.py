import os, json
from datetime import datetime, timezone, timedelta

CDT = timezone(timedelta(hours=-5))
cutoff = datetime(2026, 9, 4, 4, 3, 5, tzinfo=CDT).timestamp()
end = datetime(2026, 9, 4, 6, 0, 30, tzinfo=CDT).timestamp()

def mtime_ts(p):
    try:
        return os.path.getmtime(p)
    except OSError:
        return None

def show(p):
    t = mtime_ts(p)
    if t is None:
        print(f"MISSING  {p}")
        return
    s = datetime.fromtimestamp(t, CDT).strftime("%Y-%m-%d %H:%M:%S")
    flag = ""
    if t >= cutoff and t < end:
        flag = "  <-- CHANGED THIS WINDOW"
    print(f"{s}  {p}{flag}")

print("=== Key files mtimes (window 04:03:05 -> 06:00:30 CDT) ===")
show("/Users/sovthpaw/Documents/Projects/Projects/Ideas.md")
show("/Users/sovthpaw/Documents/Projects/Projects/topics/klerik/.system/session.md")
show("/Users/sovthpaw/Documents/Projects/Projects/topics/klerik/.system/queue.md")
show("/Users/sovthpaw/Documents/Projects/Projects/topics/senter/.system/session.md")
show("/Users/sovthpaw/Documents/Projects/Projects/topics/senter/.system/queue.md")
show("/Users/sovthpaw/Documents/Projects/Projects/topics/senter/process/lessons.md")
show("/Users/sovthpaw/Documents/Projects/Projects/topics/senter/loops/reflect/2026-09-04-17.md")

print("\n=== any queue.md / session.md changed this window ===")
root = "/Users/sovthpaw/Documents/Projects/Projects/topics"
for dirpath, dirs, files in os.walk(root):
    dirs[:] = [d for d in dirs if d not in ('_archive', '.git', 'node_modules')]
    for fn in files:
        if fn in ("queue.md", "session.md"):
            p = os.path.join(dirpath, fn)
            t = mtime_ts(p)
            if t is not None and t >= cutoff and t < end:
                s = datetime.fromtimestamp(t, CDT).strftime("%H:%M:%S")
                print(f"{s}  {p}")
