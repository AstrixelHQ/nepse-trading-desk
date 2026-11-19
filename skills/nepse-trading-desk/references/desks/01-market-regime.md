# Station 1: Market regime (is the tide in or out?)

Most NEPSE stocks rise and fall with the index. A great stock in a falling market usually still falls, so the desk
decides first how much of the account should be invested at all.

## Calls (in parallel)

- `get_market_regime()`: NEPSE against its 50- and 200-day averages, the 200-day's direction, drawdown from the
  1-year high, today's breadth (stocks up vs down), a regime label and a suggested invested share.
- `get_market_regime(index: <sector>)` for the sector of any stock you're considering (banking, hydro_power...).
- `get_sector_performance()` and `get_market_overview()` for today's picture.
- Optional colour: `get_seasonality("nepse")` (always say past months don't predict the next one).

## The regime table (the whole desk obeys it)

| Regime | What it means in plain words | Invested share for a trading account | Which sleeves to favour |
|---|---|---|---|
| 🟢 Uptrend | Tide is in: index above a rising 200-day average | 80-100% | Trend breakout, momentum, pullback |
| 🟡 Mixed | Above the average but the trend is flat or tiring | 50-70% | Pullback, value, smart money |
| 🟠 Weak | Below the average, not yet falling hard | 20-40% | Only top-scoring ideas; value, dividends |
| 🔴 Downtrend | Below a falling 200-day average | 0-20% | Mostly cash; paper-trade ideas instead |

Adjust one step down if breadth is poor (decliners more than twice advancers) or the index is more than 15% below its
1-year high, and say why.

## What to tell the user

One line with an emoji light and the number that matters: "🟡 Mixed tide: NEPSE 2,625 is 2% above its 200-day
average, but that average has stopped rising. The desk keeps about 50-70% invested and is picky." Then let the rest of
the desk use this to size and filter.
