# ---------------------------------------------------------------------------
# 77. Decode Run-Length Encoded List
# ---------------------------------------------------------------------------
# Descripción: Decode Run-Length Encoded List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def decode_rle(encoded: list) -> list:
    result = []
    for x in encoded:
        if isinstance(x, list):
            count, val = x[0], x[1]
            # Si es lista se aplana recursivamente; si no, se añade el elemento.
            result.extend([val] * count)
        else:
            result.append(x)
    return result


print(decode_rle([[2, 1], 2, 3, [2, 4], 5, 1]))  # [1, 1, 2, 3, 4, 4, 5, 1]
