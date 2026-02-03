# ---------------------------------------------------------------------------
# 142. Sum Specific Column in List of Lists (1-based column)
# ---------------------------------------------------------------------------
# Descripción: Sum Specific Column in List of Lists (1-based column)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def sum_column(matrix: list[list], col: int) -> int | float:
    # Se devuelve la suma de todos los elementos.
    return sum(row[col - 1] for row in matrix if len(row) >= col)


sample = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
print("Col 1:", sum_column(sample, 1))
print("Col 2:", sum_column(sample, 2))
print("Col 4:", sum_column(sample, 4))
