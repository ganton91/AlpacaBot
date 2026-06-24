# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-06-24

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

## CSCO
- **Status**: pending
- **Order ID**: dc98aa70-914f-4ad3-bc07-c0ab0f1a854a
- **Entry date**: 2026-06-24
- **Planned entry**: $122.89 (consolidation high)
- **Planned qty**: 80
- **Setup**: Breakout A
- **Initial stop**: $116.62 (consolidation low)

**Stop history:**
- 2026-06-24: $116.62 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-24

---

## FITB
- **Status**: pending
- **Order ID**: 874a87f5-72d4-40d4-88fc-6aa0012ad2ee
- **Entry date**: 2026-06-24
- **Planned entry**: $55.34 (consolidation high)
- **Planned qty**: 166
- **Setup**: Breakout A
- **Initial stop**: $52.30 (consolidation low)

**Stop history:**
- 2026-06-24: $52.30 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-24

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

*(2 active + 2 pending as of 2026-06-24: SAN (active @ $12.66, unrealized +5.61%, GTC breakeven stop $12.66 order 29c06248 unchanged — already correctly set), USB (active @ $59.80, unrealized +0.52%, GTC safety-net stop $55.19 order bf4e765d unchanged, below 5% band so no trailing-stop update). Removed: AAPL and FITB pending entries from 2026-06-23 both expired unfilled (DAY stop_limit orders, never triggered — confirmed OrderStatus.EXPIRED via Alpaca). New entries: CSCO and FITB (both Breakout A, max 2/session, prioritized by lowest consolidation_range_pct among 3 qualifying Option A setups — KEY (7.61% range) deferred to next session, all 3 passed earnings filter). Watchlist: removed RF (failed Trend Template). trend_template_batch.py failed (Yahoo Finance TLS error) — large-cap candidate scan skipped today. Market signal: GREEN.)*
