# ---------------------------------------------------------------------------
# 108. Extract Specified Column from Nested List (1-based)
# ---------------------------------------------------------------------------
# Descripción: Extract Specified Column from Nested List (1-based)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def extract_column(matrix: list[list], col: int) -> list:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [row[col - 1] for row in matrix]


sample = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print(extract_column(sample, 1))  # [1, 2, 1]
print(extract_column(sample, 3))  # [3, 5, 1]
