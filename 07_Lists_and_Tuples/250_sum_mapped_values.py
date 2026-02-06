# ---------------------------------------------------------------------------
# 250. Sum After Mapping
# ---------------------------------------------------------------------------
# Descripción: Sum After Mapping
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def sum_after_map(lst: list, func) -> int | float:
    # Se devuelve la suma de todos los elementos.
    return sum(func(x) for x in lst)


print(sum_after_map([1, 2, 3, 4], lambda x: x * 2))  # 20
