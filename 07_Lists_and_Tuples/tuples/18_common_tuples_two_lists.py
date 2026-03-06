# ---------------------------------------------------------------------------
# 207. Common Tuples Between Two Lists
# ---------------------------------------------------------------------------
# Descripción: Common Tuples Between Two Lists
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def common_tuples(a: list[tuple], b: list[tuple]) -> list[tuple]:
    set_b = set(b)
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [t for t in a if t in set_b]


list1 = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
list2 = [('red', 'green'), ('orange', 'pink')]
print(common_tuples(list1, list2))
