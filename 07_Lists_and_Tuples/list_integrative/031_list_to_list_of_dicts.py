# ---------------------------------------------------------------------------
# 49. Convert Two Lists to List of Dictionaries
# ---------------------------------------------------------------------------
# Descripción: Convert Two Lists to List of Dictionaries
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def lists_to_dicts(keys: list, values: list, key_name: str = 'key', val_name: str = 'value') -> list[dict]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [{key_name: k, val_name: v} for k, v in zip(keys, values)]


names = ["Black", "Red", "Maroon", "Yellow"]
codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]
result = [{'color_name': n, 'color_code': c} for n, c in zip(names, codes)]
print(result)
