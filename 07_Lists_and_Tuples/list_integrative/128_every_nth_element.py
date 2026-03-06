# ---------------------------------------------------------------------------
# 269. Get Every nth Element
# ---------------------------------------------------------------------------
# Descripción: Get Every nth Element
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def every_nth(lst: list, n: int) -> list:
    return lst[::n]


sample = list(range(1, 11))
print(every_nth(sample, 2))  # [1, 3, 5, 7, 9]
print(every_nth(sample, 5))  # [1, 6]
