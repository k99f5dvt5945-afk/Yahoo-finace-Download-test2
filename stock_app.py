import yfinance as yf
import matplotlib.pyplot as plt

stock_code = input("請輸入股票代號：")

print("你輸入的股票代號是：", stock_code)

data = yf.download(stock_code, period="1mo")

print(data[["Close", "Volume"]])

plt.plot(data.index, data["Close"])
plt.title(f"{stock_code} Closing Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()