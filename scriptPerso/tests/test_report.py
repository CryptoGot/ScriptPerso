import unittest
import pandas as pd
from report import generate_report

class TestReport(unittest.TestCase):
    def test_generate_report(self):
        # Données d'exemple
        data = pd.DataFrame({
            'product': ['A', 'B', 'C'],
            'category': ['cat1', 'cat1', 'cat2'],
            'quantity': [10, 20, 5],
            'price': [50, 100, 200]
        })

        # Nom du fichier temporaire
        output_file = 'test_report.csv'

        # Appeler la fonction
        generate_report(data, output_file)

        # Vérifier que le fichier a été généré
        result = pd.read_csv(output_file)
        self.assertEqual(len(result), 2)  # Deux catégories : cat1 et cat2
        self.assertTrue('quantity' in result.columns)
        self.assertTrue('price' in result.columns)

if __name__ == "__main__":
    unittest.main()
