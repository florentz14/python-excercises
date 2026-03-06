# ---------------------------------------------------------------------------
# 141. Remove Empty Lists from Nested List
# ---------------------------------------------------------------------------
# Descripción: Remove Empty Lists from Nested List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def remove_empty_lists(lst: list) -> list:
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [x for x in lst if x != []]


sample = [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
print(remove_empty_lists(sample))
