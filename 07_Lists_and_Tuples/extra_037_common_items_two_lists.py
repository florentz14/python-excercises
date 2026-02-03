# ---------------------------------------------------------------------------
# 37. Find Common Items in Two Lists
# ---------------------------------------------------------------------------
# Descripción: Find Common Items in Two Lists
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def common_items(a: list, b: list) -> list:
    # Se construye list/set/dict a partir del iterable (elimina duplicados en set/dict).
    return list(set(a) & set(b))


print(common_items([1, 2, 3], [2, 3, 4]))  # [2, 3]
