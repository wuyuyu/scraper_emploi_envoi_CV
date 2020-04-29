import json
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver 

import geckodriver_autoinstaller
#from webdriver_manager.fireFox import ChromeDriverManager
from selenium.webdriver.firefox.options import Options
import pandas as pd
import csv
import time


mot_cle=input("Entrez le mot clé qui doit être contenu dans le titre de l’offre: ")
ville=input("Entrez la ville ou le département: ")
#type_contrat=input("Entrez le type de contrat: ")
temps_intervalle=input("Entrez le temps d'intervalle en : ")


while True:
	for pageNumber in range(0,10):
	# specify the url
		urlpage = 'https://www.apec.fr/candidat/recherche-emploi.html/emploi?lieux='+ville+'&motsCles='+mot_cle+'&page='+str(pageNumber)

		options = Options()
		options.headless = True
		#driver = webdriver.(options=options,executable_path=ChromeDriverManager().install())

		geckodriver_autoinstaller.install()
		driver = webdriver.Firefox(options=options)

		# query the website and return the html to the variable 'content'
		driver.get(urlpage)
		content = driver.page_source
		#print(content)

		soup = BeautifulSoup(content,'html.parser')
		#print(soup)

		# find results avec les mots clé
		container = soup.find('div', attrs={'class':'container-result'})
		titreListe=[]
		entrepriseListe=[]
		contratListe=[]
		lieuListe=[]
		dateListe=[]
		lienOffreListe=[]


		for div in container.find_all('div',attrs={'class':'card-body'}):
			titre=div.find('h2',attrs={'class':'card-title'})
			entreprise=div.find('p',attrs={'class':'card-offer__company'})
			ul=div.find('ul',attrs={'class':'important-list'})
			contrat=ul.findChildren()[0]
			lieu=ul.findChildren()[2]
			date=ul.findChildren()[4]
			lienOffre=div.findParents()[2] 


			titreListe.append(titre.text)
			entrepriseListe.append(entreprise.text)
			contratListe.append(contrat.text)
			lieuListe.append(lieu.text)
			dateListe.append(date.text)

			lienOffreUrl="https://www.apec.fr"+lienOffre.get('href')
			lienOffreListe.append(lienOffreUrl)

		df = pd.DataFrame({'titre':titreListe,'entreprise':entrepriseListe,'contrat':contratListe,'lieu':lieuListe,'date':dateListe,'lien Offre Url':lienOffreListe}) 
		df.to_csv('logs.csv', index=False, encoding='utf-8',mode='a')
		
	time.sleep(3600 * int(temps_intervalle))


















