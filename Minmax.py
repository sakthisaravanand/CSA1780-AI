# Define constants
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Check if the game has a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):  # Check row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check column
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:  # Check diagonal
        return True
    if board[0][2] == player and board[1][1] player and board[2][0] == player: # Check anti-diagonal
        return True
    return False

def is_board_full(board):
    for row in board:
        if EMPTY in row:
            return False
    return True

def minimax(board, depth, is_maximizing_player):
    if check_winner(board, PLAYER_X):
        return 1  # X wins
    if check_winner(board, PLAYER_O):
        return -1  # O wins
    if is_board_full(board):
        return 0  # Draw

    if is_maximizing_player:
        max_eval = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_X
                    eval = minimax(board, depth + 1, False)
                    board[row][col] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_O
                    eval = minimax(board, depth + 1, True)
                    board[row][col] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_val = -float('inf')
    move = (-1, -1)

    # Evaluate every possible move for player X
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X
                move_val = minimax(board, 0, False)
                board[row][col] = EMPTY

                # If the value of the current move is better than the best value, update best value
                if move_val > best_val:
                    best_val = move_val
                    move = (row, col)

    return move

# Function to run the Tic Tac Toe game
def tic_tac_toe():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe with Minimax!")
    print_board(board)

    while True:
        if is_board_full(board):
            print("It's a draw!")
            break

        # Player X's turn (Maximizing)
        print("Player X's turn (Maximizing):")
        row, col = best_move(board)
        board[row][col] = PLAYER_X
        print_board(board)
        if check_winner(board, PLAYER_X):
            print("Player X wins!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        # Player O's turn (Minimizing)
        print("Player O's turn (Minimizing):")
        row, col = best_move(board)
        board[row][col] = PLAYER_O
        print_board(board)
        if check_winner(board, PLAYER_O):
            print("Player O wins!")
            break

# Start the game
if __name__ == "__main__":
    tic_tac_toe()
