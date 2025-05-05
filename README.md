
# VideoGame's Analysis

Questo progetto in Python consente di analizzare un dataset di videogiochi (in formato CSV) attraverso un'interfaccia a menu interattivo da terminale. Le analisi comprendono vendite per regione, anno, piattaforma, genere, publisher e altro.

## Requisiti

- Python 3.7 o superiore
- Moduli Python:
  - `csv`
  - `numpy`

## Dataset

Il programma richiede un file chiamato `videogame.csv` nella stessa directory dello script. Il file deve contenere le seguenti colonne:

- `Name`
- `Platform`
- `Year`
- `Genre`
- `Publisher`
- `NA_Sales`
- `EU_Sales`
- `JP_Sales`
- `Other_Sales`
- `Global_Sales`

## Esecuzione

Per avviare il programma, esegui:

```bash
python nome_file.py
```

## Funzionalità

Nel menu interattivo è possibile selezionare una delle seguenti opzioni:

1. **Vendite totali per regione**  
   Calcola il totale delle vendite in una delle regioni: `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`, `Global_Sales`.

2. **Vendite di un gioco per anno**  
   Inserendo il nome del gioco e l'anno, mostra le vendite globali in quell'anno.

3. **Piattaforma con più vendite globali**  
   Determina la piattaforma con il maggiore numero di vendite.

4. **Publisher con più vendite globali**

5. **Genere più venduto globalmente**

6. **Vendite medie per genere**

7. **Tendenza vendite annuali per piattaforma**  
   Visualizza la somma delle vendite per anno per una piattaforma selezionata.

8. **Vendita minima annuale per publisher**  
   Mostra la vendita più bassa registrata ogni anno da un publisher.

9. **Top 10 giochi per vendite globali**

0. **Esci dal programma**

## Note

- Le righe del CSV con dati mancanti o errati verranno ignorate automaticamente.
- Il programma è compatibile con Python 3.10+ per l'uso del costrutto `match-case`.

*Autore: Giacomo Visciotti-Giovanni Pisaniello*
