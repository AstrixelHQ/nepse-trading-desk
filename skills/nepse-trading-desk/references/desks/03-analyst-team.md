# Station 3: Analyst team and the confluence score

Four analysts look at each shortlisted stock independently. Each gives a score out of 25 with one plain sentence.
Their total is the **confluence score** (out of 100): how much the different kinds of evidence agree.

## Calls per stock (in parallel)

`get_stock`, `get_company_financials(limit: 8)`, `find_comparable_stocks(limit: 6)`, `get_technical_summary`,
`get_broker_activity(view: "accumulation" and "distribution", period: "1M", limit: 8)`, `get_news(limit: 6)`,
`get_market_regime(index: <its sector>)`. Add `analyze_stock_signals` if you need more scanner detail.

## 1. Fundamentals analyst (0-25)

- **Earnings trend (0-10):** NEPSE quarterly EPS is already annualised, so never multiply by 4. Compare the same quarter
  a year earlier first (Q1 vs last year's Q1), then the sequence. Rising on the year = 7-10, flat = 4-6, falling = 0-3.
  A one-quarter jump may be a one-off; check the profit amount.
- **Valuation vs peers (0-10):** P/E and P/B against the peers' median (compute it). Cheaper on both = 8-10; cheaper on
  one, richer on the other = 4-7, and say which; richer on both = 0-3. Cheap with falling earnings is not cheap.
- **Shareholder returns (0-5):** steady cash dividends over 3 to 5 years = 4-5; bonus-only or none = 0-2. Cash yield ≈
  cash % × face value (usually Rs 100) ÷ price.
- Book value per share drops right after a book closure (dividends paid, bonus shares added); that is not a loss.

## 2. Technical analyst (0-25)

- **Trend (0-10):** price above rising 20/50-day averages with higher lows = 8-10; sideways = 4-6; below falling
  averages = 0-3.
- **Momentum (0-8):** RSI 50-70 and MACD above its signal = 6-8; mixed = 3-5; RSI over 75 (stretched) or below 40
  falling = 0-2. A bearish divergence takes off 2.
- **Room to run (0-7):** distance to the next resistance vs distance to the nearest support. More room above than
  below = 5-7.
- `get_technical_summary` already gives a 0-100 score and bias; use it as a cross-check, not a substitute.

## 3. Flow analyst (0-25)

See `04-smart-money.md` for how to read the data.
- **Direction (0-10):** net accumulation over a month = 7-10; balanced = 4-6; net distribution = 0-3.
- **Scale (0-8):** top net buyers' quantity as a share of the month's total volume: 25% or more = 6-8, 10-25% = 3-5,
  under 10% = 0-2.
- **Persistence (0-7):** buying in both the last week and the last month, not one big day = 5-7.

## 4. Context analyst (0-25)

- **Sector tide (0-10):** the sector's regime from `get_market_regime(index: sector)`. Uptrend = 8-10 … downtrend = 0-2.
- **Events (0-10):** fresh good results or a dividend ahead = 7-10; nothing = 5; a right share, lock-in expiry,
  regulator action or poor results = 0-3.
- **Liquidity (0-5):** daily turnover comfortably above the sleeve floor = 4-5.

## Reading the score

| Score | Light | Meaning |
|---|---|---|
| 75-100 | 🟢 | Strong agreement across lenses |
| 55-74 | 🟡 | Mixed: one or two lenses disagree |
| 0-54 | 🔴 | Weak or conflicting evidence |

Show it as bars, one per analyst (see `report-design.md`), each with its one-sentence reason. If a lens has no data,
mark it "not available", score it 0 and say the total is incomplete.
