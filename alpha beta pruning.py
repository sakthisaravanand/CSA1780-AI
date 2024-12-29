import math

# Define the board and players
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

# Check for a winner
def check_winner(board):
    # Check rows, columns, and diagonals
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None  # No winner yet

# Check if the board is full
def is_full(board):
    for row in board:
        if EMPTY in row:
            return False
    return True

# Minimax with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    winner = check_winner(board)
    
    if winner == PLAYER_X:
        return 1  # X wins
    if winner == PLAYER_O:
        return -1  # O wins
    if is_full(board):
        return 0  # Tie (board is full)
    
    if maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break  # Beta cut-off
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break  # Alpha cut-off
        return min_eval

# Find the best move for the current player
def best_move(board):
    best_score = -math.inf
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X  # Try X move
                score = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = EMPTY

                if score > best_score:
                    best_score = score
                    move = (i, j)

    return move

# Print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Main function to play the game
def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe with Alpha-Beta Pruning\n")
    print_board(board)

    while True:
        # Player X's turn (Maximizing player)
        print("Player X's turn")
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = PLAYER_X
            print_board(board)
        if check_winner(board) == PLAYER_X:
            print("Player X wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        # Player O's turn (Minimizing player)
        print("Player O's turn")
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = PLAYER_O
            print_board(board)
        if check_winner(board) == PLAYER_O:
            print("Player O wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

# Run the game
play_game()
