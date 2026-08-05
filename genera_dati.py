import pandas as pd
import numpy as np

np.random.seed(42)

# ---- CLIENTI ----
n_clienti = 25
settori = ["Manifattura", "Tecnologia", "Alimentare", "Edilizia", "Turismo"]
citta = ["Milano", "Roma", "Torino", "Napoli", "Firenze", "Bologna"]

clienti = pd.DataFrame({
    "id_cliente": range(1, n_clienti + 1),
    "nome": ["Azienda_" + str(i) for i in range(1, n_clienti + 1)],
    "citta": np.random.choice(citta, n_clienti),
    "settore": np.random.choice(settori, n_clienti),
    "fatturato": np.random.randint(100000, 3000000, n_clienti),
})

# ---- PRESTITI ----
# Genera un numero variabile di prestiti, ognuno legato a un cliente a caso.
n_prestiti = 60
prestiti = pd.DataFrame({
    "id_prestito": range(101, 101 + n_prestiti),
    "id_cliente": np.random.randint(1, n_clienti + 1, n_prestiti),
    "importo": np.random.randint(10000, 500000, n_prestiti),
    "stato": np.random.choice(["ripagato", "in corso", "insolvente"],
                              n_prestiti, p=[0.5, 0.35, 0.15]),
})

clienti.to_csv("clienti.csv", index=False)
prestiti.to_csv("prestiti.csv", index=False)

print("=== CLIENTI (prime 5) ===")
print(clienti.head().to_string(index=False))
print()
print("=== PRESTITI (primi 5) ===")
print(prestiti.head().to_string(index=False))
print()
print(f"Creati {len(clienti)} clienti e {len(prestiti)} prestiti.")