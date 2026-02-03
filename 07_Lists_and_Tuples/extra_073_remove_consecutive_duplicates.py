# ---------------------------------------------------------------------------
# 73. Remove Consecutive Duplicates
# ---------------------------------------------------------------------------
# Descripción: Remove Consecutive Duplicates
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def remove_consecutive_duplicates(lst: list) -> list:
    result = []
    for x in lst:
        if not result or result[-1] != x:
            # Solo se añade si es el primer elemento o si es distinto al último (sin duplicados consecutivos).
            result.append(x)
    return result


sample = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
print(remove_consecutive_duplicates(sample))
