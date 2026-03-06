# ---------------------------------------------------------------------------
# 102. Extract Strings of Specified Length from List
# ---------------------------------------------------------------------------
# Descripción: Extract Strings of Specified Length from List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def strings_of_length(lst: list[str], n: int) -> list[str]:
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [s for s in lst if len(s) == n]


sample = ['Python', 'list', 'exercises', 'practice', 'solution']
print(strings_of_length(sample, 8))  # ['practice', 'solution']
