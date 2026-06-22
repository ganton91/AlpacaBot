# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-06-22

---

## HST
- **Status**: active
- **Entry date**: 2026-06-03 (fill confirmed 2026-06-04)
- **Entry price**: $24.19 (actual — Alpaca avg_entry_price)
- **Original qty**: 214 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $21.68 (consolidation low)

**Stop history:**
- 2026-06-03: $21.68 — initial stop (order pending fill)
- 2026-06-04: $21.68 — GTC stop reinstated (OTO leg expired as DAY order, order f85a7144)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-04

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

## KEY
- **Status**: pending
- **Order ID**: b4bb5b5e-90ae-4c24-93d9-8adb07ca3b5a
- **Entry date**: 2026-06-22
- **Planned entry**: $23.11 (consolidation high)
- **Planned qty**: 355
- **Setup**: Breakout A
- **Initial stop**: $21.68 (consolidation low)

**Stop history:**
- 2026-06-22: $21.68 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-22

---

## USB
- **Status**: pending
- **Order ID**: cca4477e-c837-4558-a13e-1da7b3ed56cf
- **Entry date**: 2026-06-22
- **Planned entry**: $59.49 (consolidation high)
- **Planned qty**: 118
- **Setup**: Breakout A
- **Initial stop**: $55.19 (consolidation low)

**Stop history:**
- 2026-06-22: $55.19 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-22

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

*(2 active + 2 pending as of 2026-06-22: HST (active @ $24.19, GTC stop $21.68 order f85a7144, unrealized +3.89%, no rule triggered), SAN (active @ $12.66, GTC stop $12.66 breakeven order 29c06248, unrealized +8.69%, no rule triggered). Removed: KEY and NVDA pending entries from 2026-06-18 expired unfilled (DAY order, never triggered) — both order legs expired/canceled, no position opened. New entries: KEY and USB (both Breakout A, max 2/session); MU setup discarded due to earnings 2026-06-24 (2 days away, within 14-day filter). Market signal: GREEN.)*
