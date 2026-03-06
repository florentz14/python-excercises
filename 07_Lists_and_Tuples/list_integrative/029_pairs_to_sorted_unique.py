# ---------------------------------------------------------------------------
# 45. Convert Pairs to Sorted Unique Array
# ---------------------------------------------------------------------------
# Descripción: Convert Pairs to Sorted Unique Array
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def pairs_to_sorted_unique(pairs: list[tuple]) -> list:
    return sorted(set(x for p in pairs for x in p))


print(pairs_to_sorted_unique([(1, 2), (3, 1), (2, 4)]))  # [1, 2, 3, 4]
