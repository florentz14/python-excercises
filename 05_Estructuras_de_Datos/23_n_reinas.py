# Archivo: 47_01_n_reinas.py
# Descripción: Problema de las N-Reinas (backtracking)

print("=== Algoritmos de Backtracking ===\n")
print("=== 1. Problema de las N-Reinas ===\n")


def es_seguro(tablero, fila, col, n):
    """Verifica si es seguro colocar una reina en (fila, col)."""
    for i in range(col):
        if tablero[fila][i] == 1:
            return False
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False
    for i, j in zip(range(fila, n, 1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False
    return True


def n_reinas_backtracking(tablero, col, n, soluciones):
    """Resuelve el problema de las N-Reinas usando backtracking."""
    if col >= n:
        soluciones.append([fila[:] for fila in tablero])
        return True

    res = False
    for fila in range(n):
        if es_seguro(tablero, fila, col, n):
            tablero[fila][col] = 1
            res = n_reinas_backtracking(tablero, col + 1, n, soluciones) or res
            tablero[fila][col] = 0
    return res


def resolver_n_reinas(n, encontrar_todas=True):
    """Resuelve el problema de las N-Reinas."""
    tablero = [[0] * n for _ in range(n)]
    soluciones = []
    n_reinas_backtracking(tablero, 0, n, soluciones)
    return soluciones


def imprimir_tablero(tablero):
    """Imprime el tablero de forma visual."""
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
