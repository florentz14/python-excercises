# -------------------------------------------------
# File: 23_n_reinas.py (N-Queens Problem - Backtracking)
# -------------------------------------------------
# Author: Florentino Báez
# Module: Data Structures - Backtracking
#
# Description:
#   Place N queens on an NxN chessboard so no two attack each other
#   (different rows, columns, and diagonals). Uses backtracking:
#   try each row for the current column; recurse or backtrack.
#
# Complexity: O(N!) worst case.
# -------------------------------------------------


def is_safe(board, row, col, n):
    """Returns True if placing a queen at (row, col) does not conflict."""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def _solve_n_queens(board, col, n, solutions):
    """Backtrack: place queen in current column, recurse to next."""
    if col >= n:
        solutions.append([row[:] for row in board])
        return True

    found = False
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            found = _solve_n_queens(board, col + 1, n, solutions) or found
            board[row][col] = 0
    return found


def solve_n_queens(n, find_all=True):
    """Returns list of all valid N-Queens solutions."""
    board = [[0] * n for _ in range(n)]
    solutions = []
    _solve_n_queens(board, 0, n, solutions)
    return solutions


def print_board(board):
    """Prints the board with Q for queens, . for empty."""
    n = len(board)
    print("  " + " ".join(str(i) for i in range(n)))
    for i, row in enumerate(board):
        print(f"{i} " + " ".join("Q" if cell == 1 else "." for cell in row))


if __name__ == "__main__":
    print("=== Backtracking: N-Queens ===\n")

    n = 4
    print(f"N-Queens problem (N={n}):")
    solutions = solve_n_queens(n, find_all=True)
    print(f"\nNumber of solutions: {len(solutions)}")
    if solutions:
        print("\nFirst solution:")
        print_board(solutions[0])
