# ---------------------------------------------------------------------------
# 67. Find All Values in List Greater Than Specified Number
# ---------------------------------------------------------------------------
# Descripción: Find All Values in List Greater Than Specified Number
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def greater_than(lst: list[int | float], n: int | float) -> list:
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [x for x in lst if x > n]


print(greater_than([1, 5, 3, 8, 2, 9], 4))  # [5, 8, 9]
