---
title: Les Structures de Données
weight: "1"
---

![](strucutres.png?width=25vw)

# Qu'est-ce qu'une Structure de Donnée en Python ?

Une structure de donnée avancée en Python fait référence à des collections ou des types de données qui permettent de stocker, organiser et manipuler des données de manière efficace.

Nous avons déjà vu d'autres structures de données, soit les [listes](../les-listes) et les [chaines de caractères](../les-chaines-de-caractères).

Maintenant, nous regarderons d'autres structures de données, soit les dictionnaires, les ensembles et les tuples:

# Les dictionnaires

Les dictionnaires en Python sont des collections de paires **clé-valeur**. Chaque élément dans un dictionnaire a une clé unique et une valeur associée. Les dictionnaires sont très utiles pour stocker des données associées.

Par exemple, un dictionnaire pourrait être utilisé pour maintenir un inventaire d'espèces d'arbres. Les espèces seront les clés et les quantités seront les valeurs:

| Espèces | Quantité |
| --- | --- |
| Chêne | 30 |
| Pin | 15 |
| Érable | 25 |
| Bouleau | 42 |
| Sapin | 25 |


Donc, si vous avez besoin d'une quantité, vous utiliserez le tableau ci-dessus en cherchant l'espèce qui vous intéresse.

Les dictionnaires fonctionnent très similairement:

```python

# On initialise le dictionnaire avec {} ou dict()
monDictionnaire = {}

# On ajoute des éléments
monDictionnaire["Chêne"] = 30
monDictionnaire["Pin"] = 15
monDictionnaire["Érable"] = 25
monDictionnaire["Bouleau"] = 42
monDictionnaire["Sapin"] = 25

# On accède à une valeur selon la clé
x = monDictionnaire["Pin"]   # x vaut 15

# On modifie une valeur
monDictionnaire["Érable"] = 5   # La valeur de "érable" est remplacée par 5

# On supprime une paire
monDictionnaire.pop("Sapin")    # La paire ayant la clé "Sapin" est effacée

# On vérifie si une clé est présente
uneEspece = "Chêne"
if uneEspece in monDictionnaire:
    print(f'L\'espèce {uneEspece} est présente.')
else:
    print(f'L\'espèce {uneEspece} n\'est pas présente.')
```

{{%notice style="note" title="Notez"%}}
- Les clés doivent être de type immuable, c'est-à-dire qu'elle ne peuvent pas être modifiées.
- Dans la majorité de cas, les clés sont des **chaines de caractères** ou des **nombres**.
- Les clés doivent être unique.
{{% /notice%}}


Il est aussi possible de parcourir les dictionnaires, c'est-à-dire d'itérer sur chacune des paires clé-valeur:

```python
# Initialisation avec les données
monDictionnaire = {'Chêne': 30,'Pin': 15,'Érable': 25,'Bouleau': 42,'Sapin': 25}

# Itération sur les clés
for espece in monDictionnaire.keys():
    print(espece)                       # Les clés seront affichées une après l'autre
    print(monDictionnaire[espece])      # La variable "espece" permet d'accéder à la quantité

# Itération sur les valeurs
for quantite in monDictionnaire.values():
    print(quantite)                       # Les quantités seront affichées une après l'autre

# Itération sur les paires clé-valeur
for espece, valeur in monDictionnaire.items():
    print(espece, valeur)                       # Les valeurs et quantités seront affichées une après l'autre
```


Comme pour les listes, les valeurs d'un dictionnaire peuvent être complexes.
Il est possible d'utiliser des dictionnaires ou des listes comme valeurs:

```python
# un inventaire vide
inventaire = {}

# Ajout d'une paire ayant comme clé : "site_1", et un dictionnaire comme valeur
inventaire['site_1'] = {}
# Ajout d'espèce et quantité dans le dictionnaire du site_1
inventaire['site_1']['Chêne'] = 30
inventaire['site_1']['Sapin'] = 15
inventaire['site_1']['Érable'] = 25

# Ajout d'un dictionnaire (avec information) à la clé "site_2"
inventaire['site_2'] = {'Chêne': 7,'Érable': 25,'Bouleau': 42}

# Il est possible d'ajouter d'autres dictionnaires à l'intérieur
inventaire['site_1']['Pin'] = {}
inventaire['site_1']['Pin']['Quantité'] = 125
inventaire['site_1']['Pin']['Rangée'] = "A"
inventaire['site_1']['Pin']['Grandeur'] = [3, 8, 12]


# Affichage à l'aide de pprint
from pprint import pprint

pprint(inventaire)
```
Affiche:

```python
{'site_1': {'Chêne': 30,
            'Sapin': 15,
            'Érable': 25,
            'Pin': {
                'Grandeur': [3, 8, 12],
                'Quantité': 125,
                'Rangée': 'A'
                },
 'site_2': {'Bouleau': 42,
            'Chêne': 7,
            'Érable': 25
            }
}
```

{{%notice style="note" title="Notez"%}}
- Les dictionnaires ne sont pas ordonnés.
- Par exemple, l'affichage n'est pas dans le même ordre que l'ordre d'entrée.
{{% /notice%}}


# Les Ensembles (Set)

Les ensembles (ou sets) en Python sont des collections **non ordonnées** d'éléments **uniques**. Ils sont utilisés pour stocker des éléments distincts et effectuer des opérations mathématiques comme l'union, l'intersection et la différence.

```python
# Initialisation d'un ensemble vide
monEnsemble = set()

# Ajout d'éléments
monEnsemble.add(1)      # contient 1
monEnsemble.add(2)      # contient 1 et 2
monEnsemble.add(3)      # contient 1, 2 et 3
monEnsemble.add(2)      # contient 1, 2 et 3

# Initialisation d'un ensemble à partir d'une liste
maListe = [1, 2, 3, 4, 3, 2, 1]   # liste avec des doublons
ensemble = set(maListe)           # l'ensemble ne contient que [1, 2, 3, 4]

# Suppresion d'une valeur
ensemble.remove(1)              # Supprime la valeur 1

# Vérifier si l'élément est présent
if 2 in ensemble:
    print(f'Le chiffre 2 est dans l\'ensemble')

# Itération sur les valeurs
for v in ensemble:
    print(v)            # Affiche chaque valeur de l'ensemble
```

Les ensembles supportent plusieurs opérations mathématiques :

```python
ensemble1 = {1, 2, 3}
ensemble2 = {3, 4, 5}

# Union
union = ensemble1 | ensemble2
print(union)            # {1, 2, 3, 4, 5}


# Intersection
intersection = ensemble1 & ensemble2
print(intersection)    # {3}

# Différence
difference = ensemble1 - ensemble2
print(difference)  # {1, 2}

# Différence symétrique
difference_sym = ensemble1 ^ ensemble2
print(difference_sym)  # {1, 2, 4, 5}
```


# Les Tuples

Les tuples en Python sont des séquences ordonnées et **immuables** de valeurs. Contrairement aux listes, les tuples ne peuvent pas être modifiés après leur création.

Les tuples


Pourquoi utiliser des tuples au-lieu des listes?

Contrairement aux listes, les tuples sont immuables. Dans biens des cas, cette immuabilité restreint leur utilisation et les listes sont préférées.

Par contre, les tuples peuvent être utilisés comme clé dans les dictionnaires.

Exemple: Vous placez des objets sur un plan cartésien. Vous pourriez utiliser un tuple comme clé `(x, y)` et la description de l'objet comme valeur.

```python
# une carte vide
carte = {}

# ajout d'objets
carte[(3, 5)] = "Monstre"    # un Monstre à la position (3, 5)
carte[(2, 8)] = "Trésor"     # un Trésor à la position (2, 8)
carte[(1, 3)] = "Trou"       # un Trou à la position (1, 3)
carte[(3, 4)] = "Joueur"     # un Joueur à la position (3, 4)
```

# Ateliers

[Atelier sur les Structures de données](atelier_structuresDonnees.ipynb)
