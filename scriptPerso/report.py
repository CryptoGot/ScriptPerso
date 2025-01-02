def generate_report(dataframe, output_file):
    """
    Génère un rapport récapitulatif des stocks par catégorie.
    :param dataframe: DataFrame contenant les données.
    :param output_file: Chemin du fichier CSV pour enregistrer le rapport.
    """
    try:
        report = dataframe.groupby('category').agg({
            'quantity': 'sum',
            'price': 'mean'
        })
        report.to_csv(output_file)
        print(f"Rapport généré dans : {output_file}")
    except Exception as e:
        print(f"Erreur lors de la génération du rapport : {e}")
