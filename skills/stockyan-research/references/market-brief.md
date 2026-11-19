# Market brief

For "how's the market today", "NEPSE aaja kasto bhayo", a daily or weekly summary. Short and scannable: a busy
trader reads it in thirty seconds.

## Calls (in parallel)

- `get_market_overview`: index, change, turnover, advancers vs decliners, sub-indices, top gainers and losers.
- `get_sector_performance()`: every sector's change and turnover.
- `get_top_movers(type: "turnover", explain: true)`: where the money actually traded, with a read of what the movers have in common.
- `get_market_highlights(kind: "trending")`: unusual activity over recent days.
- `get_news(limit: 8)`: the day's market-moving news (policy, NRB, results season, big IPOs).
- For a weekly brief, use `period: "1W"` on `get_top_movers`, add `get_broker_activity(view: "top_buyers", period: "1W")` (whole market) and
  `get_market_highlights(kind: "near_52_week_high")` and `kind: "near_52_week_low"`.

## Write it up (the "Market brief" layout in report-templates.md)

1. One line: index, change, turnover, and whether breadth agreed (more stocks up than down?).
2. Where the money went: the top two or three sectors by turnover and change.
3. Stand-outs: two or three stocks with a reason (volume spike, 52-week high, news).
4. One line of news that matters.
5. What to watch tomorrow (a level on the index, an event, a results date).

If the market is open, say the numbers are live and will change by the close.
