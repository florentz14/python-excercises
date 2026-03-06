# ---------------------------------------------------------------------------
# 174. Add Number to Each Element in List
# ---------------------------------------------------------------------------
# Descripción: Add Number to Each Element in List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def add_to_each(lst: list[int | float], n: int | float) -> list:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [x + n for x in lst]


print(add_to_each([3, 8, 9, 4, 5, 0, 5, 0, 3], 3))
print(add_to_each([3.2, 8, 9.9, 4.2, 5, 0.1], 0.51))
