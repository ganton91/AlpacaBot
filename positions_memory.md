# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-05-29

---

## AMZN
- **Status**: pending
- **Order ID**: 135816cd-5cd6-4ffe-b958-5f965e30c2ee
- **Entry date**: 2026-05-29
- **Planned entry**: $274.68 (consolidation high — Option A trigger)
- **Planned qty**: 26
- **Setup**: Breakout A
- **Initial stop**: $255.21 (consolidation low)

**Stop history:**
- 2026-05-29: $255.21 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-05-29

---

## RF
- **Status**: pending
- **Order ID**: 16fa1a10-4f7e-4068-a631-7302d2300605
- **Entry date**: 2026-05-29
- **Planned entry**: $28.50 (consolidation high — Option A trigger)
- **Planned qty**: 216
- **Setup**: Breakout A
- **Initial stop**: $26.16 (consolidation low)

**Stop history:**
- 2026-05-29: $26.16 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-05-29

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

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-05-29

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

**Last updated**: 2026-05-29

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

*(2 active + 2 pending as of 2026-05-29: AAPL (active, no changes — stop d81785b0 @ $290.06, unrealized +1.1%), CSCO (fill confirmed 2026-05-29 @ $121.40 — transitioned to active, GTC stop d5b01648 @ $113.60 reinstated, unrealized -0.6%), AMZN (pending Breakout A order 135816cd — stop_limit trigger $276.05/$277.43, OTO stop $255.21), RF (pending Breakout A order 16fa1a10 — stop_limit trigger $28.64/$28.79, OTO stop $26.16). Removed this session: VALE (pending order 34e7a742 expired unfilled — no position, no open order found).)*
