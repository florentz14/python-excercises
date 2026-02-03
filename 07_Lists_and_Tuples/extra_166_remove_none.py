# ---------------------------------------------------------------------------
# 166. Remove None from List
# ---------------------------------------------------------------------------
# Descripción: Remove None from List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def remove_none(lst: list) -> list:
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [x for x in lst if x is not None]


sample = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
print(remove_none(sample))
