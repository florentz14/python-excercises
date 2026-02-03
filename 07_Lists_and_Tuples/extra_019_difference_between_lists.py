# ---------------------------------------------------------------------------
# 19. Calculate Difference Between Two Lists (elements in first not in second)
# ---------------------------------------------------------------------------
# Descripción: Calculate Difference Between Two Lists (elements in first not in se...
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def list_difference(a: list, b: list) -> list:
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [x for x in a if x not in b]


# Or set difference if order doesn't matter
print(list_difference([1, 2, 3, 4], [2, 4]))  # [1, 3]
