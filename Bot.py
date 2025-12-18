from bs4 import BeautifulSoup
from seleniumbase import SB
import json

with SB() as sb:

    url = "https://www.leboncoin.fr"
    urlRecherche = "https://www.leboncoin.fr/recherche?text=cible+avec+flechette"

    # Initialisation
    sb.activate_cdp_mode(urlRecherche)

    html = sb.get_page_source()
    soup = BeautifulSoup(html, 'html.parser')

    annonces = soup.find_all("article")
    resultat = []

    for annonce in annonces:
        resAnnonce = {}

        # 1. Extraction du Titre
        span_titre = annonce.select_one("span[title*='Voir l’annonce']")
        resAnnonce["Titre"] = span_titre["title"].replace("Voir l’annonce: ", "")

        # 2. Extraction du Prix
        p_prix = annonce.select_one('p[data-test-id="price"]')
        resAnnonce["Prix"] = p_prix.get_text(strip=True).replace('\xa0', ' ')

        # 3. Extraction de la localisation
        infos = annonce.find_all("p")
        loc = "Non trouvée"
        for p in infos:
            texte = p.get_text()
            if "Située à" in texte:
                loc = texte.replace("Située à ", "").strip()
                break
        resAnnonce["Localisation"] = loc

        # 4. Extraction de l'URL
        lien = annonce.find("a")
        resAnnonce["Lien"] = url + lien["href"]

        resultat.append(resAnnonce)

    # Slicing des 10 premiers url
    resultat = resultat[:10]


# Transformation en json
    with open("annonces.json", "w", encoding="utf-8") as f:
        json.dump(resultat, f, indent=4, ensure_ascii=False)