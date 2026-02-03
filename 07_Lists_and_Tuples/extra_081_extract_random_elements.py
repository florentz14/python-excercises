# ---------------------------------------------------------------------------
# 81. Extract N Randomly Selected Elements from List
# ---------------------------------------------------------------------------
# Descripción: Extract N Randomly Selected Elements from List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

import random

def random_sample(lst: list, n: int) -> list:
    return random.sample(lst, min(n, len(lst)))


sample = [1, 1, 2, 3, 4, 4, 5, 1]
print(random_sample(sample, 3))
