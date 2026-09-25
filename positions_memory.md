# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-09-25

---

## APH
- **Status**: active
- **Entry date**: 2026-09-24 (fill confirmed 2026-09-25)
- **Entry price**: $84.93 (actual — Alpaca avg_entry_price)
- **Original qty**: 65 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $76.74 (consolidation low)

**Stop history:**
- 2026-09-24: $76.74 — initial stop (order pending fill)
- 2026-09-25: $76.74 — GTC safety net stop reinstated (no active stop found; order id: 438fa77c-b3a2-4ef9-93f6-badb4a2e3f2a)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-09-25

---

## SAN
- **Status**: pending
- **Order ID**: 53f041d9-d504-4083-add7-b41f140b3f74
- **Entry date**: 2026-09-25
- **Planned entry**: $14.85 (consolidation high / Option A trigger)
- **Planned qty**: 686
- **Setup**: Breakout A
- **Initial stop**: $14.15 (consolidation low)

**Stop history:**
- 2026-09-25: $14.15 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-09-25

---

## AAPL
- **Status**: active
- **Entry date**: 2026-09-21 (fill confirmed 2026-09-22)
- **Entry price**: $342.72 (actual — Alpaca avg_entry_price)
- **Original qty**: 8 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $309.92 (consolidation low)

**Stop history:**
- 2026-09-21: $309.92 — initial stop (order pending fill)
- 2026-09-22: $309.92 — GTC safety net stop reinstated (no active stop found; order id: 9aff2900-82b3-4f8c-9c34-7eb2d9f20bf8)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-09-22

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
