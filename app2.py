import meilisearch
from sqlalchemy import create_engine, MetaData, Table
from flask import Flask, jsonify, request

client = meilisearch.Client('http://localhost:7700')

db_url = "mysql+pymysql://root:root@127.0.0.1:3306/9mois"
engine = create_engine(db_url)
metadata = MetaData()

def meilei_add(table, list_col):
    '''table est une chaîne avec le nom de la table à ajouter, list_col est une liste de chaînes représentant les colonnes sélectionnées à indexer'''
    table_obj = Table(table, metadata, autoload_with=engine)
    with engine.connect() as connection:
        result_set = connection.execute(table_obj.select()).fetchall()
    documents = []
    for row in result_set:
        document = {column.name: getattr(row, column.name) for column in table_obj.columns if column.name in list_col}
        documents.append(document)
    # contournement pour la table 'food'
    if table == 'food':
        client.index(table).update(primary_key='code')
    client.index(table).add_documents(documents)

# Liste des colonnes récupérées
list_recipes = ['id', 'name', 'budget', 'difficulty', 'food']
list_articles = ['id', 'title', 'content']
list_food = ['code', 'name']
list_questions = ['id', 'question', 'answer', 'url_article']

# Ajout des tables à MeiliSearch
meilei_add('recipes', list_recipes)
meilei_add('articles', list_articles)
meilei_add('food', list_food)
meilei_add('questions', list_questions)

app = Flask(__name__)

@app.route("/")
def moteur_de_recherche():
    search_query = request.args.get('q', '')  # Obtenir le paramètre 'q' de l'URL, en utilisant une chaîne vide comme valeur par défaut
    index_name = request.args.get('index', '')  # Obtenir le paramètre 'index' de l'URL pour spécifier l'index à rechercher

    if not index_name:
        
        return jsonify({"erreur": "Veuillez fournir le paramètre 'index' pour spécifier l'index à rechercher"}), 400

    if search_query:
        resultats_recherche = client.index(index_name).search(search_query, {'limit': 10})
        return jsonify(resultats_recherche)
    else:
        return jsonify({"erreur": "Aucune requête de recherche fournie"}), 400

if __name__ == "__main__":
    app.run(debug=True)
