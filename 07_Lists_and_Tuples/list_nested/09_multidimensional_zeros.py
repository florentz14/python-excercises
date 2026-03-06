# ---------------------------------------------------------------------------
# 85. Create Multidimensional List with Zeros
# ---------------------------------------------------------------------------
# Descripción: Create Multidimensional List with Zeros
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def zeros_2d(rows: int, cols: int) -> list[list[int]]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [[0] * cols for _ in range(rows)]


print(zeros_2d(3, 2))  # [[0, 0], [0, 0], [0, 0]]
