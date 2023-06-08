# Exemple d'un model de Scraping avec Python:

# Import des bibliothéques :

import requests
from bs4 import BeautifulSoup
import csv

# URL de la page internet à scraper :
url = "https://github.com/BelkacemAMR"

# Effectuer la requête HTTP:
response = requests.get(url)

# Parser le contenu HTML:
soup = BeautifulSoup(response.text, "html.parser")

# Trouver les éléments à extraire:
data = []
items = soup.find_all("div", class_="item")

for item in items:
    # Extraire les informations souhaitées:
    title = item.find("h2").text.strip()
    description = item.find("p").text.strip()

    # Ajouter les données à la liste:
    data.append([title, description])


# Écrire les données dans un fichier CSV:
output_file = "data.csv"
with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    # Écrire l'en-tête du CSV
    writer.writerow(["Title", "Description"])  
    # Écrire les données
    writer.writerows(data)  

print("Scraping terminé. Les données ont été enregistrées dans", output_file)
