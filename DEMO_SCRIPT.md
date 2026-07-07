# MCP demo script

One-liner to open with: "MCP (Model Context Protocol) lets Claude talk to external tools and services as if they were built in — each connected server adds a new set of actions Claude can take beyond just writing text."

## 1. List connected MCP servers
**Say:** "Here are all the tool servers connected to this session — filesystem access, browser control, live charting, scheduling, and a connector registry. Nothing here is hypothetical, these are live and callable right now."

**Show:** the list of connected servers (filesystem, claude-in-chrome, visualize, scheduled-tasks, mcp-registry, ccd_session, ccd_session_mgmt, ccd_directory, Claude_Preview).

## 2. Filesystem MCP — read a directory
**Say:** "This server gives Claude a dedicated view into the project's files, separate from its own built-in file tools. Here's a clean recursive tree of this audit demo folder."

**Show:** the directory tree output (excluding `.git`) — `agent_logic.py`, `client_audit.txt`, `client_status.txt`, `risk_data.txt`, `start.py`.

**Talking point:** the first time we ran this, it also returned everything inside `.git` — a good reminder that MCP tools see exactly what a normal filesystem call sees, which is why scoping and permissions matter in a real deployment.

## 3. Visualize MCP — turn flat data into a live chart
**Say:** "Two of our client files had raw numbers — a debt ratio for Global Dynamics and one for Alpha Tech. Rather than reading two lines of text, here's that same data rendered live as a chart, with a risk threshold overlaid."

**Show:** the bar chart comparing debt ratios (Global Dynamics 0.72, Alpha Tech 0.65) against a 0.60 risk threshold line — both clients sit above it.

**Talking point:** this ties directly back to the audit read — both clients would land in a higher-risk review tier, and now that's visible at a glance instead of buried in a text file.

## 4. Claude-in-chrome MCP — browser automation
**Say:** "Claude can also act inside a real browser — navigate, read the page, click, screenshot — not just describe one."

**Status:** not demoed live in this session — the Chrome extension wasn't reachable (it requires the actual Google Chrome browser with the extension signed in; Safari isn't supported). Frame this as: "here's what it would do" if you can't get Chrome connected before presenting, or get Chrome running beforehand and re-run the navigate step live.

## 5. Fixing real code with the demo data
**Say:** "While reviewing these files, we found more than typos — `agent_logic.py` had a tool called `calculate_risk_category` that didn't actually calculate anything. It called a method that doesn't exist in the Anthropic SDK (`anthropic.call`) and pointed at a model name that was never real (`claude-v1`)."

**Show:** the fixed `agent_logic.py` — now uses the real SDK (`client.messages.create`), a real current model (`claude-sonnet-5`), and actually returns a usable response instead of a placeholder string.

**Talking point:** this is the practical value of the assistant beyond chat — it read the code, caught that it was non-functional placeholder code, and fixed it to real, running logic.

## 6. Data-quality fixes
**Say:** "We also caught two typos in the client data itself: `Cerdit Score` → `Credit Score` in `risk_data.txt`, and `ration` → `ratio` in the tool description in `agent_logic.py`."

**Talking point:** small, but this is exactly the kind of low-risk, obviously-correct fix that's good for a first PR — visible, reviewable, no ambiguity about correctness.

## 7. Close the loop — GitHub PR
**Say:** "All of these fixes are about to go out as an actual tracked, reviewable pull request on GitHub — from spotting a data-quality issue in an audit file, to shipping a fix through a real code review workflow."

**Status:** GitHub CLI (`gh`) install is in progress (needs Homebrew, which requires an admin password — being installed by hand outside this session). Once connected: `gh auth login`, then open the PR with the typo + code fixes above.

## 8. (Optional, deferred) Database connection
**Say:** "Right now there's no database connector attached to this session. In a real engagement, this is where we'd connect to the client's actual data source — Postgres, Snowflake, etc. — instead of reading flat files."

**Status:** intentionally not demoed yet — revisit once the above is confirmed working end-to-end.
