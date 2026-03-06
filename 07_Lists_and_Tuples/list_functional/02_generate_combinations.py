# ---------------------------------------------------------------------------
# 82. Generate Combinations of n Distinct Objects from List
# ---------------------------------------------------------------------------
# Descripción: Generate Combinations of n Distinct Objects from List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

import itertools

def combinations_from_list(lst: list, r: int) -> list:
    # Se construye list/set/dict a partir del iterable (elimina duplicados en set/dict).
    return list(itertools.combinations(lst, r))


sample = [1, 2, 3, 4, 5]
for c in combinations_from_list(sample, 2)[:5]:
    print(list(c))
