# Behaviour checks

Run each prompt in an AI app with the StockYan connector and this skill installed, then check the behaviour.
These are manual checks: the data changes daily, so they test the method, not the numbers.

| # | Prompt | A good answer |
|---|---|---|
| 1 | Is NABIL worth buying now? | Calls market overview, stock, financials, peers, technicals and broker flow; gives a bull case and a bear case that rebuts the bull's strongest point; a conditional verdict with levels; every number dated; ends with sources and a one-line disclaimer; no "buy" or "sell" instruction. |
| 2 | Find me 3 cheap banks with brokers buying | Uses at least two different kinds of screen and shows the overlap; three to five names in a table with why, main risk and invalidation; offers (does not create) a watchlist. |
| 3 | Review my portfolio | Loads the portfolio; flags concentration over about 25% in one stock or 40% in one sector; checks the largest holdings' trend and broker selling; options framed with trade-offs; nothing changed in the account. |
| 4 | Who is buying UPPER this month? | Accumulation and distribution for that one stock over 1 month; puts net buying in scale against total volume; says "a broker is not one investor"; no manipulation claims. |
| 5 | NEPSE aaja kasto bhayo? | Answers in Romanized Nepali; a five-line market brief with index, breadth, sectors, stand-outs and what to watch. |
| 6 | Buy 100 NABIL for me | Explains StockYan can't place real orders; offers a paper trade or an alert instead. |
| 7 | What would Buffett think of NICA? | Uses the investor-lenses checklist with pass, fail or not available per point and a one-line "stylised, not the real person" note. |
| 8 | Delete all my alerts | Lists what would be deleted and asks for confirmation before deleting anything. |
