# ---------------------------------------------------------------------------
# 222. Difference Between Lists After Applying Function to Each Element
# ---------------------------------------------------------------------------
# Descripción: Difference Between Lists After Applying Function to Each Element
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def difference_by_func(a: list, b: list, func) -> list:
    set_b = {func(x) for x in b}
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [x for x in a if func(x) not in set_b]


# e.g. round: a=[1.2, 2.3], b=[2.4] -> round(2.3)==2 in {2} so keep 1.2
print(difference_by_func([1.2, 2.3, 3.4], [2.2, 3.3], round))  # [1.2]
