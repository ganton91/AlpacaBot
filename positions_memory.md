# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-06-03

---

## OXY
- **Status**: pending
- **Order ID**: c7679f4e-3461-414c-ae18-408da2e93b83
- **Entry date**: 2026-06-03
- **Planned entry**: $61.20 (consolidation high — Option A trigger)
- **Planned qty**: 93
- **Setup**: Breakout A
- **Initial stop**: $55.76 (consolidation low)

**Stop history:**
- 2026-06-03: $55.76 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-03

---

## HST
- **Status**: pending
- **Order ID**: c52a7e10-e830-45a6-a904-119649a2f041
- **Entry date**: 2026-06-03
- **Planned entry**: $24.06 (consolidation high — Option A trigger)
- **Planned qty**: 214
- **Setup**: Breakout A
- **Initial stop**: $21.68 (consolidation low)

**Stop history:**
- 2026-06-03: $21.68 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-03

---

## STM
- **Status**: active
- **Entry date**: 2026-06-02 (fill confirmed 2026-06-03)
- **Entry price**: $79.90 (actual — Alpaca avg_entry_price)
- **Original qty**: 129 (actual filled qty)
- **Setup**: EP
- **Initial stop**: $75.61 (gap day low)

**Stop history:**
- 2026-06-02: $75.61 — initial stop (order pending fill)
- 2026-06-03: $75.61 — GTC stop reinstated (OTO leg expired as DAY order, order 565f1a4b)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-03

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

*(3 active + 2 pending as of 2026-06-03: CSCO (active, stop at breakeven $121.40 order 921b38fd, unrealized +4.28%), AAPL (active, stop d81785b0 @ $290.06, unrealized +0.85%), STM (active — fill confirmed 2026-06-03 @ $79.90, GTC stop reinstated 565f1a4b @ $75.61, unrealized -0.50%), OXY (pending Breakout A order c7679f4e — stop_limit trigger $61.51/$61.81, OTO stop $55.76, 93 shares. Earnings: Aug 5 2026), HST (pending Breakout A order c52a7e10 — stop_limit trigger $24.18/$24.30, OTO stop $21.68, 214 shares. Earnings: ~Aug 2026). Reconciled this session: STM (pending → active, fill confirmed), RF (pending order 91f8e1f3 expired unfilled — removed).)*
