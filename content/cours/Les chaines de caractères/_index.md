---
title: Les Chaines de caractères
weight: "1"
---

![](strings.png?width=25vw)


# Qu'est-ce qu'une chaine de caractères ?

Une chaine de caractères est simplement plusieurs caractères regroupés ensemble.
Les caractères peuvent être des lettres, chiffres, symboles ou espaces.
Les chaines de caractères sont des objets que nous pouvons manipuler.
Nous pouvons concaténer des chaines, extraire ou chercher des sous-chaines, les modifier, etc...

En python, les chaines de caractères sont entourées de guillemets simples (`'`) ou doubles (`"`):

```python
uneChaine = 'Bonjour'
uneAutre = "Allo"
```

Les chaînes en Python sont **immuables**, ce qui signifie qu'une fois créées, elles ne peuvent pas être modifiées. Toute opération qui semble modifier une chaîne crée en réalité une nouvelle chaîne. Pour l'utilisateur (programmeur), l'immutabilité est transparente dans la plupart des cas.



# Comment utiliser une chaine de caractères ?

## Fonctions, Opérations et Méthodes

| Fonctions |  |
| ---- | ----|
| len() | Retourne la longueur de la chaine |
| str() | Convertit en chaine de caractères |


| Opérations |  |
| ---- | ----|
| * | Multiplie une chaine |
| + | Concatène des chaines |


| Méthodes |  |
| ---- | ----|
| [] | Accède à un caractère selon sa position |
| lower() | Convertit tous les caractères de la chaîne en minuscules |
| upper() | Convertit tous les caractères de la chaîne en majuscules. |
| strip() | Supprime les espaces (ou autres caractères spécifiés) au début et à la fin de la chaîne |
| replace() | Remplace toutes les occurrences de la sous-chaîne |
| split() | Divise la chaîne en une liste de sous-chaînes |
| join() | Concatène une séquence d'éléments (comme une liste) en une seule chaîne |
| find() | Renvoie l'indice de la première occurrence de la sous-chaine |



## Les indices


![](chaine_01.png)


### Exemples


[Exemples sur les chaines de caractères](exemples_caracteres.ipynb)




### Charactères "spéciaux"


| Caractère |  |
| --- | --- |
| `\t` | Tabulation |
| `\n` | Retour de ligne |
| `\\` | Barre oblique inversée (Backslash) |

Le `\` permet d'échapper le caractère suivant.


## Insertion de variables

Il est possible d'insérer facilement des variables dans des chaines de caractères.
Une première solution est d'utiliser la concaténation:

```python
var1 = 23
var2 = 35
laChaine = "Le nombre " + str(var1) + " est plus petit que " + str(var2)
print(laChaine)   # Affiche:  Le nombre 23 est plus petit que 35
```

Mais il est préférable d'utiliser le f-strings :

```python
var1 = 23
var2 = 35
laChaine = f'Le nombre {var1} est plus petit que {var2}'
print(laChaine)   # Affiche:  Le nombre 23 est plus petit que 35
```


## Dans une boucle

Il est possible d'itérer sur chaque lettre de la chaine:

```python
for lettre in "Bonjour":
    print(lettre)
```


# Ateliers

[Atelier sur les chaines de caractères](atelier_caracteres.ipynb)
