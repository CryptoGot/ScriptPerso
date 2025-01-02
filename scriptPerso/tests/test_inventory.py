import unittest
import pandas as pd
from inventory_manager import read_and_merge_csv


class TestInventory(unittest.TestCase):
    """
    Tests pour les fonctionnalités liées à la gestion des fichiers CSV.
    """

    def test_read_and_merge_csv(self):
        """
        Teste la fusion de plusieurs fichiers CSV.

        Préconditions :
        - Les fichiers 'test_data/test1.csv'
        et 'test_data/test2.csv' existent et sont valides.

        Postconditions :
        - Le DataFrame fusionné contient les données des deux fichiers.
        - Le premier produit est 'A'.

        Exceptions levées :
        - AssertionError : Si la taille
        ou le contenu du DataFrame ne correspond pas aux attentes.
        """
        csv1 = pd.DataFrame({
            'product': ['A'],
            'category': ['cat1'],
            'quantity': [10],
            'price': [50]
        })
        csv2 = pd.DataFrame({
            'product': ['B'],
            'category': ['cat2'],
            'quantity': [5],
            'price': [150]
        })
        # Sauvegarder les DataFrames en fichiers CSV
        csv1.to_csv('test_data/test1.csv', index=False)
        csv2.to_csv('test_data/test2.csv', index=False)

        # Fusionner les fichiers CSV
        result = read_and_merge_csv(
            ['test_data/test1.csv', 'test_data/test2.csv'])
        self.assertEqual(len(result), 2)  # Vérifie le nombre de lignes
        self.assertEqual(result.iloc[0]['product'], 'A')  # Vérifie le contenu

    def test_missing_file(self):
        """
        Teste le comportement en cas de fichier manquant.

        Préconditions :
        - Le fichier 'nonexistent.csv' n'existe pas.

        Postconditions :
        - La fonction retourne un DataFrame vide.

        Exceptions levées :
        - AssertionError : Si le DataFrame retourné n'est pas vide.
        """
        result = read_and_merge_csv(['test_data/nonexistent.csv'])
        self.assertTrue(result.empty)  # Vérifie que le DataFrame est vide

    def test_empty_file(self):
        """
        Teste le comportement en cas de fichier CSV vide.

        Préconditions :
        - Le fichier 'test_data/empty.csv' est vide.

        Postconditions :
        - La fonction retourne un DataFrame vide.

        Exceptions levées :
        - AssertionError : Si le DataFrame retourné n'est pas vide.
        """
        # Crée un fichier CSV vide
        open('test_data/empty.csv', 'w').close()

        result = read_and_merge_csv(['test_data/empty.csv'])
        self.assertEqual(len(result), 0)  # Vérifie que le DataFrame est vide

    def test_missing_columns(self):
        """
        Teste le comportement en cas de colonnes manquantes.

        Préconditions :
        - Le fichier 'test_data/missing_columns.csv'
        ne contient pas toutes les colonnes nécessaires.

        Postconditions :
        - La fonction retourne un DataFrame vide.

        Exceptions levées :
        - AssertionError : Si le DataFrame retourné n'est pas vide.
        """
        data = pd.DataFrame(
            {'product': ['A'], 'category': ['cat1']})
        data.to_csv('test_data/missing_columns.csv', index=False)

        result = read_and_merge_csv(['test_data/missing_columns.csv'])
        self.assertTrue(result.empty)  # Vérifie que le DataFrame est vide


if __name__ == "__main__":
    unittest.main()
