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
    data["Price"] = data["Price"].str.replace(",", "").astype(float)
    data = data[["Date", "Price"]]

    macd(data)

    return data
