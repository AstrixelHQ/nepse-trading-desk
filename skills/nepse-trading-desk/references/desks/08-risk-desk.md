# Station 8: Risk desk (approve, approve with changes, or veto)

The risk officer can stop any idea. Run every check; report each as ✅ pass, ⚠️ warning or ⛔ fail.

| # | Check | ⛔ Fail when |
|---|---|---|
| 1 | Regime | 🔴 downtrend and the idea isn't a top-scoring one (confluence under 75) |
| 2 | Reward-to-risk | below 1.5 to target 1 |
| 3 | Confluence | under 55 |
| 4 | Liquidity | the position is more than 10% of average daily turnover, or daily turnover is under Rs 30 lakh |
| 5 | Gap risk | a 15% one-day fall would cost more than 2% of the account |
| 6 | Concentration | breaks a station 7 rule |
| 7 | Events in the next 2 weeks | a right share, lock-in expiry, or results with weak recent quarters (⚠️ for book closure and AGM) |
| 8 | Broker distribution | top brokers heavily net selling over the month while the price rises |
| 9 | Manipulation flags | thin float or low paid-up capital with a few brokers doing most of the trading |
| 10 | Stretch | RSI above 75 or price more than about 10% above its 20-day average (chasing) |
| 11 | Data gaps | a lens was "not available" (⚠️; ⛔ if two or more) |

**Verdict:** all ✅ = approved; any ⚠️ = approved with the change that fixes it (smaller size, wait for a pullback,
wait until after the event); any ⛔ = vetoed, with the one-line reason. A vetoed idea still goes in the report:
knowing what *not* to do is half the value.

## Desk-level brakes (for users who track a paper or real account with the desk)

- A strategy sleeve down 5% from its peak: halve its size. Down 8%: pause it, paper only.
- The whole account down 10% from its peak: halve exposure. Down 15%: cash or paper only until the regime improves.
- Down 2% in a day: no new entries that day.

Use `get_my_paper_trading` or `get_my_portfolio` to check these when the user asks the desk to manage ideas over time.
