# Portafoglio Prestiti

Questo è un progetto dove analizzo il portafoglio prestiti di una banca: ho un elenco di clienti (aziende) e i prestiti che hanno ricevuto, e uso SQL per capire come sono distribuiti i prestiti tra città, settori e clienti.

## Perché questo progetto è diverso dagli altri

Questo progetto lo sto facendo con **più autonomia** rispetto ai precedenti. Prima venivo guidata molto passo passo; qui invece provo a scrivere io le query e a ragionare da sola su cosa chiedere ai dati, chiedendo aiuto solo quando mi blocco. Per me è un passaggio importante: sto imparando a fare le cose da sola, non solo a copiarle.

## Di cosa parla

Ho due tabelle collegate tra loro:

- **clienti** — le aziende, con nome, città, settore e fatturato.
- **prestiti** — i prestiti erogati, con importo e stato (ripagato, in corso, insolvente). Ogni prestito è legato a un cliente tramite l'id_cliente.

Le due tabelle sono collegate dall'**id_cliente**, ed è proprio questo che mi permette di unirle con le JOIN.

## Cosa ho fatto
 
**1. Analisi con SQL (JOIN)**
Ho usato le JOIN per unire clienti e prestiti, così accanto a ogni prestito vedo il nome, la città e il settore del cliente. Poi, con JOIN + GROUP BY, ho risposto a domande di business: quanto è stato prestato in ogni città e in ogni settore.
 
**2. Grafici**
Ho trasformato i risultati delle query in grafici, così i numeri si leggono a colpo d'occhio (utile per chi non guarda il codice).
 
**3. Modello di machine learning**
Ho provato a costruire un modello che prevede quali prestiti andranno in insolvenza.
## La scoperta più importante
 
Il modello mi ha dato una lezione preziosa. All'inizio sembrava andare bene: aveva circa il 67% di accuratezza. Ma guardando meglio (con la **matrice di confusione**) ho scoperto che il modello **non individuava nemmeno un insolvente**: su tutti i prestiti insolventi del gruppo di test, li classificava tutti come "sani".
 
Il motivo è che i dati sono **sbilanciati**: gli insolventi erano solo 8 su 60. Con così pochi esempi, il modello "impara" a dire quasi sempre "non insolvente", perché statisticamente ci azzecca lo stesso. Il risultato è un'accuratezza che sembra buona ma un modello che, per una banca, è inutile: non trova proprio i prestiti a rischio, che sono quelli che contano di più.
 
La cosa che ho imparato è questa: **l'accuratezza da sola può ingannare**. Su dati sbilanciati bisogna guardare *cosa* sbaglia il modello, non solo quante volte ci azzecca. È un problema reale nel credito, dove le insolvenze sono (per fortuna) rare, e va gestito con attenzione.
 
## Strumenti usati
 
- **Python** e **pandas**
- **SQL** (SQLite)
- **matplotlib** per i grafici
- **scikit-learn** per il modello
- Dati **sintetici**, creati da me perché i dati veri delle banche sono riservati.
## I file
 
- `genera_dati.py` — crea le tabelle clienti e prestiti (in CSV).
- `crea_database.py` — mette i dati in un database SQLite.
- `query.py` — le query SQL con le JOIN e i riepiloghi.
- `grafici.py` — i grafici dei prestiti.
- `modello.py` — il modello di previsione insolvenze e l'analisi dello sbilanciamento.
## Cosa sto imparando
 
Con questo progetto ho messo insieme un po' tutto quello che so fare: SQL con le JOIN, i grafici e un modello di machine learning. Ma la cosa più importante che porto a casa è aver capito, con i miei occhi, che un modello va sempre interrogato con la testa e non preso per buono solo perché "l'accuratezza è alta". E poi sto imparando a cavarmela da sola con il codice, un pezzo alla volta.
