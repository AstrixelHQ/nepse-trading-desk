# Example: "What should I buy this week?"

A real, unedited-in-substance run of the NEPSE Trading Desk on live StockYan data, on **19 Nov 2026 around 11:40
Nepal time** (market open, so today's prices were provisional). Example account: **Rs 5,00,000**. About 30 tool calls.
Kept as an example of the output, not as a recommendation: prices have moved since.

---

## In plain words

The market as a whole is **soft**, so the desk keeps most of the money in cash. Banks are the bright spot: they're
the one sector in a clear uptrend, and the setup the desk found ("a healthy stock dipping back to its average") has
actually worked in banks over the past year, though not across the whole market. Two bank ideas pass the checks, both
**only on a small dip**, using about 23% of the account. Two other ideas were rejected, and the report says why.

## 1 · Market regime: is the tide in or out?

```
NEPSE 2,625.76  🟠 Weak tide       2.5% below its 200-day average (2,692.20), which has gone flat
                                   11.3% below its 1-year high (2,960.40) · 112 up / 138 down so far today
Desk rule: keep 20-40% invested, only the strongest setups.

Banking       🟢 Uptrend    8.4% above a rising 200-day average, 2.5% from its 1-year high
Hydropower    🟠 Weak       2.4% below its 200-day average
Microfinance  🔴 Downtrend  6.6% below a falling 200-day average
```

## 2 · Strategy sleeves: four ways to look for ideas

| Sleeve | Stocks found | Notes |
|---|---|---|
| Pullback in an uptrend | 15 | healthy stocks dipping back to their 20-day average |
| Value in an uptrend | 5 | all commercial banks: P/E ≤ 15, P/B ≤ 2, 50-day above 200-day average |
| Smart money | 2 | SHINE, NTC: top 5 brokers buying at least 2× what top sellers sell |
| Trend breakout | 0 | only 3 stocks had a volume spike today |

**Found by two sleeves:** KBL (pullback + value), PCBL (pullback + value), SHINE (pullback + smart money).
**Added:** GBIME, the cheapest value match, because banking is the only sector in an uptrend.

## 3-4 · Analyst team and smart money

| Stock | Fundamentals | Technicals | Smart money | Context | **Desk score** |
|---|---|---|---|---|---|
| GBIME · Global IME Bank | 18 | 17 | 16 | 20 | **71** 🟡 |
| PCBL · Prime Commercial Bank | 11 | 19 | 13 | 18 | **61** 🟡 |
| SHINE · Shine Resunga Dev. Bank | 10 | 11 | 24 | 12 | **57** 🟡 |
| KBL · Kumari Bank | 11 | 14 | 13 | 18 | **56** 🟡 |

(Each analyst scores out of 25. 75+ is strong agreement, 55-74 mixed.)

## 10 · Has this setup worked before?

```
Pullback in an uptrend · held 20 trading days · StockYan backtester

Whole market, last 12 months   605 trades · won 48% · average +0.36% → about −0.6% after ~1% costs · beat NEPSE 47%
Whole market, last 6 months    261 trades · won 54% · average −0.11% → about −1.1% after costs
Banks only, last 12 months      89 trades · won 60% · average +1.56% → about +0.6% after costs · beat NEPSE 71%  🟡

Value in an uptrend · banks · held 40 days   17 trades · won 53% · average −1.10%   🔴 small sample, no edge
```

**What this means:** the dip-buying setup hasn't paid across the whole market, but in banks it has had a modest,
real edge over a usable sample. So the desk only takes it in banks, and doesn't lean on the value sleeve.

---

## Idea 1 · GBIME (Global IME Bank)

```
GBIME · Global IME Bank                       live, 19 Nov 2026 ~11:40
🟡 Leans positive · Confidence ●●○ medium · Desk score 71/100
Plan: wait for a dip to Rs 255-259 · stop Rs 247 · targets Rs 275 / Rs 285 · reward/risk 1.8× / 2.8×

Fundamentals  ▰▰▰▰▰▰▰▱▱▱  18/25  profit per share up 20% on the same quarter last year; cheaper than peers
Technicals    ▰▰▰▰▰▰▰▱▱▱  17/25  steady uptrend, but near its 1-year high and momentum is tiring
Smart money   ▰▰▰▰▰▰▱▱▱▱  16/25  more net buying than selling for a month, still buying last week
Context       ▰▰▰▰▰▰▰▰▱▱  20/25  banking is the one sector in an uptrend; trades about Rs 10 crore a day
```

**The numbers:** price Rs 266.50 · P/E 11.4 (price ÷ yearly profit per share; bank peers' median about 13.9) ·
P/B 1.52 (peers about 1.42) · Q1 2083/84 EPS (profit per share) Rs 23.35 vs Rs 19.51 a year earlier · last year's
dividend 6% cash + 4% bonus · 85% of the way up its 52-week range (Rs 218.90 to Rs 275).

**Who's buying (7 Oct to 18 Nov, 21 trading days):** Dynamic Money Managers (44) net +5.47 lakh shares, Sun
Securities (64) +3.80 lakh, Dipshikha (38) +3.18 lakh, together about 16% of all shares traded. Against them, Shree
Krishna (28), ABC (17) and Naasa (58) each net sold about 3 to 3.5 lakh. Last week Imperial (45) added +2.64 lakh.

**Why it could work**
- Profit is growing (EPS +20% on the same quarter last year) and it's cheaper than most bank peers on earnings.
- It's in the strongest sector, with a run of higher lows since August (Rs 228.85 → Rs 262.40).
- Banks bought on this kind of dip won 60% of the time in the past year and beat NEPSE 71% of the time.

**Why it could fail**
- The strongest bull point, the uptrend, is already stretched: price is 3% under its 52-week high and RSI (a 0-100
  momentum gauge) is rising less than the price, a sign the move is tiring. Buying here leaves little room.
- Brokers aren't one-sided: three big brokers sold almost as much as the top three bought.
- The overall market tide is weak; if NEPSE slides, banks rarely escape.

**The one fact that would flip it:** a close below Rs 252.71 (support touched 6 times) breaks the uptrend.

```
Rs 285  ─── Target 2 (monthly pivot)            +10.9%
Rs 275  ─── Target 1 (52-week high)              +7.0%
Rs 266.5 ◀── now (don't chase)
Rs 259  ┐
        ├── Entry zone: wait for a dip (Fibonacci level Rs 257.37)
Rs 255  ┘
Rs 247  ─── Stop: the idea is wrong below here   −3.9%
```

With Rs 5 lakh: **250 shares (about Rs 64,250)**. If the stop is hit you lose about **Rs 2,500** (0.5% of the account,
the desk's size in a weak market) plus about Rs 500 in costs. At target 1 you'd gain about Rs 4,500 before costs and
tax; at target 2, about Rs 7,000.

**Risk desk:** ✅ regime ✅ reward/risk (at the dip) ✅ liquidity ✅ gap risk ✅ concentration ⚠️ mixed broker flow
⚠️ near the 52-week high → **approved with a change: only on a dip to Rs 255-259.** If it instead closes above Rs 275,
re-run the desk: that's a different (breakout) trade.

## Idea 2 · PCBL (Prime Commercial Bank)

```
PCBL · Prime Commercial Bank                  live, 19 Nov 2026 ~11:40
🟡 Mixed · Confidence ●○○ low · Desk score 61/100
Plan: entry near Rs 264-266 · stop Rs 252 · targets Rs 287 / Rs 296 · reward/risk 1.7× / 2.4×

Fundamentals  ▰▰▰▰▱▱▱▱▱▱  11/25  cheap on earnings, but profit per share fell 13% on last year's Q1
Technicals    ▰▰▰▰▰▰▰▰▱▱  19/25  clean uptrend: higher highs and lows since July
Smart money   ▰▰▰▰▰▱▱▱▱▱  13/25  more buyers than sellers, but small next to total volume
Context       ▰▰▰▰▰▰▰▱▱▱  18/25  banking uptrend; trades about Rs 6.5 crore a day
```

**The numbers:** price Rs 270.90 · P/E 11.95 · P/B 1.50 · Q1 EPS Rs 22.67 vs Rs 25.94 a year earlier (results
filed 17 Nov) · last dividend mostly bonus (8% bonus + 0.42% cash) · support Rs 264.73, resistance Rs 286.80
(52-week high).

**Why it could work:** a textbook uptrend (lows from Rs 227.10 in July to Rs 266 in late October), cheaper than peers on
earnings, in the leading sector, and it was one of the recent winners of this exact setup (+10.4% from 9 Sep).
**Why it could fail:** the strongest point, cheapness, rests on earnings that just fell 13% on the year; and the broker
buying is small (top three about 8% of volume) while Vision (34) net sold 2.08 lakh shares.

```
Rs 296  ─── Target 2 (monthly pivot)            +11.7%
Rs 287  ─── Target 1 (52-week high)              +8.2%
Rs 270.9 ◀── now
Rs 266  ┐
        ├── Entry zone (support Rs 264.73)
Rs 264  ┘
Rs 252  ─── Stop                                 −4.9%
```

With Rs 5 lakh: **190 shares (about Rs 50,350)**. Stop hit: about **Rs 2,470** lost. Target 1: about Rs 4,140 gained
before costs and tax.

**Risk desk:** ✅ regime ✅ reward/risk (at the entry zone) ✅ liquidity ✅ gap risk ✅ concentration ⚠️ earnings fell
on the year → **approved with a change: only near support, and smaller conviction.**

## Not taken

**SHINE (Shine Resunga Development Bank), score 57: watch or paper-trade only.** The broker buying is real and
one-sided (NIMB (75), Miyo (66) and Sharepro (65) bought about 2.6 lakh shares, roughly half of everything traded in a
month), but it's a thin stock where a few brokers can move the price. It's also expensive (P/E 27.4, P/B 2.84), and
the desk had no sector trend or same-quarter earnings comparison for it. The bank backtest doesn't cover development
banks.

**KBL (Kumari Bank), score 56: vetoed.** At Rs 232 the first target (Rs 244.27) is too close for the risk (reward/risk
1.3, below the desk's 1.5 floor), short-term momentum just turned down (9/20-day averages crossed down on 17 Nov),
profit per share was flat on the year (+1.7%), and it paid only 2.11% cash last year.

## 7 · The portfolio

```
GBIME (on a dip)   ███░░░░░░░░░░░░░  12.9%   Rs 64,250
PCBL  (on a dip)   ██░░░░░░░░░░░░░░  10.1%   Rs 50,350
Cash               ████████████░░░░  77.1%   Rs 3,85,400
```

Both are banks: 23% in one sector, within the 30% limit and inside the 20-40% the weak tide allows. If both stops hit,
the account loses about Rs 5,000 (1%). Nothing is placed automatically: ask the desk to set it up in your paper
account, with alerts at the stops and targets, if you want to follow it.

**What to watch:** NEPSE reclaiming its 200-day average (Rs 2,692) would raise the allowed exposure · GBIME at
Rs 255-259 or above Rs 275 · PCBL at Rs 264 · a close below Rs 252.71 (GBIME) or Rs 252 (PCBL) ends the idea.

---

Sources: StockYan · start_research_session, get_market_regime (NEPSE, banking, hydro_power, microfinance),
scan_strategy (4 sleeves), get_stock, get_company_financials, find_comparable_stocks, get_technical_summary,
get_broker_activity (1 month, 1 week), get_news, backtest_strategy (4 runs) · live data, 19 Nov 2026 ~11:40 NPT.
Research from live StockYan data, not investment advice. Past results don't guarantee future ones.
