# ---------------------------------------------------------------------------
# 137. Find First Even and First Odd Number in List
# ---------------------------------------------------------------------------
# Descripción: Find First Even and First Odd Number in List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def first_even_odd(lst: list[int]) -> tuple[int | None, int | None]:
    first_even = next((x for x in lst if x % 2 == 0), None)
    first_odd = next((x for x in lst if x % 2 != 0), None)
    return first_even, first_odd


sample = [1, 3, 5, 7, 4, 1, 6, 8]
print(first_even_odd(sample))  # (4, 1)
