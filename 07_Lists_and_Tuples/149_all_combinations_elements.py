# ---------------------------------------------------------------------------
# 149. Generate All Combinations of List Elements (powerset)
# ---------------------------------------------------------------------------
# Descripción: Generate All Combinations of List Elements (powerset)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

import itertools

def all_combinations(lst: list) -> list[list]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [list(c) for r in range(len(lst) + 1) for c in itertools.combinations(lst, r)]


sample = ['orange', 'red', 'green', 'blue']
print(len(all_combinations(sample)))  # 16
