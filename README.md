# 📈 Stock Valuation Dashboard

A Streamlit dashboard for exploring stock price trends. Search about 5,300 Nasdaq-listed securities by ticker or company name, or enter any Yahoo Finance ticker manually (crypto, indices, foreign stocks). It plots price history with 50-day and 200-day moving averages and shows a simple trend signal.

**[👉 View the live app](https://oladipupo-david-finance-dashboard.streamlit.app/)** (it may take a few seconds to wake up if it has been idle)

> Built with AI assistance. I led the design and feature decisions, then reviewed and tested the code.

## Features

### Search
* Searchable dropdown of 5,296 securities loaded from a local file (`tickers.txt`, Nasdaq-listed format): 4,168 non-ETF securities (stocks, warrants, rights, units) and 1,128 ETFs.
* Find companies by name (e.g., "Apple") without knowing the ticker symbol (`AAPL`).
* **Manual Entry mode** for tickers outside the list, such as:
    * Cryptocurrencies (`BTC-USD`, `ETH-USD`)
    * Market indices (`^GSPC`, `^DJI`)
    * Foreign stocks (`7203.T`)

### Charts and analysis
* Five years of daily price history from Yahoo Finance (`yfinance`), fetched on demand.
* Interactive candlestick chart (Plotly) with a 50-day SMA (orange) and 200-day SMA (blue).
* Current price and moving-average metrics.
* Trend signal: **Bullish** when the 50-day SMA is above the 200-day SMA, otherwise **Bearish**. This is the idea behind golden cross / death cross signals. If a ticker doesn't have enough history (about 200 trading days), the app shows a message instead of a signal.

### Caching and error handling
* The ticker list loads from a local file and is cached with `st.cache_data`, so the app doesn't fetch a remote list on every run.
* Price data is cached for one hour (`ttl=3600`) to limit repeat requests to Yahoo Finance.
* The app shows an error message if a ticker can't be loaded (delisted or invalid).

## Limitations
* The search list covers Nasdaq-listed securities only. NYSE and AMEX tickers (e.g., `SPY`) need Manual Entry.
* The analysis is technical only (moving averages). Despite the name, it doesn't calculate valuation metrics such as P/E or DCF.
* Data comes from Yahoo Finance through `yfinance`, an unofficial library. It can be delayed, rate-limited, or occasionally unavailable.
* The Bullish/Bearish signal is a simple indicator, not a trading strategy.

## Tech Stack
* Python 3 (tested on 3.14)
* Streamlit
* Plotly
* pandas
* yfinance

## Run Locally

```bash
git clone https://github.com/oladipupo-david-gideon/stock-evaluation-dashboard.git
cd stock-evaluation-dashboard
python -m venv venv
```

**Windows (PowerShell):**
```powershell
.\venv\Scripts\python -m pip install -r requirements.txt
.\venv\Scripts\python -m streamlit run app.py
```

**macOS / Linux:**
```bash
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Keep `tickers.txt` in the same folder as `app.py`, since the search feature reads it.

## Recent Fixes
* The default selection is now AAPL. Before, it fell back to the first ticker alphabetically (a newly listed company with almost no history).
* Tickers without enough history now show "N/A" and an info message instead of a false "Bearish" signal.

## ⚠️ Disclaimer
This dashboard is for educational purposes only. It is not financial advice. Always do your own research before trading.
