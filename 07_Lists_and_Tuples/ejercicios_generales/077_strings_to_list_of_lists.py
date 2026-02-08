# ---------------------------------------------------------------------------
# 167. Convert List of Strings to List of Lists (each string -> list of chars)
# ---------------------------------------------------------------------------
# Descripción: Convert List of Strings to List of Lists (each string -> list of ch...
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def strings_to_lists(lst: list[str]) -> list[list[str]]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [list(s) for s in lst]


sample = ['Red', 'Maroon', 'Yellow', 'Olive']
print(strings_to_lists(sample))
