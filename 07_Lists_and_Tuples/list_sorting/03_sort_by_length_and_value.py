# ---------------------------------------------------------------------------
# 96. Sort List of Lists by Length and Value
# ---------------------------------------------------------------------------
# Descripción: Sort List of Lists by Length and Value
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def sort_by_length_and_value(lists: list[list]) -> list[list]:
    # Lista de pares (longitud, lista) para poder comparar por longitud.
    return sorted(lists, key=lambda L: (len(L), L))


sample = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
print(sort_by_length_and_value(sample))
