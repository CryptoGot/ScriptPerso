import unittest
import pandas as pd


class TestSearch(unittest.TestCase):
    """
    Classe de tests pour les fonctionnalités
    de recherche de produits et catégories.
    """

    def test_search_product_not_found(self):
        """
        Teste la recherche d'un produit inexistant dans le DataFrame.

        Préconditions :
        - Le DataFrame contient des colonnes valides avec des données.
        - Le produit recherché n'existe pas dans les données.

        Postconditions :
        - Retourne un DataFrame vide pour un produit inexistant.

        Exceptions levées :
        - AssertionError : Si le résultat n'est pas un DataFrame vide.
        """
        # Crée un DataFrame avec des données valides
        data = pd.DataFrame({
            'product': ['A', 'B'],
            'category': ['cat1', 'cat2'],
            'quantity': [10, 20],
            'price': [50, 100]
        })

        # Recherche un produit inexistant
        try:
            result = data[data['product'] == 'Z']  # Produit inexistant
            self.assertTrue(
                result.empty,
                "Le résultat doit être vide pour un produit inexistant.")
        except KeyError:
            self.fail("Colonne 'product' manquante dans le DataFrame.")

    def test_search_category_not_found(self):
        """
        Teste la recherche d'une catégorie inexistante dans le DataFrame.

        Préconditions :
        - Le DataFrame contient des colonnes valides avec des données.
        - La catégorie recherchée n'existe pas dans les données.

        Postconditions :
        - Retourne un DataFrame vide pour une catégorie inexistante.

        Exceptions levées :
        - AssertionError : Si le résultat n'est pas un DataFrame vide.
        """
        # Crée un DataFrame avec des données valides
        data = pd.DataFrame({
            'product': ['A', 'B'],
            'category': ['cat1', 'cat2'],
            'quantity': [10, 20],
            'price': [50, 100]
        })

        # Recherche une catégorie inexistante
        try:
            result = data[data['category'] == 'cat3']  # Catégorie inexistante
            self.assertTrue(
                result.empty,
                "Le résultat doit être vide pour une catégorie inexistante.")
        except KeyError:
            self.fail("Colonne 'category' manquante dans le DataFrame.")


if __name__ == "__main__":
    unittest.main()
