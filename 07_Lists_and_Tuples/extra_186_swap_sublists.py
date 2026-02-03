# ---------------------------------------------------------------------------
# 186. Swap Two Sublists in List (by start indices and lengths)
# ---------------------------------------------------------------------------
# Descripción: Swap Two Sublists in List (by start indices and lengths)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def swap_sublists(lst: list, i1: int, len1: int, i2: int, len2: int) -> list:
    result = lst.copy()
    sub1 = result[i1:i1 + len1]
    sub2 = result[i2:i2 + len2]
    result[i1:i1 + len1] = sub2
    result[i2:i2 + len2] = sub1
    return result


# Sample: swap indices 1-2 with 5-7
sample = list(range(16))
print(swap_sublists(sample, 1, 2, 5, 3))
