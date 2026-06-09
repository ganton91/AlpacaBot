# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-06-09

---

## RF
- **Status**: active
- **Entry date**: 2026-06-04 (fill confirmed 2026-06-05)
- **Entry price**: $28.65 (actual — Alpaca avg_entry_price)
- **Original qty**: 356 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $27.18 (consolidation low)

**Stop history:**
- 2026-06-04: $27.18 — initial stop (order pending fill)
- 2026-06-05: $27.18 — GTC stop reinstated (OTO leg expired as DAY order, order 1d320db9)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-05

---

## CSX
- **Status**: pending
- **Order ID**: b9bd849d-e027-49ce-b046-3b8aa0d105cd
- **Entry date**: 2026-06-09
- **Planned entry**: $47.55 (consolidation high)
- **Planned qty**: 184
- **Setup**: Breakout A
- **Initial stop**: $44.82 (consolidation low)

**Stop history:**
- 2026-06-09: $44.82 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-09

---

## VTRS
- **Status**: pending
- **Order ID**: be8847f9-7e82-421f-aaa9-a2eb0047d9da
- **Entry date**: 2026-06-09
- **Planned entry**: $16.41 (consolidation high)
- **Planned qty**: 552
- **Setup**: Breakout A
- **Initial stop**: $15.50 (consolidation low)

**Stop history:**
- 2026-06-09: $15.50 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-09

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

*(2 active + 2 pending as of 2026-06-09: RF (active @ $28.65, GTC stop $27.18 order 1d320db9, unrealized -0.18%), HST (active @ $24.19, GTC stop $21.68 order f85a7144, unrealized +1.16%). CSCO closed 2026-06-09 — breakeven stop at $121.40 triggered. Old CSX order 397c3870 expired unfilled. New CSX added 2026-06-09 — pending breakout A stop-limit order b9bd849d, trigger $47.79, limit $48.03, stop loss $44.82. VTRS added 2026-06-09 — pending breakout A stop-limit order be8847f9, trigger $16.49, limit $16.57, stop loss $15.50.)*
