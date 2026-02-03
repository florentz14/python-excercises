# ---------------------------------------------------------------------------
# 214. Sort Digits of Number Ascending/Descending
# ---------------------------------------------------------------------------
# Descripción: Sort Digits of Number Ascending/Descending
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def sort_digits(n: int, descending: bool = True) -> int:
    s = ''.join(sorted(str(abs(n)), reverse=descending))
    # Se devuelve un valor u otro según la condición.
    return int(s) if n >= 0 else -int(s)


n = 134543
print("Descending:", sort_digits(n, True))   # 544331
print("Ascending:", sort_digits(n, False))  # 133445
