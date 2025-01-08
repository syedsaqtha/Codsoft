def evaluate(board):
    
    for row in board:
        if row.count('X') == 3:
            return 10
        elif row.count('O') == 3:
            return -10

    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == 'X':
            return 10
        elif board[0][col] == board[1][col] == board[2][col] == 'O':
            return -10

    
    if (board[0][0] == board[1][1] == board[2][2] == 'X' or
            board[0][2] == board[1][1] == board[2][0] == 'X'):
        return 10
    elif (board[0][0] == board[1][1] == board[2][2] == 'O' or
            board[0][2] == board[1][1] == board[2][0] == 'O'):
        return -10

    
    return 0

def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score == 10:
        return score
    elif score == -10:
        return score
    elif depth == 0:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best_score = max(best_score, minimax(board, depth - 1, False))
                    board[i][j] = ' '
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best_score = min(best_score, minimax(board, depth - 1, True))
                    board[i][j] = ' '
        return best_score

def find_best_move(board):
    best_val = -float('inf')
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move


board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

while True:
    
    row, col = map(int, input("Enter your move (row, col): ").split())
    board[row][col] = 'O'

    
    if evaluate(board) == -10:
        print("You win!")
        break


    if all(all(cell != ' ' for cell in row) for row in board):
        print("Draw!")
        break

    
    row, col = find_best_move(board)
    board[row][col] = 'X'

    
    for row in board:
        print(row)
    print()

    if evaluate(board) == 10:
        print("AI wins!")
        break 