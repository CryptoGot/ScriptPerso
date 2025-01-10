import unittest
import pandas as pd
import sys
import os

# Ajouter le chemin du module parent
sys.path.append(os.path.abspath(".."))

from inventory_manager import search_by_product, search_by_category


class TestSearch(unittest.TestCase):
    """
    Classe de tests pour les fonctionnalités de recherche de produits et catégories.
    """

    @classmethod
    def setUpClass(cls):
        """
        Configure les données communes à tous les tests.
        """
        cls.data = pd.DataFrame({
            'product': ['A', 'B', 'C', 'D'],
            'category': ['cat1', 'cat1', 'cat2', 'cat3'],
            'quantity': [10, 5, 20, 15],
            'price': [50, 100, 200, 150]
        })

    def test_search_product_found(self):
        """
        Teste la recherche d'un produit existant.
        """
        result = search_by_product(self.data, 'A')
        self.assertEqual(len(result), 1)
        self.assertEqual(result.iloc[0]['product'], 'A')

    def test_search_product_not_found(self):
        """
        Teste la recherche d'un produit inexistant.
        """
        result = search_by_product(self.data, 'Z')
        self.assertTrue(result.empty)

    def test_search_category_found(self):
        """
        Teste la recherche d'une catégorie existante.
        """
        result = search_by_category(self.data, 'cat1')
        self.assertEqual(len(result), 2)
        self.assertTrue(all(result['category'] == 'cat1'))

    def test_search_category_not_found(self):
        """
        Teste la recherche d'une catégorie inexistante.
        """
        result = search_by_category(self.data, 'cat4')
        self.assertTrue(result.empty)

if __name__ == "__main__":
    unittest.main()
