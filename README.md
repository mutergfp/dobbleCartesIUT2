Dobble serveur génération des cartes
===

Ce projet est un serveur **Python** utilisant le micro-framework web **Flask**.
Il a été créé dans le cadre de la création d'une version web du jeu de société [Dobble](https://fr.asmodee.com/fr/games/dobble/).
Ce serveur est une API REST permettant de gérer la gestion des cartes du jeu, il est donc possible de : 
* Générer un nouveau plateau de jeu en précisant le nombre de joueurs
* Générer une nouvelle carte centrale en fonction des cartes des joueurs actuels
* Récupérer une image stockée dans la base de données en précisant son id
* Ajouter une image à la base de données


## Les routes disponibles


| Route | Méthode | Paramètre(s) | Retour |
|:-:|:-:|:-:|:-:|:-:|
| /cartes/{nbplayers} | GET | Le nombre de joueurs | Un tableau contenant la carte centrale ainsi qu'un autre tableau contenant les cartes des x joueurs **{ middleCard: [Number], playersCards: [[Number]] }**|
| /carte | POST| Un tableau contenant les cartes des x joueurs **[[Number]]** | Une nouvelle carte centrale **[Number]** |
| /image/{id} | GET | L'id de l'image souhaitée | Image demandée ou code 400 si l'image n'existe pas **Buffer** |
| /image | POST | L'image à ajouter **Buffer** | Code 200 pour réussite, code 400 en cas d'erreur **String(url)**|

## Les algorithmes utilisés

### Génération de la carte du milieu et des x premières cartes

#### Variables

* nbJoueurs = nombre de joueurs
* images[] = tableau contenant tous les noms d'images
* cartes[][] = tableau contenant à cartes[0] un autre tableau de 8*[''] et à cartes [1] un tableau de nbPlayers tableau(x) de 8['']

#### Algorithme

On vérifie en premier que le nombre de joueur est compris entre [2;8], s'il ne l'est pas, on renvoie un code erreur **400** *Invalid number supplied*.

Pour i allant jusqu'à 7, 
&ensp;on sélectionne le nom d'une image qui n'est pas déjà dans la carte principale cartes[0]
&ensp;et on le stocke à cartes[0][i]

Pour i allant jusqu'à nbJoueurs,
&ensp;on séléctionne une des 8 images contenues dans la carte principale cartes[0]
&ensp;et on la stocke comme première image de la carte du joueur i, c'est à dire à cartes[1][i][0]
&ensp;&ensp;Pour j allant de 1 à 7
&ensp;&ensp;&ensp;on sélectionne une image qui n'est NI dans la carte principale cartes[0] NI dans la carte du joueur i cartes[1][i]
&ensp;&ensp;&ensp;et on la stocke comme j-ième image de la carte du joueur i à cartes[1][i][j]

On mélange toutes les cartes, la principale et celles de tous les joueurs
Puis on retourne le tableau cartes[] accompagné d'un code **200**


### Génération de la carte du milieu en fonction des cartes des x joueurs

#### Variables

* nbJoueurs = nombre de joueurs
* cartesJoueurs[][] = Un tableau de nbJoueurs tableau(x) de 8 cases
* images[] = tableau contenant tous les noms d'images
* carteMilieu[] = tableau vide de 8 cases

#### Algorithme

Pour i allant jusqu'à nJoueurs
	On séléctionne une des 8 images contenues dans la carte du joueurs i
	mais qui n'est NI déjà dans carteMilieu[] NI dans les cartes de tous les joueurs autre que le joueur i
	on stocke l'image dans carteMilieu[i]
	
pour i allant de nbJoueurs à 8
	On séléctionne une image aléatoire dans images[]
	qui n'est NI dans cartesJoueurs NI déjà dans carteMilieu
	on stocke l'image séléctionnée dans carteMilieu[i]
	
On mélange carteMilieu puis on la retourne accompagnée d'un code **200**
	
