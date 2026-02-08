# ---------------------------------------------------------------------------
# 182. Max and Min Sum Sublist in List of Lists
# ---------------------------------------------------------------------------
# Descripción: Max and Min Sum Sublist in List of Lists
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def max_min_sublist_sum(lists: list[list[int]]) -> tuple[list[int], list[int]]:
    with_sum = [(sum(L), L) for L in lists]
    # max/min por clave: se compara por el primer elemento de cada tupla (longitud).
    max_list = max(with_sum, key=lambda x: x[0])[1]
    # max/min por clave: se compara por el primer elemento de cada tupla (longitud).
    min_list = min(with_sum, key=lambda x: x[0])[1]
    return max_list, min_list


sample = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
print(max_min_sublist_sum(sample))
