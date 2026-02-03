# ---------------------------------------------------------------------------
# 215. Merge Lists into List of Lists (zip by position)
# ---------------------------------------------------------------------------
# Descripción: Merge Lists into List of Lists (zip by position)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def merge_into_list_of_lists(*lists: list) -> list[list]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [list(t) for t in zip(*lists)]


print(merge_into_list_of_lists(['a', 'b'], [1, 2], [True, False]))  # [['a', 1, True], ['b', 2, False]]
