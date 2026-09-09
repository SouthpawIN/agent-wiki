import json, datetime, collections, sys

path = "/Users/sovthpaw/.hermes/senter-bridge/events.jsonl"
events = []
with open(path) as f:
    for line in f:
        line = line.strip()
        if line:
            try:
                events.append(json.loads(line))
            except Exception:
                pass

def ts2str(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

print("total events:", len(events))
print("first:", ts2str(events[0]["ts"]), "last:", ts2str(events[-1]["ts"]))

kinds = collections.Counter(e.get("kind") for e in events)
print("\nkinds:", dict(kinds))

bots = collections.Counter(e.get("bot") for e in events)
print("\nbots:", dict(bots))

# distinct keys across events
keys = collections.Counter()
for e in events:
    for k in e.keys():
        keys[k] += 1
print("\nkeys:", dict(keys))

# show a sample of each kind
seen = set()
for e in events:
    k = e.get("kind")
    if k not in seen:
        seen.add(k)
        print("\n--- sample kind:", k, "---")
        print(json.dumps(e, indent=1)[:800])
