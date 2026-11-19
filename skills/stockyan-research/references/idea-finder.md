# Idea finder

For "which stocks look good", "find undervalued banks", "what's breaking out", "hydropower ma kun ramro".
A single scan is a list, not research. Good ideas come from where independent signals overlap.

## 1. Pin down what the user wants (ask only if it's truly unclear)

- **Style:** value (cheap vs peers), dividend, momentum or breakout, oversold bounce, or "smart money" accumulation.
- **Scope:** a sector, or the whole market. **Horizon:** days to weeks (swing) or months to years (investing).
- If they give no style, default to a balanced screen: fundamentals that are not deteriorating, plus a constructive
  chart, plus net broker buying.

## 2. Cast a wide net with two or three different kinds of screen

Pick screens that look at different things, so an overlap means something:

| Style | Screens |
|---|---|
| Value | `screen_fundamentals(screen: "fundamental", sector, peMax, pbMax, sort: "pe", direction: "asc")` |
| Dividend | `get_market_highlights(kind: "dividend_leaders", sortBy: "yield", sector)` |
| Momentum or breakout | `run_swing_scan(bucket: "breakoutBullish", sector)`, `run_indicator_scan(scanner: "ema_crossover", preset: "golden_cross")`, `get_market_highlights(kind: "near_52_week_high")` |
| Oversold bounce | `run_indicator_scan(scanner: "rsi", zone: "oversold")` or `rsiMin: 30, rsiMax: 40` for "just left oversold", with `divergence: "bullish_divergence"` |
| Money flow | `get_broker_intel(view: "aggressive_accumulators")`, `get_broker_intel(view: "dominance", side: "buyers")`, `get_market_highlights(kind: "trending")` |
| Ready-made | `get_strategy_picks`, `get_trade_lab_picks` (StockYan's own curated lists; say they are StockYan's picks) |

Use `get_scanner_options(scanner)` first if you are unsure of a scanner's valid options. Most scanners are paid: on a
free plan, lean on `get_market_highlights`, `get_top_movers`, `get_sector_performance` and per-stock checks.

## 3. Find the overlap and shortlist

- Keep stocks that appear in at least two different kinds of screen (say value + net broker buying).
- Drop thin stocks: check `get_stock` volume and turnover; a stock that trades a few hundred shares a day is not a
  practical idea for most users.
- Shortlist three to five. Fewer, well-checked ideas beat a list of twenty.

## 4. Quick check on each shortlisted stock

For each one, a light version of the deep dive: `get_stock`, `get_company_financials(limit: 4)`,
`get_technical_summary` (or price history), `get_broker_activity(view: "accumulation", symbol, period: "1M", limit: 5)`.
Write one bull point and one bear point each.

## 5. Write it up

Use the "Idea list" layout in `references/report-templates.md`: a ranked table with why each made the list, the
main risk, and the level or event that would invalidate it. Offer to add them to a watchlist (`update_watchlist`) or
set alerts. Don't do it unasked.
