# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-07-02

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

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-07-02

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

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-06-23

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

## CSX
- **Status**: pending
- **Order ID**: ec422789-ecb2-4545-a9f5-b23c319820d2
- **Entry date**: 2026-07-02
- **Planned entry**: $49.21 (consolidation high / Option A trigger)
- **Planned qty**: 135
- **Setup**: Breakout A
- **Initial stop**: $45.43 (consolidation low)

**Stop history:**
- 2026-07-02: $45.43 — initial stop (order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-07-02

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

*(3 active + 1 pending as of 2026-07-02: FITB (active @ $55.67, unrealized +2.68%, GTC stop $52.30 order 85c1a602 unchanged — below 5% band), SAN (active @ $12.66, unrealized +10.11%, GTC trailing stop updated to $13.63 MA10 order 9d128e71 — in 10-20% band, replaced order 29c06248), USB (active @ $59.80, unrealized +3.23%, GTC stop $55.19 order bf4e765d unchanged — below 5% band), CSX (pending — OTO stop_limit buy 135 shares trigger $49.46 limit $49.70 stop $45.43, order ec422789, expires 2026-07-06). No pending entries to reconcile. Earnings: FITB 7/17 (15d), SAN 7/22 (20d), USB 7/16 (14d) — all outside 2-day exit window. CSX earnings 7/22 (20d) — outside 14-day filter. Watchlist: MRVL and CIFR removed (failed Trend Template); no new adds (RIVN failed TT, MIDDV errored, MRNA gap <8%). 12 symbols remain. trend_template_batch.py failed (TLS/curl error — 7th consecutive session). GREEN signal. Market: Dow all-time high, chip sector selling off, July 3 holiday (markets closed). Next session: 2026-07-07.)*
