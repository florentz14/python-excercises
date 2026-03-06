# ---------------------------------------------------------------------------
# 28. Find Second Largest Number in List
# ---------------------------------------------------------------------------
# Descripción: Find Second Largest Number in List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def second_largest(lst: list[int | float]) -> int | float:
    uniq = sorted(set(lst), reverse=True)
    # Se devuelve un valor u otro según la condición.
    return uniq[1] if len(uniq) > 1 else uniq[0]


print(second_largest([1, 2, 3, 4, 5]))  # 4
