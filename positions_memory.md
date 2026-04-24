# OPEN POSITIONS MEMORY

This file is maintained by the bot. It is updated at the end of every session (Step 6).
A position is added when a new entry is made (Step 5) and removed only when fully closed (Step 3).
The bot reads this file at the start of Step 3 to make correct position management decisions.
This file tracks HISTORY only — current state (price, qty, stop) is always read from Alpaca.

Last updated: 2026-04-24

---

## GOOGL
- **Entry date**: 2026-04-23
- **Entry price**: $342.31
- **Original qty**: 18
- **Setup**: Breakout A
- **Initial stop**: $315.55 (consolidation low)

**Stop history:**
- 2026-04-23: $315.55 — initial stop (entry day)
- 2026-04-24: $315.55 — stop reinstated (was missing from open orders; same price, no change)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-04-24

---

## WMT
- **Entry date**: 2026-04-24
- **Entry price**: $132.45 (consolidation high / Option A trigger)
- **Original qty**: 50
- **Setup**: Breakout A
- **Initial stop**: $122.57 (consolidation low)

**Stop history:**
- 2026-04-24: $122.57 — initial stop (OTO, order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-04-24

---

## HST
- **Entry date**: 2026-04-24
- **Entry price**: $21.54 (consolidation high / Option A trigger)
- **Original qty**: 282
- **Setup**: Breakout A
- **Initial stop**: $19.77 (consolidation low)

**Stop history:**
- 2026-04-24: $19.77 — initial stop (OTO, order pending fill)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: 2026-04-24

---

<!-- TEMPLATE — copy this block when adding a new position:

## [SYMBOL]
- **Entry date**: YYYY-MM-DD
- **Entry price**: $X.XX
- **Original qty**: N
- **Setup**: [Breakout A / Breakout B / EP]
- **Initial stop**: $X.XX (consolidation low / gap day low)

**Stop history:**
- YYYY-MM-DD: $X.XX — initial stop (entry day)

**Partial profits:**
- none

**Total closed**: 0%

**Last updated**: YYYY-MM-DD

-->

---

*(3 open/pending positions as of 2026-04-24: GOOGL (live), WMT (pending fill), HST (pending fill). USB removed — stop_limit day order from 2026-04-23 expired unfilled.)*
