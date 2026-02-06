# ---------------------------------------------------------------------------
# 165. Split List into Specified-Sized Chunks
# ---------------------------------------------------------------------------
# Descripción: Split List into Specified-Sized Chunks
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def chunk_list(lst: list, size: int) -> list[list]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [lst[i:i + size] for i in range(0, len(lst), size)]


sample = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
print(chunk_list(sample, 3))
print(chunk_list(sample, 4))
