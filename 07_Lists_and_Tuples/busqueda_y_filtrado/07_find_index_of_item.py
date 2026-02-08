# ---------------------------------------------------------------------------
# 22. Find Index of an Item in a List
# ---------------------------------------------------------------------------
# Descripción: Find Index of an Item in a List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def find_index(lst: list, item) -> int:
    # Se devuelve un valor u otro según la condición.
    return lst.index(item) if item in lst else -1


# Or use lst.index(item) directly
sample = [10, 20, 30, 40]
print(sample.index(30))  # 2
