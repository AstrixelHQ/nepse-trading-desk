# Investor lenses (optional)

When the user asks how a style of investor would judge a stock, run that style's checklist against StockYan data.
These are stylised summaries of well-known public approaches, not the real people's views, and not endorsed by them.
Say so in one line. Score each check pass, fail or not available, then give an overall lean with a confidence.

## Value, quality first (Buffett-style)

1. **Understandable business:** can you describe how it earns money in one sentence?
2. **Durable advantage:** market position against peers (`find_comparable_stocks`): size, consistent EPS.
3. **Profitability:** EPS steady or rising over several years (`get_company_financials`, same quarter year on year).
4. **Financial strength:** for banks, book value growth and no sharp EPS collapses; for others, profit consistency.
5. **Shareholder returns:** a record of cash dividends, not only bonus shares.
6. **Price:** P/E and P/B against its own history and peers; is there a margin of safety?

## Deep value (Graham-style)

1. P/E at or below about 15, and P/E × P/B at or below about 22.5.
2. Earnings positive in each of the last several years.
3. An unbroken dividend record.
4. Price near the low end of its 52-week range, without a collapse in earnings explaining it.

## Growth at a fair price (Lynch-style)

1. EPS growth rate, same quarter year on year and across recent years.
2. PEG ≈ P/E ÷ EPS growth %. Below 1 is attractive, above 2 is expensive.
3. Is the growth from the core business, or one-offs?
4. Is the market already crowded into it? (`get_market_highlights(kind: "trending")`, broker flow)

## Flow and momentum (a NEPSE trader's lens)

1. Trend: higher lows and price above rising moving averages (`get_technical_summary`).
2. Money: steady net broker accumulation over a month, large as a share of volume (`references/broker-flow.md`).
3. Room: distance to resistance and to the 52-week high; is there space before supply?
4. Liquidity: enough daily turnover to get in and out.
