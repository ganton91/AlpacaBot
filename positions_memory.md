# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-08-03

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
- **Status**: pending
- **Order ID**: 2202e3f1-884e-46cb-8279-3f6c4fda1663
- **Entry date**: 2026-08-03
- **Planned entry**: $62.98 (consolidation high — Option A trigger)
- **Planned qty**: 88
- **Setup**: Breakout A
- **Initial stop**: $60.07 (consolidation low)

**Stop history:**
- 2026-08-03: $60.07 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-08-03

---

## KEY
- **Status**: pending
- **Order ID**: 78fe2010-75d8-45a1-87c3-c4004fb302d2
- **Entry date**: 2026-08-03
- **Planned entry**: $23.32 (consolidation high — Option A trigger)
- **Planned qty**: 217
- **Setup**: Breakout A
- **Initial stop**: $22.14 (consolidation low)

**Stop history:**
- 2026-08-03: $22.14 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-08-03
