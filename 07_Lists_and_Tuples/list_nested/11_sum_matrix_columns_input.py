# ---------------------------------------------------------------------------
# 87. Read Matrix from Console, Print Sum for Each Column
# ---------------------------------------------------------------------------
# Descripción: Read Matrix from Console, Print Sum for Each Column
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def read_matrix_and_sum_columns(rows: int, cols: int) -> list[int]:
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [sum(matrix[r][c] for r in range(rows)) for c in range(cols)]


# Uncomment to run interactively:
# r, c = int(input("Rows: ")), int(input("Cols: "))
# print("Sum each column:", read_matrix_and_sum_columns(r, c))
matrix = [[1, 2], [3, 4]]
print([sum(row[j] for row in matrix) for j in range(len(matrix[0]))])  # [4, 6]
