import streamlit as st
import yfinance as yf

st.title("台股歷史資料查詢")

stock_code = st.text_input("請輸入股票代號", "2330.TW")

if st.button("查詢"):
    data = yf.download(stock_code, period="1mo")

    st.write("股票代號：", stock_code)

    st.dataframe(data[["Close", "Volume"]])

    st.line_chart(data["Close"])

    st.bar_chart(data["Volume"])