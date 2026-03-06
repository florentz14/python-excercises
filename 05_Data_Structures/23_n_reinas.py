# -------------------------------------------------
# File Name: 23_n_reinas.py
# Author: Florentino Báez
# Date: Data Structures - Backtracking
# Description: N-Queens Problem (Backtracking).
#              Place N queens on an NxN board so that
#              none attack each other (not in row, column,
#              or diagonal). Tries positions column by column
#              and backtracks when there is no valid position.
#              Complexity: O(N!) in the worst case.
# -------------------------------------------------

print("=== Algoritmos de Backtracking ===\n")
print("=== 1. Problema de las N-Reinas ===\n")


def es_seguro(tablero, fila, col, n):
    """Check whether it is safe to place a queen at (fila, col)."""
    # Check row to the left
    for i in range(col):
        if tablero[fila][i] == 1:
            return False
    # Check upper left diagonal
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False
    # Check lower left diagonal
    for i, j in zip(range(fila, n, 1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False
    return True  # No conflicts → safe position


def n_reinas_backtracking(tablero, col, n, soluciones):
    """Solve the N-Queens problem using backtracking."""
    if col >= n:
        # All columns have a queen → solution found
        soluciones.append([fila[:] for fila in tablero])
        return True

    res = False
    for fila in range(n):
        if es_seguro(tablero, fila, col, n):
            tablero[fila][col] = 1  # Place queen
            res = n_reinas_backtracking(tablero, col + 1, n, soluciones) or res
            tablero[fila][col] = 0  # Backtrack: remove queen and try next row
    return res


def resolver_n_reinas(n, encontrar_todas=True):
    """Solve the N-Queens problem."""
    tablero = [[0] * n for _ in range(n)]
    soluciones = []
    n_reinas_backtracking(tablero, 0, n, soluciones)
    return soluciones


def imprimir_tablero(tablero):
    """Print the board visually."""
    n = len(tablero)
    print("  " + " ".join(str(i) for i in range(n)))
    for i, fila in enumerate(tablero):
        print(f"{i} " + " ".join("Q" if celda == 1 else "." for celda in fila))


if __name__ == "__main__":
    n_reinas = 4
    print(f"Problema de las {n_reinas}-Reinas:")
    soluciones = resolver_n_reinas(n_reinas, encontrar_todas=True)
    print(f"\nNúmero de soluciones encontradas: {len(soluciones)}")
    if soluciones:
        print("\nPrimera solución:")
        imprimir_tablero(soluciones[0])
