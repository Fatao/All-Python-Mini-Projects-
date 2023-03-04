def print_board(board):
    print("   |   |   ")
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " ")
    print("___|___|___")
    print("   |   |   ")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " ")
    print("___|___|___")
    print("   |   |   ")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " ")
    print("   |   |   ")

def check_win(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True
    # Check columns
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    # No win
    return False

def tic_tac_toe():
    # Initialize empty board
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    # Initialize players and starting player
    players = ["X", "O"]
    current_player = players[0]
    # Main game loop
    while True:
        # Print board
        print_board(board)
        # Get player input
        row = int(input(f"{current_player} row (1-3): ")) - 1
        col = int(input(f"{current_player} col (1-3): ")) - 1
        # Check if spot is empty
        if board[row][col] != " ":
            print("That spot is already taken.")
            continue
        # Update board
        board[row][col] = current_player
        # Check for win
        if check_win(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        # Check for tie
        if all([spot != " " for row in board for spot in row]):
            print_board(board)
            print("Tie game.")
            break
        # Switch to next player
        current_player = players[(players.index(current_player) + 1) % 2]

# Start game
tic_tac_toe()
