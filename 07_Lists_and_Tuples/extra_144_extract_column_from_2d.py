# ---------------------------------------------------------------------------
# 144. Extract Every First (or n-th) Element from 2D List
# ---------------------------------------------------------------------------
# Descripción: Extract Every First (or n-th) Element from 2D List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def extract_nth_column(matrix: list[list], n: int = 0) -> list:
    """n=0: first, n=2: third column."""
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [row[n] for row in matrix if len(row) > n]


sample = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
print(extract_nth_column(sample, 0))  # [1, 4, 7]
print(extract_nth_column(sample, 2))  # [3, 6, 9]
