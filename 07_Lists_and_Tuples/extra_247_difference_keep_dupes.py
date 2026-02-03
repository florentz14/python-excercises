# ---------------------------------------------------------------------------
# 247. Difference Between Iterables Without Filtering Duplicates
# ---------------------------------------------------------------------------
# Descripción: Difference Between Iterables Without Filtering Duplicates
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def difference_keep_dupes(a: list, b: list) -> list:
    result = a.copy()
    for x in b:
        if x in result:
            result.remove(x)
    return result


print(difference_keep_dupes([1, 2, 2, 3], [2]))  # [1, 2, 3]
