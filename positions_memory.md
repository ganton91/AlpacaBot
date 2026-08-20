# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-08-20

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

## BMY
- **Status**: active
- **Entry date**: 2026-08-18 (fill confirmed 2026-08-19)
- **Entry price**: $66.98 (actual — Alpaca avg_entry_price)
- **Original qty**: 75 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $63.00 (consolidation low)

**Stop history:**
- 2026-08-18: $63.00 — initial stop (order pending fill)
- 2026-08-19: $63.00 — GTC stop reinstated (OTO leg expired as DAY order)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-08-19

---

## CSX
- **Status**: pending
- **Order ID**: 3d984641-826c-4e8b-bdbc-788fad32af56
- **Entry date**: 2026-08-20
- **Planned entry**: $51.55 (consolidation high)
- **Planned qty**: 139
- **Setup**: Breakout A
- **Initial stop**: $49.72 (consolidation low)

**Stop history:**
- 2026-08-20: $49.72 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-08-20

---
