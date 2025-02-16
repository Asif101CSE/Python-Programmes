def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        row, col = -1, -1
        while row not in range(3) or col not in range(3) or board[row][col] != " ":
            try:
                row, col = map(int, input(f"Player {players[turn % 2]}, enter row and column (0-2): ").split())
            except ValueError:
                print("Invalid input. Enter two numbers between 0 and 2.")
                continue
        
        board[row][col] = players[turn % 2]
        if check_winner(board, players[turn % 2]):
            print_board(board)
            print(f"Player {players[turn % 2]} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        turn += 1

if __name__ == "__main__":
    main()
