N = 8  # Size of the chessboard

def solveNQueens(board, col):
    if col == N:
        print(board)
        return True

    for row in range(N):
        if isSafe(board, row, col):
            board[row][col] = 1
            if solveNQueens(board, col + 1):
                return True
            board[row][col] = 0

    return False

def isSafe(board, row, col):
    # Check if a queen can be placed at position (row, col) on the board
    for x in range(col):
        if board[row][x] == 1:
            return False

    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    for x, y in zip(range(row, N, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    return True

board = [[0 for _ in range(N)] for _ in range(N)]

if not solveNQueens(board, 0):
    print("No solution found")
