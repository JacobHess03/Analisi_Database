import csv
import numpy as np

# Percorso al file CSV contenente i dati sui videogiochi
csv_path = "videogame.csv"

def load_data(csv_path):
    """
    Carica il dataset dei videogiochi da un file CSV usando il modulo csv.
    Ritorna un ndarray strutturato con i campi:
    Name, Platform, Year, Genre, Publisher,
    NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales
    """
    # Definizione del tipo di dati per ogni colonna del dataset
    dtype = [("Name", "U100"), ("Platform", "U50"), ("Year", int),
             ("Genre", "U50"), ("Publisher", "U100"),
             ("NA_Sales", float), ("EU_Sales", float),
             ("JP_Sales", float), ("Other_Sales", float), ("Global_Sales", float)]

    records = []
    # Apertura del file CSV con encoding UTF-8
    with open(csv_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)  # Lettura del file come dizionario
        for row in reader:
            try:
                # Conversione e aggiunta di ogni riga al dataset
                record = (
                    row['Name'],
                    row['Platform'],
                    int(float(row['Year'])) if row['Year'] else 0,  # Gestione di valori mancanti
                    row['Genre'],
                    row['Publisher'],
                    float(row['NA_Sales'] or 0),
                    float(row['EU_Sales'] or 0),
                    float(row['JP_Sales'] or 0),
                    float(row['Other_Sales'] or 0),
                    float(row['Global_Sales'] or 0)
                )
                records.append(record)
            except ValueError:
                # Ignora righe con errori di conversione
                continue

    # Restituisce i dati come array strutturato di NumPy
    return np.array(records, dtype=dtype)

# Funzioni di analisi

def total_sales_region(data, region):
    """
    Calcola le vendite totali per una regione specifica.
    """
    if region not in data.dtype.names:
        raise ValueError(f"Regione sconosciuta: {region}")
    return np.sum(data[region])

def total_sales_for_game_year(data, game_name, year):
    """
    Calcola le vendite globali di un gioco specifico in un anno specifico.
    """
    mask = (data['Name'] == game_name) & (data['Year'] == year)
    if np.any(mask):
        return np.sum(data['Global_Sales'][mask])
    else:
        return 0.0

def top_platform_by_sales(data):
    """
    Determina la piattaforma con il maggior numero di vendite globali.
    """
    platforms = np.unique(data['Platform'])
    totals = {}
    for plat in platforms:
        totals[plat] = np.sum(data['Global_Sales'][data['Platform'] == plat])
        # Ordina le piattaforme in base alle vendite globali
    # best = max(totals, key=totals.get)
    # return best, totals[best]  # Restituisce la piattaforma con le vendite globali più alte e il totale delle vendite
    return max(totals, key=totals.get), totals[max(totals, key=totals.get)]

def top_publisher_by_sales(data):
    """
    Determina il publisher con il maggior numero di vendite globali.
    """
    pubs = np.unique(data['Publisher'])
    totals = {}
    for pub in pubs:
        totals[pub] = np.sum(data['Global_Sales'][data['Publisher'] == pub])
    return max(totals, key=totals.get), totals[max(totals, key=totals.get)]

def top_genre_by_sales(data):
    """
    Determina il genere con il maggior numero di vendite globali.
    """
    genres = np.unique(data['Genre'])
    totals = {}
    for g in genres:
        totals[g] = np.sum(data['Global_Sales'][data['Genre'] == g])
    return max(totals, key=totals.get), totals[max(totals, key=totals.get)]

def avarage_sales_by_genre(data):
    """
    Calcola le vendite medie per ogni genere.
    """
    genres = np.unique(data['Genre'])
    averages = {}
    for g in genres:
        averages[g] = np.mean(data['Global_Sales'][data['Genre'] == g])
    return averages

def yearly_sales_by_platform(data, platform):
    """
    Calcola le vendite annuali per una piattaforma specifica.
    """
    years = np.unique(data['Year'])
    trend = {}
    for y in years:
        mask = (data['Year'] == y) & (data['Platform'] == platform)
        if np.any(mask):
            trend[y] = np.sum(data['Global_Sales'][mask])
    return trend

def yearly_min_sales_by_publisher(data, publisher):
    """
    Calcola la vendita minima annuale per un publisher specifico.
    """
    years = np.unique(data['Year'])
    mins = {}
    for y in years:
        mask = (data['Year'] == y) & (data['Publisher'] == publisher)
        if np.any(mask):
            mins[y] = np.min(data['Global_Sales'][mask])
    return mins

def top_10_games(data):
    """
    Restituisce i 10 giochi con le vendite globali più alte.
    """
    sorted_data = np.sort(data, order='Global_Sales')[::-1]
    return sorted_data[:10]

# Menu interattivo con match-case

def main():
    """
    Menu interattivo per eseguire analisi sui dati dei videogiochi.
    """
    data = load_data(csv_path)  # Caricamento dei dati
    while True:
        # Stampa del menu
        print("\n--- MENU Analisi Videogiochi ---")
        print("1. Vendite totali per regione")
        print("2. Vendite totali di un gioco per anno")
        print("3. Piattaforma con più vendite")
        print("4. Publisher con più vendite")
        print("5. Genere più venduto")
        print("6. Vendite medie per genere")
        print("7. Tendenza vendite per piattaforma (per anno)")
        print("8. Vendita minima per publisher (per anno)")
        print("9. Top 10 giochi per vendite globali")
        print("0. Esci")
        choice = input("Seleziona un'opzione: ")

        # Gestione delle scelte con match-case
        match choice:
            case "1":
                region = input("Inserisci la regione (NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales): ")
                try:
                    result = total_sales_region(data, region)
                    print(f"Vendite totali in {region}: {result}")
                except ValueError as e:
                    print(e)

            case "2":
                game = input("Nome del gioco: ")
                year = int(input("Anno: "))
                result = total_sales_for_game_year(data, game, year)
                print(f"Vendite globali di {game} nel {year}: {result}")

            case "3":
                plat, sales = top_platform_by_sales(data)
                print(f"Piattaforma top: {plat} con {sales} mln")

            case "4":
                pub, sales = top_publisher_by_sales(data)
                print(f"Publisher top: {pub} con {sales} mln")

            case "5":
                gen, sales = top_genre_by_sales(data)
                print(f"Genere top: {gen} con {sales} mln")

            case "6":
                avgs = avarage_sales_by_genre(data)
                for g, m in avgs.items():
                    print(f"{g}: {m:.2f} mln")

            case "7":
                plat = input("Piattaforma: ")
                trend = yearly_sales_by_platform(data, plat)
                for y, t in trend.items():
                    print(f"{y}: {t}")

            case "8":
                publisher = input("Publisher: ")
                mins = yearly_min_sales_by_publisher(data, publisher)
                for y, m in mins.items():
                    print(f"{y}: {m}")

            case "9":
                top10 = top_10_games(data)
                for entry in top10:
                    print(f"{entry['Name']}: {entry['Global_Sales']}")

            case "0":
                print("Uscita...")
                break

            case _:
                print("Opzione non valida, riprova.")

# Punto di ingresso del programma
if __name__ == "__main__":
    main()