import pandas as pd

import processData as pdt
import matplotlib.pyplot as plt

# Przetwarzanie danych
data = pdt.process("data/dji.csv")
print(data)

# Ustawienia globalne dla wykresów
plt.rcParams.update({'font.size': 15})

# Wykres cen zamknięcia
plt.figure(figsize=(25, 10))
plt.plot(data["Date"], data["Price"], color="black")
plt.xlabel("Data zamknięcia", loc="right")
plt.ylabel("Cena zamknięcia [USD]", loc="top")
plt.title("Wykres ceny zamknięcia DJI od 27-05-2022 do 27-02-2025")
# plt.show()
plt.savefig("charts/djiPrice.png")

# Wykres MACD i Signal, punkty sprzedaży i kupna
plt.figure(figsize=(25, 10))
plt.plot(data["Date"], data["MACD"], label="MACD", color="blue", zorder=1)
plt.plot(data["Date"], data["Signal"], label="Signal", color="magenta", zorder=1)
plt.scatter(data.loc[data["Verdict"] == "BUY", "Date"], data.loc[data["Verdict"] == "BUY", "MACD"],
            color="green", label="Kupno", marker="^", s=100, zorder=2)
plt.scatter(data.loc[data["Verdict"] == "SELL", "Date"], data.loc[data["Verdict"] == "SELL", "MACD"],
            color="red", label="Sprzedaż", marker="v", s=100, zorder=2)
plt.xlabel("Data zamknięcia", loc="right")
plt.ylabel("Wartość", loc="top")
plt.title("Wykres MACD i Signal DJI od 27-05-2022 do 27-02-2025")
plt.legend()
# plt.show()
plt.savefig("charts/djiMACD.png")

# Wykres kupna i sprzedaży dla wykresu ceny zamknięcia
plt.figure(figsize=(25, 10))
plt.plot(data["Date"], data["Price"], color="black", zorder=1)
plt.scatter(data.loc[data["Verdict"] == "BUY", "Date"], data.loc[data["Verdict"] == "BUY", "Price"],
            color="green", label="Kupno", marker="^", s=100, zorder=2)
plt.scatter(data.loc[data["Verdict"] == "SELL", "Date"], data.loc[data["Verdict"] == "SELL", "Price"],
            color="red", label="Sprzedaż", marker="v", s=100, zorder=2)
plt.xlabel("Data zamknięcia", loc="right")
plt.ylabel("Cena zamknięcia [USD]", loc="top")
plt.title("Wykres ceny zamknięcia DJI od 27-05-2022 do 27-02-2025 z punktami kupna i sprzedaży")
plt.legend()
# plt.show()
plt.savefig("charts/djiBuySellPrice.png")

# Wykres prezentujący opóźnioną transakcję z zyskiem
limitedData = data[(data["Date"] >= pd.to_datetime('2023-07-01')) & (data["Date"] <= pd.to_datetime('2023-08-06'))]
plt.figure(figsize=(25, 10))
plt.plot(limitedData["Date"], limitedData["Price"], color="black", zorder=1)
plt.scatter(limitedData.loc[limitedData["Verdict"] == "BUY", "Date"], limitedData.loc[data["Verdict"] == "BUY", "Price"],
            color="green", label="Kupno", marker="^", s=200, zorder=2)
plt.scatter(limitedData.loc[limitedData["Verdict"] == "SELL", "Date"], limitedData.loc[data["Verdict"] == "SELL", "Price"],
            color="red", label="Sprzedaż", marker="v", s=200, zorder=2)
for i in range(len(limitedData)):
    if limitedData.iloc[i]["Verdict"] == "BUY":
        plt.annotate(str(limitedData.iloc[i]["Price"]), (limitedData.iloc[i]["Date"], limitedData.iloc[i]["Price"]-1))
for i in range(len(limitedData)):
    if limitedData.iloc[i]["Verdict"] == "SELL":
        plt.annotate(str(limitedData.iloc[i]["Price"]), (limitedData.iloc[i]["Date"], limitedData.iloc[i]["Price"]+0.5))
plt.xlabel("Data zamknięcia", loc="right")
plt.ylabel("Cena zamknięcia [USD]", loc="top")
plt.title("Przykład opóźnionej sprzedaży z zyskiem dla DJI")
plt.legend()
# plt.show()
plt.savefig("charts/djiProfitDelay.png")

# Wykres przedstawiający opóźnioną transakcję ze stratą
limitedData = data[(data["Date"] >= pd.to_datetime('2024-04-02')) & (data["Date"] <= pd.to_datetime('2024-05-01'))]
plt.figure(figsize=(25, 10))
plt.plot(limitedData["Date"], limitedData["Price"], color="black", zorder=1)
plt.scatter(limitedData.loc[limitedData["Verdict"] == "BUY", "Date"], limitedData.loc[data["Verdict"] == "BUY", "Price"],
            color="green", label="Kupno", marker="^", s=200, zorder=2)
plt.scatter(limitedData.loc[limitedData["Verdict"] == "SELL", "Date"], limitedData.loc[data["Verdict"] == "SELL", "Price"],
            color="red", label="Sprzedaż", marker="v", s=200, zorder=2)
for i in range(len(limitedData)):
    if limitedData.iloc[i]["Verdict"] == "BUY":
        plt.annotate(str(limitedData.iloc[i]["Price"]), (limitedData.iloc[i]["Date"], limitedData.iloc[i]["Price"]-0.7))
    elif limitedData.iloc[i]["Verdict"] == "SELL":
        plt.annotate(str(limitedData.iloc[i]["Price"]), (limitedData.iloc[i]["Date"], limitedData.iloc[i]["Price"]+0.5))
plt.xlabel("Data zamknięcia", loc="right")
plt.ylabel("Cena zamknięcia [USD]", loc="top")
plt.title("Przykład opóźnionej sprzedaży ze stratą dla DJI")
plt.legend()
# plt.show()
plt.savefig("charts/djiLossDelay.png")