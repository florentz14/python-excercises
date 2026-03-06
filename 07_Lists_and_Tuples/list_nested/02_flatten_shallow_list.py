# ---------------------------------------------------------------------------
# 23. Flatten a Shallow List (one level)
# ---------------------------------------------------------------------------
# Descripción: "Aplana" una lista que contiene listas y otros elementos:
#              cada sublista se reemplaza por sus elementos, el resto se
#              deja igual. Solo un nivel de anidación.
# ---------------------------------------------------------------------------

def flatten_shallow(lst: list) -> list:
    # Lista donde iremos acumulando los elementos ya aplanados
    result = []
    for item in lst:
        # Si el elemento es una lista, añadimos sus elementos (no la lista entera)
        if isinstance(item, list):
            # Si es lista se aplana recursivamente; si no, se añade el elemento.
            result.extend(item)
        else:
            # Si no es lista, lo añadimos tal cual
            result.append(item)
    return result


# --- Ejemplo: [[1,2], [3,4], [5]] -> [1, 2, 3, 4, 5]
sample = [[1, 2], [3, 4], [5]]
print(flatten_shallow(sample))  # [1, 2, 3, 4, 5]
