import streamlit as st
import requests

import streamlit as st
import requests

def run_meilisearch_frontend():
    
    def single_search(query, index_name):
        # Effectuer une recherche dans un seul index
        response = requests.get(f"http://localhost:5000/?q={query}&index={index_name}")
        return response.json()

    def multi_search(query):
        # Effectuer une recherche dans tous les index
        response = requests.get(f"http://localhost:5000/?q={query}")
        return response.json()

    st.title("MeiliSearch Frontend")

    # Zone de recherche
    search_query = st.text_input("Rechercher", "")

    # Sélection de l'index
    index_options = ["Tous les index", "food", "recipes", "articles", "questions"]
    index_name = st.selectbox("Sélectionner un index", index_options)

    # Bouton de recherche
    if st.button("Rechercher"):
        if not search_query:
            st.warning("Veuillez fournir une requête de recherche.")
        else:
            # Effectuer la recherche en fonction de l'index sélectionné
            if index_name == "Tous les index":
                results = multi_search(search_query)
            else:
                results = single_search(search_query, index_name)

            # Afficher les résultats
            st.json(results)

if __name__ == "__main__":
    run_meilisearch_frontend()


