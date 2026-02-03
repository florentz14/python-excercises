# ---------------------------------------------------------------------------
# 116. Sort List of Lists by Given Index of Inner List
# ---------------------------------------------------------------------------
# Descripción: Sort List of Lists by Given Index of Inner List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def sort_by_inner_index(lst: list[tuple], index: int) -> list:
    # Se ordena la lista usando key para comparar (p. ej. por longitud o valor).
    return sorted(lst, key=lambda t: t[index])


sample = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94)]
print(sort_by_inner_index(sample, 0))  # by name
print(sort_by_inner_index(sample, 2))  # by third element
