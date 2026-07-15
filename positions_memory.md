# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-07-15

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

## BAC
- **Status**: pending
- **Order ID**: 96816f94-5081-4fa6-90cc-7aa23d3fc4d1
- **Entry date**: 2026-07-15
- **Planned entry**: $62.02 (consolidation high / Option A trigger)
- **Planned qty**: 49
- **Setup**: Breakout A
- **Initial stop**: $56.84 (consolidation low)

**Stop history:**
- 2026-07-15: $56.84 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-07-15

---

*(1 pending as of 2026-07-15: BAC Option A order placed — 49 shares, stop trigger $62.33, limit $62.64, stop loss $56.84, order ID 96816f94-5081-4fa6-90cc-7aa23d3fc4d1. Prior BAC order (abd940c4) expired unfilled — price never reached $61.51 trigger. CSX disqualified — earnings Jul 22 (7 days). AAPL added to watchlist (passed Trend Template) but skipped for entry — consolidation range 13.66%, risk 12.02% exceeds 10% max. AAPL earnings Jul 30 (15 days). trend_template_batch.py failed TLS again (15th consecutive session). Signal: YELLOW (QQQ below 50MA). Next session: 2026-07-16.)*
