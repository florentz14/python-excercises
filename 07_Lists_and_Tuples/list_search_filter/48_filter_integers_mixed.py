# ---------------------------------------------------------------------------
# 212. Filter Integers from Mixed List (keep only int, not float)
# ---------------------------------------------------------------------------
# Descripción: Filter Integers from Mixed List (keep only int, not float)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def filter_integers(lst: list) -> list[int]:
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [x for x in lst if isinstance(x, int) and not isinstance(x, bool)]


sample = [34.67, 12, -94.89, 'Python', 0, 'C#']
print(filter_integers(sample))  # [12, 0]
