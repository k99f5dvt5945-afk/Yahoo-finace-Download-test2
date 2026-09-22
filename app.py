import streamlit as st
import yfinance as yf

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

    if data.empty:
        st.error("找不到這個股票代號，請確認輸入是否正確。")
        st.stop()

    st.write("股票代號：", stock_code)

    st.dataframe(data[["Close", "Volume"]])

    st.subheader("收盤價")

    st.line_chart(data["Close"])

    st.subheader("成交量")

    st.bar_chart(data["Volume"])