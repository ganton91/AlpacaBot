# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-05-13

---

## ERIC
- **Status**: active
- **Entry date**: 2026-05-04 (fill confirmed 2026-05-05)
- **Entry price**: $12.02 (actual — Alpaca avg_entry_price)
- **Original qty**: 576 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $11.04 (consolidation low)

**Stop history:**
- 2026-05-04: $11.04 — initial stop (OTO, order pending fill)
- 2026-05-05: $11.04 — GTC stop reinstated (OTO leg expired as DAY order, order 483923c0)
- 2026-05-13: $12.02 — breakeven stop (unrealized +6.11%, order e01e9a00)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-05-13

---

## HPE
- **Status**: active
- **Entry date**: 2026-05-04 (fill confirmed 2026-05-05)
- **Entry price**: $29.78 (actual — Alpaca avg_entry_price)
- **Original qty**: 219 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $27.34 (consolidation low)

**Stop history:**
- 2026-05-04: $27.34 — initial stop (OTO, order pending fill)
- 2026-05-05: $27.34 — GTC stop reinstated (OTO leg expired as DAY order, order aaa3c7c2)
- 2026-05-13: $30.07 — MA10 trailing stop (unrealized +12.79%, order 6dc0fbf3)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-05-13

---

## TEVA
- **Status**: pending
- **Order ID**: 60d79019-ca78-4b54-9957-0db4b16a4fef
- **Entry date**: 2026-05-13
- **Planned entry**: $36.99 (consolidation high / Option A trigger)
- **Planned qty**: 206
- **Setup**: Breakout A
- **Initial stop**: $34.56 (consolidation low)

**Stop history:**
- 2026-05-13: $34.56 — initial stop (OTO, order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-05-13

---

## GOOGL
- **Status**: pending
- **Order ID**: 9b7265c4-e101-467f-94bc-4a86241bdd12
- **Entry date**: 2026-05-13
- **Planned entry**: $403.69 (consolidation high / Option A trigger)
- **Planned qty**: 13
- **Setup**: Breakout A
- **Initial stop**: $365.87 (consolidation low)

**Stop history:**
- 2026-05-13: $365.87 — initial stop (OTO, order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-05-13

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

*(4 positions as of 2026-05-13: ERIC (active, filled 2026-05-05), HPE (active, filled 2026-05-05), TEVA (pending, order placed 2026-05-13), GOOGL (pending, order placed 2026-05-13). HAL expired unfilled — order f0f0b2a3 not found in open_orders on 2026-05-13 reconciliation.)*
