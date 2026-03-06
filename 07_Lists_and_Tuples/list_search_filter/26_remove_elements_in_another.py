# ---------------------------------------------------------------------------
# 117. Remove All Elements Present in Another List
# ---------------------------------------------------------------------------
# Descripción: Remove All Elements Present in Another List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def remove_if_in(list1: list, list2: list) -> list:
    set2 = set(list2)
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [x for x in list1 if x not in set2]


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]
print(remove_if_in(list1, list2))  # [1, 3, 5, 7, 9, 10]
