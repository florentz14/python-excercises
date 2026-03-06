# ---------------------------------------------------------------------------
# 69. Remove Duplicate Sublists (preserve order of first occurrence)
# ---------------------------------------------------------------------------
# Descripción: Remove Duplicate Sublists (preserve order of first occurrence)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def unique_sublists(lst: list[list]) -> list[list]:
    seen = set()
    result = []
    for sub in lst:
        key = tuple(sub)
        if key not in seen:
            seen.add(key)
            result.append(sub)
    return result


sample = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print(unique_sublists(sample))
