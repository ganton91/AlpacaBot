# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-09-21

---

## GOOG
- **Status**: active
- **Entry date**: 2026-09-17 (fill confirmed 2026-09-18)
- **Entry price**: $349.86 (actual — Alpaca avg_entry_price)
- **Original qty**: 12 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $325.66 (consolidation low)

**Stop history:**
- 2026-09-17: $325.66 — initial stop (order pending fill)
- 2026-09-18: $325.66 — GTC safety net stop reinstated (no active stop found; order id: 2c91b582-6707-40cc-8354-59f2f4d6b117)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-09-18

---

## SAN
- **Status**: pending
- **Order ID**: b74a8bfd-1424-4e05-a326-3eec4764db9c
- **Entry date**: 2026-09-21
- **Planned entry**: $14.98 (consolidation high / Option A trigger)
- **Planned qty**: 376
- **Setup**: Breakout A
- **Initial stop**: $14.30 (consolidation low)

**Stop history:**
- 2026-09-21: $14.30 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-09-21

---

## AAPL
- **Status**: pending
- **Order ID**: 67227c88-53c4-491b-8c7b-7324d4c3e9a3
- **Entry date**: 2026-09-21
- **Planned entry**: $339.62 (consolidation high / Option A trigger)
- **Planned qty**: 8
- **Setup**: Breakout A
- **Initial stop**: $309.92 (consolidation low)

**Stop history:**
- 2026-09-21: $309.92 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-09-21

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
