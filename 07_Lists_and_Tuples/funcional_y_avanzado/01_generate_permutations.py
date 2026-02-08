# ---------------------------------------------------------------------------
# 18. Generate All Permutations of a List
# ---------------------------------------------------------------------------
# Descripción: Generate All Permutations of a List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

import itertools

def all_permutations(lst: list) -> list:
    # Se construye list/set/dict a partir del iterable (elimina duplicados en set/dict).
    return list(itertools.permutations(lst))


sample = [1, 2, 3]
print(all_permutations(sample))
