# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-07-09

---

## FITB
- **Status**: active
- **Entry date**: 2026-06-25 (fill confirmed 2026-07-08 — reconstructed from Alpaca data after 2026-07-07 anomaly removed this entry)
- **Entry price**: $55.67 (actual — Alpaca avg_entry_price)
- **Original qty**: 166 (actual filled qty)
- **Setup**: Unknown (entry details lost during 2026-07-07 anomaly; reconstructed)
- **Initial stop**: $52.30 (reconstructed from 2026-07-07 session note)

**Stop history:**
- 2026-07-07: $52.30 — initial stop (reconstructed from anomaly note; original stop order 85c1a602 was cancelled that session due to zero-position anomaly)
- 2026-07-08: $52.30 — GTC stop reinstated (order de89aa55-9836-4119-a81c-0d42bec692a9, 166 shares; stop was absent — safety net triggered by Step 3d)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-07-09

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

*(1 active as of 2026-07-09: FITB (active — 166 shares, entry $55.67, GTC stop $52.30 order de89aa55, earnings 2026-07-17). No position changes today. All Option A setups (KEY, BAC, CSX) discarded — earnings within 14 days (BAC Jul 14, KEY Jul 21, CSX Jul 22). trend_template_batch.py failed TLS again (11th consecutive session). MU added to watchlist. Next session: 2026-07-10. CRITICAL: FITB earnings 2026-07-17, must close by 2026-07-15 (session on 2026-07-15 has next_open_2=2026-07-17).)*
