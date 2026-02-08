# ---------------------------------------------------------------------------
# 147. Randomly Interleave Two Lists
# ---------------------------------------------------------------------------
# Descripción: Randomly Interleave Two Lists
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

import random

def random_interleave(a: list, b: list) -> list:
    result = a + b
    random.shuffle(result)
    return result


print(random_interleave([1, 2, 7, 8], [4, 3, 8, 9]))
