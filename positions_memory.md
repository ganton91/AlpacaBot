# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-06-16

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

## SAN
- **Status**: active
- **Entry date**: 2026-06-11 (fill confirmed 2026-06-12)
- **Entry price**: $12.66 (actual — Alpaca avg_entry_price)
- **Original qty**: 729 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $11.91 (consolidation low)

**Stop history:**
- 2026-06-11: $11.91 — initial stop (order pending fill)
- 2026-06-12: $11.91 — GTC stop reinstated (OTO leg expired as DAY order, order e651530b)
- 2026-06-16: $12.66 — breakeven stop (unrealized_pl_pct 6.4%, replaced order e651530b → 29c06248)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-16

---

## CSX
- **Status**: active
- **Entry date**: 2026-06-11 (fill confirmed 2026-06-12)
- **Entry price**: $47.81 (actual — Alpaca avg_entry_price)
- **Original qty**: 177 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $44.82 (consolidation low)

**Stop history:**
- 2026-06-11: $44.82 — initial stop (order pending fill)
- 2026-06-12: $44.82 — GTC stop reinstated (OTO leg expired as DAY order, order 761185cc)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-12

---

## GOOGL
- **Status**: active
- **Entry date**: 2026-06-15 (fill confirmed 2026-06-16)
- **Entry price**: $375.43 (actual — Alpaca avg_entry_price)
- **Original qty**: 18 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $346.37 (consolidation low)

**Stop history:**
- 2026-06-15: $346.37 — initial stop (order pending fill)
- 2026-06-16: $346.37 — GTC stop reinstated (OTO leg expired as DAY order, order 38ade2a0)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-16

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

*(5 active as of 2026-06-16: RF (active @ $28.65, GTC stop $27.18 order 1d320db9, unrealized +1.22%), HST (active @ $24.19, GTC stop $21.68 order f85a7144, unrealized +2.94%), SAN (active @ $12.66, GTC stop $12.66 breakeven order 29c06248, unrealized +6.40%), CSX (active @ $47.81, GTC stop $44.82 order 761185cc, unrealized -2.26%), GOOGL (active @ $375.43, fill confirmed 2026-06-16, GTC stop $346.37 order 38ade2a0, unrealized -0.85%). No exits or new entries today (0 slots available, GREEN signal max 5). Watchlist: removed GOOGL (now held), NVDA (failed Trend Template); added TSM/CIFR (batch pre-screened). Market signal: GREEN.)*