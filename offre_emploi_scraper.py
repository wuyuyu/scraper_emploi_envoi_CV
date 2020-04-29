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

# query the website and return the html to the variable 'content'
driver.get(urlpage)
content = driver.page_source
#print(content)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(content,'html.parser')
#print(soup)

# find results avec les mots clé
container = soup.find('div', attrs={'class':'container-result'})
#results = container.find_all('div',attrs={'class':'card-body'})
#print(container)
#print('Number of results', len(results))
offers=[]
companies=[]
contracts=[]
locations=[]
dates=[]
for div in container.findAll('div', attrs={'class':'card-body'}):
    titre=div.find('h2', attrs={'class':'card-title'})
    offers.append(titre.text)
    entreprise=div.find('p', attrs={'class':'card-offer__company'})
    companies.append(entreprise.text)
    ul=div.find('ul', attrs={'class':'important-list'})
    contrat=ul.findChildren()[0]
    contracts.append(contrat.text)
    lieu=ul.findChildren()[2]
    locations.append(lieu.text)
    date=ul.findChildren()[4]
    dates.append(date.text)

df = pd.DataFrame({'Poste':offers,'Entreprise':companies,'Type de contrat':contracts,'Lieu':locations,'Date de publication':dates})
df.to_csv('rechercheEmploi.csv', index=False, encoding='utf-8')





