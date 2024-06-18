def print_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")

    player1 = input("Enter name of Player 1 (X): ")
    player2 = input("Enter name of Player 2 (O): ")

    current_player = player1
    current_symbol = 'X'

    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        while True:
            move = input(f"{current_player}'s turn ({current_symbol}), enter your move (row[1-3] column[1-3]): ")
            try:
                row, col = map(int, move.split())
                if row < 1 or row > 3 or col < 1 or col > 3:
                    raise ValueError
                if board[row-1][col-1] != ' ':
                    print("That cell is already taken. Try again.")
                else:
                    board[row-1][col-1] = current_symbol
                    break
            except ValueError:
                print("Invalid input. Please enter row and column numbers separated by space.")

        if check_winner(board, current_symbol):
            print_board(board)
            print(f"Congratulations! {current_player} ({current_symbol}) wins!")
            break

        if all(all(cell != ' ' for cell in row) for row in board):
            print_board(board)
            print("It's a draw!")
            break

        if current_player == player1:
            current_player = player2
            current_symbol = 'O'
        else:
            current_player = player1
            current_symbol = 'X'

    print("Thanks for playing!")

tic_tac_toe()
