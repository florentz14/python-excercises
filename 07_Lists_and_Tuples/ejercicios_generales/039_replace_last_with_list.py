# ---------------------------------------------------------------------------
# 58. Replace Last Element with Another List. [1,3,5,7,9,10], [2,4,6,8] -> [1,3,5,7,9,2,4,6,8]
# ---------------------------------------------------------------------------
# Descripción: Replace Last Element with Another List. [1,3,5,7,9,10], [2,4,6,8] -...
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def replace_last_with_list(lst: list, other: list) -> list:
    return lst[:-1] + other


print(replace_last_with_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]))
