# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-07-06

---

## SAN
- **Status**: active
- **Entry date**: 2026-06-11 (fill confirmed 2026-06-12)
- **Entry price**: $12.66 (actual — Alpaca avg_entry_price)
- **Original qty**: 729 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $11.91 (consolidation low)

**Stop history:**
- 2026-06-11: $11.91 — initial stop (order pending fill)
- 2026-06-12: $11.91 — GTC stop reinstated (OTO leg expired as DAY order, order e651530b)
- 2026-06-16: $12.66 — breakeven stop (unrealized_pl_pct 6.4%, replaced order e651530b → 29c06248)
- 2026-07-02: $13.63 — trailing stop at MA10 (unrealized_pl_pct 10.11%, replaced order 29c06248 → 9d128e71)
- 2026-07-06: $13.71 — trailing stop at MA10 (unrealized_pl_pct 13.51%, replaced order 9d128e71 → 1c73fed1)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-07-06

---

## USB
- **Status**: active
- **Entry date**: 2026-06-22 (fill confirmed 2026-06-23)
- **Entry price**: $59.80 (actual — Alpaca avg_entry_price)
- **Original qty**: 118 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $55.19 (consolidation low)

**Stop history:**
- 2026-06-22: $55.19 — initial stop (order pending fill)
- 2026-06-23: $55.19 — GTC stop reinstated (OTO leg expired as DAY order, order bf4e765d)
- 2026-07-06: $59.80 — breakeven stop (unrealized_pl_pct 5.07%, replaced order bf4e765d → 25cf72eb)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-07-06

---

## FITB
- **Status**: active
- **Entry date**: 2026-06-24 (fill confirmed 2026-06-25)
- **Entry price**: $55.67 (actual — Alpaca avg_entry_price)
- **Original qty**: 166 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $52.30 (consolidation low)

**Stop history:**
- 2026-06-24: $52.30 — initial stop (order pending fill)
- 2026-06-25: $52.30 — GTC stop reinstated (OTO leg expired as DAY order, order 85c1a602)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-25

---

## KEY
- **Status**: pending
- **Order ID**: d318fee3-891c-4d26-a7d9-499378359bb7
- **Entry date**: 2026-07-06
- **Planned entry**: $23.71 (consolidation high / Option A trigger)
- **Planned qty**: 438
- **Setup**: Breakout A
- **Initial stop**: $22.70 (consolidation low)

**Stop history:**
- 2026-07-06: $22.70 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-07-06

---

## CSX
- **Status**: pending
- **Order ID**: 7515d6b3-520d-4fbc-b10c-52183902a848
- **Entry date**: 2026-07-06
- **Planned entry**: $49.27 (consolidation high / Option A trigger)
- **Planned qty**: 140
- **Setup**: Breakout A
- **Initial stop**: $45.58 (consolidation low)

**Stop history:**
- 2026-07-06: $45.58 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-07-06

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

*(3 active + 2 pending as of 2026-07-06: FITB (active @ $55.67, unrealized +3.99%, GTC stop $52.30 order 85c1a602 unchanged — below 5% band), SAN (active @ $12.66, unrealized +13.51%, GTC trailing stop updated to $13.71 MA10 order 1c73fed1 — in 10-20% band, replaced order 9d128e71), USB (active @ $59.80, unrealized +5.07%, GTC breakeven stop updated to $59.80 order 25cf72eb — in 5-10% band, replaced order bf4e765d), KEY (pending — OTO stop_limit buy 438 shares trigger $23.83 limit $23.95 stop $22.70, order d318fee3, expires 2026-07-07), CSX (pending — OTO stop_limit buy 140 shares trigger $49.52 limit $49.76 stop $45.58, order 7515d6b3, expires 2026-07-07). Previous CSX order ec422789 expired unfilled 2026-07-06 (was trigger $49.46, expires noted as 2026-07-06). Earnings: FITB 7/17 (11d), SAN 7/22 (16d), USB 7/16 (10d) — all outside 2-day exit window. KEY 7/21 (15d), CSX 7/22 (16d) — outside 14-day entry filter. C (Citigroup) discarded: earnings 7/14 (8d, within 14-day filter). trend_template_batch.py failed (TLS/curl error — 8th consecutive session). GREEN signal. Nasdaq climbing, tech rebound. Next session: 2026-07-07.)*
