Backlog



Création d’Un script offre_emploi_scraper.py de scraper:
Le script prend en paramètre:
    - Le mot clé qui doit être contenu dans le titre de l’offre
    - La ville ou le département 
    - Le type de contrat
    - LE TEMPS d’intervalle en heure
Le script retourne les résultats suivants:
    - Le titre de offre
    - Infos de Ville complet 
    - La page de détails d’offre( Le mail de contact à voir)
    - Url du offre
    - La date de publication
    - l’entreprise 
Le script va stocker les résultats dans un fichier de log


Création un script envoi_CV.py d’envoi dans le offre_emploi_scraper.py:
	Le script fait appel le script offre_emploi_scraper.py
	Le script prend en paramètres tous les paramètres du offre_emploi_scraper.py
	Le script prend en paramètre (en +) :
		- mail d’expéditeur
		- le fichier du CV 
		- le fichier du contenue du mail 		
	Le script va 
		- envoyer le CV 
		- afficher un message dans le console une fois que le CV est envoyé avec les infos necessaires (date, offre, etc…)
	une fois que les mail sont envoyés, loger les infos d’envoie dans un fichier de log 


Création d’un script de offre_emploi_supervision.py, ce script a pour le but de surveiller la taille des fichiers 
	Le script prend tous les paramètres du script offre_emploi_scraper.py ET La taille du fichier
	Le script arrête le script offre_emploi_scraper.py  quand la taille du fichier dépasse la taille rentré
	Le script va ensuite compresser le fichier log et le stocker dans un .zip
	le script va noté la date et heure de stockage 
	et il relance le script offre_emploi_scraper.py une fois tous ces processus sont terminés
