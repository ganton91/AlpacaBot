# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-04-28

---

## RF
- **Status**: pending
- **Order ID**: b743b975-8764-43d6-8ce4-790e66a1d4c3
- **Entry date**: 2026-04-28
- **Planned entry**: $28.72 (consolidation high / Option A trigger)
- **Planned qty**: 349
- **Setup**: Breakout A
- **Initial stop**: $27.58 (consolidation low)

**Stop history:**
- 2026-04-28: $27.58 — initial stop (OTO, order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-04-28

---

## KEY
- **Status**: pending
- **Order ID**: c01d24ee-7324-404b-83e5-b3fe9a126069
- **Entry date**: 2026-04-28
- **Planned entry**: $22.54 (consolidation high / Option A trigger)
- **Planned qty**: 439
- **Setup**: Breakout A
- **Initial stop**: $21.40 (consolidation low)

**Stop history:**
- 2026-04-28: $21.40 — initial stop (OTO, order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-04-28

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

*(2 open/pending positions as of 2026-04-28: RF (pending fill), KEY (pending fill). Previous RF and KEY entries from 2026-04-27 expired unfilled — day orders not triggered.)*
