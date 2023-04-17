<div align="center">
  <h1>Data Server</h1>
</div>

This code defines a single endpoint, `/query`, that accepts the following parameters:

- `function`: the API function to use, which can be set to any of the following: TIME_SERIES_DAILY, NEWS_SENTIMENT, OVERVIEW, INCOME_STATEMENT, BALANCE_SHEET, CASH_FLOW, EARNINGS, EARNINGS_CALENDAR
- `symbol`: the stock symbol (required for some functions)
- `tickers`: a comma-separated list of stock symbols (required for the NEWS_SENTIMENT function)
- `horizon`: the time horizon for earnings data (required for the EARNINGS_CALENDAR function)

The endpoint returns a JSON object with two keys:

- `meta`: an object containing the metadata of the query, including the function and any required parameters
- `data`: an array of objects containing the stock data

To use this endpoint, you can run the following command in your terminal:

`uvicorn main:app --reload`

Then, you can access the endpoint at http://localhost:8000/query?function=TIME_SERIES_DAILY&symbol=IBM to get daily stock data for IBM, or at http://localhost:8000/query?function=NEWS_SENTIMENT&tickers=AAPL to get news sentiment data for Apple.



