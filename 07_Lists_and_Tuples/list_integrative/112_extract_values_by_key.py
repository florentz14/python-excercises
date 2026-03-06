# ---------------------------------------------------------------------------
# 237. Extract Values by Key from List of Dicts
# ---------------------------------------------------------------------------
# Descripción: Extract Values by Key from List of Dicts
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def extract_by_key(lst: list[dict], key) -> list:
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [d[key] for d in lst if key in d]


sample = [{'a': 1, 'b': 8}, {'a': 2, 'b': 36}, {'a': 3, 'b': 34}]
print(extract_by_key(sample, 'b'))  # [8, 36, 34]
