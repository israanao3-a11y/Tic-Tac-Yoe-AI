import math

# ==========================================
# 1. CONSTANTES ET CONFIGURATION
# ==========================================
PLAYER_X = 'X'  # L'utilisateur (Humain)
PLAYER_O = 'O'  # L'ordinateur (IA)
EMPTY = ' '

# ==========================================
# 2. FONCTIONS DE LOGIQUE (DÉFINITIONS)
# ==========================================

def print_board(board):
    """Affiche le plateau de jeu dans la console"""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def evaluate_board(board):
    """Calcule le score du plateau (+1 pour IA, -1 pour Humain)"""
    # Vérification des lignes
    for row in board:
        if row.count(PLAYER_O) == 3: return 1
        if row.count(PLAYER_X) == 3: return -1
            
    # Vérification des colonnes
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return 1 if board[0][col] == PLAYER_O else -1
            
    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return 1 if board[0][0] == PLAYER_O else -1
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return 1 if board[0][2] == PLAYER_O else -1
        
    return 0

def is_game_over(board):
    """Vérifie si la partie est terminée"""
    if evaluate_board(board) != 0:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True

def minimax(board, depth, is_maximizing):
    """L'algorithme Minimax pour l'exploration des états"""
    if is_game_over(board):
        return evaluate_board(board)

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    """Trouve le coup optimal pour l'ordinateur"""
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                score = minimax(board, 0, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# ==========================================
# 3. FONCTION PRINCIPALE (MAIN)
# ==========================================

def main():
    board = [[EMPTY] * 3 for _ in range(3)]
    print("--- Bienvenue au jeu Tic-Tac-Toe ---")
    print_board(board)

    while not is_game_over(board):
        # Tour du Joueur X (Humain)
        while True:
            try:
                entree = input("Entrez ligne et colonne (0 1 2) séparées par un espace : ")
                x, y = map(int, entree.split())
                if board[x][y] == EMPTY:
                    board[x][y] = PLAYER_X
                    break
                else:
                    print("Case déjà occupée ! Réessayez.")
            except (ValueError, IndexError):
                print("Entrée invalide. Utilisez les chiffres 0, 1 ou 2.")

        print_board(board)
        if is_game_over(board):
            break

        # Tour de l'Ordinateur O (IA)
        print("\nTour de l'ordinateur...")
        move = find_best_move(board)
        if move != (-1, -1):
            board[move[0]][move[1]] = PLAYER_O
        
        print_board(board)

    # Affichage du résultat final
    resultat = evaluate_board(board)
    if resultat == 1:
        print("\nL'ordinateur (O) a gagné !")
    elif resultat == -1:
        print("\nFélicitations ! Vous (X) avez gagné !")
    else:
        print("\nMatch nul !")

if __name__ == "__main__":
    main()