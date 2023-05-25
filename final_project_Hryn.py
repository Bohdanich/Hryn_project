def print_board(board):
    """Prints the tic-tac-toe board."""
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-" * 9)
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-" * 9)
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_win(board):
    """Checks if the game has been won."""
    wins = [
        # Rows
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        # Columns
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        # Diagonals
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return True
    return False

def get_computer_move(board):
    """Returns the computer's move."""
    # First move: place an X in the middle of the board.
    if board == [" "] * 9:
        return 4
    # Check if the computer can win in the next move.
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_win(board):
                return i
            board[i] = " "
    # Check if the player can win in the next move and block them.
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_win(board):
                board[i] = "X"
                return i
            board[i] = " "
    # Otherwise, pick a random empty square.
    import random
    while True:
        i = random.randint(0, 8)
        if board[i] == " ":
            return i

def get_player_move(board):
    """Gets the player's move."""
    while True:
        try:
            move = int(input("Enter a number between 1 and 9: ")) - 1
            if not (0 <= move <= 8):
                raise ValueError("Number must be between 1 and 9.")
            if board[move] != " ":
                raise ValueError("That square is already occupied.")
            return move
        except ValueError:
            print("You must enter only numbers between 1 and 9!")

def play_game():
    """Plays a game of tic-tac-toe."""
    board = [" "] * 9
    print("Welcome to tic-tac-toe!")
    print_board(board)
    while True:
        # Computer move
        computer_move = get_computer_move(board)
        board[computer_move] = "X"
        print("Computer's move:")
        print_board(board)
        if check_win(board):
            print("Computer wins!")
            return
        if " " not in board:
            print("It's a draw!")
            return
        # Player move
        player_move = get_player_move(board)
        board[player_move] = "O"
        print_board(board)
        if check_win(board):
            print("You win!")
            return

play_game()