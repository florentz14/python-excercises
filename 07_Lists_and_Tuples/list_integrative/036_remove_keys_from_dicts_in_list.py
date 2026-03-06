# ---------------------------------------------------------------------------
# 55. Remove Key-Value Pairs from List of Dictionaries
# ---------------------------------------------------------------------------
# Descripción: Remove Key-Value Pairs from List of Dictionaries
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def remove_keys_from_dicts(lst: list[dict], keys_to_remove: list) -> list[dict]:
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [{k: v for k, v in d.items() if k not in keys_to_remove} for d in lst]


sample = [{'a': 1, 'b': 2, 'c': 3}, {'a': 10, 'b': 20}]
print(remove_keys_from_dicts(sample, ['b']))  # [{'a': 1, 'c': 3}, {'a': 10}]
