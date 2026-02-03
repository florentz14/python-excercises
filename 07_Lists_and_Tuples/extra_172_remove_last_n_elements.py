# ---------------------------------------------------------------------------
# 172. Remove Last N Elements from List
# ---------------------------------------------------------------------------
# Descripción: Remove Last N Elements from List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def remove_last_n(lst: list, n: int) -> list:
    # Se devuelve un valor u otro según la condición.
    return lst[:-n] if n > 0 else lst[:]


sample = [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
print(remove_last_n(sample, 3))
print(remove_last_n(sample, 5))
