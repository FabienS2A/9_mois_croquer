#Indexage de la base de donnée mysql de "9 mois à croquer"

##Variables d'environements

1. Créer un fichier .env dans le dossier 'components'

Dans .env, créer les variables d'environement propre.

meili_client=http://localhost:7700 'URL pour le fonctionement en local du moteur'
meili_key= 'meilisearch main key, clée obtenue au premier lancement de meilisearch https://www.meilisearch.com/docs/learn/cookbooks/docker'
sqldb=mysql+pymysql://[ID mysql]:[password mysql]@[data base URL] 'à renseigner sans les crochets'

2. Lancer le programme : "fetch_sqldb.py

Vérification de l'indexage :

En local, se rendre sur "http://localhost:7700" et vérifier le bonne indexages des 4 tables, "recipes", "articles", "food", "questions"


