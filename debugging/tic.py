#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True

    # Check diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True

    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 2:
                return value
            else:
                print("Invalid input. Please enter a number between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Get a valid row
        row = get_valid_input(f"Enter row (0, 1, or 2) for player {player}: ")

        # Get a valid column
        while True:
            col = get_valid_input(f"Enter column (0, 1, or 2) for player {player}: ")
            if board[row][col] == " ":
                break
            else:
                print("That spot is already taken! Try again.")

        # Place the player's mark
        board[row][col] = player

        # Check for a winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check for a draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

tic_tac_toe()

