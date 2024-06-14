---
title: Les Chaines de caractères
weight: "1"
---

![](An_abstract_image_representing_strings_in_Python.png)


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



### Exemples

#### Création

```python
maChaine = "Bonjour"
```

#### Longueur

```python
longueur = len(maChaine)
print(maChaine)   # Affiche: 7
```

#### Conversion en chaine de caractères

```python
laChaine = str(123)   #   laChaine sera une "string" et non plus un nombre
```



#### Concaténation

```python
maChaine = maChaine + " le monde"
print(maChaine)   # Affiche: "Bonjour le monde"
```

#### Multiplication

```python
uneChaineRepetee = "Allo" * 3
print(uneChaineRepetee)   # Affiche: "AlloAlloAllo"
```

#### []

```python
print(maChaine[0])   # Affiche: "B"

c = maChaine[0] + maChaine[2]
print(c)   # Affiche: "Bn"     soit la 1ere et 3e lettre de "Bonjour"

print(maChaine[1:5])   # Affiche: "onjo"   
```

#### lower()

```python
c = maChaine.lower()
print(c)   # Affiche:   "bonjour le monde"
print(maChaine)   # Affiche:   "Bonjour le monde"
```

#### upper()

```python
c = maChaine.upper()
print(c)   # Affiche:   "BONJOUR LE MONDE"
print(maChaine)   # Affiche:   "Bonjour le monde"
```

#### strip()

```python
c = "  allo\t"
print(len(c))   # Affiche:  7
c = c.strip()
print(len(c))   # Affiche:  4
```

#### replace()

```python
uneChaine = "abababababa"
uneChaine = uneChaine.replace('a', 'b')
print(uneChaine)   # Affiche:  "bbbbbbbbbbb"

uneChaine = uneChaine.replace('bbb', 'c')
print(uneChaine)   # Affiche:  "cccbb"
```

#### find()

```python
uneChaine = "Bonjour tout le monde"
indice = uneChaine.find("o")
print(indice)   # Affiche:  1

indice = uneChaine.find("z")
print(indice)   # Affiche:  -1

indice = "Une autre phrase".find("p")
print(indice)   # Affiche:  10
```

Pour trouver toutes les indices d'une lettre:
```python
uneChaine = "Bonjour tout le monde"
lettreRecherchee = "o"

indice = uneChaine.find(lettreRecherchee)

while indice != 0:
    print(indice, "=>", uneChaine[indice])
    indice = uneChaine.find(lettreRecherchee, indice + 1) # le 2e argument permet d'indiquer où la recherche doit commencer (0 par défaut)

# Affichera :
# 1 => o
# 4 => o
# 9 => o
# 17 => o
```


#### split()

```python
uneChaine = "un-deux-trois-quatre"
nombres = uneChaine.split("-")
print(nombres)   # Affiche:  ['un', 'deux', 'trois', 'quatre']

nombres = uneChaine.split("-t")
print(nombres)   # Affiche:  ['un-deux', 'rois-quatre']
```

#### join()

```python
listeMots = ['un', 'deux', 'trois', 'quatre']
uneChaine = "-".join(listeMots)
print(uneChaine)   # Affiche:  "un-deux-trois-quatre"

uneChaine = " ==> ".join(listeMots)
print(uneChaine)   # Affiche:  "un ==> deux ==> trois ==> quatre"
```




### Charactères "spéciaux"


| Caractère |  |
| --- | --- |
| `\t` | Tabulation |
| `\n` | Retour de ligne |
| `\\` | Barre oblique inversée (Backslash) |

Le `\` permet d'échapper le caractère suivant.


Exemple:

```python
uneChaine = "la\tchaine de\ncaractères"
print(uneChaine)

# Affiche:
# la	chaine de
# caractères
```


## f-strings

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
rang = 1
for lettre in "Bonjour":
    print(f'La lettre numéro {rang} est : {lettre}')
    rang += 1

# Affichera
# La lettre numéro 1 est : B
# La lettre numéro 2 est : o
# La lettre numéro 3 est : n
# La lettre numéro 4 est : j
# La lettre numéro 5 est : o
# La lettre numéro 6 est : u
# La lettre numéro 7 est : r
```


# Ateliers

[Atelier sur les chaines de caractères](atelier_caracteres.ipynb){:download}


# Traces d'exécution
