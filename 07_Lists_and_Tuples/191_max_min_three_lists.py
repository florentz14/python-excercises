# ---------------------------------------------------------------------------
# 191. Max and Min Values Across Three Lists
# ---------------------------------------------------------------------------
# Descripción: Max and Min Values Across Three Lists
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def max_min_three(*lists: list[int | float]) -> tuple:
    flat = [x for L in lists for x in L]
    return max(flat), min(flat)


list1 = [2, 3, 5, 8, 7, 2, 3]
list2 = [4, 3, 9, 0, 4, 3, 9]
list3 = [2, 1, 5, 6, 5, 5, 4]
print(max_min_three(list1, list2, list3))  # (9, 0)
