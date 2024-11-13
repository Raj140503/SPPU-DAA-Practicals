# Design 8-Queens matrix having first Queen placed. Use backtracking to place remaining Queens to generate the final 8-queen’s matrix.

N = 8 

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve(board, row):
    if row == N:
        return True
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if solve(board, row + 1):
                return True
            board[row] = -1 
    return False

board = [-1] * N
board[0] = 0

if solve(board, 1):
    for i in range(N):
        print(" ".join("Q" if board[i] == j else "." for j in range(N)))
else:
    print("No solution exists.")

'''
Output:

Q . . . . . . .
. . . . Q . . .
. . . . . . . Q
. . . . . Q . .
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
. . . Q . . . .
'''