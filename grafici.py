import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("portafoglio.db")

query = """
SELECT
    clienti.citta,
    SUM(prestiti.importo) AS totale_prestato
FROM prestiti
JOIN clienti ON prestiti.id_cliente = clienti.id_cliente
GROUP BY clienti.citta
ORDER BY totale_prestato DESC;
"""
dati = pd.read_sql(query, conn)
conn.close()

plt.figure(figsize=(8, 5))
plt.bar(dati["citta"], dati["totale_prestato"], color="steelblue")
plt.title("Totale prestato per città")
plt.xlabel("Città")
plt.ylabel("Totale prestato (€)")
plt.tight_layout()
plt.savefig("prestato_per_citta.png")
print("Grafico salvato!")