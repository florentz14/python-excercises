# ---------------------------------------------------------------------------
# 230. All Indices Where Element Satisfies Function
# ---------------------------------------------------------------------------
# Descripción: All Indices Where Element Satisfies Function
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def all_indices_where(lst: list, predicate) -> list[int]:
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [i for i, x in enumerate(lst) if predicate(x)]


print(all_indices_where([1, 2, 3, 2, 4], lambda x: x == 2))  # [1, 3]
