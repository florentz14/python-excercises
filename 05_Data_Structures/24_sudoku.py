# -------------------------------------------------
# File Name: 24_sudoku.py
# Author: Florentino Báez
# Date: Data Structures - Backtracking
# Description: Sudoku Solver (Backtracking).
#              Solves a 9x9 Sudoku by finding empty cells (0),
#              trying numbers 1-9 and verifying they do not
#              repeat in row, column or 3x3 box. If a number
#              does not lead to a solution, backtracks.
#              Complexity: O(9^(empty cells)) worst case.
# -------------------------------------------------

print("=== 2. Solucionador de Sudoku ===\n")


def es_valido_sudoku(tablero, fila, col, num):
    """Check whether it is valid to place num at (fila, col)."""
    n = len(tablero)
    tam_cuadrante = int(n ** 0.5)

    # Check that num is not in the same row
    for j in range(n):
        if tablero[fila][j] == num:
            return False
    # Check that num is not in the same column
    for i in range(n):
        if tablero[i][col] == num:
            return False

    # Check that num is not in the 3x3 box
    inicio_fila = (fila // tam_cuadrante) * tam_cuadrante
    inicio_col = (col // tam_cuadrante) * tam_cuadrante
    for i in range(inicio_fila, inicio_fila + tam_cuadrante):
        for j in range(inicio_col, inicio_col + tam_cuadrante):
            if tablero[i][j] == num:
                return False
    return True  # The number is valid in this position


def resolver_sudoku(tablero):
    """Solve the Sudoku using backtracking."""
    n = len(tablero)
    fila_vacia = col_vacia = -1

    # Find the first empty cell (value 0)
    for i in range(n):
        for j in range(n):
            if tablero[i][j] == 0:
                fila_vacia, col_vacia = i, j
                break
        if fila_vacia != -1:
            break

    if fila_vacia == -1:
        return True  # No empty cells → Sudoku solved

    # Try numbers from 1 to 9
    for num in range(1, n + 1):
        if es_valido_sudoku(tablero, fila_vacia, col_vacia, num):
            tablero[fila_vacia][col_vacia] = num  # Place number
            if resolver_sudoku(tablero):
                return True
            tablero[fila_vacia][col_vacia] = 0  # Backtrack: remove number
    return False  # No number works → backtrack


def imprimir_sudoku(tablero):
    """Print the Sudoku visually."""
    n = len(tablero)
    tam_cuadrante = int(n ** 0.5)
    for i in range(n):
        if i % tam_cuadrante == 0 and i != 0:
            print("-" * (n * 2 + tam_cuadrante))
        for j in range(n):
            if j % tam_cuadrante == 0 and j != 0:
                print("|", end=" ")
            print(tablero[i][j] if tablero[i][j] != 0 else ".", end=" ")
        print()


if __name__ == "__main__":
    sudoku_ejemplo = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Sudoku original:")
    imprimir_sudoku(sudoku_ejemplo)

    if resolver_sudoku(sudoku_ejemplo):
        print("\nSudoku resuelto:")
        imprimir_sudoku(sudoku_ejemplo)
    else:
        print("\nNo se encontró solución")
