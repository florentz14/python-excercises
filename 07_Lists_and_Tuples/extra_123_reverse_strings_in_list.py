# ---------------------------------------------------------------------------
# 123. Reverse Each String in List
# ---------------------------------------------------------------------------
# Descripción: Reverse Each String in List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def reverse_strings(lst: list[str]) -> list[str]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [s[::-1] for s in lst]


sample = ['Red', 'Green', 'Blue', 'White', 'Black']
print(reverse_strings(sample))  # ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
