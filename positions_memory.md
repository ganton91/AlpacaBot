# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-05-28

---

## CSCO
- **Status**: pending
- **Order ID**: 65ea2b16-3cd0-4a8d-a991-3c860ec615a1
- **Entry date**: 2026-05-28
- **Planned entry**: $120.79 (consolidation high — Option A trigger)
- **Planned qty**: 70
- **Setup**: Breakout A
- **Initial stop**: $113.60 (consolidation low)

**Stop history:**
- 2026-05-28: $113.60 — initial stop (OTO, order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-05-28

---

## VALE
- **Status**: pending
- **Order ID**: 34e7a742-fbd8-45a3-99d4-7185b90b50b4
- **Entry date**: 2026-05-28
- **Planned entry**: $17.02 (consolidation high — Option A trigger)
- **Planned qty**: 434
- **Setup**: Breakout A
- **Initial stop**: $15.85 (consolidation low)

**Stop history:**
- 2026-05-28: $15.85 — initial stop (OTO, order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-05-28

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

**Last updated**: 2026-05-28

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

*(1 active + 2 pending as of 2026-05-28: AAPL (active, no changes — stop d81785b0 @ $290.06, unrealized +1.3%), CSCO (pending Breakout A order 65ea2b16 — stop_limit trigger $121.39/$122.00, OTO stop $113.60), VALE (pending Breakout A order 34e7a742 — stop_limit trigger $17.11/$17.19, OTO stop $15.85). Closed/removed this session: ERIC (anomaly — active in memory but not in Alpaca; assumed stopped out at $12.91; removed), CSX (pending order 5a2b157e expired unfilled; removed), SLB (closed — stagnant rule: 10 days, -0.5% 10d change, sell order 8c823ba2), HPE (closed — earnings June 1 = next_open_2, sell order 3dea187e; total closed 100% incl. prior partials).)*
