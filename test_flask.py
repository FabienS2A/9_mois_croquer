import pytest
from flask_testing import TestCase
from api import app

class TestMoteurDeRecherche(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_recherche_sans_index(self):
        response = self.client.get('/?q=test_query')
        data = response.get_json()

        assert response.status_code == 200
        assert 'food' in data
        assert 'recipes' in data
        assert 'articles' in data
        assert 'questions' in data

    def test_recherche_avec_index(self):
        response = self.client.get('/?q=test_query&index=food')
        data = response.get_json()

        assert response.status_code == 200
        assert 'hits' in data
        # Add more assertions based on the expected structure of the response

    def test_erreur_aucune_requete(self):
        response = self.client.get('/')
        data = response.get_json()

        assert response.status_code == 400
        assert 'erreur' in data
        assert data['erreur'] == 'Aucune requête de recherche fournie'

if __name__ == '__main__':
    pytest.main()
