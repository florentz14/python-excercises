# Archivo: 47_02_sudoku.py
# Descripción: Solucionador de Sudoku (backtracking)

print("=== 2. Solucionador de Sudoku ===\n")


def es_valido_sudoku(tablero, fila, col, num):
    """Verifica si es válido colocar num en (fila, col)."""
    n = len(tablero)
    tam_cuadrante = int(n ** 0.5)

    for j in range(n):
        if tablero[fila][j] == num:
            return False
    for i in range(n):
        if tablero[i][col] == num:
            return False

    inicio_fila = (fila // tam_cuadrante) * tam_cuadrante
    inicio_col = (col // tam_cuadrante) * tam_cuadrante
    for i in range(inicio_fila, inicio_fila + tam_cuadrante):
        for j in range(inicio_col, inicio_col + tam_cuadrante):
            if tablero[i][j] == num:
                return False
    return True


def resolver_sudoku(tablero):
    """Resuelve el Sudoku usando backtracking."""
    n = len(tablero)
    fila_vacia = col_vacia = -1

    for i in range(n):
        for j in range(n):
            if tablero[i][j] == 0:
                fila_vacia, col_vacia = i, j
                break
        if fila_vacia != -1:
            break

    if fila_vacia == -1:
        return True

    for num in range(1, n + 1):
        if es_valido_sudoku(tablero, fila_vacia, col_vacia, num):
            tablero[fila_vacia][col_vacia] = num
            if resolver_sudoku(tablero):
                return True
            tablero[fila_vacia][col_vacia] = 0
    return False


def imprimir_sudoku(tablero):
    """Imprime el Sudoku de forma visual."""
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
