# 📈 S&P 500 Valuation Dashboard

A live financial dashboard that visualizes the S&P 500 (SPY) price history, calculates technical indicators, and screens for trading signals. Built with Python and Streamlit.

**[👉 Click here to view the Live App]([INSERT YOUR STREAMLIT APP LINK HERE])**

## 🚀 Features
* **Real-Time Data:** Fetches the last 5 years of market data using the Yahoo Finance API (`yfinance`).
* **Interactive Charts:** Zoomable "Candlestick" charts powered by **Plotly**.
* **Technical Analysis:**
    * **50-Day SMA** (Simple Moving Average) - Orange Line
    * **200-Day SMA** (Simple Moving Average) - Blue Line
* **Automated Signals:** Automatically detects "Golden Cross" (Bullish) or "Death Cross" (Bearish) trends based on moving averages.
* **Key Metrics:** Displays current price, daily return, and 52-week highs.

## 🛠️ Tech Stack
* **Python 3.9+**
* **Streamlit** (Frontend/Dashboarding)
* **Plotly Graph Objects** (Financial Visualization)
* **Pandas** (Data Manipulation & Rolling Statistics)
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

## ⚠️ Disclaimer
This dashboard is for educational purposes only. It is not financial advice. Always do your own research before trading.
