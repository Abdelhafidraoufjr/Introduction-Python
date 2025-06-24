def display_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---+---+---")
    print("\n")

def player_input(player, board):
    while True:
        try:
            pos = int(input(f"Joueur {player}, entrez une position (1-9): "))
            if pos < 1 or pos > 9:
                print("Position invalide, entrez un nombre entre 1 et 9.")
                continue
            row = (pos - 1) // 3
            col = (pos - 1) % 3
            if board[row][col] != " ":
                print("Cette case est déjà prise, choisis-en une autre.")
            else:
                return row, col
        except ValueError:
            print("Entrée invalide, entrez un nombre.")

def check_win(board):
    lines = []

    for i in range(3):
        lines.append(board[i])

    for j in range(3):
        lines.append([board[i][j] for i in range(3)])

    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    for line in lines:
        if line == ["X", "X", "X"]:
            return "X"
        elif line == ["O", "O", "O"]:
            return "O"
    return None

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def play():
    board = [[" "] * 3 for _ in range(3)]
    current_player = "X"

    while True:
        display_board(board)
        row, col = player_input(current_player, board)
        board[row][col] = current_player

        winner = check_win(board)
        if winner:
            display_board(board)
            print(f"Félicitations, joueur {winner} a gagné !")
            break

        if is_board_full(board):
            display_board(board)
            print("Match nul, le plateau est rempli sans gagnant.")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play()