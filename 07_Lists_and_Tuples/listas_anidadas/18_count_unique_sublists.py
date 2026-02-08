# ---------------------------------------------------------------------------
# 94. Count Unique Sublists (frequency of each distinct sublist)
# ---------------------------------------------------------------------------
# Descripción: Count Unique Sublists (frequency of each distinct sublist)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

from collections import Counter

def unique_sublist_counts(lists: list[list]) -> dict:
    # Se construye list/set/dict a partir del iterable (elimina duplicados en set/dict).
    return dict(Counter(tuple(L) for L in lists))


sample = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
print(unique_sublist_counts(sample))
