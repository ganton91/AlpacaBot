# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-06-04

---

## RF
- **Status**: pending
- **Order ID**: 6237d5a5-c2b5-437e-a75e-b83cc140cb9d
- **Entry date**: 2026-06-04
- **Planned entry**: $28.50 (consolidation high — Option A trigger)
- **Planned qty**: 356
- **Setup**: Breakout A
- **Initial stop**: $27.18 (consolidation low)

**Stop history:**
- 2026-06-04: $27.18 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-04

---

## SAN
- **Status**: pending
- **Order ID**: 40a4c8d0-5d6d-4c16-86e4-f2b735e8cafe
- **Entry date**: 2026-06-04
- **Planned entry**: $12.71 (consolidation high — Option A trigger)
- **Planned qty**: 736
- **Setup**: Breakout A
- **Initial stop**: $12.02 (consolidation low)

**Stop history:**
- 2026-06-04: $12.02 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-04

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

## AAPL
- **Status**: active
- **Entry date**: 2026-05-21 (fill confirmed 2026-05-22)
- **Entry price**: $308.18 (actual — Alpaca avg_entry_price)
- **Original qty**: 32 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $290.06 (consolidation low)

**Stop history:**
- 2026-05-21: $290.06 — initial stop (order pending fill)
- 2026-05-22: $290.06 — GTC stop reinstated (OTO leg expired as DAY order, order d81785b0)

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

*(3 active + 2 pending as of 2026-06-04: HST (active — fill confirmed 2026-06-04 @ $24.19, GTC stop reinstated f85a7144 @ $21.68, unrealized +1.03%), CSCO (active, stop at breakeven $121.40 order 921b38fd, unrealized +6.96%), AAPL (active, stop d81785b0 @ $290.06, unrealized +0.99%), RF (pending Breakout A order 6237d5a5 — stop_limit trigger $28.64/$28.79, OTO stop $27.18, 356 shares. Earnings: Jul 17 2026), SAN (pending Breakout A order 40a4c8d0 — stop_limit trigger $12.77/$12.84, OTO stop $12.02, 736 shares. Earnings: Jul 22 2026). Reconciled this session: HST (pending → active, fill confirmed), OXY (pending order c7679f4e expired unfilled — removed), STM (fully closed — GTC stop hit at $75.08 on 2026-06-04, entry was $79.90, loss -6.03%).)*
