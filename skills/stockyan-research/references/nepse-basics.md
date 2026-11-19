# NEPSE basics

Facts the research depends on. Rules change: when a tool's output disagrees with this file, trust the tool and say so.

## Trading

- **Days and hours:** Monday to Friday, regular session 11:00 to 15:00 Nepal time (NPT, UTC+5:45), pre-open
  10:30 to 10:45. Closed on public holidays, which are frequent around Dashain and Tihar.
- **Settlement:** T+2.
- **Daily price band:** ±15% for an individual stock (since 21 Apr 2026; it was ±10%). A stock at +15% is "upper
  circuit" and can't trade higher that day.
- **Minimum lot:** generally 10 units (kitta) in the regular market.
- **Face value:** usually Rs 100 per share (some, like mutual funds, Rs 10). Dividend % is quoted on face value.

## Money and units

- Rs with Nepali grouping: Rs 1,23,45,678. 1 lakh = 1,00,000; 1 crore = 100 lakh = 10 million;
  1 arba = 100 crore = 1 billion. Turnover is usually discussed in crore or arba.
- "Kitta" means units or shares.

## Costs and tax (individuals)

- **Capital gains tax** on listed shares, by sale date: 5% if held 365 days or less, 3.75% if held longer (from
  22 Sep 2026). Earlier rates: 7.5% / 10% from 17 Jul 2026, 5% / 7.5% before that.
- **Cash dividends** are taxed at source (5%); bonus shares are also taxed via the company.
- Brokerage is tiered by trade size, plus a SEBON fee and a Rs 25 DP charge per sell. StockYan's portfolio figures
  already include these, so don't recompute them by hand.

## Reading company numbers

- **Quarterly EPS is already annualised** in NEPSE filings. Q1 EPS of Rs 33.89 means a yearly pace of Rs 33.89.
  Don't multiply by 4. P/E = LTP ÷ that EPS.
- **Fiscal year** runs mid-July to mid-July (Shrawan to Ashadh) and is written in Bikram Sambat, e.g. 2083/84.
  Q1 ends mid-October, Q2 mid-January, Q3 mid-April, Q4 mid-July.
- **Book closure:** the date to hold shares to get a dividend or bonus or right. After it, the price adjusts down by
  the bonus or right (StockYan's price history is adjusted for these).
- **Promoter shares** are locked in after an IPO; when a lock-in expires, extra supply can hit the market.
- Banks are regulated by Nepal Rastra Bank (NRB); its directives (capital, loan limits, interest spread) move the
  whole banking sector.

## Sectors (slugs used by the tools)

banking, development_bank, finance, hotel_tourism, hydro_power, investment, life_insurance, manufacturing,
microfinance, mutual_fund, non_life_insurance, others, trading.
