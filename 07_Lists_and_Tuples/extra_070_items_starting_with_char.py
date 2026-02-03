# ---------------------------------------------------------------------------
# 70. Find Items Starting with Specific Character
# ---------------------------------------------------------------------------
# Descripción: Find Items Starting with Specific Character
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def items_starting_with(lst: list[str], char: str) -> list[str]:
    # Lista por comprensión: se incluyen solo los elementos que cumplen la condición.
    return [s for s in lst if s.startswith(char)]


sample = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'dagfa', 'acjd']
print("Start with 'a':", items_starting_with(sample, 'a'))
print("Start with 'd':", items_starting_with(sample, 'd'))
