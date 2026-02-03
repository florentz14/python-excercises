# ---------------------------------------------------------------------------
# 107. Remove Specified Column from Nested List (1-based column index)
# ---------------------------------------------------------------------------
# Descripción: Remove Specified Column from Nested List (1-based column index)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def remove_column(matrix: list[list], col: int) -> list[list]:
    """col is 1-based: 1 = first column."""
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [[row[i] for i in range(len(row)) if i != col - 1] for row in matrix]


sample = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print(remove_column(sample, 1))  # [[2, 3], [4, 5], [1, 1]]
