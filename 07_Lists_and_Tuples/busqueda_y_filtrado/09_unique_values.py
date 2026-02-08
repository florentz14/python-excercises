# ---------------------------------------------------------------------------
# 29. Get Unique Values from List (preserve order)
# ---------------------------------------------------------------------------
# Descripción: Get Unique Values from List (preserve order)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def unique_values(lst: list) -> list:
    # Se construye list/set/dict a partir del iterable (elimina duplicados en set/dict).
    return list(dict.fromkeys(lst))


print(unique_values([1, 2, 2, 3, 3, 3, 4]))  # [1, 2, 3, 4]
