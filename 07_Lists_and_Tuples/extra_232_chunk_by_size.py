# ---------------------------------------------------------------------------
# 232. Chunk List by Size
# ---------------------------------------------------------------------------
# Descripción: Chunk List by Size
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def chunk_by_size(lst: list, size: int) -> list[list]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [lst[i:i + size] for i in range(0, len(lst), size)]


print(chunk_by_size([1, 2, 3, 4, 5, 6, 7, 8], 3))  # [[1,2,3], [4,5,6], [7,8]]
