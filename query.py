import pandas as pd
import sqlite3

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

conn = sqlite3.connect("portafoglio.db")

# --- QUERY 1: elenco prestiti con dati cliente ---
query1 = """
SELECT
    prestiti.id_prestito,
    clienti.nome,
    prestiti.importo,
    clienti.citta,
    clienti.settore
FROM prestiti
JOIN clienti ON prestiti.id_cliente = clienti.id_cliente;
"""
risultato1 = pd.read_sql(query1, conn)
print("=== ELENCO PRESTITI ===")
print(risultato1)

# --- QUERY 2: totale prestato per citta ---
query2 = """
SELECT
    clienti.citta,
    COUNT(prestiti.id_prestito) AS numero_prestiti,
    SUM(prestiti.importo) AS totale_prestato
FROM prestiti
JOIN clienti ON prestiti.id_cliente = clienti.id_cliente
GROUP BY clienti.citta
ORDER BY totale_prestato DESC;
"""
risultato2 = pd.read_sql(query2, conn)
print()
print("=== TOTALE PER CITTA ===")
print(risultato2)

# --- QUERY 3: totale prestato per settore ---
query3 = """
SELECT
    clienti.settore,
    COUNT(prestiti.id_prestito) AS numero_prestiti,
    SUM(prestiti.importo) AS totale_prestato
FROM prestiti
JOIN clienti ON prestiti.id_cliente = clienti.id_cliente
GROUP BY clienti.settore
ORDER BY totale_prestato DESC;
"""
risultato3 = pd.read_sql(query3, conn)
print()
print("=== TOTALE PER SETTORE ===")
print(risultato3)

conn.close()