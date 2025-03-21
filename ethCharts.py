import pandas as pd

import processData as pdt
import matplotlib.pyplot as plt

# Przetwarzanie danych
data = pdt.process("data/eth.csv")


# Ustawienia globalne dla wykresów
plt.rcParams.update({'font.size': 15})


# Wykres cen zamknięcia
plt.figure(figsize=(25, 10))
plt.plot(data["Date"], data["Price"], color="black")
plt.xlabel("Data zamknięcia", loc="right")
plt.ylabel("Cena zamknęcia [USD]", loc="top")
plt.title("Wykres ceny zamknięcia ETH od 27-05-2022 do 27-02-2025")
plt.savefig("charts/ethPrice.png")


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
plt.title("Wykres MACD i Signal ETH od 27-05-2022 do 27-02-2025")
plt.legend()
plt.savefig("charts/ethMACD.png")


# Wykres kupna i sprzedaży dla wykresu ceny zamknięcia
plt.figure(figsize=(25, 10))
plt.plot(data["Date"], data["Price"], color="black", zorder=1)
plt.scatter(data.loc[data["Verdict"] == "BUY", "Date"], data.loc[data["Verdict"] == "BUY", "Price"],
            color="green", label="Kupno", marker="^", s=100, zorder=2)
plt.scatter(data.loc[data["Verdict"] == "SELL", "Date"], data.loc[data["Verdict"] == "SELL", "Price"],
            color="red", label="Sprzedaż", marker="v", s=100, zorder=2)
plt.xlabel("Data zamknięcia", loc="right")
plt.ylabel("Cena zamknięcia [USD]", loc="top")
plt.title("Wykres ceny zamknięcia ETH od 27-05-2022 do 27-02-2025 z punktami kupna i sprzedaży")
plt.legend()
plt.savefig("charts/ethBuySellPrice.png")


# Wykres prezentujący opóźnioną transakcję z zyskiem
limitedData = data[(data["Date"] >= pd.to_datetime('2023-12-01')) & (data["Date"] <= pd.to_datetime('2023-12-17'))]
plt.figure(figsize=(25, 10))
plt.plot(limitedData["Date"], limitedData["Price"], color="black", zorder=1)
plt.scatter(limitedData.loc[limitedData["Verdict"] == "BUY", "Date"],
            limitedData.loc[limitedData["Verdict"] == "BUY", "Price"],
            color="green", label="Kupno", marker="^", s=200, zorder=2)
plt.scatter(limitedData.loc[limitedData["Verdict"] == "SELL", "Date"],
            limitedData.loc[limitedData["Verdict"] == "SELL", "Price"],
            color="red", label="Sprzedaż", marker="v", s=200, zorder=2)
for i in limitedData.index:
    if limitedData.at[i, "Verdict"] == "BUY":
        plt.annotate(str(limitedData.at[i, "Price"]),
                     (limitedData.at[i, "Date"], limitedData.at[i, "Price"]),
                     textcoords="offset points", xytext=(20, -25), ha="center", fontsize=12,
                     bbox=dict(boxstyle="round,pad=0.15", edgecolor="black", facecolor="white"))

    elif limitedData.at[i, "Verdict"] == "SELL":
        plt.annotate(str(limitedData.at[i, "Price"]),
                     (limitedData.at[i, "Date"], limitedData.at[i, "Price"]),
                     textcoords="offset points", xytext=(20, -25), ha="center", fontsize=12,
                     bbox=dict(boxstyle="round,pad=0.15", edgecolor="black", facecolor="white"))
plt.xlabel("Data zamknięcia", loc="right")
plt.ylabel("Cena zamknięcia [USD]", loc="top")
plt.title("Przykład opóźnionej sprzedaży z zyskiem dla ETH")
plt.legend()
plt.savefig("charts/ethProfitDelay.png")


# Powyższa transakcja w skali makro
transactionData = limitedData
limitedData = data[(data["Date"] >= pd.to_datetime('2023-11-8')) & (data["Date"] <= pd.to_datetime('2024-01-20'))]
plt.figure(figsize=(25, 10))
plt.plot(limitedData["Date"], limitedData["Price"], color="black", zorder=1)
plt.scatter(limitedData.loc[limitedData["Verdict"] == "BUY", "Date"],
            limitedData.loc[limitedData["Verdict"] == "BUY", "Price"],
            color="green", label="Kupno", marker="^", s=200, zorder=2)
plt.scatter(limitedData.loc[limitedData["Verdict"] == "SELL", "Date"],
            limitedData.loc[limitedData["Verdict"] == "SELL", "Price"],
            color="red", label="Sprzedaż", marker="v", s=200, zorder=2)
plt.scatter(transactionData.loc[transactionData["Verdict"] == "BUY", "Date"],
            transactionData.loc[transactionData["Verdict"] == "BUY", "Price"],
            color="green", label="Wejście transakcji", marker="^", s=300, edgecolors='red', linewidths=3, zorder=3)
plt.scatter(transactionData.loc[transactionData["Verdict"] == "SELL", "Date"],
            transactionData.loc[transactionData["Verdict"] == "SELL", "Price"],
            color="red", label="Wyjście transakcji", marker="v", s=200, edgecolors='green', linewidths=3, zorder=3)
for i in transactionData.index:
    if transactionData.at[i, "Verdict"] == "BUY":
        plt.annotate(str(transactionData.at[i, "Price"]),
                     (transactionData.at[i, "Date"], transactionData.at[i, "Price"]),
                     textcoords="offset points", xytext=(20, -25), ha="center", fontsize=12,
                     bbox=dict(boxstyle="round,pad=0.15", edgecolor="black", facecolor="white"))

    elif transactionData.at[i, "Verdict"] == "SELL":
        plt.annotate(str(transactionData.at[i, "Price"]),
                     (transactionData.at[i, "Date"], transactionData.at[i, "Price"]),
                     textcoords="offset points", xytext=(20, -25), ha="center", fontsize=12,
                     bbox=dict(boxstyle="round,pad=0.15", edgecolor="black", facecolor="white"))
plt.xlabel("Data zamknięcia", loc="right")
plt.ylabel("Cena zamknięcia [USD]", loc="top")
plt.title("Przykład nieudanych transakcji dla ETH")
plt.legend()
plt.savefig("charts/ethProfitDelayMakro.png")


# Wykres przedstawiający opóźnioną transakcję ze stratą
limitedData = data[(data["Date"] >= pd.to_datetime('2025-02-08')) & (data["Date"] <= pd.to_datetime('2025-02-27'))]
plt.figure(figsize=(25, 10))
plt.plot(limitedData["Date"], limitedData["Price"], color="black", zorder=1)
plt.scatter(limitedData.loc[limitedData["Verdict"] == "BUY", "Date"],
            limitedData.loc[limitedData["Verdict"] == "BUY", "Price"],
            color="green", label="Kupno", marker="^", s=200, zorder=2)
plt.scatter(limitedData.loc[limitedData["Verdict"] == "SELL", "Date"],
            limitedData.loc[limitedData["Verdict"] == "SELL", "Price"],
            color="red", label="Sprzedaż", marker="v", s=200, zorder=2)
for i in limitedData.index:
    if limitedData.at[i, "Verdict"] == "BUY":
        plt.annotate(str(limitedData.at[i, "Price"]),
                     (limitedData.at[i, "Date"], limitedData.at[i, "Price"]),
                     textcoords="offset points", xytext=(20, -25), ha="center", fontsize=12,
                     bbox=dict(boxstyle="round,pad=0.15", edgecolor="black", facecolor="white"))

    elif limitedData.at[i, "Verdict"] == "SELL":
        plt.annotate(str(limitedData.at[i, "Price"]),
                     (limitedData.at[i, "Date"], limitedData.at[i, "Price"]),
                     textcoords="offset points", xytext=(20, -25), ha="center", fontsize=12,
                     bbox=dict(boxstyle="round,pad=0.15", edgecolor="black", facecolor="white"))
plt.xlabel("Data zamknięcia", loc="right")
plt.ylabel("Cena zamknięcia [USD]", loc="top")
plt.title("Przykład opóźnionej sprzedaży ze stratą dla ETH")
plt.legend()
plt.savefig("charts/ethLossDelay.png")


# Powyższa transakcja w skali makro
transactionData = limitedData
limitedData = data[(data["Date"] >= pd.to_datetime('2025-01-20')) & (data["Date"] <= pd.to_datetime('2025-02-27'))]
plt.figure(figsize=(25, 10))
plt.plot(limitedData["Date"], limitedData["Price"], color="black", zorder=1)
plt.scatter(limitedData.loc[limitedData["Verdict"] == "BUY", "Date"],
            limitedData.loc[limitedData["Verdict"] == "BUY", "Price"],
            color="green", label="Kupno", marker="^", s=200, zorder=2)
plt.scatter(limitedData.loc[limitedData["Verdict"] == "SELL", "Date"],
            limitedData.loc[limitedData["Verdict"] == "SELL", "Price"],
            color="red", label="Sprzedaż", marker="v", s=200, zorder=2)
plt.scatter(transactionData.loc[transactionData["Verdict"] == "BUY", "Date"],
            transactionData.loc[transactionData["Verdict"] == "BUY", "Price"],
            color="green", label="Wejście transakcji", marker="^", s=300, edgecolors='red', linewidths=3, zorder=3)
plt.scatter(transactionData.loc[transactionData["Verdict"] == "SELL", "Date"],
            transactionData.loc[transactionData["Verdict"] == "SELL", "Price"],
            color="red", label="Wyjście transakcji", marker="v", s=200, edgecolors='green', linewidths=3, zorder=3)
for i in transactionData.index:
    if transactionData.at[i, "Verdict"] == "BUY":
        plt.annotate(str(transactionData.at[i, "Price"]),
                     (transactionData.at[i, "Date"], transactionData.at[i, "Price"]),
                     textcoords="offset points", xytext=(20, -25), ha="center", fontsize=12,
                     bbox=dict(boxstyle="round,pad=0.15", edgecolor="black", facecolor="white"))

    elif transactionData.at[i, "Verdict"] == "SELL":
        plt.annotate(str(transactionData.at[i, "Price"]),
                     (transactionData.at[i, "Date"], transactionData.at[i, "Price"]),
                     textcoords="offset points", xytext=(20, -25), ha="center", fontsize=12,
                     bbox=dict(boxstyle="round,pad=0.15", edgecolor="black", facecolor="white"))
plt.xlabel("Data zamknięcia", loc="right")
plt.ylabel("Cena zamknięcia [USD]", loc="top")
plt.title("Kolejny przykład nieudanych transakcji dla ETH")
plt.legend()
plt.savefig("charts/ethLossDelayMakro.png")


# Symulacja inwestycji
initialPortfolio, finalPortfolio, totalTrades, profitableTrades, losingTrades = \
    (pdt.simulate(data, 0, 1000, 26 + 9))
print("Portfel początkowy: " + str(round(initialPortfolio, 2)) + " $")
print("Portfel końcowy:    " + str(round(finalPortfolio, 2)) + " $")
print("Zysk:               " + str(round(finalPortfolio - initialPortfolio, 2)) + " $")
print("Zysk procentowy:    " + str(round((finalPortfolio - initialPortfolio) / initialPortfolio * 100, 2)) + " %")
print("\nLiczba transakcji: " + str(totalTrades))
print("Liczba zyskownych transakcji: " + str(profitableTrades))
print("Liczba stratnych transakcji:  " + str(losingTrades))
buy = 0
sell = 0
for i in range(len(data)):
    if data.at[i, "Verdict"] == "SELL":
        sell += 1
    elif data.at[i, "Verdict"] == "BUY":
        buy += 1
print("\nLiczba sygnałów kupna: " + str(buy))
print("Liczba sygnałów sprzedaży: " + str(sell))

plt.figure(figsize=(25, 10))
plt.plot(data["Date"], data["Portfolio"] / pow(10, 6), label="MACD", color="red")
plt.plot(data["Date"], data["HoldPortfolio"] / pow(10, 6), label="Hold", color="blue")
plt.xlabel("Data zamknięcia", loc="right")
plt.ylabel("Wartość portfela [mln USD]", loc="top")
plt.title("Symulacja inwestycji dla ETH")
plt.legend()
plt.savefig("charts/ethSimulation.png")
