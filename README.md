# 🎮 Tic-Tac-Toe AI (Algorithme Minimax)

> Un agent intelligent imbattable développé en Python pour le jeu du Morpion.

## 🌟 Présentation du Projet
Ce projet a été réalisé dans le cadre d'un **TP d'Intelligence Artificielle**. L'objectif est d'implémenter l'algorithme de recherche **Minimax** pour créer un agent capable de jouer de manière optimale au Tic-Tac-Toe.

## 🧠 L'Intelligence derrière le jeu
L'agent utilise une approche de recherche dans l'espace d'états :
- **Algorithme** : Minimax (Récursif).
- **Heuristique** : 
  - `+1` si l'ordinateur (O) gagne.
  - `-1` si l'humain (X) gagne.
  - `0` pour un match nul.
- **Complexité** : L'IA explore toutes les combinaisons possibles pour garantir qu'elle ne perde jamais.

## 🛠️ Structure Technique
Le code est structuré de manière modulaire pour une meilleure lisibilité :
* `evaluate_board()` : Analyse le plateau pour détecter un vainqueur.
* `is_game_over()` : Détermine si la partie est terminée.
* `minimax()` : Calcule le meilleur score possible pour chaque mouvement.
* `find_best_move()` : Sélectionne la coordonnée optimale.
* `main()` : Gère l'interface utilisateur et la boucle de jeu.

## 🚀 Installation et Utilisation

1. **Cloner le projet** :
   ```bash
   git clone [https://github.com/israanao3-a11y/Tic-Tac-Yoe-AI.git](https://github.com/israanao3-a11y/Tic-Tac-Yoe-AI.git)
