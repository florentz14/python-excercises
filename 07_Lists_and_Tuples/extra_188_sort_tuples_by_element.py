# ---------------------------------------------------------------------------
# 188. Sort List of Tuples by Specified Element (1-based index)
# ---------------------------------------------------------------------------
# Descripción: Sort List of Tuples by Specified Element (1-based index)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def sort_tuples_by(tuples: list[tuple], index: int) -> list[tuple]:
    """index 1 = first element, 2 = second, etc."""
    # Se devuelve un valor u otro según la condición.
    return sorted(tuples, key=lambda t: t[index - 1] if len(t) >= index else t)


sample = [('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]
print(sort_tuples_by(sample, 1))  # by name
print(sort_tuples_by(sample, 2))  # by number
print(sort_tuples_by(sample, 3))  # by float
