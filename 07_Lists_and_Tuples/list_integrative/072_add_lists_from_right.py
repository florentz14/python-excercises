# ---------------------------------------------------------------------------
# 156. Add Two Lists from Right (align by last element, pad left)
# ---------------------------------------------------------------------------
# Descripción: Add Two Lists from Right (align by last element, pad left)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def add_lists_right(a: list[int], b: list[int]) -> list[int]:
    na, nb = len(a), len(b)
    if na >= nb:
        b_padded = [0] * (na - nb) + b
        # Lista por comprensión: se construye la lista a partir del iterable.
        return [a[i] + b_padded[i] for i in range(na)]
    else:
        a_padded = [0] * (nb - na) + a
        # Lista por comprensión: se construye la lista a partir del iterable.
        return [a_padded[i] + b[i] for i in range(nb)]


print(add_lists_right([2, 4, 7, 0, 5, 8], [3, 3, -1, 7]))  # [2, 4, 10, 3, 4, 15]
