import pandas as pd


def read_and_merge_csv(files):
    """
    Lit et fusionne plusieurs fichiers CSV en un seul DataFrame.

    Préconditions :
    - `files` est une liste de chemins vers des fichiers CSV.
    - Chaque fichier doit contenir les colonnes : 'product', 'category', 'quantity', 'price'.

    Postconditions :
    - Retourne un tableau avec toutes les données fusionnées.
    - Si aucun fichier valide n'est fourni, retourne un tableau vide.

    Exceptions levées :
    - FileNotFoundError : Si un fichier n'est pas trouvé.
    - pd.errors.EmptyDataError : Si un fichier est vide.
    - ValueError : Si un fichier ne contient pas les colonnes obligatoires.
    - Exception : En cas d'erreur inattendue.
    """
    required_columns = {'product', 'category', 'quantity', 'price'}
    dataframes = []

    for file in files:
        try:
            # Lecture du fichier CSV
            df = pd.read_csv(file)
            # Vérification des colonnes obligatoires
            if not required_columns.issubset(df.columns):
                raise ValueError(
                    f"Colonnes manquantes dans le fichier : {file}")
            dataframes.append(df)
        except FileNotFoundError:
            print(f"Erreur : Le fichier {file} est introuvable.")
        except pd.errors.EmptyDataError:
            print(f"Erreur : Le fichier {file} est vide.")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(
                f"Erreur inattendue lors de la lecture du fichier {file} : {e}"
                )

    if not dataframes:
        print("Erreur : Aucun fichier CSV valide trouvé.")
        return pd.DataFrame()  # Retourne un DataFrame vide

    # Fusionner les DataFrames
    try:
        merged_df = pd.concat(dataframes, ignore_index=True)
        return merged_df
    except Exception as e:
        print(f"Erreur lors de la fusion des fichiers : {e}")
        return pd.DataFrame()  # Retourne un DataFrame vide


def search_by_category(dataframe, category):
    """
    Recherche toutes les lignes correspondant à une catégorie spécifique.

    Préconditions :
    - `dataframe` doit avoir une colonne 'category'.
    - `category` est une chaîne de texte.

    Postconditions :
    - Retourne les lignes correspondant à la catégorie.
    - Retourne un tableau vide si la catégorie n'existe pas.

    Exceptions levées :
    - KeyError : Si la colonne 'category' est absente du DataFrame.
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

    Préconditions :
    - `dataframe` doit avoir une colonne 'product'.
    - `product` est une chaîne de texte.

    Postconditions :
    - Retourne les lignes correspondant au produit.
    - Retourne un tableau vide si le produit n'existe pas.

    Exceptions levées :
    - KeyError : Si la colonne 'product' est absente du DataFrame.
    """
    try:
        filtered_df = dataframe[dataframe['product'] == product]
        if filtered_df.empty:
            print(f"Aucune donnée trouvée pour le produit : {product}")
        return filtered_df
    except KeyError:
        print("Erreur : La colonne 'product' est absente du DataFrame.")
        return pd.DataFrame()
