# notes - stuff I didn't know!
[Tucker Balch]

## lesson 1 - introduction
Mini courses:
1. manipulating financial data in python
2. computational investing
3. learning algorithms for trading

## lesson 2 - reading & plotting stock data
Quiz:
Company name is not in  stock data since it does not change over time.
Only date/time & prices are in the stock data.

Pandas library was created by Wes McKineey at a hedge fund called AQR.

## lesson 8 - Sharpe Ratio & other portfolio statistics
A portfolio is an allocation of funds to a set of stocks.
We assume the allocations sum to `1.0`.
We want to be able to calculate the total value of a portfolio day by day.
Then we can compute statistics on the overall portfolio.

So we are given:
1. `start_val` (something like 1,000,000)
2. `start_date` (something like `2009-1-1`)
3. `end_date` (something like `2011-12-31`)
4. `symbols` (like ['SPY', 'XOM', 'GOOG', 'GLD'])
5. `allocs` (like [0.4, 0.4, 0.1, 0.1])

To calculate daily portfolio value:
```python
normed = prices/prices[0]  # normalise using the first row, i.e. start date prices
alloced = normed * allocs
pos_vals = alloced * start_val  # position values, start_val is initial investment
port_val = pos_vals.sum(axis=1)  # portfolio values
```

So `port_val` is daily portfolio value.
`port_val` is a series.

__PortfolioStatistics__:
- we can compute `daily_rets` with first value 0.
We remove the first value using `daily_rets = daily_rets[1:]`

4 important portfolio statistics:
1. `cum_ret = (port_val[-1] - port_val[0])/port_val[0]`
2. `avg_daily_ret = daily_rets.mean()`
3. `std_daily_ret = daily_rets.std()` aka `risk`
4. `sharpe_ratio`

`sharpe_ratio` considers return or reward in the context of `risk`.
`risk` is considered to be `std` or `volatility`.
`volatility` is `std` of portfolio return.

_sharperatio_:
Named after `William Sharpe`.
`risk` adjusted `return`. All else being equal,
- lower risk is better
- higher return is better
Also considers risk-free rate of return.
The value of a portfolio is directly proportional to the return it generates over some baseline (here risk-free rate), and inversely proportional to its volatility.

```python
s = mean(daily_rets - daily_rf)/std(daily_rets - daily_rf)
```

For the risk-free rate (`daily_rf`) we use:
1. LIBOR (London Interbank Offer Rate)
2. intereset rate on the 3 month T-bill (treasury bill)
3. 0.

Use `daily_rf = math.pow(1.0 + 0.1, 1/252) - 1`, if 0.1% annually.
So, it is a constant. We remove it from the denominator in `s`.

SR can vary widely depending on how frequently we sample. It is an annual measure.
So `sr_annualized = k * s` where `k = sqrt(#samples_per_year)`.
For daily frequency, we have `k = sqrt(252)`.
`k` depends only on the frequency at which we are sampling.

`bps` is basis points. 1 basis point is `1/100` of a percent.
It could be a unit for `daily_rets` or `daily_rf`.

---
