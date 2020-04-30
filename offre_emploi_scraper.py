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
import time
import pandas
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd
import csv

entree_contrat_not_ok=True
choix_lieu_not_ok=True
entree_lieu_not_ok=True

mot_cle=input('Entrez le mot clé qui doit être contenu dans le titre de l\’offre: ')
while entree_contrat_not_ok:
    entree_contrat=input('Choisissez le type de contrat recherché:\n1-CDI\n2-CDD\n3-CDI Alternance - Contrat d\'apprentissage\n4-CDI Alternance - Contrat de professionalisation\n5-CDD Alternance - Contrat d\'apprentissage\n6-CDD Alternance - Contrat de professionalisation\n7-CDI Intérimaire\n8-Mission d\'intérim\nEntrez le numéro correspondant: ')
    if entree_contrat=='1':
        type_contrat='101888'
        entree_contrat_not_ok=False
    elif entree_contrat=='2':
        type_contrat='101887'
        entree_contrat_not_ok=False
    elif entree_contrat=='3':
        type_contrat='597139'
        entree_contrat_not_ok=False
    elif entree_contrat=='4':
        type_contrat='597140'
        entree_contrat_not_ok=False
    elif entree_contrat=='5':
        type_contrat='597137'
        entree_contrat_not_ok=False
    elif entree_contrat=='6':
        type_contrat='597138'
        entree_contrat_not_ok=False
    elif entree_contrat=='7':
        type_contrat='597141'
        entree_contrat_not_ok=False
    elif entree_contrat=='8':
        type_contrat='101889'
        entree_contrat_not_ok=False
    else:
        entree_contrat_not_ok=True

while choix_lieu_not_ok:
    choix_lieu=input('Souhaitez-vous chercher par région(1) ou par département(2)? ')
    if choix_lieu == '1':
        choix_lieu_not_ok = False
        while entree_lieu_not_ok:
            entree_lieu=input('Choisissez la région souhaitée:\n1-Auvergne-Rhône-Alpes\n2-Bourgogne-Franche-Comté\n3-Bretagne\n4-Centre-Val de Loire\n5-Corse\n6-Grand Est\n7-Hauts-de-France\n8-Île-de-France\n9-Normandie\n10-Nouvelle-Aquitaine\n11-Occitanie\n12-Pays de la Loire\n13-Provence-Alpes-Côte d\’Azur\n14-Guadeloupe\n15-Martinique\n16-Guyane\n17-La Réunion\n18-Mayotte\nEntrez le numéro correspondant: ')
            if entree_lieu=='1':
                ville='20049'
                entree_lieu_not_ok=False
            elif entree_lieu == '2':
                ville ='20071'
                entree_lieu_not_ok = False
            elif entree_lieu == '3':
                ville ='705'
                entree_lieu_not_ok = False
            elif entree_lieu == '4':
                ville ='20070'
                entree_lieu_not_ok = False
            elif entree_lieu == '5':
                ville ='20'
                entree_lieu_not_ok = False
            elif entree_lieu == '6':
                ville ='20074'
                entree_lieu_not_ok = False
            elif entree_lieu == '7':
                ville ='20073'
                entree_lieu_not_ok = False
            elif entree_lieu == '8':
                ville ='711'
                entree_lieu_not_ok = False
            elif entree_lieu == '9':
                ville ='20072'
                entree_lieu_not_ok = False
            elif entree_lieu == '10':
                ville ='20075'
                entree_lieu_not_ok = False
            elif entree_lieu == '11':
                ville ='20076'
                entree_lieu_not_ok = False
            elif entree_lieu == '12':
                ville ='717'
                entree_lieu_not_ok = False
            elif entree_lieu == '13':
                ville ='720'
                entree_lieu_not_ok = False
            elif entree_lieu == '14':
                ville ='97100'
                entree_lieu_not_ok = False
            elif entree_lieu == '15':
                ville ='97200'
                entree_lieu_not_ok = False
            elif entree_lieu == '16':
                ville ='97300'
                entree_lieu_not_ok = False
            elif entree_lieu == '17':
                ville ='97400'
                entree_lieu_not_ok = False
            elif entree_lieu == '18':
                ville ='97600'
                entree_lieu_not_ok = False
            else:
                entree_lieu_not_ok=True
    elif choix_lieu == '2':
        choix_lieu_not_ok = False
        while entree_lieu_not_ok:
            entree_lieu = input('Choisissez le département souhaité:\n01-Ain\n02-Aisne\n03-Allier\n04-Alpes-de-Haute-Provence\n05-Hautes-alpes\n06-Alpes-maritimes\n07-Ardèche\n08-Ardennes\n09-Ariège\n10-Aube\n11-Aude\n12-Aveyron\n13-Bouches-du-Rhône\n14-Calvados\n15-Cantal\n16-Charente\n17-Charente-maritime\n18-Cher\n19-Corrèze\n2A-Corse-du-sud\n2B-Haute-Corse\n21-Côte-d\'Or\n22-Côtes-d\'Armor\n23-Creuse\n24-Dordogne\n25-Doubs\n26-Drôme\n27-Eure\n28-Eure-et-loir\n29-Finistère\n30-Gard\n31-Haute-garonne\n32-Gers\n33-Gironde\n34-Hérault\n35-Ille-et-vilaine\n36-Indre\n37-Indre-et-loire\n38-Isère\n39-Jura\n40-Landes\n41-Loir-et-cher\n42-Loire\n43-Haute-loire\n44-Loire-atlantique\n45-Loiret\n46-Lot\n47-Lot-et-garonne\n48-Lozère\n49-Maine-et-loire\n50-Manche\n51-Marne\n52-Haute-marne\n53-Mayenne\n54-Meurthe-et-moselle\n55-Meuse\n56-Morbihan\n57-Moselle\n58-Nièvre\n59-Nord\n60-Oise\n61-Orne\n62-Pas-de-calais\n63-Puy-de-dôme\n64-Pyrénées-atlantiques\n65-Hautes-Pyrénées\n66-Pyrénées-orientales\n67-Bas-rhin\n68-Haut-rhin\n69-Rhône\n70-Haute-saône\n71-Saône-et-loire\n72-Sarthe\n73-Savoie\n74-Haute-savoie\n75-Paris\n76-Seine-maritime\n77-Seine-et-marne\n78-Yvelines\n79-Deux-sèvres\n80-Somme\n81-Tarn\n82-Tarn-et-Garonne\n83-Var\n84-Vaucluse\n85-Vendée\n86-Vienne\n87-Haute-vienne\n88-Vosges\n89-Yonne\n90-Territoire de belfort\n91-Essonne\n92-Hauts-de-seine\n93-Seine-Saint-Denis\n94-Val-de-marne\n95-Val-d\'Oise\n971-Guadeloupe\n972-Martinique\n973-Guyane\n974-La réunion\n976-Mayotte\nEntrez le numéro du département: ')
            if entree_lieu=='01':
                ville='1'
                entree_lieu_not_ok=False
            elif entree_lieu == '02':
                ville ='2'
                entree_lieu_not_ok = False
            elif entree_lieu == '03':
                ville ='3'
                entree_lieu_not_ok = False
            elif entree_lieu == '04':
                ville ='4'
                entree_lieu_not_ok = False
            elif entree_lieu == '05':
                ville ='5'
                entree_lieu_not_ok = False
            elif entree_lieu == '06':
                ville ='6'
                entree_lieu_not_ok = False
            elif entree_lieu == '07':
                ville ='7'
                entree_lieu_not_ok = False
            elif entree_lieu == '08':
                ville ='8'
                entree_lieu_not_ok = False
            elif entree_lieu == '09':
                ville ='9'
                entree_lieu_not_ok = False
            elif entree_lieu == '10':
                ville ='10'
                entree_lieu_not_ok = False
            elif entree_lieu == '11':
                ville ='11'
                entree_lieu_not_ok = False
            elif entree_lieu == '12':
                ville ='12'
                entree_lieu_not_ok = False
            elif entree_lieu == '13':
                ville ='13'
                entree_lieu_not_ok = False
            elif entree_lieu == '14':
                ville ='14'
                entree_lieu_not_ok = False
            elif entree_lieu == '15':
                ville ='15'
                entree_lieu_not_ok = False
            elif entree_lieu == '16':
                ville ='16'
                entree_lieu_not_ok = False
            elif entree_lieu == '17':
                ville ='17'
                entree_lieu_not_ok = False
            elif entree_lieu == '18':
                ville ='18'
                entree_lieu_not_ok = False
            elif entree_lieu=='19':
                ville='19'
                entree_lieu_not_ok=False
            elif entree_lieu == '2A':
                ville ='750'
                entree_lieu_not_ok = False
            elif entree_lieu == '2B':
                ville ='751'
                entree_lieu_not_ok = False
            elif entree_lieu == '21':
                ville ='21'
                entree_lieu_not_ok = False
            elif entree_lieu == '22':
                ville ='22'
                entree_lieu_not_ok = False
            elif entree_lieu == '23':
                ville ='23'
                entree_lieu_not_ok = False
            elif entree_lieu == '24':
                ville ='24'
                entree_lieu_not_ok = False
            elif entree_lieu == '25':
                ville ='25'
                entree_lieu_not_ok = False
            elif entree_lieu == '26':
                ville ='26'
                entree_lieu_not_ok = False
            elif entree_lieu == '27':
                ville ='27'
                entree_lieu_not_ok = False
            elif entree_lieu == '28':
                ville ='28'
                entree_lieu_not_ok = False
            elif entree_lieu == '29':
                ville ='29'
                entree_lieu_not_ok = False
            elif entree_lieu == '30':
                ville ='30'
                entree_lieu_not_ok = False
            elif entree_lieu == '31':
                ville ='31'
                entree_lieu_not_ok = False
            elif entree_lieu == '32':
                ville ='32'
                entree_lieu_not_ok = False
            elif entree_lieu == '33':
                ville ='33'
                entree_lieu_not_ok = False
            elif entree_lieu == '34':
                ville ='34'
                entree_lieu_not_ok = False
            elif entree_lieu == '35':
                ville ='35'
                entree_lieu_not_ok = False
            elif entree_lieu=='36':
                ville='36'
                entree_lieu_not_ok=False
            elif entree_lieu == '37':
                ville ='37'
                entree_lieu_not_ok = False
            elif entree_lieu == '38':
                ville ='38'
                entree_lieu_not_ok = False
            elif entree_lieu == '39':
                ville ='39'
                entree_lieu_not_ok = False
            elif entree_lieu == '40':
                ville ='40'
                entree_lieu_not_ok = False
            elif entree_lieu == '41':
                ville ='41'
                entree_lieu_not_ok = False
            elif entree_lieu == '42':
                ville ='42'
                entree_lieu_not_ok = False
            elif entree_lieu == '43':
                ville ='43'
                entree_lieu_not_ok = False
            elif entree_lieu == '44':
                ville ='44'
                entree_lieu_not_ok = False
            elif entree_lieu == '45':
                ville ='45'
                entree_lieu_not_ok = False
            elif entree_lieu == '46':
                ville ='46'
                entree_lieu_not_ok = False
            elif entree_lieu == '47':
                ville ='47'
                entree_lieu_not_ok = False
            elif entree_lieu == '48':
                ville ='48'
                entree_lieu_not_ok = False
            elif entree_lieu == '49':
                ville ='49'
                entree_lieu_not_ok = False
            elif entree_lieu == '50':
                ville ='50'
                entree_lieu_not_ok = False
            elif entree_lieu == '51':
                ville ='51'
                entree_lieu_not_ok = False
            elif entree_lieu == '52':
                ville ='52'
                entree_lieu_not_ok = False
            elif entree_lieu == '53':
                ville ='53'
                entree_lieu_not_ok = False
            elif entree_lieu == '54':
                ville ='54'
                entree_lieu_not_ok = False
            elif entree_lieu == '55':
                ville ='55'
                entree_lieu_not_ok = False
            elif entree_lieu == '56':
                ville ='56'
                entree_lieu_not_ok = False
            elif entree_lieu == '57':
                ville ='57'
                entree_lieu_not_ok = False
            elif entree_lieu == '58':
                ville ='58'
                entree_lieu_not_ok = False
            elif entree_lieu == '59':
                ville ='59'
                entree_lieu_not_ok = False
            elif entree_lieu == '60':
                ville ='60'
                entree_lieu_not_ok = False
            elif entree_lieu == '61':
                ville ='61'
                entree_lieu_not_ok = False
            elif entree_lieu == '62':
                ville ='62'
                entree_lieu_not_ok = False
            elif entree_lieu == '63':
                ville ='63'
                entree_lieu_not_ok = False
            elif entree_lieu == '64':
                ville ='64'
                entree_lieu_not_ok = False
            elif entree_lieu == '65':
                ville ='65'
                entree_lieu_not_ok = False
            elif entree_lieu == '66':
                ville ='66'
                entree_lieu_not_ok = False
            elif entree_lieu == '67':
                ville ='67'
                entree_lieu_not_ok = False
            elif entree_lieu == '68':
                ville ='68'
                entree_lieu_not_ok = False
            elif entree_lieu == '69':
                ville ='69'
                entree_lieu_not_ok = False
            elif entree_lieu == '70':
                ville ='70'
                entree_lieu_not_ok = False
            elif entree_lieu=='71':
                ville='71'
                entree_lieu_not_ok=False
            elif entree_lieu == '72':
                ville ='72'
                entree_lieu_not_ok = False
            elif entree_lieu == '73':
                ville ='73'
                entree_lieu_not_ok = False
            elif entree_lieu == '74':
                ville ='74'
                entree_lieu_not_ok = False
            elif entree_lieu == '75':
                ville ='75'
                entree_lieu_not_ok = False
            elif entree_lieu == '76':
                ville ='76'
                entree_lieu_not_ok = False
            elif entree_lieu == '77':
                ville ='77'
                entree_lieu_not_ok = False
            elif entree_lieu == '78':
                ville ='78'
                entree_lieu_not_ok = False
            elif entree_lieu == '79':
                ville ='79'
                entree_lieu_not_ok = False
            elif entree_lieu == '80':
                ville ='80'
                entree_lieu_not_ok = False
            elif entree_lieu == '81':
                ville ='81'
                entree_lieu_not_ok = False
            elif entree_lieu == '82':
                ville ='82'
                entree_lieu_not_ok = False
            elif entree_lieu == '83':
                ville ='83'
                entree_lieu_not_ok = False
            elif entree_lieu == '84':
                ville ='84'
                entree_lieu_not_ok = False
            elif entree_lieu == '85':
                ville ='85'
                entree_lieu_not_ok = False
            elif entree_lieu == '86':
                ville ='86'
                entree_lieu_not_ok = False
            elif entree_lieu == '87':
                ville ='87'
                entree_lieu_not_ok = False
            elif entree_lieu == '88':
                ville ='88'
                entree_lieu_not_ok = False
            elif entree_lieu=='89':
                ville='89'
                entree_lieu_not_ok=False
            elif entree_lieu == '90':
                ville ='90'
                entree_lieu_not_ok = False
            elif entree_lieu == '91':
                ville ='91'
                entree_lieu_not_ok = False
            elif entree_lieu == '92':
                ville ='92'
                entree_lieu_not_ok = False
            elif entree_lieu == '93':
                ville ='93'
                entree_lieu_not_ok = False
            elif entree_lieu == '94':
                ville ='94'
                entree_lieu_not_ok = False
            elif entree_lieu == '95':
                ville ='95'
                entree_lieu_not_ok = False
            elif entree_lieu == '971':
                ville ='97100'
                entree_lieu_not_ok = False
            elif entree_lieu == '972':
                ville ='97200'
                entree_lieu_not_ok = False
            elif entree_lieu == '973':
                ville ='97300'
                entree_lieu_not_ok = False
            elif entree_lieu == '974':
                ville ='97400'
                entree_lieu_not_ok = False
            elif entree_lieu == '976':
                ville ='97600'
                entree_lieu_not_ok = False
            else:
                entree_lieu_not_ok=True
    else:
        choix_lieu_not_ok=True

temps_intervalle=input("Entrez le temps d'intervalle en heure: ")



while True:
    for pageNumber in range(0, 10):
        # specify the url
        urlpage = 'https://www.apec.fr/candidat/recherche-emploi.html/emploi?lieux=' + ville + '&motsCles=' + mot_cle + '&typesContrat=' + type_contrat + '&page='  + str(
            pageNumber)

        #option to not open a browser when the script is runned
        options = Options()
        options.headless = True

        # run chrome webdriver from executable path of your choice
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

        #lists to collect the wanted datas
        offers=[]
        companies=[]
        contracts=[]
        locations=[]
        dates=[]
        links=[]
        isOffertListed=False

         #to browse all the results in the page
        for div in container.findAll('div', attrs={'class':'card-body'}):
            # search the job title
            titre = div.find('h2', attrs={'class': 'card-title'})
            # search the company name
            entreprise = div.find('p', attrs={'class': 'card-offer__company'})
            # to acceed the list containing the others infos
            ul = div.find('ul', attrs={'class': 'important-list'})
            # search the type of contract
            contrat = ul.findChildren()[0]
            # search the job location
            lieu = ul.findChildren()[2]
            # search the publication date of the offer
            date = ul.findChildren()[4]
            # to acceed the tag containing the link of the offer
            a = div.findParents()[2]
            lien = "https://www.apec.fr" + a.get('href')
            try:
                with open('rechercheEmploi.csv') as recherche:
                    dataFrame=pandas.read_csv('rechercheEmploi.csv')
                    search = csv.reader(recherche)
                    emploi=[titre.text, entreprise.text, contrat.text, lieu.text, date.text]
                    for row in search:
                        temp=[]
                        temp.append(row[0])
                        temp.append(row[1])
                        temp.append(row[2])
                        temp.append(row[3])
                        temp.append(row[4])
                        print('temp = ', temp, ' emploi = ', emploi)
                        if temp == emploi:
                            isOffertListed=True

            except:
                isOffertListed=False

            if isOffertListed==False:
                offers.append(titre.text)
                companies.append(entreprise.text)
                contracts.append(contrat.text)
                locations.append(lieu.text)
                dates.append(date.text)
                links.append(lien)
            else:
                break

        if len(links)!=0:
            # store the collected datas in a cvs table (can use to_excel)
            df = pd.DataFrame(
                {'Poste': offers, 'Entreprise': companies, 'Type de contrat': contracts, 'Lieu': locations,
                 'Date de publication': dates, 'Lien de l\'offre': links})
            df.to_csv('rechercheEmploi.csv', index=False, encoding='utf-8', mode='a')

    #to pause the execution
    time.sleep(3600 * float(temps_intervalle))





