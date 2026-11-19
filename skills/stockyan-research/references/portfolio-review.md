# Portfolio review

For "review my portfolio", "kun share bechne", "how am I doing". This uses the user's real StockYan portfolio,
which is private: discuss it with them, and never paste it anywhere else.

## 1. Load it

- `get_my_portfolio()`: every portfolio with totals, and the default one's holdings (units, WACC, investment, LTP,
  value, unrealised P/L, today's change). If they have several portfolios, ask which, or review the default.
- `get_my_transactions(limit: 50)` when holding period matters (tax, "how long have I held this").
- `get_my_account()` once, to know which tools their plan includes.

## 2. The health check

1. **Concentration.** Each holding's share of the portfolio value, and each sector's. Flag any single stock above
   about 25% or a sector above about 40%: one bad result or regulation can hit hard.
2. **Winners and losers.** Biggest unrealised gains and losses in rupees and %. StockYan's P/L already includes
   buying costs and estimated selling costs (brokerage, SEBON fee, DP fee, capital gains tax).
3. **Tax timing.** Capital gains tax for individuals is 5% if held 365 days or less and 3.75% after (rates from
   22 Sep 2026). A holding a few weeks short of a year may be worth noting if they plan to sell.
4. **What's changed underneath.** For the largest five to eight holdings by value, run `get_technical_summary` (or
   `analyze_stock_signals`) and `get_broker_activity(view: "distribution", symbol, period: "1M", limit: 5)`. Flag
   holdings where the trend has broken down or brokers are steadily selling.
5. **Upcoming events.** `get_news(symbol)` for the bigger holdings: book closures, AGMs, right shares (which need
   money), and `get_ipo_calendar` for lock-in unlocks.
6. **Idle money and dividends.** Realised P/L and dividends received, if the user asks how the year went.

## 3. Write it up

Use the "Portfolio review" layout in `references/report-templates.md`: overall picture, what's working, what needs
a look (with the reason), and a short list of things to watch. Frame actions as options with trade-offs, for example
"trimming X would cut your bank exposure from 55% to 40%, at the cost of Rs 12,400 tax on the gain". Don't instruct.

Offer useful follow-ups: alerts on stop-loss or target levels (`set_price_alert`), a note on a holding (`save_note`),
or adding a watched replacement to a watchlist. Only on a yes.

## Recording trades

If the user asks you to add a buy or sell they made ("I bought 50 NABIL at 549"), use `add_portfolio_transaction`.
Repeat the details back first (symbol, units, price, date, buy or sell). It's a record in their app, not an order.
