import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.title("S&P Valuation Dashboard (Final)")

# --- Data Loading ---
@st.cache_data
def load_data():
    ticker = yf.Ticker('SPY')
    data = ticker.history(period='5y')
    data.reset_index(inplace=True)
    return data

df = load_data()

# --- Calculations ---
df['SMA_50'] = df['Close'].rolling(window=50).mean()
df['SMA_200'] = df['Close'].rolling(window=200).mean()

# --- Layout ---
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("Price History & Moving Averages")
    
    # Create Plotly Chart
    fig = go.Figure()

    # Candlestick
    fig.add_trace(go.Candlestick(
        x=df['Date'], 
        open=df['Open'], 
        high=df['High'], 
        low=df['Low'], 
        close=df['Close'],
        name='SPY'
    ))

    # Moving Averages Traces
    fig.add_trace(go.Scatter(
        x=df['Date'], 
        y=df['SMA_50'], 
        line=dict(color='orange', width=1), 
        name='50-Day SMA'))
    fig.add_trace(go.Scatter(
        x=df['Date'], 
        y=df['SMA_200'], 
        line=dict(color='blue', width=1), 
        name='200-Day SMA'))

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
    
    # Logic check for Golden Cross
    if sma_50 > sma_200:
        st.success("Trend: Bullish (50 > 200)")
    else:
        st.error("Trend: Bearish (50 < 200)")