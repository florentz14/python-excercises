# ---------------------------------------------------------------------------
# 275. Sum of List Excluding Each Index (return list of sums)
# ---------------------------------------------------------------------------
# Descripción: Sum of List Excluding Each Index (return list of sums)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def sum_excluding_each(lst: list[int]) -> list[int]:
    total = sum(lst)
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [total - lst[i] for i in range(len(lst))]


print(sum_excluding_each([0, 9, 2, 4, 5, 6]))  # [26, 17, 24, 22, 21, 20]
print(sum_excluding_each([-4, 0, 6, 1, 0, 2]))  # [9, 5, -1, 4, 5, 3]
