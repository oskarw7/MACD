import processData as pdt
import matplotlib.pyplot as plt

data = pdt.process("data/eth.csv")
print(data)

plt.rcParams.update({'font.size': 15})
plt.figure(figsize=(15, 10))
plt.plot(data["Date"], data["Price"])
plt.xlabel("Data zamknięcia", loc="right")
plt.ylabel("Cena zamknęcia [USD]", loc="top")
plt.title("Wykres ceny zamknięcia ETH od 27-05-2022 do 27-02-2025")
plt.show()
