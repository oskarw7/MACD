import pandas as pd


def ema(data: pd.DataFrame, period: int, source: str, destination: str):
    alpha = 2 / (period + 1)
    for i in range(period, len(data)):
        upperSum = 0
        lowerSum = 0
        for j in range(period+1):
            upperSum += ((1 - alpha) ** j) * data.at[i - j, source]
            lowerSum += (1 - alpha) ** j
        data.at[i, destination] = upperSum / lowerSum


def analyze(data: pd.DataFrame):
    data.at[0, "Verdict"] = "HOLD"
    for i in range(1, len(data)):
        if data.at[i, "MACD"] < data.at[i, "Signal"] and data.at[i-1, "MACD"] > data.at[i-1, "Signal"]:
            data.at[i, "Verdict"] = "SELL"
        elif data.at[i, "MACD"] > data.at[i, "Signal"] and data.at[i-1, "MACD"] < data.at[i-1, "Signal"]:
            data.at[i, "Verdict"] = "BUY"
        else:
            data.at[i, "Verdict"] = "HOLD"


def macd(data: pd.DataFrame):
    ema(data, 12, "Price", "EMA12")
    ema(data, 26, "Price", "EMA26")
    data["MACD"] = data["EMA12"] - data["EMA26"]
    ema(data, 9, "MACD", "Signal")
    analyze(data)


def process(filePath: str) -> pd.DataFrame:
    data = pd.read_csv(filePath)
    data["Date"] = pd.to_datetime(data["Date"], dayfirst=True)
    if data["Price"].dtype == "object":
        data["Price"] = data["Price"].str.replace(",", "").astype(float)
    data = data[["Date", "Price"]]
    macd(data)
    return data


def simulate(data: pd.DataFrame, money: float, stocks: float, offset: int,
             sellFactor: float = 1, buyFactor: float = 1) -> [float, float, int, int, int]:
    initialPortfolio = money + stocks * data.at[offset, "Price"]
    initialMoney = money
    initialStocks = stocks
    buyPrice = None
    totalTrades = 0
    profitableTrades = 0
    losingTrades = 0
    for i in range(offset, len(data)):
        if data.at[i, "Verdict"] == "SELL":
            toSell = stocks * sellFactor
            stocks -= toSell
            money += toSell * data.at[i, "Price"]
            if buyPrice is not None:
                totalTrades += 1
                if data.at[i, "Price"] > buyPrice:
                    profitableTrades += 1
                else:
                    losingTrades += 1
                buyPrice = None
        elif data.at[i, "Verdict"] == "BUY":
            toBuy = money * buyFactor
            money -= toBuy
            stocks += toBuy / data.at[i, "Price"]
            buyPrice = data.at[i, "Price"]
        data.at[i, "Portfolio"] = money + stocks * data.at[i, "Price"]
        data.at[i, "HoldPortfolio"] = initialMoney + initialStocks * data.at[i, "Price"]
    finalPortfolio = money + stocks * data.at[len(data) - 1, "Price"]
    return initialPortfolio, finalPortfolio, totalTrades, profitableTrades, losingTrades
