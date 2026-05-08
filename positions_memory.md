# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-05-08

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

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-05-08

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

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-05-08

---

## USB
- **Status**: pending
- **Order ID**: f37b6c3f-f756-48d6-b795-d1e0fa150412
- **Entry date**: 2026-05-08
- **Planned entry**: $57.04 (consolidation high / Option A trigger)
- **Planned qty**: 172
- **Setup**: Breakout A
- **Initial stop**: $54.91 (consolidation low)

**Stop history:**
- 2026-05-08: $54.91 — initial stop (OTO, order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-05-08

---

## AMZN
- **Status**: pending
- **Order ID**: 1769a9c8-cf35-4c39-83f1-3b3b149d11af
- **Entry date**: 2026-05-08
- **Planned entry**: $278.53 (consolidation high / Option A trigger)
- **Planned qty**: 22
- **Setup**: Breakout A
- **Initial stop**: $256.18 (consolidation low)

**Stop history:**
- 2026-05-08: $256.18 — initial stop (OTO, order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-05-08

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

*(4 entries as of 2026-05-08: ERIC (active, filled 2026-05-05), HPE (active, filled 2026-05-05), USB (pending fill, order f37b6c3f), AMZN (pending fill, order 1769a9c8). UMC closed — GTC stop at $14.70 triggered between sessions. Previous AMZN order cef1963a expired unfilled.)*
