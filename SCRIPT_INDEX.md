# SCRIPT INDEX

Reference guide for all scripts in `scripts/`. Each entry explains what the script does, what data it fetches, what criteria it applies, and what it outputs. Read this to understand the pipeline without reading the Python code.

All scripts support `--json` for machine-readable output and a human-readable default mode.

---

## market_schedule.py
**Used in:** Step 0

**What it does:**
Determines whether the bot should run today or skip. Calls the Alpaca calendar API to check if today is an official US market trading day, and the Alpaca clock API for next open/close times.

**Output fields:**
- `mode` — `"run"` (trading day) or `"skip"` (weekend / holiday)
- `reason` — `"weekday"`, `"weekend"`, or `"market_holiday"`
- `next_open` — ISO timestamp of next market open (used by Step 3 earnings check)
- `next_open_2` — date string of the trading day after `next_open` (used by Step 3 earnings check)
- `hours_until_open` — hours until next open

**No filtering criteria** — purely informational.

---

## market_health.py
**Used in:** Step 1

**What it does:**
Fetches raw market data so the bot can determine the GREEN/YELLOW/RED signal. Does NOT decide the signal itself — that is done by the bot using the rules in the execution guide.

**Data fetched:**
- 250 days of daily bars for SPY and QQQ (IEX feed)
- VIX closing price from CBOE (Yahoo Finance as fallback)

**Calculations:**
- SPY and QQQ: 50-day MA, 200-day MA, whether price is above each MA, whether 50MA is rising (vs 10 days ago)
- VIX: today vs yesterday → direction `"rising"` or `"falling"`

**Output fields:**
- `spy` / `qqq`: price, ma50, ma200, above_50ma, above_200ma, ma50_rising
- `vix`: value, prev_value, direction, source

**Signal rules (applied by the bot, not this script):**
- **RED** — both indices below 50MA, OR death cross (50MA < 200MA), OR VIX > 30 rising
- **GREEN** — both indices above 50MA rising, AND VIX < 20 OR falling
- **YELLOW** — everything else

---

## account_snapshot.py
**Used in:** Step 2

**What it does:**
Fetches a complete picture of the current account state — equity, positions, and open orders. For each open position it also calculates moving averages and recent price momentum inline, so Step 3 needs no additional API calls.

**Data fetched:**
- Account: equity, cash, buying power
- All open US equity positions
- 120 days of daily bars per position (IEX feed) for MA calculation
- All open orders for each position (to find days_open)
- All open stock orders (for stop management)

**Calculations per position:**
- 10-day, 20-day, 50-day SMA
- `above_ma10`, `above_ma20`, `above_ma50` — boolean flags
- `unrealized_pl_pct` — P&L % from entry
- `days_open` — days since oldest filled buy order
- `price_change_10d` — % price change over last 10 trading days

**Output fields:**
- `account`: equity, cash, buying_power, exposure_pct
- `positions`: count, slots_available (vs MAX 5), stocks array
- `open_orders`: id, symbol, side, type, qty, stop_price, limit_price

---

## trend_template.py
**Used in:** Step 4 (for watchlist screening and new candidates)

**What it does:**
Takes a list of symbols and screens each one against the Minervini Trend Template. Returns only stocks that pass ALL 8 criteria plus the volume filter.

**Data fetched:**
- 250 trading days of daily bars per symbol (IEX feed, split-adjusted)

**Criteria (ALL must be true):**
1. Price ≥ $10.00
2. Price > 50-day MA
3. Price > 150-day MA
4. Price > 200-day MA
5. 50-day MA > 150-day MA
6. 150-day MA > 200-day MA
7. 200-day MA is rising (higher than 20 trading days ago)
8. Price ≥ 52-week high × 0.75 (within 25% of 52-week high)
9. Price ≥ 52-week low × 1.30 (at least 30% above 52-week low)
10. Average daily volume (20-day, excluding today) ≥ 500,000

**Usage:** `python scripts/trend_template.py --symbols SYM1,SYM2,SYM3 --json`
Symbols must be comma-separated with no spaces.

**Output fields per passing stock:**
- price, ma50, ma150, ma200, ma200_direction
- week52_high, week52_low, pct_from_52w_high, pct_above_52w_low
- avg_volume_20d, criteria (dict of individual pass/fail per criterion)

---

## trend_template_batch.py
**Used in:** Step 4 (Action 4 — primary base-breakout universe)

**What it does:**
Dynamically fetches the top 1000 large cap US-listed stocks (NYSE + NASDAQ, market cap > $10B) via Yahoo Finance screener (yfinance), then screens them against the full Minervini Trend Template using batch fetching for efficiency. Results are pre-screened — they do NOT need to be re-screened via `trend_template.py`.

**Data fetched:**
- Top 1000 large cap symbols from Yahoo Finance (yfinance EquityQuery, sorted by market cap descending)
- 250 trading days of daily bars in batches of 50 symbols (IEX feed)

**Pre-filter (before Trend Template):**
- Price ≥ $10
- Exchange: NYSE (NYQ) or NASDAQ (NMS) only
- Symbols with `-` are normalized to `.` (e.g. `BRK-A` → `BRK.A`) since Alpaca uses dot notation for preferred shares / class variants

**Criteria:** Identical to `trend_template.py` — all 10 criteria must pass.

**Output fields per passing stock:**
- Same as trend_template.py output

**Note:** Symbol list is fetched dynamically at runtime — always current, no manual maintenance needed.

---

## candidates.py
**Used in:** Step 4 (Action 4 — EP-focused universe)

**What it does:**
Fetches today's top gainers (top 20) and most active stocks by volume (top 30) from the Alpaca screener. Combines and deduplicates them. These are potential EP (Episodic Pivot) candidates — stocks making big moves today.

**Filters applied here:**
- Price ≥ $10 (removes penny stocks)
- Deduplication (gainers take priority)

**Filters NOT applied here** (done separately via `trend_template.py`):
- Volume ≥ 500,000
- Minervini Trend Template criteria

**Output fields per candidate:**
- symbol, price, change_pct, source (`"gainers"` or `"most_active"`)

---

## setup_scanner.py
**Used in:** Step 5 (Action 1)

**What it does:**
For each symbol in the watchlist, calculates Breakout and EP metrics to identify actionable entry setups.

**Data fetched:**
- 60 calendar days of daily bars per symbol (IEX feed) — ensures 20+ trading days

**Breakout metrics (last 10 bars = ~2 weeks consolidation):**
- `consolidation_high` — max high of last 10 bars (resistance level / entry trigger)
- `consolidation_low` — min low of last 10 bars (stop level)
- `consolidation_range_pct` — (high - low) / low × 100 — base width %
- `pct_from_resistance` — (price - consolidation_high) / consolidation_high × 100
- `volume_declining` — avg vol of last 5 base bars < avg vol of prior 4 base bars (today excluded)
- `today_volume_ratio` — today's volume / 20-day avg volume (today excluded from avg)

**EP metrics:**
- `gap_pct` — (today open - yesterday close) / yesterday close × 100
- `gap_day_high` — today's high
- `gap_day_low` — today's low (used as stop_price for Option C entries)
- `close_location` — (close - gap_day_low) / (gap_day_high - gap_day_low) — where the close sits within the day's range (0=low, 1=high)
- `volume_ratio` — today volume / 20-day avg volume
- `is_ep_candidate` — true if gap_pct ≥ 8% AND volume_ratio ≥ 2.0 AND close_location ≥ 0.67

**Setup identification (done by the bot, not this script):**
- **Option A** (Breakout approaching): pct_from_resistance between -3% and 0% AND volume_declining: true
- **Option B** (Breakout confirmed): pct_from_resistance between 0% and +3% AND today_volume_ratio ≥ 1.5 AND volume_declining: true
- **Option C** (EP): is_ep_candidate: true + confirmed catalyst via web search

**Usage:** `python scripts/setup_scanner.py --symbols SYM1,SYM2,SYM3 --json`
Symbols must be comma-separated with no spaces.
