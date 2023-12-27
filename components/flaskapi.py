import meilisearch
from sqlalchemy import create_engine, MetaData, Table
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")
def moteur_de_recherche():
    search_query = request.args.get('q', '')  # Obtenir le paramètre 'q' de l'URL, en utilisant une chaîne vide comme valeur par défaut

    if search_query:
        resultats_recherche = client.multi_search(
            [
                {'indexUid': 'food', 'q': search_query, 'limit': 10},
                {'indexUid': 'recipes', 'q': search_query, 'limit': 10},
                {'indexUid': 'articles', 'q': search_query, 'limit': 10},
                {'indexUid': 'questions', 'q': search_query, 'limit': 10}
            ]
        )
        return jsonify(resultats_recherche)
    else:
        return jsonify({"erreur": "Aucune requête de recherche fournie"}), 400

if __name__ == "__main__":
    app.run(debug=True)

