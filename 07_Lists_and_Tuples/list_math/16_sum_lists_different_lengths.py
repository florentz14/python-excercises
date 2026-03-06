# ---------------------------------------------------------------------------
# 194. Sum Two or More Lists (Different Lengths) - element-wise, pad with 0
# ---------------------------------------------------------------------------
# Descripción: Sum Two or More Lists (Different Lengths) - element-wise, pad with 0
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def sum_lists(*lists: list[int]) -> list[int]:
    max_len = max(len(L) for L in lists)
    result = [0] * max_len
    for L in lists:
        for i, x in enumerate(L):
            result[i] += x
    return result


print(sum_lists([1, 2, 4], [2, 4, 4], [1, 2]))  # [4, 8, 8]
print(sum_lists([1], [2, 4, 4], [1, 2], [4]))   # [8, 6, 4]
