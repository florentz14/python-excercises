# ---------------------------------------------------------------------------
# 143. Frequency of Elements in Nested List (flatten then count)
# ---------------------------------------------------------------------------
# Descripción: Frequency of Elements in Nested List (flatten then count)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

from collections import Counter

def frequency_nested(lists: list[list]) -> dict:
    flat = [x for row in lists for x in row]
    # Se construye list/set/dict a partir del iterable (elimina duplicados en set/dict).
    return dict(Counter(flat))


sample = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
print(frequency_nested(sample))
