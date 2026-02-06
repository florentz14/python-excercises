# ---------------------------------------------------------------------------
# 199. Convert Unicode List to List of Strings (ensure str type)
# ---------------------------------------------------------------------------
# Descripción: Convert Unicode List to List of Strings (ensure str type)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def unicode_to_strings(lst: list) -> list[str]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [str(x) for x in lst]


sample = ['S001', 'S002', 'S003', 'S004']
print(unicode_to_strings(sample))
