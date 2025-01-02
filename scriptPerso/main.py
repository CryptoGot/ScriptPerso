import argparse
from inventory_manager import (
    read_and_merge_csv,
    search_by_category,
    search_by_product
)
from report import generate_report


def main():
    """
    Point d'entrée principal du programme.

    Préconditions :
    - L'utilisateur fournit des arguments valides via la ligne de commande :
      - Fichiers CSV existants pour fusion ou recherche.
      - Une catégorie ou un produit valide pour la recherche.
      - Un chemin valide pour le fichier de rapport.

    Postconditions :
    - Les résultats des recherches ou le rapport
    généré sont affichés ou enregistrés selon les options fournies.

    Exceptions levées :
    - FileNotFoundError : Si les fichiers spécifiés n'existent pas.
    - ValueError : Si les fichiers spécifiés ne contiennent
    pas les colonnes nécessaires.
    - KeyError : Si une colonne requise manque dans les données.
    """
    try:
        # Définir les arguments du programme
        parser = argparse.ArgumentParser(description="Gestion de l'inventaire")
        parser.add_argument(
            "csv_files", nargs="+", help="Liste des fichiers CSV à consolider"
        )
        parser.add_argument(
            "-o", "--output", help="Nom du fichier pour le rapport généré",
            default="rapport.csv"
        )
        parser.add_argument(
            "--search-product",
            help="Recherche les informations d'un produit spécifique"
        )
        parser.add_argument(
            "--search-category",
            help="Recherche les informations d'une catégorie spécifique"
        )
        args = parser.parse_args()

        # Lecture et fusion des fichiers CSV
        data = read_and_merge_csv(args.csv_files)
        if data.empty:
            print(
                "Aucune donnée valide n'a été trouvée dans les fichiers CSV.")
            return

        # Recherche par produit
        if args.search_product:
            product_data = search_by_product(data, args.search_product)
            if product_data.empty:
                print(f"Produit '{args.search_product}' introuvable.")
            else:
                print(f"Résultats pour le produit '{args.search_product}':")
                print(product_data)
            return  # Fin du programme après la recherche

        # Recherche par catégorie
        if args.search_category:
            category_data = search_by_category(data, args.search_category)
            if category_data.empty:
                print(f"Catégorie '{args.search_category}' introuvable.")
            else:
                print(f"Résultats pour la catégorie '{args.search_category}':")
                print(category_data)
            return  # Fin du programme après la recherche

        # Si aucune recherche, générer le rapport
        print("Aperçu des données fusionnées :")
        print(data.head())  # Affiche un aperçu des données fusionnées
        generate_report(data, args.output)

    except FileNotFoundError as fnfe:
        print(f"Erreur : Fichier introuvable. Détails : {fnfe}")
    except ValueError as ve:
        print(f"Erreur de validation des fichiers : {ve}")
    except KeyError as ke:
        print(f"Erreur : Données manquantes ou mal formatées. Détails : {ke}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")


if __name__ == "__main__":
    main()
