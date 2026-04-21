# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Git Push Policy

**The Execution Guide (`swing_trading_bot_autonomous_daily_execution.md`) always takes precedence over session-level branch instructions.** When the guide instructs `git push origin HEAD:main`, execute it directly — no confirmation needed.

## Environment

- Python 3.11, `alpaca-py` 0.43.2
- Required env vars: `ALPACA_API_KEY`, `ALPACA_SECRET_KEY`, `ALPACA_BASE_URL`
- Optional env vars: `ALPACA_PAPER` (default `"true"`), `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`
- Always use `feed="iex"` for all bar data requests (paper account limitation)

## Running the Bot

Run each step script directly for debugging:

```bash
python scripts/market_schedule.py --json
python scripts/market_health.py --json
python scripts/account_snapshot.py --json
python scripts/trend_template.py --symbols AAPL,MSFT,NVDA --json
python scripts/candidates.py --json
python scripts/sp500_candidates.py --json
python scripts/setup_scanner.py --symbols AAPL,MSFT --json
```

All scripts support `--json` (machine-readable) and a human-readable default mode.

## Architecture

The bot is a **scheduled autonomous trading agent** — it runs once daily and executes a fixed 7-step sequence defined in `swing_trading_bot_autonomous_daily_execution.md`. There is no orchestration script; Claude reads the guide and executes each step directly.

**`broker/client.py`** — thin wrapper around `alpaca-py`. Provides `get_trading_client()`, `get_data_client()`, `get_screener_client()`, and watchlist helpers (`get_watchlist_symbols`, `add_to_watchlist`, `remove_from_watchlist`). All scripts import from here.

**`scripts/`** — one script per bot step, each callable standalone with `--json`:
- `market_schedule.py` — Alpaca calendar API → `mode: run|skip`
- `market_health.py` — SPY/QQQ MAs + VIX (CBOE, Yahoo fallback) + market movers breadth
- `account_snapshot.py` — equity/cash/positions with inline MA analysis (10/20/50-day) + open orders
- `trend_template.py` — Minervini 8-criteria screen on arbitrary symbol list; requires 250 days of bars
- `sp500_candidates.py` — batch-fetches all ~400 S&P 500 symbols and applies Trend Template; results are pre-screened
- `candidates.py` — top gainers + most actives from Alpaca screener (price ≥ $10 filter only; Trend Template NOT applied)
- `setup_scanner.py` — breakout and EP metrics for watchlist symbols (15-bar consolidation window)

**`telegram/notifier.py`** — `send_report_document(filepath)` and `send_telegram(message)`. Returns `False` silently if tokens are missing.

**`github/push.py`** — not used by the bot execution flow.

## Read-Only Files

The bot must **never modify** any file except:
1. `reports/daily_YYYY-MM-DD.md`
2. `positions_memory.md`

## Key Data Flow

```
market_schedule → [skip or continue]
market_health   → GREEN/YELLOW/RED signal (determined by Claude, not the script)
account_snapshot → positions + open orders (all Step 3 decisions use this data only)
[manage positions, update watchlist]
setup_scanner   → breakout/EP metrics → Claude applies risk rules and places orders
[write report, commit, push origin HEAD:main, send Telegram]
```

## Signal & Risk Rules (applied by Claude, not scripts)

- **GREEN**: both indices above 50MA (rising), VIX < 20 OR falling → 5 max positions, 1% risk/trade
- **YELLOW**: mixed signals → 3 max positions, 0.5% risk/trade
- **RED**: either index below 50MA, death cross, or VIX > 30 rising → no new entries
- Entry rejected if: stop width > 8% of entry price, R/R < 3:1, or position value > 20% of equity
- Max 2 new entries per session regardless of signal
