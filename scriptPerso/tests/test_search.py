import unittest
import pandas as pd

class TestSearch(unittest.TestCase):
    def test_search_product_not_found(self):
        data = pd.DataFrame({
            'product': ['A', 'B'],
            'category': ['cat1', 'cat2'],
            'quantity': [10, 20],
            'price': [50, 100]
        })

        result = data[data['product'] == 'Z']  # Produit inexistant
        self.assertTrue(result.empty)  # Le résultat doit être vide

    def test_search_category_not_found(self):
        data = pd.DataFrame({
            'product': ['A', 'B'],
            'category': ['cat1', 'cat2'],
            'quantity': [10, 20],
            'price': [50, 100]
        })

        result = data[data['category'] == 'cat3']  # Catégorie inexistante
        self.assertTrue(result.empty)  # Le résultat doit être vide
