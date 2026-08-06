import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

conn = sqlite3.connect("portafoglio.db")

# Passo 1: JOIN per avere importo + info cliente + stato
query = """
SELECT
    prestiti.importo,
    clienti.fatturato,
    prestiti.stato
FROM prestiti
JOIN clienti ON prestiti.id_cliente = clienti.id_cliente;
"""
dati = pd.read_sql(query, conn)
conn.close()

# Passo 2: trasformo lo stato in 0/1 (PRIMA di usarlo!)
dati["insolvenza"] = (dati["stato"] == "insolvente").astype(int)

print(dati.head(10))
print()
print("Quanti insolventi:", dati["insolvenza"].sum(), "su", len(dati))

# Passo 3: il modello
X = dati[["importo", "fatturato"]]
y = dati["insolvenza"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modello = LogisticRegression(max_iter=1000)
modello.fit(X_train, y_train)

previsioni = modello.predict(X_test)

print()
print("Accuratezza:", round(accuracy_score(y_test, previsioni) * 100, 1), "%")
print()
print("Matrice di confusione (righe=realtà, colonne=previsione):")
print(confusion_matrix(y_test, previsioni))