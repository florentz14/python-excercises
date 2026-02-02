# ---------------------------------------------------------------------------
# 7. Remove Duplicates from List
# ---------------------------------------------------------------------------
# Descripción: Elimina elementos duplicados de una lista manteniendo el
#              orden de la primera aparición de cada valor.
# Entrada: Lista (cualquier tipo de elementos).
# Salida: Lista sin duplicados, mismo orden.
# ---------------------------------------------------------------------------

def remove_duplicates(lst: list) -> list:
    # Conjunto para recordar qué elementos ya hemos visto
    seen = set()
    # Lista por comprensión: añadimos x solo si no estaba en seen.
    # "seen.add(x)" se ejecuta al evaluar; add() devuelve None, así que
    # "x in seen or seen.add(x)" es True si ya estaba, o añade y devuelve None (falsy)
    return [x for x in lst if not (x in seen or seen.add(x))]


# Alternativa: dict.fromkeys(lst) mantiene orden (Python 3.7+) y las claves son únicas
def remove_duplicates_alt(lst: list) -> list:
    # fromkeys crea un dict con claves = elementos de lst (sin duplicados)
    # list() convierte las claves de vuelta en lista
    return list(dict.fromkeys(lst))


# --- Ejemplo de uso ---
sample = [1, 2, 2, 3, 4, 3, 5]
print(remove_duplicates(sample))  # [1, 2, 3, 4, 5]
