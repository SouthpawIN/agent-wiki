---
name: productivity-office-tools
description: "Productivity & office tools: Airtable, Google Workspace, Notion, PowerPoint, Maps, nano-pdf, Obsidian, Teams meetings, Email (Himalaya)."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: ["productivity", "office", "airtable", "google-workspace", "notion", "powerpoint", "maps", "obsidian", "teams", "email", "pdf"]
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [productivity, office, airtable, google-workspace, notion, powerpoint, maps, obsidian, teams, email, pdf]
    category: productivity-office
    related_skills: [social-media-communication, smart-home-iot, creative-design-systems]
---

# Productivity & Office Tools

Unified skill for office productivity, document management, and workplace automation. Covers nine complementary tools:

1. **Airtable** — REST API via curl: bases, tables, records CRUD, filters, upserts
2. **Google Workspace** — Gmail, Calendar, Drive, Docs, Sheets via gws CLI or Python
3. **Notion** — API + ntn CLI: pages, databases, markdown, Workers
4. **PowerPoint** — Create, read, edit .pptx decks, slides, notes, templates
5. **Maps** — Geocode, POIs, routes, timezones via OpenStreetMap/OSRM
6. **nano-pdf** — Edit PDF text/typos/titles via nano-pdf CLI (NL prompts)
4. **Obsidian** — Read, search, create, edit notes in Obsidian vault
5. **Teams Meeting Pipeline** — Operate Teams meeting summary pipeline via Hermes CLI
6. **Himalaya** — IMAP/SMTP email from terminal (cli email client)

Load this skill when the user wants to:
- Manage Airtable bases and records
- Work with Google Workspace (email, calendar, drive, docs, sheets)
- Interact with Notion (pages, databases, markdown)
- Create or edit PowerPoint presentations
- Geocode addresses, find nearby places, get directions
- Edit PDF text content
- Manage Obsidian vault notes
- Process Teams meeting summaries
- Send/receive email via IMAP/SMTP

---

## Quick Decision Guide

| Goal | Use This Section |
|------|------------------|
| Airtable database operations | [Airtable](#airtable) |
| Google Workspace (Gmail, Calendar, Drive, Docs, Sheets) | [Google Workspace](#google-workspace) |
| Notion pages, databases, markdown | [Notion](#notion) |
| Create/edit PowerPoint presentations | [PowerPoint](#powerpoint) |
| Geocoding, routing, nearby places | [Maps](#maps) |
| Edit PDF text/typos/titles | [nano-pdf](#nano-pdf) |
| Obsidian vault management | [Obsidian](#obsidian) |
| Teams meeting summaries | [Teams Meeting Pipeline](#teams-meeting-pipeline) |
| Terminal email (IMAP/SMTP) | [Himalaya Email](#himalaya-email) |

---

## Airtable

> **Source:** Absorbed from `airtable` skill. Airtable REST API via curl. Records CRUD, filters, upserts.

### Prerequisites
1. Create **Personal Access Token (PAT)** at https://airtable.com/create/tokens (starts with `pat...`)
2. Grant scopes: `data.records:read`, `data.records:write`, `schema.bases:read`
3. Add target bases to token's **Access** list
4. Store in `~/.hermes/.env`: `AIRTABLE_API_KEY=pat_your_token_here`

### API Basics
- Endpoint: `https://api.airtable.com/v0`
- Auth: `Authorization: Bearer $AIRTABLE_API_KEY`
- Rate limit: 5 requests/sec/base
- IDs: bases `app...`, tables `tbl...`, records `rec...`, fields `fld...`

### Common Queries
```bash
# List bases
curl -s "https://api.airtable.com/v0/meta/bases" -H "Authorization: Bearer $AIRTABLE_API_KEY"

# List tables + schema
curl -s "https://api.airtable.com/v0/meta/bases/$BASE_ID/tables" -H "Authorization: Bearer $AIRTABLE_API_KEY"

# List records (with filter)
FORMULA="{Status}='Todo'"
ENC=$(python3 -c 'import sys, urllib.parse; print(urllib.parse.quote(sys.argv[1], safe=""))' "$FORMULA")
curl -s "https://api.airtable.com/v0/$BASE_ID/$TABLE?filterByFormula=$ENC&maxRecords=20" -H "Authorization: Bearer $AIRTABLE_API_KEY"
```

### Common Mutations
```bash
# Create record
curl -s -X POST "https://api.airtable.com/v0/$BASE_ID/$TABLE" -H "Authorization: Bearer $AIRTABLE_API_KEY" -H "Content-Type: application/json" -d '{"fields":{"Name":"New task","Status":"Todo"}}'

# Batch create (up to 10)
curl -s -X POST "https://api.airtable.com/v0/$BASE_ID/$TABLE" -H "Authorization: Bearer $AIRTABLE_API_KEY" -H "Content-Type: application/json" -d '{"typecast":true,"records":[{"fields":{"Name":"A"}},{"fields":{"Name":"B"}}]}'

# Update record (PATCH)
curl -s -X PATCH "https://api.airtable.com/v0/$BASE_ID/$TABLE/$RECORD_ID" -H "Authorization: Bearer $AIRTABLE_API_KEY" -H "Content-Type: application/json" -d '{"fields":{"Status":"Done"}}'

# Upsert by merge field
curl -s -X PATCH "https://api.airtable.com/v0/$BASE_ID/$TABLE" -H "Authorization: Bearer $AIRTABLE_API_KEY" -H "Content-Type: application/json" -d '{"performUpsert":{"fieldsToMergeOn":["Email"]},"records":[{"fields":{"Email":"user@example.com","Status":"Active"}}]}'
```

### Pitfalls
- **filterByFormula MUST be URL-encoded** — use Python `urllib.parse.quote`
- **Empty fields omitted from responses** — check schema first
- **PATCH merges, PUT replaces** — default to PATCH
- **Single-select options must exist** — use `typecast: true` to auto-create
- **Per-base token scoping** — 403 on one base = token lacks access to that base
- **Rate limits per base** — 5 req/sec, monitor `Retry-After` on 429

---

## Google Workspace

> **Source:** Absorbed from `google-workspace` skill. Gmail, Calendar, Drive, Docs, Sheets via gws CLI or Python.

### Prerequisites
```bash
# Credentials in ~/.hermes/
google_token.json       # OAuth2 token (created by setup)
google_client_secret.json  # OAuth2 client credentials (from Google Cloud Console)
```

### First-Time Setup
```bash
GSETUP="python ${HERMES_HOME:-$HOME/.hermes}/skills/productivity/google-workspace/scripts/setup.py"

# Check if authenticated
$GSETUP --check

# 1. Ask user: Email only? → Use Himalaya instead (App Password, no Cloud project)
# 2. Ask user: Advanced Protection? → Admin must allowlist OAuth client
# 3. Create OAuth client: Google Cloud Console → APIs → Credentials → Desktop app
# 4. Enable APIs: Gmail, Calendar, Drive, Sheets, Docs, People
# 5. Download client_secret.json, run:
$GSETUP --client-secret /path/to/client_secret.json

# 6. Get auth URL (choose services)
$GSETUP --auth-url --services email,calendar --format json
# User visits URL, copies redirected URL

# 7. Exchange code
$GSETUP --auth-code "THE_URL_OR_CODE" --format json

# 8. Verify
$GSETUP --check  # Should print "AUTHENTICATED"
```

### Usage (via API script)
```bash
GAPI="python ${HERMES_HOME:-$HOME/.hermes}/skills/productivity/google-workspace/scripts/google_api.py"

# Gmail
$GAPI gmail search "is:unread" --max 10
$GAPI gmail get MESSAGE_ID
$GAPI gmail send --to user@example.com --subject "Hello" --body "Message"
$GAPI gmail reply MESSAGE_ID --body "Thanks"

# Calendar
$GAPI calendar list --start 2026-03-01T00:00:00Z --end 2026-03-07T23:59:59Z
$GAPI calendar create --summary "Standup" --start "2026-03-01T10:00:00-06:00" --end "2026-03-01T10:30:00-06:00"

# Drive
$GAPI drive search "quarterly report" --max 10
$GAPI drive upload /path/to/report.pdf
$GAPI drive download FILE_ID --output ~/doc.pdf
$GAPI drive share FILE_ID --email alice@example.com --role reader

# Sheets
$GAPI sheets create --title "Budget"
$GAPI sheets get SHEET_ID "Sheet1!A1:D10"
$GAPI sheets update SHEET_ID "Sheet1!A1:B2" --values '[["Name","Score"],["Alice","95"]]'
$GAPI sheets append SHEET_ID "Sheet1!A:C" --values '[["new","row","data"]]'

# Docs
$GAPI docs get DOC_ID
$GAPI docs create --title "Meeting Notes"
$GAPI docs append DOC_ID --text "Additional content"
```

### Rules
1. **Confirm before writes** — show recipients, file IDs, content, share role
2. **Check auth first** — `$GSETUP --check`
3. **Use timezone in ISO 8601** — `2026-03-01T10:00:00-06:00` or `Z`
4. **Respect rate limits** — batch reads when possible

---

## Notion

> **Source:** Absorbed from `notion` skill. Notion API + ntn CLI: pages, databases, markdown, Workers.

### Setup
```bash
# 1. Create integration at https://notion.so/my-integrations
# 2. Copy API key (starts with ntn_ or secret_)
# 3. Store in ~/.hermes/.env: NOTION_API_KEY=ntn_your_key_here
# 4. SHARE target pages/databases with integration in Notion UI

# macOS/Linux: Install ntn CLI
curl -fsSL https://ntn.dev | bash
export NOTION_API_TOKEN=$NOTION_API_KEY
export NOTION_KEYRING=0
```

### Common Operations (ntn CLI preferred on macOS/Linux)

#### Pages & Markdown
```bash
# Search
ntn api v1/search query="page title"

# Read page as markdown (agent-friendly)
ntn api v1/pages/{page_id}/markdown

# Create page from markdown
ntn api v1/pages parent[page_id]=xxx properties[title][0][text][content]="Notes" markdown="# Agenda\n\n- Item 1"

# Patch page with markdown
ntn api v1/pages/{page_id}/markdown -X PATCH markdown="## Update\n\nDone."
```

#### Databases (Data Sources)
```bash
# Query database
ntn api v1/data_sources/{data_source_id}/query -X POST filter[property]=Status filter[select][equals]=Active

# Complex query (pipe JSON)
echo '{"filter":{"property":"Status","select":{"equals":"Active"}},"sorts":[{"property":"Date","direction":"descending"}]}' | ntn api v1/data_sources/{id}/query -X POST --json -

# Create database item
ntn api v1/pages parent[database_id]=xxx properties[Name][title][0][text][content]="New Item" properties[Status][select][name]=Todo
```

#### File Uploads (one-liner)
```bash
ntn files create < photo.png
ntn files create --external-url https://example.com/photo.png
```

### HTTP + curl (cross-platform, default on Windows)
```bash
# All requests need:
# -H "Authorization: Bearer $NOTION_API_KEY"
# -H "Notion-Version: 2025-09-03"
# -H "Content-Type: application/json"

# Read page as markdown
curl -s "https://api.notion.com/v1/pages/{page_id}/markdown" -H "Authorization: Bearer $NOTION_API_KEY" -H "Notion-Version: 2025-09-03"

# Create page from markdown
curl -s -X POST "https://api.notion.com/v1/pages" -H "Authorization: Bearer $NOTION_API_KEY" -H "Notion-Version: 2025-09-03" -H "Content-Type: application/json" -d '{"parent":{"page_id":"xxx"},"properties":{"title":[{"text":{"content":"Notes"}}]},"markdown":"# Agenda\n\n- Item 1"}'
```

### Notion Workers (requires Business/Enterprise, macOS/Linux)
```bash
ntn workers new my-worker
# Edit src/index.ts
ntn workers deploy --name my-worker
```

### Common Property Types
- Title: `{"title":[{"text":{"content":"..."}}]}`
- Select: `{"select":{"name":"Option"}}`
- Multi-select: `{"multi_select":[{"name":"A"},{"name":"B"}]}`
- Date: `{"date":{"start":"2026-01-15","end":"2026-01-16"}}`
- Checkbox: `{"checkbox":true}`
- Number: `{"number":42}`

---

## PowerPoint

> **Source:** Absorbed from `powerpoint` skill. Create, read, edit .pptx decks, slides, notes, templates.

### Quick Reference
| Task | Tool |
|------|------|
| Read/analyze content | `python -m markitdown presentation.pptx` |
| Edit/create from template | `scripts/editing.py` |
| Create from scratch | `pptxgenjs` (npm) |

### Reading Content
```bash
# Text extraction
python -m markitdown presentation.pptx

# Visual overview (thumbnails)
python scripts/thumbnail.py presentation.pptx

# Raw XML
python scripts/office/unpack.py presentation.pptx unpacked/
```

### Creating/Editing
1. **From template**: `scripts/clean.py` → `scripts/add_slide.py` → manipulate → `scripts/clean.py` → pack
2. **From scratch**: `npm install -g pptxgenjs` → use pptxgenjs API

### Design Principles (Anti-Slop)
- **Bold, content-informed color palette** — one dominant color (60-70%), 1-2 supporting, 1 sharp accent
- **Dark/light contrast** — dark for title/conclusion, light for content (sandwich)
- **Visual motif** — ONE distinctive element repeated (rounded frames, icon circles, side borders)
- **Every slide needs visual element** — image, chart, icon, shape (never text-only)
- **Interesting font pairings** — Georgia/Calibri, Arial Black/Arial, Cambria/Calibri
- **Vary layouts** — two-column, icon+text, grids, half-bleed images

### Color Palettes (pick one)
| Theme | Primary | Secondary | Accent |
|-------|---------|-----------|--------|
| Midnight Executive | `1E2761` | `CADCFC` | `FFFFFF` |
| Forest & Moss | `2C5F2D` | `97BC62` | `F5F5F5` |
| Coral Energy | `F96167` | `F9E795` | `2F3C7E` |
| Charcoal Minimal | `36454F` | `F2F2F2` | `212121` |
| Teal Trust | `028090` | `00A896` | `02C39A` |

### Required QA Loop
```bash
# 1. Generate → Convert to images → Inspect
python scripts/office/soffice.py --headless --convert-to pdf output.pptx
pdftoppm -jpeg -r 150 output.pdf slide

# 2. Inspect with subagent (fresh eyes)
# 3. Fix issues
# 4. Re-verify affected slides
# 5. Repeat until clean pass
```

### Pitfalls
- Don't center body text (left-align)
- Don't default to blue (pick topic-specific colors)
- Don't use accent lines under titles (AI tell)
- Don't create text-only slides
- Don't mix spacing randomly

---

## Maps

> **Source:** Absorbed from `maps` skill. Geocode, POIs, routes, timezones via OpenStreetMap/OSRM.

### Prerequisites
Python 3.8+ (stdlib only, no pip installs)

```bash
MAPS=~/.hermes/skills/maps/scripts/maps_client.py
```

### Commands
```bash
# Geocode place name
python3 $MAPS search "Eiffel Tower"

# Reverse geocode
python3 $MAPS reverse 48.8584 2.2945

# Nearby places (46 categories)
python3 $MAPS nearby 48.8584 2.2945 restaurant --limit 10
python3 $MAPS nearby --near "Times Square, New York" --category cafe

# Distance & time
python3 $MAPS distance "Paris" --to "Lyon" --mode driving
python3 $MAPS distance "Big Ben" --to "Tower Bridge" --mode walking

# Turn-by-turn directions
python3 $MAPS directions "Eiffel Tower" --to "Louvre Museum" --mode walking

# Timezone
python3 $MAPS timezone 48.8584 2.2945

# Area bounding box
python3 $MAPS area "Manhattan, New York"

# Search within bbox
python3 $MAPS bbox 40.75 -74.00 40.77 -73.98 restaurant --limit 20
```

### Categories (46)
restaurant, cafe, bar, hospital, pharmacy, hotel, guest_house, camp_site, supermarket, atm, gas_station, parking, museum, park, school, university, bank, police, fire_station, library, airport, train_station, bus_stop, church, mosque, synagogue, dentist, doctor, cinema, theatre, gym, swimming_pool, post_office, convenience_store, bakery, bookshop, laundry, car_wash, car_rental, bicycle_rental, taxi, veterinary, zoo, playground, stadium, nightclub

### Telegram Location Pins
```bash
# User sends pin at lat/lon
python3 $MAPS nearby 36.17 -115.14 cafe --radius 1500
```

---

## nano-pdf

> **Source:** Absorbed from `nano-pdf` skill. Edit PDF text/typos/titles via nano-pdf CLI (NL prompts).

### Installation
```bash
# macOS
brew install nanite-ai/tap/nano-pdf

# Linux
curl -fsSL https://github.com/nanite-ai/nano-pdf/releases/latest/download/nano-pdf-linux -o ~/.local/bin/nano-pdf && chmod +x ~/.local/bin/nano-pdf
```

### Usage
```bash
# Fix a typo
nano-pdf document.pdf "change 'teh' to 'the' on page 3"

# Update title
nano-pdf document.pdf "set the title on page 1 to 'Annual Report 2026'"

# Bulk edits
nano-pdf document.pdf "replace all occurrences of 'Acme Corp' with 'Acme Inc'"
```

### Notes
- Uses natural language prompts (not exact string matching)
- Preserves layout/formatting
- Works on scanned PDFs with OCR

---

## Obsidian

> **Source:** Absorbed from `obsidian` skill. Read, search, create, edit notes in Obsidian vault.

### Vault Path
- `OBSIDIAN_VAULT_PATH` env var (e.g., from `~/.hermes/.env`)
- Fallback: `~/Documents/Obsidian Vault`

### Operations (use file tools)
```bash
# Read note
read_file "/path/to/vault/note.md"

# List notes
search_files target="files" pattern="*.md" path="/path/to/vault"

# Search content
search_files target="content" pattern="keyword" file_glob="*.md" path="/path/to/vault"

# Create note
write_file "/path/to/vault/new-note.md" "# Title\n\nContent"

# Append/edit
patch "/path/to/vault/note.md" "old_string" "new_string"
```

### Wikilinks
Use `[[Note Name]]` syntax for internal links

---

## Teams Meeting Pipeline

> **Source:** Absorbed from `teams-meeting-pipeline` skill. Operate Teams meeting summary pipeline via Hermes CLI.

### Prerequisites
```bash
# In ~/.hermes/.env
MSGRAPH_TENANT_ID=...
MSGRAPH_CLIENT_ID=...
MSGRAPH_CLIENT_SECRET=...
```

### Commands
```bash
# Status & inspection
hermes teams-pipeline validate
hermes teams-pipeline token-health
hermes teams-pipeline list
hermes teams-pipeline list --status failed
hermes teams-pipeline show <job-id>
hermes teams-pipeline subscriptions

# Re-running / debugging
hermes teams-pipeline run <job-id>              # replay
hermes teams-pipeline fetch --meeting-id <id>   # dry-run
hermes teams-pipeline fetch --join-web-url "<url>"

# Subscription management
hermes teams-pipeline subscribe --resource communications/onlineMeetings/getAllTranscripts --notification-url https://<host>/msgraph/webhook --client-state "$MSGRAPH_WEBHOOK_CLIENT_STATE"
hermes teams-pipeline renew-subscription <sub-id> --expiration <iso-8601>
hermes teams-pipeline delete-subscription <sub-id>
hermes teams-pipeline maintain-subscriptions --dry-run
```

### Critical Pitfall: Graph Subscriptions Expire in 72h
Microsoft Graph caps webhook subscriptions at 72 hours — **no auto-renewal**. If pipeline stops working:
1. `hermes teams-pipeline subscriptions` — check expiration
2. Recreate with `subscribe`
3. **Automate renewal** via cron (12h interval): `hermes cron add "0 */12 * * *" "hermes teams-pipeline maintain-subscriptions"`

---

## Himalaya Email

> **Source:** Absorbed from `himalaya` skill. Himalaya CLI: IMAP/SMTP email from terminal.

### Prerequisites
```bash
# Install
curl -sSL https://raw.githubusercontent.com/pimalaya/himalaya/master/install.sh | PREFIX=~/.local sh
# Or: brew install himalaya / cargo install himalaya

# Configure
himalaya account configure
# Creates ~/.config/himalaya/config.toml
```

### Config Example (Gmail)
```toml
[accounts.personal]
email = "you@gmail.com"
display-name = "Your Name"
default = true

backend.type = "imap"
backend.host = "imap.gmail.com"
backend.port = 993
backend.encryption.type = "tls"
backend.login = "you@gmail.com"
backend.auth.type = "password"
backend.auth.cmd = "pass show email/imap"

message.send.backend.type = "smtp"
message.send.backend.host = "smtp.gmail.com"
message.send.backend.port = 587
message.send.backend.encryption.type = "start-tls"
message.send.backend.login = "you@gmail.com"
message.send.backend.auth.type = "password"
message.send.backend.auth.cmd = "pass show email/smtp"

folder.aliases.inbox = "INBOX"
folder.aliases.sent = "Sent"
folder.aliases.drafts = "Drafts"
folder.aliases.trash = "Trash"
```

### Common Operations
```bash
# List emails
himalaya envelope list --folder "INBOX" --page 1 --page-size 20

# Search
himalaya envelope list from "john@example.com" subject "meeting"

# Read email
himalaya message read 42

# Send email (non-interactive)
cat << 'EOF' | himalaya template send
From: you@example.com
To: recipient@example.com
Subject: Test
Body here
EOF

# Reply (template approach)
himalaya template reply 42 | sed 's/^$/Your reply here\n/' | himalaya template send

# Move/Copy
himalaya message move 42 "Archive"
himalaya message copy 42 "Important"

# Attachments
himalaya attachment download 42 --dir ~/Downloads
```

### Output Formats
```bash
himalaya envelope list --output json
```

---

## Decision Matrix

| Task | Tool | Why |
|------|------|-----|
| **Structured data, forms, views** | Airtable | Base/tables/records API, filters, upserts |
| **Team collaboration, email, calendar, docs** | Google Workspace | Full suite, OAuth, real-time Sheets |
| **Knowledge base, wiki, databases** | Notion | Pages, databases, markdown, Workers |
| **Presentations, decks** | PowerPoint | .pptx create/read/edit, design principles |
| **Location, routing, geocoding** | Maps | Free OSM/OSRM, 46 POI categories |
| **PDF text fixes** | nano-pdf | NL prompts, preserves layout |
| **Personal knowledge management** | Obsidian | Local vault, wikilinks, markdown |
| **Corporate meeting summaries** | Teams Pipeline | Graph webhooks, automated processing |
| **Personal email (IMAP/SMTP)** | Himalaya | CLI email client, multiple accounts |

---

## Related Skills

- **`social-media-communication`** — X/Twitter (xurl), Yuanbao
- **`smart-home-iot`** — Hue lights (openhue), TouchDesigner
- **`creative-design-systems`** — Design systems (popular-web-designs), design specs (design-md)
- **`research-knowledge-retrieval`** — Blog monitoring, paper writing, prediction markets, YouTube
- **`mlops-model-registry-tracking`** — W&B, HF Hub for experiment tracking
