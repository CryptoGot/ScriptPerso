# Gestion d'Inventaire

Ce programme permet de gérer facilement des fichiers CSV contenant des informations sur des stocks. Il offre plusieurs fonctionnalités pour fusionner les fichiers, rechercher des informations, et générer un rapport récapitulatif.

## Fonctionnalités

### Fusion des fichiers CSV :

- Combine plusieurs fichiers CSV en une seule base de données.
- Par exemple, fusionner des fichiers de différents départements ou catégories.

### Recherche rapide :

- Recherche par produit avec l'option ```--search-product.```
- Recherche par catégorie avec l'option ```--search-category.```

### Génération de rapport :

- Regroupe les données par catégorie.
- Calcule la somme des quantités et la moyenne des prix pour chaque catégorie.  
- Sauvegarde le rapport dans un fichier CSV.  

## Installation

1. Prérequis :

- Python 3.x installé.
- La librairie pandas (si non installée, utilisez la commande suivante) :
```pip install pandas```

2. Cloner le dépôt GitHub :

- Téléchargez ou clonez ce projet depuis GitHub :
```git clone <URL_DU_DEPOT>```
```cd scriptPerso```

## Utilisation
### Commandes principales
1. Fusionner des fichiers CSV et générer un rapport :
```python main.py <fichier1.csv> <fichier2.csv> ... -o <rapport.csv>```
- Exemple :
```python main.py produits1.csv produits2.csv -o rapport.csv```
2. Rechercher par produit :
```python main.py <fichier1.csv> <fichier2.csv> --search-product <NomDuProduit>```
- Exemple :
```python main.py produits1.csv produits2.csv --search-product Chaise```
3. Rechercher par catégorie :
```python main.py <fichier1.csv> <fichier2.csv> --search-category <NomDeLaCategorie>```
- Exemple :
```python main.py produits1.csv produits2.csv --search-category Meubles```
## Exemple d'utilisation
### Fichiers CSV initiaux
- produits1.csv :
```text 
product,category,quantity,price
Chaise,Meubles,10,50
Table,Meubles,5,150
```
- produits2.csv :
```text 
product,category,quantity,price
Lampe,Luminaires,15,30
Canapé,Meubles,2,500
```
### Résultat après fusion et génération de rapport
- Commande :
```python main.py produits1.csv produits2.csv -o rapport.csv```
- Terminal :
```text 
  product    category  quantity  price
0  Chaise     Meubles        10     50
1   Table     Meubles         5    150
2   Lampe  Luminaires        15     30
3  Canapé     Meubles         2    500
Rapport généré dans : rapport.csv
```
- Contenu de rapport.csv :
```text 
category,quantity,price
Luminaires,15,30.0
Meubles,17,233.33
```

## Organisation du projet
- main.py : Point d'entrée du programme
- inventory.py : Contient les fonctions pour fusionner les fichiers CSV et rechercher des informations.
- report.py : Contient la fonction pour générer des rapports.
- tests/ : Dossier contenant les tests unitaires pour valider le programme.

## Tests unitaires
Les tests unitaires sont disponibles dans le dossier tests. Pour les exécuter, utilisez la commande suivante :  
python -m unittest discover tests

