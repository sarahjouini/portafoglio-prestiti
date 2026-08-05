import pandas as pd
import sqlite3

clienti = pd.read_csv("clienti.csv")
prestiti = pd.read_csv("prestiti.csv")

conn = sqlite3.connect("portafoglio.db")
clienti.to_sql("clienti", conn, if_exists="replace", index=False)
prestiti.to_sql("prestiti", conn, if_exists="replace", index=False)
conn.close()

print("Database creato con le tabelle clienti e prestiti.")