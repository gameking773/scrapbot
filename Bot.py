from seleniumbase import BaseCase
from seleniumbase import SB


with SB() as sb:

    url = "https://www.leboncoin.fr/"
    urlRecherche = "https://www.leboncoin.fr/recherche?text=cible+avec+flechette"

    sb.activate_cdp_mode(urlRecherche)
    sb.sleep(2)
    sb.solve_captcha()

    # Ce sleep sert à la réalisation des Captchas par l'utilisateur
    sb.sleep(20)

