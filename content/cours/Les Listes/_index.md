---
title: Les Listes
weight: "1"
---

![](An_abstract_illustration_representing_Python_lists_converted.png)

# Pourquoi utiliser des listes ?


## Mise en situation

Vous devez gérer les données des étudiants du cours.
Chaque étudiant a un nom et un âge.
Vous ne savez pas combien d'étudiants seront inscrits dans le cours.
Vous devez afficher le nom de tous les étudiants et leur âge.


### Solution sans liste

```
# On saisit chaque variable
etudiant_01_nom = "Emma"
etudiant_01_age = 18
etudiant_02_nom = "Julien"
# ....
etudiant_37_age = "20"


# On affiche les noms et âge un par un
print(etudiant_01_nom, etudiant_01_age)
# ....
print(etudiant_37_nom, etudiant_37_age)
```


### Solution avec une liste

L'utilisation des listes permettra d'exécuter cette tâche beaucoup plus facilement.
Vous pourrez ajouter/modifier/enlever des étudiants.
Et vous pourrez ajouter plusieurs informations pour chaque étudiant.  

```
# On remplit la liste
etudiants = []
etudiants.append(["Emma", 18])
etudiants.append(["Julien", 17])
....
etudiants.append(["Sophie", 20])

# On affiche les noms et âge dans une boucle
for e in etudiants:
    print(e[0], e[1])
```


# Qu'est-ce qu'une liste ?

En Python, une liste est une collection ordonnée et modifiable d'éléments. Les listes sont utilisées pour stocker plusieurs éléments dans une seule variable et peuvent contenir des éléments de différents types, y compris des nombres, des chaînes de caractères, d'autres listes, etc. Les listes en Python sont définies en utilisant des crochets [].

## Caractéristiques d'une liste

- **Ordonnée** : Les éléments de la liste conservent un ordre défini, ce qui signifie que l'ordre dans lequel vous ajoutez les éléments est préservé.
- **Modifiable** : Une liste peut être modifiée après sa création, ce qui signifie que vous pouvez ajouter, supprimer ou changer des éléments.
- **Taille Dynamique** : Une liste en Python peut changer de taille dynamiquement. Vous pouvez ajouter ou supprimer des éléments sans avoir à spécifier la taille initiale de la liste.
- **Hétérogène** : En *Python*, une liste peut contenir des éléments de différents types (entiers, chaînes de caractères, listes, etc.).


# Comment utiliser une liste ?

## Fonctions

| Fonction |  |
| ---- | ----|
| len() | Retourne la longueur de la liste |
| append() | Ajoute un élément à la fin de la liste |
| insert() | Ajoute un élément à un endroit spécifique dans la liste |
| remove() | Supprime un élément de la valeur spécifiée |
| pop() | Supprime un élément selon sa position et retourne la valeur |
| del() | Supprime un élément selon sa position |
| [] | Permet d'accéder à un élément de la liste selon sa position |
| extend() | Ajoute tous les éléments d'une liste dans une autre liste |
| clear() | Efface tous les éléments d'une liste |
| index() | Retourne l'indice du premier élément dont la valeur est égale à celle spécifiée |
| sort() | Trie les éléments de la liste |
| reverse() | Inverse l'ordre des éléments de la liste |
| copy() | Retourne une copie superficielle de la liste |
| max() | Retourne la valeur maximum de la liste |
| min() | Retourne la valeur minimum de la liste |



## Opérations simples

### Création d'une liste

```
# Création d'une liste vide
ma_liste = []

# Liste avec des éléments
ma_liste = [1, 2, 3, 4, 5]
```

### Accès aux Éléments d'une Liste

```
# Accès au premier élément
print(ma_liste[0])  # Affiche 1

# Accès au dernier élément
print(ma_liste[-1])  # Affiche 5
```

Notez que les indices commencent à zéro.

### Ajout d'Éléments

```
# Ajouter un élément à la fin de la liste
ma_liste.append(6)
print(ma_liste)  # Affiche [1, 20, 3, 4, 5, 6]

# Insérer un élément à une position spécifique
ma_liste.insert(1, 15)
print(ma_liste)  # Affiche [1, 15, 20, 3, 4, 5, 6]
```


### Suppression d'Éléments

```
# Supprimer un élément spécifique
ma_liste.remove(20)
print(ma_liste)  # Affiche [1, 15, 3, 4, 5, 6]

# Supprimer le dernier élément
ma_liste.pop()
print(ma_liste)  # Affiche [1, 15, 3, 4, 5]

# Supprimer le deuxième élément
ma_liste.pop(1)
print(ma_liste)  # Affiche [1, 3, 4, 5]
```


### Modification des Éléments

```
# Modification du deuxième élément
ma_liste[1] = 20
print(ma_liste)  # Affiche [1, 20, 4, 5]
```


## Dans une boucle


Il est possible de parcourir chacun des éléments de la liste avec une boucle FOR:

```
# Affichage de chacun des éléments de la liste
for element in ma_liste:
    print(element)
```

Il est aussi possible d'utiliser la fonction `range()` afin de parcourir la liste à l'aide des indices:

```
# On additionne 1 à chaque élément de la liste
for i in range(len(ma_liste)):
    ma_liste[i] = ma_liste[i] + 1
```


Il est aussi possible de parcourir une liste dans une boucle WHILE:

```
# On affiche les premiers éléments de la liste.
# On arrête dès que le total atteint au moins 10

ma_liste = [1, 2, 3, 4, 5, 6, 7]
total = 0
i = 0
while total < 10:
    print(ma_liste[i])
    i += 1
```



## Les listes dans les listes

Il est possible de mettre n'importe quel type d'élément dans les listes.
Il est donc possible de mettre des listes dans des listes.
Nous parlons alors de listes (ou tableaux) en 2 dimensions.


```
# Liste contenant 3 éléments
# Chaque élément est une liste contenant 2 nombres
matrice = [[1, 2], [3, 4], [5, 6]]
```

Pour parcourir toutes les listes, il suffit de mettre une boucle dans une boucle :

```
# On parcourt chaque éléments de la liste principale
for sousliste in matrice:
    # et ensuite chaque élément de la "sous-liste"
    for e in sousListe:
        print(e)
```


Les opérations vues sur les listes en 1 dimension fonctionnent aussi pour les listes en 2D:

```
print(matrice[0]) # affiche la première liste de la matrice
print(matrice[0][1]) # affiche le 2e élément de la première liste de la matrice

matrice.append([7, 8]) # ajoute une nouvelle liste à la matrice
```

Il est aussi possible de parcourir les listes en utilisant les indices et la fonction `range()`:

```
# On ajoute 1 à chaque élément de la matrice
for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        matrice[i][j] += 1
```


# Quand utiliser une liste ?

-


# Ateliers

[Atelier sur les listes](atelier_listes.ipynb){:download}



# Traces d'exécution

```
maListe = []
```

![](imagesListes/trace_01.png)


```
maListe.append(6)
```

![](imagesListes/trace_02.png)

```
maListe.append(3)
```

![](imagesListes/trace_03.png)

```
maListe.append(8)
maListe.append(9)
maListe.append(7)
maListe.append(3)
maListe.append(1)
maListe.append(2)
```

![](imagesListes/trace_04.png)


```
maListe[2] = 0
maListe[4] = maListe[7]
```

![](imagesListes/trace_05.png)


```
maListe[0] = maListe[maListe[7]]
```

![](imagesListes/trace_06.png)


```
maListe[4] = maListe[maListe[7] + maListe[6]]
```

![](imagesListes/trace_07.png)


```
maListe.pop()
```

![](imagesListes/trace_08.png)


```
maListe.pop(2)
```

![](imagesListes/trace_09.png)


```
maListe.insert(3, 7)
```

![](imagesListes/trace_10.png)



```
maListe.remove(3)
```

![](imagesListes/trace_11.png)




```
maListe.sort()
```

![](imagesListes/trace_12.png)

```
maListe.sort(reverse=True)
```

![](imagesListes/trace_13.png)

```
autreListe = [5, 6]
maListe.extend(autreListe)
```

![](imagesListes/trace_14.png)


```
maListe.clear()
```

![](imagesListes/trace_01.png)