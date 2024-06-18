---
title: Les Librairies systèmes
weight: "1"
---

![](librairies.png?width=25vw)


# Qu'est-ce qu'une Librairie système ?

En Python, les librairies système fournissent des interfaces pour interagir avec le système d'exploitation et les ressources matérielles sous-jacentes.


Une librairie système est un ensemble de modules et de fonctions fournies par le système d'exploitation ou par des bibliothèques externes qui permettent aux programmes :

- De communiquer avec le système d'exploitation
- D'accéder aux ressources matérielles
- De gérer des processus
- De manipuler des fichiers
- D'effectuer d'autres opérations système de bas niveau.


# Exemples


```python
import os  # importation de la librairie os

print(os.listdir('.'))  # Liste les fichiers dans le répertoire courant
os.mkdir("foo")         # Crée le répertoire foo
```



# Ateliers

[Atelier sur les objets](atelier_objets.ipynb)
