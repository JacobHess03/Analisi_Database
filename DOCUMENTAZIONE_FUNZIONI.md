
# 📚 Documentazione Funzioni - Analisi Dati Videogiochi

Questa documentazione descrive nel dettaglio ogni funzione presente nel progetto Python per l'analisi dei dati sui videogiochi.

---

## 📂 Funzione: `load_data(csv_path)`

**Descrizione:**  
Carica il dataset dei videogiochi da un file CSV.

**Parametri:**  
- `csv_path` *(str)*: Percorso del file CSV.

**Ritorna:**  
- `np.ndarray`: Array strutturato NumPy con i seguenti campi:  
  `Name`, `Platform`, `Year`, `Genre`, `Publisher`, `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`, `Global_Sales`.

---

## 📂 Funzione: `total_sales_region(data, region)`

**Descrizione:**  
Calcola il totale delle vendite per una regione specificata.

**Parametri:**  
- `data` *(np.ndarray)*: Dataset.
- `region` *(str)*: Nome della regione (es. `NA_Sales`, `EU_Sales`, ecc.).

**Ritorna:**  
- `float`: Somma totale delle vendite nella regione.

---

## 📂 Funzione: `total_sales_for_game_year(data, game_name, year)`

**Descrizione:**  
Restituisce le vendite globali di un gioco in un anno specifico.

**Parametri:**  
- `data` *(np.ndarray)*: Dataset.
- `game_name` *(str)*: Nome del videogioco.
- `year` *(int)*: Anno di riferimento.

**Ritorna:**  
- `float`: Vendite globali del gioco in quell'anno.

---

## 📂 Funzione: `top_platform_by_sales(data)`

**Descrizione:**  
Trova la piattaforma con il numero più alto di vendite globali.

**Parametri:**  
- `data` *(np.ndarray)*: Dataset.

**Ritorna:**  
- `tuple`: Nome della piattaforma e totale vendite globali.

---

## 📂 Funzione: `top_publisher_by_sales(data)`

**Descrizione:**  
Trova il publisher con il numero più alto di vendite globali.

**Parametri:**  
- `data` *(np.ndarray)*: Dataset.

**Ritorna:**  
- `tuple`: Nome del publisher e vendite totali.

---

## 📂 Funzione: `top_genre_by_sales(data)`

**Descrizione:**  
Restituisce il genere con le vendite globali più alte.

**Parametri:**  
- `data` *(np.ndarray)*: Dataset.

**Ritorna:**  
- `tuple`: Genere e vendite totali.

---

## 📂 Funzione: `avarage_sales_by_genre(data)`

**Descrizione:**  
Calcola la media delle vendite globali per ciascun genere.

**Parametri:**  
- `data` *(np.ndarray)*: Dataset.

**Ritorna:**  
- `dict`: Dizionario con il genere come chiave e media vendite come valore.

---

## 📂 Funzione: `yearly_sales_by_platform(data, platform)`

**Descrizione:**  
Mostra l'andamento delle vendite annuali per una piattaforma.

**Parametri:**  
- `data` *(np.ndarray)*: Dataset.
- `platform` *(str)*: Nome della piattaforma.

**Ritorna:**  
- `dict`: Anno → vendite globali.

---

## 📂 Funzione: `yearly_min_sales_by_publisher(data, publisher)`

**Descrizione:**  
Mostra le vendite minime per anno da parte di un publisher.

**Parametri:**  
- `data` *(np.ndarray)*: Dataset.
- `publisher` *(str)*: Nome del publisher.

**Ritorna:**  
- `dict`: Anno → vendita minima.

---

## 📂 Funzione: `top_10_games(data)`

**Descrizione:**  
Restituisce i 10 giochi con le vendite globali più alte.

**Parametri:**  
- `data` *(np.ndarray)*: Dataset.

**Ritorna:**  
- `np.ndarray`: Array con i 10 giochi più venduti.

---

## 🧩 Funzione: `main()`

**Descrizione:**  
Menu interattivo per accedere alle analisi disponibili.

**Funzionalità:**  
- Avvia un ciclo `while True` che presenta un menu.
- Usa `match-case` per gestire l'opzione selezionata dall'utente.

---

## ✅ Esecuzione del programma

La funzione `main()` viene eseguita solo se lo script è eseguito direttamente:

```python
if __name__ == "__main__":
    main()
```
