# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-06-02

---

## STM
- **Status**: pending
- **Order ID**: 8f37b25e-f943-42ab-8d94-52873ee1d9b8
- **Entry date**: 2026-06-02
- **Planned entry**: $79.52 (current price — EP Option C trigger)
- **Planned qty**: 129
- **Setup**: EP
- **Initial stop**: $75.61 (gap day low)

**Stop history:**
- 2026-06-02: $75.61 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-02

---

## RF
- **Status**: pending
- **Order ID**: 91f8e1f3-a216-4e41-8e67-0ebebef556b9
- **Entry date**: 2026-06-02
- **Planned entry**: $28.50 (consolidation high — Option A trigger)
- **Planned qty**: 285
- **Setup**: Breakout A
- **Initial stop**: $26.70 (consolidation low)

**Stop history:**
- 2026-06-02: $26.70 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-02

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

*(2 active + 2 pending as of 2026-06-02: CSCO (active, stop raised to breakeven $121.40 order 921b38fd, unrealized +5.35%), AAPL (active, no changes — stop d81785b0 @ $290.06, unrealized +2.28%), STM (pending EP order 8f37b25e — stop_limit trigger $79.52/$79.92, OTO stop $75.61, 129 shares, catalyst: STM raised data center revenue target to $1B), RF (pending Breakout A order 91f8e1f3 — stop_limit trigger $28.64/$28.79, OTO stop $26.70, 285 shares). Reconciled this session: SAN (pending order 63b16b3a expired unfilled — removed), CX (pending order 59309391 expired unfilled — removed).)*
