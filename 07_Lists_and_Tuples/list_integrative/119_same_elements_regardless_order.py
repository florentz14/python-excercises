# ---------------------------------------------------------------------------
# 257. Check If Two Lists Have Same Elements (Regardless of Order)
# ---------------------------------------------------------------------------
# Descripción: Check If Two Lists Have Same Elements (Regardless of Order)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def same_elements(a: list, b: list) -> bool:
    # Se devuelve la cantidad de elementos.
    return len(a) == len(b) and set(a) == set(b)


print(same_elements([1, 2, 4], [2, 4, 1]))  # True
print(same_elements([1, 2, 3], [1, 2, 4]))  # False
