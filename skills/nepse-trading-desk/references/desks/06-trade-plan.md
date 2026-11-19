# Station 6: Trade plan (entry, stop, target, size)

A trade plan turns a view into something the user can check. It is a plan the user may follow if *they* decide to
act, never an instruction. Read `../nepse-basics.md` for costs and the price band first.

## The parts

**1. Entry zone.** Prefer a zone near support or the 20-day average, not the day's high. Breakout sleeves can use
"above the breakout level after a close above it". Give a range: "Rs 532 to Rs 540".

**2. Stop (where the idea is wrong).** Just below the nearest real support or the last swing low under the entry
(from `get_technical_summary` levels), **but never closer than 1.5 × ATR to the entry** (ATR = the stock's typical
daily range; `get_technical_summary` gives it). If the support is closer than that, use entry − 1.5 × ATR, so normal
daily wiggle doesn't stop you out. If the nearest support is more than 3 × ATR away, the setup is too loose: wait for a
better entry. Say it as a closing rule: "exit if it closes below Rs 247".

If the reward-to-risk is poor at today's price, don't force it: find the entry where it works (a dip to support or
a Fibonacci level, or a close above resistance) and make the plan conditional on that ("wait for a dip to Rs 255-259").

**3. Targets.** Target 1 at the next resistance; target 2 at the 52-week high or the next level above. Compute the
**reward-to-risk** = (target − entry) ÷ (entry − stop). The desk wants at least **2.0** to target 1 or 2. Below 1.5,
the risk desk will usually veto.

**4. Position size: risk first, then caps.** Ask for the account size if you don't know it; otherwise show sizes for
an example Rs 5 lakh account and say so.

```
Risk per trade = 1% of the account (0.5% for small or thin stocks, low confidence, or a 🟠/🔴 regime)
Shares         = (account × risk %) ÷ (entry − stop)
```

Then apply the caps and use the **smallest** result:

| Cap | Why | Limit |
|---|---|---|
| Gap cap | A stock can fall the full 15% band in one day and jump past any stop | A 15% fall in this position costs at most 2% of the account: position ≤ about 13% of the account |
| Liquidity cap | You must be able to get out | Position ≤ 10% of the stock's average daily turnover (5% for thin stocks) |
| Regime cap | The tide decides total exposure | Fits inside the invested share from station 1 |
| Lot | NEPSE trades in board lots | Round down to a multiple of 10 shares |

**5. Costs.** Round trip is roughly 0.8% to 1% (brokerage, SEBON fee, DP fee) plus capital gains tax on a profit
(5% if held a year or less). Show the break-even price: entry × 1.01 is a fair rule of thumb.

**6. Time stop.** If a swing trade hasn't moved toward target 1 within about 20 trading days, the plan says to
re-check it.

## Show it as a price ladder

A worked example with round numbers (an illustration of the method, not a real stock):

```
Rs 580  ─── Target 2 (52-week high)          +16%
Rs 540  ─── Target 1 (next resistance)        +8%
Rs 500  ◀── Entry (near support)
Rs 480  ─── Stop: exit on a close below       −4%
```

- Reward-to-risk to target 1: (540 − 500) ÷ (500 − 480) = **2.0** ✓
- Account Rs 5,00,000, risk 1% = Rs 5,000 → 5,000 ÷ 20 = 250 shares (Rs 1,25,000, a quarter of the account)
- Gap cap: at most about 13% of the account = Rs 65,000 → **130 shares**. The gap cap is the smallest, so it wins.
- In rupees: if the stop is hit, about **Rs 2,600** lost (0.5% of the account). At target 1, about **Rs 5,200** gained
  before costs and tax (about Rs 4,500 after brokerage, fees and 5% tax).

Always end the plan with that rupee line: beginners understand "you could lose about Rs 2,600" far better than ratios.
