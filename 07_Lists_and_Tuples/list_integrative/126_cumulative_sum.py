# ---------------------------------------------------------------------------
# 267. Cumulative Sum of List
# ---------------------------------------------------------------------------
# Descripción: Cumulative Sum of List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def cumulative_sum(lst: list[int | float]) -> list[int | float]:
    result = []
    total = 0
    for x in lst:
        total += x
        result.append(total)
    return result


print(cumulative_sum([1, 2, 3, 4]))      # [1, 3, 6, 10]
print(cumulative_sum([-1, -2, -3, 4]))   # [-1, -3, -6, -2]
