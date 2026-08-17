# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-08-17

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

## BAC
- **Status**: active
- **Entry date**: 2026-08-03 (fill confirmed 2026-08-04)
- **Entry price**: $63.29 (actual — Alpaca avg_entry_price)
- **Original qty**: 88 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $60.07 (consolidation low)

**Stop history:**
- 2026-08-03: $60.07 — initial stop (order pending fill)
- 2026-08-04: $60.07 — GTC stop reinstated (OTO leg expired as DAY order)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-08-17

---

## CSX
- **Status**: pending
- **Order ID**: 2933193e-b28d-4e0e-b0e5-4a8bdbd26ff5
- **Entry date**: 2026-08-17
- **Planned entry**: $51.59 (consolidation high)
- **Planned qty**: 118
- **Setup**: Breakout A
- **Initial stop**: $49.43 (consolidation low)

**Stop history:**
- 2026-08-17: $49.43 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-08-17

---

## BMY
- **Status**: pending
- **Order ID**: 608dad99-92ee-4a96-aa86-bf071cacdb2d
- **Entry date**: 2026-08-17
- **Planned entry**: $66.31 (consolidation high)
- **Planned qty**: 77
- **Setup**: Breakout A
- **Initial stop**: $63.00 (consolidation low)

**Stop history:**
- 2026-08-17: $63.00 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-08-17

---
