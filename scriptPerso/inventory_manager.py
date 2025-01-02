import pandas as pd


def read_and_merge_csv(files):
    """
    Lit et fusionne plusieurs fichiers CSV en un seul DataFrame.
    :param files: Liste des chemins vers les fichiers CSV.
    :return: DataFrame fusionné ou DataFrame vide en cas d'erreur.
    """
    required_columns = {'product', 'category', 'quantity', 'price'}
    dataframes = []

    try:
        for file in files:
            try:
                # Lecture du fichier CSV
                df = pd.read_csv(file)
                # Vérifie si toutes les colonnes nécessaires sont présentes
                if not required_columns.issubset(df.columns):
                    print(f"Erreur : Colonnes manquantes dans le fichier : {file}")
                    return pd.DataFrame()  # Retourne un DataFrame vide
                # Ajoute le DataFrame à la liste
                dataframes.append(df)
            except pd.errors.EmptyDataError:
                print(f"Erreur : Le fichier {file} est vide.")
            except FileNotFoundError:
                print(f"Erreur : Le fichier {file} est introuvable.")
        # Fusionne tous les DataFrames
        if not dataframes:
            print("Erreur : Aucun fichier CSV valide trouvé.")
            return pd.DataFrame()  # Retourne un DataFrame vide si aucun fichier valide
        merged_df = pd.concat(dataframes, ignore_index=True)
        return merged_df
    except Exception as e:
        print(f"Erreur inattendue lors de la lecture ou de la fusion des fichiers CSV : {e}")
        return pd.DataFrame()  # Retourne un DataFrame vide en cas d'erreur


def search_by_category(dataframe, category):
    """
    Recherche toutes les lignes correspondant à une catégorie spécifique.
    :param dataframe: Le DataFrame contenant les données.
    :param category: La catégorie à rechercher.
    :return: Un DataFrame filtré par la catégorie ou un DataFrame vide si la catégorie n'existe pas.
    """
    try:
        filtered_df = dataframe[dataframe['category'] == category]
        if filtered_df.empty:
            print(f"Aucune donnée trouvée pour la catégorie : {category}")
        return filtered_df
    except KeyError:
        print("Erreur : La colonne 'category' est absente du DataFrame.")
        return pd.DataFrame()


def search_by_product(dataframe, product):
    """
    Recherche toutes les lignes correspondant à un produit spécifique.
    :param dataframe: Le DataFrame contenant les données.
    :param product: Le produit à rechercher.
    :return: Un DataFrame filtré par le produit ou un DataFrame vide si le produit n'existe pas.
    """
    try:
        filtered_df = dataframe[dataframe['product'] == product]
        if filtered_df.empty:
            print(f"Aucune donnée trouvée pour le produit : {product}")
        return filtered_df
    except KeyError:
        print("Erreur : La colonne 'product' est absente du DataFrame.")
        return pd.DataFrame()
