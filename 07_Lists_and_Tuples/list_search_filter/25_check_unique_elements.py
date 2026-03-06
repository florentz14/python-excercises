# ---------------------------------------------------------------------------
# 115. Check If All Elements in List Are Unique
# ---------------------------------------------------------------------------
# Descripción: Check If All Elements in List Are Unique
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def all_unique(lst: list) -> bool:
    # Se devuelve la cantidad de elementos.
    return len(lst) == len(set(lst))


print(all_unique([1, 2, 4, 6, 8]))   # True
print(all_unique([1, 2, 4, 6, 8, 2]))  # False
