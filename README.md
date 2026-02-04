# 📈 Universal Stock Valuation Dashboard

A professional-grade financial dashboard that allows users to analyze **any** public stock, cryptocurrency, or index. It visualizes price history, calculates technical indicators, and screens for trading signals using real-time data.

**[👉 Click here to view the Live App]([INSERT YOUR STREAMLIT APP LINK HERE])**

## 🚀 New Features (v2.0)

### 1. 🔍 Universal Search with Smart Autocomplete
* **Database of 8,000+ Stocks:** The app now queries a local database of every stock traded on NASDAQ, NYSE, and AMEX.
* **Search by Name:** Users can find companies by typing their name (e.g., "Apple") without needing to memorize the ticker symbol (`AAPL`).

### 2. 🛠️ Manual Entry Mode (Fault Tolerance)
* **Beyond the Stock Market:** Added a "Manual Entry" toggle that bypasses the standard list.
* **Supports All Assets:** This mode allows users to analyze assets not found in standard exchange lists, including:
    * **Cryptocurrencies** (e.g., `BTC-USD`, `ETH-USD`)
    * **Market Indices** (e.g., `^GSPC` for S&P 500, `^DJI`)
    * **Foreign Stocks** (e.g., `7203.T` for Toyota)

### 3. ⚡ Performance Optimization
* **Zero-Latency Loading:** Replaced slow external network requests with a cached local dataset (`tickers.txt`). The app now loads instantly and is immune to external server timeouts.

---

## 📊 Core Capabilities
* **Real-Time Data:** Fetches the last 5 years of daily market data using the `yfinance` API.
* **Interactive Charts:** Zoomable "Candlestick" charts powered by **Plotly**.
* **Technical Indicators:**
    * **50-Day SMA** (Orange Line)
    * **200-Day SMA** (Blue Line)
* **Trend Analysis:** Automatically interprets data to flag "Bullish" or "Bearish" trends based on the Golden Cross/Death Cross logic.

## 🛠️ Tech Stack
* **Python 3.9+**
* **Streamlit** (Frontend/Dashboarding)
* **Plotly Graph Objects** (Financial Visualization)
* **Pandas** (Data Manipulation & File I/O)
* **YFinance** (Market Data API)

## 💻 How to Run Locally

If you want to run this dashboard on your own machine:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/sp500-dashboard.git](https://github.com/YOUR_USERNAME/sp500-dashboard.git)
    cd sp500-dashboard
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app**
    ```bash
    streamlit run app.py
    ```
    *Note: Ensure the `tickers.txt` file is present in the root directory for the search feature to work.*

## ⚠️ Disclaimer
This dashboard is for educational purposes only. It is not financial advice. Always do your own research before trading.
