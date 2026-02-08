# ---------------------------------------------------------------------------
# 206. Remove Additional/Extra Spaces from List (strip each string)
# ---------------------------------------------------------------------------
# Descripción: Remove Additional/Extra Spaces from List (strip each string)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def remove_extra_spaces(lst: list[str]) -> list[str]:
    # Se devuelve un valor u otro según la condición.
    return [s.strip() if isinstance(s, str) else s for s in lst]


sample = ['abc ', ' ', ' ', 'sdfds ', ' ', ' ', 'sdfds ', 'huy']
print(remove_extra_spaces(sample))
