# Station 10: Backtest (has this setup worked before?)

A setup that looks good today may have failed most of the time in the past. The desk checks.

## With Strategy Builder in the plan

Run the sleeve's rules with `backtest_strategy(rules, holdDays, period: "1Y")`. Match `holdDays` to the trade's
horizon (5 or 10 for bounces, 20 for swings, 40 for trends). Add the stock's sector rule to test it where it trades.
Broker and fundamentals rules are skipped by the backtest (they describe today only); say so.

Read the result like this:

| Number | What it tells the user |
|---|---|
| `trades` | How much evidence there is. Under 10 = anecdote, 10-29 = weak, 30+ = usable |
| `winRate` | How often a trade ended up |
| `avgReturn`, `medianReturn` | Typical result; a big gap between them means a few big wins carry it |
| `beatMarketRate` | How often it did better than simply holding NEPSE |
| `worst` | The pain to be ready for |

The engine's returns are before costs: subtract about 1% per trade for the round trip. If the average return after
that is near zero, the setup has no real edge, whatever the win rate says.

Split check, when the sample allows: re-run with `period: "6M"` and compare with `"1Y"`. If the edge flips sign in
the recent half, it may have stopped working.

## Without Strategy Builder

Use `get_price_history(symbol, limit: 400)` and look back through the stock's own history for the same setup (for
example, "RSI under 30 then an up day"). For each past case, note the price 10 and 20 trading days later. Report how
many cases, how many ended higher, and the typical result, and label it "a rough look at N past cases in this one
stock". If you can run code, compute it; otherwise go through the cases by eye and say so.

## Pitfalls to name when relevant

Small samples, the strategy chosen *because* it looked good (try several and one will look good by luck), stocks that
merged or delisted aren't in today's list, and prices that hit the 15% band couldn't actually be traded at.

## Show it simply

```
Backtest: pullback in an uptrend · banks · held 20 days · last 12 months
Trades 42 · Won 26 (62%) · Typical result +2.1% (after ~1% costs: +1.1%) · Beat NEPSE 57% of the time
Verdict: 🟡 a modest edge with a usable sample
```
(Illustrative layout; fill it from the tool.)
