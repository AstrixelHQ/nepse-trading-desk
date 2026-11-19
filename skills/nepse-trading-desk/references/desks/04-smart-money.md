# Station 4: Smart-money tracker (floorsheet and broker flow)

NEPSE publishes which broker bought from which broker on every trade. That is a real edge most markets don't
offer, and the easiest place to overclaim. Read it as evidence about demand, not as proof of who or why.

## Tools

| Question | Call |
|---|---|
| Who net bought or sold this stock? | `get_broker_activity(view: "accumulation" \| "distribution", symbol, period)` |
| Biggest buyers or sellers of this stock by amount | `get_broker_activity(view: "top_buyers" \| "top_sellers", symbol, period)` |
| Biggest buyers across the whole market | the same without `symbol` (the result says `scope: "whole market"`) |
| What has broker 58 been buying? | `get_broker_activity(view: "broker_holdings", brokerId: 58, period)` |
| Stocks where a few brokers dominate buying or selling | `get_broker_intel(view: "dominance", side)` (paid) |
| Single brokers taking a big share of a stock's volume | `get_broker_intel(view: "aggressive_accumulators", tier)` (paid) |
| Heavy sellers | `get_broker_intel(view: "distribution_leaders")` (paid) |
| Big positions built by one broker over months | `get_broker_intel(view: "aggressive_holding")` (paid) |
| Same buyer and seller broker trading together | `get_broker_intel(view: "matching_pairs")` (paid) |
| Individual trades on a day | `get_floor_sheet(symbol, date)` |
| Block trades | `get_bulk_transactions(symbol, date)` |

## How to read it

- **Time beats size.** A broker net buying steadily across three or four weeks says more than one huge day. Compare
  1W with 1M and 3M.
- **Scale it.** Net quantities mean little alone: compare them with the stock's total volume over the same period.
- **Concentration matters.** If the top 3 net buyers account for most of the net buying, demand is concentrated
  (someone specific is building a position). Many small buyers means broad interest.
- **Average rates tell you where they bought.** If accumulating brokers averaged Rs 540 and the price is Rs 600,
  they are already in profit and may sell into strength.
- **Buying while the price falls** (absorption) or **selling while the price rises** (distribution into strength) are
  the interesting divergences. Say which you see.
- **Selling is the clearer signal.** Heavy, steady net selling by a few brokers is a more reliable warning than buying
  is an invitation. Weight distribution a little more than accumulation.
- **Thin stocks are easy to push.** In low paid-up-capital or low-float stocks, a few brokers can move the price on
  little money, and circular trading has been documented in NEPSE. Treat "smart money" in these as a caution flag.
- **Data timing.** Broker numbers on trades are published after the close, so intraday broker data isn't available.
- **A broker is not one investor.** Each broker executes for thousands of clients. "Broker 58 bought" means its
  clients bought, together.
- **Matching pairs and circular trading.** The same pair trading back and forth can mean wash-style trades, but it
  can also be two big clients at the same brokers. Call it "possible" and "worth caution", never "manipulation".

## Write-up pattern

One line on the verdict ("steady, concentrated accumulation over a month"), then a small table: broker, net qty,
net Rs, average buy, average sell. Then what it could mean and the caution, then what would change it (for
example, "if these brokers turn net sellers above Rs 600"). Always say the period and date range from the tool output.
