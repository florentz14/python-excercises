# ---------------------------------------------------------------------------
# 129. Reverse Each List in Nested List
# ---------------------------------------------------------------------------
# Descripción: Reverse Each List in Nested List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def reverse_each(lst: list[list]) -> list[list]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [sublist[::-1] for sublist in lst]


sample = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(reverse_each(sample))
