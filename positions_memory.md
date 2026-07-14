# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-07-14

---

## BAC
- **Status**: pending
- **Order ID**: abd940c4-457d-4b64-a63d-00992aa0f343
- **Entry date**: 2026-07-14
- **Planned entry**: $61.20 (consolidation high / Option A trigger)
- **Planned qty**: 117
- **Setup**: Breakout A
- **Initial stop**: $56.84 (consolidation low)

**Stop history:**
- 2026-07-14: $56.84 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-07-14

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

*(1 pending as of 2026-07-14: BAC Option A order placed — 117 shares, stop trigger $61.51, limit $61.81, stop loss $56.84, order ID abd940c4-457d-4b64-a63d-00992aa0f343. BAC earnings reported today Jul 14 (beat: $1.21 vs $1.13 est), next earnings Oct 14. CSX disqualified — earnings Jul 22 (8 days). Watchlist: removed C (failed Trend Template); 6 symbols remaining: AMD, UMC, ASX, KEY, CSX, BAC. trend_template_batch.py failed TLS again (14th consecutive session). Signal: GREEN. Next session: 2026-07-15.)*
