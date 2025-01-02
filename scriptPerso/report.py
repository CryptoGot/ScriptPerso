def generate_report(dataframe, output_file):
    """
    Génère un rapport récapitulatif des stocks par catégorie.

    Préconditions :
    - `dataframe` est un DataFrame contenant
    les colonnes 'category', 'quantity' et 'price'.
    - `output_file` est un chemin valide pour enregistrer le fichier CSV.

    Postconditions :
    - Génère un fichier CSV avec le rapport.

    Exceptions levées :
    - KeyError : Si les colonnes nécessaires sont absentes.
    - IOError : Si le fichier ne peut pas être créé ou écrit.
    """
    try:
        report = dataframe.groupby('category').agg({
            'quantity': 'sum',
            'price': 'mean'
        })
        report.to_csv(output_file)
        print(f"Rapport généré dans : {output_file}")
    except KeyError as ke:
        print(f"Erreur : Colonnes manquantes dans le DataFrame ({ke}).")
        raise
    except IOError as ioe:
        print(f"Erreur : Impossible d'écrire dans le fichier ({ioe}).")
        raise
