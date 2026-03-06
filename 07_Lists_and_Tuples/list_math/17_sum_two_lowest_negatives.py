# ---------------------------------------------------------------------------
# 213. Sum of Two Lowest Negative Numbers
# ---------------------------------------------------------------------------
# Descripción: Sum of Two Lowest Negative Numbers
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def sum_two_lowest_negatives(lst: list[int]) -> int | None:
    negatives = sorted([x for x in lst if x < 0])
    if len(negatives) < 2:
        return None
    return negatives[0] + negatives[1]


print(sum_two_lowest_negatives([-14, 15, -10, -11, -12, -13, 16, 17]))  # -27
print(sum_two_lowest_negatives([-4, 5, -2, 0, 3, -1, 4, 9]))  # -6
