# Choplifter

## I - Besoins

**Python 3** ou une version plus récente
> Librairie "**Pygame 2.5.0**"  
> Paquet "**PyInstaller 6.7.0**"  
  
## II - Commandes du CHPrompt

**1 - /clear**  
> Vide le CHPrompt  
  
**2 - /exit**  
> Ferme le CHPrompt  
  
**3 - /help**  
> Affiche la liste des commandes 
  
**4 - /play** *[ -f ]* *[ -s ]*  
> Lance le Choplifter  
> [ -f ] - Mode plein-écran *(experimental)*  
> [ -s ] - Mode survie 
  
**5 - /repo**  
> Renvoie le lien du repository  
  
## III - Jeu  
  
### Introduction
  
> Le jeu *Choplifter* est une simulation de sauvetage d'otages à l'aide d'un hélicoptère, où le joueur doit éviter les ennemis et sauver le maximum d'otages. Ce jeu nécessite Python et la bibliothèque Pygame.  
  
### Logique du jeu
  
> **Initialisation**: Configuration de la fenêtre de jeu, chargement des images, et initialisation des variables de jeu.  
> **Boucle principale**: Gestion des entrées du joueur, mise à jour de l'état du jeu, et rendu des graphiques.  
> **Gestion des collisions**: Détecte les collisions entre l'hélicoptère, les ennemis, les otages, et les projectiles pour gérer les interactions.  
> **Sauvetage d'otages**: L'hélicoptère doit atterrir près des otages pour les sauver. Les otages se dirigent vers l'hélicoptère lorsque celui-ci est au sol.  
> **Fin du jeu**: Le jeu se termine lorsque tous les otages sont sauvés ou que l'hélicoptère est détruit.  
  
### Éléments du jeu
  
> **Hélicoptère**: Le véhicule du joueur. Peut se déplacer dans toutes les directions et tirer des projectiles.  
> **Ennemis**: Tanks, jets, et aliens tentant de détruire l'hélicoptère.  
> **Otages**: Civils à sauver. Ils se déplacent vers l'hélicoptère lorsqu'il atterrit.  
> **Base**: Structures où les otages sont initialement localisés.  
> **Projectiles**: Tirés par l'hélicoptère pour éliminer les ennemis.  
  
### Fin du jeu
  
>Le jeu se termine lorsque tous les otages sont sauvés ou que l'hélicoptère est détruit. Le score final, basé sur le nombre d'otages sauvés et d'ennemis détruits, est affiché à l'écran.  
  
## IV - Développeurs
  
> [MOERUYONAKI](https://www.github.com/MOERUYONAKI)  
> [Kevin-Sawyer](https://www.github.com/Kevin-Sawyer)  
  
