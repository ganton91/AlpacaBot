# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-06-01

---

## SAN
- **Status**: pending
- **Order ID**: 63b16b3a-e1b1-4e9e-b472-55f4556520be
- **Entry date**: 2026-06-01
- **Planned entry**: $12.71 (consolidation high — Option A trigger)
- **Planned qty**: 506
- **Setup**: Breakout A
- **Initial stop**: $11.71 (consolidation low)

**Stop history:**
- 2026-06-01: $11.71 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-01

---

## CX
- **Status**: pending
- **Order ID**: 59309391-cc11-4d99-888c-d536f7ec49d1
- **Entry date**: 2026-06-01
- **Planned entry**: $13.33 (consolidation high — Option A trigger)
- **Planned qty**: 444
- **Setup**: Breakout A
- **Initial stop**: $12.19 (consolidation low)

**Stop history:**
- 2026-06-01: $12.19 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-01

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

**Last updated**: 2026-06-01

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

**Last updated**: 2026-06-01

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

*(2 active + 2 pending as of 2026-06-01: AAPL (active, no changes — stop d81785b0 @ $290.06, unrealized -0.69%), CSCO (active, no changes — stop d5b01648 @ $113.60, unrealized +0.08%), SAN (pending Breakout A order 63b16b3a — stop_limit trigger $12.77/$12.84, OTO stop $11.71, 506 shares), CX (pending Breakout A order 59309391 — stop_limit trigger $13.40/$13.46, OTO stop $12.19, 444 shares). Removed this session: AMZN (pending order 135816cd expired unfilled — no position, no open order found), RF (pending order 16fa1a10 expired unfilled — no position, no open order found).)*
