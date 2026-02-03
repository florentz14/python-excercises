# ---------------------------------------------------------------------------
# 163. Index of First Element Greater Than Specified Value
# ---------------------------------------------------------------------------
# Descripción: Index of First Element Greater Than Specified Value
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def first_index_greater_than(lst: list[int | float], x: int | float) -> int:
    for i, v in enumerate(lst):
        if v > x:
            return i
    return -1


sample = [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]
print(first_index_greater_than(sample, 73))  # 4
print(first_index_greater_than(sample, 55))  # 3
