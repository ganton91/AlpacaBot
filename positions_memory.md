# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-06-23

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

## AAPL
- **Status**: pending
- **Order ID**: b7607ab7-a146-4783-bb7c-620501d48d7c
- **Entry date**: 2026-06-23
- **Planned entry**: $302.42 (consolidation high)
- **Planned qty**: 33
- **Setup**: Breakout A
- **Initial stop**: $287.38 (consolidation low)

**Stop history:**
- 2026-06-23: $287.38 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-23

---

## FITB
- **Status**: pending
- **Order ID**: 16318eac-d207-47c0-968b-7d7b90f03c38
- **Entry date**: 2026-06-23
- **Planned entry**: $55.28 (consolidation high)
- **Planned qty**: 156
- **Setup**: Breakout A
- **Initial stop**: $52.05 (consolidation low)

**Stop history:**
- 2026-06-23: $52.05 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-23

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

*(2 active + 2 pending as of 2026-06-23: SAN (active @ $12.66, GTC stop $12.66 breakeven order 29c06248, unrealized +7.42%, no rule triggered), USB (fill confirmed today @ $59.80, GTC safety-net stop $55.19 placed order bf4e765d — OTO leg had expired as DAY order). Closed: HST — stagnant position (days_open 19 >= 10, price_change_10d 1.51% < 2%), market sell order submitted, stop order f85a7144 canceled. Removed: KEY pending entry from 2026-06-22 expired unfilled (DAY order, never triggered) — order leg expired, no position opened. New entries: AAPL and FITB (both Breakout A, max 2/session, prioritized by lowest consolidation_range_pct among 4 qualifying Option A setups — KEY and CSCO setups deferred to next session, all passed earnings filter). Market signal: GREEN.)*
