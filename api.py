import meilisearch
from sqlalchemy import create_engine, MetaData, Table
from flask import Flask, jsonify, request


from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='components/.env')
meili_env = os.getenv("meili_client")
meili_key = os.getenv("meili_key")
if meili_key == False :
        client = meilisearch.Client(meili_env)
else :
        client = meilisearch.Client(meili_env, meili_key)

app = Flask(__name__)

@app.route("/")
def moteur_de_recherche():
    search_query = request.args.get('q', '')  # Obtenir le paramètre 'q' de l'URL, en utilisant une chaîne vide comme valeur par défaut
    index_name = request.args.get('index', '')  # Obtenir le paramètre 'index' de l'URL pour spécifier l'index à rechercher

    if not index_name:
        
        resultats_sans_index = client.multi_search(
    [
        {'indexUid': 'food', 'q': search_query, 'limit': 50},
        {'indexUid': 'recipes', 'q': search_query, 'limit': 50},
        {'indexUid': 'articles', 'q': search_query, 'limit': 50},
        {'indexUid': 'questions', 'q': search_query, 'limit': 50}
    ]
)

        return jsonify(resultats_sans_index)

    if search_query:
        resultats_recherche = client.index(index_name).search(search_query, {'limit': 10})
        return jsonify(resultats_recherche)
    else:
        return jsonify({"erreur": "Aucune requête de recherche fournie"}), 400

if __name__ == "__main__":
    app.run(debug=True)

