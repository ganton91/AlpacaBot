# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-05-06

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

**Last updated**: 2026-05-05

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

**Last updated**: 2026-05-05

---

## KEY
- **Status**: active
- **Entry date**: 2026-05-05 (fill confirmed 2026-05-06)
- **Entry price**: $22.41 (actual — Alpaca avg_entry_price)
- **Original qty**: 449 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $21.50 (consolidation low)

**Stop history:**
- 2026-05-05: $21.50 — initial stop (OTO, order pending fill)
- 2026-05-06: $21.50 — GTC stop reinstated (OTO leg expired as DAY order, order 46ace413)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-05-06

## AMD
- **Status**: pending
- **Order ID**: bf49dd90-65fe-4a4e-8388-5c63249b29fb
- **Entry date**: 2026-05-06
- **Planned entry**: $421.55 (current price / EP trigger)
- **Planned qty**: 23
- **Setup**: EP
- **Initial stop**: $402.25 (gap day low)

**Stop history:**
- 2026-05-06: $402.25 — initial stop (OTO, order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-05-06

---

## UMC
- **Status**: pending
- **Order ID**: 25e67645-37d9-4352-869d-fa4373e38d4c
- **Entry date**: 2026-05-06
- **Planned entry**: $15.22 (current price / EP trigger)
- **Planned qty**: 659
- **Setup**: EP
- **Initial stop**: $14.70 (gap day low)

**Stop history:**
- 2026-05-06: $14.70 — initial stop (OTO, order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-05-06

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

*(5 positions as of 2026-05-06: ERIC (active, filled 2026-05-05), HPE (active, filled 2026-05-05), KEY (active, filled 2026-05-06), AMD (pending fill), UMC (pending fill).)*
