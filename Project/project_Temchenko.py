from random import randrange

def display_board(board):
    print("-------------")
    for i, row in enumerate(board):
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print("\n-------------")

def enter_move(board):
    while True:
        try:
            user_input = int(input("Enter your move (1-9): "))
            if 1 <= user_input <= 9:
                row = (user_input - 1) // 3
                col = (user_input - 1) % 3
                if board[row][col] == 'O' or board[row][col] == 'X':
                    print("Invalid move. The cell is already taken. Try again.")
                else:
                    board[row][col] = 'O'
                    break
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] != 'O' and board[row][col] != 'X':
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or all(board[j][i] == sign for j in range(3)):
            return True

    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True

    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = 'X'

board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]

display_board(board)

while True:
    enter_move(board)
    display_board(board)
    print("Your move:")

    if victory_for(board, 'O'):
        print("You win!")
        break

    print("Computer's move:")
    draw_move(board)
    display_board(board)

    if victory_for(board, 'X'):
        print("Computer wins!")
        break

    if not make_list_of_free_fields(board):
        print("It's a draw!")
        break
