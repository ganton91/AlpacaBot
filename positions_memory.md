# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-06-05

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

## CSCO
- **Status**: active
- **Entry date**: 2026-05-28 (fill confirmed 2026-05-29)
- **Entry price**: $121.40 (actual — Alpaca avg_entry_price)
- **Original qty**: 70 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $113.60 (consolidation low)

**Stop history:**
- 2026-05-28: $113.60 — initial stop (OTO, order pending fill)
- 2026-05-29: $113.60 — GTC stop reinstated (OTO leg expired as DAY order, order d5b01648)
- 2026-06-02: $121.40 — raised to breakeven (unrealized +5.35%, 5–10% band, order 921b38fd)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-02

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

*(3 active as of 2026-06-05: RF (active — fill confirmed 2026-06-05 @ $28.65, GTC stop reinstated 1d320db9 @ $27.18, unrealized -0.38%), HST (active, GTC stop f85a7144 @ $21.68, unrealized +0.25%), CSCO (active, stop at breakeven $121.40 order 921b38fd, unrealized -0.13%). AAPL closed 2026-06-05 — exit rule: stagnant position (days_open=14, price_change_10d=0.83% < 2%), market sell order 1ce3ee03 accepted, executes Mon 2026-06-08. SAN pending order 40a4c8d0 expired unfilled — removed.)*
