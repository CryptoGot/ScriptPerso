import unittest
import pandas as pd
from report import generate_report


class TestReport(unittest.TestCase):
    """
    Classe de tests pour les fonctionnalités de génération de rapports.
    """

    def test_generate_report_empty_data(self):
        """
        Teste la génération d'un rapport à partir d'un DataFrame vide.

        Préconditions :
        - Le DataFrame fourni est vide.
        - Le chemin du fichier de sortie est valide.

        Postconditions :
        - Le fichier CSV généré est vide.

        Exceptions levées :
        - AssertionError : Si le fichier généré n'est pas vide.
        """
        # Crée un DataFrame vide
        data = pd.DataFrame(
            columns=['product', 'category', 'quantity', 'price'])
        output_file = 'test_data/empty_report.csv'

        # Génère le rapport
        generate_report(data, output_file)

        # Vérifie que le fichier généré est vide
        try:
            result = pd.read_csv(output_file)
            self.assertTrue(result.empty)  # Le fichier généré doit être vide
        except FileNotFoundError:
            self.fail(f"Le fichier {output_file} n'a pas été créé.")

    def test_generate_report_calculations(self):
        """
        Teste la précision des calculs de quantité et de prix moyen.

        Préconditions :
        - Le DataFrame contient des colonnes valides avec des données.

        Postconditions :
        - Les colonnes 'quantity' et
        'price' du rapport sont correctement calculées.

        Exceptions levées :
        - AssertionError : Si les calculs dans le rapport ne sont pas corrects.
        """
        # Crée un DataFrame avec des données valides
        data = pd.DataFrame({
            'product': ['A', 'B', 'C'],
            'category': ['cat1', 'cat1', 'cat2'],
            'quantity': [10, 20, 5],
            'price': [50, 100, 200]
        })
        output_file = 'test_data/test_calculations_report.csv'

        # Génère le rapport
        generate_report(data, output_file)

        # Vérifie les calculs
        try:
            result = pd.read_csv(output_file)
            self.assertEqual(
                result[result['category'] == 'cat1']['quantity'].iloc[0], 30)
            self.assertEqual(
                result[result['category'] == 'cat1']['price'].iloc[0], 75)
        except FileNotFoundError:
            self.fail(f"Le fichier {output_file} n'a pas été créé.")
        except KeyError as e:
            self.fail(f"Colonne manquante dans le rapport : {e}")


if __name__ == "__main__":
    unittest.main()
