import csv
import matplotlib.pyplot as plt

# BAR CHAR EXEMPLE

# dataset a /data/natgas.csv

#global constants
DATASET_PATH = "../data/"
DATASET_FILE_NAME = "natgas"
DATASET_FILE_EXTENSION = ".csv"

#filters
YEAR_TIME = 2021
DATATYPE = "BALANCE"
PRODUCT = "NATGASCM"
FLOW = "GDINCTRO"
COUNTRIES = ["AUSTRIA", "BELGIUM", "DENMARK", "FINLAND", "FRANCE", "GERMANY", "GREECE", "HUNGARY", "IRELAND",
             "ITALY", "CZECH", "NETHLAND", "NORWAY", "POLAND", "PORTUGAL", "SLOVENIA", "SPAIN",
             "SWEDEN", "SWITLAND", "UK"]

# Funció que llegeix el fitxer CSV amb una ',' com a separador i filtra els registres quedant-se amb els que compleixen
# 1. PRODUCT = NATGASCM (producte comú a tots de gas natural)
# 2. DATATYPE = BALANCE (volem un balanç)
# 3. COUNTRY, agafem 20 països europeus importants per reduir les categories:
    # 1.AUSTRIA
    # 2.BELGIUM
    # 3.CZECH
    # 4.DENMARK
    # 5.FINLAND
    # 6.FRANCE
    # 7.GERMANY
    # 8.GREECE
    # 9.HUNGARY
    # 10.IRELAND
    # 11.ITALY
    # 12.NETHLAND
    # 13.NORWAY
    # 14.POLAND
    # 15.PORTUGAL
    # 16.SLOVENIA
    # 17.SPAIN
    # 18.SWEDEN
    # 19.SWITLAND
    # 20.UK
# 4. FLOW = GDINCTRO (interessa mostrar el balanç de les entregues interiors brutes)
# 5. TIME = 2021 (acotem els resultats només per l'any 2021)
# Finalment, es crea i retorna un diccionari amb els resultats dels registres filtrats on 'COUNTRY' es la key i 'value' la value
def readCSV():
    results_data = {}
    # obrim fitxer .csv i el llegim
    with open(DATASET_PATH + DATASET_FILE_NAME + DATASET_FILE_EXTENSION, "r") as dataset_file:
        reader = csv.DictReader(dataset_file)
        # Si el registre supera les condicions del filtre
        for registre in reader:
            if (registre["TIME"] == str(YEAR_TIME) and
                    registre["DATATYPE"] == DATATYPE and
                    registre["PRODUCT"] == PRODUCT and
                    registre["FLOW"] == FLOW and
                    registre["COUNTRY"] in COUNTRIES):

                # capturem pais i valor de producció de GN
                country = registre["COUNTRY"]
                value = float(registre["VALUE"])
                # ho afegim al diccionari de valors, si la clau ja existeix, realitzem un sumatori (no hauria de passar)
                if country in results_data:
                    results_data[country] = value
                else:
                    results_data[country] = value

    return results_data

# Funció que realitza la generació del diagrama de barres a partir de les dades obtingudes dels països
# El diagrama de barres conté barres verticals i de color blau
def plot_bar_chart(results):
    # Obtenim, del diccionari de resultats, les categories (països) i els valors
    countries = list(results.keys())
    values = list(results.values())

    # Generem el diagrama de barres verticals
    # Mida de la figura
    plt.figure(figsize=(14, 7))
    # Barres verticales de color blau
    plt.bar(countries, values, color='blue')
    # labels eixos 'x' i 'y' en negreta
    plt.xlabel('PAÏSOS', fontweight='bold')
    plt.ylabel('VALOR', fontweight='bold')
    # títol
    plt.title("Balanç de producció de GAS NATURAL en 20 països europeus durant l'any 2021")
    plt.xticks(rotation=45)  # Rotación de etiquetas de países para mejor visualización
    # ajustament
    plt.tight_layout()
    # Mostra
    plt.show()

def main(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'EXEMPLE {name}\n')

    dataset = DATASET_PATH+DATASET_FILE_NAME+DATASET_FILE_EXTENSION

    print("Visualització que mostra el balanç de les entregues interiors brutes comercialitzables de GAS NATURAL en 20 països europeus durant l'any 2021.")

    print(f'dataset emprat -->: {dataset}')

    # Crida de la funció que llegeix el fitxer de dades, filtra els registres que ens interessen i retorna el diccionari de valors
    data_result = readCSV()
    print("Resultats filtrats:", data_result)

    plot_bar_chart(data_result)



main("DIAGRAMA DE BARRES")



