# CLAUDE.md

## Git Push Policy

After saving the daily report, push to main using the `mcp__github__push_files` tool — NOT `git push`. This bypasses the Anthropic git proxy which blocks pushes to main from session branches.

The correct sequence in Step 6 is:
1. `git add reports/daily_YYYY-MM-DD.md positions_memory.md && git commit -m "Daily report YYYY-MM-DD"` — commits to the session branch for local history
2. Use `mcp__github__push_files` with `owner="ganton91"`, `repo="AlpacaBot"`, `branch="main"`, `message="Daily report YYYY-MM-DD"` to push both files directly to main via GitHub API

If the `mcp__github__push_files` call fails for any reason, send a Telegram notification immediately using `send_telegram` from `telegram/notifier.py` with the following text:
`"⚠️ SwingBot MCP push FAILED — daily report NOT pushed to main. Error: [exact error message]. Files were committed locally on session branch. Manual intervention required."`

Do this before ending the session. Do not silently skip the failure.

## Read-Only Repo Access

The ONLY files you are permitted to create or modify in this repository are:
1. `reports/daily_YYYY-MM-DD.md` — the daily report
2. `positions_memory.md` — the open positions history file (root folder)

You must NEVER modify, overwrite, or delete any other file — including scripts, the execution guide, broker client, or any configuration file. The only git commands you may run are `git add reports/daily_YYYY-MM-DD.md positions_memory.md` and `git commit`.

For all other instructions, read and follow `swing_trading_bot_autonomous_daily_execution.md`.

## Script Index Sync

Scripts in `scripts/` may only be modified when the user explicitly requests it and confirms the change. Never modify a script on your own initiative. When a script is modified, update `SCRIPT_INDEX.md` to reflect the change before committing.
