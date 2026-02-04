import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(layout="wide", page_title="Stock Dashboard")
st.title("Stock Valuation Dashboard")

# --- 1. Load the Master Ticker List ---
@st.cache_data
def get_ticker_list():
    """
    Downloads the official list of all stocks traded on US exchanges 
    (NYSE, NASDAQ, AMEX) directly from the Nasdaq FTP server.
    """
    try:
        # Official source for all US-traded securities
        url = "http://ftp.nasdaqtrader.com/dynamic/SymDir/nasdaqtraded.txt"
        df = pd.read_csv(url, sep='|')
        
        # Filter out test data and clean up
        df = df[df['Test Issue'] == 'N']
        df = df[~df['Symbol'].isnull()]
        
        # Create a search label: "AAPL - Apple Inc."
        df['Search_Label'] = df['Symbol'] + " - " + df['Security Name']
        
        return df[['Symbol', 'Search_Label']].sort_values('Symbol')
    except Exception as e:
        # Fallback list if the FTP server is down
        st.warning("Could not download full ticker list. Using fallback list.")
        return pd.DataFrame({
            'Symbol': ['SPY', 'AAPL', 'NVDA', 'MSFT', 'TSLA', 'AMZN', 'GOOGL'], 
            'Search_Label': ['SPY - SPDR S&P 500', 'AAPL - Apple Inc', 'NVDA - NVIDIA', 'MSFT - Microsoft', 'TSLA - Tesla', 'AMZN - Amazon', 'GOOGL - Alphabet']
        })

# Load tickers once
ticker_df = get_ticker_list()

# --- 2. Search Interface ---
col_search, col_mode = st.columns([3, 1])

with col_mode:
    # Toggle between searching the list or typing a manual code (for Crypto/Indices)
    input_mode = st.radio("Input Mode:", ["Search US Stocks", "Manual Entry"], horizontal=True)

if input_mode == "Search US Stocks":
    # Dropdown with 8,000+ options. 
    # typing 'App' will show 'AAPL - Apple Inc', 'APPL - Appell...', etc.
    selected_item = st.selectbox(
        "Search for a stock:", 
        options=ticker_df['Search_Label'],
        index=ticker_df[ticker_df['Symbol'] == 'SPY'].index[0] if 'SPY' in ticker_df['Symbol'].values else 0
    )
    # Extract the symbol from the selection string (everything before " - ")
    selected_ticker = selected_item.split(" - ")[0]
else:
    # Manual text entry for things not in the US stock list (e.g., ^GSPC, BTC-USD)
    selected_ticker = st.text_input("Enter Ticker Symbol (e.g., BTC-USD, ^GSPC):", value="SPY").upper()

# --- 3. Data Loading ---
@st.cache_data(ttl=3600) # Cache data for 1 hour to prevent spamming Yahoo
def load_data(symbol):
    ticker = yf.Ticker(symbol)
    try:
        data = ticker.history(period='5y')
        if data.empty:
            return None
        data.reset_index(inplace=True)
        return data
    except Exception:
        return None

# Load the data based on user selection
df = load_data(selected_ticker)

if df is None or df.empty:
    st.error(f"❌ Could not load data for **{selected_ticker}**. It may be delisted or invalid.")
    st.stop()

# --- Calculations ---
df['SMA_50'] = df['Close'].rolling(window=50).mean()
df['SMA_200'] = df['Close'].rolling(window=200).mean()

# --- Layout ---
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader(f"Price History: {selected_ticker}")
    
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'],
        name=selected_ticker
    ))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['SMA_50'], line=dict(color='orange', width=1), name='50-Day SMA'))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['SMA_200'], line=dict(color='blue', width=1), name='200-Day SMA'))
    fig.update_layout(xaxis_rangeslider_visible=False, height=600)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Analysis")
    current_price = df['Close'].iloc[-1]
    sma_50 = df['SMA_50'].iloc[-1]
    sma_200 = df['SMA_200'].iloc[-1]
    
    st.metric("Current Price", f"${current_price:.2f}")
    st.metric("50-Day SMA", f"${sma_50:.2f}")
    st.metric("200-Day SMA", f"${sma_200:.2f}")
    
    if sma_50 > sma_200:
        st.success("Trend: Bullish")
    else:
        st.error("Trend: Bearish")
