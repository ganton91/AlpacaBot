# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-05-26

---

## ERIC
- **Status**: active
- **Entry date**: 2026-05-04 (fill confirmed 2026-05-05)
- **Entry price**: $12.02 (actual — Alpaca avg_entry_price)
- **Original qty**: 576 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $11.04 (consolidation low)

**Stop history:**
- 2026-05-04: $11.04 — initial stop (OTO, order pending fill)
- 2026-05-05: $11.04 — GTC stop reinstated (OTO leg expired as DAY order, order 483923c0)
- 2026-05-13: $12.02 — breakeven stop (unrealized +6.11%, order e01e9a00)
- 2026-05-21: $12.62 — MA10 trailing stop (unrealized +10.86%, order a061c424)
- 2026-05-22: $12.79 — MA10 trailing stop (unrealized +12.35%, order 9c2b75d3)
- 2026-05-26: $12.91 — MA10 trailing stop (unrealized +14.75%, order 68f657df; replaced 9c2b75d3 which was stuck in PENDING_REPLACE — auto-resolved)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-05-26

---

## HPE
- **Status**: active
- **Entry date**: 2026-05-04 (fill confirmed 2026-05-05)
- **Entry price**: $29.78 (actual — Alpaca avg_entry_price)
- **Original qty**: 219 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $27.34 (consolidation low)

**Stop history:**
- 2026-05-04: $27.34 — initial stop (OTO, order pending fill)
- 2026-05-05: $27.34 — GTC stop reinstated (OTO leg expired as DAY order, order aaa3c7c2)
- 2026-05-13: $30.07 — MA10 trailing stop (unrealized +12.79%, order 6dc0fbf3)
- 2026-05-14: $30.60 — MA10 trailing stop updated (unrealized +14.62%, order af6fed79)
- 2026-05-15: $31.06 — MA10 trailing stop updated (unrealized +10.95%, order 2dd239e6)
- 2026-05-18: $31.48 — MA10 trailing stop updated (unrealized +11.15%, order 8330196b)
- 2026-05-20: $32.08 — MA10 trailing stop updated (unrealized +13.7%, order e49bb48a)
- 2026-05-21: $32.51 — MA10 trailing stop updated (unrealized +14.17%, order 83894864)
- 2026-05-22: $32.51 — stop replaced to 147 shares (order bfe2eb7c; original order 83894864 stuck in PENDING_REPLACE)
- 2026-05-26: No stop update — MA20 ($31.66) is lower than last stop ($32.51); stop unchanged at bfe2eb7c

**Partial profits:**
- 2026-05-26: 72 shares sold at market (~$38.16), 33% of original qty 219 (order 21cc9d9b, DAY — fills tomorrow)

**Total closed**: 33%

**Last updated**: 2026-05-26

---

## SLB
- **Status**: active
- **Entry date**: 2026-05-15 (fill confirmed 2026-05-18)
- **Entry price**: $57.23 (actual — Alpaca avg_entry_price)
- **Original qty**: 119 (actual filled qty)
- **Setup**: Breakout A
- **Initial stop**: $52.76 (consolidation low)

**Stop history:**
- 2026-05-15: $52.76 — initial stop (OTO, order pending fill)
- 2026-05-18: $52.76 — GTC stop reinstated (OTO leg expired as DAY order, order 937f3d3c)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-05-18

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

**Last updated**: 2026-05-22

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

*(4 active positions as of 2026-05-26: ERIC (active, stop updated to $12.91 MA10, order 68f657df), HPE (active, 28.14% unrealized; partial profit of 72 shares placed as DAY market sell order 21cc9d9b fills tomorrow; stop bfe2eb7c @ $32.51 for 147 shares — MA20 $31.66 would be lower so stop unchanged), SLB (active, no changes), AAPL (active, no changes). KMI CLOSED — stagnant rule: 11 days open, +1.92% 10d change; stop cancelled b19d946c, close order d45fad17 placed DAY fills tomorrow.)*
