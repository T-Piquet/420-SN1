# Setup Hugo - Relearn

Il est préférable d'installer la dernier version de [HUGO](https://gohugo.io/commands/hugo_server/) pour fonctionner avec [Relearn](https://mcshelby.github.io/hugo-theme-relearn/basics/installation/index.html).

Operationel sur la version 0.122 de HUGO.

# Script de conversion

Le script `obs2relearn.py` converti les .md de obsidian en .md compatible avec le thème [Relearn](https://github.com/McShelby/hugo-theme-relearn.git) de HUGO.

Fonctionnalitées compatible:
- Boites de callout (tip et warning fonctionel, il faut tester les autres type de callout)
- insertions des images avec parametre de taille (`![[image.png | 300]]`)
    - positionnement pas pris en compte (droite, gauche, centre)
    - nécessite la copie manuelle des images dans le repertoire de la page, si un repertoire `images` n'existe pas dans la structure obsidian
- Multiple liens par ligne.
- Poids des pages avec l'argument `weight` dans le frontmatter Obsidian.

# Commande
`python3 ./obs2relearn.py <path to obsidian md> <path to relearn content> <lesson name>`

# Structure obsidian
```
introduction reseau/
| images/
| | adresseIPv6.png
| | ...
| couche application.md
| couche transport.md
| ...
```

## Structure des fichier .md
### En-tête
```
---
export: true / false
cours: ze5 / 4c6 / ...
path: cours / base de connaissances
weigth: 2
---
```

Le paramètre `weight` est utilisé pour ordonner les pages entre elles dans Relearn. Les autres paramètres servent au script pour creer les nouvelles pages.

### Corps du fichier
- Pour séparer les paragraphes dans relearn, il faut une ligne vide entre chaque paragraphe dans obsidian.
- Généralement, il faut laisser une ligne vide après l'insertion d'une image. Même en fin de fichier.