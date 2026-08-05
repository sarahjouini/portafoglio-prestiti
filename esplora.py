import pandas as pd
clienti = pd.read_csv("clienti.csv")
prestiti = pd.read_csv("prestiti.csv")

print("=== clienti ===")
print(clienti.head())
print()
print("=== prestiti ===")
print(prestiti.head())