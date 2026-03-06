# ---------------------------------------------------------------------------
# 216. Group Elements by Function and Return Count per Group
# ---------------------------------------------------------------------------
# Descripción: Group Elements by Function and Return Count per Group
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

from collections import defaultdict

def group_by_count(lst: list, key_func) -> dict:
    groups = defaultdict(int)
    for x in lst:
        groups[key_func(x)] += 1
    # Se construye list/set/dict a partir del iterable (elimina duplicados en set/dict).
    return dict(groups)


print(group_by_count([1, 2, 3, 4, 5, 6], lambda x: x % 3))  # {0: 2, 1: 2, 2: 2}
print(group_by_count([1, 2, 3, 4, 5, 6], lambda x: x % 2))  # {0: 3, 1: 3}
