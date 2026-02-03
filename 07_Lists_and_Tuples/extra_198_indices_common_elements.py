# ---------------------------------------------------------------------------
# 198. Indices of Values in First List That Appear in Second List
# ---------------------------------------------------------------------------
# Descripción: Indices of Values in First List That Appear in Second List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def indices_in_both(list1: list, list2: list) -> list[int]:
    set2 = set(list2)
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [i for i, x in enumerate(list1) if x in set2]


list1 = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 5, 2, 10, 12]
print(indices_in_both(list1, list2))  # [1, 4]
