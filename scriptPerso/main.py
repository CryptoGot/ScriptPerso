import argparse
from inventory_manager import read_and_merge_csv, search_by_category
from report import generate_report


def main():
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
    if data is None:
        print("Impossible de lire ou de fusionner les fichiers CSV.")
        return

    # Recherche par produit
    if args.search_product:
        product_data = data[data['product'] == args.search_product]
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
    print(data.head())  # Affiche un aperçu des données fusionnées
    generate_report(data, args.output)


if __name__ == "__main__":
    main()
