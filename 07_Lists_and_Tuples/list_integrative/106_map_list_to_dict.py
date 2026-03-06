# ---------------------------------------------------------------------------
# 220. Map List to Dict: key=original value, value=function(value)
# ---------------------------------------------------------------------------
# Descripción: Map List to Dict: key=original value, value=function(value)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def map_to_dict(lst: list, func) -> dict:
    return {x: func(x) for x in lst}


print(map_to_dict([1, 2, 3], lambda x: x ** 2))  # {1: 1, 2: 4, 3: 9}
