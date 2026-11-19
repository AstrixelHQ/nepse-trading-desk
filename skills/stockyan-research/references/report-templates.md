# Report layouts

Use these as shapes, not forms: drop a section that has nothing in it, and keep the whole thing as short as the
question deserves. Numbers always carry their date. Everything in angle brackets is a placeholder: fill it from
tool output, never from these examples.

## Stock report

```
## <SYMBOL> — <leans positive | mixed | leans negative>, <high | moderate | low> conviction
Two or three sentences: the verdict, the main reason, the main risk.

| | Value | Note |
|---|---|---|
| Price (<date> close) | Rs <LTP> | <x>% of 52-week range |
| P/E · P/B | <pe> · <pb> | peers' median P/E <peer pe> |
| EPS trend (last 4 quarters) | <oldest> → <latest> | <rising / flat / falling> |
| Broker flow (1 month) | <net buying / selling>, top 3 = <x>% | <steady / one-off> |

**Fundamentals** — one or two lines. **Technicals** — one or two lines. **Money flow** — one or two lines.
**Context** — one or two lines.

**Bull case:** 2 or 3 bullets, each with its evidence.
**Bear case:** 2 or 3 bullets, each with its evidence.
**Risks:** liquidity, events, band, lock-in.

**What to watch:** support Rs <level> · resistance Rs <level> · <next event and date>.

Sources: StockYan get_stock, get_company_financials, find_comparable_stocks, get_technical_summary,
get_broker_activity (data to <date>).
Research from StockYan data, not investment advice.
```

## Idea list

```
## <N> <sector> stocks that are <screen 1> and <screen 2> (<date> close)
One line on how they were found (which screens overlapped).

| # | Stock | Why it made the list | Main risk | Invalidated if |
|---|---|---|---|---|
| 1 | <SYMBOL> | <evidence from two screens> | <the main risk> | <level or event> |

Offer: add these to a watchlist or set alerts?
```

## Portfolio review

```
## Your portfolio: Rs <value>, <+/-x>% overall (<live | close>, <date time>)
Two lines: the overall picture and the one thing most worth attention.

**Working:** ...  **Needs a look:** holding — the reason (trend broke below 50-day average; brokers net selling).
**Concentration:** <sector> <x>% of value; top holding <x>%.
**Coming up:** book closure, right share, lock-in dates.
**Options to consider:** framed with trade-offs, not instructions.
```

## Market brief

```
## NEPSE <index> (<change>%) · turnover Rs <x> arba · <up> up / <down> down (<date>)
- Money went to: <sectors with share of turnover>
- Stand-outs: <SYMBOL> <change>% on <x>× volume; ...
- News: <one line>
- Watch tomorrow: <index level or event>
```
