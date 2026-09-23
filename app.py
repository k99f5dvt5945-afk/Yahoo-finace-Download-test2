import streamlit as st
import yfinance as yf
import pandas as pd

st.title("台股歷史資料查詢")

stock_code = st.text_input(
    "請輸入股票代號",
    "2330.TW"
)

period_option = st.selectbox(
    "查詢期間",
    [
        "從最早資料到最新資料",
        "1 個月",
        "3 個月",
        "6 個月",
        "1 年",
        "5 年"
    ]
)

if st.button("查詢"):

    if period_option == "從最早資料到最新資料":
        data = yf.download(stock_code, period="max")
    elif period_option == "1 個月":
        data = yf.download(stock_code, period="1mo")
    elif period_option == "3 個月":
        data = yf.download(stock_code, period="3mo")
    elif period_option == "6 個月":
        data = yf.download(stock_code, period="6mo")
    elif period_option == "1 年":
        data = yf.download(stock_code, period="1y")
    elif period_option == "5 年":
        data = yf.download(stock_code, period="5y")

    # 把多層欄位攤平成單層，避免 KeyError
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    if data.empty:
        st.error("找不到這個股票代號，請確認輸入是否正確。")
        st.stop()

    # 計算多條均線
    ma_periods = [5, 10, 20, 50, 100, 200]
    for p in ma_periods:
        data[f"MA{p}"] = data["Close"].rolling(window=p).mean()

    st.write("股票代號：", stock_code)

    st.dataframe(data[["Close", "Volume"]])

    st.subheader("收盤價與均線")
    ma_columns = ["Close"] + [f"MA{p}" for p in ma_periods]
    st.line_chart(data[ma_columns])

    st.subheader("成交量")
    st.bar_chart(data["Volume"])