import yfinance as yf

ticker = "AMZN"
data = yf.download(ticker,  start="2023-04-18", end="2023-04-19", interval="15m")

# print(data)

data.to_csv("AMZN_prices_15m_0418.csv")




ticker = "GOOGL"

data = yf.download(ticker,  start="2023-04-18", end="2023-04-19", interval="15m")

# print(data)

data.to_csv("GOOG_prices_15m_0418.csv")



ticker = "AAPL"

data = yf.download(ticker,  start="2023-04-18", end="2023-04-19", interval="15m")

# print(data)

data.to_csv("APPL_prices_15m_0418.csv")






