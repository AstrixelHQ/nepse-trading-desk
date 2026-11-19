# Station 2: Strategy sleeves (several ways to find ideas)

Like a multi-strategy fund, the desk doesn't trust one way of picking stocks. Each sleeve below is an independent
strategy with its own logic. A stock that two different sleeves find is more interesting than one that tops a single
list.

## Running a sleeve

- With Strategy Builder in the user's plan, run the sleeve's rules with `scan_strategy(rules)`: it returns today's
  matches, how many stocks survive each rule, and the "almost" list.
- Without it, use the fallback calls listed per sleeve.
- Respect the regime from station 1: run the favoured sleeves first; in a 🔴 downtrend, run at most two and say ideas
  are for watching or paper trading.

## The sleeves (rules are tested against StockYan's Strategy Builder)

**1. Trend breakout:** strong stocks breaking above resistance on rising volume. Holds weeks.
```json
[{"type":"trend","ma":"ema","fast":20,"slow":50,"when":"above"},{"type":"levels","at":["breakAbove"]},
 {"type":"volume","multiple":1.5,"days":20},{"type":"liquidity","minTurnover":5000000,"days":20}]
```
Fallback: `run_swing_scan(bucket: "breakoutBullish")`, `run_price_action_scan`.

**2. Pullback in an uptrend:** a healthy stock dipping back to its 20-day average. Holds weeks.
```json
[{"type":"trend","ma":"ema","fast":50,"slow":200,"when":"above"},{"type":"priceVsAverage","ma":"ema","period":20,"minPct":-3,"maxPct":1},
 {"type":"rsi","min":40,"max":55},{"type":"liquidity","minTurnover":3000000,"days":20}]
```
Fallback: `run_indicator_scan(scanner: "rsi", rsiMin: 40, rsiMax: 55)` then keep stocks whose technical summary shows
an uptrend.

**3. Oversold bounce:** beaten-down stocks turning up. Short holds (days to two weeks); higher risk.
```json
[{"type":"rsi","zones":["oversold"]},{"type":"priceAction","moves":["strongUp","weakUp"]},
 {"type":"liquidity","minTurnover":3000000,"days":20}]
```
Fallback: `run_indicator_scan(scanner: "rsi", zone: "oversold", divergence: "bullish_divergence")`.

**4. Momentum near the high:** leaders within 5% of their 52-week high with momentum building.
```json
[{"type":"yearRange","at":"nearHigh","withinPct":5},{"type":"trend","ma":"ema","fast":20,"slow":50,"when":"above"},
 {"type":"macd","signals":["above","rising"]},{"type":"liquidity","minTurnover":5000000,"days":20}]
```
Fallback: `get_market_highlights(kind: "near_52_week_high")`.

**5. Smart money:** a few brokers dominating the buying while the trend is up. (Broker rules describe today only,
so this sleeve can't be backtested; say so.)
```json
[{"type":"brokers","side":"buyers","group":5,"minRatio":2,"period":"1W"},{"type":"trend","ma":"ema","fast":20,"slow":50,"when":"above"},
 {"type":"liquidity","minTurnover":3000000,"days":20}]
```
Fallback: `get_broker_intel(view: "aggressive_accumulators")`, `get_broker_intel(view: "dominance", side: "buyers")`.

**6. Value in an uptrend:** cheap on earnings and book value, with the price trend already turning up.
```json
[{"type":"fundamentals","pe":{"max":15},"pb":{"max":2}},{"type":"trend","ma":"sma","fast":50,"slow":200,"when":"above"}]
```
Fallback: `screen_fundamentals(peMax: 15, pbMax: 2, sort: "pe", direction: "asc")`, plus
`get_market_highlights(kind: "dividend_leaders", sortBy: "yield")` for income.

**7. Squeeze breakout:** a quiet stock (narrow Bollinger bands) in an uptrend, often before a big move.
```json
[{"type":"bollinger","signals":["squeeze"]},{"type":"trend","ma":"ema","fast":20,"slow":50,"when":"above"},
 {"type":"liquidity","minTurnover":3000000,"days":20}]
```

**8. Events (judgement, no rule):** results season, AGMs, book closures, right shares, lock-in expiries, NRB policy.
Use `get_news`, `get_ipo_calendar` and `get_company_financials`. Evidence from Nepal suggests prices often fall after
right-share announcements and into book closures, so event ideas are usually reasons to wait or avoid, not to chase.

Narrow any sleeve to a sector by adding `{"type":"sector","sectors":["hydro_power"]}`. Liquidity is average daily
turnover in rupees: Rs 30 lakh to 50 lakh keeps out stocks that are hard to exit.

## Shortlist

1. Collect every sleeve's matches. Note which sleeves found each stock.
2. Rank: found by two or more sleeves first, then by sleeve fit with the regime.
3. Drop stocks under the liquidity floor, and penny or thin-float names where manipulation is common (low paid-up
   capital, a few brokers doing all the trading).
4. Keep 3 to 6 for the analyst team. Fewer, better-checked ideas beat a long list.

Show the user a small map: which sleeves ran, how many each found, which stocks overlapped.
