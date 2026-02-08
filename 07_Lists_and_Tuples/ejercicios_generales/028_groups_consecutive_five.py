# ---------------------------------------------------------------------------
# 44. Generate Groups of Five Consecutive Numbers
# ---------------------------------------------------------------------------
# Descripción: Generate Groups of Five Consecutive Numbers
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def groups_of_five(n: int) -> list[list[int]]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [list(range(i, i + 5)) for i in range(1, n - 4 + 1)]


# e.g. 3 groups: [1,2,3,4,5], [2,3,4,5,6], [3,4,5,6,7]
print(groups_of_five(10)[:3])
