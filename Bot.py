from seleniumbase import SB

with SB() as sb:

    url = "https://www.leboncoin.fr"
    urlRecherche = "https://www.leboncoin.fr/recherche?text=cible+avec+flechette"

    sb.activate_cdp_mode(urlRecherche)
    sb.sleep(2)
    sb.solve_captcha()

    # Ce sleep sert à la réalisation des Captchas par l'utilisateur
    sb.sleep(10)

    annonces = sb.find_elements("article")
    resultat = []

    for annonce in annonces:
        resAnnonce = {}
        # Extraction du Titre
        spanTitre = annonce.querySelector("span[title*='Voir l’annonce']")
        titre = spanTitre.get_attribute("title").replace("Voir l’annonce: ", "")
        resAnnonce["Titre"]= titre

        # Extraction du prix
        pPrix = annonce.querySelector('p[data-test-id="price"] span')
        resAnnonce["Prix"] = pPrix.text.replace('\xa0', ' ')

        # Extraction de l'URL
        ancreUrl = annonce.querySelector("a")
        lien = ancreUrl.get_attribute("href")
        resAnnonce["Lien"]= url+lien

        resultat.append(resAnnonce)

        # Slicing des 10 premiers url
    resultat = resultat[:10]


    print(resultat)