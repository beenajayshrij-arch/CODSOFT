import math

board = [" " for _ in range(9)]

def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_draw():
    return " " not in board

def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)

        return best_score

def ai_move():
    best_score = -math.inf
    best_move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"

def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Please enter a number between 1 and 9.")
            elif board[move] != " ":
                print("That position is already taken.")
            else:
                board[move] = "X"
                break

        except ValueError:
            print("Invalid input. Enter a number.")

def show_positions():
    print("\nBoard Positions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()

def play_game():
    print("===== TIC-TAC-TOE AI =====")
    print("You are X")
    print("AI is O")

    show_positions()

    while True:
        print_board()

        human_move()

        if check_winner("X"):
            print_board()
            print("🎉 You Win!")
            break

        if is_draw():
            print_board()
            print("🤝 It's a Draw!")
            break

        ai_move()

        if check_winner("O"):
            print_board()
            print("🤖 AI Wins!")
            break

        if is_draw():
            print_board()
            print("🤝 It's a Draw!")
            break

play_game()
