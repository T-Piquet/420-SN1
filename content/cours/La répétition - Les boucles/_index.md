---
title: La répétition - Les boucles
weight: "2"
---

# Cours
## La répétition en informatique
Un des avantages de l'informatique est qu'on est capable de traiter énormément d'information en très peu de temps. Et ce traitement est souvent le même, mais avec des données différentes.

Par exemple, on a un relevé quotidien de température d'une station météo et on souhaite calculer la température moyenne de chaque semaine de l'année. Dans ce cas, il faut répéter 52 fois une moyenne de 7 températures. 

Un autre exemple, si on a un modèle météorologique et que l'on souhaite tester la relation entre le niveau de CO2 dans l'atmosphère et l'augmentation de la température terrestre. Dans ce cas, il faudra exécuter un grand nombre de simulations en faisant varier le niveau CO2 dans l'atmosphère pour obtenir la température correspondante. On répètera la simulation le nombre fois nécessaire pour couvrir l'amplitude choisie.

Imaginez qu'on souhaite demander à l'utilisateur de saisir le prix unitaire d'un produit, mais que ce prix ne doit pas être négatif. Donc **tant que** le prix unitaire fourni est négatif, il faut redemander une nouvelle valeur à l'utilisateur.
 
```python
prix_unitaire = int(input("Entrez le prix unitaire: "))
if prix_unitaire < 0:
	print("Un prix ne peut être négatif")
	
	prix_unitaire = int(input("Entrez le prix unitaire: "))
	if prix_unitaire < 0:
		print("Un prix ne peut être négatif")

		prix_unitaire = int(input("Entrez le prix unitaire: "))
		if prix_unitaire < 0:
			print("Un prix ne peut être négatif")
			#...
```

On voit que sans structure de répétition, on peut continuer cette imbrication de `if` à l'infini.

## Boucle while

{{%notice style="tip"%}}
La boucle `while` est pratique pour faire des boucles où on ne sait pas combien de fois on va devoir répéter des instructions. Typiquement avec des saisies utilisateurs. **Il faut une condition de sortie**.
{{% /notice%}}

```python
prix_unitaire = int(input("Entrez le prix unitaire: "))
while prix_unitaire < 0:
	print("Un prix ne peut être négatif")
	prix_unitaire = int(input("Entrez le prix unitaire: "))
```

TODO: ajouter ordinogramme

La boucle `while` répète les instructions **tant que** une certaine condition est remplie. La condition de bouclage prend exactement la même forme que les conditions avec l'instruction `if`. Vous pouvez donc créer des conditions complexes pour sortir de la boucle.

Par exemple, on peut modifier la condition pour autoriser seulement les prix unitaires entre 0 et 1000.

```python
prix_unitaire = int(input("Entrez le prix unitaire: "))
while prix_unitaire < 0 or prix_unitaire > 1000:
	print("Un prix ne peut être négatif, ou supéieur a 1000")
	prix_unitaire = int(input("Entrez le prix unitaire: "))
```

La forme générique de l'instruction `while` est :

```python
while <condition>:
	instruction1
	instruction2
	instruction3
	...
```

### Boucle infinie
```python
while true:
	instruction1
	instruction2
	instruction3
	...
```

Pour sortir d'une boucle infinie, il faut utiliser le clavier et taper les touches `ctrl+c`

## Boucle for

{{%notice style="tip"%}}
La boucle `for` est pratique pour faire des boucles où on sait à l'avance combien de fois on va devoir répéter des instructions. Typiquement pour le traitement de données, on connait à l'avance le nombre de données que l'on va analyser. **Il faut une liste d'éléments**.
{{% /notice%}}

La forme générale de la boucle `for` est :

```python
for variable in range(n):
	instruction1
	instruction2
	instruction3
	...
```

La boucle `for` est basée sur une variable d'itération. Cette variable peut être utilisée dans les instructions de la boucle. Et cette variable prend les valeurs générées par l'instruction `range()`
### L'instruction range

> Que fait le code suivant ?

```python
for i in range(10):
	if i % 2 == 0:
		print(i)
```

`range` est une instruction qui permet de générer une suite de nombre avec lesquels nous allons faire nos répétitions.

La forme générale de la fonction est : `range(début, fin, pas)`

Si 1 seul paramètre est spécifié, il s'agit du paramètre `fin`. Dans ce cas `début = 0` et `pas = 1`.

```
range(10)
=> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Si 2 paramètres sont spécifiés, il s'agit des paramètres `début` et `fin`. Dans ce cas `pas = 1`.

```
range(4, 10)
=> [4, 5, 6, 7, 8, 9]
```

Avec les 3 paramètres spécifiés, on peut obtenir ce genre de résultat :

```
range(2, 100, 10)
=> [2, 12, 22, 32, 42, 52, 62, 72, 82, 92]
```

> Que fait le code suivant ?

```python
for i in range(0, 10, 2):
	print(i)
```

### L'instruction break

Lorsque l'on parcourt un grand ensemble de données avec une boucle `for`, on peut vouloir arrêter les calculs si jamais une valeur ne fait pas de sens. 

Par exemple, une donnée négative dans un relevé démographique. Dans ce cas, l'instruction `break` va interrompre la boucle.

```python
for i in range(taille_des_donnees):
	if data[i] < 0:
		print("Erreur: population négative")
		break
	instruction1
	instruction2
	instruction3
	...
```

Dans cet exemple, si la population est négative, on alerte l'usagé et on sort de la boucle pour ne par exécuter les instructions suivantes.

## Imbrication de boucles

Une instruction de bouclage reste une instruction comme les autres, on peut les enchainer les unes dans les autres.

> Que fait le code suivant ?

```python
cote = 3
for i in range(cote):
	for j in range(cote):
		print("#", end="")
	print("")
```

{{%notice style="warning"%}}
 En règle générale, il est rare d'avoir plus de 3 boucles les unes dans les autres. Si vous devez en imbriquer plus que 3 pour résoudre un algorithme, il y a probablement un problème de logique dans la conception de votre solution.
{{% /notice%}}

# Remarque du jour

{{%notice style="tip"%}}
 90% de temps d'exécution d'un programme se passe dans 10% du code
{{% /notice%}}

Il y a seulement quelques boucles responsables de la majeure partie du temps de calcul d'un programme. C'est en optimisant ces boucles que vous gagnerez en performance.

# Lab

[**Atelier sur les boucles**](Boucles.ipynb)

