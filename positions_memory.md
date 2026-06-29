# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-06-29

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

*(3 active as of 2026-06-29: FITB (active @ $55.67, unrealized +1.99%, GTC stop $52.30 order 85c1a602 unchanged, below 5% band so no trailing-stop update), SAN (active @ $12.66, unrealized +7.71%, GTC breakeven stop $12.66 order 29c06248 unchanged — already correctly set at calculated breakeven level), USB (active @ $59.80, unrealized +2.52%, GTC safety-net stop $55.19 order bf4e765d unchanged, below 5% band so no trailing-stop update). No pending entries to reconcile. Earnings checked for all three (FITB 7/17, SAN ~7/22-29, USB 7/16) — all >14 days away, no exit triggered. GREEN signal — 2 slots available, but no qualifying setups found on watchlist scan (no Option A in range had volume_declining, no symbol above resistance for Option B, no EP candidates), so Step 5 placed no new orders. Watchlist: no removals (all 15 symbols still pass Trend Template re-screen); no new candidates passed (UPC/SDOT/OC/ALAB from gainers+web search failed Trend Template, ASTG/ASTT/ASTY/ASUP/ASTX errored — likely invalid/illiquid tickers). trend_template_batch.py failed again (Yahoo Finance TLS/curl error) — large-cap candidate scan skipped, now 4 consecutive sessions. Market signal: GREEN.)*
