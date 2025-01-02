import unittest
import pandas as pd
from inventory_manager import read_and_merge_csv


class TestInventory(unittest.TestCase):
    def test_read_and_merge_csv(self):
        # Données d'exemple
        csv1 = pd.DataFrame({'product': ['A'], 'category': ['cat1'], 'quantity': [10], 'price': [50]})
        csv2 = pd.DataFrame({'product': ['B'], 'category': ['cat2'], 'quantity': [5], 'price': [150]})
        
        # Sauvegarder les DataFrames en CSV temporaires
        csv1.to_csv('test1.csv', index=False)
        csv2.to_csv('test2.csv', index=False)

        # Test de fusion
        result = read_and_merge_csv(['test_data/test1.csv', 'test_data/test2.csv'])
        self.assertEqual(len(result), 2)
        self.assertEqual(result.iloc[0]['product'], 'A')
    
    def test_missing_file(self):
        result = read_and_merge_csv(['nonexistent.csv'])
        self.assertTrue(result.empty)  # Le DataFrame doit être vide si le fichier est introuvable


    def test_empty_file(self):
        # Crée un fichier CSV vide
        open('empty.csv', 'w').close()

        result = read_and_merge_csv(['test_data/empty.csv'])
        self.assertEqual(len(result), 0)  # Le DataFrame doit être vide

    def test_missing_columns(self):
        # Crée un fichier CSV avec des colonnes manquantes
        data = pd.DataFrame({'product': ['A'], 'category': ['cat1']})
        data.to_csv('missing_columns.csv', index=False)

        result = read_and_merge_csv(['test_data/missing_columns.csv'])
        self.assertTrue(result.empty)  # Le DataFrame doit être vide si le fichier est introuvable



if __name__ == "__main__":
    unittest.main()
