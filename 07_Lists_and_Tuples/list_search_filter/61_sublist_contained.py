# ---------------------------------------------------------------------------
# 270. Check If First List Is Contained in Second (Regardless of Order)
# ---------------------------------------------------------------------------
# Descripción: Check If First List Is Contained in Second (Regardless of Order)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def sublist_contained(sub: list, lst: list) -> bool:
    # Se construye list/set/dict a partir del iterable (elimina duplicados en set/dict).
    return set(sub) <= set(lst)


print(sublist_contained([1, 2], [1, 2, 3, 4]))   # True
print(sublist_contained([1, 5], [1, 2, 3, 4]))   # False
