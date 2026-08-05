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

- **JOIN** per unire clienti e prestiti, così accanto a ogni prestito vedo il nome, la città e il settore del cliente (non solo il numero).
- **Query di riepilogo** (JOIN + GROUP BY) per rispondere a domande di business, tipo:
  - quanto è stato prestato in ogni città;
  - quanto è stato prestato in ogni settore.

## Strumenti usati

- **Python** e **pandas**
- **SQL** (SQLite)
- Dati **sintetici**, creati da me perché i dati veri delle banche sono riservati.

## I file

- `genera_dati.py` — crea le tabelle clienti e prestiti (in CSV).
- `crea_database.py` — mette i dati in un database SQLite.
- `query.py` — le query SQL con le JOIN e i riepiloghi.

## Cosa sto imparando

Con questo progetto sto imparando le JOIN, cioè come unire due tabelle collegate, che è una delle cose più usate nel lavoro vero di un data analyst. Ma soprattutto sto imparando a **cavarmela da sola** con il codice, un pezzo alla volta.