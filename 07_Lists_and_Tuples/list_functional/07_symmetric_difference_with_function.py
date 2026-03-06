# ---------------------------------------------------------------------------
# 227. Symmetric Difference After Applying Function
# ---------------------------------------------------------------------------
# Descripción: Symmetric Difference After Applying Function
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def symmetric_diff_by_func(a: list, b: list, func) -> list:
    set_a = {func(x) for x in a}
    set_b = {func(x) for x in b}
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [x for x in a if func(x) not in set_b] + [x for x in b if func(x) not in set_a]


print(symmetric_diff_by_func([1.2, 2.3], [2.2, 3.4], round))  # [1.2, 3.4]
