# Station 9: Simulated execution (paper trading, journal, alerts)

StockYan can't place real orders, but the user can rehearse the plan with virtual money and get alerts on their phone.
Do this only after the user says yes, and list exactly what you'll create first:

> "Shall I (1) buy 130 XYZ at about Rs 500 in your paper account, (2) save the plan in your trading journal, and
> (3) set alerts at Rs 480 (stop) and Rs 540 (target)?"

## On a yes

1. `place_paper_trade`: buy the planned quantity in the paper account (fills at the current price, like the app).
2. `save_journal_entry`: the plan: stock, strategy sleeve, entry zone, stop, targets, reason in one line.
3. `set_price_alert`: the stop and target 1 (and target 2 if the user wants).
4. Confirm what was created, with the paper fill price.

## Following up

When the user comes back ("how is my paper trade?"), use `get_my_paper_trading` and `get_my_trading_journal`: show the
P/L, distance to stop and target, and whether the original reasons still hold (re-run stations 3 and 4 briefly).
Over time, the journal becomes the user's own track record: which sleeves actually worked for them.
