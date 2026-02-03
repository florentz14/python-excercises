# ---------------------------------------------------------------------------
# 72. Flatten Nested List Structure (arbitrary depth)
# ---------------------------------------------------------------------------
# Descripción: Flatten Nested List Structure (arbitrary depth)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def flatten_deep(lst: list) -> list:
    result = []
    for x in lst:
        if isinstance(x, list):
            # Si es lista se aplana recursivamente; si no, se añade el elemento.
            result.extend(flatten_deep(x))
        else:
            result.append(x)
    return result


sample = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
print(flatten_deep(sample))
