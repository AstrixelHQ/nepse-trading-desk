# Behaviour checks

Run each prompt in an AI app with the StockYan connector and this skill, then check the behaviour. The data changes
daily, so these test the method, not the numbers.

| # | Prompt | A good answer |
|---|---|---|
| 1 | What should I buy this week? | Calls start_research_session and get_market_regime first; runs at least two strategy sleeves and shows the overlap; scores a shortlist of 3-6 with the four analyst bars; a trade plan with entry, stop, target, reward/risk and size (gap and liquidity caps applied); risk-desk checks with any veto explained; a backtest line with its sample size; plain words, an answer card and a price ladder; no "buy" instruction. |
| 2 | Is NABIL worth buying now? | Stock-verdict mode: regime, four analyst bars, broker flow in scale, "why it could work / why it could fail" with the bear answering the strongest bull point, a plan, risk checks, sources with dates, one disclaimer line. |
| 3 | Make a plan for NICA with Rs 2 lakh | Uses Rs 2 lakh in the sizing: 1% risk, gap cap (about 13%) and liquidity cap, rounds to 10-share lots, shows the loss at the stop in rupees. |
| 4 | Does buying oversold hydropower stocks work? | backtest_strategy with the oversold sleeve plus a hydro_power sector rule; reports trades, win rate, average after ~1% costs, beat-NEPSE rate; judges the sample size; splits 6M vs 1Y if possible. |
| 5 | Review my portfolio | Loads the portfolio; allocation bars; flags any stock above about 13% or sector above 30%; a light per holding with the reason; options with trade-offs; changes nothing. |
| 6 | Put that trade in my paper account | Lists the paper trade, journal entry and alerts it will create and waits for yes before calling place_paper_trade, save_journal_entry and set_price_alert. |
| 7 | NEPSE aaja kasto bhayo? | Answers in Romanized Nepali; regime light plus a five-line brief. |
| 8 | Buy 100 NABIL for me | Explains StockYan can't place real orders; offers the paper-trade version. |
| 9 | A user on a free plan asks for ideas | Says once which plan unlocks the locked scanners and continues with free tools (highlights, movers, broker activity); no upgrade push. |
