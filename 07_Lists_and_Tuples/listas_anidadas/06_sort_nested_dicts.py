# ---------------------------------------------------------------------------
# 50. Sort List of Nested Dictionaries
# ---------------------------------------------------------------------------
# Descripción: Sort List of Nested Dictionaries
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def sort_nested_dicts(lst: list[dict], key: str) -> list[dict]:
    # Se ordena la lista usando key para comparar (p. ej. por longitud o valor).
    return sorted(lst, key=lambda d: d.get(key, 0))


sample = [{'a': 2, 'b': 1}, {'a': 1, 'b': 2}, {'a': 3, 'b': 0}]
print(sort_nested_dicts(sample, 'a'))
