# Station 7: Portfolio construction (how it fits with the rest)

One good idea can still be a bad addition. This station checks the idea against the whole account.

## Calls

`get_my_portfolio()` (only if the user wants their real portfolio considered; it's private) or
`get_my_paper_trading()` for the paper account.

## The desk's construction rules

| Rule | Default | Why |
|---|---|---|
| Number of positions | 5 to 10 | Fewer is a bet, more is hard to follow |
| One stock | at most about 13% (the gap cap) | A 15% one-day fall costs at most 2% of the account |
| One sector | at most 30% | Banks, hydro and microfinance move as groups |
| Look-alikes | at most 2 per cluster (e.g. two hydro projects in the same river basin, two microfinance) | They fall together |
| Cash | at least 15%, more in weak regimes | No short selling in NEPSE: cash is the only shelter |
| Total invested | inside the regime band from station 1 | The tide decides |
| Strategy mix | no one sleeve above about 40% of what's invested | If one strategy stops working, the rest carry on |

If a new idea would break a rule, size it down or name what it would replace ("adding NABIL takes banks to 38%;
trimming X first keeps you at 30%"). Framed as an option with its trade-off, not an instruction.

## Show it as a picture

A simple allocation table with bars:

```
Banking       ██████████░░░░░░  28%
Hydropower    ███████░░░░░░░░░  19%
Microfinance  ████░░░░░░░░░░░░  11%
Cash          ████████░░░░░░░░  22%
```
and one line: what changes if the user takes the new idea.
