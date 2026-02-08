# ---------------------------------------------------------------------------
# 241. Frequency Dict from List (unique values as keys, count as value)
# ---------------------------------------------------------------------------
# Descripción: Frequency Dict from List (unique values as keys, count as value)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

from collections import Counter

def frequency_dict(lst: list) -> dict:
    # Se construye list/set/dict a partir del iterable (elimina duplicados en set/dict).
    return dict(Counter(lst))


print(frequency_dict(['a', 'b', 'a', 'c', 'a', 'b', 'f', 'e', 'e']))
