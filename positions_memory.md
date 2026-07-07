# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-07-07

---

## CSX
- **Status**: pending
- **Order ID**: 176b48c4-f338-40e2-8152-1afedcf3ad5e
- **Entry date**: 2026-07-07
- **Planned entry**: $49.27 (consolidation high / Option A trigger)
- **Planned qty**: 36
- **Setup**: Breakout A
- **Initial stop**: $45.94 (consolidation low)

**Stop history:**
- 2026-07-07: $45.94 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-07-07

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

*(1 pending as of 2026-07-07: CSX (pending — OTO stop_limit buy 36 shares trigger $49.52 limit $49.76 stop $45.94, order 176b48c4, expires 2026-07-07). CRITICAL ANOMALY: Account showed 0 positions despite SAN, USB, FITB being active in positions_memory.md as of 2026-07-06. Their GTC stop orders were still in open_orders (SAN 1c73fed1 stop $13.71, USB 25cf72eb stop $59.80, FITB 85c1a602 stop $52.30) but the positions themselves were absent from the account. Orphaned stop orders were cancelled. SAN, USB, FITB removed from positions_memory.md. KEY pending order d318fee3 expired unfilled. Old CSX pending order 7515d6b3 expired unfilled. Earnings filters: BAC 7/14 (7d), USB 7/16 (9d), KEY 7/21 (14d) — all disqualified. CSX 7/22 (15d) — within margin, qualified. YELLOW signal. Financial sector (BAC, USB) at 52-wk highs. trend_template_batch.py failed (TLS error — 9th consecutive session). Next session: 2026-07-08.)*
