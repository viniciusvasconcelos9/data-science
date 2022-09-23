import yfinance as yf
import streamlit as st

st.write("""
# SIMPLE STOCK PRICE APP

Shown are the stock *closing price* and *volume* of Petrobras!

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'PBR'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2017-6-20', end='2022-6-20')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write("""### Closing Price""")
st.line_chart(tickerDf.Close)
st.write("""### Volume""")
st.line_chart(tickerDf.Volume)
