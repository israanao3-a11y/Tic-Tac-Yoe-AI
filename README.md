# 🎮 Tic-Tac-Toe AI (Algorithme Minimax)

> **Un agent intelligent imbattable** développé en Python. Ce projet utilise l'algorithme Minimax pour garantir une stratégie de jeu optimale.

---

## 🌟 Présentation du Projet
Ce projet a été réalisé dans le cadre d'un **TP d'Intelligence Artificielle**. L'objectif est de concevoir un jeu de Morpion (Tic-Tac-Toe) où l'ordinateur analyse toutes les possibilités futures pour choisir le meilleur coup possible.

## 🧠 Concepts d'Intelligence Artificielle
L'agent repose sur les piliers suivants :
* **Algorithme Minimax** : Exploration récursive de l'arbre des états.
* **Fonction d'Évaluation** : Attribution de scores pour quantifier l'avantage (IA : +1, Humain : -1, Nul : 0).
* **Espace d'états** : Analyse de toutes les configurations possibles du plateau 3x3.

## 🛠️ Architecture du Code
Le programme est structuré de manière modulaire :

| Fonction | Description |
| :--- | :--- |
| `evaluate_board` | Analyse le plateau et retourne le score heuristique. |
| `is_game_over` | Détecte si la partie est terminée (victoire ou match nul). |
| `minimax` | Calcule de manière récursive la valeur de chaque position. |
| `find_best_move` | Sélectionne la coordonnée optimale pour l'ordinateur. |
| `main` | Gère l'interface utilisateur, les entrées et la boucle de jeu. |

## 🚀 Installation et Lancement

1. **Cloner le dépôt :**
   ```bash
   git clone [https://github.com/israanao3-a11y/Tic-Tac-Yoe-AI.git](https://github.com/israanao3-a11y/Tic-Tac-Yoe-AI.git)
