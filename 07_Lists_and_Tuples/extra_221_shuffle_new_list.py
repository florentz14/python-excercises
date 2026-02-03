# ---------------------------------------------------------------------------
# 221. Shuffle List and Return New List
# ---------------------------------------------------------------------------
# Descripción: Shuffle List and Return New List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

import random

def shuffle_new(lst: list) -> list:
    result = lst.copy()
    random.shuffle(result)
    return result


print(shuffle_new([1, 2, 3, 4, 5, 6]))
