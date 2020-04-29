"""

 Création d’Un script offre_emploi_scraper.py de scraper:
 Le script prend en paramètre:
     - Le mot clé qui doit être contenu dans le titre de l’offre
     - La ville ou le département
     - LE TEMPS d’intervalle en heure
 Le script retourne les résultats suivants:
     - Le titre de offre
     - Infos de Ville complet
     - La page de détails d’offre( Le mail de contact à voir)
     - Url du offre
     - La date de publication
     - l’entreprise
Le script va stocker les résultats dans un fichier de log

 """

#import libraries
import json
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd
import csv

#mot_cle=input("Entrez le mot clé qui doit être contenu dans le titre de l’offre: ")
#ville=input("Entrez la ville ou le département: ")
#type_contrat=input("Entrez le type de contrat: ")
#temps_intervalle=input("Entrez le temps d'intervalle en minutes: ")

# specify the url
urlpage = 'https://www.apec.fr/candidat/recherche-emploi.html/emploi?lieux=711&motsCles=d%C3%A9veloppeur&page=0'

options = Options()
options.headless = True

# run firefox webdriver from executable path of your choice
driver = webdriver.Chrome(options=options,executable_path=ChromeDriverManager().install())
driver.get(urlpage)

content = driver.page_source

# query the website and return the html to the variable 'page'
#page = urllib.request.urlopen(urlpage)
print(content)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(content,'html.parser')
#jpage = json.load(page)

#print(jpage)

# find results avec les mots clé
#container = soup.find_next_siblings('div', attrs={'class':'container-result'})
#results = soup.find_all('div',attrs={'class':'card-body'})

#print(container)

#print('Number of results', len(results))





