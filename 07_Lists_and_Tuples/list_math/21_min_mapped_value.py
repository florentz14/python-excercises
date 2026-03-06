# ---------------------------------------------------------------------------
# 249. Min Value After Mapping
# ---------------------------------------------------------------------------
# Descripción: Min Value After Mapping
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def min_after_map(lst: list, func) -> int | float:
    return min(func(x) for x in lst)


print(min_after_map([1, 2, 3, 4], lambda x: x * 2))  # 2
