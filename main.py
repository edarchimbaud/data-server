from typing import Optional
from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/query")
def get_stock_data(function: str, symbol: Optional[str] = None, tickers: Optional[str] = None, horizon: Optional[str] = None):
    if function == "TIME_SERIES_DAILY":
        if symbol is None:
            return {"error": "Missing symbol parameter."}
        stock = yf.Ticker(symbol)
        data = stock.history(period="max").reset_index().rename(columns={"Date": "date", "Open": "open", "High": "high", "Low": "low", "Close": "close", "Volume": "volume"})
        data = data.to_dict("records")
        return {"meta": {"function": function, "symbol": symbol}, "data": data}
    elif function == "NEWS_SENTIMENT":
        if tickers is None:
            return {"error": "Missing tickers parameter."}
        news = yf.Tickers(tickers)
        data = []
        for ticker in news.tickers:
            sentiment = ticker.news
            if len(sentiment) > 0:
                sentiment = sentiment.iloc[0].to_dict()
                sentiment["symbol"] = ticker.ticker
                data.append(sentiment)
        return {"meta": {"function": function, "tickers": tickers}, "data": data}
    elif function == "OVERVIEW":
        if symbol is None:
            return {"error": "Missing symbol parameter."}
        stock = yf.Ticker(symbol)
        data = stock.info
        return {"meta": {"function": function, "symbol": symbol}, "data": data}
    elif function == "INCOME_STATEMENT":
        if symbol is None:
            return {"error": "Missing symbol parameter."}
        stock = yf.Ticker(symbol)
        data = stock.financials
        data = data.reset_index().rename(columns={"index": "date"})
        data = data.to_dict("records")
        return {"meta": {"function": function, "symbol": symbol}, "data": data}
    elif function == "BALANCE_SHEET":
        if symbol is None:
            return {"error": "Missing symbol parameter."}
        stock = yf.Ticker(symbol)
        data = stock.balance_sheet
        data = data.reset_index().rename(columns={"index": "date"})
        data = data.to_dict("records")
        return {"meta": {"function": function, "symbol": symbol}, "data": data}
    elif function == "CASH_FLOW":
        if symbol is None:
            return {"error": "Missing symbol parameter."}
        stock = yf.Ticker(symbol)
        data = stock.cashflow
        data = data.reset_index().rename(columns={"index": "date"})
        data = data.to_dict("records")
        return {"meta": {"function": function, "symbol": symbol}, "data": data}
    elif function == "EARNINGS":
        if symbol is None:
            return {"error": "Missing symbol parameter."}
        stock = yf.Ticker(symbol)
        data = stock.earnings
        data = data.reset_index().rename(columns={"index": "date"})
        data = data.to_dict("records")
        return {"meta": {"function": function, "symbol": symbol}, "data": data}
    elif function == "EARNINGS_CALENDAR":
        if horizon is None:
            return {"error": "Missing horizon parameter."}
        if horizon not in ["1day", "1week", "1month", "3month"]:
            return {"error": "Invalid horizon parameter. Please use 1day, 1week, 1month, or 3month."}
        earnings = yf.Earnings()
        data = earnings.get_earnings_of(horizon)
        data = data.reset_index().rename(columns={"index": "date"})
        data = data.to_dict("records")
        return {"meta": {"function": function, "horizon": horizon}, "data": data}
    else:
        return {"error": "Function not supported. Please use one of the following functions: TIME_SERIES_DAILY, NEWS_SENTIMENT, OVERVIEW, INCOME_STATEMENT, BALANCE_SHEET, CASH_FLOW, EARNINGS, EARNINGS_CALENDAR."}
