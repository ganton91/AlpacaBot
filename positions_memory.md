# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-07-01

---

## SAN
- **Status**: active
- **Entry date**: 2026-06-11 (fill confirmed 2026-06-12)
- **Entry price**: $12.66 (actual — Alpaca avg_entry_price)
- **Original qty**: 729 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $11.91 (consolidation low)

**Stop history:**
- 2026-06-11: $11.91 — initial stop (order pending fill)
- 2026-06-12: $11.91 — GTC stop reinstated (OTO leg expired as DAY order, order e651530b)
- 2026-06-16: $12.66 — breakeven stop (unrealized_pl_pct 6.4%, replaced order e651530b → 29c06248)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-16

---

## USB
- **Status**: active
- **Entry date**: 2026-06-22 (fill confirmed 2026-06-23)
- **Entry price**: $59.80 (actual — Alpaca avg_entry_price)
- **Original qty**: 118 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $55.19 (consolidation low)

**Stop history:**
- 2026-06-22: $55.19 — initial stop (order pending fill)
- 2026-06-23: $55.19 — GTC stop reinstated (OTO leg expired as DAY order, order bf4e765d)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-23

---

## FITB
- **Status**: active
- **Entry date**: 2026-06-24 (fill confirmed 2026-06-25)
- **Entry price**: $55.67 (actual — Alpaca avg_entry_price)
- **Original qty**: 166 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $52.30 (consolidation low)

**Stop history:**
- 2026-06-24: $52.30 — initial stop (order pending fill)
- 2026-06-25: $52.30 — GTC stop reinstated (OTO leg expired as DAY order, order 85c1a602)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-25

---

<!-- TEMPLATE — two stages. Use PENDING when placing the order; transition to ACTIVE when fill is confirmed in Step 3.

PENDING (copy this when placing a new order in Step 5):

## [SYMBOL]
- **Status**: pending
- **Order ID**: [alpaca_order_id]
- **Entry date**: YYYY-MM-DD
- **Planned entry**: $X.XX (consolidation high / Option A trigger / current price)
- **Planned qty**: N
- **Setup**: [Breakout A / Breakout B / EP]
- **Initial stop**: $X.XX (consolidation low / gap day low)

**Stop history:**
- YYYY-MM-DD: $X.XX — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: YYYY-MM-DD

---

ACTIVE (replace the pending block with this once fill is confirmed in Step 3):

## [SYMBOL]
- **Status**: active
- **Entry date**: YYYY-MM-DD (fill confirmed YYYY-MM-DD)
- **Entry price**: $X.XX (actual — Alpaca avg_entry_price)
- **Original qty**: N (actual filled qty)
- **Setup**: [Breakout A / Breakout B / EP]
- **Initial stop**: $X.XX (consolidation low / gap day low)

**Stop history:**
- YYYY-MM-DD: $X.XX — initial stop

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: YYYY-MM-DD

-->

---

*(3 active as of 2026-07-01: FITB (active @ $55.67, unrealized +3.27%, GTC stop $52.30 order 85c1a602 unchanged — below 5% band, no trailing-stop update), SAN (active @ $12.66, unrealized +9.08%, GTC breakeven stop $12.66 order 29c06248 unchanged — in 5-10% band, stop already at entry price so no update), USB (active @ $59.80, unrealized +3.61%, GTC safety-net stop $55.19 order bf4e765d unchanged — below 5% band, no trailing-stop update). No pending entries to reconcile. Earnings confirmed via web search: FITB 7/17 (16 days), SAN 7/22 (21 days), USB 7/16 (15 days) — all outside 2-day exit window and outside 14-day new-entry filter. GREEN signal — 2 slots available. Setup scanner: no qualifying setups — KEY at -1.9% and CSX at -0.5% were closest to Option A threshold but both had volume_declining=false. Watchlist: F removed (failed Trend Template re-screen); META and SNDK from web search failed Trend Template; SDOT failed Trend Template. 14 symbols remain. trend_template_batch.py failed again (TLS/curl error) — 6th consecutive session. No orders placed. Market signal: GREEN.)*
