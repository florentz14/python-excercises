# ---------------------------------------------------------------------------
# 30. Count Frequency of Elements in List
# ---------------------------------------------------------------------------
# Descripción: Count Frequency of Elements in List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

from collections import Counter

def frequency(lst: list) -> dict:
    # Se construye list/set/dict a partir del iterable (elimina duplicados en set/dict).
    return dict(Counter(lst))


# Or manual: {x: lst.count(x) for x in set(lst)}
print(frequency([1, 2, 2, 3, 3, 3, 4]))
