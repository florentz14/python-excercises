# ---------------------------------------------------------------------------
# 264. Convert List of Lists to 2D (transpose to tuples of columns)
# ---------------------------------------------------------------------------
# Descripción: Convert List of Lists to 2D (transpose to tuples of columns)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def rows_to_columns(matrix: list[list]) -> list[tuple]:
    # Se construye list/set/dict a partir del iterable (elimina duplicados en set/dict).
    return list(zip(*matrix))


sample = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(rows_to_columns(sample))  # [(1,4,7,10), (2,5,8,11), (3,6,9,12)]
