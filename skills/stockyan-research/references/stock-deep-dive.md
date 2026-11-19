# Stock deep dive

For "tell me about X", "is X a good buy", "X ko analysis garnus". Gather all four lenses, then judge
(see the analyst-team method in SKILL.md). Fetch in parallel where the calls don't depend on each other.

## 1. Snapshot

- `get_stock(symbol)`: price, change, volume, EPS, P/E, book value, P/B, market cap, 52-week range, promoter vs
  public shares, lock-in unlock date, recent dividends.
- Note where the price sits in its 52-week range ((LTP − low) ÷ (high − low)). Near the high and near the low
  read very differently.

## 2. Fundamentals lens

- `get_company_financials(symbol, include: "all", limit: 8)`: the last 6 to 8 quarters.
  - **EPS trend:** NEPSE quarterly reports state EPS already annualised, so never multiply by 4. Quarters are
    seasonal (Q1 is often the weakest), so compare **the same quarter a year earlier** first ("Q1 33.89 vs Q1 last
    year 25.49, +33%"), then the sequence. Watch for a single-quarter jump (one-off gain, provision write-back).
  - **Net worth per share (book value)** trend: growing book value is the quiet sign of a healthy bank or insurer. It
    drops right after a book closure because cash dividends leave and bonus shares add units, so check the dividend
    history before reading a fall as losses.
  - **Dividends:** the last 3 to 5 years of cash % and bonus %. Cash dividend yield ≈ (cash % × face value) ÷ LTP,
    where face value is usually Rs 100. A bonus dilutes EPS; a right share asks holders for money.
- `find_comparable_stocks(symbol, limit: 6)`: P/E and P/B against the closest peers in its sector. Compute the peers'
  median for each and say how far the stock sits from it. A P/E well below peers is either value or a warning
  (falling profit, bad loans); check the EPS trend before calling it cheap. When P/E and P/B disagree (cheap on
  earnings, rich on book value), say so: it usually means high return on equity, or earnings that won't last.
- Sector norms differ: banks and insurers are judged on P/B and book value growth; hydropower on project status,
  debt and seasonality; microfinance on asset quality news. Don't compare a hydro's P/E with a bank's.

## 3. Technicals lens

- `get_technical_summary(symbol)`: overall score and bias, RSI, MACD, moving averages, support and resistance,
  pivots, Fibonacci levels, candlestick and broker dominance in one call (paid).
- `analyze_stock_signals(symbol)` (paid) adds scanner-by-scanner signals; add aspects such as
  `["swing", "support_resistance", "candlestick"]` when levels matter.
- `get_price_history(symbol, timeframe: "daily", limit: 120)`: check the summary by eye. Note the trend over 1, 3
  and 6 months, the biggest drop from a recent high, and whether volume rose on up days or down days.
- Free plan fallback: use `get_price_history` alone and describe the trend, highs and lows, and volume plainly.
- Prices in StockYan are adjusted for bonus and right shares, so a big "drop" on a book-closure date is not a crash;
  check the dividend history before calling one.

## 4. Money-flow lens (NEPSE's edge)

- `get_broker_activity(view: "accumulation", symbol, period: "1M", limit: 10)` and
  `view: "distribution"`: which brokers net bought or net sold, with average rates. Strong one-sided buying by a few
  brokers over weeks matters more than one day's noise.
- Put it in scale: compare the top net buyers' combined net quantity with the period's total volume (average daily
  volume from `get_technical_summary` × trading days in the range). Net buying of 5% of volume is noise; 25% or more
  is a real footprint.
- `get_broker_activity(view: "top_buyers" | "top_sellers", symbol, period: "1W")`: the biggest gross buyers and sellers
  of this stock by amount.
- `get_bulk_transactions(symbol)`: block trades on the latest day.
- Read `references/broker-flow.md` for how to interpret this without overclaiming.

## 5. Context lens

- `get_sector_performance(sector)`: is the whole sector moving, or just this stock?
- `get_news(symbol, limit: 8)`: AGM, dividend announcement, book closure, right share, quarterly result, regulatory news.
- `get_ipo_calendar`: lock-in unlocks (promoter shares becoming sellable) and right issues for this company.
- `get_seasonality(symbol)` only as colour, never as a reason on its own; say past patterns don't guarantee anything.

## 6. Judge and write

Follow the analyst-team passes in SKILL.md and the "Stock report" layout in `references/report-templates.md`.
Before you finish, re-read every number in your draft and make sure each one came from a tool output above.

## Common mistakes to avoid

- Calling a stock cheap on P/E alone when EPS is falling or the last quarter had a one-off gain.
- Treating one day of broker buying as "accumulation".
- Quoting RSI or MACD without the trend: RSI 30 in a strong downtrend is not a buy signal by itself.
- Forgetting liquidity: a thinly traded stock can be impossible to exit at the shown price.
