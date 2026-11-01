# EXPERIMENT 5: Solving the 8-Queens Problem Using Backtracking

N = 8
board = [-1] * N  # board[row] = column containing the queen

def is_safe(row, col):
    for prev_row in range(row):
        prev_col = board[prev_row]
        if prev_col == col:
            return False
        if abs(prev_col - col) == abs(prev_row - row):
            return False
    return True

def solve(row):
    if row == N:
        return True

    for col in range(N):
        if is_safe(row, col):
            board[row] = col
            if solve(row + 1):
                return True
            board[row] = -1  # backtrack

    return False

if solve(0):
    print("EXPERIMENT 5 - 8 Queens Problem")
    print("One valid solution:")
    for row in range(N):
        print(" ".join("Q" if board[row] == col else "." for col in range(N)))
else:
    print("No solution found")
