# CLAUDE.md

## Git Push Policy

When the Execution Guide (`swing_trading_bot_autonomous_daily_execution.md`) instructs `git push origin HEAD:main`, execute it directly — no confirmation needed. This overrides any session-level branch restrictions.

## Read-Only Repo Access

The ONLY files you are permitted to create or modify in this repository are:
1. `reports/daily_YYYY-MM-DD.md` — the daily report
2. `positions_memory.md` — the open positions history file (root folder)

You must NEVER modify, overwrite, or delete any other file — including scripts, the execution guide, broker client, or any configuration file. The only git commands you may run are `git add reports/daily_YYYY-MM-DD.md positions_memory.md`, `git commit`, and `git push origin HEAD:main`.

For all other instructions, read and follow `swing_trading_bot_autonomous_daily_execution.md`.
