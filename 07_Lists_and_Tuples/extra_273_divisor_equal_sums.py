# ---------------------------------------------------------------------------
# 273. Find Element That Divides List into Two Parts with Equal Sum
# ---------------------------------------------------------------------------
# Descripción: Find Element That Divides List into Two Parts with Equal Sum
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def equal_sum_divider(lst: list[int]) -> int | str:
    """Return element at index i where sum(lst[:i]) == sum(lst[i+1:])."""
    for i in range(len(lst)):
        if sum(lst[:i]) == sum(lst[i + 1:]):
            return lst[i]
    return "No such element!"


print(equal_sum_divider([0, 9, 2, 4, 5, 6]))   # 4 (0+9+2 = 11, 5+6 = 11)
print(equal_sum_divider([-4, 0, 6, 1, 0, 2]))  # 1
print(equal_sum_divider([1, 2, 3, 4]))         # No such element!
print(equal_sum_divider([-4, 0, 5, 1, 0, 1]))  # 1
